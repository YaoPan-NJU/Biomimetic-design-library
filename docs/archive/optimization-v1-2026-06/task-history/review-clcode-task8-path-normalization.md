# Task 8 — Path Normalization Sweep Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Overview

Scanned `仿生文献库/` (578 PDFs) and cross-matched against 937 `source_file` entries across all `prototypes_db/**/*.json`.

## Results

| category | count | percentage |
|---|---|---|
| Direct/library match (already correct) | 189 | 20.2% |
| Variant match ( 2.pdf/ 3.pdf suffix or partial) | 610 | 65.1% |
| Truly unmatched | 138 | 14.7% |
| **Total** | **937** | **100%** |

**Match rate after normalization: 85.3%** (was ~18% before, because most paths used bare filenames)

## Paths Fixed by Prototype

| prototype | paths fixed | remaining unmatched |
|---|---|---|
| metal-organic-framework | 234 | 2 |
| starch-granule | 120 | 0 |
| cellulose-nanocrystal | 98 | 8 |
| chitosan | 47 | 66 |
| mussel-foot-adhesion | 32 | 10 |
| chlorella-cell-wall | 20 | 0 |
| plant-tannin | 15 | 0 |
| alginate | 11 | 29 |
| oyster-shell | 9 | 0 |
| scallop-shell | 7 | 0 |
| fish-scale-hydroxyapatite | 6 | 0 |
| mangrove-root | 5 | 0 |
| iron-oxidizing-bacteria | 4 | 0 |
| lotus-leaf | 1 | 3 |
| mycelium | 1 | 1 |
| polydopamine-coating | 0 | 4 |
| cell-membrane-ion-channel | 0 | 14 |
| lobster-exoskeleton | 0 | 1 |
| **Total** | **610** | **138** |

## Truly Unmatched (138 entries) — Need External Acquisition

### High-impact missing PDFs (affect many rows)

| PDF | affected rows | prototype |
|---|---|---|
| 2021-Keshvardoostchokami-chitosan-adsorption-adsorbent-wastewater-review.pdf | 1 | chitosan |
| 2020-Upadhyay-chitosan-adsorption-adsorbent-heavy-metal-review.pdf | 3 | chitosan |
| 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 14 | chitosan, MOF |
| 2025-Dong-alginate-adsorption-heavy-metal-dye-review.pdf | 26 | alginate |
| 2022-CN114887602A-聚多巴胺-纤维素-吸附-除磷.pdf | 4 | PDA |
| 2022-Shaeli-membrane-review.pdf | 14 | cell-membrane-ion-channel |
| 2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf | 1 | lobster |

### By prototype

| prototype | unmatched | key missing PDFs |
|---|---|---|
| chitosan | 66 | Aramesh2021, Upadhyay2020, Keshvardoostchokami2021, Vo2023 |
| alginate | 29 | Dong2025 (26 rows) |
| cell-membrane-ion-channel | 14 | Shaeli2022, Pachaiappan2022, Foorginezhad2025 |
| mussel-foot-adhesion | 10 | CN114849661A, Foroutan2021, Shi2021 |
| cellulose-nanocrystal | 8 | Syeda2021, Qiao2021 |
| polydopamine-coating | 4 | CN114887602A |
| lotus-leaf | 3 | Zheng2024, Usman2021, Li2023 |
| metal-organic-framework | 2 | Aramesh2021 |
| lobster-exoskeleton | 1 | Vo2023 |
| mycelium | 1 | Zhang2022 |

## Recovery Potential

Of the 138 unmatched entries:
- ~66 are chitosan review PDFs (likely need external download)
- ~29 are alginate Dong2025 (single PDF, 26 rows)
- ~14 are membrane review PDFs (likely need external download)
- ~10 are PDA patent PDFs (may exist under different filenames)
- ~19 are other scattered missing PDFs

**Estimated recovery if key PDFs are acquired:**
- Dong2025 → recovers 26 alginate rows
- Aramesh2021 → recovers 14 chitosan + 2 MOF rows
- Shaeli2022 → recovers 14 cell-membrane rows
- CN114887602A → recovers 4 PDA rows
- Total: ~56 rows from 4 PDFs

## Files Modified

All 15 prototype JSON files had source_file paths normalized:
- `prototypes_db/chitosan.json`
- `prototypes_db/plant-tannin.json`
- `prototypes_db/oyster-shell.json`
- `prototypes_db/scallop-shell.json`
- `prototypes_db/fish-scale-hydroxyapatite.json`
- `prototypes_db/chlorella-cell-wall.json`
- `prototypes_db/iron-oxidizing-bacteria.json`
- `prototypes_db/mycelium.json`
- `prototypes_db/mangrove-root.json`
- `prototypes_db/mussel-foot-adhesion.json`
- `prototypes_db/separation/lotus-leaf.json`
- `prototypes_db/materials_reference/alginate.json`
- `prototypes_db/materials_reference/cellulose-nanocrystal.json`
- `prototypes_db/materials_reference/metal-organic-framework.json`
- `prototypes_db/materials_reference/starch-granule.json`
