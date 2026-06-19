# Task 17 — Scope Caveats + Metadata Batch Write Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Summary

**92 changes** across 13 JSON files.

## Changes by Category

### Keep-Soft Caveats (67 changes)
| prototype | rows | caveat |
|---|---|---|
| wood-xylem | perf[0-1] | biomass biochar, not preserved xylem-channel |
| oyster-shell | perf[6-12] | generic shell review, not oyster-specific |
| scallop-shell | perf[0-6] | generic modified-shell review |
| fish-scale-hydroxyapatite | perf[2-6] | rice-husk HAp biochar, not fish-scale |
| chlorella-cell-wall | perf[6-7] | algal-derived-biochar |
| chlorella-cell-wall | perf[8-21] | general-algae-background |
| superhydrophobic-artificial | Li2022 rows | fluoropolymer membrane background |
| alginate | Pan rows | composite (chitosan-alginate) |
| cellulose-nanocrystal | CN121130847A rows | bio-foam |
| cellulose-nanocrystal | Radjai2022 rows | cellulose-diatomite composite |

### Scope Decisions (4 changes)
| prototype | change |
|---|---|
| cellulose-nanocrystal | provenance_summary.scope = broad_cellulose_family |
| pitcher-plant-slippery-surface | scope note: surface engineering, not adsorption |
| spider-silk | scope_caveat: broad superhydrophobic spillover |

### Value Fixes (25 changes)
| prototype | rows | fix |
|---|---|---|
| plant-tannin | perf[11] | 3429 mg/g physically unusual caveat |
| starch-granule | perf[52-59] | metric_type = concentration_dependent_uptake |
| starch-granule | perf[66-76] | source_type = review_maximum |
| starch-granule | perf[73] | material_class = superhydrophobic_cryogel |
| starch-granule | all 121 rows | verification: unverified → needs_review |
| polydopamine-coating | perf[23-25] | material_class = CNF-TA-PMMT-PEI_composite |

### Mechanical Metadata (2 changes)
| prototype | change |
|---|---|
| biomineralization-template | Added Wang2025 Nd3+ 787.93 mg/g performance row |
