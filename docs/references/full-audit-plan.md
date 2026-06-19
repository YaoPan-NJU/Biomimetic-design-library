# Full Evidence Audit Plan

status: active

Last updated: 2026-06-16

## Decision Policy

Selected mode: A1 + B1 + C1.

- A1: phased full audit across the prototype library.
- B1: queue-before-edit; do not modify `prototypes_db/*.json` until Yao approves queued actions.
- C1: evidence-graded boundaries using `hard_do_not`, `soft_boundary`, and `knowledge_gap`.

## Hard Rules

- Do not modify `prototypes_db/*.json` during audit batch generation.
- Do not run `tools/build_prototypes_db.py`.
- Do not upgrade `verification` or hard/soft boundary status without explicit approval.
- Every supported field needs source, locator, and quote when the source PDF exists.
- Missing PDFs, wrong sources, and inferred-only fields must be explicitly labeled.
- DO-NOT and boundary items must include evidence grade and target JSON path.

## Field Coverage

Each batch audits these field families where present:

- `performance_data`
- `mechanisms`
- `mechanisms[].causal_chain`
- `mechanisms[].causal_chain.boundary_conditions`
- `narrative.entries`
- `engineering_constraints`
- source metadata: `source_file`, `ref_doi`, `page`, `locator`, `verification`, `verification_quote`
- derived quality flags: `missing_pdf`, `wrong_source`, `inferred_only`, `quote_mismatch`, `locator_missing`

## Evidence Labels

| label | meaning |
|---|---|
| supported | PDF exists and quote/locator directly supports the field. |
| partial | PDF exists but supports only part of the field or requires claim narrowing. |
| keep_soft | useful background or review support, not enough for verified engineering claim. |
| missing_pdf | cited source cannot be found locally. |
| wrong_source | source exists but is about a different topic/claim. |
| inferred_only | field is LLM/domain inferred with no source support. |
| needs_human_decision | evidence is ambiguous or requires policy choice. |

## Boundary Labels

| boundary_type | use |
|---|---|
| hard_do_not | literature-backed constraint that should block recommendation under specified conditions. |
| soft_boundary | evidence-backed caution or operating condition that should influence ranking but not block by itself. |
| knowledge_gap | important boundary suspected or currently inferred, but not yet literature-supported. |

## Batch Plan

| batch_id | scope | files |
|---|---|---|
| full-audit-00-priority | Completed priority review | pitcher-plant, spider-silk, lobster-exoskeleton, magnetic-bacteria, coral-skeleton |
| full-audit-01-biopolymers | Core adsorption biopolymers and coatings | chitosan, polydopamine-coating, plant-tannin, silk-fibroin, wood-xylem |
| full-audit-02-minerals-shells | Mineral/shell/hydroxyapatite prototypes | oyster-shell, scallop-shell, fish-scale-hydroxyapatite, bone-structure, biomineralization-template |
| full-audit-03-microbes-cells | Microbial/cell-wall prototypes | chlorella-cell-wall, iron-oxidizing-bacteria, sulfate-reducing-bacteria, mycelium, cell-membrane-ion-channel |
| full-audit-04-separation-surfaces | Separation and superwetting surfaces | lotus-leaf, shark-skin, water-strider-leg, cactus-spine, superhydrophobic-artificial |
| full-audit-05-selective-materials | Selective/molecular/material-reference set | dna-aptamer, diatom-frustule, mangrove-root, alginate, cellulose-nanocrystal, metal-organic-framework, starch-granule |
| full-audit-06-enrichment-crosscheck | Enrichment mirror consistency | all `prototypes_db/enrichment/*.json` corresponding to audited prototypes |
| full-audit-07-parked-and-registry | Parked and index consistency | parked/namib-beetle plus duplicate/cross-directory source consistency |

## Output Files

- `review-full-audit-worklog.md`
- `review-full-audit-decision-queue.md`
- `review-boundary-do-not-register.md`
- `review-full-audit-batch-*.md`

## GitHub Sync

Push a checkpoint to branch `review` after each completed batch review or after any protocol/schema update.
