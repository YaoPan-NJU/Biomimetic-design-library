# Evidence Review Batch — magnetic-bacteria

> **Status:** ready_for_codex_review
> **Actor:** OpenClaw/mimo-v2.5
> **Date:** 2026-06-16
> **Source PDF:** `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf`
> **Original library path:** `/Users/panyao/Desktop/Biomimetic-design-library/仿生文献库/论文/第6组-功能仿生/2022-Mtb-biomineralization-magnetic-heavy-metal-review 3.pdf`
> **Target JSON:** `prototypes_db/magnetic-bacteria.json`
> **Extraction JSON:** `tools/litextract/outputs/extractions/论文/json/2022-Mtb-biomineralization-magnetic-heavy-metal-review.json`

---

## Summary

The primary PDF (Goswami2022, npj Biofilms and Microbiomes) is a **review paper** on magnetotactic bacteria (MTB) ecology, evolution, and environmental implications. It covers MTB biomineralization, magnetosome structure, heavy-metal sequestration, and bioremediation potential — but as a **review/background source**, not a direct experimental study on a designed engineered adsorbent system.

All performance-like claims in the extraction JSON (Cd²⁺, Co²⁺, Se, Te) refer to **organismal biogeochemistry** (culture-based MTB experiments on living cells) or **review-reported examples**, not to a designed magnetosome-based adsorbent material. Therefore, no claim qualifies for `upgrade_candidate`. The correct action is `keep_soft` for background-supported claims and `needs_human_decision` where the claim bridges organismal biology and engineering design.

---

## Claim Review Table

| claim_id | prototype_id | source_pdf_path | path_exists_yes_no | page_or_section | candidate_quote | quote_supports_claim_yes_no | source_is_on_topic_yes_no | needs_multimodal_yes_no | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| mech-1 | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.1 Introduction | "MTB form magnetite (Fe3O4) and/or greigite (Fe3S4) crystals, generally in bead-like chains." | Yes — supports magnetosome as natural magnetic nanoparticles with chain structure | Yes | No | keep_soft | Supports background concept: magnetosomes are natural magnetic NPs in chain arrangement. But this is organismal biology, not an engineered adsorbent. Original library: `仿生文献库/论文/第6组-功能仿生/2022-Mtb-biomineralization-magnetic-heavy-metal-review 3.pdf`. Target: `prototypes_db/magnetic-bacteria.json`. |
| mech-1 | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.9 Outlook | "The magnetism of MTB ensures that metal-loaded MTB cells can be separated magnetically from contaminated waters." | Yes — directly supports magnetic separation/recovery concept | Yes | No | keep_soft | Confirms magnetic separation principle for MTB cells. However, this describes whole-cell magnetic separation, not a functionalized magnetosome adsorbent material. Does not demonstrate surface functionalization for adsorption after extraction. |
| mech-1 | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.1 Introduction | "MTB are so far the only known group of prokaryotes with the ability to perform both biomineralization and magnetoreception." | Partially — establishes MTB uniqueness but not adsorption-after-functionalization | Yes | No | keep_soft | Establishes biomineralization + magnetoreception dual capability. The claim specifies "adsorption after functionalization" which is not directly demonstrated in this review. |
| narr-1 | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.9 Outlook | "In addition, MTB can be used in pollution bioremediation by accumulating heavy metals on their surfaces by adsorption (e.g., Cd) and intracellularly (e.g., O3Te2− and Se)." | Yes — supports MTB heavy-metal sequestration background narrative | Yes | No | keep_soft | Directly supports the narrative that MTB sequester heavy metals via surface adsorption and intracellular accumulation. This is a review-reported summary of culture experiments, not an engineered adsorbent study. |
| narr-1 | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.9 Ecosystem functions of MTB | "A novel Alphaproteobacterium MTB species grown in a cobalt supplemented medium has efficient biosorption competence with 89% cobalt removed by magnetic separation." | Yes — supports MTB bioremediation narrative with quantitative example | Yes | No | keep_soft | 89% Co removal via magnetic separation of biomass is a culture-based organismal result, not a designed adsorbent system. Keep as background evidence. |
| perf-cd | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.9 Ecosystem functions of MTB | "Arakaki and colleagues observed electron-dense Cd2+ deposits enveloping RS-1 cell surfaces under TEM when cells were cultured in growth media containing 1.3 ppm Cd2+. Mono-dispersed crystalline inclusions have 20–40 nm sizes and were easily distinguished from magnetic particles in TEM images." | Yes — supports Cd²⁺ surface adsorption on MTB cells | Yes | No | keep_soft | Organismal biogeochemistry: Cd²⁺ adsorption on living RS-1 cells at 1.3 ppm. This is not an engineered adsorbent; the 20–40 nm deposits are on cell surfaces, not on extracted/functionalized magnetosomes. |
| perf-se-te | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.9 Ecosystem functions of MTB | "Se accumulated by MTB is higher than O3Te2− uptake and Cd adsorbed by factors of 2.4 and 174, respectively." | Yes — supports Se/Te/Cd comparative accumulation data | Yes | No | keep_soft | Review-reported quantitative comparison of intracellular Se vs Te vs Cd accumulation in MTB cultures. Not an engineered adsorbent performance claim. Treat as background organismal data only. |
| perf-co | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.9 Ecosystem functions of MTB | "A novel Alphaproteobacterium MTB species grown in a cobalt supplemented medium has efficient biosorption competence with 89% cobalt removed by magnetic separation of the biomass." | Yes — supports Co²⁺ removal via MTB magnetic separation | Yes | No | keep_soft | 89% Co removal is from a culture experiment on living MTB cells, not from an engineered magnetosome-based adsorbent. Keep as organismal background. |
| magnetosome-structure | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.6 Ecosystem functions of MTB | "Magnetotaxis is best achieved with fully developed crystals (~30–150 nm) rather than with immature crystals (~30 nm or smaller)." | Yes — supports optimal magnetosome size for magnetic function | Yes | No | keep_soft | 30–150 nm optimal size window is well-supported. Relevant to biomimetic material design but this is organismal optimal size, not an engineered material specification. |
| magnetosome-chain | magnetic-bacteria | `/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/workspace/pdf_review/mtb2022-magnetic-heavy-metal-3.pdf` | Yes | p.4 Magnetic characterization | "the entire chain will act as a single needle with uniaxial magnetization that does not interact with other chains" | Yes — supports chain-as-single-domain concept | Yes | No | keep_soft | Chain magnetic behavior well-documented in review. Supports the biomimetic design principle of chain-like magnetic structures. |

---

## Key Findings

1. **All claims are background-supported, not upgradeable.** The PDF is a T5_review (literature review) and provides organismal/biogeochemical background on MTB, not experimental data on a designed magnetosome-based adsorbent.

2. **Performance data (Cd, Co, Se, Te) are organismal, not engineered.** The 89% Co removal, Cd²⁺ surface deposits, and Se/Te intracellular accumulation all come from culture experiments on living MTB cells, not from functionalized magnetosome adsorbents.

3. **The "adsorption after functionalization" aspect of mech-1 is not directly addressed.** The review describes surface adsorption on living cells (Cd²⁺, Co²⁺) and intracellular accumulation (Se, Te), but does not discuss extracting magnetosomes and functionalizing them as standalone adsorbent materials.

4. **No multimodal check needed.** All claims can be evaluated from the text layer; no figures/tables require visual inspection for these specific claims.

5. **C-class literature gap confirmed.** As noted in the evidence-review-report, a dedicated experimental paper on magnetosome extraction, functionalization, and adsorption performance is needed to upgrade mech-1 beyond `keep_soft`.
