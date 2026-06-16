# Full Audit Batch 02: biomineralization-template

status: codex_reviewed

## Scope

- **Prototype JSON:** `prototypes_db/biomineralization-template.json`
- **Enrichment JSON:** `prototypes_db/enrichment/biomineralization-template.json`
- **Audit date:** 2026-06-16
- **Worker:** Codex local PDF text audit (`pdftotext`)
- **Paper in scope:** Wang2025 LanM@ZIF-8 rare-earth adsorption, DOI `10.1016/j.cej.2025.164827`
- **PDF found:** `仿生文献库/3rd/第B组-新方向/B2-生物矿化模板/2025-Wang-biomineralization-lanmodulin-heavy-metal-rare-earth-adsorption.pdf`

## Audit Summary

- The PDF supports a real adsorption result for LanM@ZIF-8: Nd3+ `Qmax = 787.93 mg/g` at 25 C, equilibrium within 1 h, and carboxyl/O/N coordination.
- The prototype has `performance_data` count 0, so the strongest numeric result exists only inside the mechanism quote.
- `provenance_summary` says `n_papers=0` and `n_verified=0`, although `mechanisms[0]` cites a real DOI/PDF and is marked `verified`.
- The causal-chain wording is broader than the paper: the source supports LanM-doped ZIF-8 / protein-MOF rare-earth adsorption, not a general statement that all biomineralization templates form multilevel inorganic adsorbent skeletons.
- Boundary conditions are still placeholders (`待文献确定具体失效边界`) even though the PDF supports a pH operating boundary around pH 4.
- No `prototypes_db/*.json` changes were made.

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BMT-MC-01 | biomineralization-template.json | mechanisms[0] | mechanism | LanM incorporation increases ZIF-8 adsorption capacity and gives high Nd3+ selectivity | Wang2025 LanM@ZIF-8 PDF | 10.1016/j.cej.2025.164827 | Y | Abstract; Results; Conclusions | "incorporation of LanM increases the adsorption capacity of ZIF-8" | supported | add_quote_locator | Mechanism quote is real, but source is marked `llm_inference`; provenance summary is inconsistent. |
| BMT-PF-01 | biomineralization-template.json | performance_data | performance | Nd3+ maximum adsorption capacity 787.93 mg/g at 25 C; equilibrium within 1 h | same | same | Y | Abstract; isotherm discussion; Conclusions | "Qmax = 787.93 mg/g, 25 C" | supported | add_performance_after_approval | Numeric adsorption evidence is absent from `performance_data`. |
| BMT-MC-02 | biomineralization-template.json | mechanisms[0].causal_chain | causal_chain | Generic biomineralization template controls inorganic crystal growth and multilevel pore skeleton | same | same | Y | Mechanism discussion | "-COOH, O and N atoms" coordinated with Nd ions | partial | narrow_claim | Source supports LanM protein/MOF coordination and ZIF-8 synergy, not a broad all-biomineralization template rule. |
| BMT-BD-01 | biomineralization-template.json | mechanisms[0].causal_chain.boundary_conditions[0-1] | boundary | Placeholder boundary conditions with no locator/quote | same | same | Y | pH-effect section | pH 4 is the favorable adsorption condition | inferred_only | replace_or_demote_placeholder | Use pH 4 as a supported soft boundary, keep other failure limits as knowledge gaps. |
| BMT-SM-01 | biomineralization-template.json | provenance_summary; mechanisms[0].source | source_metadata | `n_papers=0`, `n_verified=0`, and mechanism `source=llm_inference` conflict with DOI/PDF-backed verified claim | same | same | Y | JSON/PDF cross-check | N/A | partial | fix_metadata_after_approval | Metadata cleanup is decision-ready but not applied. |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| BMT-BD-01 | biomineralization-template.json | mechanisms[0].causal_chain.boundary_conditions | soft_boundary | LanM@ZIF-8 adsorption is pH-sensitive, with pH 4 favorable for Nd3+ uptake. | Do not generalize 787.93 mg/g outside the tested pH/temperature system without extra evidence. | Wang2025 LanM@ZIF-8 PDF | pH-effect section | "pH = 4 was the most favorable" | supported | This is a soft operating boundary, not a universal biomineralization rule. |
| BMT-BD-02 | biomineralization-template.json | mechanisms[0].causal_chain.boundary_conditions[0-1] | knowledge_gap | Current placeholder boundaries have no source quote. | They should not be treated as design constraints. | N/A | N/A | N/A | inferred_only | Replace with sourced pH boundary or leave as unresolved. |

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---|---|---|---|
| 10.1016/j.cej.2025.164827 | mechanisms[0], provenance_summary | Real DOI/PDF exists but metadata says zero papers/verified and mechanism source is `llm_inference`. | Correct provenance/source metadata after Yao approval. |
| Wang2025 LanM@ZIF-8 | performance_data | Strong Qmax evidence is not represented in `performance_data`. | Add a performance row after approval, or explicitly keep the result as mechanism-only evidence. |
| mechanisms[0].causal_chain | mechanism scope | Generic biomineralization wording overreaches beyond LanM@ZIF-8 evidence. | Narrow to protein-assisted ZIF-8 rare-earth adsorption or add a separate true biomineralization-template source. |

## Audit Statistics

- performance_data audited: 0 existing rows; 1 supported candidate missing from JSON.
- mechanisms audited: 1 supported but scope/metadata partial.
- boundary candidates: 1 supported soft boundary, 1 placeholder knowledge gap.
