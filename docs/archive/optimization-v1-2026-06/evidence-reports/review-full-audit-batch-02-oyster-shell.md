# Full Audit Batch 02: oyster-shell

status: codex_reviewed

## Scope

- **Prototype JSON:** `prototypes_db/oyster-shell.json`
- **Enrichment JSON:** `prototypes_db/enrichment/oyster-shell.json`
- **Audit date:** 2026-06-16
- **Worker:** Codex local PDF text audit (`pdftotext`)
- **Papers in scope:** Qiu2021 oyster-shell Ca-Al-LDH phosphate adsorbent; Li2017 oyster-shell modified peanut-shell biochar; Xu2022 oyster-shell modified peanut-shell biochar; Wang2021 marine-shell HA Congo Red; Zhang2024 modified shell-powder review; Zhang2021 shellfish soil passivation review.
- **PDFs found:** 6/6, but several JSON `source_file` paths omit real directory prefixes or ` 2.pdf` / ` 3.pdf` suffixes.

## Audit Summary

- `performance_data[0]` Qiu2021 is supported for phosphate adsorption by oyster-shell-derived Ca-Al-LDHs, but pollutant is empty and source_file path omits actual suffixes.
- `performance_data[1-3]` Li2017/Xu2022 phosphate adsorption values are supported; `performance_data[2].pollutant` is empty, and source paths need normalization.
- `mechanisms[0]` should be narrowed: the Li2017/Xu2022 evidence supports CaO/Ca(OH)2 induced phosphate precipitation as hydroxyapatite, not a generic heavy-metal oyster-shell mechanism.
- `performance_data[4-5]` Wang2021 supports marine-shell HA/Congo Red and explicitly reports the 495.5626 mg/g maximum for abalone HA microspheres. Using that value as oyster-shell performance is source/prototype ambiguous.
- `performance_data[6-10]` and `mechanisms[1]` are review-backed generic modified-shell-powder evidence, not all oyster-specific primary evidence.
- `performance_data[11-12]` and `mechanisms[2]` come from a shellfish soil-passivation review. They are useful boundary/background evidence but should not be treated as direct aqueous adsorption evidence.
- No `prototypes_db/*.json` changes were made.

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OYS-PF-01 | oyster-shell.json | performance_data[0] | performance | Ca-Al-LDHs from oyster shell/pull-tab waste adsorb phosphate: CAs-4/CA-4 around 126-127 mg/g | Qiu2021 PDF | 10.1016/j.jenvman.2021.114235 | Y | Abstract; Conclusions | "maximum adsorption capacity...127.50 and 126.67 mg/g" | supported | fill_pollutant_and_add_quote | Pollutant should be phosphate; source_file path needs actual suffix. |
| OYS-PF-02 | oyster-shell.json | performance_data[1-2] | performance | Oyster-shell modified peanut-shell biochar adsorbs phosphorus 197.3 mg/g, about 17x unmodified | Li2017 PDF | 10.16663/j.cnki.lskj.2021.02.025 | Y | Abstract; Conclusions | "maximum adsorption capacity...197.3 mg/g" | supported | fill_pollutant_and_add_quote | `performance_data[2].pollutant` is empty; source_file path omits ` 2.pdf`. |
| OYS-PF-03 | oyster-shell.json | performance_data[3] | performance | Oyster-shell modified peanut-shell biochar phosphate adsorption 144.35 mg/g; pH 4; 60 min | Xu2022 PDF | 10.19319/j.cnki.issn.1008-021x.2022.15.005 | Y | Abstract; Results; Conclusions | "maximum adsorption capacity...144.35 mg/g" | supported | add_quote_locator | PDF reports pH 4 as optimum and phosphate as HAp after adsorption. |
| OYS-PF-04 | oyster-shell.json | performance_data[4-5] | performance | Marine-shell HA Congo Red qmax 495.5626 mg/g and temperature capacities | Wang2021 marine-shell HA PDF | 10.1016/j.matlet.2021.130573 | Y | Abstract; Results | "abalone HA microspheres...495.5626 mg/g" | partial | narrow_or_reassign | Paper includes oyster and abalone shells, but the cited qmax is explicitly abalone HA. |
| OYS-PF-05 | oyster-shell.json | performance_data[6-10] | performance | Modified shell-powder heavy-metal values from Zhang2024 review | Zhang2024 review PDF | 10.3969/j.issn.1672-7304.2024.02.0011 | Y | review sections | calcination increased Pb capacity 32.34 to 57.79 mg/g | keep_soft | keep_soft_or_split_shell_general | Review contains oyster, mussel, scallop, and generic shell evidence; not all rows are oyster-specific. |
| OYS-PF-06 | oyster-shell.json | performance_data[11-12] | performance | Shellfish waste passivation/removal values from soil-passivation review | Zhang2021 shellfish review PDF | 10.13254/j.jare.2020.0504 | Y | review/table sections | calcined oyster shell Cd/Pb capacities 2184.29/1949.39 mg/g | keep_soft | mark_domain_boundary | Source is soil passivation/shellfish review, useful background but not direct water-treatment adsorption unless field is narrowed. |
| OYS-MC-01 | oyster-shell.json | mechanisms[0] | mechanism | CaCO3/CaO oyster-shell biochar releases Ca/OH and forms hydroxyapatite with phosphate | Li2017/Xu2022 PDFs | 10.16663/j.cnki.lskj.2021.02.025 | Y | mechanism sections | phosphate and calcium formed hydroxyapatite crystals | partial | narrow_claim_and_replace_quote | Current verification quote is title-like and mentions heavy metals beyond the source claim. |
| OYS-MC-02 | oyster-shell.json | mechanisms[1] | mechanism | Modified shell-powder adsorption has film diffusion, intraparticle diffusion, and surface reaction | Zhang2024 review PDF | 10.3969/j.issn.1672-7304.2024.02.0011 | Y | mechanism section | "3 steps: film diffusion...intraparticle diffusion...adsorption reaction" | keep_soft | add_quote_locator | Generic modified-shell mechanism, not oyster-only. |
| OYS-MC-03 | oyster-shell.json | mechanisms[2] | mechanism | Shellfish passivation mechanism: liming, precipitation, physical adsorption, ion exchange | Zhang2021 shellfish review PDF | 10.13254/j.jare.2020.0504 | Y | mechanism section | "石灰效应、沉淀效应和吸附效应" | keep_soft | mark_soil_domain | Soil-passivation domain; keep as boundary/background only. |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| OYS-BD-01 | oyster-shell.json | performance_data[0] | soft_boundary | Qiu2021 phosphate adsorption is stable across pH 4-10 and peaks around pH 7. | Do not generalize the qmax outside the Ca-Al-LDH phosphate system without condition notes. | Qiu2021 PDF | pH-effect/conclusions | "stable pH range from 4 to 10" | supported | Also note possible carbonate/anion competition in applications. |
| OYS-BD-02 | oyster-shell.json | performance_data[3] | soft_boundary | Xu2022 optimum phosphate adsorption occurs around pH 4 and 60 min. | Treat 144.35 mg/g as condition-specific, not universal oyster-shell capacity. | Xu2022 PDF | Abstract; pH/time sections | "optimal pH value was 4" | supported | The mechanism is phosphate mineralization, not generic metal adsorption. |
| OYS-BD-03 | oyster-shell.json | performance_data[4-5] | hard_do_not | Abalone HA qmax 495.5626 mg/g must not be reported as oyster-shell qmax without explicit species/material qualification. | Species/source ambiguity would overstate oyster-specific evidence. | Wang2021 marine-shell HA PDF | Abstract | "abalone HA microspheres...495.5626 mg/g" | partial | Move to generic marine-shell HA or mark as abalone-specific. |
| OYS-BD-04 | oyster-shell.json | performance_data[11-12], mechanisms[2] | soft_boundary | Zhang2021 shellfish evidence is primarily soil heavy-metal passivation. | Do not use it as direct aqueous adsorption performance without domain caveat. | Zhang2021 shellfish review PDF | Abstract | "钝化农田土壤中重金属" | supported | Background and boundary evidence only. |

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---|---|---|---|
| Qiu2021 DOI 10.1016/j.jenvman.2021.114235 | performance_data[0], narrative.entries[0] | PDF exists but actual filenames include ` 2.pdf` and ` 3.pdf`; pollutant field empty. | Normalize path and fill phosphate after approval. |
| Li2017 DOI 10.16663/j.cnki.lskj.2021.02.025 | performance_data[1-2], mechanisms[0] | PDF exists as `...废水 2.pdf`; quote is not a real mechanism quote. | Normalize path and replace quote with Ca/HAp precipitation evidence. |
| Xu2022 DOI 10.19319/j.cnki.issn.1008-021x.2022.15.005 | performance_data[3], narrative.entries[2] | Supported but path needs actual suffix/prefix confirmation. | Add quote/locator and pH/time boundary after approval. |
| Wang2021 DOI 10.1016/j.matlet.2021.130573 | performance_data[4-5] | Value is abalone HA, not clearly oyster-shell performance. | Narrow or reassign after Yao approval. |
| Zhang2024 / Zhang2021 shell reviews | performance_data[6-12], mechanisms[1-2] | Review/generic shell and soil-passivation evidence mixed into oyster-shell. | Keep as soft background or split into generic-shell evidence. |

## Audit Statistics

- performance_data audited: 3 supported oyster/phosphate rows, 2 partial abalone/marine-shell rows, 7 keep_soft review/domain rows.
- mechanisms audited: 1 partial/narrowing needed, 2 keep_soft review/background mechanisms.
- boundary candidates: 2 supported soft operating boundaries, 1 hard DO-NOT for abalone qmax mislabeling, 1 soft soil-domain boundary.
