# Full Audit Batch 02: bone-structure

status: codex_reviewed

## Scope

- **Prototype JSON:** `prototypes_db/bone-structure.json`
- **Enrichment JSON:** `prototypes_db/enrichment/bone-structure.json`
- **Audit date:** 2026-06-16
- **Worker:** Codex local PDF text audit (`pdftotext`)
- **Papers in scope:** Bambaeero2020 natural composite adsorbent; Jaffar2024 HAp adsorbent/membrane review; Chen2021 MOF dye/Cr(VI) review.
- **PDFs found:** 3/3, with `Bambaeero2020` actual filename using a ` 2.pdf` suffix.

## Audit Summary

- `performance_data[0-1]` are supported by Bambaeero2020, but `performance_data[1].pollutant` is empty although the field is about Cu(II).
- `engineering_constraints[0]` is supported as a study-scope boundary: pH 4-6 was tested because Cu precipitation occurs above pH 6. It should not become a universal HAp boundary.
- `mechanisms[0]`, `mechanisms[2]`, and `mechanisms[3]` are supported by Jaffar2024 but currently lack `source_file`, locators, and verification quotes.
- `mechanisms[1]` is partially supported: Bambaeero supports HAp as an adsorbent and the composite context, but the four detailed HAp heavy-metal mechanisms need Jaffar/Balasooriya-style HAp review evidence and sourced boundary conditions.
- `performance_data[2]` and `mechanisms[4]` are wrong-source for this prototype: the source is a MOF review for printing/dyeing wastewater dye and Cr(VI), not bone/HAp.
- No `prototypes_db/*.json` changes were made.

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BONE-PF-01 | bone-structure.json | performance_data[0] | performance | Higher Cu concentration lowers Cu removal percentage under same conditions | Bambaeero2020 PDF | 10.1016/j.cjche.2020.07.066 | Y | RSM discussion | low Cu concentration and increased pH increase Cu removal | supported | add_quote_locator | Source_file in JSON omits ` 2.pdf`; paper is simultaneous Cu/Zn adsorption. |
| BONE-PF-02 | bone-structure.json | performance_data[1] | performance | Increasing adsorbent dose increases Cu removal; maximum at 0.030 g and pH 5 | Bambaeero2020 PDF | 10.1016/j.cjche.2020.07.066 | Y | pH/dose discussion | "maximum amount of Cu ion removal was obtained at 0.030 g... at pH 5" | supported | fill_pollutant_and_add_quote | Pollutant field is empty; should be Cu(II) after approval. |
| BONE-PF-03 | bone-structure.json | performance_data[2] | performance | HPU-13@Fe3O4 Cr2O7/CrO4 adsorption 398.41/471.69 mg/g | Chen2021 MOF review | none | Y | MOF Cr(VI) section | "HPU-13@Fe3O4...398.41 mg/g and 471.69 mg/g" | wrong_source | remove_or_reassign | Value is real but belongs to a MOF/Cr(VI) prototype, not bone-structure. |
| BONE-MC-01 | bone-structure.json | mechanisms[0] | mechanism | HAp membranes and composites remove heavy metals; chitosan/HAp nanofiber membrane Pb/Co/Ni capacities | Jaffar2024 PDF | 10.1016/j.jtice.2024.105668 | Y | membrane section | "Pb(II), Co(II), and Ni(II) ... 296.7, 180.2, 213.8 mg/g" | supported | add_source_file_quote_locator | Source_file is blank in JSON. |
| BONE-MC-02 | bone-structure.json | mechanisms[1].causal_chain | mechanism | Four HAp heavy-metal adsorption mechanisms and pH dissolution boundary | Bambaeero2020 + HAp reviews | 10.1016/j.cjche.2020.07.066 | Y | Intro; mechanism review | "HAP has been used as an adsorbent in the removal of Sr, Zn, Co, Cd" | partial | augment_sources_or_narrow | Four-mechanism detail is not fully supported by Bambaeero alone; boundary conditions are LLM-inferred. |
| BONE-MC-03 | bone-structure.json | mechanisms[2-3] | mechanism | HAp membrane fabrication by NIPS/TIPS/electrospinning and membrane types | Jaffar2024 PDF | 10.1016/j.jtice.2024.105668 | Y | membrane fabrication section | "phase inversion and electrospinning techniques" | supported | add_source_file_quote_locator | Good review evidence, but metadata is incomplete. |
| BONE-MC-04 | bone-structure.json | mechanisms[4] | mechanism | MOFs photocatalytic dye degradation mechanism | Chen2021 MOF review | none | Y | MOF photocatalysis section | MOFs generate radical species for dye degradation | wrong_source | remove_or_reassign | Not bone/HAp evidence. |
| BONE-EC-01 | bone-structure.json | engineering_constraints[0] | engineering | pH range limited to 4-6 because pH > 6 causes Cu precipitation | Bambaeero2020 PDF | 10.1016/j.cjche.2020.07.066 | Y | Experimental design | "pH: 4-6 (because of the copper ions precipitation... above 6 were not studied)" | supported | add_quote_locator | This is a study boundary for Cu/Zn composite adsorption, not a hard HAp rule. |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| BONE-BD-01 | bone-structure.json | engineering_constraints[0] | soft_boundary | Bambaeero2020 only studied pH 4-6 because Cu precipitates above pH 6. | Do not generalize the Cu/Zn removal trends beyond pH 4-6 without extra evidence. | Bambaeero2020 PDF | experimental design | "above 6 were not studied" | supported | Scope is Cu/Zn natural composite adsorption. |
| BONE-BD-02 | bone-structure.json | performance_data[2], mechanisms[4] | hard_do_not | MOF dye/Cr(VI) review evidence must not be used as bone/HAp evidence. | Would contaminate bone-structure recommendations with MOF photocatalysis and Cr(VI) adsorption. | Chen2021 MOF review | title/abstract | "Metal organic frameworks... dyes and Cr(VI)" | wrong_source | Remove or reassign after Yao approval. |
| BONE-BD-03 | bone-structure.json | mechanisms[1].causal_chain.boundary_conditions | knowledge_gap | Acidic HAp dissolution boundary is currently inferred in JSON. | Should not be treated as a hard design limit until directly sourced. | N/A | N/A | N/A | inferred_only | HAp reviews can likely support pH sensitivity, but this row has no quote. |

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---|---|---|---|
| 10.1016/j.cjche.2020.07.066 | performance_data[0-1], engineering_constraints[0], mechanisms[1] | PDF exists as `...hydroxyapatite 2.pdf`; some JSON source paths omit suffix. | Normalize source_file and add locators after approval. |
| 10.1016/j.jtice.2024.105668 | mechanisms[0], mechanisms[2-3], narrative.entries[2] | PDF exists but source_file/quote metadata is blank for several supported HAp membrane fields. | Add source_file, locator, and quotes after approval. |
| Chen2021 MOF review | performance_data[2], mechanisms[4] | Correct source for MOF dye/Cr(VI), wrong prototype for bone-structure. | Remove or reassign after Yao approval. |

## Audit Statistics

- performance_data audited: 2 supported, 1 wrong-source.
- mechanisms audited: 2 supported groups, 1 partial, 1 wrong-source.
- engineering_constraints audited: 1 supported soft boundary.
- critical fixes queued: MOF wrong-source removal/reassignment, source_file completion, pollutant fill for `performance_data[1]`, HAp causal-chain source augmentation.
