# Biomimetic-design-library — AI 工作指令

> 本文档是给 AI Agent 的工作指令。任何 AI 在操作本仓库时，必须先阅读并遵守以下规则。
> 最后更新：2026-06-08

---

## 一、项目身份

**仓库名**：Biomimetic-design-library（生物原型知识库）

**定位**：水处理仿生吸附材料开发智能体系统（ADRMATS）的仿生启发检索基座。本库不是材料设计器，不是事实数据库，它的唯一职责是让每个原型都能干净、可溯源、标注诚实地供出 brief 三件套（匹配、机制、设计转译）。

**核心数据**：`prototypes_db/*.json` 是正典数据源（canonical source），`prototypes/*/prototype.md` 是渲染产物（从 JSON 生成）。`feature-mapping.json` 是四层映射结构的检索入口。

**关联仓库**：`Literature-extracting`（文献提取工具 LitExtract），通过 `.gitmodules` 以子模块形式挂载在 `tools/litextract`。

---

## 二、分支策略

### 2.1 分支定义

| 分支 | 用途 | 保护级别 |
|------|------|----------|
| `main` | 稳定发布分支，始终对应最新可用版本 | 受保护，仅接受 PR 合入 |
| `develop` | 日常开发集成分支 | 受保护，仅接受 PR 合入 |
| `feature/*` | 功能开发分支，从 develop 拉出，完成后 PR 回 develop | 自由操作 |
| `release/*` | 发布准备分支，从 develop 拉出，稳定后 PR 回 main 和 develop | 仅修 bug 和改文档 |
| `hotfix/*` | 紧急修复，从 main 拉出，修完 PR 回 main 和 develop | 仅限紧急修复 |

### 2.2 分支规则

- **禁止直接向 main 或 develop 推送**。所有变更必须通过 PR。
- **feature 分支命名规范**：`feature/功能描述`，如 `feature/pollutant-standardization`、`feature/golden-standard-validation`。
- **release 分支命名规范**：`release/vX.Y`，如 `release/v1.0`、`release/v2.0`。
- **feature 分支生命周期**：从 develop 创建 → 开发 → PR 回 develop → 删除 feature 分支。
- **不允许在 feature 分支之间互相合并**，它们应当独立。
- **清理**：PR 合入后，远程分支必须删除。本地分支用 `git branch -d` 清理。

### 2.3 版本号规则

采用语义化版本 `vX.Y.Z`：
- **X**（主版本）：schema 结构变更（如 brief 结构重定义、prototypes_db JSON schema 重构）
- **Y**（次版本）：新增原型、新增映射数据、新增功能
- **Z**（修订版本）：数据修正、bug 修复、文档更正

---

## 三、目录结构规范

### 3.1 允许的目录结构

```
Biomimetic-design-library/
├── README.md                      # 项目介绍（唯一版本，不接受 README-clean.md 等变体）
├── .gitignore
├── .gitmodules
│
├── feature-mapping.json           # 四层映射（核心检索数据）
├── feature_matching_rules.json    # 分子特征匹配规则
├── pollutant_aliases.json         # 污染物名称归一化表
├── pollutant_profiles.json        # 污染物分子特征画像
│
├── prototypes_db/                 # 正典数据（JSON，canonical source）
│   ├── {prototype-id}.json        # 每个原型一个 JSON
│   └── separation/                # 搁置的分离簇原型（如保留）
│       └── {prototype-id}.json
│
├── prototypes/                    # 渲染产物（由 prototypes_db 生成）
│   ├── {prototype-id}/
│   │   └── prototype.md
│   └── separation/                # 分离簇渲染
│       └── {prototype-id}/prototype.md
│
├── docs/                          # 项目文档
│   ├── design.md                  # 设计规范（含库定位、brief schema、schema 冻结策略）
│   ├── ADRMATS_DELIVERY_PLAN.md   # 交付计划与里程碑
│   ├── ADRMATS_INTEGRATION.md     # 分层检索策略与接口契约
│   └── context/                   # 跨设备协同文件（详见第五节）
│       └── SESSION-CONTEXT.md     # 唯一的跨会话状态文档
│
├── examples/                      # 真实接口输出示例
│   └── adrmats_briefs/
│       └── {pollutant}_{场景}.json
│
├── templates/
│   └── prototype-template.md      # 原型条目模板
│
├── taxonomy/                      # 分类体系
│   ├── organisms.md
│   ├── mechanisms.md
│   └── pollutants.md
│
└── tools/                         # 管线脚本与工具
    ├── biomimetic_context.py      # 核心接口
    ├── generate_prototype_md.py   # 渲染脚本
    ├── verify_data.py             # 数据验证
    ├── ...                        # 其他工具脚本
    └── litextract/                # 子模块（Literature-extracting）
```

### 3.2 根目录文件限制

根目录只允许以下文件：`README.md`、`.gitignore`、`.gitmodules`、`feature-mapping.json`、`feature_matching_rules.json`、`pollutant_aliases.json`、`pollutant_profiles.json`。

**禁止在根目录放置**：任何 `.md` 评估/审计/指令文件、任何 brief JSON 测试文件、任何 `*_evaluation.md`、任何 `*_brief_*.json`。

---

## 四、文件准入规则

### 4.1 禁止提交的文件类型

| 类型 | 示例 | 理由 |
|------|------|------|
| AI 协作过程文件 | `AI_AGENT_PROGRESS.md`、`AI_COORDINATION_PROTOCOL.md`、`AI_SUPERVISOR_DIRECTIVE.md` | AI Agent 间的通信状态，不是项目交付物 |
| 评分表/评估报告 | `*_evaluation.md`、`*_evaluation_v*.md`、`five_gold_standards_evaluation.md` | 过程验证产物，结论应写入 docs/ 的正式文档 |
| 质量审计报告 | `quality-audit-*.md` | 一次性审计产物，结论应整合进正式文档后删除 |
| 交接指针文件 | `HANDOFF.md`、`REVIEW-GUIDE.md` | 一次性交接产物，功能应由 docs/context/ 承担 |
| 手写 brief JSON | `*_brief_*.json`（根目录） | 冒充接口产物违反交付计划的禁止条款，真实输出应在 examples/ |
| 执行指令文件 | `任务布置_*.md`、`分层核查标准_*.md`、`下一步执行计划_*.md` | AI 执行指令，完成后结论应沉淀进正式文档 |
| 排障/诊断文档 | `路径映射修复指令.md`、`最新提取质量问题汇总.md` | 一次性排障产物 |
| 编译缓存 | `__pycache__/`、`*.pyc` | 应加入 .gitignore |
| 本地配置 | `.env`、`*.local` | 应加入 .gitignore |
| PDF/大型二进制文件 | 文献 PDF、图片 | 使用外部存储或子模块 |

### 4.2 判断原则

问自己三个问题：
1. **这个文件是项目使用者（人或程序）需要的吗？** 如果只是开发过程中的中间产物，不提交。
2. **这个文件的信息是否已经被其他文件覆盖？** 如果是，不提交。
3. **三个月后这个文件还有价值吗？** 如果不会，不提交。

### 4.3 重复文件规则

- **不允许同一内容出现在两个路径**。发现重复时必须选择一处保留，另一处删除。
- **不允许同一原型的两个不同版本共存于同级目录**。如 `prototypes/cactus-spine/` 和 `prototypes/separation/cactus-spine/` 不能同时存在（选一处）。
- **旧版本文件必须删除**，不用 `_v1`、`_old`、`_bak` 后缀保留。Git 历史就是版本记录。

---

## 五、跨设备协同文件规则

### 5.1 允许的协同文件

仓库中只允许存在 **一个** 跨设备协同文件：

```
docs/context/SESSION-CONTEXT.md
```

这个文件的作用是：当开发者（人或 AI）换设备继续工作时，提供项目当前状态的快速恢复。

### 5.2 SESSION-CONTEXT.md 的内容规范

该文件必须包含且仅包含以下节：

```
# 项目会话上下文
## 当前状态
- 分支、最新 commit
- prototypes_db 数量、performance_data 总数、verified 百分比
- 当前 milestone 进度
## 架构决策记录
- 关键设计决策及其理由（简洁版）
## 待办任务
- 未完成的工作项及其优先级
## 已知问题
- 当前未修复的数据/代码问题
## 关键文件索引
- 指向正式文档的路径（不重复内容）
## 恢复命令
- 检查仓库状态的 shell/python 命令
```

### 5.3 生命周期规则

- SESSION-CONTEXT.md **必须在每次重要 commit 后更新**（至少更新状态数字和待办项）。
- 文件中的数字必须与实际仓库数据一致。如果发现矛盾，以仓库实际数据为准，立即更新该文件。
- **禁止在仓库中保留 HANDOFF.md、README 状态面板等重复状态信息**。状态只维护在 SESSION-CONTEXT.md 一处。
- 任务布置、核查标准、评分卡等**已完成的指令文件**，其结论必须沉淀到 `docs/` 下的正式文档中，原文件移入 `docs/archive/` 或删除。

### 5.4 归档目录

`docs/archive/` 用于存放有历史参考价值但不再是活跃文档的文件：审查报告、历史核实记录、已完成的执行指令等。归档文件不再更新，仅供回溯。

---

## 六、Commit 规范

### 6.1 Commit 消息格式

```
@type: 简要描述

详细说明（可选）
```

type 取值：
- `@feat`：新功能、新原型、新数据
- `@fix`：修复 bug、修正数据
- `@docs`：文档变更
- `@refactor`：代码重构（不改变功能）
- `@chore`：清理、整理、格式调整
- `@test`：测试相关

### 6.2 Commit 规则

- **一个 commit 只做一件事**。不要把"修了 3 个 bug + 加了 2 个原型 + 整理了文档"塞进一个 commit。
- **提交前必须跑验证**（`tools/verify_data.py`），确保 0 校验错误。
- **提交前检查文件位置**：根目录不应有新增的非规定文件。
- **提交前检查重复**：确保没有引入内容重复的文件。
- **commit 消息用中文或英文均可**，但必须能让人一眼看懂改了什么。

---

## 七、数据质量规则

### 7.1 原型数据

- `prototypes_db/*.json` 是唯一的正典数据源。`prototypes/*/prototype.md` 必须从 JSON 生成，不允许手动编辑。
- 每个原型 JSON 必须有完整的 YAML 元信息：id、name_zh、name_en、organism、biomimetic_dimension、features。
- **organism 字段必须是该原型的真实生物来源**，不允许出现"嵌合体"（chimera）——即把多个不相关物种塞进一个原型。
- 每条 performance_data 必须标注 `verification` 字段（verified / corroborated / single_source / unverified / needs_review）。

### 7.2 污染物命名

- 使用 `pollutant_aliases.json` 中定义的 canonical name 作为标准名。
- 标准格式：重金属用 `元素(价态)` 如 `Pb(II)`、`Hg(II)`；有机物用标准缩写如 `PFOA`、`SMX`、`BPA`、`TC`。
- **禁止使用** Unicode 上标如 `Pb²⁺`、`Hg²⁺`。

### 7.3 Brief 数据

- `examples/adrmats_briefs/` 中只存放 `tools/biomimetic_context.py` 的真实接口输出。
- **禁止手写 JSON 冒充接口产物**。
- 每个 brief 文件命名格式：`{pollutant}_{应用场景}.json`。

---

## 八、README 维护规则

- 仓库只有一个 README.md，位于根目录。
- README 必须包含：项目简介（一段话）、目录结构说明、feature-mapping 四层结构简述、三层匹配机制说明、覆盖范围、使用方法、与 Literature-extracting 仓库的关系。
- README 中的数字（原型数量等）必须与实际数据一致。每次数据变更时同步更新。
- **不允许**在 README 中放置状态面板、commit hash、验证统计等易过期信息。这些信息只在 `docs/context/SESSION-CONTEXT.md` 中维护。
- **不允许**创建 README 的变体文件（如 README-clean.md、README-new.md、README-final.md）。

---

## 九、禁止操作清单

1. **禁止直接推送到 main 或 develop 分支**
2. **禁止在根目录创建评估报告、审计文件、AI 指令文档**
3. **禁止创建 README 的变体文件**
4. **禁止保留已被取代的旧版文件**（用 git 历史追溯，不用文件名后缀）
5. **禁止在同一层级存放同一原型的两个版本**
6. **禁止手写 brief JSON 冒充接口产物放入 examples/**
7. **禁止提交 __pycache__、.pyc、.env 等应被 gitignore 的文件**
8. **禁止在 commit 中包含 PDF 或大型二进制文件**
9. **禁止在文档中维护与其他文件矛盾的状态数字**
10. **禁止 force push 到任何公共分支**
