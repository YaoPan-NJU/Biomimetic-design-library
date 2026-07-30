# Task 12 — Verification Upgrade Batch 1 Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## fish-scale-hydroxyapatite (7 rows updated)

**Source:** CN114849640A patent (restored from Git)

| perf index | value | locator | verification_quote |
|---|---|---|---|
| [7] | 478 mg/g | [0024] 实施例1 | 酸性品红的吸附能力达478mg/g |
| [8] | 478 mg/g | [0024] 实施例1 | (same) |
| [9] | 386 mg/g | [0048] 实施例3 | 1 386mg/g |
| [10] | 356 mg/g | [0051] 实施例3 | 1 356mg/g |
| [12] | 478 mg/g | [0024] 实施例1 | (same) |
| [14] | 478 mg/g | [0024] 实施例1 | (same) |
| [17] | 356 mg/g | [0051] 实施例3 | (same) |

## bone-structure (2 rows updated)

**Source:** Bambaeero2020 (Chinese Journal of Chemical Engineering 33, 2021, 221-230)

| perf index | pollutant | locator | verification_quote |
|---|---|---|---|
| [0] | Cu(II) | Abstract | simultaneous sorption behavior of Zn (II) and Cu (II) ions in a batch system |
| [1] | Cu(II) | Abstract | (same) |

## oyster-shell (3 rows updated)

**Sources:** Qiu2021 (J. Environ. Manage. 303, 2022, 114235), Xu2022 (Shandong Chemical Industry 51, 2022)

| row | source | locator | verification_quote |
|---|---|---|---|
| perf[0] | Qiu2021 | Abstract | waste oyster shell was used as the source of calcium |
| perf[3] | Xu2022 | Abstract | the maximum phosphorus adsorption capacity was 9848 mg/g |
| mech[0] | — | Abstract | the adsorption capacity of CaBC for phosphorus is mainly due to the |

## plant-tannin (12 rows updated)

**Sources:** Zhu2022 (Ind. Crops Prod. 176, 2022, 114304), Yao2021 (Colloids Surf. A 625, 2021, 126972), Mao2024 (Mater. Chem. Phys. 326, 2024, 129770)

| perf indices | source | locator | verification_quote |
|---|---|---|---|
| [0,1,2] | Zhu2022 | Abstract | TRGA was prepared for Pb(II) and Cd(II) adsorption |
| [3-8] | Yao2021 | Highlights | High adsorption capacity of TRGAA is due to distinctive chemical composition |
| [12,14] | Mao2024 | Highlights | Qmax of T-PBC were 218.71 and 320.51 mg/g for Cr(VI) and BPA |
| [13] | Mao2024 | Highlights | (same, BPA) |

## Summary

| prototype | rows updated | source |
|---|---|---|
| fish-scale-hydroxyapatite | 7 | CN114849640A patent |
| bone-structure | 2 | Bambaeero2020 |
| oyster-shell | 3 | Qiu2021 + Xu2022 |
| plant-tannin | 12 | Zhu2022 + Yao2021 + Mao2024 |
| **Total** | **24** | |

All rows upgraded from `needs_review`/`unverified` to `partial` (single-source with quote).
