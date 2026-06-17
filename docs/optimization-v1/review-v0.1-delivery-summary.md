# v0.1-alpha Delivery Summary

generated: 2026-06-17
actor: Claude Code (Tasks 1-24)

## Data Scale

| dimension | count |
|---|---|
| Active prototypes | 34 |
| Performance data rows | 918 |
| Mechanisms | 986 |
| Engineering constraints | 356 |
| Boundary rules | 54 (6 hard, 48 soft) |

## Verification Coverage

| status | rows | percentage |
|---|---|---|
| partial (with quote) | 49 | 5.3% |
| needs_review | 287 | 31.3% |
| knowledge_gap/missing_pdf | 3 | 0.3% |
| unverified/other | 579 | 63.1% |
| **Has verification_quote** | **48** | **5.2%** |

## Decision Queue Status

| status | count |
|---|---|
| applied/resolved | 107 |
| pending_yao | 39 |
| **Total** | **146** |

## Build Status

`tools/build_prototypes_db.py` **failed** with 32 blocklist violations:
- 3 prototypes with violations (likely pre-existing)
- Blocklist hits on "猪笼草", "荷叶" in mechanisms/narratives
- Script also has a `NameError: name 'sys' is not defined` bug

**Action needed:** Fix blocklist violations and script bug before v0.1 release.

## Validation Status

| script | result |
|---|---|
| validate_consistency.py | ✅ 0 errors, 132 warnings |
| check_chimera.py | ✅ 0 violations |
| check_causal_chain.py | ⚠️ 2 prototypes without qualified cards |
| check_boundary_guardrail.py | ❌ 2 prototypes missing BC |
| check_translation_specificity.py | ✅ 25/25 pass |

## Known Limitations

1. **39 pending_yao items** in decision queue (missing PDFs, scope decisions, value verification)
2. **138 unmatched source_file paths** (PDFs not locally available)
3. **OCR incomplete:** CN113244898A, CN114570339A, CN113275374A need full OCR
4. **Abu2023 Pb²⁺ 2000 mg/g** needs primary source cross-validation
5. **Dong2025 alginate review PDF** not acquired
6. **2 prototypes** (chlorella-cell-wall, diatom-frustule) missing boundary conditions

## Session Work Summary (Tasks 1-24)

| round | tasks | key changes |
|---|---|---|
| Round 1 | Task 1-4 | Analysis: queue summary, boundary register, missing PDFs, roadmap |
| Round 2 | Task 5-7 | Fixes: metadata, wrong-source removal, queue update |
| Round 3 | Task 8-10 | Infrastructure: path normalization (610 fixes), queue batch update, lotus assessment |
| Round 4 | Task 11-13 | Reconciliation + verification: chlorella/BMT fixes, PDF recovery, 47 quotes added |
| Round 5 | Task 14-16 | Execution: 52 queue updates, lotus scope split (346→49), PDA OCR fix |
| Round 6 | Task 17-24 | Bulk: 92 caveats, lotus cleanup, 23 quotes, 6 scope notes, validation, delivery |

**Total JSON modifications:** ~200+ across 25+ prototype files
**Total quotes added:** ~70 verification quotes with locators
**Total wrong-source removed:** ~300+ mechanisms/rows
