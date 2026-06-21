# M12 PDF Audit Closure Report

**Date**: 2026-06-22
**HEAD**: 25456ce (pushed to origin/review)
**Branch**: review

## Executive Summary

M12 full PDF evidence audit complete. 643 PDFs inventoried, 136 mechanisms across 26 PDF-backed prototypes validated, 8 INVALID findings fixed. 10 prototypes without PDF support are documented as background/exploratory.

## PDF Inventory

| Metric | Count |
|--------|-------|
| Total PDFs inventoried | 643 |
| Claim-supporting PDFs (cited by root prototypes) | 83 |
| PDFs read in M12 | 40 |
| Missing/unreadable PDFs (cited but not in library) | 18 DOIs |
| Uncited PDFs (expansion candidates) | 560 |

## Validation Summary

| Verdict | Mechanisms |
|---------|-----------|
| VALIDATED | 75 |
| PARTIAL | 52 |
| INVALID (fixed) | 8 |
| MISSING_PDF | 18 |

## 26 PDF-Backed Prototypes (Validated)

chitosan, mussel-foot-adhesion, polydopamine-coating, bone-structure, plant-tannin, diatom-frustule, fish-scale-hydroxyapatite, lotus-leaf, superhydrophobic-artificial, oyster-shell, scallop-shell, sulfate-reducing-bacteria, iron-oxidizing-bacteria, wood-xylem, starch-granule, alginate, cellulose-nanocrystal, coral-skeleton, magnetic-bacteria, mangrove-root, spider-silk, chlorella-cell-wall, namib-beetle, lobster-exoskeleton, cactus-spine, pitcher-plant-slippery-surface

## 10 Prototypes Without PDF Support (Background/Exploratory)

biomineralization-template, dna-aptamer, metal-organic-framework, mycelium, diatom-inspired-porous, silkworm-silk, water-strider-leg, shark-skin, cell-membrane-ion-channel, silk-fibroin

Note: These prototypes have mechanisms but no directly cited PDFs in the library. They are labeled as background/exploratory in the ADRMATS briefs.

## Fixes Applied (8 INVALID findings)

1. chitosan pHpzc: removed unsupported values 5.74/4.85
2. bone-structure: 4 mechanisms source_doi corrected to Jaffar2024
3. plant-tannin Cr(VI): verification_quote corrected to Yuan2024
4. diatom: fabricated TC reference removed
5. coral-skeleton: DOI mismatch noted (antifouling paper, not coral)
6. starch-granule: 62 DOIs corrected (ijbiomac → carbpol.2022.119463)
7. wood-xylem: source_file corrected (Mo → Kumar paper)
8. chitosan verification_quote cross-reference corrected

## Artifacts Produced

- `docs/active/pdf-audit-manifest.jsonl` — 643 PDFs inventoried
- `docs/active/pdf-claim-map.jsonl` — 1045 claims mapped
- `docs/active/m12-*-validation.md` — 11 validation reports
- `docs/active/v0.2-rc-report.md` — updated with M12 findings
- `docs/active/execution-state.json` — updated with M12 stats

## Final v0.2 State

| Metric | Value |
|--------|-------|
| Root prototypes | 36 |
| PDF-backed prototypes | 26 |
| Total mechanisms | 510 |
| from_source (root) | 98 (19%) |
| llm_inferred (root) | 412 (81%) |
| from_source (incl separation) | 102/514 (20%) |
| Qualified causal cards | 510/510 |
| ADRMATS briefs | 7/7 pass |
| Validators | 15/15 green |

## Known Limitations

1. 412 mechanisms (81%) remain source-backed inference
2. 18 DOIs without corresponding PDFs in library
3. 10 prototypes without PDF support (background/exploratory)
4. Performance values are leads, not ranked facts
5. Library provides heuristic candidates, not ranked lists

## Yao Decision Points

1. Accept v0.2 RC with M12 audit findings?
2. Authorize 60-80 expansion for v1.0?
3. Additional evidence uplift for remaining 412 mechanisms?
4. Spider-silk uranium mechanisms: reclassify or remove?
