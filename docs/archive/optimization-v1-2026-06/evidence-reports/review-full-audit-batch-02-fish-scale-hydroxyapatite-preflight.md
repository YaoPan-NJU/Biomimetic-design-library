# Full Audit Batch 02: fish-scale-hydroxyapatite preflight

status: codex_preflight_reviewed

## Scope

- **Prototype JSON:** `prototypes_db/fish-scale-hydroxyapatite.json`
- **Enrichment JSON:** `prototypes_db/enrichment/fish-scale-hydroxyapatite.json`
- **Audit date:** 2026-06-16
- **Worker:** Codex local PDF text audit (`pdftotext`)
- **Reason for preflight instead of one-pass full review:** this prototype contains 29 performance rows, 89 mechanisms, 12 engineering constraints, and 10 narrative entries. The mechanism list has a large block of special-wettability/membrane content that is structurally unrelated to fish-scale HAp adsorption.
- **PDFs spot-checked:** Dou2021 fish-scale porous biochar/CIP; Wu2022 HAp-tailored hierarchical porous biochar/Cd/Pb; Balasooriya2022 nano-HAp adsorption review; CN114849640A fish-scale HAp/acid fuchsin patent; CN113275374A biomineralization-heavy-metal patent; Zhang2024 shell-powder review.

## Audit Summary

- A major wrong-source block is present: `mechanisms[0-53]`, `mechanisms[56-86]`, and `engineering_constraints[0-10]` are mostly special-wettability, superhydrophobic membrane, Janus membrane, or photocatalytic membrane content. These should not support fish-scale HAp adsorption.
- `performance_data[0-1]`, `mechanisms[55]`, and `engineering_constraints[11]` are supported by Dou2021, but the source is fish-scale-derived porous activated biochar for ciprofloxacin. It is not fish-scale hydroxyapatite as the final adsorbent; the paper states HAp-based inorganics are removed during biochar preparation.
- `performance_data[2-6]` are supported by Wu2022 for hydroxyapatite-tailored hierarchical porous biochar, but the biochar feedstock is rice husk. This is HAp/biochar evidence, not fish-scale-specific HAp evidence.
- `performance_data[7-17]` are supported by CN114849640A for fish-scale extracted HAp adsorbing acid fuchsin, but these rows contain duplicates and need quote/locator normalization.
- `performance_data[18-21]` depend on CN113275374A, a scanned 20 MB patent. `pdftotext` produced only form-feed characters; values cannot be verified without OCR/visual reading.
- `mechanisms[54]` cites Balasooriya2022 and is useful for general HAp heavy-metal adsorption mechanisms, but its current title "八重协同吸附机制" mixes the Dou2021 CIP/biochar mechanism with general HAp review evidence.
- `performance_data[22-23]` reuse Wang2021 marine-shell HA/Congo Red rows. These are abalone/marine-shell HA evidence, not fish-scale HAp evidence.
- No `prototypes_db/*.json` changes were made.

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FISH-WRONG-01 | fish-scale-hydroxyapatite.json | mechanisms[0-53], mechanisms[56-86] | mechanism | Special-wettability, superhydrophobic membrane, Janus membrane, and laser-structured surface content | multiple membrane/superwetting reviews | multiple | mixed | title/domain check | source titles are membrane/superwetting, not HAp adsorption | wrong_source | remove_or_reassign_after_approval | Candidate reassign targets: lotus-leaf, water-strider-leg, superhydrophobic-artificial, separation-surface batch. |
| FISH-WRONG-02 | fish-scale-hydroxyapatite.json | engineering_constraints[0-10] | engineering | Constraints about smart membranes, superhydrophobic stability, Fe-PA/OTMS/PI flux, PTFE cycles, TiO2/PANI mesh | membrane/superwetting reviews | multiple | mixed | title/domain check | not fish-scale HAp adsorption | wrong_source | remove_or_reassign_after_approval | Do not use as HAp design boundaries. |
| FISH-PF-01 | fish-scale-hydroxyapatite.json | performance_data[0-1] | performance | Fish-scale-derived porous biochar removes ciprofloxacin: Langmuir qmax 1013.96 mg/g; dynamic capacity 880.53 mg/g | Dou2021 PDF | 10.1016/j.chemosphere.2021.131962 | Y | Abstract; isotherm; fixed-bed section | "qmax...1013.96 mg/g"; "880.53 mg/g" | supported | needs_human_decision | Strong evidence for fish-scale biochar/CIP, but not final HAp adsorbent. |
| FISH-MC-01 | fish-scale-hydroxyapatite.json | mechanisms[55], engineering_constraints[11] | mechanism/engineering | CIP adsorption mechanism: hydrophobic effect, pore filling, pi-pi, cation exchange, H-bond; regeneration to 498 mg/g after five cycles | Dou2021 PDF | 10.1016/j.chemosphere.2021.131962 | Y | mechanism/regeneration section | "hydrophobic effect, pi-pi interaction...pore filling" | partial | split_scope_or_narrow | This belongs to porous carbon/biochar mechanism, not HAp heavy-metal mechanism. |
| FISH-PF-02 | fish-scale-hydroxyapatite.json | performance_data[2-6] | performance | HA-3HPB removes Cd/Pb: Langmuir 88.06/110.22 mg/g; Pb removal >=99.83%; Cd co-cation effects | Wu2022 PDF | 10.1016/j.jhazmat.2022.129330 | Y | Abstract; pH/co-ion/isotherm sections | "Langmuir adsorption capacities...88.1 and 110.2 mg/g" | supported | keep_soft_or_reassign | HAp/biochar evidence, but feedstock is rice husk, not fish scale. |
| FISH-PF-03 | fish-scale-hydroxyapatite.json | performance_data[7-17] | performance | Fish-scale extracted HAp adsorbs acid fuchsin; example capacities 478, 386, 356, 423, 450, 430, 462 mg/g | CN114849640A PDF | none | Y | patent examples [0045]-[0063] | "酸性品红的吸附能力达478mg/g" | supported | add_quote_locator_and_deduplicate | This is the strongest fish-scale HAp performance source; repeated 478 rows need deduplication. |
| FISH-PF-04 | fish-scale-hydroxyapatite.json | performance_data[18-21] | performance | Biomineralization-heavy-metal patent Cd/Pb removal values | CN113275374A PDF | none | scanned | N/A | N/A | needs_human_decision | OCR_or_visual_verify | Local PDF is scanned; `pdftotext` extracted no text. |
| FISH-PF-05 | fish-scale-hydroxyapatite.json | performance_data[22-23] | performance | Marine-shell HA Congo Red qmax/temperature values | Wang2021 marine-shell HA PDF | 10.1016/j.matlet.2021.130573 | Y | Abstract; Results | "abalone HA microspheres...495.5626 mg/g" | wrong_source | remove_or_reassign | Source is marine-shell/abalone HA, not fish-scale HAp. |
| FISH-MC-02 | fish-scale-hydroxyapatite.json | mechanisms[54] | mechanism | General nano-HAp heavy-metal mechanisms | Balasooriya2022 PDF | 10.3390/ma14202324 | Y | Abstract; mechanism sections | "ionic exchange...surface complexation...co-precipitation" | partial | narrow_claim_and_fix_doi | Useful for HAp, but current DOI/ref mix with Dou2021 and "八重协同" label is misleading. |
| FISH-MC-03 | fish-scale-hydroxyapatite.json | mechanisms[87] | mechanism | MICP urea hydrolysis/CaCO3 precipitation | no source | none | N/A | N/A | N/A | wrong_source | remove_or_source | No clear relation to fish-scale HAp. |
| FISH-MC-04 | fish-scale-hydroxyapatite.json | mechanisms[88], performance_data[24-28] | mechanism/performance | Generic modified shell-powder adsorption mechanism and heavy-metal values | Zhang2024 review PDF | 10.3969/j.issn.1672-7304.2024.02.0011 | Y | review sections | modified shell powder heavy-metal review | wrong_source | remove_or_reassign | Belongs to generic shell/shell-powder evidence, not fish-scale HAp. |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| FISH-BD-01 | fish-scale-hydroxyapatite.json | mechanisms[0-53], mechanisms[56-86], engineering_constraints[0-10] | hard_do_not | Special-wettability/membrane mechanisms must not be used as fish-scale HAp adsorption evidence. | Would drive wrong recommendations toward oil-water separation, Janus membranes, and superhydrophobic coatings. | multiple membrane/superwetting review sources | title/domain check | source domains are membrane/superwetting | wrong_source | Remove/reassign after Yao approval. |
| FISH-BD-02 | fish-scale-hydroxyapatite.json | performance_data[0-1], mechanisms[55], engineering_constraints[11] | soft_boundary | Dou2021 supports fish-scale-derived porous biochar for ciprofloxacin, not HAp as the final adsorbent. | Keep only if prototype scope explicitly includes fish-scale biochar; otherwise reassign. | Dou2021 PDF | Abstract; methods; mechanism | "fish scale-based porous activated biochar" | supported | Human decision needed on prototype scope. |
| FISH-BD-03 | fish-scale-hydroxyapatite.json | performance_data[7-17] | soft_boundary | CN114849640A acid fuchsin values are measured under patent-specific conditions: 100 mg/L dye, 5 mg HAp, 25 mL solution, 30 C, 24 h. | Do not generalize 478 mg/g to other dyes or contact times. | CN114849640A PDF | claims/examples | "100mg/L...酸性品红...30C...24h" | supported | Strong condition-specific fish-scale HAp evidence. |
| FISH-BD-04 | fish-scale-hydroxyapatite.json | performance_data[18-21] | knowledge_gap | CN113275374A values cannot be text-verified from local scanned PDF. | Cd/Pb patent values should not be used until OCR/visual verification. | scanned patent | N/A | N/A | needs_human_decision | OCR required. |
| FISH-BD-05 | fish-scale-hydroxyapatite.json | performance_data[22-23] | hard_do_not | Marine-shell/abalone HA Congo Red values must not be used as fish-scale HAp evidence. | Would import another shell prototype's performance into fish-scale HAp. | Wang2021 marine-shell HA PDF | Abstract | "abalone HA microspheres...495.5626 mg/g" | wrong_source | Remove/reassign after Yao approval. |
| FISH-BD-06 | fish-scale-hydroxyapatite.json | mechanisms[54].causal_chain.boundary_conditions | knowledge_gap | HAp pH dissolution/adsorption boundary exists in general literature, but this JSON row has no direct quote for its specific wording. | Keep as soft/knowledge gap until sourced. | Balasooriya2022 or Jaffar2024 | mechanism/pH sections | N/A | partial | Source and quote before converting into a boundary. |

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---|---|---|---|
| superwetting/membrane DOI block | mechanisms[0-53], mechanisms[56-86], engineering_constraints[0-10] | Large wrong-source contamination. | Remove/reassign after Yao approval before fine-grained HAp edits. |
| 10.1016/j.chemosphere.2021.131962 | performance_data[0-1], mechanisms[55], engineering_constraints[11] | Strong fish-scale-derived biochar/CIP source, but not final HAp adsorbent. | Decide whether fish-scale-biochar belongs inside this prototype or needs a new/moved prototype. |
| 10.1016/j.jhazmat.2022.129330 | performance_data[2-6] | Supported HAp-tailored biochar data, but rice-husk feedstock, not fish-scale. | Keep soft or reassign to HAp-biochar general after approval. |
| CN114849640A | performance_data[7-17] | Strong fish-scale HAp acid-fuchsin patent; duplicate rows and missing locators. | Deduplicate and add patent paragraph locators after approval. |
| CN113275374A | performance_data[18-21] | Scanned PDF, no text extraction. | OCR/visual verify before relying on values. |
| Wang2021 DOI 10.1016/j.matlet.2021.130573 | performance_data[22-23] | Marine-shell/abalone HA evidence, not fish-scale HAp. | Remove or reassign after Yao approval. |
| Balasooriya2022 DOI 10.3390/ma14202324 | mechanisms[54] | General nano-HAp review useful for mechanisms, but JSON row mixes it with Dou2021 DOI/name. | Fix DOI/source and narrow label after approval. |

## Audit Statistics

- performance_data preflighted: 18 supported but scope-split/dedup candidates, 4 scanned/unverified patent rows, 7 wrong-source or generic-shell/marine-shell rows.
- mechanisms preflighted: at least 85/89 are wrong-source or require reassign/scope decisions; 1 general HAp mechanism is partial; 1 biochar/CIP mechanism is supported but scope-split.
- engineering_constraints preflighted: 10 wrong-source membrane/superwetting constraints, 1 supported biochar/CIP regeneration constraint, 1 not deeply audited.
- recommended next step: split fish-scale into a cleanup sub-batch before full row-by-row quote insertion.
