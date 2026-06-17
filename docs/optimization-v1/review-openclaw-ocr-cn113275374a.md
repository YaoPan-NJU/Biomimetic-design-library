# OCR Verification Report — CN113275374A

**Date:** 2026-06-18
**Patent:** CN113275374A — 生物矿化重金属吸附专利
**Source:** Scanned images (CN113275374A-01.png through CN113275374A-11.png)

## Summary

OCR verification of 8 performance_data rows across 2 prototype files:
- `prototypes_db/iron-oxidizing-bacteria.json` (rows 0–3)
- `prototypes_db/fish-scale-hydroxyapatite.json` (rows 18–21)

All 8 rows updated from `missing_pdf`/`needs_review` → `partial`.

## Data Found in Patent

### Paragraph [0040] (p.5)
> 三种碳酸盐矿化菌混合后对Cd²⁺、Pb²⁺的去除率为98.52、99.49％，混合菌体的去除效果优于单一菌体。

Supports: 混合菌对Cd²⁺去除率 (98.52%), 混合菌对Pb²⁺去除率 (99.49%)

### 表1 (p.5–6): 不同混合比例碳酸盐矿化菌对Cd²⁺、Pb²⁺的去除效果

| 混合比例 | Cd²⁺去除率 | Pb²⁺去除率 |
|---------|-----------|-----------|
| 0.5:0.5:1 | 94.54% | 92.66% |
| 1:1:1 | 98.52% | 99.49% |
| 2:2:1 | 96.23% | 95.61% |

Supports: 不同混合比例对Cd²⁺去除率, 不同混合比例对Pb²⁺去除率

## Verification Notes

- All 8 data values match exactly between patent text and JSON values
- Row 0 (Cd²⁺ 98.52%): Matches paragraph [0040] text "98.52"
- Row 1 (Pb²⁺ 99.49%): Matches paragraph [0040] text "99.49"
- Row 2 (Cd²⁺ ratios): Matches 表1 rows for Cd²⁺ initial 10 mg/L
- Row 3 (Pb²⁺ ratios): Matches 表1 rows for Pb²⁺ initial 100 mg/L
- Conditions (200mL, 10g/L尿素, 2g/L乙酸钙, 30°C, 150r/min, 72h) match paragraph [0040]

## Files Modified

| File | Rows | Before | After |
|------|------|--------|-------|
| iron-oxidizing-bacteria.json | 0–3 | missing_pdf | partial |
| fish-scale-hydroxyapatite.json | 18–21 | needs_review | partial |

## Validation

- ✅ `validate_consistency.py`: 0 errors (pre-existing warnings only)
- ✅ `check_chimera.py --strict`: 0 violations
