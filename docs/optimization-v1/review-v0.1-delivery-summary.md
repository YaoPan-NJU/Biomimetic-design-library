# v0.1-alpha Delivery Summary

generated: 2026-06-17
actor: Claude Code (Tasks 1-30)

## Final Data Statistics

| dimension | count |
|---|---|
| Active prototypes | 34 |
| Performance data rows | 957 |
| Mechanisms | 1,095 |
| Engineering constraints | 374 |
| Boundary rules | 24 |
| Rows with locator/quote | 955 (99.8%) |

## Verification Coverage

| status | description |
|---|---|
| Has locator/quote | 955/957 rows |
| Partial verification | ~70 rows (Task 12-13, 19-22) |
| Needs review | ~287 rows |
| Knowledge gap | ~3 rows |

## Decision Queue Status

| status | count |
|---|---|
| Applied/resolved | 119 |
| Pending Yao | 27 |
| **Total** | **146** |

## Validation Status

| script | result | notes |
|---|---|---|
| validate_consistency.py | ✅ 0 errors | 197 warnings (pre-existing) |
| check_chimera.py | ⚠️ 32 violations | Cached issue; direct check passes 0 |
| check_causal_chain.py | ⚠️ 24 prototypes | Without qualified causal_chain cards |
| check_boundary_guardrail.py | ❌ 24 prototypes | Missing boundary_conditions in causal_chain |
| check_translation_specificity.py | ✅ 25/25 pass | |

## Build Status

`tools/build_prototypes_db.py`:
- NameError fixed (sys.exit → _sys.exit)
- Chimera check: cached 32 violations (direct check_chimera.py passes 0)
- Build output: not generated due to cached chimera failure

## Session Work Summary (Tasks 1-30)

| round | tasks | key changes |
|---|---|---|
| Round 1 | Task 1-4 | Analysis: queue summary, boundary register, missing PDFs, roadmap |
| Round 2 | Task 5-7 | Fixes: metadata, wrong-source removal, queue update |
| Round 3 | Task 8-10 | Infrastructure: path normalization (610 fixes), queue batch update, lotus assessment |
| Round 4 | Task 11-13 | Reconciliation + verification: chlorella/BMT fixes, PDF recovery, 47 quotes added |
| Round 5 | Task 14-16 | Execution: 52 queue updates, lotus scope split (346→49), PDA OCR fix |
| Round 6 | Task 17-24 | Bulk: 92 caveats, lotus cleanup, 23 quotes, 6 scope notes, validation, delivery |
| Round 7 | Task 25-30 | Build fix, chimera cleanup (32→0 direct), 12 queue updates, boundary rules |

## Known Limitations

1. **27 pending_yao items** (missing PDFs, scope decisions, value verification)
2. **138 unmatched source_file paths** (PDFs not locally available)
3. **24 prototypes** without qualified causal_chain cards
4. **Build script** chimera cache issue (direct check passes)
5. **Enrichment mirrors** mostly empty/placeholder

## Chimera Cleanup Summary

| prototype | before | after | removed |
|---|---|---|---|
| mussel-foot-adhesion | 94 mechs, 54 perf | 88 mechs, 27 perf | cellulose/CNC contamination |
| polydopamine-coating | 66 mechs | 65 mechs | Stenocara/beetle mechanism |
| spider-silk | 36 mechs, 8 narr | 31 mechs, 4 narr | lotus/pitcher-plant contamination |
