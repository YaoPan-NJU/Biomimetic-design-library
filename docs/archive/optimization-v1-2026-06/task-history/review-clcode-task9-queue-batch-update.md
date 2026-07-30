# Task 9 — Decision Queue Batch Status Update Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Updates Applied

### Previously Updated (Task 7) — 10 items
| status | count |
|---|---|
| applied_metadata_fix | 7 |
| applied_wrongsource_removal | 1 |
| applied_scope_annotation | 1 |
| (F08-DNA-001 matched but already updated) | 1 |

### Newly Updated (Task 9) — 11 items
| id | new status | operation |
|---|---|---|
| F01-PLT-002 | applied_package_a1 | plant-tannin BPA pollutant fill |
| F01-WOOD-002 | applied_package_a1 | wood-xylem pollutant fills |
| F02-BONE-003 | applied_package_a1 | bone-structure Cu(II) pollutant |
| F02-OYS-001 | applied_package_a1 | oyster-shell phosphate pollutant |
| F09-DIAT-001 | applied_package_a1 | diatom path normalization |
| F09-DIAT-002 | applied_package_a1 | diatom dedup (performance) |
| F09-DIAT-003 | applied_package_a1 | diatom dedup (mechanism/constraint/narrative) |
| F02-BONE-001 | applied_package_b1 | bone Chen2021 MOF wrong-source |
| F03-CHL-001 | applied_package_b1 | chlorella dye vs Pb wrong-source |
| F03-CHL-003 | applied_package_b1 | chlorella CaO/nZVI wrong-source |
| F03-MYC-001 | applied_package_b1 | mycelium cellulose/nanocellulose wrong-source |
| F03-SRB-003 | applied_package_b1 | SRB iron-cycle wrong-source |
| F05-MOF-002 | applied_package_b1 | MOF Aramesh chitosan wrong-source |
| F05-MOF-003 | applied_package_b1 | MOF Cheng2024 membrane wrong-source |
| F09-DIAT-004 | applied_package_b1 | diatom wrong DOI |
| F09-DIAT-005 | applied_package_b1 | diatom microalgae template wrong-source |
| F11-FISH-005 | applied_package_b1 | fish-scale abalone/shell wrong-source |
| F11-FISH-006 | applied_package_b1 | fish-scale superwetting wrong-source |

**Note:** Some items matched multiple operation categories (e.g., path normalization in Package A1 + wrong-source in B1). The highest-priority status was applied.

## Current Queue Status Distribution

| status | count | meaning |
|---|---|---|
| pending_yao | 107 | Still awaiting Yao decision |
| applied_package_b1 | 11 | Qoder first-layer wrong-source cleared |
| applied_package_a1 | 7 | Package A1 low-risk cleanup |
| applied_metadata_fix | 6 | Task 5 metadata fixes |
| partially_applied_package_* | 8 | Various partial cleanups |
| applied_package_a8/a9 | 2 | Patent/remaining-core paths |
| applied_wrongsource_removal | 1 | Task 6 lotus/PDA/DNA |
| applied_scope_annotation | 1 | DNA aptamer biosensor scope |
| accepted_codex / resolved_codex | 3 | Accepted by Codex |
| **Total** | **146** | |

## Remaining 107 pending_yao Items

| category | count | action needed |
|---|---|---|
| wrong_source (not yet cleared) | ~12 | Yao approval → removal |
| missing_pdf | ~9 | Acquire PDFs or demote |
| needs_human_decision (scope) | ~25 | Yao individual review |
| needs_human_decision (values) | ~10 | Yao value verification |
| partial (more fixes needed) | ~18 | Further metadata work |
| knowledge_gap / inferred_only | ~15 | Acknowledge as gaps |
| supported/ready | ~12 | No action needed |
| scope decisions | ~6 | Yao decision |

## Items Still Needing Yao Decision (High Priority)

| id | prototype | question |
|---|---|---|
| F12-PDA-MU-001 | mussel-foot-adhesion | 32 duplicate rows: PDA vs mussel ownership? |
| F03-CMIC-001 | cell-membrane-ion-channel | Keep as separation or split from adsorption? |
| F14-B08-003 | coral-skeleton, magnetic-bacteria | Zero performance — keep, park, or retire? |
| F07-REG-001 | namib-beetle | Zero performance, scope overlap — keep parked? |
| F02-FISH-002 | fish-scale-hydroxyapatite | Dou2021 biochar: expand scope or split? |
| F10-STARCH-006 | starch-granule | Pb2+ 2000 mg/g extreme: verify primary source |
