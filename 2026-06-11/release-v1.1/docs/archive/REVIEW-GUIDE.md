# 第三方审查指南

> 本文件为外部审查 AI 准备，提供项目全貌和审查入口。

## ⚠️ 重要：本项目由两个仓库组成

| 仓库 | 分支 | 内容 |
|------|------|------|
| **[Biomimetic-design-library](https://github.com/YaoPan-NJU/Biomimetic-design-library/tree/feature/extraction-results)** | `feature/extraction-results` | 仿生设计库（原型、映射、校验、审计） |
| **[Literature-extracting](https://github.com/YaoPan-NJU/Literature-extracting/tree/feature/biomimetic-extraction)** | `feature/biomimetic-extraction` | 提参工具 LitExtract（提示词、脚本、提取结果 JSON） |

**必须两个仓库都读**，否则会缺失：
- 提参提示词（v1/v2）— 理解"怎么提取的"
- 315 个提取结果 JSON — 原始数据
- 提参脚本（preprocess.py、multi_worker_extract.sh 等）— 理解工程实现
- Schema 定义 — 理解数据结构

`Biomimetic-design-library` 的 `tools/litextract/` 是 Literature-extracting 的 git submodule 引用。

## 审查目标

对 Biomimetic-design-library 项目的**数据质量、架构设计、工程规范**进行全面审查，给出改进建议。

## 推荐阅读顺序

### 1. 项目概览（5 min）

| 文件 | 内容 |
|------|------|
| `README.md` | 项目简介、架构、三层匹配机制 |
| `SESSION-CONTEXT.md` | 当前状态总览（提参进度、原型进度、待办任务） |

### 1.5 提参工具与提示词（Literature-extracting 仓库）（15 min）⭐

在 [Literature-extracting](https://github.com/YaoPan-NJU/Literature-extracting/tree/feature/biomimetic-extraction) 仓库中阅读：

| 文件 | 内容 |
|------|------|
| `prompts/biomimetic_extraction_prompt.md` | v1 提示词（基础版，330 行） |
| `prompts/biomimetic_extraction_prompt_v2.md` | v2 提示词（含仿生元数据、专利/标准策略，625 行）⭐ |
| `schema/` | JSON Schema 定义（biomimetic-v1、biomimetic-v2） |
| `scripts/preprocess.py` | PDF 预处理（多模态提取文本+表格） |
| `scripts/multi_worker_extract.sh` | 多路并发提取脚本（支持 1/2/3 路） |
| `outputs/extractions/论文/json/` | 275 个论文提取结果 |
| `outputs/extractions/专利/json/` | 37 个专利提取结果 |
| `outputs/extractions/标准/json/` | 3 个标准提取结果 |

**v2 提示词是核心**，它定义了：
- Step 1-3：基础提取（knowledge_items、source、evidence）
- Step 4：仿生元数据提取（prototype_targets、biomimetic_metadata、biomimetic_narrative）
- 专利/标准专项策略（patent_number、standard_number）
- evidence 质量分级规则（reliable/needs_review/suspicious/unavailable）

### 2. 设计与架构（10 min）

| 文件 | 内容 |
|------|------|
| `docs/design.md` | 详细设计文档 |
| `feature-mapping.json` | 核心数据：四层映射结构（pollutant→prototype, feature→prototype, metadata, mechanism bridge） |
| `templates/prototype-template.md` | 原型条目的标准格式（YAML frontmatter + 6 个标准章节） |

### 3. 质量审计报告（10 min）⭐ 关键文件

| 文件 | 内容 |
|------|------|
| `quality-audit-2026-06-07.md` | 另一个 AI 做的全面质量审计，发现 3 个严重 bug + 多个数据完整性问题 |

**这份报告是审查的核心输入**，它详细列出了：
- 桥接管道 3 个严重 bug（ID 分裂、模板忽略、数据覆盖）
- 42 个原型中 0 个满足质量基线
- 6 对完全重复的原型
- 14 个专利缺 patent_number
- 校验脚本仅实现 1.5/6 条规则

### 4. 桥接管道代码（15 min）⭐ 需要审查的代码

| 文件 | 行数 | 职责 | 已知问题 |
|------|------|------|----------|
| `tools/litextract/scripts/map_to_prototypes.py` | 239 | JSON→原型映射 | ID 分裂 bug、递归扫描 backup 目录 |
| `tools/litextract/scripts/aggregate_per_prototype.py` | 166 | 聚合 knowledge_items | dict.update() 覆盖数据、关键词过宽 |
| `tools/litextract/scripts/generate_prototype_md.py` | 221 | 渲染 prototype.md | 完全忽略模板、无 YAML frontmatter |
| `tools/validate_consistency.py` | 180 | 校验一致性 | 仅实现 1.5/6 条规则 |

### 5. 提取结果样本（10 min）

| 路径 | 数量 | 说明 |
|------|------|------|
| `tools/litextract/outputs/extractions/论文/json/` | 275 | 论文提取结果（v1 schema，质量扎实） |
| `tools/litextract/outputs/extractions/专利/json/` | 37 | 专利提取结果（v1/v2 混合，4 个重复） |
| `tools/litextract/outputs/extractions/标准/json/` | 3 | 标准提取结果（1 个失败） |

建议抽查 2-3 个 JSON 看 knowledge_items 结构。

### 6. 原型产出样本（10 min）

| 路径 | 说明 |
|------|------|
| `prototypes/lotus-leaf/prototype.md` | 有实质内容（15KB） |
| `prototypes/metal-organic-framework/prototype.md` | 有实质内容（18KB），有重复副本 mof-adsorbent |
| `prototypes/dna-aptamer/prototype.md` | 占位符（341B，零数据） |
| `prototypes/polydopamine-coating/prototype.md` | 主题偏离（聚焦药物递送非水处理） |

### 7. 执行计划（5 min）

| 文件 | 内容 |
|------|------|
| `下一步执行计划_本地AI.md` | 完整任务清单（12 个任务，10 已完成 2 待启动） |

## 审查重点问题

请重点关注以下方面：

### 架构层面
1. 四层匹配机制（feature-mapping.json）的设计是否合理？
2. 桥接管道的三步流程（map→aggregate→generate）是否是最优方案？
3. 原型 ID 命名规范和映射策略是否可持续维护？

### 数据质量层面
1. 3 个严重 bug 的修复方案是否正确？
2. 42 个原型的基线标准是否合理？
3. 如何处理 v1/v2 schema 混合问题？

### 工程层面
1. 校验脚本应覆盖哪些规则？
2. 如何保证后续扩展到 100 个原型时的质量？
3. 与下游 ADRMATS 系统的接口是否清晰？

### 战略层面
1. 当前优先级排序（P0/P1/P2）是否合理？
2. 是否有遗漏的风险或依赖？
3. 从 42 扩展到 100 的路径是否可行？

## 分支说明

### Biomimetic-design-library

| 分支 | 内容 | 推荐 |
|------|------|------|
| `feature/extraction-results` | **最新**：42 个原型 + 桥接管道代码 + 审计报告 + 子模块引用 | ⭐ 主要审查对象 |
| `main` | 基础框架（taxonomy、template、feature-mapping） | 参考 |

### Literature-extracting

| 分支 | 内容 | 推荐 |
|------|------|------|
| `feature/biomimetic-extraction` | **最新**：提示词 v2 + 提参脚本 + 315 个 JSON + schema 定义 | ⭐ 必读 |
| `main` | LitExtract 框架基础代码 | 参考 |

**两个仓库的 `feature/*` 分支都需要审查。**

## 项目数据概览

```
提取结果：315 个 JSON（论文 275 + 专利 37 + 标准 3）
原型目录：42 个（6 对重复 = 实际 36 个唯一原型）
有实质内容：28 个
占位符：7 个
满足质量基线：0 个（verification=verified 全线缺失）
桥接管道 bug：3 个严重
校验规则：1.5/6 已实现
```

## 克隆与初始化

```bash
# 克隆仿生设计库
git clone -b feature/extraction-results https://github.com/YaoPan-NJU/Biomimetic-design-library.git
cd Biomimetic-design-library

# 初始化子模块（获取提参工具和提取结果）
git submodule init
git submodule update
```

子模块初始化后，`tools/litextract/` 目录将包含完整的提参工具代码和 315 个 JSON 提取结果。

## 相关仓库

| 仓库 | 分支 | 内容 |
|------|------|------|
| [Biomimetic-design-library](https://github.com/YaoPan-NJU/Biomimetic-design-library/tree/feature/extraction-results) | `feature/extraction-results` | 本项目（仿生设计库） |
| [Literature-extracting](https://github.com/YaoPan-NJU/Literature-extracting/tree/feature/biomimetic-extraction) | `feature/biomimetic-extraction` | 提参工具（LitExtract）— 提示词、脚本、提取结果 |

---

*本文件由 Claude Code 自动生成于 2026-06-07*
