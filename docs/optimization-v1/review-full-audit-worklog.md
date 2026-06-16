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
| 2026-06-16 13:06 CST | Codex | full-audit-03-microbes-cells | codex_preflight_reviewed | Added Batch 03 preflight for chlorella-cell-wall, iron-oxidizing-bacteria, sulfate-reducing-bacteria, mycelium, and cell-membrane-ion-channel. Queued supported metadata fixes, wrong-source removals/reassignments, scope decisions, and DO-NOT/boundary candidates. No prototypes_db files modified. |
| 2026-06-16 13:21 CST | Codex | full-audit-04-separation-surfaces | codex_preflight_reviewed | Added Batch 04 preflight for lotus-leaf, shark-skin, water-strider-leg, cactus-spine, and superhydrophobic-artificial under prototypes_db/separation. Queued scope-split decisions, missing-PDF checks, patent-backed artificial superhydrophobic evidence, and DO-NOT/boundary candidates. No prototypes_db files modified. |
| 2026-06-16 13:45 CST | Codex | full-audit-05-selective-materials | codex_preflight_reviewed | Added Batch 05 preflight for dna-aptamer, diatom-frustule, mangrove-root, and materials_reference alginate/cellulose-nanocrystal/metal-organic-framework/starch-granule. Queued sparse-DNA, diatom path/dedup, mangrove system-scope, material-reference split, MOF verification-semantics, and starch sanity-check decisions. No prototypes_db files modified. |
| 2026-06-16 13:51 CST | Codex | full-audit-06-enrichment-crosscheck | codex_preflight_reviewed | Added Batch 06 enrichment mirror crosscheck. Found 525/525 enrichment causal chains blank, four empty enrichment mirrors, schema mismatch between enrichment object maps and main JSON arrays, and several mechanism-count mismatches. No prototypes_db files modified. |
| 2026-06-16 | Yao + Codex | review-openclaw-coordination.md | role_split_updated | Yao decided OpenClaw should own bulk evidence work. Codex role narrowed to key decisions, stage acceptance, spot-checking, queue curation, boundary register, worklog/sync summary, and GitHub checkpoints. |
| 2026-06-16 13:56 CST | Codex | review-openclaw-next-tasks.md | openclaw_tasks_prepared | Prepared next OpenClaw worker tasks for Batch 07 parked/registry consistency and targeted sub-batches for DNA aptamer, diatom path/dedup, MOF verification semantics, and starch extreme-value sanity checks. |
| 2026-06-16 14:12 CST | Codex | review-openclaw-worker-prompts.md | openclaw_prompts_prepared | Prepared copy-paste OpenClaw worker prompts for Batch 07 and targeted DNA aptamer, diatom, MOF, and starch sub-batches. No prototypes_db files modified. |

## Batch 06 Codex Checkpoint - 2026-06-16

Current state:

- `review-full-audit-batch-06-enrichment-crosscheck-preflight.md` covers all 24 enrichment mirror files.
- No `prototypes_db/*.json` files were modified.
- No build script was run.
- All Batch 06 JSON-change candidates were queued as `pending_yao`.

Key findings:

- Enrichment `mechanisms` are object maps keyed by mechanism names, while main JSON `mechanisms` are arrays. This is a schema mismatch that needs explicit handling before automated sync.
- 525/525 enrichment mechanism entries have empty or placeholder causal-chain fields.
- `biomineralization-template`, `coral-skeleton`, `dna-aptamer`, and `magnetic-bacteria` enrichment files are empty `{}` despite main JSON mechanisms.
- `diatom-frustule`, `pitcher-plant-slippery-surface`, `plant-tannin`, and `silk-fibroin` enrichment mirrors have fewer mechanisms than their main JSONs.
- Enrichment entries should not be treated as source-backed evidence until they are populated from approved main JSON rows with locators and quotes.

Next execution strategy:

- Wait for Yao approval before changing prototype or enrichment JSON.
- Do not mechanically synchronize enrichment mirrors before wrong-source cleanup decisions are resolved.
- If continuing before approval, move to Batch 07 parked/registry consistency or continue source-path normalization reports only.

## Batch 05 Codex Checkpoint - 2026-06-16

Current state:

- `review-full-audit-batch-05-selective-materials-preflight.md` covers three ordinary prototypes and four large material-reference JSONs.
- No `prototypes_db/*.json` files were modified.
- No build script was run.
- All Batch 05 JSON-change candidates were queued as `pending_yao`.

Key findings:

- `dna-aptamer` is underbuilt: zero performance rows, one mechanism, zero provenance, and an empty enrichment mirror despite many local aptamer PDFs/extractions.
- `diatom-frustule` has local PDFs for major source groups, but source paths are often bare filenames or suffix-mismatched, and duplicated row groups should be cleaned before quote insertion.
- `mangrove-root` is system-level constructed-wetland evidence, so NH4+-N/PO4 removal percentages must not be compared with material qmax values.
- `materials_reference` files are reference stores, not ordinary prototypes. They need material/source-family sub-batching before direct ranking use.
- `metal-organic-framework` has a verification-semantics problem: `n_verified=252` is mostly `verification=single_source`, not quote+locator verification under the full audit protocol.
- `starch-granule` has high false-ranking risk from extreme or mixed-unit review-table values, including dye capacity ranges and oil/pharmaceutical maxima.

Next execution strategy:

- Wait for Yao approval before changing prototype JSON.
- If continuing audit before approval, move to Batch 06 enrichment crosscheck only after noting that Batch 04/05 commits are still blocked by Git write escalation quota.
- If cleanup is approved, start with `dna-aptamer` targeted evidence build, `diatom-frustule` path/dedup cleanup, and MOF verification-semantics correction.

## Batch 04 Codex Checkpoint - 2026-06-16

Current state:

- `review-full-audit-batch-04-separation-surfaces-preflight.md` covers five separation/superwetting prototypes under `prototypes_db/separation/`.
- No `prototypes_db/*.json` files were modified.
- No build script was run.
- All Batch 04 JSON-change candidates were queued as `pending_yao`.

Key findings:

- `lotus-leaf` is an overaggregated special-wettability/oil-water-separation store, with 4 performance rows, 355 mechanisms, 22 constraints, 33 narrative entries, and zero verified provenance. It should be split before row-level quote insertion.
- `shark-skin`, `water-strider-leg`, and `cactus-spine` have zero performance rows and mostly generic review/background mechanisms.
- `superhydrophobic-artificial` has the strongest direct evidence in this batch: CN113244892B supports organic-liquid adsorption capacities of 132-233 g/g for superhydrophobic/oleophilic biochar foam, while CN121130847A supports MOF-modified bio-based foam adsorption of 51.5-122 g/g with a wettability-classification caveat.
- CN114874407A supports an artificial TiO2/fluorosilane superhydrophobic sponge, not direct lotus-leaf biological performance.

Next execution strategy:

- Wait for Yao approval before changing prototype JSON.
- If continuing audit before approval, start the next batch with the same local text-first workflow.
- If cleanup is approved, prioritize splitting `lotus-leaf` and adding locators/quotes to the artificial superhydrophobic patent evidence.

## Batch 03 Codex Checkpoint - 2026-06-16

Current state:

- `review-full-audit-batch-03-microbes-cells-preflight.md` covers all five Batch 03 prototypes.
- No `prototypes_db/*.json` files were modified.
- No build script was run.
- All Batch 03 JSON-change candidates were queued as `pending_yao`.

Key findings:

- `chlorella-cell-wall` has a strong Cheng2021 Pb microalgae source and Peng2022 Chlorella-derived magnetic biochar source, but dye-mechanism and unrelated wastewater-technology rows must be corrected or removed.
- `iron-oxidizing-bacteria` has strong Luo2021/Jhariya2024 Fe-mineral evidence, but CN113275374A scanned patent/MICP rows need OCR and reassignment decisions.
- `sulfate-reducing-bacteria` has a supported SRB sulfide-precipitation mechanism but zero verified performance rows; iron-cycle constraints are wrong-source.
- `mycelium` should keep Liu2021 fungal biosorption evidence with better locators, while Zhang2022 cellulose/nanocellulose rows need removal or reassignment.
- `cell-membrane-ion-channel` is mainly a separation/filtration prototype; membrane metric rows must not be mixed with adsorption qmax without a scope decision.

Next execution strategy:

- Wait for Yao approval before changing prototype JSON.
- Continue Batch 04 separation/superwetting surfaces if auditing continues before JSON cleanup.
- If cleaning approved items first, prioritize Batch 03 hard wrong-source groups: Chlorella Technology rows, SRB iron-cycle constraints, mycelium Zhang2022 rows, and cell-membrane metric normalization.

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
