# Task 3 — Missing PDF Source Analysis

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Overview

Across all `prototypes_db/*.json` files:
- **167** source_file paths found locally ✓
- **748** source_file paths NOT found locally ✗
- **18 prototypes** affected

## Impact by Prototype

| prototype | missing unique PDFs | affected rows | severity |
|---|---|---|---|
| chitosan | 34 | ~113/117 | **critical** — 97% rows unverified |
| metal-organic-framework | 28 | ~252 | high — most rows single_source |
| cellulose-nanocrystal | 27 | ~108 | high — overbroad store |
| mussel-foot-adhesion | 12 | ~32 | medium — duplicates with PDA |
| starch-granule | 10 | ~121 | high — all rows unverified |
| chlorella-cell-wall | 7 | ~21 | medium |
| alginate | 5 | ~36 | medium — Dong2025 drives 26 rows |
| plant-tannin | 4 | ~14 | low — most rows applied |
| lotus-leaf | 4 | ~4 | low — overaggregated scope |
| cell-membrane-ion-channel | 3 | ~14 | low — scope decision pending |
| oyster-shell | 3 | ~13 | low — partial applied |
| fish-scale-hydroxyapatite | 2 | ~28 | low — CN113275374A is scanned |
| mycelium | 2 | ~5 | low — wrong_source pending |
| scallop-shell | 2 | ~7 | low — generic reviews |
| iron-oxidizing-bacteria | 1 | ~22 | low — partial applied |
| lobster-exoskeleton | 1 | ~1 | low — single row |
| mangrove-root | 1 | ~5 | low — system-level evidence |
| polydopamine-coating | 1 | ~4 | low — CN114887602A only |

## Critical Missing PDFs (Highest Impact)

### Tier 1: Chitosan (34 PDFs, ~113 rows blocked)

The chitosan prototype is the most affected. Key missing PDFs:

| DOI | filename | affected rows | priority |
|---|---|---|---|
| 10.1016/j.ijbiomac.2021.04.158 | Aramesh2021 chitosan dye-removal review | ~14 | high |
| 10.1016/j.carbpol.2020.117000 | Upadhyay2020 chitosan heavy-metal review | ~3 | high |
| 10.1007/s10311-023-01563-9 | Vo2023 chitosan/HAp membrane review | ~1 | medium |
| 10.1016/j.rechem.2024.101332 | Hsu2024 chitosan heavy-metal review | ~1 | medium |
| various | 30 more review/patent PDFs | ~94 | mixed |

**Note:** Most missing chitosan PDFs are review papers. The actual experimental data rows may be review-table summaries rather than primary-source qmax values.

### Tier 2: MOF (28 PDFs, ~252 rows affected)

| DOI | filename | affected rows | priority |
|---|---|---|---|
| various | 28 MOF review/primary PDFs | ~252 | high |

**Note:** MOF `n_verified=252` is inflated by `single_source` semantics. Many rows may be review-table values even after PDF acquisition.

### Tier 3: Cellulose-Nanocrystal (27 PDFs, ~108 rows affected)

**Note:** The CNC store is overbroad (mixes CNC, CNF, cellulose, composite, membrane rows). Scope splitting should precede PDF acquisition.

### Tier 4: Starch-Granule (10 PDFs, ~121 rows affected)

**Note:** All starch rows are unverified. Extreme values (CV 24,375 mg/g, oil 13,000 mg/g) need source verification before ranking.

## PDFs Found Under Variant Paths

Some "missing" PDFs exist locally under different paths or with ` 2.pdf` suffixes:

| source_file in JSON | actual local path | status |
|---|---|---|
| `2021-CN113275374A-biomineralization-heavy-metal.pdf` | `仿生文献库/3rd/第三波-仿生吸附专利/2021-CN113275374A-...pdf` | **found** |
| `2021-Dou-hydrophobic-porous-biochar-adsorption.pdf` | `仿生文献库/论文/第4组-生物矿化/2021-Dou-... 2.pdf` | **found** (with ` 2.pdf` suffix) |

**Path normalization opportunity:** Several missing PDFs may actually exist with ` 2.pdf` suffixes or in subdirectories. A systematic path scan could recover ~20-30% of "missing" PDFs.

## Truly Missing PDFs (Need External Acquisition)

These PDFs were not found under any local path variant:

| priority | PDF | reason |
|---|---|---|
| **critical** | Aramesh2021 (10.1016/j.ijbiomac.2021.04.158) | Affects 14 chitosan dye rows |
| **critical** | Upadhyay2020 (10.1016/j.carbpol.2020.117000) | Affects 3 chitosan heavy-metal rows |
| **critical** | Dong2025 | Affects 26 alginate rows |
| **critical** | CN114887602A patent | Affects 4 PDA phosphorus rows |
| **high** | Vo2023 (10.1007/s10311-023-01563-9) | Affects lobster + chitosan rows |
| **high** | ~20 MOF review PDFs | Affects MOF ranking |
| **medium** | ~10 starch review PDFs | Affects starch ranking |
| **low** | ~30 other review/patent PDFs | Various prototypes |

## Recommendations

1. **Path normalization sweep** — Re-scan `仿生文献库/` for ` 2.pdf`/` 3.pdf` variants of currently "missing" PDFs. Estimated recovery: 20-30%.
2. **Acquire Tier 1 PDFs** — Download Aramesh2021, Upadhyay2020, Dong2025, CN114887602A from DOI/patent databases.
3. **Demote unverified rows** — For PDFs that cannot be acquired, demote affected rows to `missing_pdf` status and exclude from ranking.
4. **Scope splitting before acquisition** — For CNC and MOF, split overbroad stores before investing in PDF acquisition.
