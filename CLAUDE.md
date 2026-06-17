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
