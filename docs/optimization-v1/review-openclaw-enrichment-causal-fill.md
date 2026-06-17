---
status: ready_for_qoderwork_acceptance
task: enrichment-causal-chain-batch-fill
date: 2026-06-17
model: xiaomi/mimo-v2.5-pro
scope: prototypes_db/enrichment/*.json
---

# Enrichment Causal Chain Batch Fill Report

## Summary

| Metric | Count |
|--------|-------|
| Total enrichment mechanisms | 478 |
| **Filled this run** | **452** |
| Already filled (pre-existing) | 19 |
| No main JSON match | 1 |
| Main had no description/causal_chain | 6 |
| Files skipped (3 empty per rules) | 3 |

**Fill rate: 452/459 eligible mechanisms (98.5%)**

## Scope

- 24 enrichment JSON files in `prototypes_db/enrichment/`
- 3 skipped: `biomineralization-template.json`, `coral-skeleton.json`, `magnetic-bacteria.json` (per rules: main JSON lacks sufficient mechanism info)
- 21 processed

## Method

1. Enrichment structure: `{mechanisms: {name_key: {causal_chain: {...}}}}`
2. Main JSON structure: `{mechanisms: [{name, causal_chain, description, ref_doi}, ...]}`
3. Matching: exact `name` key match between enrichment dict keys and main JSON mechanism `name` field
4. Fill priority:
   - If main mechanism has non-empty `causal_chain` → direct copy
   - If main mechanism has `description` + `ref_doi` → keyword-based extraction into 4 fields (pollutant_feature, bio_structure, interaction, why_it_works)
   - If neither → leave empty
5. All filled fields tagged with `basis: "from_source"` (if ref_doi present) or `from_mechanism_description`
6. `locator` set to `mechanism[index]` referencing main JSON position

## Per-File Breakdown

| File | Total | Filled | Already | No Match | No Data |
|------|-------|--------|---------|----------|---------|
| bone-structure.json | 5 | 0 | 5 | 0 | 0 |
| cell-membrane-ion-channel.json | 13 | 0 | 13 | 0 | 0 |
| chitosan.json | 132 | 130 | 0 | 0 | 2 |
| chlorella-cell-wall.json | 13 | 13 | 0 | 0 | 0 |
| diatom-frustule.json | 13 | 13 | 0 | 0 | 0 |
| dna-aptamer.json | 1 | 0 | 1 | 0 | 0 |
| fish-scale-hydroxyapatite.json | 89 | 89 | 0 | 0 | 0 |
| iron-oxidizing-bacteria.json | 6 | 6 | 0 | 0 | 0 |
| lobster-exoskeleton.json | 1 | 1 | 0 | 0 | 0 |
| mangrove-root.json | 1 | 1 | 0 | 0 | 0 |
| mussel-foot-adhesion.json | 88 | 86 | 0 | 0 | 2 |
| mycelium.json | 4 | 4 | 0 | 0 | 0 |
| oyster-shell.json | 3 | 3 | 0 | 0 | 0 |
| pitcher-plant-slippery-surface.json | 21 | 20 | 0 | 1 | 0 |
| plant-tannin.json | 13 | 13 | 0 | 0 | 0 |
| polydopamine-coating.json | 17 | 15 | 0 | 0 | 2 |
| scallop-shell.json | 3 | 3 | 0 | 0 | 0 |
| silk-fibroin.json | 19 | 19 | 0 | 0 | 0 |
| spider-silk.json | 31 | 31 | 0 | 0 | 0 |
| sulfate-reducing-bacteria.json | 1 | 1 | 0 | 0 | 0 |
| wood-xylem.json | 4 | 4 | 0 | 0 | 0 |

## Unfilled Mechanisms (7 total)

### No main match (1)
- **pitcher-plant-slippery-surface.json**: `Nepenthes pitcher plant trapping mechanism` — main JSON has no mechanism with this name

### Main had no description/causal_chain (6)
These 3 names appear in 2 enrichment files each (mussel-foot-adhesion + polydopamine + chitosan), so 6 total empty entries:
- `PDA吸附机制-姜黄素` — main JSON has `description: null`, `ref_doi: null`
- `PDA吸附机制-番茄红素` — main JSON has `description: null`, `ref_doi: null`

## Quality Notes

- Pre-existing filled mechanisms (bone-structure, cell-membrane-ion-channel, dna-aptamer) were **not modified** — 19 total
- All enrichment `verification` fields left untouched
- Main JSON files **not modified**
- `build_prototypes_db.py` **not modified**
- No git commits or pushes performed

## Script

`scripts/enrichment_causal_fill.py` — batch processing script, reusable for future runs.
