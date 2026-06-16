# Evidence Review Sync Summary

status: active_full_audit

Last updated: 2026-06-16 14:12 Asia/Shanghai

## Scope

This review covered the five priority prototypes from `evidence-review-report.md`:

- `pitcher-plant-slippery-surface`
- `spider-silk`
- `lobster-exoskeleton`
- `magnetic-bacteria`
- `coral-skeleton`

The task was evidence review and decision preparation only. No `prototypes_db/*.json` files were edited, and `tools/build_prototypes_db.py` was not run.

## Outputs

- `docs/optimization-v1/evidence-review-report.md`
- `docs/optimization-v1/review-worklog.md`
- `docs/optimization-v1/review-decision-queue.md`
- `docs/optimization-v1/review-batch-pitcher-plant.md`
- `docs/optimization-v1/review-batch-spider-silk.md`
- `docs/optimization-v1/review-batch-lobster-exoskeleton.md`
- `docs/optimization-v1/review-batch-magnetic-bacteria.md`
- `docs/optimization-v1/review-batch-coral-skeleton.md`

## Results By Prototype

| prototype_id | result |
|---|---|
| pitcher-plant-slippery-surface | 4 Zeng2021 evidence items queued; 1 Yu2022 fog-harvesting wrong_source decision queued. |
| spider-silk | 7 strong Zhou2021/Zhang2021 evidence items queued; 1 antifouling mechanism item requires claim narrowing or additional elasticity evidence. |
| lobster-exoskeleton | Vo2023 PDF is missing locally; 1385 mg/g remains extraction-only/unverified. Current mechanism DOI points to the wrong source. |
| magnetic-bacteria | Goswami2022 supports MTB background and magnetic separation as keep_soft only; no engineered magnetosome adsorbent evidence found. |
| coral-skeleton | Coral CaCO3 adsorption source is missing; Han2020 antifouling review is wrong_source for coral-skeleton adsorption. |

## Decision Queue

`review-decision-queue.md` now contains decision-ready items for Yao approval. `queued_for_yao_decision` does not authorize edits by itself.

Approval is needed before:

- adding quotes/locators to prototype JSON files,
- changing any verification status,
- removing wrong-source narrative entries,
- replacing missing PDFs or changing source DOI/path metadata.

## GitHub Sync Policy

Milestone updates are pushed to the `review` branch so progress is visible remotely while local review continues.

## Execution Model

Current role split:

- OpenClaw owns bulk PDF/extraction/OCR verification and draft batch outputs.
- Codex owns scope control, key decisions, stage acceptance, spot checks, queue curation, boundary register, worklog/sync summary, and GitHub checkpoints.
- Codex should not do large manual row-by-row audits unless needed for acceptance spot checks or critical disputes.

## Full Audit Continuation

Yao selected A1+B1+C1 for the next stage:

- phased full audit across the prototype library,
- queue-before-edit, with no `prototypes_db/*.json` edits before approval,
- evidence-graded boundaries: `hard_do_not`, `soft_boundary`, `knowledge_gap`.

## Full Audit Outputs

- `docs/optimization-v1/review-full-audit-plan.md`
- `docs/optimization-v1/review-openclaw-coordination.md`
- `docs/optimization-v1/review-openclaw-next-tasks.md`
- `docs/optimization-v1/review-openclaw-worker-prompts.md`
- `docs/optimization-v1/review-full-audit-worklog.md`
- `docs/optimization-v1/review-full-audit-decision-queue.md`
- `docs/optimization-v1/review-boundary-do-not-register.md`
- Batch 01 files for `chitosan`, `polydopamine-coating`, `plant-tannin`, `silk-fibroin`, `wood-xylem`
- Batch 02 files for `biomineralization-template`, `bone-structure`, `oyster-shell`, `scallop-shell`, plus `fish-scale-hydroxyapatite` preflight
- Batch 03 preflight file for `chlorella-cell-wall`, `iron-oxidizing-bacteria`, `sulfate-reducing-bacteria`, `mycelium`, and `cell-membrane-ion-channel`
- Batch 04 preflight file for `lotus-leaf`, `shark-skin`, `water-strider-leg`, `cactus-spine`, and `superhydrophobic-artificial`
- Batch 05 preflight file for `dna-aptamer`, `diatom-frustule`, `mangrove-root`, and material-reference `alginate`, `cellulose-nanocrystal`, `metal-organic-framework`, `starch-granule`
- Batch 06 enrichment mirror crosscheck file for all 24 `prototypes_db/enrichment/*.json` files

## Latest Checkpoint

OpenClaw next-task package is prepared after Batch 06 enrichment mirror crosscheck. No prototype JSON files were edited and `tools/build_prototypes_db.py` was not run.

| area | latest result |
|---|---|
| execution model | OpenClaw owns bulk evidence verification; Codex owns stage acceptance, spot checks, queue curation, boundaries, and GitHub checkpoints. |
| next OpenClaw tasks | Prepared task list and copy-paste worker prompts for Batch 07 parked/registry consistency, DNA aptamer evidence build, diatom path/dedup cleanup, MOF verification semantics, and starch extreme-value sanity checks. |
| enrichment schema | Enrichment `mechanisms` are object maps keyed by mechanism names, while main JSON `mechanisms` are arrays. |
| causal chains | 525/525 enrichment mechanism entries have empty or placeholder causal-chain fields. |
| empty mirrors | `biomineralization-template`, `coral-skeleton`, `dna-aptamer`, and `magnetic-bacteria` enrichment files are `{}` despite main JSON mechanisms. |
| count mismatches | `diatom-frustule`, `pitcher-plant-slippery-surface`, `plant-tannin`, and `silk-fibroin` enrichment mirrors have fewer mechanisms than main JSONs. |
| evidence policy | Enrichment entries should not be treated as source-backed evidence until populated from approved main JSON rows with locators and quotes. |

## Prior Full-Audit Checkpoint

Batch 05 selective/material-reference preflight remains queued for Yao decision.

| prototype_id | latest result |
|---|---|
| dna-aptamer | Underbuilt: zero performance rows, one mechanism, zero provenance, and empty enrichment mirror despite local aptamer PDFs/extractions. |
| diatom-frustule | Local PDFs exist for major source groups, but source paths are often bare or suffix-mismatched; duplicated row groups need cleanup before quote insertion. |
| mangrove-root | Evidence is constructed-wetland/system removal percentage evidence; keep separate from material qmax ranking. |
| alginate | Largest row block depends on missing Dong2025 PDF; patent rows need exact path and paragraph locators. |
| cellulose-nanocrystal | Overbroad material-reference store mixing CNC, CNF, general cellulose, bio-foam, diatomite composite, membrane, and tannin-cellulose evidence. |
| metal-organic-framework | `n_verified=252` is mostly `verification=single_source`, not full quote+locator verification; chitosan and membrane rows are wrong-source candidates. |
| starch-granule | All performance rows are unverified and several extreme/mixed-unit review-table values need sanity checking before ranking. |

## Earlier Full-Audit Checkpoint

Batch 04 separation/superwetting surfaces preflight remains queued for Yao decision.

| prototype_id | latest result |
|---|---|
| lotus-leaf | Overaggregated special-wettability/oil-water-separation store with 355 mechanisms and zero verified provenance; needs split before row-level quote insertion. |
| shark-skin | Zero performance rows and mostly generic antifouling/superhydrophobic background mechanisms; direct shark-skin performance evidence is still a knowledge gap. |
| water-strider-leg | Zero performance rows and generic wetting/membrane rows; keep as background until direct water-strider evidence is added. |
| cactus-spine | Zero performance rows and mixed cactus/desert-beetle/honeycomb/fog-collection content; needs scope split. |
| superhydrophobic-artificial | CN113244892B and CN121130847A provide the strongest direct artificial-foam evidence, with scope and wettability-classification caveats queued. |

## Older Full-Audit Checkpoint

Batch 03 microbes/cells preflight remains queued for Yao decision.

| prototype_id | latest result |
|---|---|
| chlorella-cell-wall | Cheng2021 supports Pb microalgae adsorption and Peng2022 supports Chlorella-derived magnetic biochar, but dye-mechanism and wastewater-technology rows need correction or reassignment. |
| iron-oxidizing-bacteria | Luo2021/Jhariya2024 Fe-mineral evidence is useful with metadata fixes; CN113275374A scanned patent/MICP rows need OCR and scope decision. |
| sulfate-reducing-bacteria | Kumar2020 supports SRB sulfide-precipitation mechanism, but there are zero verified performance rows and iron-cycle constraints are wrong-source. |
| mycelium | Liu2021 fungal biosorption evidence is usable with locator/title cleanup; Zhang2022 cellulose/nanocellulose rows are wrong-source or scope-split candidates. |
| cell-membrane-ion-channel | Evidence supports membrane separation/ion-selective filtration more than adsorption; metric rows must be separated from adsorption qmax before ranking. |

## Oldest Full-Audit Checkpoint

Batch 02 mineral/shell audit remains queued for Yao decision.

| prototype_id | latest result |
|---|---|
| biomineralization-template | Wang2025 supports real LanM@ZIF-8 Nd3+ adsorption, but provenance/source metadata and missing performance_data need approval. |
| bone-structure | Bambaeero/Jaffar HAp evidence is usable with metadata fixes; Chen2021 MOF/Cr(VI) rows are wrong-source. |
| oyster-shell | Qiu/Li/Xu phosphate evidence is supported; Wang2021 abalone HA and generic shell/soil reviews need narrowing or reassignment. |
| scallop-shell | Wang2024 scallop Congo Red evidence is strong; existing performance rows are mostly generic shell reviews. |
| fish-scale-hydroxyapatite | Preflight found large membrane/superwetting wrong-source contamination; CN114849640A is the strongest fish-scale HAp source, while CN113275374A needs OCR. |
