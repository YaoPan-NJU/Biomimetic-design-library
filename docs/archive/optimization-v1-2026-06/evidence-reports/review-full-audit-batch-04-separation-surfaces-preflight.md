# Full Audit Batch 04: separation/superwetting surfaces preflight

status: codex_preflight_reviewed

## Scope

- **Batch ID:** `full-audit-04-separation-surfaces`
- **Prototype JSONs:** `prototypes_db/separation/lotus-leaf.json`, `prototypes_db/separation/shark-skin.json`, `prototypes_db/separation/water-strider-leg.json`, `prototypes_db/separation/cactus-spine.json`, `prototypes_db/separation/superhydrophobic-artificial.json`
- **Audit date:** 2026-06-16
- **Worker:** Codex local JSON/PDF text audit (`jq`, `rg --files -uuu`, `pdftotext`)
- **Reason for preflight:** the separation/superwetting prototypes are highly cross-contaminated by review-level special-wettability, membrane, antifouling, fog-collection, and artificial sponge evidence. The main risk is prototype-scope mixing rather than lack of literature. No `prototypes_db/*.json` files were modified.

## Prototype Coverage

| prototype_id | path | performance_data | mechanisms | engineering_constraints | narrative_entries | provenance_summary |
|---|---|---:|---:|---:|---:|---|
| lotus-leaf | `prototypes_db/separation/lotus-leaf.json` | 4 | 355 | 22 | 33 | 36 papers, 0 verified, 359 unverified |
| shark-skin | `prototypes_db/separation/shark-skin.json` | 0 | 31 | 1 | 4 | 5 papers, 0 verified, 31 unverified |
| water-strider-leg | `prototypes_db/separation/water-strider-leg.json` | 0 | 61 | 0 | 5 | 5 papers, 0 verified, 61 unverified |
| cactus-spine | `prototypes_db/separation/cactus-spine.json` | 0 | 11 | 0 | 3 | 3 papers, 0 verified, 11 unverified |
| superhydrophobic-artificial | `prototypes_db/separation/superhydrophobic-artificial.json` | 8 | 78 | 8 | 4 | 8 papers, 0 verified, 96 unverified |

## Audit Summary

- All five JSONs have `provenance_summary.n_verified = 0`, so even in-domain claims should remain unverified until source paths, locators, and quotes are added.
- `lotus-leaf` is currently a general superhydrophobic/oil-water-separation aggregator, not a clean lotus-leaf prototype. It mixes lotus effect, water strider, shark skin, gecko/rose-petal, Janus membranes, membrane distillation, antibacterial coatings, MOFs, artificial sponges, and shell/graphene evidence.
- `shark-skin`, `water-strider-leg`, and `cactus-spine` have no performance rows. Their mechanisms are mostly generic special-wettability or antifouling/fog-collection review rows, so they should be treated as background until direct prototype-specific evidence is added.
- `superhydrophobic-artificial` has the strongest directly supported performance evidence in this batch. CN113244892B supports superhydrophobic/oleophilic biochar foam adsorption capacities of 132-233 g/g for organic liquids, and CN121130847A supports MOF-modified bio-based foam adsorption of 51.5-122 g/g. These are artificial materials, not lotus-leaf biological evidence.
- Several `lotus-leaf` performance sources are missing or path-mismatched locally. `2022-Khan-wastewater-water-treatment-review` exists with ` 2.pdf`/` 3.pdf` suffixes, but the row is scallop-shell-template 3D graphene foam evidence, not lotus-leaf performance.

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SEP-PATH-01 | all Batch 04 JSONs | target_json path | metadata | Batch 04 files live under `prototypes_db/separation/`, not repository root. | local filesystem | N/A | Y | path scan | N/A | supported | use_full_relative_path_in_future_edits | Prevent cleanup scripts from targeting missing root-level JSONs. |
| LOTUS-SCOPE-01 | `prototypes_db/separation/lotus-leaf.json` | entire prototype | scope | 4 performance rows, 355 mechanisms, 22 constraints, and 33 narrative entries are aggregated from broad superwetting/separation literature. | multiple sources | multiple | mixed | JSON/source grouping | N/A | partial | split_or_reassign_before_row_edits | Scope cleanup should precede detailed quote insertion. |
| LOTUS-PF-01 | `prototypes_db/separation/lotus-leaf.json` | performance_data[0], [2], [3] | performance | Three lotus performance rows point to missing or path-mismatched PDFs in the local library. | Zheng2024, Usman2021, Li2023 review paths | multiple | N in path scan | N/A | N/A | missing_pdf | locate_pdf_or_demote | Only extraction JSON/visual cache was found for several cited sources. |
| LOTUS-PF-02 | `prototypes_db/separation/lotus-leaf.json` | performance_data[1] | performance | 3D graphene foam from scallop-shell template adsorbs oils/solvents up to 250x own weight. | `2022-Khan-wastewater-water-treatment-review 2.pdf` | 10.3390/jmse10040534 | Y | functional-materials review / cited Shi2016 example | "functional materials...oil-water separation" | keep_soft | reassign_or_caveat | Review supports wastewater/oil separation and scallop-shell/graphene context, not direct lotus-leaf performance. |
| LOTUS-MC-01 | `prototypes_db/separation/lotus-leaf.json` | mechanisms[*], engineering_constraints[*], narrative.entries[*] | mechanism/engineering/narrative | Many entries are non-lotus special-wettability examples: water strider, shark skin, gecko, rose petal, Janus membranes, membrane distillation, antibacterial coatings, MOF, artificial sponge, shell/graphene. | multiple review and patent sources | multiple | mixed | title/domain/source grouping | non-lotus domains | wrong_source | split_to_correct_prototypes_or_demote | Do not report these as lotus-leaf-specific evidence. |
| SHARK-SCOPE-01 | `prototypes_db/separation/shark-skin.json` | entire prototype | scope | Zero performance rows; mechanisms are mostly generic antifouling/superhydrophobic review rows and include lotus/gecko/rose-petal examples. | multiple review sources | multiple | mixed | JSON/source grouping | N/A | keep_soft | add_direct_shark_evidence_or_demote | Current file supports background antifouling topology more than direct adsorption/separation performance. |
| WSTR-SCOPE-01 | `prototypes_db/separation/water-strider-leg.json` | entire prototype | scope | Zero performance rows; mechanisms are mostly generic superhydrophobic, electrospun, membrane-distillation, Janus, and wetting-theory rows. | multiple review sources | multiple | mixed | JSON/source grouping | N/A | keep_soft | add_direct_water_strider_evidence_or_demote | Treat as wetting-design background until direct evidence is sourced. |
| CACT-SCOPE-01 | `prototypes_db/separation/cactus-spine.json` | entire prototype | scope | Zero performance rows; mechanisms mix 2021 penetration/electrospinning review content with 2022 ADFM honeycomb/desert-beetle/pitcher-inspired fog collection. | 2021-Penetration review; 2022-ADFM review | multiple | mixed | JSON/source grouping | N/A | keep_soft | split_cactus_beetle_fog_collection | Current file is not cactus-spine-specific enough for direct recommendations. |
| SHART-PF-01 | `prototypes_db/separation/superhydrophobic-artificial.json` | performance_data[1-7], engineering_constraints[4-7] | performance/engineering | CN113244892B supports superhydrophobic/oleophilic biochar foam capacities of 132-233 g/g, single-solvent values, Q formula, pH 1-11 stability, and recyclability. | `仿生文献库/专利/2022-CN113244892B-超疏水-吸附-泡沫 2.pdf` | patent | Y | [0060]-[0067] | "132-233g/g"; "pH值1-11" | supported | add_quote_locator_and_normalize_metadata | Strongest performance evidence in Batch 04 for artificial superhydrophobic adsorbent foam. |
| SHART-PF-02 | `prototypes_db/separation/superhydrophobic-artificial.json` | performance_data[0], engineering_constraints[1-3] | performance/engineering | CN121130847A supports MOF-modified bio-based foam adsorption of 51.5-122 g/g and DCM cycling from 70.7 to 61.7 g/g after 20 cycles. | `仿生文献库/专利/2025-CN121130847A-壳聚糖-纤维素-生物基-MOF 2.pdf` | patent | Y | [0034], [0037], [0045] | "51.5-122g/g"; "70.7g/g...61.7g/g" | supported | add_quote_locator_and_fix_source_path | Row source path is missing the patent directory prefix. |
| SHART-CA-01 | `prototypes_db/separation/superhydrophobic-artificial.json` | performance_data[0], related mechanisms | classification | The key CN121130847A example reports WCA around 140.01 degrees after diazotization, below the usual >=150 degree superhydrophobic threshold. | CN121130847A PDF | patent | Y | [0036] | "平均值为140.01" | partial | label_as_high_hydrophobic_unless_extra_support | Do not rely on this example alone to prove superhydrophobicity. |
| SHART-MC-01 | `prototypes_db/separation/superhydrophobic-artificial.json` | mechanisms[19-24], engineering_constraints[0] | mechanism/engineering | DOI 10.3390/polym14245439 is a fluoropolymer membrane-distillation review. It is in-domain for membranes but not direct adsorption-foam evidence. | Li2022 fluoropolymer membrane review | 10.3390/polym14245439 | Y in prior audits | title/domain check | membrane distillation / membrane crystallization | keep_soft | keep_as_membrane_background_or_reassign | Same DOI was wrong-source for plant-tannin; here it is still not foam adsorption evidence. |
| LOTUS-PAT-01 | `prototypes_db/separation/lotus-leaf.json` | narrative.entries[32] and related artificial-sponge references | narrative/mechanism | CN114874407A supports an artificial TiO2/flourosilane superhydrophobic sponge: WCA 151 degrees, >150 after pH 2/13 durability, >98% separation after 30+ cycles, 60-120x organic-liquid absorption. | `仿生文献库/专利/2022-CN114874407A-超疏水-海绵 2.pdf` | patent | Y | [0035]-[0038] | "接触角为151°"; "60-120倍" | supported | reassign_to_artificial_sponge_scope | Strong artificial-sponge evidence, not direct lotus-leaf biological performance. |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| LOTUS-BD-01 | `prototypes_db/separation/lotus-leaf.json` | entire prototype | knowledge_gap | `lotus-leaf` has zero verified provenance and a broad overaggregated evidence pool. | Do not use current rows as verified lotus-specific evidence until split and quoted. | aggregate | JSON/provenance scan | `n_verified = 0` | partial | Scope cleanup first. |
| LOTUS-BD-02 | `prototypes_db/separation/lotus-leaf.json` | performance_data[0], [2], [3] | knowledge_gap | Several cited performance PDFs are missing or path-mismatched locally. | These performance rows cannot support design decisions yet. | Zheng2024/Usman2021/Li2023 cited paths | path scan | N/A | missing_pdf | Locate PDFs or demote. |
| LOTUS-BD-03 | `prototypes_db/separation/lotus-leaf.json` | non-lotus mechanism/performance groups | hard_do_not | Non-lotus examples must not be reported as lotus-leaf-specific evidence. | Would merge water-strider, shark, gecko, rose-petal, membrane, MOF, shell, and artificial-sponge mechanisms into one biological prototype. | multiple sources | title/domain check | non-lotus domains | wrong_source | Split/reassign after Yao approval. |
| SHARK-BD-01 | `prototypes_db/separation/shark-skin.json` | entire prototype | knowledge_gap | Zero performance rows and mostly generic antifouling/superhydrophobic mechanisms. | Do not rank as a verified adsorption/separation performer until direct shark-skin evidence is added. | aggregate | JSON/provenance scan | N/A | knowledge_gap | Keep background only. |
| WSTR-BD-01 | `prototypes_db/separation/water-strider-leg.json` | entire prototype | knowledge_gap | Zero performance rows and generic wetting/membrane rows dominate. | Do not use as direct water-strider-leg performance evidence. | aggregate | JSON/provenance scan | N/A | knowledge_gap | Keep wetting-design background only. |
| CACT-BD-01 | `prototypes_db/separation/cactus-spine.json` | entire prototype | knowledge_gap | Zero performance rows and mixed cactus/desert-beetle/honeycomb/pitcher-inspired fog-collection content. | Do not treat current fields as cactus-spine-specific adsorption/separation evidence. | aggregate | JSON/source grouping | N/A | keep_soft | Split fog-harvesting prototypes if retained. |
| SHART-BD-01 | `prototypes_db/separation/superhydrophobic-artificial.json` | performance_data[1-7], engineering_constraints[4-7] | soft_boundary | CN113244892B evidence is for organic-liquid/oil adsorption by superhydrophobic/oleophilic biochar foam, including pH 1-11 stability. | Do not generalize these capacities to inorganic aqueous pollutants or non-oil wastewater without extra evidence. | CN113244892B PDF | [0060]-[0067] | "二氯甲烷、苯乙烯、邻二甲苯、正己烷、石油醚" | supported | Good condition-specific artificial foam evidence. |
| SHART-BD-02 | `prototypes_db/separation/superhydrophobic-artificial.json` | performance_data[0], related mechanisms | soft_boundary | CN121130847A key diazotized foam example reports WCA around 140.01 degrees. | Do not label that example superhydrophobic solely from this measurement; use high-hydrophobic/MOF bio-foam wording unless another source supports >=150 degrees. | CN121130847A PDF | [0036] | "平均值为140.01" | partial | Classification caution. |
| SHART-BD-03 | `prototypes_db/separation/superhydrophobic-artificial.json`; `lotus-leaf.json` | artificial sponge patent rows | soft_boundary | CN114874407A TiO2/fluorosilane sponge supports artificial superhydrophobic-superoleophilic separation, not natural lotus-leaf performance. | Keep as artificial sponge/material evidence and do not use as lotus biological evidence. | CN114874407A PDF | [0035]-[0038] | "接触角为151°"; "分离效率仍保持在98%以上" | supported | Reassign after approval if cleanup proceeds. |

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---|---|---|---|
| `2024-Zheng-silk-superhydrophobic-hydrophobic-separation-review.pdf` | lotus-leaf performance_data[0] | PDF not found at cited path; only extraction/visual cache found in local scan. | Locate PDF or demote row to missing_pdf. |
| `2021-Usman-superhydrophobic-hydrophobic-oil-water-separation-review.pdf` | lotus-leaf performance_data[2] | PDF not found at cited path. | Locate PDF or demote row to missing_pdf. |
| `2023-Li-oil-water-separation-wastewater-review.pdf` | lotus-leaf performance_data[3] | PDF not found at cited path. | Locate PDF or demote row to missing_pdf. |
| `2022-Khan-wastewater-water-treatment-review 2.pdf` | lotus-leaf performance_data[1] | PDF exists but claim is scallop-shell-template graphene foam, not lotus-leaf performance. | Keep soft or reassign to shell/graphene/artificial foam. |
| CN113244892B | superhydrophobic-artificial performance_data[1-7] | Strong patent evidence but missing quotes/locators and patent metadata fields. | Add locators and normalize source metadata after approval. |
| CN121130847A | superhydrophobic-artificial performance_data[0], constraints[1-3] | Strong high-hydrophobic/MOF bio-foam evidence; source path lacks patent directory; WCA classification needs caution. | Add locators/source path and avoid unsupported superhydrophobic threshold claim. |
| CN114874407A | lotus narrative/artificial sponge references | Strong artificial sponge evidence, not lotus-specific. | Reassign to artificial superhydrophobic sponge/material scope. |
| DOI 10.3390/polym14245439 | superhydrophobic-artificial mechanisms[19-24], constraint[0] | Fluoropolymer membrane-distillation review, not adsorption foam performance. | Keep as membrane background or reassign to membrane prototype. |

## Audit Statistics

- performance_data preflighted: 12 rows across five prototypes.
- mechanisms preflighted by source/scope grouping: 536 rows across five prototypes.
- engineering_constraints preflighted: 31 rows across five prototypes.
- direct performance evidence preserved: CN113244892B artificial biochar foam; CN121130847A MOF-modified bio-based foam; CN114874407A artificial superhydrophobic sponge.
- highest-priority cleanup before row-level verification: split `lotus-leaf` into lotus-specific theory/background vs artificial superhydrophobic/membrane/other-bio-prototype evidence, then add quotes to the artificial superhydrophobic patent rows.
