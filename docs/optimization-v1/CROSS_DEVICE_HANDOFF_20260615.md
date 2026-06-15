# 跨设备交接快照 — 2026-06-15

用途：从当前电脑切换到家里电脑继续 Phase 8 patch、Phase 9、最终 review。本文只压缩上下文，不替代阶段报告。

## 当前仓库状态

- 当前工作目录：`C:\Users\15995\Biomimetic-design-library`
- 当前分支：`opt/curation-grounding-v1`
- 远端跟踪：`origin/opt/curation-grounding-v1`
- 当前 HEAD：`333b092 @ Phase 8 patch: 修复 review 发现的 schema/护栏问题`
- 当前分支比远端领先 3 个已提交 commit：
  - `437eb9f @ Phase 7.5: 修复接口候选排序诚实度 + pitcher-plant function 字段`
  - `53dff3c @ Phase 8: 失效边界补全 + DO-NOT 导出`
  - `333b092 @ Phase 8 patch: 修复 review 发现的 schema/护栏问题`
- Phase 8 patch 已提交；Phase 9 尚未开始。

## Phase 8 Patch 快照

Phase 8 patch 已在 `333b092` 提交，包含：

- `docs/optimization-v1/phase8-report.md`
- `exports/adrmats_do_not.json`
- `prototypes_db/plant-tannin.json`
- `prototypes_db/silk-fibroin.json`
- `prototypes_db/sulfate-reducing-bacteria.json`
- `tools/check_boundary_guardrail.py`

这些修改对应已发现的 Phase 8 放行前问题：

1. `plant-tannin` 的 B 档 boundary 在 `condition.value` 中残留数值 `[10]`。
2. `silk-fibroin` 两处 B 档 boundary 在 `condition.value` 中残留数值 `[2, 11]`。
3. `sulfate-reducing-bacteria` 的 SRB 厌氧 boundary 原本 `basis=from_source`，但只有 `locator="biology knowledge"`，没有真实 PDF locator/quote，也没有 `verification`。
4. `check_boundary_guardrail.py` 初版只查 `text` 数字，不查 `condition.operator/value`，存在盲区。

## 已确认的重要结论

### Phase 7.5

Phase 7.5 修复了接口排序诚实度问题：

- `query()` 不再盲取 `mechanisms[0]`。
- 候选机制按 verification 优先级选择。
- `needs_review` 机制不会再以普通置信度进入强排序。
- `verify_adrmats_delivery.py` 已适配 `confidence` 字段。

此前实际验收结果：

- `verify_adrmats_delivery.py`：6/6 PASS
- PFOA / SMX / BPA 不再伪装 direct evidence
- Pb(II) 前排 direct evidence 候选展示 verified 机制

### Phase 8

Phase 8 初版完成：

- 24 个 active 原型都有 boundary condition。
- 28 个 qualified 机制都有 BC。
- 当前导出应为 62 条 boundary。
- 当前硬 DO-NOT 为 0。
- 当前 soft caution 为 62。

Phase 8 初版不能直接进入 Phase 9；现在 Phase 8 patch 已完成并通过关键 gate，可以进入 Phase 9。

## 当前阻断项

Phase 9 还没有开始。Phase 8 patch 的关键 gate 已通过：

1. `check_boundary_guardrail.py`：PASS，62 条 BC，0 hard DO-NOT，62 soft caution。
2. `verify_adrmats_delivery.py`：6/6 PASS。
3. `export_do_not.py`：成功导出 62 条 boundary，涉及 24 个原型。

当前剩余阻断项转移到 Phase 9：

1. `check_repo_hygiene.py` 之前仍有治理失败，需要 Phase 9 修到 PASS。
2. README / SUPPORT / FINAL-report 需要和真实统计对齐。
3. Phase 9 examples 不能把 `needs_review` 写进 facts 或强排序。

## 关键铁律

- 严禁运行 `tools/build_prototypes_db.py`。
- canon 唯一真源是 `prototypes_db/*.json`。
- `needs_review` 可以存在，但不能进入强排序、facts、hard DO-NOT、verified 证据链。
- `llm_inferred` 永不升级为 `verified`。
- B 档和未核验 C 档 boundary 只能定性，不能携带数值阈值。
- 具体数值阈值只能出现在 A 档：`basis=from_source` 且 `verification=verified/corroborated` 且有真实 locator + quote。
- Phase 9 是打包和总验收阶段，必须在 Phase 8 patch gate 通过后再启动。

## 回家后第一步

如果家里电脑是原始文件所在地，请先确认：

```powershell
cd <家里电脑的 Biomimetic-design-library 路径>
git status --short --branch
git log --oneline --decorate -n 8
```

需要看到：

- 当前分支是 `opt/curation-grounding-v1`
- 已包含 `437eb9f`、`53dff3c`、`333b092`
- 如果家里电脑没有 `333b092`，先不要开 Phase 9；需要先同步 Phase 8 patch。

同步方式二选一：

1. 当前电脑 push 当前分支，然后家里电脑 pull。
2. 如果不能 push，把 `333b092` patch 或整个仓库状态打包带回家，再在家里电脑应用。

## 推荐下一步

继续按 `docs/optimization-v1/HOME_PHASE9_WORK_PLAN_20260615.md` 执行。
