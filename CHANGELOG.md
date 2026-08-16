# Changelog

本仓库（xhqing）是 GitHub 个人主页仓库，也是 PersonalAssistantAgent（Kit）的子项目。本 CHANGELOG 记录本仓库的变更。

## 1.1.0 - 2026-08-16

### 新增（舰队集中式访问统计 + Profile README 全量信息更新）

- **为什么改**：用户要求（1）为全舰队仓库做「真去重」的访问量统计——图片徽章方案因 GitHub camo 代理隐藏访客 IP/UA 而无法去重，故走官方 Traffic API + 定时落盘路线，集中部署在本仓库、各 fleet 仓库零负担只挂徽章；（2）Profile README 与全局「智能体命名注册表」对齐——此前缺少 Hermes / Anvil / Ada 三个 agent 及「agent 负责的子项目」信息。
- **改了什么**：
  - 新增 `scripts/update_traffic.py`：遍历 18 个 fleet 仓库（15 个 agent 主仓库 + xhqing + CC-BRIDGE / XPilot / AgentCortex 三个子项目），拉取官方 Traffic API 的 14 天滚动数据，按日期差集幂等合并进 `traffic/<repo>.json` 累计值，并生成 shields.io endpoint 徽章（`traffic/badges/<repo>.json`，展示按日去重访客累计）与舰队汇总徽章 `traffic/badges/fleet-total.json`。SiteBuilderAgent、NeuralCoreAgent 尚未推上 GitHub（本地零提交），API 404 自动跳过。
  - 新增 `.github/workflows/traffic.yml`：每日 UTC 02:23 定时运行统计脚本并把数据 commit 回本仓库（`[skip ci]` 防循环）；认证用仓库 secret `FLEET_TRAFFIC_PAT`（classic PAT、repo scope，本机备忘见 `tmp/pat_note.md`，待用户创建并配置后生效）。
  - README.md / README_cn.md：舰队表格补齐 Hermes（NetOpsAgent）、Anvil（BackendEngineerAgent）、Ada（NeuralCoreAgent）三行；新增「Agent-owned subprojects / Agent 负责的子项目」表格（Kit→xhqing、Anvil→CC-BRIDGE、Hermes→XPilot、Ada→AgentCortex）；新增舰队汇总访问量徽章；流水线说明后补一段独立 agent 协作关系（Markowitz→Victor 加权信号、Hermes 供网、Ada 推理引擎、Anvil 后端、Tinker 补丁、Prometheus 能力底座）。
  - 新增本 CHANGELOG 与 `VERSION`（1.1.0）——本仓库首次引入项目标配两件套。
- **语义边界（徽章数字怎么读）**：徽章展示的是「各仓库按日去重访客数的累计和」——GitHub 只提供每日 uniques，跨天不去重（同一人多天访问会计多次）；且跨仓库不去重（同一人访问多个仓库会在多个仓库各计一次）。累计自 2026-08-01（UTC）起：首次采集时 API 返回了整个 14 天窗口，窗口内历史数据已全部回补落盘；2026-08-01 之前的访问量超出 API 窗口、不可追溯。API 的 14 天窗口随后续运行向前滚动（旧日期逐渐移出 API 响应），但落盘数据只增不删，已记录的日期永久保留，累计起点固定为 2026-08-01、不随窗口漂移。

### 变更（舰队汇总访问量徽章并入顶部徽章行，说明文字单独成行）

- **为什么改**：徽章原本单独放在「Flagship Project / 旗舰项目」段落中间、且说明文字与徽章挤在同一行渲染，位置突兀、排版松散；用户要求把它与其他徽章放在一起、说明文字单独起一行。
- **改了什么**：README.md / README_cn.md——fleet 徽章（`traffic/badges/fleet-total.json` endpoint）移到顶部徽章行（followers · Sponsor · Profile views 之后，以 `&nbsp;` 间隔同行排列），说明文字经 `<br/>` 换行后以 `<sub>` 小字单独成行；原「旗舰项目」段内的独立徽章块整块移除。

### 变更（徽章口径从「累计」改为「滚动 14 天日均」，舰队表格加「日均访问」列）

- **为什么改**：用户要求看「每个仓库最近的平均访问量」而非历史累计——累计值随时间单调增长、不能反映近期热度；口径定义为「滚动 14 天 API 窗口内按日去重访客的日均值」（零访问日也计入分母，若每天只有本人访问则均值恰为 1），fleet 徽章 = 各仓库日均之和。同时要求在 Profile README 的舰队表格里能直接看出每个仓库的日均值。
- **改了什么**：
  - [`scripts/update_traffic.py`](scripts/update_traffic.py)：`merge()` 在窗口数据基础上计算 `avg14`（当前 API 窗口 uniques 总和 ÷ 窗口天数，含零访问日）存入 `traffic/<repo>.json`；单仓库徽章 label 从 `visitors`（累计）改为 `visits/day`（日均）；fleet 徽章从 `fleet visitors`（累计和）改为 `fleet visits/day`（各仓库**精确值**先求和再格式化，避免逐仓四舍五入的累计误差）；`.meta.json` 同步记录 `avg14`。日均随窗口滚动反映近期流量，历史日明细与累计 totals 仍完整保留在 stats JSON 中。
  - README.md / README_cn.md：舰队表格新增第四列「Visits/day / 日均访问」，每行内嵌该仓库的 `visits/day` endpoint 徽章（Mason / Ada 对应仓库尚未推上 GitHub、无数据，暂以「—」占位，仓库上线后由脚本自动生成徽章、届时补上）；顶部 fleet 徽章说明文字同步改为日均口径。
- **验证**：本地重跑实测——各仓库 avg14 手算之和 4.570 与 fleet 徽章 4.6 一致（先求和后取一位小数）；DayTradingAgent 17 uniques ÷ 14 天 = 1.214 → 徽章「1.2」；连续重跑两次 diff 不变，幂等保持。

### 变更（采集合并逻辑修复：日内快照更新制，冻结首个快照的漏计缺陷 + action 版本升级）

- **为什么改**：首跑验证（workflow 手动触发成功）后复查发现原「日期差集合并」的设计缺陷——Traffic API 返回的是**当天实时累计快照**，某天的数字会持续增长到当天结束；原逻辑「已存在的日期跳过」会把每个日期**第一次被采到时的部分数字冻结**（每日 cron 在 UTC 02:23 跑，等于只记每天头 2 小时的访问量，之后约九成流量漏计）。
- **改了什么**：
  - [`scripts/update_traffic.py`](scripts/update_traffic.py)：合并逻辑从「日期差集、旧日期跳过」改为「**日内快照更新制**」——已存在的日期用 API 最新快照覆盖（日内数字只增不减，更新即纠正），totals 从整个日期表全量重算；数据未变时不产生 diff，幂等性保持（已实测重跑 no diff）。每日一跑足以完整计账：次日的运行会把前一天的最终数字补齐（前一天仍在 14 天窗口内）。脚本头部 docstring 同步说明合并语义。
  - [`.github/workflows/traffic.yml`](.github/workflows/traffic.yml)：`actions/checkout` v4→v5、`actions/setup-python` v5→v6（消除首跑日志里 Node.js 20 弃用警告）。
- **验证**：本地重跑 totals 正确重算（xhqing 11/3、DayTradingAgent 53/17 与修复前一致——当前数据碰巧无变化，逻辑正确性以「日内增长会被更新」为准）；连续两次运行输出无 diff，幂等确认。

## Unreleased

### 变更（措辞全面换向「团队 / AI Agent」+ 徽章体系重构：删 fleet 汇总徽章、Profile 与各仓徽章改「近半月去重日均（不含本人）」口径）

- **为什么改**：用户 2026-08-16 逐条提出 Profile README 措辞与徽章口径的一系列修改——（1）「舰队」改「团队」（英文 fleet → team 同步），表达「打造智能体团队」；（2）主标题「开源数字产品变现系统」改「开源智能体团队能力」；（3）简介行改为「机器学习 · 数据科学 · 量化交易 · 智能体交易 · 数字产品 · 区块链」六项并列；（4）凡涉及智能体的英文表达统一特指「AI Agent」；（5）删 fleet 汇总徽章（`fleet-total.json`）及其说明文字；（6）Profile views 徽章从 komarev 第三方计数图片换成本仓库自建 endpoint 徽章，口径为「近半月（滚动 14 天窗口）按日去重访客的日均值、不含仓库所有者本人的访问」——大于 0 即代表近半月有其他人访问；（7）各仓库的日均访问徽章同用该口径（Traffic API 统计本身即此口径，见下）。
- **改了什么**：
  - README.md / README_cn.md：主标题、简介行、旗舰项目段（舰队→团队、agent→AI Agents）、表格表头与独立段标题（Agent→AI Agent、Standalone agents→Standalone AI Agents）、子项目段（Agent→AI Agent）、协作段整句改写（「流水线之外，其它智能体都有各自的负责领域：Markowitz 开发量化策略；Hermes 负责网络问题；……」）；Victor 角色去掉「（HK / US）」、Hermes 去掉「（代理选路与故障转移）」、Ada 去掉「（推理引擎）」括号注；「Prompt 包」大写、产品与渠道两处枚举加「等」；页脚「关注舰队 / Watch the fleets grow」→「团队 / the team grow」；顶部徽章行删 fleet 汇总徽章与说明行、komarev Profile views 换为 `traffic/badges/profile.json` endpoint 徽章（alt「Profile Visits/day」）。
  - [`scripts/update_traffic.py`](scripts/update_traffic.py)：删除 fleet 汇总徽章生成逻辑（fleet_views / fleet_uniques / fleet_avg 累计与 `fleet-total.json` 写出）；新增 profile 徽章——采集 xhqing 主页仓库时同步写出 `traffic/badges/profile.json`（label「Profile Visits/day」、message 取该仓 avg14）；docstring 措辞 fleet→team 并写明徽章语义（Traffic API 在所有者登录状态下已排除其本人访问；未登录的自访可能混入，API 不提供访客身份、无法事后剔除——这是口径的边界，如实记录）。
  - `traffic/badges/`：删 `fleet-total.json`；新增 `profile.json`（当前 message「0.2」，= 近 14 天 3 个去重访客 ÷ 14 天，由既有 `traffic/xhqing.json` 实算）。各仓单库徽章（label「Visits/day」）机制不变——其口径本就是「滚动 14 天窗口按日去重、且 Traffic API 天然不含所有者登录态访问」，与用户新定口径一致，无需改数。
- **语义边界（「去掉我自己的访问」怎么落实）**：GitHub Traffic API 不提供访客身份，无法在数据侧事后剔除本人访问；但官方口径是**所有者登录状态下的自身访问不计入统计**（见 GitHub Community Discussion #23048 / #194224）。因此徽章数字采信 API 原值即已「默认不含本人（登录态）」；唯一的残余偏差是所有者未登录（如隐身窗口）访问自己仓库会被计入且无法甄别——该边界已写入脚本 docstring，属已知且接受。
- **回归检查**：与 1.1.0「徽章口径从累计改为日均」「日内快照更新制」两条改动正交——本次只动徽章的**呈现层**（哪些徽章存在、label 文字、README 引用），采集、合并、日均计算逻辑均未动；删 fleet 徽章不影响各仓数据文件与单仓徽章的生成。

### 变更（徽章英文首字母大写规定落地：badge label 与 alt 文本统一大写；Visitors 徽章命名全局统一）

- **为什么改**：用户立规（2026-08-16）——README 徽章上的英文小写首字母（`visits/day`、`fleet visits/day`、`license-MIT` 等）观感不一致、显得随意，与 fleet 统一的专业视觉风格不符；首字母大写是英文标识词的标准书写规范。规定写入全局 `~/.claude/CLAUDE.md`（CapabilityManagerAgent 镜像同步），本仓库作为集中统计的数据源侧同步落地存量修正。随后用户进一步要求「Visitors 徽章全局统一、首字母大写」——`Visits/day` 作为徽章 label 术语在所有出现处（含 fleet 徽章的次词）统一大写，README 的 alt 与说明文字与 JSON label 对齐。
- **改了什么**：
  - [`scripts/update_traffic.py`](scripts/update_traffic.py)：单仓库徽章 label `visits/day` → `Visits/day`；fleet 徽章 label `fleet visits/day` → `Fleet Visits/day`（次词 `visits` 同步大写，与 README alt「Fleet Visits/day」对齐；后续每日采集自动按新 label 生成，无需再改）。
  - `traffic/badges/*.json`：16 个单仓库徽章 + 1 个 fleet 徽章的 `label` 字段同步改为首字母大写（`Visits/day` / `Fleet Visits/day`），`message` 数字不变。
  - README.md / README_cn.md：fleet 徽章 `alt="fleet visits/day"` → `alt="Fleet Visits/day"`；舰队表格各行 `alt="visitors"` → `alt="Visitors"`、英文版行内 alt `"<Name> visits/day"` → `"<Name> Visits/day"`；`<sub>` 说明文字起头 `fleet visits/day` → `Fleet Visits/day`；komarev Profile views 徽章 `alt="views"` → `alt="Profile views"`（与 URL 里 label 参数对齐，顺手统一）。
- **回归检查**：与 1.1.0「徽章口径从累计改为日均」改动正交（本次只改文字大小写，口径、数字、URL 均不变）；各 fleet 仓库 README 的 `alt="visitors"` → `alt="Visitors"` 修正由各仓库自行记录，不在此重复。

### 变更（Visitors 徽章命名全局统一：各 fleet 仓库 README alt 首字母大写）

- **为什么改**：承接上条「首字母大写」规定与用户「Visitors 徽章全局统一、首字母大写」指令——集中统计上线时各 fleet 仓库 README 挂的访问量徽章 alt 写的是小写 `visitors`，与 badge JSON label `Visits/day` 及大写规范不一致，需一次收口。
- **改了什么**：16 个仓库的 README / README_cn（存在的版本）里 `alt="visitors"` 统一改为 `alt="Visitors"`（各仓库自行记 CHANGELOG；本条只记数据源侧的发起与核对）。
- **验证**：`grep -rn 'alt="visitors"' */README*.md` 已无残留（SiteBuilderAgent、NeuralCoreAgent 尚未挂徽章，上线时直接按 `alt="Visitors"` 挂）。

### 变更（README 顶部简介行换向：突出量化与智能体方向）

- **为什么改**：用户方向重心已从「联邦学习 / 隐私 / 统计 / Python」这类学术背景标签，转向「量化交易 + 智能体应用 + 数字产品」的实战方向（对应舰队里的 Victor / Markowitz 交易线与销售流水线），要求同步改掉 Profile README 顶部的这行简介。
- **改了什么**：README.md / README_cn.md 第 9 行简介行——去掉「联邦学习 · 隐私 / 统计 / Python（Federated Learning · Privacy · Statistics · Python）」，保留「机器学习 / 数据科学（ML · Data Science）」，新增「量化交易 / 智能体应用 / 智能体交易 / 数字产品（Quant Trading · AI Agent Apps · Agent Trading · Digital Products）」，仍按「背景领域 | 当前方向」两组以竖线分隔。

### 变更（英文简介行「AI Agent Apps · Agent Trading」改为「AI Agents · Agentic Trading」）

- **为什么改**：用户指出「Apps」一词会误导读者以为是手机 app 或 GUI 桌面软件——而 fleet 里全是 CLI agent、规则集、框架，无一 GUI 产物，语义与实际不符；且「Agent Trading」的说法不够地道。中文版「智能体应用 · 智能体交易」按用户要求保持不动。
- **改了什么**：README.md 第 9 行简介行——「AI Agent Apps · Agent Trading」→「AI Agents · Agentic Trading」，消除 Apps 歧义并采用更地道的「Agentic Trading」表述。

### 变更（「AI agent」统一为「AI Agent」）

- **为什么改**：两个 README 里同一术语大小写混用（副标题、旗舰项目段、赞助段共 5 处小写「AI agent / AI agents」，而表格与协作段用大写「AI Agent」），用户要求全仓统一为大写「AI Agent」。
- **改了什么**：README.md / README_cn.md 共 5 处「AI agent(s)」→「AI Agent(s)」——README_cn.md 第 7、123 行；README.md 第 7、25、123 行。全仓 grep 验证已无小写残留。

