# Oyster-Shell Performance Data Verification Report

**Date:** 2026-06-18  
**Target:** `prototypes_db/oyster-shell.json`  
**Auditor:** OpenClaw bulk worker  

---

## Summary

| Metric | Count |
|--------|-------|
| Total performance_data rows | 13 |
| Rows modified | 10 |
| `needs_review` → `partial` | 9 |
| `needs_review` → `missing_pdf` | 1 |
| Existing `partial` rows (already had quotes) | 3 (unchanged) |
| Total `partial` after update | 12 |
| Total `missing_pdf` after update | 1 |

---

## Verification Details

### Row 3 — CAs-4 vs CA-4 adsorption (Qiu2021)
- **Status:** `needs_review` → `missing_pdf`
- **Reason:** Source PDF `仿生文献库/论文/第4组-生物矿化/2021-Qiu-oyster-shell-adsorption-adsorbent.pdf` does not exist on disk. Cannot verify.

### Rows 5–6 — Wang2021 (Congo Red adsorption)
**PDF:** `仿生文献库/3rd/第C组-零数据原型/C4 - 扇贝壳（3 篇）/2021-Wang-shell-congo-red-adsorption.pdf`

| Row | Parameter | Verification Quote | Source Locator |
|-----|-----------|-------------------|----------------|
| 5 | 最大吸附容量 qmax (CR) = 495.5626 mg/g | "The maximum adsorption capacity of abalone HA microspheres for CR could reach 495.5626 mg/g when the initial CR concentration reaches 800 mg/L." | Wang2021 p.2 / Section 3.2 & Abstract |
| 6 | 不同温度下的吸附容量 (25/35/45°C) | "Temperature (K) 298: qe 159.7623 mg/g; 308: 135.6735 mg/g; 318: 128.3043 mg/g" | Wang2021 p.2 / Table 1 |

### Rows 7–8 — Zhang2021 (Shell-heavy-metal-passivation review)
**PDF:** `仿生文献库/3rd/第C组-零数据原型/C4 - 扇贝壳（3 篇）/2021-Zhang-shellfish-heavy-metal-passivation-review.pdf`

| Row | Parameter | Verification Quote | Source Locator |
|-----|-----------|-------------------|----------------|
| 7 | 煅烧牡蛎壳(800℃) Cd²⁺ 2184.29 / Pb²⁺ 1949.39 mg/g | "对 Cd²⁺ 最大吸附量达 2 184.29 mg·g⁻¹，对 Pb²⁺最大吸附量达 1 949.39 mg·g⁻¹" | Zhang2021 p.791 / Table 1 (800℃ 牡蛎壳行) |
| 8 | 煅烧双色牡蛎壳去除率 Cu/Co/Pb | "煅烧贝壳对铜、钴、铅的去除率可分别达到 94.4%、96.5%、96.7%（材料添加量为 2 g·L⁻¹；金属离子浓度为 10 mg·L⁻¹）" | Zhang2021 p.791 / Section 3.3 (ref [74] ESMAEILI等) |

### Rows 9–13 — Zhang2024 (Modified-shell-powder review)
**PDF:** `仿生文献库/3rd/第B组-新方向/B2-生物矿化模板/2024-Zhang-shell-powder-heavy-metal-review.pdf`

| Row | Parameter | Verification Quote | Source Locator |
|-----|-----------|-------------------|----------------|
| 9 | 煅烧改性对Pb吸附容量 (32.34→57.79 mg/g) | "煅烧前贝壳粉对铅离子的吸附容量为 32.34 mg/g；煅烧后的吸附容量为 57.79 mg/g" | Zhang2024 p.71 / Section 1.2 (ref [11] 王征等) |
| 10 | 贝壳基羟基磷灰石吸附容量 (Pb 20.0, Cd 2.5, Cr 9.5, Cu 7.5 mg/g) | "贝壳基羟基磷灰石对铅、镉、铬和铜 4 种重金属具有较强的吸附能力，其平均吸附容量分别达到 20.0、2.5、9.5 和 7.5 mg/g" | Zhang2024 p.71 / Section 1.2 (ref [14] 宋杨等) |
| 11 | 贝壳基羟基磷灰石去除率 (Pb 100%, Cr 51.7%, Cd 76%, Cu 52.2%) | "采用羟基磷灰石去除贝肉蒸煮液中重金属发现，铅、铬、镉和铜的去除率分别达到了 100.0%、51.7%、76.0%和 52.2%" | Zhang2024 p.71-72 / Section 1.2 (ref [14] 宋杨等) |
| 12 | 吸附剂用量对Cd去除率的影响 | "当吸附剂用量是 10.0 mg 的时候，Cd 离子去除率是 30%；当吸附剂用量是 20.0 mg 的时候，Cd 离子去除率是 70%；当吸附剂的用量超过 40.0 mg 的时候，溶液中的 Cd 离子被完全去除" | Zhang2024 p.72 / Section 2.1 (ref [20] 杜洋) |
| 13 | 改性贻贝壳粉Pb吸附容量 (57.8 mg/g) | "当铅离子初始浓度达到 100.0 mg/L 时，其吸附容量提升到 57.8 mg/g" | Zhang2024 p.73 / Section 2.3 (ref [25] 王权) |

### Existing `partial` rows (1–2, 4) — No changes needed
Rows 1, 2, and 4 already had `verification_quote` and `source_locator` fields populated. Verified they are consistent with the JSON. No modifications made.

---

## Validation Results

| Check | Result |
|-------|--------|
| `validate_consistency.py` | ✅ 1 pre-existing error (bone-structure, unrelated), 0 new errors |
| `check_chimera.py --strict` | ✅ 0 violations |

---

## Rules Compliance

- [x] No row set to `verified` — only `partial` or `missing_pdf`
- [x] No modifications to mechanisms, boundary_conditions, or engineering_constants
- [x] Did not run `build_prototypes_db.py`
- [x] Did not commit or push
- [x] `provenance_summary` updated to reflect actual counts
