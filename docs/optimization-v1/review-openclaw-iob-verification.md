# Iron-Oxidizing-Bacteria Performance Data Verification Report

**Date:** 2026-06-18  
**Target:** `prototypes_db/iron-oxidizing-bacteria.json`  
**Method:** PDF text extraction via `pdftotext -layout`, exact quote matching

---

## Summary

| Metric | Count |
|--------|-------|
| Total performance_data rows | 23 |
| Needs review (before) | 23 |
| Updated to `partial` (PDF verified) | 19 |
| Updated to `missing_pdf` (scanned patent) | 4 |
| Needs review (after) | 0 |
| Mechanisms/boundary_conditions/eng_constraints modified | 0 |

---

## PDF Sources Used

### 1. Luo2021 — 施氏矿物除砷综述 (7 rows → partial)
- **File:** `2021-Luo-schwertmannite-arsenic-review.pdf`
- **DOI:** `10.7524/j.issn.0254-6108.2020070302`
- **Title:** 施氏矿物的矿物学特征及其除砷研究进展

| Parameter | Value | Source Locator | Quote (key fragment) |
|-----------|-------|----------------|---------------------|
| 施氏矿物7次循环后对As(V)去除率(pH 3.0) | 95.3% | p.3535 / Section 2.1.1 | "在 pH 3.0 和 pH 7.0 对 As(Ⅴ) 的去除率分别为 95.3% 和 63.9%" |
| 施氏矿物7次循环后对As(V)去除率(pH 7.0) | 63.9% | p.3535 / Section 2.1.1 | (same) |
| 施氏矿物7次循环后对As(III)去除率(pH 3.0) | 31.0% | p.3535 / Section 2.1.1 | "在 pH 3.0 和 pH 7.0 对 As(Ⅲ) 的去除率分别为 31.0% 和 81.6%" |
| 施氏矿物7次循环后对As(III)去除率(pH 7.0) | 81.6% | p.3536 / Section 2.1.1 | (same) |
| 生物施氏矿物对As(III)最大去除率及pH范围 | >98% at pH 7-9 | p.3536 / Section 2.1.2(3)pH | "As(Ⅲ) 的最大去除率发生在 pH 7—9 左右，最大去除率超过 98%" |
| 加热温度对生物施氏矿物As(III)去除率的影响(105°C) | 25.1% | p.3536 / Section 2.1.2(4)温度 | "105 ℃ 干燥的 0.25 g·L⁻¹ 施氏矿物…As(Ⅲ) 去除率为 25.1%" |
| 加热温度对生物施氏矿物As(III)去除率的影响(250°C) | 93.0% | p.3536 / Section 2.1.2(4)温度 | "当使用 250 ℃ 加热的施氏矿物作为吸附剂时，去除效率提高到 93.0%" |

### 2. Xu2022 — BKFMs Sb/As吸附 (4 rows → partial)
- **File:** `2022-Xu-arsenic-antimony-adsorption-water-treatment.pdf`
- **DOI:** `10.1016/j.clay.2021.106392`
- **Title:** Simultaneous removal of antimony(III/V) and arsenic(III/V) from aqueous solution by bacteria–mediated kaolin@Fe–Mn binary (hydr)oxides composites

| Parameter | Value | Source Locator | Quote (key fragment) |
|-----------|-------|----------------|---------------------|
| 最大吸附容量 qmax (Sb(III), Langmuir) | 177.19 mg/g | p.5 / Section 3.3 | "the calculated maximum adsorption capacities were 177.19, 56.26, 62.92 and 42.18 mg/g for Sb(III), Sb(V), As(III) and As(V), respectively" |
| 最大吸附容量 qmax (Sb(V), Langmuir) | 56.26 mg/g | p.5 / Section 3.3 | (same) |
| 最大吸附容量 qmax (As(III), Langmuir) | 62.92 mg/g | p.5 / Section 3.3 | (same) |
| 最大吸附容量 qmax (As(V), Langmuir) | 42.18 mg/g | p.5 / Section 3.3 | (same) |

### 3. Jhariya2024 — 施氏矿物/黄钾铁矾除Se (8 rows → partial)
- **File:** `2024-Jhariya-schwertmannite-jarosite-adsorption.pdf`
- **DOI:** `10.1016/j.jhazmat.2024.136256`
- **Title:** Effective selenate removal using pH modulated synthesis of biogenic jarosite

| Parameter | Value | Source Locator | Quote (key fragment) |
|-----------|-------|----------------|---------------------|
| J-2.5对Se(VI)去除率(0.2 mM) | 63% | p.7 / Section 3.3 | "achieving 63 % removal (0.13 mmol/g) at 0.20 mM" |
| J-2.5对Se(VI)去除率(2.0 mM) | 15% | p.7 / Section 3.3 | "and 15 % (0.30 mmol/g) at 2.0 mM Se(VI)" |
| J-3.5对Se(VI)去除率(0.2 mM) | 16% | p.7 / Section 3.3 | "showed significantly lower removal efficiencies of 16 % (0.03 mmol/g) at 0.20 mM" |
| J-90C对Se(VI)去除率(0.2 mM) | 9% | p.7 / Section 3.3 | "exhibited the lowest removal efficiencies among the jarosite's, with 9 % (0.02 mmol/g) at 0.20 mM" |
| S-2.5对Se(VI)去除率(0.2 mM) | 77% | p.7 / Section 3.3 | "achieving 77 % removal (0.16 mmol/g) at 0.20 mM Se(VI)" |
| S-2.5对Se(VI)去除率(2.0 mM) | 33% | p.7 / Section 3.3 | "and 33 % (0.65 mmol/g) at 2.0 mM Se(VI)" |
| EDS元素原子比(J-2.5 after Se removal) | Fe(1.0):S(0.36):K(0.05):Se(0.04) | p.8 / Section 3.3 | "a uniformly distributed atomic ratio of Fe(1.0): S(0.36): K(0.05): Se(0.04)" |
| EDS元素原子比(S-2.5 after Se removal) | Fe(1.0):S(0.11):Se(0.11) | p.8 / Section 3.3 | "S-2.5 showed a uniform distribution of the S (0.11): Fe (1.0): Se (0.11) atomic ratio" |

### 4. CN113275374A — 扫描专利 (4 rows → missing_pdf)
- **File:** `2021-CN113275374A-biomineralization-heavy-metal.pdf`
- **Status:** Scanned patent, OCR processing needed
- **Rows affected:** 混合菌对Cd²⁺去除率, 混合菌对Pb²⁺去除率, 不同混合比例对Cd²⁺去除率, 不同混合比例对Pb²⁺去除率

---

## Provenance Summary (updated)

```json
{
  "n_papers": 7,
  "n_verified": 0,
  "n_unverified": 0,
  "n_partial": 19
}
```

---

## Validation Results

| Check | Result |
|-------|--------|
| `validate_consistency.py` | ✅ 1 pre-existing error (bone-structure, unrelated), 181 warnings (all pre-existing) |
| `check_chimera.py --strict` | ✅ 0 violations |

---

## Notes

- All 19 literature-sourced rows matched exact values in their respective PDFs. Verification set to `partial` (not `verified`) per hard rules.
- All 4 patent rows marked `missing_pdf` with note "Scanned patent, OCR processing needed".
- No changes made to mechanisms, boundary_conditions, or engineering_constraints.
- `build_prototypes_db.py` was not run.
- No git commits or pushes made.
