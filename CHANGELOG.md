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
- **语义边界（徽章数字怎么读）**：徽章展示的是「各仓库按日去重访客数的累计和」——GitHub 只提供每日 uniques，跨天不去重（同一人多天访问会计多次）；且跨仓库不去重（同一人访问多个仓库会在多个仓库各计一次）。只能从 2026-08-16 部署之日起累计，之前的访问量不可追溯。

## Unreleased

### 变更（README 顶部简介行换向：突出量化与智能体方向）

- **为什么改**：用户方向重心已从「联邦学习 / 隐私 / 统计 / Python」这类学术背景标签，转向「量化交易 + 智能体应用 + 数字产品」的实战方向（对应舰队里的 Victor / Markowitz 交易线与销售流水线），要求同步改掉 Profile README 顶部的这行简介。
- **改了什么**：README.md / README_cn.md 第 9 行简介行——去掉「联邦学习 · 隐私 / 统计 / Python（Federated Learning · Privacy · Statistics · Python）」，保留「机器学习 / 数据科学（ML · Data Science）」，新增「量化交易 / 智能体应用 / 智能体交易 / 数字产品（Quant Trading · AI Agent Apps · Agent Trading · Digital Products）」，仍按「背景领域 | 当前方向」两组以竖线分隔。

### 变更（英文简介行「AI Agent Apps · Agent Trading」改为「AI Agents · Agentic Trading」）

- **为什么改**：用户指出「Apps」一词会误导读者以为是手机 app 或 GUI 桌面软件——而 fleet 里全是 CLI agent、规则集、框架，无一 GUI 产物，语义与实际不符；且「Agent Trading」的说法不够地道。中文版「智能体应用 · 智能体交易」按用户要求保持不动。
- **改了什么**：README.md 第 9 行简介行——「AI Agent Apps · Agent Trading」→「AI Agents · Agentic Trading」，消除 Apps 歧义并采用更地道的「Agentic Trading」表述。

### 变更（「AI agent」统一为「AI Agent」）

- **为什么改**：两个 README 里同一术语大小写混用（副标题、旗舰项目段、赞助段共 5 处小写「AI agent / AI agents」，而表格与协作段用大写「AI Agent」），用户要求全仓统一为大写「AI Agent」。
- **改了什么**：README.md / README_cn.md 共 5 处「AI agent(s)」→「AI Agent(s)」——README_cn.md 第 7、123 行；README.md 第 7、25、123 行。全仓 grep 验证已无小写残留。

