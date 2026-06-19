# review-batch-lobster-exoskeleton.md

status: ready_for_codex_review

## Claim Verification Table

| claim_id | prototype_id | source_pdf_path | path_exists_yes_no | page_or_section | candidate_quote | quote_supports_claim_yes_no | source_is_on_topic_yes_no | needs_multimodal_yes_no | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| perf-1 | lobster-exoskeleton | 仿生文献库/论文/第1组-配位螯合/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf | No | N/A | N/A - source PDF missing | N/A | N/A | No | missing_pdf | 第1组-配位螯合 directory does not exist. No PDF with this filename found anywhere in 仿生文献库/. Extraction JSON exists at tools/litextract/outputs/extractions/论文/json/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.json with unverified quote "chitosan/Fe-hydroxyapatite beads exhibit an adsorption capacity of 1385 mg/g" (ki_001, page 1 Abstract). Note: extraction JSON marks this evidence quality as "suspicious" (二次引用). Target in prototypes_db: lobster-exoskeleton.json performance_data[0]. |
| narr-1 | lobster-exoskeleton | 仿生文献库/论文/第1组-配位螯合/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf | No | N/A | N/A - source PDF missing | N/A | N/A | No | missing_pdf | Same missing PDF as perf-1. Extraction JSON exists (ki_001-ki_031) with extensive structured data from the Vo2023 chitosan beads review, but all verification="unverified". Do not mark upgrade_candidate without local PDF. The 2024-Vo-wastewater-review 2.pdf in 第7组-系统仿生 is a different paper (microalgae-bacteria consortia, not chitosan beads). Target in prototypes_db: lobster-exoskeleton.json narrative.entries[0]. |
| mech-1 | lobster-exoskeleton | 仿生文献库/ (no matching PDF found) | No | N/A | N/A - source PDF missing | N/A | N/A | No | wrong_source | DOI 10.1016/j.polymer.2020.123316 in lobster-exoskeleton.json actually references Lei2021 (Mussel-magnetic-carboxymethyl-chitosan-aerogel, Polymer 2021), NOT a chitosan beads mechanism paper. The Lei2021 PDF exists at 仿生文献库/2nd/ but is about carboxymethyl chitosan aerogel for dye removal, not "chitosan beads六种吸附机制". The actual chitosan bead mechanisms are described in the missing Vo2023 review PDF. The 6 mechanisms (electrostatic, complexation, hydrogen bonding, acid-base, coordination/chelation, ion exchange) are documented in Vo2023 extraction JSON ki_003 (page 3, "Adsorption mechanisms section"). Recommendation: mech-1 DOI should be corrected to 10.1007/s10311-023-01563-9 (Vo2023) once PDF is obtained. Target in prototypes_db: lobster-exoskeleton.json mechanisms[0]. |

## Summary

- **0/3 claims** have a readable local PDF.
- **2 claims** (perf-1, narr-1): `missing_pdf` — the Vo2023 chitosan beads review PDF is not in the library. The `第1组-配位螯合` directory does not exist (directories are 第2组 through 第8组 only).
- **1 claim** (mech-1): `wrong_source` — DOI 10.1016/j.polymer.2020.123316 belongs to Lei2021 (mussel-magnetic carboxymethyl chitosan aerogel), not a chitosan beads mechanism paper. The correct source is the missing Vo2023 review.
- The `2024-Vo-wastewater-review 2.pdf` in 第7组-系统仿生 is confirmed as "Microalgae-bacteria consortia for organic pollutants remediation from wastewater" (Tan Phat Vo et al.), not the chitosan beads review. Must not be used as evidence.
- Extraction JSON for Vo2023 exists with 31 knowledge items but all are unverified. Treat as extraction-only evidence; do not upgrade status.
