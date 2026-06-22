# Biomimetic Design Library — Claude Code Project Guide

## 当前权威覆盖（2026-06-22，优先级高于下方历史审计规则）

- \`v0.2\` 已接受并打 tag；V1-A 已在 \`1106089\` 接受。
- 当前阶段是 **V1-B：按 ADRMATS 域缺口扩充生物/仿生原型**，目标是从现有 36 个 root prototypes 继续向 v1.0 推进。
- 下方“不要修改 \`prototypes_db/*.json\` / 不要提交 git / 24 个原型 / 全量证据审计 Batch 09”等内容是历史审计阶段规则；若与本节冲突，以本节为准。
- V1-B 允许在通过准入门槛时创建新的 root prototype、修改 \`prototypes_db/*.json\`、\`prototypes/<id>/prototype.md\`、\`feature-mapping.json\`、\`docs/active/**\`，并做安全 checkpoint commit/push。
- **身份门槛：root prototype 必须是生物来源/仿生机制/可迁移自然结构**，能回答“ADRMATS 可以从哪个生物机制借设计原则”。不得把通用合成材料类别作为 root prototype，例如 generic biochar、hydrogel、silica、nanofiber membrane、graphene oxide、magnetic adsorbent、polydopamine composite。
- 合成材料、工程材料、制备路线可作为已有/新增生物原型的 \`material_realization_examples\`、implementation handle 或 performance evidence；不能单独冒充 biological prototype。
- 新 root prototype 准入门槛：至少 1 个 fully grounded from-source mechanism（真实 DOI/专利/标准 + quote + locator + scope match）、honesty ledger、至少 1 个 boundary/boundary note、actionable design_translation、source mapping、相关 domain/gold-set 行为。
- 不得引用或复活 \`docs/registries/refuted-log.md\` 中的来源；遇到 refuted DOI 的候选必须降级、隔离或重新取证。
- 计量口径：对外区分“挂引文/locator 的机制数”和“全因果链完全接地的比例”；不要把前者表述为“已验证率”。verified 层数量需单独报告。
- 模型路由：PDF/OCR/多模态/图像页读取用 \`mimo-v2.5\` 子 agent 或 OpenClaw；文本推理、source-to-claim、JSON/schema 工作用 \`mimo-v2.5-pro\`。
- 仍然禁止：\`git add -A\`、force-push、history rewrite、无授权删除/merge/park/rename 已接受原型、证据标签膨胀、修改 \`tools/litextract\` / \`*_doi_map.json\` / \`docs/optimization-v1\` / \`.claude/settings.local.json\`。

## 项目概述

仿生吸附设计库策展与接地（curation & grounding）项目。目标：对 `prototypes_db/` 中的 24 个仿生吸附原型做全量证据审计，确保每条性能数据、机制、工程约束都有 PDF 级文献支撑。

## 关键路径（办公室 Windows 环境）

| 路径 | 说明 |
|------|------|
| `C:\Users\15995\Desktop\Biomimetic-design-library` | 项目根目录 |
| `仿生文献库\2nd\` | 第二波文献 PDF（按原型分组） |
| `仿生文献库\3rd\` | 第三波文献 PDF（按方向分组） |
| `仿生文献库\专利\` | 中国专利 PDF + visual_cache JSON |
| `仿生文献库\论文\` | 论文 PDF |
| `仿生文献库\标准\` | 标准文档 |
| `prototypes_db\` | 原型 JSON 数据库（主库） |
| `prototypes_db\enrichment\` | enrichment mirror JSON |
| `prototypes_db\materials_reference\` | 材料参考 JSON（MOF、starch 等） |
| `prototypes_db\parked\` | 停用原型 JSON |
| `prototypes_db\separation\` | 分离/超疏水原型 JSON |
| `tools\` | 验证/构建脚本 |
| `tools\litextract\` | 文献提取子模块（已初始化） |
| `docs\archive\optimization-v1-2026-06\` | 归档：阶段报告、证据审计、旧交接、任务历史、生成日志（原 `docs\optimization-v1\` 已迁入） |
| `docs\registries\` | 活跃机器账本：decision-queue、boundary-do-not-register、refuted-log |
| `docs\references\` | 标准/计划：definitions、optimization-plan-v1、full-audit-plan |
| `docs\active\` | 当前恢复操作文档（恢复设计、接手指南、本清单） |

## 当前工作阶段

**全量证据审计（Full Evidence Audit）** — Batch 09 已完成，等待 Yao 审批决策队列。

### 执行模型

- **OpenClaw / Claude Code**：批量 PDF 证据验证、路径规范化、OCR、草稿批次输出
- **Codex / Qoder**：范围控制、验收抽查、决策队列/边界寄存器维护、worklog、GitHub checkpoint
- **Yao**：最终审批决策

### 当前硬性限制（V1-B 生物/仿生扩展阶段）

1. **允许修改 `prototypes_db/*.json`**，但仅限已授权的 V1-B 生物/仿生扩展或既有原型证据卫生；新增 root prototype 必须满足上方“当前权威覆盖”的生物身份门槛与准入门槛。
2. **不要运行 `tools/build_prototypes_db.py`** — 它会从旧提取反向重建 canon，可能冲掉整改成果。
3. **不要把通用材料类别作为 root prototype**：biochar、hydrogel、silica、nanofiber membrane、graphene oxide、magnetic adsorbent、polydopamine composite 等只能作为 material_realization_examples / implementation handle / performance evidence。
4. **不要升级 `verification`、`hard_do_not`、`soft_boundary` 状态** — 除非 Codex/Yao 明确授权。
5. **允许安全 checkpoint commit/push**，但禁止 `git add -A`、force-push、history rewrite；提交前必须排除本地设置、会话日志、`docs/optimization-v1`、受保护工具/映射资产。
6. 缺 PDF、扫描专利、OCR 不确定、LLM 推断内容 → 标为 `missing_pdf` / `needs_human_decision` / `knowledge_gap` / `inferred_only`，不得证据膨胀。
7. 只有明确来源错配或直接文献支持的边界 → 才可建议 `wrong_source` 或 `hard_do_not`。

### 审计批次输出规范

每个批次输出一个 Markdown 文件；**新审计/证据报告的位置由 `docs/active/execution-roadmap.md`（operational runbook）规定**——`docs/archive/**` 仅用于历史追溯，**不得**作为新审计输出目录或硬编码输出路径。

每项必须包含：`prototype_id`、`target_json`、`field_path`、`claim_summary`、`local source_file` 或 `missing_pdf`、`locator`、`quote`、`evidence_label`、`recommended_action`、`notes`

### 文献库路径注意

- 家里 macOS 路径格式：`/Users/panyao/Desktop/Biomimetic-design-library/仿生文献库/...`
- 办公室 Windows 路径格式：`C:\Users\15995\Desktop\Biomimetic-design-library\仿生文献库\...`
- JSON 中 `source_file` 字段存储的是相对路径或家里绝对路径，批量操作时需注意路径适配
- PDF 文件名中的空格和中文字符是正常的，不要修改文件名

## 决策队列 / 寄存器（活跃）

`docs/registries/decision-queue.md` — 所有待审批项（活跃机器账本）

`docs/registries/boundary-do-not-register.md` — 边界/DO-NOT 寄存器（活跃）

`docs/registries/refuted-log.md` — 已移除的 wrong-source 行（不得复活）

> 历史 worklog / sync-summary 已迁入 `docs/archive/optimization-v1-2026-06/old-handoffs/`，仅作历史追溯，不再作为启动必读或当前状态入口。

## 协调协议

角色分工、worker prompt、模型路由、验收两阶段门等**当前**规范见 `docs/active/`：
`model-routing-protocol.md`（协作与模型路由）、`evidence-quality-standard.md`（证据验收）、`execution-roadmap.md`（里程碑与 acceptance runbook）。
（历史 `review-openclaw-coordination.md` / `worker-prompts.md` / `next-tasks.md` 已归档于 `docs/archive/.../task-history/`，仅供追溯。）

## 启动入口（每次启动先读）

> **入口是 `docs/README.md`，随后 `docs/active/**`、`docs/registries/**`、`docs/references/**`。**
> `docs/archive/**` 仅用于历史追溯，不是启动必读、不是新报告输出目录。

1. `docs/README.md` — 文档总索引与目录布局
2. `docs/active/execution-entry.md` — 当前状态与下一步（live entry point）
3. `docs/active/PROJECT-RECOVERY-DESIGN.md` — 恢复架构（权威）
4. `docs/active/recovery-master-plan.md`、`docs/active/canon-recovery-spec.md`、`docs/active/evidence-quality-standard.md`、`docs/active/model-routing-protocol.md`、`docs/active/execution-roadmap.md`
5. `docs/registries/`（decision-queue、boundary-do-not-register、refuted-log）、`docs/references/`（definitions、optimization-plan-v1 等）

**工作循环（恢复阶段）：** 读取 `execution-entry.md` 的当前状态 → 按 `execution-roadmap.md` 的里程碑推进 → 每个字段级 canon 改动写一条 `docs/registries/canon-recovery-ledger.jsonl` 条目 → 遇歧义/工具/canon 边界即停止并升级。


## 模型选择规则

- **默认模型 mimo-v2.5-pro**：文本任务（Task 1-3），包括 JSON 对比、PDF 文本提取、路径核查
- **多模态模型 mimo-v2.5**：需要读取图片时使用（Task 4 专利 OCR、visual_cache.json 中的截图验证）
- 切换到 mimo-v2.5 的时机：当需要查看 visual_cache 截图、扫描版专利图片、或 figure-estimated values 时
- ultracode 模式下可为不同子智能体分配不同模型：文本审计用 mimo-v2.5-pro，多模态子任务用 mimo-v2.5

## 并发限制

- **最多 3 个并行子智能体**，共享同一个 API key，超出会触发 429 限流
- 之前的 OpenClaw 在 Batch 01 同时启动 5 个 worker 导致大面积 429 错误，引以为戒
- 建议策略：1-2 个并行 + 1 个串行验收

## 历史任务记录（2026-06-17，归档追溯用，非当前指令）

> 以下"当前任务 / 下一批任务 / 第N轮"小节是 **2026-06-17 OpenClaw/Codex 协作期的历史任务分配**，对应输出已写入 `docs/archive/optimization-v1-2026-06/`。它们仅作历史追溯，**不是当前启动必读，不是新报告输出位置**。新审计/证据报告位置由 `docs/active/execution-roadmap.md` 规定。

## 当前任务（Qoder 分配  2026-06-17）

### 任务 1：Enrichment Mirror Gap Fill（最高优先级）
- 525/525 enrichment causal_chain 字段为空
- 4 个 enrichment 文件为空 {}（biomineralization-template, coral-skeleton, dna-aptamer, magnetic-bacteria）
- 对照主 JSON 和源 PDF，为已验证的 mechanism 填充 causal_chain
- **不要**机械同步；只从 source-backed 的主 JSON mechanism 中提取
- 输出文件：docs/archive/optimization-v1-2026-06/task-history/review-clcode-enrichment-audit.md

### 任务 2：Missing PDF 路径验证
- chitosan.json: 99 个 missing_pdf 项  检查路径是否有  2.pdf/ 3.pdf 后缀变体
- 产出可操作的路径映射表
- 输出文件：docs/archive/optimization-v1-2026-06/task-history/review-clcode-missing-pdf-paths.md

### 任务 3：Wrong-Source 二次验证
- lotus-leaf.json：355 个 mechanisms 按实际生物来源分组
- cellulose-nanocrystal.json：按材料类型分组（CNC/CNF/通用纤维素/复合材料）
- 输出文件：docs/archive/optimization-v1-2026-06/task-history/review-clcode-wrong-source-deep.md

### 任务 4：Patent OCR 辅助
- 对扫描版专利的 visual_cache.json 做文本提取
- 验证 decision queue 中标记的 figure-estimated values

### 协作方式
- Qoder 会通过写文件或对话分配任务
- 完成后产出审计文件到 docs/archive/optimization-v1-2026-06/task-history/review-clcode-*.md
- Qoder 会 spot-check 后决定是否 accept
- 有歧义标记 
eeds_qoder_review，不要自行决定


## 下一批任务（2026-06-17 第二轮）

Qoder 已完成第一层 wrong-source 清除、Scope 决策、边界规则写入。以下是你的新任务：

### Task 5: Metadata Fix Batch（25 项）
参考 docs/archive/optimization-v1-2026-06/task-history/review-clcode-task1-decision-queue-summary.md Category D 列表：
- 修正 false precision（silk-fibroin: 86.24%→86%, 96.29%→96%）
- 修正 verification_quote 为真实文本摘录而非标题（silk-fibroin）
- 修正 source_file 路径（path normalization，参考 Task 3 报告）
- 修正 single_source verification 语义（MOF）
- 修正 unit mismatch（starch-granule mmol/g vs mg/g）

### Task 6: 剩余 Wrong-Source 清除
以下 3 个原型的 wrong-source 数据尚未清除：
- **lotus-leaf**: 非莲花示例（shark, gecko, rose-petal, membrane, MOF, shell, sponge）必须从 mechanisms/performance_data 中移除
- **polydopamine-coating enrichment**: 超疏水/抗菌/膜综述机制必须从 enrichment 中移除
- **dna-aptamer**: biosensor LOD/Kd 值不能作为吸附容量，需要标注或移除

产出：
eview-clcode-task5-metadata-fixes.md + 
eview-clcode-task6-remaining-wrongsource.md

### Task 7: Decision Queue 状态更新
将已处理的 decision queue 项的 status 更新：
- 已删除的 wrong-source 项：status → pplied_package_b1
- 已写入的 scope 决策项：status → pplied_scope_decision
- 已写入的边界规则项：status → pplied_boundary
参考：docs/registries/decision-queue.md

### 执行约束
- 最多 3 个并行子智能体
- 文本任务用 mimo-v2.5-pro，多模态用 mimo-v2.5
- 修改 JSON 前先 dry-run
- 不改 build_prototypes_db.py
- 产出 review-clcode-*.md 报告后结束


## 第三轮任务（2026-06-17 第三轮）

### Task 8: Path Normalization Sweep（最高优先级）
参考 docs/archive/optimization-v1-2026-06/task-history/review-clcode-task3-missing-pdf-analysis.md：
- 扫描 仿生文献库/ 目录，查找所有  2.pdf、 3.pdf 后缀变体
- 将 prototypes_db/**/*.json 中所有 source_file 路径与实际本地 PDF 做交叉匹配
- 对能匹配的路径：直接修正 source_file 字段
- 对仍无法匹配的路径：记录到报告中标注 	ruly_missing
- 重点关注：chitosan（34 PDFs）、MOF（28 PDFs）、CNC（27 PDFs）、starch（10 PDFs）

### Task 9: Decision Queue 批量状态更新
Task 7 只更新了 9 项。现在补充更新其余 ~108 项：
- 对照已执行的 wrong-source 清除（150+30 条）：status → pplied_package_b1
- 对照已写入的 scope 决策（8 项）：status → pplied_scope_decision
- 对照已写入的 boundary rules（47 条）：status → pplied_boundary
- 对照 Task 5 metadata fix（12 项）：status → pplied_metadata_fix
- 无法匹配到已执行操作的项：保持 pending_yao
参考文件：
- docs/registries/decision-queue.md
- docs/registries/boundary-do-not-register.md（已标记 guard_rule 的 14 项）

### Task 10: Lotus-Leaf Scope Assessment
lotus-leaf 有 346 条剩余机制（Task 6 已移除 9 条膜/蒸馏）。现在评估：
- 逐条检查 346 条 mechanisms 的 source_doi/source
- 分类为：lotus-specific / shared-wetting / generic-review / off-topic
- 统计各类数量
- 提出 scope split 建议方案
产出：
eview-clcode-task10-lotus-scope-assessment.md

### 执行约束（同前）
- 最多 3 个并行子智能体
- 文本任务用 mimo-v2.5-pro
- 修改 JSON 前先 dry-run
- 不改 build_prototypes_db.py
- 每个任务产出 review-clcode-*.md 报告


## 第四轮任务（2026-06-17 第四轮）

家里 Codex 对账发现了几个需要修复的问题，同时进入逐原型验证升级阶段。

### Task 11: 对账修复（Codex 发现的问题）
参考 `docs/archive/optimization-v1-2026-06/evidence-reports/review-post-office-reconciliation.md`：

1. **B03-CHL-001 清除**：chlorella-cell-wall 的 mechanisms[0]（Cheng2021 Pb2+ 作为染料去除机制）仍在 JSON 中，需要移除
2. **Biomineralization scope review**：mechanisms[0] 的文字过于宽泛（"有机模板控制无机晶体生长方向/形态"），Wang2025 实际只支持 LanM@ZIF-8 稀土吸附。需要缩窄 mechanism 文字或标注 scope caveat
3. **CN114887602A 恢复**：PDF 不在当前 worktree 但在 Git object 中（`9ee5da0`）。从 Git 提取到 `仿生文献库/专利/` 路径，然后更新 PDA performance_data 的 source_file

### Task 12: 验证升级 - 第 1 批原型（优先级最高）
目标：给存活机制和性能行添加 quote + locator，从 `needs_review` / `unverified` 升级为 `partial` 或 `corroborated`。

按优先级处理以下原型（证据最充分、PDF 最齐全）：
1. **fish-scale-hydroxyapatite** - CN114849640A 是核心源，给 perf[7-17] 添加专利段落 locator
2. **bone-structure** - Bambaeero2020, 给 mechanisms[0-3] 和 perf[0-1] 添加 quote+locator
3. **oyster-shell** - Qiu2021/Xu2022, 给 perf[0-5] 添加 quote+locator
4. **plant-tannin** - Mao2024/Tan2023, 给 mechanisms[6-10] 和 perf[0-5] 添加 quote+locator

每个原型的验证步骤：
- 读取对应 PDF 的本地文本（或 extraction JSON）
- 为每个 mechanism/performance 行找到源文本中的确切引文
- 写入 `verification_quote`（真实文本摘录，非标题）和 `source_page` / `source_locator`
- 将 `verification` 从 `needs_review`/`unverified` 改为 `partial`（有 quote 但单源）或 `corroborated`（多源支持）

### Task 13: 验证升级 - 第 2 批原型
1. **silk-fibroin** - 补充 Task 5 清理的引文，从 PDF 提取真实摘录
2. **wood-xylem** - Kumar2021/Mo2021, 给 mechanisms[0] 和 perf[0-1] 添加引文
3. **scallop-shell** - Wang2024, 给 mechanisms[0] 和 perf[0-6] 添加引文
4. **iron-oxidizing-bacteria** - Luo2021, 给 perf[0-6] 添加引文（Task 5 标记 IOB 需要 deeper work）

### 执行约束
- 最多 3 个并行子智能体
- 用 mimo-v2.5-pro（纯文本任务）
- 修改 JSON 前先 dry-run
- 不改 build_prototypes_db.py
- 每个任务产出 review-clcode-*.md 报告


## 第五轮任务（2026-06-17 第五轮）

Yao 已完成 7 批人工审批（91 项 pending_yao），需要执行所有已审批决策。

### Task 14: Decision Queue 全量状态更新（最高优先级）
参考 `docs/registries/decision-queue.md`

将以下已审批项从 `pending_yao` 更新为对应状态：

**机械性操作（Batch 1, 12项）→ applied_mechanical_fix**
F01-PLT-003, F02-BONE-002, F02-BMT-002, F03-CMIC-003, F04-SHART-001, F11-FISH-001, F01-WOOD-003, F02-FISH-006, F03-SRB-002, F03-MYC-002, F02-SCAL-001, F08-DNA-002

**Enrichment 占位符（Batch 2, 3项）→ acknowledged_placeholder**
F01-CHI-002, F01-WOOD-005, F01-CHI-003

**Keep-Soft（Batch 3, 14项）→ applied_keep_soft**
F01-WOOD-006, F02-OYS-004, F02-SCAL-002, F02-SCAL-003, F02-FISH-003, F03-CHL-002, F03-CHL-004, F04-CACT-001, F04-SHART-003, F05-ALG-003, F05-CNC-002, F05-CNC-003, F14-B08-004, F14-B08-005

**Scope 决策（Batch 4, 8项）**
F04-LOTUS-001 → applied_scope_B (lotus+wetting=56条)
F05-CNC-001 → applied_scope_B (broad_cellulose_family)
F03-CMIC-002 → applied_scope_A (metric_type分离)
F02-BMT-003 → applied_scope_B (broad+scope_caveat)
F05-STARCH-001 → applied_scope_A (needs_review标记)
F12-PDA-MU-003 → applied_scope_A (composite caveat)
F14-B08-004 → applied_scope_A (scope caveat) [注意：已在Batch3中出现]
F03-CHL-002 → applied_scope_A (algal-biochar) [注意：已在Batch3中出现]

**OCR/扫描（Batch 5a）**
F01-PDA-003 → knowledge_gap_ocr_pending (mimo-v2.5待办)
F02-FISH-005 → knowledge_gap_ocr_pending (mimo-v2.5待办)
F03-IOB-002 → applied_removed
F11-FISH-004 → applied_removed
F13-PDA-OCR-002 → human_verified_keep (人工确认~38 mg/g正确)

**极端值（Batch 5b）**
F01-PLT-005 → applied_keep_caveat (3429 mg/g保留)
F05-STARCH-002 → applied_demote (不参与排名)
F10-STARCH-005 → applied_keep_material_caveat (cryogel保留)
F10-STARCH-006 → hold_pending_primary_source (2000 mg/g待验证)
F13-PDA-OCR-003 → applied_value_change_96_31 (改为96.31%)

**其他（Batch 5c）**
F01-PLT-004 → applied_keep_cross_domain
F07-MOF-003 → applied_keep_hybrid_caveat
F07-MOF-007 → applied_needs_review_patent
F07-REG-002 → applied_merged
F09-DIAT-006 → applied_removed

**Wrong Source（Batch 6）**
F01-PDA-002 → applied_removed (27条enrichment机制已移除)
F03-CHL-001 → applied_removed (Task 11已执行)

**Boundary（Batch 7）**
8项已写入JSON boundary_rules，状态更新为 applied_boundary_2026_06_17_batch2

### Task 15: Scope 决策执行 — Lotus-Leaf Split
Yao 决策 4-1=B：保留 32 条 lotus-specific + 24 条 wetting-theory = 56 条。

操作步骤：
1. 参考 `review-clcode-task10-lotus-scope-assessment.md` 的分类结果
2. 从 `prototypes_db/separation/lotus-leaf.json` 移除不属于 lotus-specific 和 wetting-theory 的 290 条 mechanisms
3. 同时评估 22 条 engineering_constraints 和 33 条 narrative_entries，移除明显非莲花特异的
4. 4 条 performance_data：[0-2] 标记 knowledge_gap（PDF缺失），[3] 标记 scope_mismatch（scallop-shell）
5. 添加 scope_note：保留 lotus-specific + wetting-theory，其余已移除/重分配

### Task 16: PDA OCR 值修正
F13-PDA-OCR-003：将 `polydopamine-coating.json` performance_data[19] 的值从 95.68% 改为 96.31%（人工确认 OCR 摘要最佳条件值）。

### 执行约束
- 最多 3 个并行子智能体
- 用 mimo-v2.5-pro（纯文本任务）
- 修改 JSON 前先 dry-run
- 不改 build_prototypes_db.py
- 每个任务产出 review-clcode-*.md 报告

### 待办备忘（不在本轮执行）
- mimo-v2.5 OCR 待办：CN113244898A (PDA Pb), CN114570339A (PDA U), CN113275374A (fish-scale Cd/Pb)
- Abu2023 Pb2+ 2000 mg/g 需要 primary source 交叉验证


## 第六轮任务（2026-06-17 第六轮 — 大批量）

Yao 已审批全部 7 批人工决策。本轮执行所有剩余的 JSON 修改、验证升级和收尾工作。

### Task 17: Scope Caveats 和 Metadata 批量写入
将以下已审批决策写入对应 JSON 文件：

**Keep-Soft caveats（Batch 3, 14项）：**
- chitosan.json: enrichment causal_chain 标注 `enrichment_placeholder`
- wood-xylem.json: Kumar2021 行添加 applicability_note "biomass biochar, not preserved xylem-channel"
- oyster-shell.json: Zhang2024/Zhang2021 行添加 scope_caveat "generic shell review, not oyster-specific"
- scallop-shell.json: 添加 scope_caveat "generic modified-shell review"
- fish-scale-hydroxyapatite.json: Wu2022 行添加 scope_caveat "rice-husk HAp biochar, not fish-scale"
- chlorella-cell-wall.json: Peng2022 行标注 evidence_type "algal-derived-biochar"; generic algae 行标注 "general-algae-background"
- cactus-spine.json: 添加 scope_caveat "mixes cactus/desert-beetle/honeycomb/fog-harvesting evidence"
- superhydrophobic-artificial.json: Li2022 行标注 "fluoropolymer membrane background"
- alginate.json: chitosan-alginate 行标注 "composite material"
- cellulose-nanocrystal.json: CN121130847A 行标注 "bio-foam"; Radjai2022 行标注 "cellulose-diatomite composite"
- pitcher-plant-slippery-surface.json: 添加 scope_note "surface engineering prototype, not adsorption"
- spider-silk.json: 添加 scope_caveat "31 mechanisms include broad superhydrophobic/femtosecond-laser spillover"

**Scope 决策写入（Batch 4）：**
- cellulose-nanocrystal.json: provenance_summary 添加 scope "broad_cellulose_family"
- cell-membrane-ion-channel.json: 给所有 performance_data 行添加 metric_type 字段（区分 adsorption_qmax / rejection_rate / permeance）
- starch-granule.json: 所有 121 个 performance_data 行的 verification 确保标记为 needs_review（不是 unverified）

**值修正（Batch 5）：**
- plant-tannin.json perf[11]: 添加 caveat "3429.23 mg/g physically unusual, verify experimental conditions"
- starch-granule.json: 对 perf[52-59] Ihsanullah2022 行添加 metric_type "concentration_dependent_uptake"（非 Langmuir qmax）
- starch-granule.json perf[66-77]: Khoo2023 review 行添加 source_type "review_maximum"
- starch-granule.json perf[73]: 添加 material_class "engineered_superhydrophobic_cryogel"
- polydopamine-coating.json: Yuan2024 行添加 material_class "CNF-TA-PMMT-PEI_composite"

**机械性 Metadata 添加（Batch 1, 需要实际写入 JSON）：**
- bone-structure.json: mechanisms[0-3] 和 perf[0-1] 添加 Bambaeero2020 的 source_file 和 locator（如果 Task 12 已有引文则跳过）
- biomineralization-template.json: 添加 Wang2025 Nd3+ 787.93 mg/g 的 performance_data 行
- dna-aptamer.json: mechanisms[0].source 从 llm_inference 改为 literature-backed（如果已有 scope_note 则跳过）

### Task 18: Lotus-Leaf 收尾清理
Task 15 已将 mechanisms 从 346 减至 49，但 engineering_constraints 和 narrative 未清理。

1. 评估 22 条 engineering_constraints：保留与 lotus-specific 或 wetting-theory 相关的，移除非莲花特异的
2. 评估 33 条 narrative_entries：同上，保留莲花和润湿理论相关的
3. 参考 review-clcode-task15-lotus-scope-split.md 和 review-clcode-task10-lotus-scope-assessment.md

### Task 19: 验证升级 — 第 3 批（高优先级原型）
给以下 4 个原型添加真实 PDF 引文（verification_quote + source_locator）：

1. **chitosan** — 117 条 performance_data，核心源包括 Bambaeero2020（已部分处理）、CN114849640A 等。重点给 top-10 高 qmax 行添加引文
2. **mussel-foot-adhesion** — PDA 重叠行已有，重点给 biological adhesion 行添加引文
3. **polydopamine-coating** — CN114887602A 已恢复，给 P 吸附行添加引文
4. **diatom-frustule** — 去重后给存活行添加 Du2021/Guo2022/Qin2024 引文

### Task 20: 验证升级 — 第 4 批（中优先级原型）
1. **sulfate-reducing-bacteria** — Kumar2020 机制引文补充，添加 performance_data 行（如有 PDF 支持）
2. **mycelium** — Liu2021 真菌生物吸附引文补充
3. **mangrove-root** — 系统级证据，标注 metric_type "system_removal_percentage"
4. **dna-aptamer** — Bilibana2022 RNA-GO MC-LR 吸附添加为 low-confidence performance_data

### Task 21: 验证升级 — 第 5 批（低优先级/特殊原型）
1. **shark-skin** — 零性能行，添加 scope_note "background-only, no direct performance"
2. **water-strider-leg** — 零性能行，同上
3. **cactus-spine** — 零性能行，标注 scope contamination
4. **coral-skeleton** — 零性能行，标注 "placeholder, no coral/CaCO3 adsorption source"
5. **magnetic-bacteria** — 零性能行，标注 "review-level ecological source"
6. **lobster-exoskeleton** — Vo2023 PDF 缺失，标注 knowledge_gap

### Task 22: OCR 扫描专利处理（使用 mimo-v2.5 多模态模型）
**重要：本任务需要切换到 mimo-v2.5 模型处理 PDF 图片/扫描件。**

1. **CN113244898A**（polydopamine-coating.json perf[17-19]）：
   - 文件：`仿生文献库/3rd/第三波-仿生吸附专利/2022-CN113244898A-polydopamine-Pb-adsorbent.pdf`
   - 提取：Pb(II) 吸附容量、pH 影响、最佳条件去除率
   - 特别关注：perf[19] 已改为 96.31%，验证其他行

2. **CN114570339A**（polydopamine-coating.json perf[26-32]）：
   - 文件：`仿生文献库/3rd/第三波-仿生吸附专利/2022-CN114570339A-polydopamine-uranium-adsorbent.pdf`
   - 提取：U(VI) 吸附容量、pH 影响图、选择性数据
   - 特别关注：perf[30] H-PDA-SO pH6 (~38 mg/g 已人工确认), perf[32] U ~8.2 mg/g（选择性图值）

3. **CN113275374A**（fish-scale-hydroxyapatite.json perf[18-21]）：
   - 文件：查找本地路径（可能在 仿生文献库/ 下，20MB 扫描专利）
   - 提取：Cd/Pb 混合细菌+HAp MICP 去除值
   - 注意：此专利已决策为移除（F03-IOB-002, F11-FISH-004），仅在移除决策未执行时提取

### Task 23: 校验脚本全跑和修复
运行以下校验脚本，记录结果：

```
python -X utf8 tools/validate_consistency.py
python -X utf8 tools/check_chimera.py
python -X utf8 tools/check_causal_chain.py
python -X utf8 tools/check_boundary_guardrail.py
python -X utf8 tools/check_translation_specificity.py
```

对发现的 error（非 warning）：
- 如果是本批次引入的：修复
- 如果是预存的：记录到报告中，不修复

### Task 24: 交付准备
为 v0.1-alpha 交付准备：

1. 运行 `python -X utf8 tools/build_prototypes_db.py`（如果存在），生成构建产物
2. 如果 build 脚本不存在或报错，记录错误
3. 统计最终数据摘要：原型数、机制数、性能行数、验证覆盖率、boundary rules 数
4. 生成 `review-v0.1-delivery-summary.md` 包含：
   - 数据规模统计
   - 验证覆盖率
   - 已知局限（pending_yao 残留项、missing PDF、OCR 待办）
   - 后续版本计划

### 执行约束
- 最多 3 个并行子智能体
- 文本任务用 mimo-v2.5-pro
- **Task 22 强制使用 mimo-v2.5（多模态）**
- 修改 JSON 前先 dry-run
- 不改 build_prototypes_db.py（如果运行报错就记录）
- 每个任务产出 review-clcode-*.md 报告

### 待办备忘（不在本轮执行）
- Abu2023 Pb2+ 2000 mg/g 需要 primary source 交叉验证（需要下载原始论文）
- Dong2025 alginate review PDF 获取
