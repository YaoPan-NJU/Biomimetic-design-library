# Evidence Review Batch: coral-skeleton

status: ready_for_codex_review

> Generated: 2026-06-16T02:00+08:00 | Actor: OpenClaw/mimo-v2.5
> Source files inspected:
> - prototypes_db/coral-skeleton.json
> - tools/litextract/outputs/extractions/论文/json/2020-Han-antifouling-review.json
> - PDF search: `仿生文献库/论文/` (recursive, case-insensitive for coral/coralline/CaCO3/carbonate/aragonite/phosphate/heavy metal/adsorption)
> - evidence-review-report.md (coral-skeleton section)

## Summary

- **2 claims checked**, 0 verbatim quotes extracted (no PDFs available for this prototype).
- **1 missing_pdf**: mech-1 has no source file; no coral-skeleton-specific PDF exists in the local library.
- **1 wrong_source**: narr-1 references 2020-Han-antifouling-review, which is a marine antifouling coatings review — not about coral skeleton CaCO3 adsorption. Additionally, the PDF does not exist locally.

### PDF Search Results

| search_pattern | result |
|---|---|
| `*coral*` | **0 matches** in 仿生文献库/ |
| `*coralline*` | **0 matches** |
| `*CaCO3*` | **0 matches** (CaCO₃ appears in filenames as `CaCO3` but none matched coral context) |
| `*carbonate*` | **0 matches** |
| `*aragonite*` | **0 matches** |
| `*2020*Han*antifouling*` | **0 matches** — extraction JSON says file_name=`2020-Han-antifouling-review.pdf` but no such PDF in library |

### Why 2020-Han is wrong_source

The extraction JSON (`2020-Han-antifouling-review.json`) metadata shows:
- **Title**: "The progress on antifouling organic coating: From biocide to biomimetic surface"
- **DOI**: 10.1016/j.jmst.2020.07.002
- **Topic**: Marine antifouling organic coatings (biocide→biomimetic surface evolution)
- **Content** (from narrative entry): Covers biofouling stages, Sharklet micro-topography, PDMS coatings, zwitterionic hydrogels, Baier curve surface energy theory

This is a **coatings/materials review** about preventing marine biofouling on ship hulls and membranes. It has **no connection** to coral skeleton CaCO3 adsorption of heavy metals or phosphate. The narrative entry in `coral-skeleton.json` maps "antifouling biological solutions" to coral skeleton, which is a misattribution — coral is mentioned as one of many organisms in the antifouling context, not as a CaCO3 adsorption material.

---

## Claim Review Table

| claim_id | prototype_id | source_pdf_path | path_exists_yes_no | page_or_section | candidate_quote | quote_supports_claim_yes_no | source_is_on_topic_yes_no | needs_multimodal_yes_no | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| mech-1 | coral-skeleton | N/A (source_file: null in prototypes_db/coral-skeleton.json mechanisms[0]) | no | N/A | N/A - source PDF missing | N/A | N/A | no | missing_pdf | Claim is 100% LLM-inferred: "珊瑚骨骼的多孔CaCO₃结构与牡蛎壳类似，可通过离子交换和沉淀机制去除重金属和磷酸盐". No local PDF supports this. No coral/coralline/CaCO3/aragonite PDF exists in 仿生文献库/. Requires Phase 8 C-class literature download (coral skeleton + CaCO3 + adsorption + heavy metal/phosphate). Target: prototypes_db/coral-skeleton.json mechanisms[0]. |
| narr-1 | coral-skeleton | /Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/outputs/extractions/论文/json/2020-Han-antifouling-review.json (extraction JSON only; PDF not found locally) | no | N/A | N/A - source PDF missing | no | no | no | wrong_source | 2020-Han-antifouling-review is "The progress on antifouling organic coating: From biocide to biomimetic surface" (DOI: 10.1016/j.jmst.2020.07.002). Topic: marine antifouling coatings (Sharklet, PDMS, zwitterionic hydrogels). NOT about coral skeleton CaCO3 adsorption. The narrative entry maps antifouling strategies to coral skeleton — a misattribution. Target: prototypes_db/coral-skeleton.json narrative.entries[0]. Recommend: remove this narrative entry or replace with a genuine coral skeleton adsorption source. |
