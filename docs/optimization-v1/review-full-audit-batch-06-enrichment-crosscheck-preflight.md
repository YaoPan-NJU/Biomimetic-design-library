# Full Audit Batch 06: enrichment mirror crosscheck preflight

status: codex_preflight_reviewed

## Scope

- **Batch ID:** `full-audit-06-enrichment-crosscheck`
- **Files inspected:** all 24 files under `prototypes_db/enrichment/*.json`
- **Audit date:** 2026-06-16
- **Worker:** Codex local JSON consistency preflight (`find`, `jq`)
- **Reason for preflight:** enrichment files are evidence mirrors or causal-chain expansions for audited prototypes, but they have a different structure from main JSONs and mostly contain empty causal-chain placeholders. No `prototypes_db/*.json` files were modified.

## Summary

- 24 enrichment files exist.
- 4 enrichment files are empty objects with no `mechanisms`: `biomineralization-template`, `coral-skeleton`, `dna-aptamer`, `magnetic-bacteria`.
- 20 enrichment files use `mechanisms` as an object keyed by mechanism names, while main JSONs use `mechanisms` arrays.
- Across those 20 files, there are 525 enrichment mechanism entries and all 525 have blank or placeholder causal-chain fields.
- 8 enrichment files have mechanism-count mismatches against their corresponding main JSONs.
- Enrichment files generally do not carry enough source metadata, locators, or verification quotes to be treated as evidence.

## Consistency Table

| prototype_id | main_mechanisms | enrichment_mechanisms | status | notes |
|---|---:|---:|---|---|
| biomineralization-template | 1 | none | missing_mirror | enrichment file is `{}` |
| bone-structure | 5 | 5 | placeholder_only | all causal chains blank |
| cell-membrane-ion-channel | 13 | 13 | placeholder_only | all causal chains blank |
| chitosan | 132 | 132 | placeholder_only | all causal chains blank |
| chlorella-cell-wall | 13 | 13 | placeholder_only | all causal chains blank |
| coral-skeleton | 1 | none | missing_mirror | enrichment file is `{}` |
| diatom-frustule | 15 | 13 | count_mismatch | all causal chains blank |
| dna-aptamer | 1 | none | missing_mirror | enrichment file is `{}` |
| fish-scale-hydroxyapatite | 89 | 89 | placeholder_only | all causal chains blank; includes wrong-source groups already queued in Batch 02 |
| iron-oxidizing-bacteria | 6 | 6 | placeholder_only | all causal chains blank |
| lobster-exoskeleton | 1 | 1 | placeholder_only | all causal chains blank |
| magnetic-bacteria | 1 | none | missing_mirror | enrichment file is `{}` |
| mangrove-root | 1 | 1 | placeholder_only | all causal chains blank |
| mussel-foot-adhesion | 88 | 88 | placeholder_only | all causal chains blank; not yet audited as a main batch prototype |
| mycelium | 4 | 4 | placeholder_only | all causal chains blank |
| oyster-shell | 3 | 3 | placeholder_only | all causal chains blank |
| pitcher-plant-slippery-surface | 22 | 21 | count_mismatch | all causal chains blank |
| plant-tannin | 14 | 13 | count_mismatch | all causal chains blank |
| polydopamine-coating | 65 | 65 | placeholder_only | all causal chains blank |
| scallop-shell | 3 | 3 | placeholder_only | all causal chains blank |
| silk-fibroin | 20 | 19 | count_mismatch | all causal chains blank |
| spider-silk | 31 | 31 | placeholder_only | all causal chains blank |
| sulfate-reducing-bacteria | 1 | 1 | placeholder_only | all causal chains blank |
| wood-xylem | 4 | 4 | placeholder_only | all causal chains blank |

## Field Audit Table

| item_id | target_json | field_path | field_type | finding | evidence_label | recommended_action | notes |
|---|---|---|---|---|---|---|---|
| ENR-STRUCT-01 | `prototypes_db/enrichment/*.json` | `mechanisms` | schema | Enrichment `mechanisms` is an object keyed by mechanism names, while main JSON `mechanisms` is an array. | partial | Treat enrichment as a separate mirror schema or write migration rules before automated syncing. | Scripts assuming arrays will fail. |
| ENR-PLACEHOLDER-01 | 20 enrichment files | `mechanisms.*.causal_chain` | causal_chain | 525/525 enrichment mechanism entries have blank causal-chain fields or placeholder `needs_review` values. | inferred_only | Do not use enrichment causal chains as evidence until populated from approved source rows. | This includes Batch 01-05 audited prototypes. |
| ENR-EMPTY-01 | biomineralization-template, coral-skeleton, dna-aptamer, magnetic-bacteria | entire enrichment file | enrichment | Four enrichment files are `{}` despite corresponding main JSONs containing at least one mechanism. | knowledge_gap | Populate from main JSON only after source verification, or explicitly mark empty. | Three of these were priority/prototype review targets. |
| ENR-COUNT-01 | diatom-frustule, pitcher-plant-slippery-surface, plant-tannin, silk-fibroin | mechanism count | consistency | Enrichment mechanism count is lower than main JSON count. | partial | Reconcile after wrong-source removals and source-approved cleanup. | Count mismatch should not be fixed blindly before Yao decisions. |
| ENR-SOURCE-01 | enrichment mirror set | source metadata | metadata | Enrichment entries usually lack source_file, locator, and direct verification_quote fields. | inferred_only | Treat enrichment as derived/placeholder until fields are tied back to approved source evidence. | Avoid source-free causal-chain claims. |
| ENR-SCOPE-01 | `prototypes_db/enrichment/mussel-foot-adhesion.json` | entire enrichment file | scope | Mussel-foot-adhesion has 88 enrichment entries but has not yet been audited in the main full-audit batch plan. | knowledge_gap | Park for later main-prototype audit or add to a future batch. | Do not clean it opportunistically inside enrichment-only work. |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| ENR-BD-01 | `prototypes_db/enrichment/*.json` | `mechanisms.*.causal_chain` | knowledge_gap | Enrichment causal chains are empty placeholders. | Do not use enrichment causal chains as reviewed evidence or design boundaries. | N/A | JSON scan | N/A | inferred_only | Populate only after source-backed main JSON decisions. |
| ENR-BD-02 | biomineralization-template, coral-skeleton, dna-aptamer, magnetic-bacteria enrichment files | entire enrichment file | knowledge_gap | Enrichment mirrors are empty objects. | Do not infer absence of mechanisms from empty enrichment mirrors. | N/A | JSON scan | `{}` | knowledge_gap | Main JSONs still contain mechanisms. |
| ENR-BD-03 | enrichment/main mismatch files | mechanism mirror count | knowledge_gap | Enrichment and main mechanism counts differ. | Do not synchronize mechanically until wrong-source cleanup and Yao decisions are resolved. | N/A | JSON scan | count mismatch | partial | Applies to diatom, pitcher plant, plant tannin, silk fibroin, and empty mirror files. |

## Recommended Next Step

- Treat Batch 06 as a schema/consistency issue, not a literature-content issue.
- Do not edit enrichment JSONs until Yao approves main JSON cleanup decisions, because wrong-source rows should not be propagated into causal chains.
- When cleanup is approved, use a two-stage process: first resolve main JSON source decisions, then regenerate or populate enrichment causal chains from accepted rows with source locators.
