---
status: ready_for_qoderwork_acceptance
date: 2026-06-17
model: mimo-v2.5-pro
scope: 8 Yao-approved boundary rules → JSON writes
validation:
  check_boundary_guardrail: pass (no new errors; pre-existing pitcher-plant-slippery-surface missing BC unchanged)
  validate_consistency: pass (0 errors, 194 warnings — all pre-existing)
---

# B1 Boundary Rule JSON Writes — Execution Report

## Summary

| # | Rule ID | Target File | Status | Action |
|---|---------|-------------|--------|--------|
| 1 | B01-CHI-002 | chitosan.json | ✅ Done | engineering_constraints appended (→ 61 items) |
| 2 | B01-PDA-003 | enrichment/polydopamine-coating.json | ℹ️ No action | No 疏水膜/抗菌/非吸附综述 mechanisms found |
| 3 | B03-CHL-001 | chlorella-cell-wall.json | ⚠️ Yao decision needed | Cheng2021 Pb2+ NOT in mechanisms[0] |
| 4 | B03-CMIC-001 | cell-membrane-ion-channel.json | ✅ Done | provenance_summary.scope_note added |
| 5 | B04-SHART-003 | separation/superhydrophobic-artificial.json | ⚠️ Yao decision needed | CN114874407A NOT in performance_data |
| 6 | B05-MATREF-001 | materials_reference/*.json (×4) | ✅ Done | review_table_caveat added to all 4 files |
| 7 | B07-REG-002 | parked/namib-beetle.json | ✅ Done | provenance_summary.scope_note added |
| 8 | B13-PDA-OCR-002 | polydopamine-coating.json | ✅ Done | perf[34] metric_type/ranking_exclusion/notes added |

**Result: 6/8 applied, 2 need Yao decision, 1 informational (no action needed)**

---

## Detailed Results

### 1. B01-CHI-002 → chitosan.json ✅

Appended to `engineering_constraints` (index 60, total now 61):

```json
{
  "text": "Cu(II)吸附最佳pH≈5，pH>6时Cu(OH)₂沉淀干扰吸附测量",
  "type": "soft_boundary",
  "basis": "from_source",
  "source_file": "Bambaeero2020",
  "verification": "needs_review",
  "gate_level": "soft",
  "evidence_label": "keep_soft",
  "notes": "Bambaeero2020 Cu吸附pH约束，Yao审批2026-06-17"
}
```

### 2. B01-PDA-003 → enrichment/polydopamine-coating.json ℹ️

Inspected all 17 mechanism keys in the enrichment PDA dict. All are adsorption-related:

```
[0] 吸附机制 — 配位螯合
[1] PDA吸附机制-姜黄素
[2] PDA吸附机制-番茄红素
[3] 吸附机制
[4] pHpzc和pH影响
[5] 吸附机理六重协同
[6] 吸附机制-酚羟基参与
[7] pH对吸附的影响机制
[8] XPS分析-吸附机理
[9] 吸附活性基团协同
[10] XPS吸附机理
[11] Cr(VI)吸附机制总结
[12] Cu(II)吸附机制总结
[13] CR吸附机制总结
[14] 吸附机理-pH依赖性
[15] 吸附机制类型
[16] PDA吸附机制补充
```

**No 疏水膜/抗菌/非吸附综述 mechanisms found.** The 21 erroneous mechanisms referenced in the original audit may have already been removed in a prior cleanup. No deletion needed.

### 3. B03-CHL-001 → chlorella-cell-wall.json ⚠️

**Finding:** `mechanisms[0]` is **NOT** Cheng2021 Pb2+. Current mechanisms[0] is:

> "藻类去除合成染料的三种机制 Three mechanisms of dye removal by algae" (ref_doi: 10.1155/2021/9923643)

The closest Pb2+ reference is `mechanisms[7]`:
> "微藻吸附Pb²⁺的两阶段机制 Two-stage adsorption mechanism" (ref_doi: 10.19824/j.cnki.cn32-1786/x.2021.0078)

**No "Cheng2021" identifier found in any mechanism.** This mechanism may have been removed or renumbered since the audit was drafted.

**Action:** No edit made. Yao to confirm:
- Is the Cheng2021 Pb2+ scope caveat still needed?
- If so, which mechanism index should it target?

### 4. B03-CMIC-001 → cell-membrane-ion-channel.json ✅

Added to `provenance_summary`:

```json
"scope_note": "Separation/desalination prototype, not adsorption. Performance metrics are rejection_rate/permeance, not qmax."
```

### 5. B04-SHART-003 → separation/superhydrophobic-artificial.json ⚠️

**Finding:** CN114874407A (TiO2/氟硅烷海绵) is **NOT present** in the `performance_data` array (8 entries checked). The patent may be referenced in mechanisms or elsewhere in the file but has no performance_data row.

**Action:** No edit made. Yao to confirm:
- Should the `ownership_note` be added to a mechanism entry instead?
- Or is this patent's performance data expected to be added in a future extraction round?

### 6. B05-MATREF-001 → all materials_reference/*.json ✅

Added to `provenance_summary` of all 4 files:

```json
"review_table_caveat": "Aggregate review-table values; cross-comparison requires normalization for methodology, pH, and temperature differences"
```

Files modified:
- `alginate.json`
- `cellulose-nanocrystal.json`
- `metal-organic-framework.json`
- `starch-granule.json`

### 7. B07-REG-002 → parked/namib-beetle.json ✅

Added to `provenance_summary`:

```json
"scope_note": "Generic fog-harvesting review sources; background reference only, no direct adsorption evidence"
```

### 8. B13-PDA-OCR-002 → polydopamine-coating.json ✅

Modified `performance_data[34]` (CN114570339A, H-PDA-SO对U(VI)吸附容量, 图7估读, ~8.2 mg/g):

```json
{
  "metric_type": "selectivity_figure_value",
  "ranking_exclusion": true,
  "notes": "~8.2 mg/g from selectivity figure, excluded from qmax ranking per Yao decision 2026-06-17"
}
```

Other CN114570339A rows (perf[28-33]) are actual adsorption capacity measurements at various temperatures/pH — NOT marked as exclusions.

---

## Validation Results

### check_boundary_guardrail.py

```
active 原型数: 24
总 BC 条数: 61
  硬 DO-NOT (hard): 5
  软 caution (soft): 56

❌ 缺少 BC 的原型 (1): pitcher-plant-slippery-surface  ← pre-existing, not caused by this batch
✅ BC 缺必填字段=0
✅ basis 非法值=0
✅ gate_level 不一致=0
✅ from_source 但 locator 缺失/无效=0
```

### validate_consistency.py

```
错误: 0
警告: 194 (all pre-existing)
✅ 报告模式：无错误
```

---

## Pending Yao Decisions

1. **B03-CHL-001:** Cheng2021 Pb2+ mechanism not found in chlorella-cell-wall.json. Is scope_caveat still needed? If so, which mechanism index?
2. **B04-SHART-003:** CN114874407A not in superhydrophobic-artificial.json performance_data. Is the ownership_note targeting a different location?
