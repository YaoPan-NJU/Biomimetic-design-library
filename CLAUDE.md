# Biomimetic Design Library — Claude Code Project Guide

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
| `docs\optimization-v1\` | 审计文档、决策队列、worklog |

## 当前工作阶段

**全量证据审计（Full Evidence Audit）** — Batch 09 已完成，等待 Yao 审批决策队列。

### 执行模型

- **OpenClaw / Claude Code**：批量 PDF 证据验证、路径规范化、OCR、草稿批次输出
- **Codex / Qoder**：范围控制、验收抽查、决策队列/边界寄存器维护、worklog、GitHub checkpoint
- **Yao**：最终审批决策

### 硬性限制

1. **不要修改 `prototypes_db/*.json`** — 除非 Yao 已审批对应决策队列项
2. **不要运行 `tools/build_prototypes_db.py`** — 审计期间不构建
3. **不要升级 `verification`、`hard_do_not`、`soft_boundary` 状态** — 需 Yao 审批
4. **不要提交 git** — 除非明确要求
5. 缺 PDF、扫描专利、OCR 不确定、LLM 推断内容 → 标为 `missing_pdf` / `needs_human_decision` / `knowledge_gap` / `inferred_only`
6. 只有明确来源错配或直接文献支持的边界 → 才可建议 `wrong_source` 或 `hard_do_not`

### 审计批次输出规范

每个批次输出一个 Markdown 文件到 `docs\optimization-v1\`，命名：`review-full-audit-openclaw-batch-XX-<scope>.md`

每项必须包含：`prototype_id`、`target_json`、`field_path`、`claim_summary`、`local source_file` 或 `missing_pdf`、`locator`、`quote`、`evidence_label`、`recommended_action`、`notes`

### 文献库路径注意

- 家里 macOS 路径格式：`/Users/panyao/Desktop/Biomimetic-design-library/仿生文献库/...`
- 办公室 Windows 路径格式：`C:\Users\15995\Desktop\Biomimetic-design-library\仿生文献库\...`
- JSON 中 `source_file` 字段存储的是相对路径或家里绝对路径，批量操作时需注意路径适配
- PDF 文件名中的空格和中文字符是正常的，不要修改文件名

## 决策队列

`docs\optimization-v1\review-full-audit-decision-queue.md` — 所有待审批项

`docs\optimization-v1\review-boundary-do-not-register.md` — 边界/DO-NOT 寄存器

`docs\optimization-v1\review-full-audit-worklog.md` — 工作日志

`docs\optimization-v1\review-sync-summary.md` — 同步摘要（最新状态）

## 协调协议

`docs\optimization-v1\review-openclaw-coordination.md` — 角色分工和输出规范

`docs\optimization-v1\review-openclaw-worker-prompts.md` — worker prompt 模板

`docs\optimization-v1\review-openclaw-next-tasks.md` — 下一批任务

## 协作协议（必读）

**每次启动时，先读以下文件：**
1. docs/optimization-v1/COLLABORATION-PROTOCOL.md  角色、权限、决策层级、工作流
2. docs/optimization-v1/COLLAB-BOARD.md  当前任务板（你的任务在这里）
3. docs/optimization-v1/COLLAB-HANDOFF.md  最近一次交接状态

**工作循环：**
- 读取 BOARD.md 中 status=assigned 且 assigned_to=clcode 的任务
- 执行任务，产出 review-clcode-*.md
- 更新 BOARD.md 中对应任务的 status=done
- 追加一条记录到 HANDOFF.md
- 如果所有任务完成，检查是否还有 enrichment/path 类任务可自主推进


## 模型选择规则

- **默认模型 mimo-v2.5-pro**：文本任务（Task 1-3），包括 JSON 对比、PDF 文本提取、路径核查
- **多模态模型 mimo-v2.5**：需要读取图片时使用（Task 4 专利 OCR、visual_cache.json 中的截图验证）
- 切换到 mimo-v2.5 的时机：当需要查看 visual_cache 截图、扫描版专利图片、或 figure-estimated values 时
- ultracode 模式下可为不同子智能体分配不同模型：文本审计用 mimo-v2.5-pro，多模态子任务用 mimo-v2.5

## 并发限制

- **最多 3 个并行子智能体**，共享同一个 API key，超出会触发 429 限流
- 之前的 OpenClaw 在 Batch 01 同时启动 5 个 worker 导致大面积 429 错误，引以为戒
- 建议策略：1-2 个并行 + 1 个串行验收

## 当前任务（Qoder 分配  2026-06-17）

### 任务 1：Enrichment Mirror Gap Fill（最高优先级）
- 525/525 enrichment causal_chain 字段为空
- 4 个 enrichment 文件为空 {}（biomineralization-template, coral-skeleton, dna-aptamer, magnetic-bacteria）
- 对照主 JSON 和源 PDF，为已验证的 mechanism 填充 causal_chain
- **不要**机械同步；只从 source-backed 的主 JSON mechanism 中提取
- 输出文件：docs/optimization-v1/review-clcode-enrichment-audit.md

### 任务 2：Missing PDF 路径验证
- chitosan.json: 99 个 missing_pdf 项  检查路径是否有  2.pdf/ 3.pdf 后缀变体
- 产出可操作的路径映射表
- 输出文件：docs/optimization-v1/review-clcode-missing-pdf-paths.md

### 任务 3：Wrong-Source 二次验证
- lotus-leaf.json：355 个 mechanisms 按实际生物来源分组
- cellulose-nanocrystal.json：按材料类型分组（CNC/CNF/通用纤维素/复合材料）
- 输出文件：docs/optimization-v1/review-clcode-wrong-source-deep.md

### 任务 4：Patent OCR 辅助
- 对扫描版专利的 visual_cache.json 做文本提取
- 验证 decision queue 中标记的 figure-estimated values

### 协作方式
- Qoder 会通过写文件或对话分配任务
- 完成后产出审计文件到 docs/optimization-v1/review-clcode-*.md
- Qoder 会 spot-check 后决定是否 accept
- 有歧义标记 
eeds_qoder_review，不要自行决定


## 下一批任务（2026-06-17 第二轮）

Qoder 已完成第一层 wrong-source 清除、Scope 决策、边界规则写入。以下是你的新任务：

### Task 5: Metadata Fix Batch（25 项）
参考 docs/optimization-v1/review-clcode-task1-decision-queue-summary.md Category D 列表：
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
参考：docs/optimization-v1/review-full-audit-decision-queue.md

### 执行约束
- 最多 3 个并行子智能体
- 文本任务用 mimo-v2.5-pro，多模态用 mimo-v2.5
- 修改 JSON 前先 dry-run
- 不改 build_prototypes_db.py
- 产出 review-clcode-*.md 报告后结束


## 第三轮任务（2026-06-17 第三轮）

### Task 8: Path Normalization Sweep（最高优先级）
参考 docs/optimization-v1/review-clcode-task3-missing-pdf-analysis.md：
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
- docs/optimization-v1/review-full-audit-decision-queue.md
- docs/optimization-v1/review-boundary-do-not-register.md（已标记 guard_rule 的 14 项）

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
参考 `docs/optimization-v1/review-post-office-reconciliation.md`：

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
