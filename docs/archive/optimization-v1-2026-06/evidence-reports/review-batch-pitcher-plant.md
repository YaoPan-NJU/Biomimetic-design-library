# Evidence Batch: pitcher-plant-slippery-surface

status: ready_for_codex_review

## Batch Metadata

| field | value |
|---|---|
| prototype_id | pitcher-plant-slippery-surface |
| source_pdf | tools/litextract/workspace/pdf_review/zeng2021-antifouling-review-2.pdf |
| paper_id | Zeng2021_SLIPS_Review |
| doi | 10.1007/s42242-021-00133-8 |
| claims_checked | 5 (4 upgrade_candidate + 1 wrong_source) |
| batch_created | 2026-06-16 |

## Claim Evidence Table

| claim_id | prototype_id | source_pdf_path | path_exists_yes_no | page_or_section | candidate_quote | quote_supports_claim_yes_no | source_is_on_topic_yes_no | needs_multimodal_yes_no | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| mech-1 | pitcher-plant-slippery-surface | /Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/zeng2021-antifouling-review-2.pdf | yes | p.507 (PDF p.2), "Theoretical foundation" section | "when the angle is 90° < θ ≤ 180°, the surface not be wetted by water and is called hydrophobic" | yes | yes | no | upgrade_candidate | Verbatim Young's model discussion. Defines hydrophobic threshold as 90° < θ ≤ 180°. Original library path: 仿生文献库/论文/第2组-超疏水/2021-Zeng-antifouling-porous-review 2.pdf |
| mech-4 | pitcher-plant-slippery-surface | /Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/zeng2021-antifouling-review-2.pdf | yes | p.509–510 (PDF p.4–5), SLIPS section | "The peristome is characterized by a regular microstructure with radial ridges of smooth overlapping epidermal cells, which form a series of steps toward the pitcher inside and make it superhydrophilic. This superhydrophilic surface can be completely wetted by rain in humid weather, so that a uniform liquid film covers the surface." | yes | yes | no | upgrade_candidate | Verbatim Nepenthes trapping mechanism: peristome microstructure → superhydrophilic → uniform liquid film → insect aquaplaning. Original library path: 仿生文献库/论文/第2组-超疏水/2021-Zeng-antifouling-porous-review 2.pdf |
| mech-10 | pitcher-plant-slippery-surface | /Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/zeng2021-antifouling-review-2.pdf | yes | p.515–516 (PDF p.10–11), lubricant loss section | "The common means of lubricant loss are diffusion to the surrounding surface, external shear, and the influence of gravity or evaporation" | yes | yes | no | upgrade_candidate | Verbatim lubricant loss mechanisms: four pathways (diffusion, shear, gravity, evaporation). Original library path: 仿生文献库/论文/第2组-超疏水/2021-Zeng-antifouling-porous-review 2.pdf |
| perf-1 | pitcher-plant-slippery-surface | /Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/zeng2021-antifouling-review-2.pdf | yes | p.518 (PDF p.13), anti-icing section, Figs. 9i–9k | "the tensile force required to pull off the surface without lubrication is about six times that required for SLIPS" | yes | yes | no | upgrade_candidate | Verbatim Mg alloy SLIPS ice adhesion data: bare Mg sheet requires ~6× the force vs SLIPS for ice removal. Ref: Long et al. spraying method. Original library path: 仿生文献库/论文/第2组-超疏水/2021-Zeng-antifouling-porous-review 2.pdf |
| narr-3 | pitcher-plant-slippery-surface | /Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/outputs/extractions/论文/json/2022-Progress-review.json | yes | N/A (fog harvesting review) | N/A — paper title: "Fog Harvesting Devices Inspired from Single to Multiple Creatures"; DOI: 10.1002/adfm.202200359 | no | no | no | wrong_source | Yu2022 is a fog harvesting/water collection review. While it mentions pitcher plant, the target is fog droplet collection, not SLIPS/slippery surfaces for anti-fouling. Off-topic for this prototype. Original library path: 仿生文献库/论文/第2组-超疏水/2022-Progress-review.pdf |

## Summary

- **4 claims upgraded** from needs_review → upgrade_candidate with verbatim PDF quotes from Zeng2021
- **1 claim flagged** as wrong_source (Yu2022 fog harvesting review — off-topic for SLIPS prototype)
- **0 claims** need multimodal re-read (all quotes verified via text-layer PDF extraction)
- All source PDFs confirmed to exist on disk
- No missing PDFs in this batch
