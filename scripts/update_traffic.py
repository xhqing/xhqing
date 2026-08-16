#!/usr/bin/env python3
"""Fleet-wide GitHub traffic collector (centralized, runs in xhqing repo).

Pulls the 14-day rolling view/unique-visitor stats of every fleet repo via the
official Traffic API, merges them by date-diff into per-repo cumulative JSON,
and emits shields.io endpoint badges. Idempotent: re-runs never double-count.

Data layout:
  traffic/<owner>__<repo>.json   per-repo cumulative stats (days + totals)
  traffic/badges/<repo>.json     shields.io endpoint badge for README embedding
"""

import json
import os
import sys
import urllib.error
import urllib.request

API = 'https://api.github.com'
# Fleet roster: every repo owned by xhqing that belongs to the agent fleet.
FLEET = [
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


def merge(stats, new_days):
    """Date-diff merge into existing cumulative stats. Idempotent."""
    changed = False
    for day, row in new_days.items():
        if day not in stats['days']:
            stats['days'][day] = row
            stats['total_views'] += row['views']
            stats['total_uniques'] += row['uniques']
            changed = True
    return changed


def write_badge(repo, total_views, total_uniques):
    os.makedirs('traffic/badges', exist_ok=True)
    badge = {
        'schemaVersion': 1,
        'label': 'visitors',
        'message': f'{total_uniques:,}',
        'color': 'brightgreen',
    }
    with open(f'traffic/badges/{repo}.json', 'w') as f:
        json.dump(badge, f, indent=2)
    # total_views kept in a side file so badges stay single-number while the
    # full data remains queryable in the stats JSON
    with open(f'traffic/badges/{repo}.meta.json', 'w') as f:
        json.dump({'total_views': total_views, 'total_uniques': total_uniques},
                  f, indent=2)


def main():
    token = os.environ['GH_TOKEN']
    os.makedirs('traffic', exist_ok=True)
    fleet_views = fleet_uniques = 0
    for repo in FLEET:
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
        write_badge(repo, stats['total_views'], stats['total_uniques'])
        fleet_views += stats['total_views']
        fleet_uniques += stats['total_uniques']
    # fleet-wide totals: sum across repos (one visitor may count in several)
    with open('traffic/badges/fleet-total.json', 'w') as f:
        json.dump({'schemaVersion': 1, 'label': 'fleet visitors',
                   'message': f'{fleet_uniques:,}', 'color': 'blue'}, f, indent=2)
    print('done.')


if __name__ == '__main__':
    main()
