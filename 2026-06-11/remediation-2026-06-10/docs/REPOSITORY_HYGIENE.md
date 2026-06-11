# 仓库治理规范

> 本库是 ADRMATS 的仿生启发检索模块
> 最后更新：2026-06-08

---

## 1. 分支策略

### 1.1 当前分支结构

| 分支 | 用途 |
|------|------|
| `main` | 稳定发布分支 |
| `release/v1.1` | **v1.1 交付分支** |
| `feature/extraction-results` | 开发分支 |

**当前工作流**：`feature/extraction-results` → merge → `release/v1.1` → PR → `main`

**未来可引入**：`develop` 分支用于日常集成，但当前以 feature → release → main 为准。

### 1.2 分支规则

- 禁止直接向 main 推送，所有变更必须通过 PR
- feature 分支命名：`feature/功能描述`
- release 分支命名：`release/vX.Y`
- PR 合入后删除远程 feature 分支

### 1.3 版本号规则

采用语义化版本 `vX.Y.Z`：
- X（主版本）：schema 结构变更
- Y（次版本）：新增原型、新增映射数据
- Z（修订版本）：数据修正、bug 修复

---

## 2. 目录结构规范

### 2.1 正式交付物（必须保留）

```
Biomimetic-design-library/
├── README.md                      # 项目介绍
├── .gitignore
├── .gitmodules
│
├── feature-mapping.json           # 四层映射
├── feature_matching_rules.json    # 分子特征匹配规则
├── pollutant_aliases.json         # 污染物名称归一化表
├── pollutant_profiles.json        # 污染物分子特征画像
│
├── prototypes_db/                 # 正典数据（JSON）
├── prototypes/                    # 渲染产物（prototype.md）
│
├── docs/                          # 项目文档
│   ├── design.md                  # 设计规范
│   ├── ADRMATS_DELIVERY_PLAN.md   # 交付计划
│   ├── ADRMATS_CALL_GUIDE.md      # 调用说明
│   ├── ADRMATS_INTEGRATION.md     # 分层检索策略
│   ├── SUPPORT_SCOPE_AND_RISKS.md # 支持范围与风险
│   ├── REPOSITORY_HYGIENE.md      # 仓库治理规范
│   └── archive/                   # 归档文档（过程文件、评估报告）

**docs/ 允许的 md 文件**：
- design.md
- ADRMATS_DELIVERY_PLAN.md
- ADRMATS_CALL_GUIDE.md
- ADRMATS_INTEGRATION.md
- SUPPORT_SCOPE_AND_RISKS.md
- REPOSITORY_HYGIENE.md

**docs/ 不允许的文件**：
- 过程文件（AI_*.md, HANDOFF.md 等）→ 移到 docs/archive/
- 评估报告（*_evaluation.md）→ 移到 docs/archive/
- 临时指令（任务布置_*.md 等）→ 移到 docs/archive/
│
├── examples/                      # 真实接口输出示例
│   └── adrmats_briefs/
│
├── templates/                     # 模板
├── taxonomy/                      # 分类体系
└── tools/                         # 工具脚本
```

### 2.2 过程文件（不应长期保留）

| 文件 | 用途 | 处理方式 |
|------|------|----------|
| `AI_AGENT_PROGRESS.md` | AI 执行状态 | 任务完成后归档或删除 |
| `AI_SUPERVISOR_DIRECTIVE.md` | 监督指令 | 任务完成后归档或删除 |
| `AI_COORDINATION_PROTOCOL.md` | 协作协议 | 任务完成后归档或删除 |
| `HANDOFF.md` | 交接指针 | 归档 |
| `SESSION-CONTEXT.md` | 会话上下文 | 归档 |
| `REVIEW-GUIDE.md` | 审查指南 | 归档 |
| `*_evaluation.md` | 评估报告 | 归档 |
| `quality-audit-*.md` | 质量审计 | 归档 |
| `任务布置_*.md` | 执行指令 | 归档 |
| `分层核查标准_*.md` | 核查标准 | 归档 |

### 2.3 根目录文件限制

根目录只允许：
- `README.md`
- `.gitignore`
- `.gitmodules`
- `feature-mapping.json`
- `feature_matching_rules.json`
- `pollutant_aliases.json`
- `pollutant_profiles.json`

禁止在根目录放置：
- 任何 `.md` 评估/审计/指令文件
- 任何 brief JSON 测试文件
- 任何 `*_evaluation.md`
- 任何 `*_brief_*.json`

---

## 3. 文件准入规则

### 3.1 禁止提交的文件类型

| 类型 | 示例 | 理由 |
|------|------|------|
| AI 协作过程文件 | `AI_*.md` | AI Agent 间通信状态 |
| 评分表/评估报告 | `*_evaluation.md` | 过程验证产物 |
| 质量审计报告 | `quality-audit-*.md` | 一次性审计产物 |
| 交接指针文件 | `HANDOFF.md` | 一次性交接产物 |
| 手写 brief JSON | `*_brief_*.json`（根目录） | 冒充接口产物 |
| 执行指令文件 | `任务布置_*.md` | AI 执行指令 |
| 编译缓存 | `__pycache__/`、`*.pyc` | 应加入 .gitignore |
| 本地配置 | `.env`、`*.local` | 应加入 .gitignore |
| PDF/大型二进制文件 | 文献 PDF | 使用外部存储 |

### 3.2 判断原则

1. 这个文件是项目使用者需要的吗？
2. 这个文件的信息是否已经被其他文件覆盖？
3. 三个月后这个文件还有价值吗？

### 3.3 重复文件规则

- 不允许同一内容出现在两个路径
- 旧版本文件必须删除，用 git 历史追溯

---

## 4. 验证命令

### 4.1 ADRMATS 验收命令

```bash
# 完整验收
python -X utf8 tools/verify_adrmats_delivery.py

# 校验一致性
python -X utf8 tools/validate_consistency.py

# 检查 chimera
python -X utf8 tools/check_chimera.py

# 检查仓库治理
python -X utf8 tools/check_repo_hygiene.py
```

### 4.2 验收标准

- `verify_adrmats_delivery.py`：6/6 通过
- `validate_consistency.py`：0 error
- `check_chimera.py`：0 violation
- `check_repo_hygiene.py`：0 issue

---

## 5. Commit 规范

### 5.1 Commit 消息格式

```
type: 简要描述

详细说明（可选）
```

type 取值：
- `feat`：新功能、新原型、新数据
- `fix`：修复 bug、修正数据
- `docs`：文档变更
- `refactor`：代码重构
- `chore`：清理、整理、格式调整
- `test`：测试相关

### 5.2 Commit 规则

- 一个 commit 只做一件事
- 提交前必须跑验证
- 提交前检查文件位置

---

## 6. 数据质量规则

### 6.1 原型数据

- `prototypes_db/*.json` 是唯一的正典数据源
- 每个原型 JSON 必须有完整的元信息
- organism 字段必须是真实生物来源，不允许 chimera
- 每条 performance_data 必须标注 verification 字段

### 6.2 污染物命名

- 使用 `pollutant_aliases.json` 中定义的 canonical name
- 重金属用 `元素(价态)` 如 `Pb(II)`
- 禁止使用 Unicode 上标如 `Pb²⁺`

### 6.3 Brief 数据

- `examples/adrmats_briefs/` 中只存放真实接口输出
- 禁止手写 JSON 冒充接口产物

---

## 7. 禁止操作清单

1. 禁止直接推送到 main 分支
2. 禁止在根目录创建评估报告、审计文件
3. 禁止创建 README 的变体文件
4. 禁止保留已被取代的旧版文件
5. 禁止手写 brief JSON 冒充接口产物
6. 禁止提交 __pycache__、.pyc、.env
7. 禁止在 commit 中包含 PDF 或大型二进制文件
8. 禁止在文档中维护矛盾的状态数字
9. 禁止 force push 到任何公共分支

---

*本文件是仓库治理的唯一规范。*
