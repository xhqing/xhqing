# Changelog

本仓库（xhqing）是 GitHub 个人主页仓库，也是 ExecutiveAssistantAgent（Kit）的子项目。本 CHANGELOG 记录本仓库的变更。

## [未发布]

### 变更（英文正文渠道列举 Xiaohongshu 统一为 RedNote）

- **为什么改**：用户 2026-09-09 确认统一口径——小红书官方英文名是 RedNote，Connect 徽章已改用，英文正文（销售流水线 Buzz 步骤的渠道列举）同步统一；中文版正文用中文名「小红书」不变（各语言用各自地道的官方名）。
- **改了什么**（2026-09-09）：`README.md` 销售流水线第 4 步渠道列举 `Xiaohongshu` → `RedNote`（`README_cn.md` 对应句用「小红书」，无需改）。

### 变更（Connect 区补充邮箱与小红书两个联系方式）

- **为什么改**：用户 2026-09-09 要求 Connect 部分再加上小红书和邮箱（此前只有 GitHub 与微信两个联系方式）；小红书号与主页链接均由用户提供（831230194，主页链接已实测 200）。
- **改了什么**（2026-09-09）：`README.md` / `README_cn.md` Connect 区各新增两枚徽章——`Email`（huaqing.xu.hk@gmail.com，mailto: 链接，Gmail 红）与 `RedNote`（小红书官方英文名，显示小红书号 831230194，点击跳转小红书主页，小红书品牌红；图标经 simple-icons 的 xiaohongshu slug 渲染——该库无 rednote slug，实测 logo=rednote 无图标）。

### 变更（页脚删去「用 ❤️ 与 Claude Code 构建」署名）

- **为什么改**：用户 2026-09-09 指出页脚的构建署名只写了 Claude Code，但实际用的构建工具不止它一个（还用了其它工具），只写一家不严谨——干脆不写；这也与 README「不含点明 LLM / 厂商的徽章」的既有约定同向。
- **改了什么**（2026-09-09）：`README.md` / `README_cn.md` 页脚行各删去第三段「🍻 Built with ❤️ & Claude Code」/「🍻 用 ❤️ 与 Claude Code 构建」，保留 Star 与关注团队壮大两段。

### 变更（Victor 条目口径更正：就是日内交易员）

- **为什么改**：用户 2026-09-09 指出小组介绍里 Victor 的描述「按标定后的信号做港股 / 美股实盘日内交易」解释不对——Victor 不是按 Markowitz 标定的信号做实盘交易，就是日内交易员，描述按此简化。
- **改了什么**（2026-09-09）：`README.md` / `README_cn.md` 各两处——① 小组介绍列表 Victor 分句改为「**Victor** 是日内交易员。」（英文 "…; **Victor** is the day trader."），删去「按标定后的信号做港股 / 美股实盘日内交易」表述；② 名册表投资与交易小组表头标语「从量化信号到实盘日内交易」同源问题，改为「量化策略与日内交易」（英文 "quant signals to live day-trading" → "quant strategies & day trading"），一并去掉「实盘 + 信号串联」的错误定性。

### 变更（Hopkins 条目改为工作接单全链路专门负责）

- **为什么改**：用户 2026-09-08 拍板找单接活找工作整体交给 Hopkins 专门负责（Kit 定位多面手、不再发起找单找岗），原句「Kit 发起找单找岗动作，Hopkins 让投出去的申请更多转化」的分工表述失效。
- **改了什么**（2026-09-08，Kit 会话）：`README.md` / `README_cn.md` 小组介绍列表 Hopkins 条目——职责开头改为「专门负责工作接单全链路：找单找岗、投递材料工程、漏斗追踪、报价与薪资测试」，删去「Kit 发起」分句。Kit 条目已于同日早前改为多面手口径（见「Kit 条目重写」条）。

### 变更（Kit 条目重写：定位多面手、icon 更正）

- **为什么改**：用户 2026-09-08 指出 Kit 是最重要的 Agent（第一助理），介绍不应限定在「找单找岗接活」——该职能相对定位不值一提；Kit 的定位是**多面手**，几乎任何事务都接得住、处理得了，不做某个领域的深度研究，什么都会、什么都能管。另小组介绍列表里 Kit 的 icon 误用了 👔（与名册表、架构图的 👩‍💼 职业女性形象不符）。
- **改了什么**（2026-09-08，Kit 会话）：`README.md` / `README_cn.md` 小组介绍列表 Kit 条目重写——icon 由 👔 改为 👩‍💼；描述改为「用户的第一助理、团队多面手：几乎任何事务都接得住、处理得了——不是某个领域的深度专家，而是什么都会、什么都能管」，删去「在远程工作社区与招聘平台找单找岗接活」的职能限定。

### 变更（旗舰项目节重排：组织结构前置，数字产品销售小组降为后置专段）

- **为什么改**：用户 2026-09-08 指出内容顺序问题——此前开篇以「数字产品全链路变现流水线」切入（那是三个小组之一的故事），组织全貌反而靠后；作为个人主页的旗舰展示，应先介绍组织结构（20 个专岗 Agent、三个小组 + 四位直属），再展开其中一个小组（数字产品销售）的流水线细节。
- **改了什么**（2026-09-08，Kit 会话）：`README.md` / `README_cn.md` 同构重排——① 开篇第一句从「多智能体团队跑通数字产品变现」改为组织全貌句（20 个专岗 Agent、三个业务小组 + 四位直属、Huaqing Xu 直接领导），原变现句与「六个组成流水线」句降级到销售小组专段开头；② 碳硅混合组织说明段、架构 mermaid 图、名册表、小组介绍列表（直属四条 + 三小组）保持在前半部，构成完整的组织结构介绍；③ 新增三级节「🛍️ 数字产品销售小组：产物接力的六段流水线」（an artifact-relay pipeline），收编变现句、六步接力详解、流水线注释；④ 子项目表随之移到销售专段之后；⑤ 小组介绍列表里销售小组条目的「上方六段流水线」引用改为「详见下文」（六步详解已移至列表后方）。两版节结构逐行对称（105 行销售专段 / 135 行组织怎么运转，位置一致）。

### 变更（CyberRipple 挂起：撤下互链，组织内容合并回本主页）

- **为什么改**：用户 2026-09-08 重新决策——CyberRipple Organization 目前为空组织，当前主线是投递找工作、对外链接全部指向 github.com/xhqing，组织门面没有访客入口、招聘方点进空组织反而是负资产；个人主页是唯一展示位，内容应集中一处做深。此前双处维护已实际发生漂移（子项目表过时、括号注未同步、流水线注重复出现两次）。CyberRipple 挂起（README 留白、底稿留本地），本仓库吸收其增量内容成为唯一门面。
- **改了什么**（2026-09-08，Kit 会话）：`README.md` / `README_cn.md` 各七处——① 撤下「🏢 组织门面：CyberRipple」互链行；② 原位改为完整组织架构 mermaid 图（自 CyberRipple 迁入），图前补「碳硅混合组织」说明段（全员 AI Agent、为吸纳人类成员而设计）；③ roster 表 Hopkins / Justin 行删括号注（用户同日裁定：名册行不加括号解释）；④ subprojects 表对齐全局超集映射表——删 market-data-backup（不在映射表、私有仓库链接对外无效）、补 zcode-cli / zcode-vsce / gridtrader，引导句「六个 AI Agent 各自维护一个专项项目」改为不限数的表述；⑤ 删 subprojects 表后重复出现的流水线注释行；⑥ squads 列表 Hopkins / Justin 段删同款括号注（Justin「跨组服务全部小组」融入正文，「财务岗位暂时空缺」系内部管理状态、删除）；⑦ 新增「⚙️ 组织怎么运转」节（自 CyberRipple 迁入：产物交接、共享能力层、推理引擎作为基础设施、三权分立质量门禁、合同与收款五条 + 数字一览一行）。CyberRipple 侧的留白与底稿处理见其仓库 CHANGELOG。

### 变更（Justin 条目口径清理：纯法务、财务岗位暂时空缺）

- **为什么改**：用户 2026-09-08 明确 Justin 定位为纯法务（直属用户、不属任何小组），财务职能暂时空缺——roster 表与 squads 列表里 Justin 行的「finance & legal / 财务与法务」括注与新口径矛盾，随全局注册表口径更新一并清理。
- **改了什么**（2026-09-08，Hopkins 会话）：`README.md` / `README_cn.md` 各两处——roster 表 Justin 行括注与 squads 列表 Justin 段落括注，统一改为「pure legal; serves all squads cross-team — the finance seat is currently open / 纯法务；跨组服务全部小组——财务岗位暂时空缺」。链接保持 `LegalAgent`（注册表新名；GitHub 仓库未建、立项待办见 ApplyOptimizerAgent TODO T12）。

### 变更（旗舰项目节新增 CyberRipple 组织门面互链）

- **为什么改**：用户的 AI Agent 团队有完整组织架构（五小组 + 直属，20+ 专岗 Agent），此前只有本个人主页一处呈现；用户 2026-09-08 决定启用 GitHub Organization「CyberRipple」作组织门面（org profile README 写清组织架构、链接指回个人仓库，仓库不迁移避免断链）。个人主页加互链入口，双门户互相引流。
- **改了什么**（2026-09-08，Hopkins 会话）：`README.md` / `README_cn.md` 旗舰项目节各加一行 blockquote——指向 github.com/CyberRipple 的组织主页链接（英文「Organization front door」/ 中文「组织门面」）。CyberRipple org 侧 `.github` 仓库与 profile README 同日新建（本地 /Users/xhq/Developer/CyberRipple），待推送。

### 变更（小组更名同步：任务池投标小组 → 工作接单小组）

- **为什么改**：用户 2026-09-06 拍板小组更名（「任务池投标」降为小组下的接单策略之一、与招聘平台求职并列），本仓库 roster 双语的分组行与五小组列表、Kit 子项目 `.claude/CLAUDE.md` 的对口表述须同步。
- **改了什么**：① `README.md` / `README_cn.md`：Hopkins 所在分组行（Task-pool bidding squad → Work-intake squad / 任务池投标小组 → 工作接单小组，分组描述注明 task-pool bidding & job-platform applications / 任务池投标与招聘平台求职为并行接单策略）、五小组列表该行开头；② `.claude/CLAUDE.md`：工作原则第一条与「你的位置」小组名两处。

### 变更（roster Hopkins 行更名 ApplyOptimizerAgent；Kit 口径与 traffic 清单同步）

- **为什么改**：电鸭平台岗位多为全职岗、有详细 JD、沟通需发简历——与 BOSS直聘求职同构，「投单」与「找工作」合流为同一条投递漏斗（2026-09-06 用户拍板），Hopkins 项目由 BidOptimizerAgent 更名 ApplyOptimizerAgent、Title「投递转化率优化师」。本仓库 roster（双语）的 Hopkins 行、任务池投标小组描述、Kit 的找单找岗口径、访问统计采集清单须同步。
- **改了什么**：① `README.md` / `README_cn.md`：Hopkins roster 行（Bid Optimizer → Apply Optimizer、职称、仓库链接）、任务池投标小组段落（投递材料工程（标书 + 简历 + 打招呼话术）/ 漏斗含沟通与面试、成单与 offer / 报价与薪资测试）、Kit 直属行找单找岗口径与渠道举例（电鸭、BOSS直聘）；② `.claude/CLAUDE.md`（Kit 子项目超集内容）同步同样口径；③ `scripts/update_traffic.py` 的 `TEAM` 清单 `'BidOptimizerAgent'` → `'ApplyOptimizerAgent'`；④ 预建 `traffic/badges/ApplyOptimizerAgent.json` + `.meta.json`（零值，与 TestEngineerAgent 预建格式一致；原 BidOptimizerAgent.json 从未生成过，无历史数据可迁移）。
- **注意**：GitHub 仓库 rename 完成前，采集清单里的新名字在 GitHub API 中尚不存在——需先完成 rename、再 push 本仓库让 Action 按新清单采集。

### 变更（roster 双语纳入 Hopper / TestEngineerAgent；traffic 采集清单同步）

- **为什么改**：新建软件测试 Agent TestEngineerAgent（Hopper，软件测试工程师，2026-09-06 立项，隶属基础设施小组）——为全团队软件项目建功能测试与回归防护网（用例先行 + CI 红灯门禁），把「改 A 坏 B」拦在合并进 main 之前。按集中式访问统计机制，新仓库须列入 `update_traffic.py` 的 `TEAM` 清单才会有徽章数据源（TestEngineerAgent 的 README 已挂该徽章）。
- **改了什么**：① `README.md` / `README_cn.md` 基础设施小组 roster 各加 Hopper 行（🐞 软件测试工程师 / Test Engineer，含徽章 endpoint）；两版基础设施小组文字描述各补 Hopper 一句（回归防护网：开发前先写验收测试用例、合并前 CI 红灯门禁）。② `scripts/update_traffic.py` 的 `TEAM` 清单加 `'TestEngineerAgent', # Hopper`。③ 预建 `traffic/badges/TestEngineerAgent.json`（schemaVersion 1 / Visits/day (14d) / 0 / brightgreen）与 `TestEngineerAgent.meta.json`（零值），与既有项目格式一致。
- **回归检查**：Gatsby 及其余 roster 行、五小组结构、既有徽章 JSON 未动；update_traffic.py 仅追加一行清单项。

### 变更（Gatsby 行社群描述更新：社群定名「AI前沿跨界交流群」、清退「互帮互助」表述）

- **为什么改**：CommunityManagerAgent（Gatsby）侧定位校准（2026-08-27 / 08-28）——群主定名社群为「AI前沿跨界交流群」，并裁定「互帮互助」不在任何地方体现（多数群友为获取信息而来、无明确求助需求且不想被求助打扰，互助是群活跃后的自然副产品）。本仓库 roster 双语 Gatsby 行的社群描述仍是旧口径「以 AI 为纽带的跨界互帮互助交流群」，须同步更新。
- **改了什么**：`README.md` / `README_cn.md` Gatsby 行社群描述改为「运营用户自己的微信社群『AI前沿跨界交流群』」（英文版 an AI-frontier, cross-industry exchange group）。其余未动。
- **回归检查**：Gatsby 行之外的 roster 内容、五小组结构、徽章 URL 未动。

### 变更（roster 双语纳入 Gatsby / CommunityManagerAgent；traffic 采集清单同步）

- **为什么改**：新建微信社群运营 Agent CommunityManagerAgent（Gatsby，社群运营官，2026-08-25 立项）——运营用户的微信社群（以 AI 为纽带的跨界互帮互助交流群），理念方法由 agent 出、群主辅助引导执行；用户裁定不分组、直属用户（与 Kit 同待遇，主页「直属用户」段需加行、职责说明段需从一位改两位）。按集中式访问统计机制，新仓库须列入 `update_traffic.py` 的 `TEAM` 清单才会有徽章数据源（CommunityManagerAgent 的 README 已挂该徽章，仓库未推上 GitHub 前访问列以「—」占位）。
- **改了什么**：`README.md` / `README_cn.md` 同步——「直属用户」表格段加 Gatsby 行（🥂 / Community Manager / 社群运营官 / CommunityManagerAgent 链接 + 访问列「—」占位）；职责说明段「一位助理」改「两位助理」并补 Gatsby 直属说明（私域社群运营，公域投放归 Buzz）。`scripts/update_traffic.py` 的 `TEAM` 清单追加 `'CommunityManagerAgent'`（# Gatsby，仓库数 24 → 25）；预建 `traffic/badges/CommunityManagerAgent.json` 与 `.meta.json`（零值初始，格式与既有徽章一致，避免仓库上线前 README 徽章 dangling）。
- **回归检查**：六段流水线成员与顺序、接力说明、子项目表未动；五小组结构未动（Gatsby 不进任何小组）；徽章 URL 形态不变。

### 变更（Kit 主项目更名联动：roster 链接 / Visitors 徽章 / traffic badge 文件与流量脚本清单更新）

- **为什么改**：Kit 主项目由 PersonalAssistantAgent 更名为 ExecutiveAssistantAgent（Title「总经理助理」定名后的名字对齐，GitHub 仓库同步改名、旧名 URL 由 GitHub 自动重定向，详见该项目 CHANGELOG）——本仓库 README roster 的仓库链接 / Visitors 徽章 URL、`traffic/badges/` 数据文件名、`scripts/update_traffic.py` 团队清单均含旧名，不改则徽章 404、每日采集会再生成旧名 JSON 造成数据分叉。
- **改了什么**：`README.md` / `README_cn.md` Kit 行（GitHub 链接、徽章 URL；英文版两处职称 GM's Assistant → Executive Assistant：roster 表 + 直属用户职责说明段）；`traffic/badges/PersonalAssistantAgent.json` / `.meta.json` 更名为 `ExecutiveAssistantAgent.*`（历史累计数据随文件保留，GitHub 改名后 Traffic API 按新仓库名继续累计）；`scripts/update_traffic.py` `TEAM` 清单同步更名（仓库数不变）；本 CHANGELOG 头部说明句同步。`xhqing/.claude/CLAUDE.md` 指代说明按超集规则同步（源头变更记 ExecutiveAssistantAgent 的 CHANGELOG）。


### 变更（小组重组为五个：新增财务与法务小组，Justin 移入；Kit 改「总经理助理」不分组；纳入 Hopkins / BidOptimizerAgent）

- **为什么改**：用户 2026-08-23 三项裁定——① 新建「财务与法务小组」，Justin（LegalAgent）移入该组，职责升格为「负责整个团队所有跟合同和收款相关的事项」（跨组服务）；② Kit 的 Title 由「个人助理」改为「总经理助理」，且不分组、不属于任何小组（直属用户的第一助理）；③ 新建投标转化率优化 Agent Hopkins（BidOptimizerAgent），加入任务池投标小组（漏斗上游：标书工程 / 漏斗追踪 / 中标率归因 / 报价测试）。团队分组由四个变为五个。
- **改了什么**：README.md / README_cn.md 同步——表格头新增「👔 直属用户」段放 Kit（Title 改 GM's Assistant / 总经理助理）；任务池投标小组成员由 Kit+Justin 改为 Hopkins（Justin 移出）；新增「💰 财务与法务小组」段放 Justin；职责说明段同步重写为「五位助理之外五小组」结构。`scripts/update_traffic.py` 的 `TEAM` 清单追加 `'BidOptimizerAgent'`（# Hopkins，仓库数 23 → 24）。Kit 主项目（PersonalAssistantAgent）的 CLAUDE.md / README 双语 Title 同步改，并按超集规则覆盖 xhqing/.claude/CLAUDE.md。BidOptimizerAgent / LegalAgent 仓库尚未推上 GitHub，访问列暂以「—」占位。
- **回归检查**：六段流水线成员与顺序、接力说明、子项目表未动；本次「五小组」重组覆盖同日早前的「四小组」条目，后者为迭代中间态、已由本条目取代（历史条目保留不删）。

### 变更（舰队表格重组为四个小组分类；纳入 Justin / LegalAgent；补 Atlas 遗漏行）

- **为什么改**：① 用户 2026-08-23 裁定全团队按涉及领域分四个小组——任务池投标小组、数字产品销售小组、投资与交易小组、基础设施小组，主页表格需按此分类展示；② 新建 LegalAgent（Justin，法务顾问 Agent，合同 / 收款 / 纠纷归口），进「任务池投标小组」（与 Kit 搭档：Kit 找单、Justin 保障交易）；③ 发现 Atlas（FullStackEngineerAgent）此前只进了 traffic 采集清单（CHANGLOG 有记录）、主页表格一直漏了行——本次重组顺带补上，进「基础设施小组」。
- **改了什么**：README.md / README_cn.md 同步——舰队表格从「销售流水线 + 独立 Agent」两段重组为四段：🎯 任务池投标小组（Kit、Justin）/ 🛍️ 数字产品销售小组（六段流水线成员）/ 📈 投资与交易小组（Victor、Markowitz）/ 🧰 基础设施小组（Tinker、Prometheus、Hermes、Anvil、Atlas、Ada、Alfred）；「流水线之外」职责段改写为四小组逐组说明，并注明「凡涉及合同与钱的场合 Justin 同时服务其它三个小组」；补 Atlas 行（含 traffic 徽章）。`scripts/update_traffic.py` 的 `TEAM` 清单追加 `'LegalAgent'`（# Justin，仓库数 22 → 23）；LegalAgent 仓库尚未推上 GitHub，表格中其访问列暂以「—」占位、徽章数据源待仓库上线后由 Action 自动生成。
- **回归检查**：六段流水线的成员与顺序、接力说明段、子项目表均未动；徽章 URL 形态（指向 xhqing traffic/badges/ 的 endpoint）不变；Justin 尚无 badge JSON，「—」占位与 Mason / Ada 同法处理，无 dangling 引用风险（endpoint 徽章在 JSON 未生成前显示为加载失败占位，故用「—」纯文本代替）。

### 变更（traffic 采集清单纳入 Atlas 主仓库及其子项目）

- **为什么改**：新建 FullStackEngineerAgent（Atlas，全栈开发工程师 Agent），其子项目 zcode-cli（非官方 ZCode 终端客户端）随之入 fleet——按 2026-08-16 集中式访问统计的机制，各 fleet 仓库须列入 `update_traffic.py` 的 `TEAM` 清单才会有 `traffic/badges/<repo>.json` 徽章数据源（FullStackEngineerAgent 的 README 已挂该徽章；zcode-cli 当前为 fork、尚未确认是否挂）。
- **改了什么**：`scripts/update_traffic.py` 的 `TEAM` 清单追加 `'FullStackEngineerAgent'`（# Atlas）与 `'zcode-cli'`（# Atlas's subproject）两行，仓库数从 20 增至 22；采集逻辑不变。

### 变更（Profile README 舰队表格与子项目表纳入 Alfred / DeviceStewardAgent）

- **为什么改**：新建 DeviceStewardAgent（Alfred，电脑管家 Agent）已推上 GitHub（2026-08-20），ResourceMonitor 确认为其子项目——Profile README 的舰队表格与「Agent 负责的子项目」表需与全局注册表对齐（此前缺 Alfred 行，读者看不到第 16 个 agent）。
- **改了什么**：README.md / README_cn.md——舰队表格「独立 AI Agent」段末尾加 Alfred（🖥️ / Device Steward / DeviceStewardAgent + traffic 徽章）；子项目表加「Alfred → ResourceMonitor」行、计数从五个改六个；「流水线之外」职责句补 Alfred（设备资源管理：本地电脑 / 远程服务器 / 云电脑）。两版同步改。

### 变更（traffic 采集清单纳入 Alfred 主仓库及其子项目）

- **为什么改**：新建 DeviceStewardAgent（Alfred，电脑管家 Agent）并推上 GitHub，其子项目 ResourceMonitor（VSCode 扩展：整机资源监控 + AI 清理建议）随之正式入 fleet——按 2026-08-16 集中式访问统计的机制，各 fleet 仓库须列入 `update_traffic.py` 的 `TEAM` 清单才会有 `traffic/badges/<repo>.json` 徽章数据源（DeviceStewardAgent 的 README 已挂该徽章，ResourceMonitor 后续挂）。
- **改了什么**：`scripts/update_traffic.py` 的 `TEAM` 清单追加 `'DeviceStewardAgent'`（# Alfred）与 `'ResourceMonitor'`（# Alfred's subproject）两行，仓库数从 18 增至 20；采集逻辑不变（未挂徽章不影响采集，404 自动跳过的保护仍在）。

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

### 变更（赞助段措辞：「持续造」改「持续创造」并扩展到「AI Agent 和 Project」）

- **为什么改**：用户要求（2026-08-16）赞助段一句「让我有动力持续造更多 AI Agent」改为「让我有动力持续创造更多 AI Agent 和 Project」——「造」改「创造」更规范，同时把创作对象从单一 AI Agent 扩展到 AI Agent 与 Project 两类。
- **改了什么**：README_cn.md 第 110 行赞助段——「持续造更多 AI Agent」→「持续创造更多 AI Agent 和 Project」；README.md 第 110 行英文版同步——「build more AI Agents」→「build more AI Agents and Projects」（英文按原句 "build" 动词顺延补 "and Projects"，与中文语义对齐）。

### 变更（Prometheus 职责描述去掉 settings.json）

- **为什么改**：用户指出 Prometheus 开源的通用能力枚举里不应包含 settings.json——按全局规矩（「底层通用能力开源」节，2026-08-04 起范围为三部分），开源镜像只覆盖 `skills/`、`rules/`、`CLAUDE.md` 三部分，settings.json 不在其中，README 枚举与实际范围不符。
- **改了什么**：README.md 第 72 行——「such as the global CLAUDE.md, global skills, global rules, and settings.json」→「such as the global CLAUDE.md, global skills, and global rules」；README_cn.md 第 72 行同步——「如全局 CLAUDE.md、全局 skills、全局 rules 以及 settings.json 等」→「如全局 CLAUDE.md、全局 skills、全局 rules 等」（按「中英双语 README 内容自动同步」规矩两版同轮改）。

### 变更（赞助段措辞再改：「这让我有动力」+「更多更优质」+「或其它 Project」）

- **为什么改**：用户要求（2026-08-17）在上一条措辞基础上进一步打磨——（1）句首补主语「这」，指代前文「赞助」这件事，句子更完整；（2）「更多」改「更多更优质」，表达不只要数量、还要质量提升；（3）连接词「和」改「或其它」，表明 AI Agent 与 Project 是列举关系（Project 泛指 AI Agent 之外的其它项目），并列改或然列举。
- **改了什么**：README_cn.md 第 110 行赞助段——「让我有动力持续创造更多 AI Agent 和 Project」→「这让我有动力持续创造更多更优质的 AI Agent 或其它 Project」；README.md 第 110 行英文版按新立的「中英双语 README 内容自动同步」全局规矩（2026-08-17）一并同步——「build more AI Agents and Projects」→「this keeps me motivated to keep creating more and better AI Agents and other Projects」（补指代主语 this、叠加 more and better 表「更多更优质」、and other Projects 表「或其它 Project」）。

### 变更（访问量徽章更名：Visitors → Visits/day (14d)，表达「近半月日均」口径）

- **为什么改**：用户要求（2026-08-17）「Profile Visitors」与各仓「Visitors」徽章的 label 需表达出「最近半个月日均访问量」，且名字不能太长——`Visitors` 不含日均与时间窗口信息，读者看不出数字的口径。经候选比较（`Visits/day (14d)` / `Daily Visits (14d)` / `Visits/day · 14d` / `Avg Visits/day`）定为 `Visits/day (14d)`：`Visits/day` 是 shields.io 生态表达日均的惯例写法（同 `downloads/day`），括号 `(14d)` 是标注统计窗口的通行方式（Grafana / Datadog 常用），组合 17 字符、语义完整。
- **改了什么**：
  - [`scripts/update_traffic.py`](scripts/update_traffic.py)：单仓徽章 label `Visitors` → `Visits/day (14d)`（第 120 行），profile 徽章 label `Profile Visitors` → `Profile Visits/day (14d)`（第 156 行），docstring 的 label 说明同步；后续每日 Action 采集自动按新 label 生成。
  - `traffic/badges/*.json`：16 个单仓徽章 + 1 个 profile 徽章的 `label` 字段同步改为新名（`message` 数字不变），免等下次 Action、即刻生效。
  - README.md：顶部 profile 徽章 alt、舰队表格第四列表头 `Visitors` → `Visits/day (14d)`、14 行内嵌徽章 alt `<Name> Visitors` → `<Name> Visits/day (14d)`；README_cn.md：profile 徽章 alt 同步、表格表头「日均访问」→「近半月日均访问」、14 行 alt「<名> 日均访问」→「<名> 近半月日均访问」（中文按窗口口径表意，不硬译英文 label）。
- **历史漂移修正**：CHANGELOG 早期条目（1.1.0「徽章英文首字母大写」等）记录的 label 为 `Visits/day`，但当前脚本与 JSON 实际是 `Visitors`——上次「删 fleet 徽章 + Profile 徽章改口径」重构时 label 被改成了 `Visitors` 而未在 CHANGELOG 里记录这次 label 变化。本次以实际文件为准收口为 `Visits/day (14d)`，与早期条目的 `Visits/day` 一脉相承（加上窗口标注）。
- **回归检查**：与「徽章口径从累计改为日均」（1.1.0）、「删 fleet 汇总徽章 + Profile 改近半月口径」（Unreleased）、「徽章英文首字母大写」（Unreleased）三条改动的关系——本次只改 label / alt / 表头的**文字**，口径（avg14 算法）、数字、URL、生成逻辑均不动；新 label 首字母大写符合「徽章英文首字母必须大写」规矩，无回归。

