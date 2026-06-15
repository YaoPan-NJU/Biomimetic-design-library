# 交接文档 — 仿生吸附库整改复核（Post-Phase 9）

> 用途：把复核/编排角色交给家里 Codex 或另一个 AI。当前不是整改中途，而是 Phase 9 后的最终状态复核与证据增强 review。

## 1. 一句话现状

仿生库 9 阶段整改已完成，final acceptance review 已通过，成果已合入并推送到 `adsorption/dev`。当前可作为 ADRMATS 仿生启发检索模块继续使用；后续重点是用家里电脑上的原始 PDF 做证据增强，把有充分来源的 soft caution 升级为 hard DO-NOT。

## 2. 仓库与分支

- 仓库：`github.com/YaoPan-NJU/Biomimetic-design-library`
- 家里应使用分支：`adsorption/dev`
- 源工作分支：`opt/curation-grounding-v1`
- 已接受 commit：`bac696a`
- 关键状态：`adsorption/dev` 与 `opt/curation-grounding-v1` 在办公室最后核对时均包含 Phase 9 成果

## 3. 当前能力边界

本库定位是 ADRMATS 的仿生启发检索模块。它提供：

- 可检索的生物原型
- 原型机制和可迁移因果链
- 设计转译建议
- rule-based cautions
- 诚实的 evidence / confidence 标注

它不直接设计材料、不预测性能、不替代工程放大。

## 4. 当前硬指标

| 指标 | 数值 |
|---|---:|
| active 原型 | 24 |
| materials_reference | 4 |
| parked | 1 |
| 机制总数 | 534 |
| 合格因果链卡 | 28 |
| PDF 已核验 verified | 23 |
| boundary_conditions | 62 |
| hard DO-NOT | 0 |
| soft caution | 62 |
| official brief examples | 4 |
| validation error | 0 |
| chimera 违规 | 0 |

## 5. 已通过验收

最终验收结果：

- `verify_adrmats_delivery.py`：6/6 PASS
- `check_boundary_guardrail.py`：8 项全绿
- `export_do_not.py`：62 条，0 hard，62 soft
- `test_interface_honesty.py`：3/3 PASS
- `check_translation_specificity.py`：25/25 合格
- `check_chimera.py --strict`：0 违规
- `validate_consistency.py`：0 error
- `check_repo_hygiene.py`：PASS

## 6. 必须保留的风险表述

不要把当前库说成“所有边界已核验”。准确说法是：

- 当前 hard DO-NOT 为 0。
- 当前 62 条 boundary 全是 soft caution。
- soft caution 可以提示风险，但不能作为硬门控。
- hard DO-NOT 需要 PDF 原文 quote、真实 locator、`basis=from_source`、`verification=verified/corroborated`。

## 7. 后续 Review 重点

### 优先级 1：5 个待文献原型

- coral-skeleton
- magnetic-bacteria
- pitcher-plant
- lobster-exoskeleton
- spider-silk

如果家里电脑有新下载 PDF，先从这些原型开始。

### 优先级 2：62 条 soft caution

目标是找出哪些 soft caution 能从 PDF 中得到明确支持。能支持的进入 `upgrade_candidate`，不能支持的保持 soft。

### 优先级 3：高频 brief 候选

优先抽查 Pb(II)、PFOA、SMX、BPA 四个 official examples 中出现的候选机制，确认它们没有把 `needs_review` 冒充为 verified。

### 优先级 4：silk-fibroin 重复机制

先报告重复机制的影响，再决定是否清理。不要未经确认直接合并或删除。

## 8. 本地 AI 的职责边界

本地 AI 可以：

- 跑验收脚本
- 打开 PDF
- 查 quote 是否存在
- 判断 source 是否对口
- 生成 review 表
- 提出 `upgrade_candidate` 或 `keep_soft`

本地 AI 不可以：

- 自动升级 `needs_review`
- 自动把 soft caution 改成 hard DO-NOT
- 自动新增数值阈值
- 自动删除或合并机制
- 为了通过脚本删除风险记录

## 9. 多模态模型使用

- 用 `mimo-v2.5-pro` 做复杂文本推理和最终判断。
- 用 `mimo-v2.5` 多模态处理扫描 PDF、表格、图注、页面定位。
- 多模态只解决“看见和定位”的问题，不自动提高证据等级。

## 10. 回家第一步

执行：

```powershell
cd <家里电脑的 Biomimetic-design-library 路径>
git fetch origin
git checkout adsorption/dev
git pull --ff-only origin adsorption/dev
git log --oneline --decorate -n 10
git status --short --branch
```

然后按：

- `docs/optimization-v1/CROSS_DEVICE_HANDOFF_20260615.md`
- `docs/optimization-v1/HOME_PHASE9_WORK_PLAN_20260615.md`

继续。

## 11. 停止条件

遇到这些情况必须停下来问 Yao：

- 没有同步到 `bac696a` 或更新 commit
- 验收脚本失败
- 工作区已有不明未提交修改
- PDF 不存在或打不开
- source 与原型不对口
- quote 不能支持边界
- 想升级 hard DO-NOT
- 想删除、合并、重排机制
