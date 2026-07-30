# Full Audit Batch 02: scallop-shell

status: codex_reviewed

## Scope

- **Prototype JSON:** `prototypes_db/scallop-shell.json`
- **Enrichment JSON:** `prototypes_db/enrichment/scallop-shell.json`
- **Audit date:** 2026-06-16
- **Worker:** Codex local PDF text audit (`pdftotext`)
- **Papers in scope:** Wang2024 scallop-shell Congo Red adsorption; Zhang2024 modified shell-powder heavy-metal review; Zhang2021 shellfish soil-passivation review.
- **PDFs found:** 3/3.

## Audit Summary

- Wang2024 is the strongest scallop-specific source. It supports calcined Chlamys farreri scallop shell powder for Congo Red, with 900 C calcination performing best, fast uptake in the first 5 min, near-equilibrium after 150 min, pseudo-second-order kinetics, and Freundlich/multiphase adsorption.
- `mechanisms[0]` is marked verified but its causal-chain `pollutant_feature` says heavy metals and phosphate; the actual Wang2024 source is Congo Red dye.
- `mechanisms[2]` is likely supported by Wang2024: CaO hydration to Ca(OH)2 and O-H hydrogen bonding with Congo Red are discussed, but the JSON lacks source_file/locator/quote.
- Existing `performance_data[0-6]` do not use Wang2024; they are copied from Zhang2024/Zhang2021 shell review sources and are not scallop-specific primary performance rows.
- The Zhang2021 shellfish review is soil passivation/background evidence and should not be treated as direct aqueous adsorption performance without a domain caveat.
- No `prototypes_db/*.json` changes were made.

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SCAL-MC-01 | scallop-shell.json | mechanisms[0] | mechanism | Calcined scallop shell powder adsorbs Congo Red; Freundlich model fits multiphase adsorption | Wang2024 PDF | 10.11759/hykx20221122001 | Y | Abstract; kinetics/isotherm sections | "Freundlich 模型...属于多相吸附" | supported | fix_pollutant_feature_and_add_locator | Causal-chain pollutant feature incorrectly says heavy metals/phosphate. |
| SCAL-MC-02 | scallop-shell.json | mechanisms[0].causal_chain.boundary_conditions[0] | boundary | Calcination temperature affects crystal conversion and adsorption performance | Wang2024 PDF | 10.11759/hykx20221122001 | Y | calcination sections | "900 C...吸附性能最好" | supported | replace_inferred_boundary_with_quote | Current boundary is plausible but marked LLM-inferred and lacks quote. |
| SCAL-MC-03 | scallop-shell.json | mechanisms[2] | mechanism | Ca(OH)2 O-H groups form hydrogen bonding with Congo Red | Wang2024 PDF | 10.11759/hykx20221122001 | Y | calcination/mechanism section | "Ca(OH)2 的 O-H 键...氢键作用" | supported | add_source_file_quote_locator | Source metadata is blank in JSON. |
| SCAL-PF-01 | scallop-shell.json | performance_data[0-4] | performance | Modified shell-powder heavy-metal values from Zhang2024 review | Zhang2024 review PDF | 10.3969/j.issn.1672-7304.2024.02.0011 | Y | review sections | calcination increased Pb capacity 32.34 to 57.79 mg/g | keep_soft | keep_soft_or_split_shell_general | Same generic shell-review rows also appear under oyster-shell; not scallop-specific primary data. |
| SCAL-PF-02 | scallop-shell.json | performance_data[5-6] | performance | Shellfish passivation/removal values from Zhang2021 review | Zhang2021 shellfish review PDF | 10.13254/j.jare.2020.0504 | Y | review/table sections | calcined oyster shell Cd/Pb capacities 2184.29/1949.39 mg/g | keep_soft | mark_domain_boundary | Soil passivation and generic shellfish review evidence. |
| SCAL-PF-03 | scallop-shell.json | performance_data | performance | Missing Wang2024 scallop-shell Congo Red performance rows | Wang2024 PDF | 10.11759/hykx20221122001 | Y | Abstract; kinetics/isotherm sections | "5 min...150 min...96.2%" | supported | add_performance_after_approval | Consider adding Wang2024 condition-specific performance rather than relying on generic review rows. |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| SCAL-BD-01 | scallop-shell.json | mechanisms[0].causal_chain.boundary_conditions[0] | soft_boundary | 900 C calcination gives best Congo Red adsorption; 550/700 C do not significantly improve capacity. | Do not generalize scallop-shell performance without calcination-temperature condition. | Wang2024 PDF | calcination-temperature section | "900 C calcined shell powder...best adsorption performance" | supported | This should replace the current inferred boundary. |
| SCAL-BD-02 | scallop-shell.json | mechanisms[0], candidate performance | soft_boundary | Uptake is rapid in first 5 min and reaches near-equilibrium after 150 min. | Do not assume shorter contact time reaches the reported equilibrium removal/capacity. | Wang2024 PDF | kinetics section | "5 min...150 min" | supported | Useful operational boundary for Congo Red. |
| SCAL-BD-03 | scallop-shell.json | performance_data[5-6], mechanisms[1] | soft_boundary | Zhang2021 shellfish review is soil passivation/background evidence. | Do not treat as direct aqueous adsorption evidence without domain caveat. | Zhang2021 shellfish review PDF | Abstract | "钝化农田土壤中重金属" | supported | Keep soft or split to a soil-passivation context. |

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---|---|---|---|
| 10.11759/hykx20221122001 | mechanisms[0], mechanisms[2], missing performance_data | Strong scallop-specific source exists, but JSON uses it mostly in mechanisms and has pollutant-feature mismatch. | Fix causal-chain pollutant and add condition-specific performance rows after approval. |
| 10.3969/j.issn.1672-7304.2024.02.0011 | performance_data[0-4] | Generic modified shell-powder review rows duplicated with oyster-shell. | Keep as soft background or move to shell-general evidence after approval. |
| 10.13254/j.jare.2020.0504 | performance_data[5-6], mechanisms[1] | Soil-passivation shellfish review, not direct water adsorption. | Add domain caveat or remove from performance data after approval. |

## Audit Statistics

- performance_data audited: 7 existing rows are keep_soft review/domain evidence; 1 missing Wang2024 performance candidate identified.
- mechanisms audited: 2 supported Wang2024 mechanisms, 1 keep_soft soil-passivation mechanism.
- boundary candidates: 2 supported scallop/Congo Red operating boundaries, 1 soil-domain boundary.
