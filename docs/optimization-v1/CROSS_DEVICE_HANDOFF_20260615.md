# 跨设备交接快照 — 2026-06-15（Phase 9 后）

用途：把办公室电脑上的最新上下文压缩给家里电脑、家里 Codex 和本地 AI。本文是“接着干什么”的入口，不替代阶段报告。

## 一句话状态

Phase 0-9 已完成，final acceptance review 已通过，`opt/curation-grounding-v1` 的成果已经合入并推送到 `adsorption/dev`。回家后不要再启动 Phase 9；先同步 `adsorption/dev`，复跑验收，再进入“证据增强 review”。

## 当前仓库状态

- 办公室工作目录：`C:\Users\15995\Biomimetic-design-library`
- 当前应使用分支：`adsorption/dev`
- 源工作分支：`opt/curation-grounding-v1`
- 远端：`origin`
- 已接受的关键 commit：
  - `333b092`：Phase 8 patch，修复 boundary schema/护栏问题
  - `ccded69`：Phase 9，打包与总验收
  - `bac696a`：Phase 9 acceptance patch，修正最终文档和示例目录
- 办公室最后核对时：`adsorption/dev`、`origin/adsorption/dev`、`opt/curation-grounding-v1`、`origin/opt/curation-grounding-v1` 均指向 `bac696a`。

如果回家后看到的最新 commit 不是 `bac696a` 或更新的文档交接 commit，先不要 review，先同步仓库。

## 已完成内容

### Phase 8 Patch

`333b092` 已修复：

- `plant-tannin` B 档 boundary 的隐藏数值 `[10]`
- `silk-fibroin` 两条 B 档 boundary 的隐藏数值 `[2,11]`
- `sulfate-reducing-bacteria` 的 SRB 厌氧 boundary 从伪 `from_source` 降回 `llm_inferred / needs_review / soft`
- `tools/check_boundary_guardrail.py` 升级为 8 项检查，覆盖必填字段、basis 合法性、condition.value、locator、verification 等

### Phase 9

`ccded69` 已完成：

- 刷新 `exports/adrmats_do_not.json`
- 生成 4 个新版 ADRMATS brief 示例
- 更新 `README.md`
- 更新 `docs/SUPPORT_SCOPE_AND_RISKS.md`
- 创建 `docs/optimization-v1/FINAL-report.md`
- 修复 `check_repo_hygiene.py` 暴露的治理问题

### Final Acceptance Patch

`bac696a` 已完成：

- 对齐 README、SUPPORT、FINAL-report 的最终状态表述
- 移走 `examples/adrmats_briefs/` 中的旧中文示例
- 保留 4 个新版 `brief_*.json` 作为官方示例
- 复跑后 `check_repo_hygiene.py` PASS

## 当前硬指标

| 指标 | 当前值 |
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
| 校验错误 | 0 |
| chimera 违规 | 0 |

## 已通过的验收

办公室最终验收已确认：

- `verify_adrmats_delivery.py`：6/6 PASS
- `check_boundary_guardrail.py`：8 项全绿，62 BC，0 hard，62 soft
- `export_do_not.py`：导出 62 条，覆盖 24 个原型
- `test_interface_honesty.py`：3/3 PASS
- `check_translation_specificity.py`：25/25 合格
- `check_chimera.py --strict`：0 违规
- `validate_consistency.py`：0 error，193 个既有 warning
- `check_repo_hygiene.py`：PASS
- `examples/adrmats_briefs/`：仅 4 个新版 `brief_*.json`，均包含 `rule_based_cautions`

注意：`tools/check_causal_chain.py` 可能会重写 `docs/optimization-v1/phase5-chains.md`。如果只是复核，不要把它产生的无意 diff 提交；先看 `git status`。

## 剩余风险

这些不是 Phase 9 blocker，但会影响后续证据质量：

1. **0 hard DO-NOT / 62 soft caution**：当前所有边界都是软提示，没有 PDF 逐条核验的硬约束。
2. **5 个原型待文献下载**：coral-skeleton、magnetic-bacteria、pitcher-plant、lobster-exoskeleton、spider-silk。
3. **silk-fibroin 重复机制**：两个同名“吸附机制”及重复 BC，属于既有数据质量问题。
4. **大量 needs_review**：低置信候选可以出现，但已经标为 `confidence: low`，不会冒充 verified。

## 回家后第一步

在家里电脑执行：

```powershell
cd <家里电脑的 Biomimetic-design-library 路径>
git status --short --branch
git fetch origin
git checkout adsorption/dev
git pull --ff-only origin adsorption/dev
git log --oneline --decorate -n 10
```

期望至少看到：

```text
bac696a @ Phase 9 patch: align final docs and examples after acceptance review
ccded69 @ Phase 9: 打包与总验收
333b092 @ Phase 8 patch: 修复 review 发现的 schema/护栏问题
```

如果看不到 `bac696a`，不要继续 review，先解决同步问题。

## 家里 Codex / 本地 AI 应先读这些文件

按顺序读：

1. `README.md`
2. `docs/SUPPORT_SCOPE_AND_RISKS.md`
3. `docs/optimization-v1/FINAL-report.md`
4. `docs/optimization-v1/CROSS_DEVICE_HANDOFF_20260615.md`
5. `docs/optimization-v1/HOME_PHASE9_WORK_PLAN_20260615.md`
6. `docs/optimization-v1/DEFINITIONS.md`
7. `docs/optimization-v1/literature-requests.md`

## 禁令

- 不要再跑 Phase 9。
- 不要运行 `tools/build_prototypes_db.py`。
- 不要把 `needs_review` 自动改成 `verified`。
- 不要为了让脚本全绿而删除风险记录。
- 不要把 soft caution 写成 hard DO-NOT。
- 不要在没有真实 source locator + quote 的情况下写数值阈值。

## 下一步入口

继续按 `docs/optimization-v1/HOME_PHASE9_WORK_PLAN_20260615.md` 执行。
