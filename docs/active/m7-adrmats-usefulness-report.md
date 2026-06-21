# M7 ADRMATS Usefulness Hardening Report

**Date**: 2026-06-21
**HEAD**: (to be updated after commit)
**Branch**: review

## Executive Summary

M7 usefulness hardening complete. Deepened DT for 8 more high-impact prototypes, added honesty_summary and boundary_summary to all brief candidates, created brief usefulness regression check script. All validators pass.

## Changes Made

### DT Deepening (8 new prototypes)
| Prototype | Evidence Tier | Key Design Principle |
|-----------|--------------|---------------------|
| lotus-leaf | lead | 超疏水微纳层级结构→油水分离 |
| silk-fibroin | lead | β-折叠结晶+无定形区官能团 |
| iron-oxidizing-bacteria | lead | IOB→施氏矿物→含氧阴离子吸附 |
| cell-membrane-ion-channel | inference | 仿生离子通道→选择性分离 |
| bone-structure | fact | HAp离子交换→磷氯铅矿沉淀 |
| scallop-shell | lead | CaCO₃→CaO煅烧→重金属吸附 |
| mangrove-root | lead | 铁膜+根际微生物→重金属转化 |
| mycelium | lead | 几丁质/葡聚糖→生物吸附 |

**Total DT deepened**: 19/36 root prototypes (11 from M6 + 8 from M7)

### Brief Structure Improvements
- Added `honesty_summary`: human-readable explanation of candidate_honesty classification
- Added `boundary_summary`: concise count of hard/soft boundaries per candidate
- Both fields present in all 7 brief candidates

### Regression Check
- Created `tools/check_brief_usefulness.py`
- Checks: required fields, candidate_honesty validity, material_handle presence, honesty_summary, boundary_summary
- Result: 7/7 briefs pass, 0 issues

## Before/After Score Movement

| Case | Cand | Fact | Lead | Infer | BC | DT_ok |
|------|------|------|------|-------|-----|-------|
| BPA | 4 | 0 | 1 | 3 | 7 | 4/4 |
| Cr(VI) | 5 | 3 | 1 | 1 | 12 | 5/5 |
| Pb(II) | 8 | 3 | 4 | 1 | 19 | 6/8 |
| PFOA | 4 | 0 | 1 | 3 | 8 | 4/4 |
| SMX | 4 | 0 | 1 | 3 | 7 | 4/4 |
| 亚甲基蓝 | 5 | 0 | 2 | 3 | 8 | 5/5 |
| 油水分离 | 3 | 0 | 0 | 3 | 3 | 1/3 |

### Key Improvements from M6→M7
1. **DT coverage**: 11→19 prototypes deepened (73% → 53% of root still pending)
2. **honesty_summary**: Every candidate now has a human-readable explanation
3. **boundary_summary**: Every candidate has a concise boundary count
4. **Regression check**: Automated check prevents future quality regression

## Validation Results

| Validator | Result |
|-----------|--------|
| validate_consistency --strict | 0 errors, 171 warnings |
| check_chimera --strict | 0 violations |
| check_boundary_guardrail | PASS |
| canon_metrics --guard | GREEN |
| canon_metrics --check-integrity | PASS |
| verify_adrmats_delivery | 6/6 PASS |
| check_brief_usefulness | 7/7 PASS |

## Remaining Backlog

1. DT deepening for remaining 17 root prototypes
2. Honesty upgrade: most candidates still 'lead' not 'fact' — need PDF access for quote extraction
3. Boundary upgrade: most boundaries are llm_inferred — need from_source verification
4. Oil-water brief: all inference, no direct evidence
5. Full 60-80 prototype expansion (requires Yao authorization)

## Next Steps

Await Codex review. If accepted, continue usefulness iteration or expansion.
