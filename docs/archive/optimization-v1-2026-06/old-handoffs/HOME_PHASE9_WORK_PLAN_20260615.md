# 回家后执行计划 — Post-Phase 9 Review

> 给家里 Codex 和本地 AI 的可执行计划。当前 Phase 9 已完成并通过 final acceptance；回家后不要再跑 Phase 9，先同步 `adsorption/dev`，再做 post-merge 验证和证据增强 review。

## 目标

在家里电脑上完成三件事：

1. 确认家里仓库已经同步到办公室最终状态。
2. 独立复跑 post-merge 验收，确认没有跨设备差异。
3. 在原始 PDF 可用的基础上，开始证据增强 review，把能核实的 soft caution 升级为真正的 hard DO-NOT。

## 角色分工

- **Yao**：做关键决策。凡是要升级证据等级、改 hard/soft、删除或合并机制，都必须停下来让 Yao 确认。
- **家里 Codex**：主复核者。负责读文档、跑验收、设计抽查、判断是否可以让本地 AI 批量执行。
- **本地 AI**：执行者。负责跑脚本、打开 PDF、提取 locator/quote、整理候选表。不能自行拍板升级 verified。
- **mimo-v2.5-pro**：优先用于复杂推理、证据等级判断、跨文件一致性判断。
- **mimo-v2.5 多模态**：用于扫描版 PDF、表格截图、图注、版面定位等需要视觉能力的任务。

质量优先级：高质量 > 快速。不用考虑模型费用。

## 总体顺序

```text
1. 同步 adsorption/dev
2. 复跑 post-merge 验收
3. 读最终文档，确认当前风险
4. 决定是否开始证据增强 review
5. PDF 证据 review：只报告，不越权修改
6. Yao/Codex 决策后再改数据
7. 改完后复跑验收
```

## Task 1: 同步仓库

### Step 1.1 切到项目目录

```powershell
cd <家里电脑的 Biomimetic-design-library 路径>
```

### Step 1.2 检查当前状态

```powershell
git status --short --branch
git log --oneline --decorate -n 5
```

如果工作区有未提交修改，先停下，让 Yao 判断这些修改是不是家里电脑已有工作。不要直接覆盖。

### Step 1.3 同步 `adsorption/dev`

```powershell
git fetch origin
git checkout adsorption/dev
git pull --ff-only origin adsorption/dev
git log --oneline --decorate -n 10
```

期望看到：

```text
bac696a @ Phase 9 patch: align final docs and examples after acceptance review
ccded69 @ Phase 9: 打包与总验收
333b092 @ Phase 8 patch: 修复 review 发现的 schema/护栏问题
```

如果看不到 `bac696a` 或更新的交接文档 commit，先解决同步，不进入 review。

## Task 2: Post-Merge 验收

### Step 2.1 运行全套验收

```powershell
python -X utf8 tools\verify_adrmats_delivery.py
python -X utf8 tools\check_boundary_guardrail.py
python -X utf8 tools\export_do_not.py
python -X utf8 tools\test_interface_honesty.py
python -X utf8 tools\check_translation_specificity.py
python -X utf8 tools\check_chimera.py --strict
python -X utf8 tools\validate_consistency.py
python -X utf8 tools\check_repo_hygiene.py
```

通过标准：

- `verify_adrmats_delivery.py`：6/6 PASS
- `check_boundary_guardrail.py`：8 项全绿
- `export_do_not.py`：62 条，0 hard，62 soft
- `test_interface_honesty.py`：3/3 PASS
- `check_translation_specificity.py`：25/25 合格
- `check_chimera.py --strict`：0 违规
- `validate_consistency.py`：0 error
- `check_repo_hygiene.py`：PASS

### Step 2.2 可选运行因果链检查

```powershell
python -X utf8 tools\check_causal_chain.py
```

期望：28 张合格卡，覆盖 24/24 active 原型。

注意：这个脚本可能重写 `docs/optimization-v1/phase5-chains.md`。跑完必须执行：

```powershell
git status --short
```

如果只有 `phase5-chains.md` 被重写，先不要提交，交给 Yao/Codex 判断是否恢复或保留。

### Step 2.3 核查官方 brief 示例

```powershell
python -X utf8 -c "import json,glob,os; files=glob.glob('examples/adrmats_briefs/*.json'); print(len(files),[os.path.basename(f) for f in files]); assert len(files)==4; missing=[os.path.basename(f) for f in files if 'rule_based_cautions' not in ((d:=json.load(open(f,encoding='utf-8'))).get('brief') or d)]; print('missing_rule_based_cautions=',missing); assert not missing"
```

期望只有 4 个新版示例：

```text
brief_BPA.json
brief_Pb_II.json
brief_PFOA.json
brief_SMX.json
```

## Task 3: 读当前状态

家里 Codex / 本地 AI 先读这些文件，不要凭记忆做判断：

```text
README.md
docs/SUPPORT_SCOPE_AND_RISKS.md
docs/optimization-v1/FINAL-report.md
docs/optimization-v1/DEFINITIONS.md
docs/optimization-v1/literature-requests.md
exports/adrmats_do_not.json
```

读完后输出一段短报告：

```text
当前分支：
当前 HEAD：
验收命令结果：
hard DO-NOT 数量：
soft caution 数量：
官方 examples 数量：
仍需人工/AI review 的风险：
是否建议进入证据增强 review：
```

## Task 4: 决定是否开始证据增强 Review

如果 Task 2 全绿，就可以开始证据增强 review。它不是 Phase 9 blocker，而是下一轮质量提升。

本轮 review 的目标不是“把所有 needs_review 都清零”，而是优先处理最影响交付质量的证据边界：

1. 5 个待文献原型：coral-skeleton、magnetic-bacteria、pitcher-plant、lobster-exoskeleton、spider-silk。
2. 可能被 ADRMATS brief 高频展示的候选机制。
3. 当前 62 条 soft caution 中，有机会从 PDF 明确抽取边界的条目。
4. silk-fibroin 重复机制，先报告影响，再决定是否清理。

## Task 5: 证据增强 Review 的规则

### 不可越权规则

本地 AI 可以查证和报告，但不能自行做这些事：

- 把 `needs_review` 改成 `verified`
- 把 `llm_inferred` 改成 `from_source`
- 把 soft caution 改成 hard DO-NOT
- 新增数值阈值
- 删除机制或合并重复机制

这些动作必须进入 decision queue，由 Yao/Codex 决定。

### A 档 hard DO-NOT 标准

只有同时满足以下条件，才能考虑升级为 hard DO-NOT：

- PDF/source 是关于该生物原型、结构或机制的对口来源
- 原文中确实存在可定位的 quote
- locator 能精确到文件名 + 页码/章节/表格/句子线索
- quote 支持的是“失效边界”，不是泛泛背景
- `basis=from_source`
- `verification=verified` 或 `corroborated`
- 如果写数值阈值，数值必须来自原文，不可推断

任一条件缺失，保持 soft caution 或 `needs_review`。

### 多模态使用规则

优先用 `mimo-v2.5-pro` 做文本和判断；遇到以下情况切到 `mimo-v2.5` 多模态：

- PDF 是扫描版，文本提取不可靠
- 证据在表格、图注、曲线、示意图中
- 页码/版面定位需要视觉确认
- OCR 后 quote 断裂，需要看原图确认

多模态只能帮助定位和确认，不等于自动 verified。最终仍按 A 档标准判断。

## Task 6: 本地 AI 的输出格式

每批 review 最多 10 条，输出这个表：

| id | 原型 | 机制/边界 | 当前等级 | PDF/source | locator | quote 是否真在原文 | source 是否对口 | 建议动作 | 需要 Yao 决策 |
|---|---|---|---|---|---|---|---|---|---|

建议动作只能写：

- `keep_soft`
- `upgrade_candidate`
- `downgrade_or_fix`
- `needs_human_decision`
- `missing_source`

不要直接改 JSON。

## Task 7: 决策后修改数据

只有当 Yao/Codex 明确批准某条修改后，本地 AI 才能改 `prototypes_db/*.json`。

修改后必须复跑：

```powershell
python -X utf8 tools\check_boundary_guardrail.py
python -X utf8 tools\export_do_not.py
python -X utf8 tools\verify_adrmats_delivery.py
python -X utf8 tools\check_repo_hygiene.py
git status --short
```

如果修改影响机制排序、brief 或 examples，再额外跑：

```powershell
python -X utf8 tools\test_interface_honesty.py
python -X utf8 tools\check_translation_specificity.py
python -X utf8 tools\check_chimera.py --strict
python -X utf8 tools\validate_consistency.py
```

## 给家里 Codex 的启动提示词

```text
你正在接手 Biomimetic-design-library 的 post-Phase 9 review。

当前目标不是重新跑 Phase 9。Phase 9 已完成，final acceptance 已通过，成果已合入 adsorption/dev。你要先同步 adsorption/dev，复跑 post-merge 验收，然后准备证据增强 review。

请先读取：
1. README.md
2. docs/SUPPORT_SCOPE_AND_RISKS.md
3. docs/optimization-v1/FINAL-report.md
4. docs/optimization-v1/CROSS_DEVICE_HANDOFF_20260615.md
5. docs/optimization-v1/HOME_PHASE9_WORK_PLAN_20260615.md
6. docs/optimization-v1/DEFINITIONS.md
7. docs/optimization-v1/literature-requests.md

铁律：
- 不运行 tools/build_prototypes_db.py
- 不再启动 Phase 9
- 不把 needs_review 自动升级为 verified
- 不把 soft caution 自动升级为 hard DO-NOT
- 不写没有 PDF quote 支撑的数值阈值
- 数据修改前先给 decision queue，让 Yao 决策

第一步请执行同步和 post-merge 验收，并给出：
当前 HEAD、脚本结果、0 hard/62 soft 是否保持、examples 是否只有 4 个新版 brief、是否可以进入证据增强 review。
```

## 停止条件

遇到以下任一情况，停止并问 Yao：

- 拉不到 `bac696a` 或更新状态
- 验收脚本失败
- 工作区有未知未提交修改
- 原始 PDF 不在家里电脑
- source 与原型不对口
- 想升级 hard DO-NOT 但 quote/locator 不完整
- 需要删除、合并或重排机制
