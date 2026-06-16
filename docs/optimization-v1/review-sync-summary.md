# Evidence Review Sync Summary

status: active_full_audit

Last updated: 2026-06-16 12:48 Asia/Shanghai

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

## Full Audit Continuation

Yao selected A1+B1+C1 for the next stage:

- phased full audit across the prototype library,
- queue-before-edit, with no `prototypes_db/*.json` edits before approval,
- evidence-graded boundaries: `hard_do_not`, `soft_boundary`, `knowledge_gap`.

## Full Audit Outputs

- `docs/optimization-v1/review-full-audit-plan.md`
- `docs/optimization-v1/review-full-audit-worklog.md`
- `docs/optimization-v1/review-full-audit-decision-queue.md`
- `docs/optimization-v1/review-boundary-do-not-register.md`
- Batch 01 files for `chitosan`, `polydopamine-coating`, `plant-tannin`, `silk-fibroin`, `wood-xylem`
- Batch 02 files for `biomineralization-template`, `bone-structure`, `oyster-shell`, `scallop-shell`, plus `fish-scale-hydroxyapatite` preflight

## Latest Checkpoint

Batch 02 mineral/shell audit is queued for Yao decision. No prototype JSON files were edited and `tools/build_prototypes_db.py` was not run.

| prototype_id | latest result |
|---|---|
| biomineralization-template | Wang2025 supports real LanM@ZIF-8 Nd3+ adsorption, but provenance/source metadata and missing performance_data need approval. |
| bone-structure | Bambaeero/Jaffar HAp evidence is usable with metadata fixes; Chen2021 MOF/Cr(VI) rows are wrong-source. |
| oyster-shell | Qiu/Li/Xu phosphate evidence is supported; Wang2021 abalone HA and generic shell/soil reviews need narrowing or reassignment. |
| scallop-shell | Wang2024 scallop Congo Red evidence is strong; existing performance rows are mostly generic shell reviews. |
| fish-scale-hydroxyapatite | Preflight found large membrane/superwetting wrong-source contamination; CN114849640A is the strongest fish-scale HAp source, while CN113275374A needs OCR. |
