# Full Evidence Audit Worklog

status: active

## Entries

| time | actor | file | status | notes |
|---|---|---|---|---|
| 2026-06-16 | Yao | full audit policy | selected | Selected A1+B1+C1: phased full audit, queue-before-edit, evidence-graded DO-NOT/boundary handling. |
| 2026-06-16 | Codex | review-full-audit-plan.md | initialized | Created full-audit protocol, field coverage, evidence labels, boundary labels, and batch plan. |
| 2026-06-16 12:30 CST | OpenClaw workers | full-audit-01-biopolymers | partial_batch_ready | Four batch files produced: chitosan, polydopamine-coating, plant-tannin, silk-fibroin. wood-xylem did not produce a batch. Logs showed 429 rate limits, PDF allowed-path failures, >10MB PDF limits, and session takeover errors. |
| 2026-06-16 12:45 CST | Codex | review-full-audit-decision-queue.md | batch01_queued | Added decision-ready queue items from the four ready Batch 01 files. No prototypes_db files modified. |

| 2026-06-16 12:46 CST | Codex | review-boundary-do-not-register.md | batch01_boundaries | Added evidence-graded DO-NOT, soft_boundary, and knowledge_gap candidates. Missing/scanned PDFs are treated as knowledge gaps, not hard DO-NOT. |

| 2026-06-16 13:15 CST | Codex | review-full-audit-batch-01-wood-xylem.md | codex_reviewed | Completed local PDF text audit for wood-xylem after OpenClaw failure; all three performance values supported, one mechanism source/quote mismatch queued, enrichment placeholders queued. |
| 2026-06-16 12:48 CST | Codex | full-audit-02-minerals-shells | codex_reviewed_checkpoint | Added Batch 02 audit docs for biomineralization-template, bone-structure, oyster-shell, scallop-shell, and fish-scale-hydroxyapatite preflight. Updated full-audit decision queue and boundary register. No prototypes_db files modified. |

## Batch 02 Codex Checkpoint - 2026-06-16

Current state:

- `biomineralization-template`, `bone-structure`, `oyster-shell`, and `scallop-shell` have Codex-reviewed Batch 02 audit files.
- `fish-scale-hydroxyapatite` has a preflight audit file because the prototype contains 29 performance rows, 89 mechanisms, 12 engineering constraints, and a large wrong-source membrane/superwetting block.
- No `prototypes_db/*.json` files were modified.
- No build script was run.
- All Batch 02 JSON-change candidates were queued as `pending_yao`.

Key findings:

- `fish-scale-hydroxyapatite` has the highest cleanup priority in this batch: special-wettability/membrane mechanisms and constraints should be removed or reassigned before detailed HAp quote insertion.
- `bone-structure` contains a clear MOF/Cr(VI) wrong-source row that should not remain as bone/HAp evidence.
- `oyster-shell` and `scallop-shell` both contain generic shell-review and soil-passivation evidence that should be kept soft or split to shell-general evidence.
- Strong supported evidence exists but needs metadata normalization: Wang2025 LanM@ZIF-8, Bambaeero2020, Jaffar2024, Qiu2021, Li2017, Xu2022, Wang2024 scallop shell, and CN114849640A.

Next execution strategy:

- Wait for Yao approval before changing prototype JSON.
- If continuing audit before approval, start Batch 03 with low-concurrency/local text-first workflow.
- If cleaning Batch 02 after approval, begin with `fish-scale-hydroxyapatite` source-block removal/reassignment, then add missing quote/locator metadata to supported mineral/shell fields.

## Batch 01 Codex Checkpoint - 2026-06-16

Current state:

- Raw extraction/audit output exists for `chitosan`, `polydopamine-coating`, `plant-tannin`, and `silk-fibroin`.
- `wood-xylem` failed to produce a batch and must be rerun.
- No `prototypes_db/*.json` files were modified.
- No build script was run.
- Main execution issue: first batch used too much concurrent OpenClaw/API capacity and hit `429 Too many requests`; several PDFs also failed because of allowed-path and >10 MB limits.

Codex review stance:

- Queue only decision-ready issues with concrete field targets.
- Treat missing PDFs, scanned patents, and figure-estimated values as `knowledge_gap` or `needs_human_decision`, not hard DO-NOT.
- Treat clear wrong-source contamination as high-priority removal/demotion candidates, subject to Yao approval.

Next execution strategy:

- Rerun `wood-xylem` as a single low-concurrency `mimo-v2.5` worker.
- For future batches, use one or two concurrent workers, not five.
- Pre-normalize PDF paths and use text/OCR extraction for large or scanned PDFs before asking the AI worker to verify claims.
