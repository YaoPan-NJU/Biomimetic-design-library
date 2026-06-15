# Evidence Review Sync Summary

status: decision_queue_ready

Last updated: 2026-06-16 07:57 Asia/Shanghai

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
