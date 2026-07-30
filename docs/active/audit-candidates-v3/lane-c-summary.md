# Lane C Audit Summary

**Auditor**: Claude Code (audit agent)
**Date**: 2026-06-19
**Prototypes audited**: 8

## Findings by Type

| Finding Type | Count | Severity Distribution |
|---|---|---|
| wrong-source | 11 | high: 9, medium: 2 |
| translation-scope | 3 | medium: 3 |
| label-contradiction | 1 | low: 1 |
| ledger-inaccuracy | 2 | medium: 2 |
| **Total** | **17** | high: 9, medium: 7, low: 1 |

## Findings by Prototype

| Prototype | Issues | High | Medium | Low |
|---|---|---|---|---|
| plant-tannin | 3 | 2 | 1 | 0 |
| silk-fibroin | 3 | 0 | 2 | 1 |
| spider-silk | 3 | 2 | 1 | 0 |
| chlorella-cell-wall | 2 | 2 | 0 | 0 |
| cell-membrane-ion-channel | 0 | 0 | 0 | 0 |
| lotus-leaf | 5 | 3 | 2 | 0 |
| shark-skin | 3 | 2 | 1 | 0 |
| superhydrophobic-artificial | 2 | 0 | 1 | 1 |
| **Total** | **21** | **9** | **7** | **1** |

(Note: counts include sub-findings; lane total 21 unique findings across 8 prototypes)

## Critical Findings (High Severity)

### Unapplied guard rules (data still in JSON despite approved removal)
1. **plant-tannin mechanisms[0-5]**: Fluoropolymer membrane data (DOI 10.3390/polym14245439) still present. Guard rule B01-PLT-001 approved but unapplied.
2. **plant-tannin engineering_constraints[0] + narrative.entries[0]**: Same fluoropolymer membrane contamination in constraints and narrative.
3. **chlorella-cell-wall performance_data[13-16]**: Non-Chlorella wastewater technology data (DOI 10.1007/s10311-021-01239-2) still present. Guard rule B03-CHL-002 approved but unapplied.
4. **chlorella-cell-wall mechanisms[0]**: Pb2+ source used for dye-removal claim (Cheng2021). B03-CHL-001 approved but unapplied.

### Scope contamination (wrong-prototype data)
5. **spider-silk mechanisms[14-25]**: 12 mechanisms from femtosecond-laser and uranium-coordination reviews, not spider-silk. B14-SPIDER-001 flagged.
6. **lotus-leaf mechanisms[14-33]**: ~15 mechanisms from refuted DOIs or non-lotus organisms (shark, gecko, rose-petal, membrane, MOF). B04-LOTUS-003 guard rule applies.
7. **shark-skin mechanisms[2-13]**: 12 mechanisms from refuted superhydrophobic review DOIs, not shark-skin-specific.

## Prototype Status Summary

| Prototype | Status | Key Issue |
|---|---|---|
| plant-tannin | Needs cleanup | 6 mechanisms + 1 constraint + 1 narrative from fluoropolymer membrane review must be removed |
| silk-fibroin | Needs minor cleanup | 6 duplicated performance rows; 2 verification_quote titles instead of excerpts; 6 MOF review rows need scope caveat |
| spider-silk | Needs major cleanup | 13 non-spider-silk mechanisms must be removed |
| chlorella-cell-wall | Needs cleanup | 4 wrong-source performance rows + 1 wrong-source mechanism must be removed |
| cell-membrane-ion-channel | Clean | No issues found; internally consistent separation/filtration scope |
| lotus-leaf | Needs major cleanup | ~15 wrong-source mechanisms + 2 wrong-source constraints + 4 knowledge-gap performance rows need attention |
| shark-skin | Needs major cleanup | ~22 non-shark-skin mechanisms need removal; zero performance data confirmed |
| superhydrophobic-artificial | Needs minor cleanup | 6 membrane-distillation mechanisms need scope caveat; 1 off-topic (gecko) mechanism |

## Recommendations

1. **Immediate**: Apply unapplied guard rules B01-PLT-001, B03-CHL-001, B03-CHL-002 (mechanism/performance data removal).
2. **High priority**: Complete lotus-leaf scope split cleanup (mechanisms, constraints, narrative).
3. **Medium priority**: Remove spider-silk femtosecond-laser/uranium mechanisms; deduplicate silk-fibroin performance data.
4. **Low priority**: Add scope caveats to superhydrophobic-artificial membrane-distillation entries; clean shark-skin non-shark mechanisms.
