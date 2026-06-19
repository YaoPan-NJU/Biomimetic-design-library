# v0.1-alpha Delivery Summary

generated: 2026-06-17
actor: Claude Code (Tasks 1-38)

## Final Data Statistics

| dimension | count |
|---|---|
| Active prototypes | 34 |
| Performance data rows | 957 |
| Mechanisms | 1,095 |
| Engineering constraints | 374 |
| Boundary rules | 18 |
| Has locator/quote | 955/957 (99.8%) |

## Decision Queue Final Status

| status | count |
|---|---|
| applied/resolved | 127 |
| deferred_v0.2 | 6 |
| pending_yao | 13 |
| **Total** | **146** |

## Validation Final Status

| script | result | notes |
|---|---|---|
| validate_consistency.py | ✅ 0 errors | 181 warnings (pre-existing) |
| check_chimera.py | ✅ 0 violations | All chimera contamination removed |
| check_causal_chain.py | ⚠️ 24 prototypes | Without qualified causal_chain cards |
| check_boundary_guardrail.py | ⚠️ 24 prototypes | Missing boundary_conditions in causal_chain |
| check_translation_specificity.py | ✅ 25/25 pass | |

## Build Status

`tools/build_prototypes_db.py`:
- NameError fixed
- Chimera check: 0 violations (direct check), 32 cached (build script issue)
- Build output: not generated due to cached chimera failure

## Session Work Summary (Tasks 1-38)

| round | tasks | key changes |
|---|---|---|
| Round 1 | Task 1-4 | Analysis: queue summary, boundary register, missing PDFs, roadmap |
| Round 2 | Task 5-7 | Fixes: metadata, wrong-source removal, queue update |
| Round 3 | Task 8-10 | Infrastructure: path normalization (610 fixes), queue batch update, lotus assessment |
| Round 4 | Task 11-13 | Reconciliation + verification: chlorella/BMT fixes, PDF recovery, 47 quotes added |
| Round 5 | Task 14-16 | Execution: 52 queue updates, lotus scope split (346→49), PDA OCR fix |
| Round 6 | Task 17-24 | Bulk: 92 caveats, lotus cleanup, 23 quotes, 6 scope notes, validation, delivery |
| Round 7 | Task 25-30 | Build fix, chimera cleanup (32→0), 12 queue updates, boundary rules |
| Round 8 | Task 31-35 | Mechanical fixes (8), enrichment deferral (6), final validation + tag |
| Round 9 | Task 33-38 | PDF path fixes (17), new PDF verification (43), DNA evidence build, diatom dedup, path cleanup |

## Known Limitations

1. **13 pending_yao items** (missing PDFs, scope decisions, value verification)
2. **6 deferred_v0.2 items** (enrichment structural issues)
3. **24 prototypes** without qualified causal_chain cards
4. **Build script** chimera cache issue (direct check passes)

## Chimera Cleanup Summary

| prototype | before | after | removed |
|---|---|---|---|
| mussel-foot-adhesion | 94 mechs, 54 perf | 88 mechs, 27 perf | cellulose/CNC contamination |
| polydopamine-coating | 66 mechs | 65 mechs | Stenocara/beetle mechanism |
| spider-silk | 36 mechs, 8 narr | 31 mechs, 4 narr | lotus/pitcher-plant contamination |
