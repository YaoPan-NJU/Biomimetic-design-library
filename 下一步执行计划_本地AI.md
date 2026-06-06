# 项目下一步执行计划 v3（交本地 AI 执行 · 可直接处理原始文献）

> 适用项目：Biomimetic-design-library（生物原型知识库，ADRMATS 系统的仿生检索模块）
> 适用执行者：能直接读取本地原始文献（PDF）的 AI agent（OpenClaw / Claude Code）
> 编制日期：2026-06-06（v3 更新）

---

## 当前状态总览（2026-06-06 23:55）

### 提参进度

| 分类 | 总数 | 已提取 | 剩余 | 提示词版本 | 状态 |
|------|------|--------|------|-----------|------|
| 论文 | 302 | 296 | 6 | v2 ✅ | 2 路并发运行中 |
| 专利 | 33 | 33 | 0 | v1 ❌ | 需用 v2 重跑（无 biomimetic_metadata） |
| 标准 | 6 | 0 | 6 | v2 已优化 | 待重跑 |
| **总计** | **341** | **329** | **12** | | |

### Git 状态

| 仓库 | 分支 | 状态 |
|------|------|------|
| Biomimetic-design-library | `main` | 当前分支 |
| Biomimetic-design-library | `feature/extraction-results` | 刚创建，待提交 |
| Literature-extracting | `feature/biomimetic-extraction` | ✅ 已推送（代码） |

### 已知问题

| 问题 | 状态 | 说明 |
|------|------|------|
| 仿生文献库在项目内 | ⚠️ 待处理 | 需移出项目目录，否则 git 历史会包含大文件 |
| macOS fork crash | ✅ 已绕过 | watchdog 自动重启机制 |
| 重复文件（" 2"） | ✅ 已过滤 | 192 个 macOS Finder 重复文件已跳过 |
| 孤立对象泄漏 | ⏳ 待修复 | 42/285 文件有 knowledge_items 结构泄漏 |

---

## 任务清单

### 任务 0【已完成】LitExtract 提参基础设施搭建

- ✅ 提示词 v2（含仿生设计库元数据提取、专利/标准专项策略）
- ✅ Schema v2（biomimetic-v2，含 patent_number/standard_number 字段）
- ✅ 多路并发提取脚本（multi_worker_extract.sh，支持 1/2/3 路）
- ✅ 后处理脚本（fix_structure_leakage.py、relabel_evidence_quality.py、standardize_organism.py）
- ✅ 心跳汇报机制（iMessage 每小时汇报）
- ✅ macOS watchdog 自动重启（解决 fork crash 问题）
- ✅ 代码推送到 Literature-extracting（feature/biomimetic-extraction）

### 任务 1【进行中】论文全量提取

- 目标：302 篇论文全部提取完成
- 当前：296/302（98%），2 路并发运行中（bailian/qwen3.6-plus + mimo/mimo-v2.5）
- 剩余：约 6 篇
- 命令：`cd tools/litextract && bash scripts/multi_worker_extract.sh --pdf-dir ../仿生文献库/论文 --workers 2 --mode multimodal`
- 验收：302/302 论文 JSON 存在于 `outputs/extractions/论文/json/`

### 任务 2【待启动】专利重跑（v2 提示词）

- 目标：33 篇专利用优化后的提示词重跑
- 原因：当前专利用 v1 提示词提取，缺少 `biomimetic_metadata`、`biomimetic_narrative`、`patent_number` 字段
- 步骤：
  1. **备份旧 JSON**（不要直接 rm）：
     ```bash
     mkdir -p outputs/extractions/专利/json_backup_v1
     mv outputs/extractions/专利/json/*.json outputs/extractions/专利/json_backup_v1/
     ```
  2. 重跑：
     ```bash
     cd tools/litextract && bash scripts/multi_worker_extract.sh --pdf-dir ../仿生文献库/专利 --workers 2 --mode multimodal
     ```
- 验收：33/33 专利 JSON 存在，含 `patent_number` 和 `biomimetic_metadata`

### 任务 3【待启动】标准重跑（优化后提示词）

- 目标：6 篇标准用优化后的提示词重跑
- 原因：当前标准用未优化的提示词提取，缺少 `standard_number` 字段，且"性能数据"应为限值而非 qmax
- 步骤：
  1. **备份旧 JSON**：
     ```bash
     mkdir -p outputs/extractions/标准/json_backup_v1
     mv outputs/extractions/标准/json/*.json outputs/extractions/标准/json_backup_v1/
     ```
  2. 重跑：
     ```bash
     cd tools/litextract && bash scripts/multi_worker_extract.sh --pdf-dir ../仿生文献库/标准 --workers 1 --mode multimodal
     ```
- 验收：6/6 标准 JSON 存在，含 `standard_number`，knowledge_items 中有限值数据

### 任务 4【待启动】后处理 + 合并结果

- 目标：修复 JSON 结构缺陷，合并结果到统一目录
- 步骤：
  1. `python3 scripts/fix_structure_leakage.py` — 修复孤立对象泄漏
  2. `python3 scripts/relabel_evidence_quality.py` — 重标质量标签
  3. `python3 scripts/standardize_organism.py` — 标准化生物名称
  4. `python3 scripts/merge_results.py` — 合并结果到统一目录
  5. `python3 scripts/update_extraction_progress_doc.py` — 更新进度文档
- 验收：所有 JSON 结构完整，manifest 文件正确反映进度

### 任务 5【待启动】增量推送到 Biomimetic-design-library

- 目标：将已提取结果推送到 Biomimetic-design-library 仓库（增量，不等全量完成）
- 分支：`feature/extraction-results`
- 内容：`outputs/extractions/` 下的所有 JSON 和 manifest
- 排除：仿生文献库（PDF）、.env（API keys）
- 时机：**每完成一个分类（论文/专利/标准）就推送一次**，避免丢失已有产出
- 命令：
  ```bash
  cd /Users/panyao/Desktop/Biomimetic-design-library
  git add -A
  git commit -m "feat: 论文提参完成 (302篇)"
  git push origin feature/extraction-results
  ```

### 任务 6【关键缺口】实现 LitExtract → prototype.md 桥接管道

**这是核心任务。** 没有这个管道，后面的 7-12 全是空中楼阁。

LitExtract 已经产出了 341 个精细 JSON，但这些 JSON 和 prototype.md 之间没有数据通道。需要实现 3 个脚本：

#### 6.1 map_to_prototypes.py（JSON → 原型分类）

- 输入：`outputs/extractions/` 下的所有 JSON
- 逻辑：读取每个 JSON 的 `routing.prototype_targets`，按 `prototype_id` 分组
- 输出：`outputs/prototype_mapping.json`（每个原型 → 对应的 JSON 文件列表）
- 附加：结合 `standardize_organism.py` 的映射表，统一生物名称

#### 6.2 aggregate_per_prototype.py（聚合 → 结构化数据）

- 输入：`outputs/prototype_mapping.json` + 各 JSON 文件
- 逻辑：将同一原型下的所有 knowledge_items 聚合，生成：
  - `performance_data`：从 knowledge_items 中提取 qmax/去除率/限值，按污染物分组
  - `mechanisms`：从 knowledge_items 中提取吸附机制描述
  - `biomimetic_narrative`：从各 JSON 的 `biomimetic_narrative` 合并
  - `engineering_constraints`：从 knowledge_items 中提取工程约束
- 输出：`outputs/prototypes/<id>/aggregated_data.json`

#### 6.3 generate_prototype_md.py（渲染 → prototype.md）

- 输入：`outputs/prototypes/<id>/aggregated_data.json`
- 逻辑：按 `templates/prototype-template.md` 格式渲染为 Markdown
- 输出：`prototypes/<id>/prototype.md`
- 注意：所有数据带 provenance（`ref_doi`/`patent_number`/`standard_number` + `source_file`）

#### 验收

- 至少 1 个标杆原型（如 mussel-foot-adhesion）的 prototype.md 由管道自动生成且内容非空
- 生成的 prototype.md 中所有定量数据有来源标识
- `python3 tools/validate_consistency.py` 通过

### 任务 7【待启动】清理 5 个手工标杆

- **前置**：任务 6（桥接管道）完成
- 目标：清理 chitosan、lotus-leaf、MOF、mussel-foot-adhesion、SRB 的编造内容
- 方法：用桥接管道从 LitExtract JSON 自动生成新的 prototype.md，替换旧的编造内容
- 验收：5 个标杆中不存在任何"数值 + 未核实引用"

### 任务 8【待启动】provenance 模板 + 双层校验

- **前置**：任务 6（桥接管道）完成
- 目标：更新模板、新建校验脚本
- 验收：脚本能检出断链、孤儿、category 问题

### 任务 9【待启动】用桥接管道重建 5 个标杆

- **前置**：任务 6（桥接管道）+ 任务 7（清理）+ 任务 8（校验）完成
- 目标：用桥接管道从 LitExtract JSON 自动生成 5 个标杆的 prototype.md
- **不再从零读 PDF**，而是利用已有的 296+ 个 JSON 产出
- 步骤：
  1. 运行 `map_to_prototypes.py` 生成原型映射
  2. 运行 `aggregate_per_prototype.py` 聚合数据
  3. 运行 `generate_prototype_md.py` 生成 prototype.md
  4. 人工/AI 审核生成内容，补充缺失的叙事部分
  5. 运行 `validate_consistency.py` 校验
- 验收：5 个标杆达质量基线，每条数据 verified

### 任务 10【待启动】批量深化剩余原型

- **前置**：任务 9（5 个标杆验证通过）
- 目标：用桥接管道批量生成剩余约 25 个空壳 + 5 个零覆盖原型的 prototype.md
- 方法：运行桥接管道三件套（map → aggregate → generate），然后 AI 审核补充
- 验收：每个原型达基线且带完整 provenance

### 任务 11【待启动】核查设计规则

- **前置**：任务 10 完成
- 目标：核查 design-rules.json 的 40 条规则
- 验收：超过 80% 规则有真实证据支撑

### 任务 12【待启动】扩到 100

- **前置**：任务 11 完成
- 目标：补充文献，扩展原型到 100
- 验收：原型约 100，每个过基线与双层校验

---

## 时间评估

| 阶段 | 任务 | 预估时间 | 说明 |
|------|------|----------|------|
| **一：提参收尾** | 任务 1（论文 6 篇） | ~15 分钟 | API 调用时间 |
| | 任务 2（专利 33 篇重跑） | ~1 小时 | 2 路并发 |
| | 任务 3（标准 6 篇重跑） | ~15 分钟 | 1 路 |
| **二：后处理** | 任务 4（脚本运行） | ~20 分钟 | 已有脚本 |
| **三：桥接管道** | 任务 6（写 3 个脚本） | ~3 小时 | 核心开发工作 |
| **四：原型建设** | 任务 7（清理标杆） | ~30 分钟 | 用管道自动生成 |
| | 任务 8（校验脚本） | ~1 小时 | |
| | 任务 9（重建 5 标杆） | ~1 小时 | 管道 + AI 审核 |
| | 任务 10（批量 25 原型） | ~2 小时 | 管道批量运行 |
| | 任务 11（核查规则） | ~1 小时 | |
| | 任务 12（扩到 100） | ~5 小时 | 含补充文献 |
| **总计** | | **~15 小时** | |

**关键路径**：任务 1 → 任务 6（桥接管道）→ 任务 9（验证）→ 任务 10（批量）→ 任务 12（扩展）

---

## 待处理事项（立即）

### 1. 仿生文献库移出项目目录

**问题**：仿生文献库（PDF 原始文件）在项目目录内，导致 git 历史包含大文件。

**解决方案**：手动移出项目目录：
```bash
mv /Users/panyao/Desktop/Biomimetic-design-library/仿生文献库 /Users/panyao/Desktop/仿生文献库
```

**移出后**：重新创建干净分支，从 main 开始，只添加需要的文件。

### 2. Git 推送策略

**问题**：之前两次推送都把仿生文献库推上去了。

**根本原因**：
1. 仿生文献库在 git 历史中（commit 9ee5da0 包含 564 个文件）
2. `.gitignore` 只对未跟踪文件生效，已提交的文件不会被排除

**解决方案**：
1. 移出仿生文献库后，从 main 创建新分支
2. 只添加需要的文件（代码、结果、文档）
3. 推送前用 `git ls-tree -r HEAD | grep "仿生文献库"` 验证

---

## 已知技术问题

### 1. macOS fork crash

**问题**：macOS 上 bash `&` 后台 fork 进程后运行 openclaw（Node.js）会触发 CoreFoundation segfault。

**解决方案**：已添加 watchdog 机制，worker 崩溃后自动重启。详见 `scripts/multi_worker_extract.sh` 的 launch 部分。

**根本解决**：需要修改 worker 启动方式，避免 fork。可考虑用 `launchctl` 或 `osascript` 启动独立进程。

### 2. DASHSCOPE_API_KEY 配置

**规则**：DASHSCOPE_API_KEY 只调用 qwen3.7-max，不调用 qwen3.6-plus。qwen3.6-plus 通过 BAILIAN_CODING_PLAN_API_KEY 调用。

**三路配置**：
- Worker 1: dashscope → qwen3.7-max（按量付费，推理能力强）
- Worker 2: bailian → qwen3.6-plus（Coding Plan，多模态）
- Worker 3: mimo → mimo-v2.5（MiMo Token Plan，速度快）

### 3. 重复文件

文献库中有 192 个 macOS Finder 重复文件（" 2.pdf" 后缀），已在队列构建时跳过。实际有效论文 = 494 - 192 = 302 篇。

---

## 证据完整性铁律

整个项目的成败系于一条规则：

**AI 可以推理与综合（标注清楚即可），但绝不能给一个它没有从原文读到的数值挂上引用。**

- 有引用不等于可信——编造条目也带格式完整的引用
- 数值必须来自原文的表格、图或正文，保留原文精度和单位
- 缺源即留空，不许编造填补
- 推断性内容标为 `source: llm_inference`，不挂文献引用
- `verification=verified` 永远不许由生成方自报，只能由核查产生

---

## 不要做的事

- 不要给任何未从原文读到的数值挂引用（铁律）。
- 不要让生成方自报 `verification=verified`；它只能由核查产生。
- 不要 LLM 直接撰写内容；所有内容来自对真实 PDF 的 grounded 提取。
- 不要跨论文拼凑或外推性能数值；不要取整美化。
- 不要上传仿生文献库（PDF 原始文件）到 GitHub。
- 不要上传 .env 文件（API keys）到 GitHub。
- 不要用 `rm` 直接删除旧 JSON，先备份。
- 不要相信旧文档或任何"已完成"自述的进度，以本文件和实际 JSON 文件为准。
