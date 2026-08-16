#!/usr/bin/env python3
"""Team-wide GitHub traffic collector (centralized, runs in xhqing repo).

Pulls the 14-day rolling view/unique-visitor stats of every team repo via the
official Traffic API, merges them into per-repo cumulative JSON, and emits
shields.io endpoint badges. Idempotent: re-runs never double-count.

Badge semantics: each repo badge shows the repo's AVERAGE DAILY unique
visitors over the rolling 14-day API window (in-day dedup; days with zero
visits count in the divisor, so a repo visited by one person every day
averages exactly 1). A value above 0 means someone OTHER than the repo owner
visited in the last half month — GitHub's Traffic API already excludes the
owner's own views while logged in (logged-out self-visits may still slip in,
as the API exposes no visitor identity to filter after the fact). Badge
labels are "Visitors" (per repo) and "Profile Visitors" (profile).

Merge semantics: GitHub returns the latest snapshot for each day in the
window — a day's figures keep growing until that day ends, so an already
recorded day is UPDATED to the API's newer numbers (not skipped), and totals
are recomputed from the full day map. A single daily run is enough: the next
day's run finalizes yesterday's numbers while that day is still inside the
14-day window.

Data layout:
  traffic/<repo>.json          per-repo cumulative stats (days + totals + avg14)
  traffic/badges/<repo>.json   shields.io endpoint badge (daily average) for README embedding
  traffic/badges/profile.json  profile badge (xhqing repo daily average) for the profile README
"""

import json
import os
import sys
import urllib.error
import urllib.request

API = 'https://api.github.com'
# Team roster: every repo owned by xhqing that belongs to the AI Agent team.
TEAM = [
    'xhqing',                    # this profile repo (Kit's subproject)
    'ProductStrategistAgent',    # Scout
    'ProductProducerAgent',      # Wright
    'SiteBuilderAgent',          # Mason
    'GrowthMarketerAgent',       # Buzz
    'DigiVendAgent',             # Vendy
    'DataAnalystAgent',          # Echo
    'PersonalAssistantAgent',    # Kit
    'DayTradingAgent',           # Victor
    'PatchClaudeAgent',          # Tinker
    'CapabilityManagerAgent',    # Prometheus
    'QuantStrategistAgent',      # Markowitz
    'NetOpsAgent',               # Hermes
    'BackendEngineerAgent',      # Anvil
    'NeuralCoreAgent',           # Ada
    'CC-BRIDGE',                 # Anvil's subproject
    'XPilot',                    # Hermes' subproject
    'AgentCortex',               # Ada's subproject
]


def gh(path, token):
    req = urllib.request.Request(
        f'{API}{path}',
        headers={
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.github+json',
        })
    return json.load(urllib.request.urlopen(req))


def collect(repo, token):
    """Fetch the 14-day traffic window; return {date: {views, uniques}}."""
    try:
        data = gh(f'/repos/xhqing/{repo}/traffic/views', token)
    except urllib.error.HTTPError as e:
        print(f'  WARN {repo}: traffic API {e.code} — skipped', file=sys.stderr)
        return None
    return {d['timestamp'][:10]: {'views': d['count'], 'uniques': d['uniques']}
            for d in data.get('views', [])}


def fmt_avg(v):
    """Format a daily average as a compact number: 1, 1.2, 0.8 — no trailing 0."""
    s = f'{v:.1f}'.rstrip('0').rstrip('.')
    return s if s else '0'


def merge(stats, new_days):
    """Merge the API day-snapshot into cumulative stats.

    An existing day is updated to the API's latest numbers (they only grow
    within a day), then totals are recomputed from the whole day map — so a
    day is never frozen at its first partial capture, and reruns with
    unchanged data still produce no diff.

    avg14 is the rolling daily average over the CURRENT API window (zero-visit
    days included in the divisor), recomputed from new_days each run — it
    reflects recent traffic, not the all-time history in stats['days'].
    """
    changed = False
    for day, row in new_days.items():
        if stats['days'].get(day) != row:
            stats['days'][day] = row
            changed = True
    if new_days:
        avg = sum(d['uniques'] for d in new_days.values()) / len(new_days)
        if abs(stats.get('avg14', -1) - avg) > 1e-9:
            stats['avg14'] = avg
            changed = True
    if changed:
        stats['total_views'] = sum(d['views'] for d in stats['days'].values())
        stats['total_uniques'] = sum(d['uniques'] for d in stats['days'].values())
    return changed


def write_badge(repo, stats):
    os.makedirs('traffic/badges', exist_ok=True)
    badge = {
        'schemaVersion': 1,
        'label': 'Visitors',
        'message': fmt_avg(stats.get('avg14', 0)),
        'color': 'brightgreen',
    }
    with open(f'traffic/badges/{repo}.json', 'w') as f:
        json.dump(badge, f, indent=2)
    # totals kept in a side file so badges stay single-number while the
    # full data remains queryable in the stats JSON
    with open(f'traffic/badges/{repo}.meta.json', 'w') as f:
        json.dump({'total_views': stats['total_views'],
                   'total_uniques': stats['total_uniques'],
                   'avg14': round(stats.get('avg14', 0), 3)}, f, indent=2)


def main():
    token = os.environ['GH_TOKEN']
    os.makedirs('traffic', exist_ok=True)
    for repo in TEAM:
        print(f'collecting {repo} ...')
        days = collect(repo, token)
        if days is None:
            continue
        path = f'traffic/{repo}.json'
        try:
            with open(path) as f:
                stats = json.load(f)
        except FileNotFoundError:
            stats = {'days': {}, 'total_views': 0, 'total_uniques': 0}
        if merge(stats, days):
            with open(path, 'w') as f:
                json.dump(stats, f, indent=2, sort_keys=True)
        write_badge(repo, stats)
        if repo == 'xhqing':
            # profile badge: the xhqing repo's daily average, labelled for the
            # profile README (owner-logged-in views already excluded by GitHub)
            with open('traffic/badges/profile.json', 'w') as f:
                json.dump({'schemaVersion': 1, 'label': 'Profile Visitors',
                           'message': fmt_avg(stats.get('avg14', 0)),
                           'color': 'brightgreen'}, f, indent=2)
    print('done.')


if __name__ == '__main__':
    main()
