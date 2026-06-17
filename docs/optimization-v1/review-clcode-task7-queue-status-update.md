# Task 7 — Decision Queue Status Update Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Updated Items

### From Task 5 (Metadata Fixes) — 7 items

| id | prototype | old status | new status | action taken |
|---|---|---|---|---|
| F01-SILK-002 | silk-fibroin | pending_yao | applied_metadata_fix | False precision 86.24%→86%, 96.29%→96% |
| F01-SILK-003 | silk-fibroin | pending_yao | applied_metadata_fix | Cleared invalid verification_quotes (paper titles) |
| F01-SILK-004 | silk-fibroin | pending_yao | applied_metadata_fix | Added inferred note for carboxyl group claim |
| F02-BMT-001 | biomineralization-template | pending_yao | applied_metadata_fix | Fixed provenance n_papers/n_verified, mechanism source |
| F02-OYS-002 | oyster-shell | pending_yao | applied_metadata_fix | Cleared title-like verification_quote |
| F05-MOF-001 | metal-organic-framework | pending_yao | applied_metadata_fix | Added verification semantics note |
| F10-STARCH-007 | starch-granule | pending_yao | applied_metadata_fix | Added mmol/g→mg/g conversion notes |

### From Task 6 (Wrong-Source Clearing) — 2 items

| id | prototype | old status | new status | action taken |
|---|---|---|---|---|
| F04-LOTUS-003 | lotus-leaf | pending_yao | applied_wrongsource_removal | Removed 9 membrane/distillation mechanisms |
| F12-PDA-MU-004 | PDA enrichment | pending_yao | applied_wrongsource_removal | Removed 21 wrong-source enrichment mechanisms |
| F08-DNA-001 | dna-aptamer | pending_yao | applied_scope_annotation | Added biosensor scope annotation |

## Current Queue Status Summary

| status | count (approx) |
|---|---|
| pending_yao | ~117 |
| applied_package_a1–a9 | 14 |
| applied_metadata_fix | 7 |
| applied_wrongsource_removal | 2 |
| applied_scope_annotation | 1 |
| partially_applied_* | 7 |
| accepted_codex / resolved_codex | 3 |

## Remaining pending_yao Breakdown

| category | count | action needed |
|---|---|---|
| wrong_source (batch approve) | ~18 | Yao batch approval |
| missing_pdf | ~9 | Acquire PDFs or demote |
| needs_human_decision | ~30 | Yao individual review |
| partial (metadata) | ~18 | More fixes needed |
| knowledge_gap / inferred_only | ~15 | Acknowledge as gaps |
| scope decisions | ~10 | Yao decision |
| supported/ready | ~12 | No action needed |
