# Evidence Review Sync Summary

status: active_full_audit

Last updated: 2026-06-17 06:03 Asia/Shanghai

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

## Package A1 Cleanup Checkpoint

Yao approved only low-risk mechanical cleanup. The first applied batch changed `prototypes_db` in a limited scope:

- normalized source paths and removed exact duplicate rows in `prototypes_db/diatom-frustule.json`;
- filled direct-source pollutant fields in `plant-tannin`, `wood-xylem`, `bone-structure`, and `oyster-shell`;
- normalized confirmed ` 2.pdf` source-file suffixes for wood, bone, and oyster rows.

This checkpoint did not upgrade verification status, did not apply hard/soft boundary changes, did not remove wrong-source rows, and did not run `tools/build_prototypes_db.py`.

## Package A2 Cleanup Checkpoint

The second applied Package A batch continued only low-risk metadata cleanup:

- `oyster-shell`: filled the remaining Li2017 phosphate/phosphorus pollutant field and normalized Li2017/Xu2022 source paths to the actual local PDF files.
- `iron-oxidizing-bacteria`: filled Luo2021 As(III)/As(V) pollutant fields for `performance_data[0-6]` and normalized the Luo2021 source path to the C2 local PDF.

This checkpoint still did not upgrade verification status, did not narrow mechanisms, did not apply hard/soft boundaries, did not remove wrong-source rows, and did not run `tools/build_prototypes_db.py`.

## Package A3 Cleanup Checkpoint

The third applied Package A batch continued only low-risk metadata cleanup:

- `silk-fibroin`: normalized confirmed local source paths for Supriya, Adil, Bruder, Martis, Xing, and the second Martis extraction family.
- `silk-fibroin`: filled three direct pollutant fields for Cu/Cr and MB rows where the audit already identified the pollutants.

This checkpoint skipped false-precision value narrowing, same-DOI deduplication, quote replacement, mechanism changes, and any verification upgrades.

## Package A4 Cleanup Checkpoint

The fourth applied Package A batch continued path-only cleanup:

- `iron-oxidizing-bacteria`: normalized Xu2022 and Jhariya2024 performance-row source paths to the confirmed C2 local PDFs.

This checkpoint did not add new mechanism/constraint source fields, did not demote Qian2021 background rows, did not change verification status, and did not run `tools/build_prototypes_db.py`.

## Package A5 Cleanup Checkpoint

The fifth applied Package A batch made one path-only cleanup:

- `superhydrophobic-artificial`: normalized the CN121130847A performance-row source path to the confirmed patent PDF under `仿生文献库/专利/`.

This checkpoint did not change WCA classification, pollutant fields, constraints, verification status, or run `tools/build_prototypes_db.py`.

## Package A6 Cleanup Checkpoint

The sixth applied Package A batch made one path-only cleanup:

- `fish-scale-hydroxyapatite`: normalized CN114849640A acid-fuchsin performance rows `performance_data[7-17]` to the confirmed patent PDF under `仿生文献库/专利/`.

This checkpoint deliberately did not deduplicate repeated 478 mg/g rows, add patent paragraph locators, change verification status, apply boundary decisions, or run `tools/build_prototypes_db.py`.

## Fish-Scale OpenClaw Acceptance Checkpoint

OpenClaw produced `review-full-audit-openclaw-fish-scale-cleanup.md`, and Codex accepted only decision-ready findings after spot-checking local extraction quotes.

Key accepted findings:

- CN114849640A is the core fish-scale extracted HAp acid-fuchsin source; repeated 478 mg/g rows are semantic duplicates from the same 实施例1, not independent replication.
- Dou2021 supports fish-scale-derived porous biochar/CIP, not fish-scale HAp as final adsorbent.
- Wu2022 supports rice-husk HAp-biochar, not fish-scale material.
- CN113275374A supports MICP/mixed-bacteria biomineralization and should not be used as fish-scale HAp evidence without reassignment.
- Wang2021 and Zhang2024 are shell/abalone/generic shell-powder sources, not fish-scale HAp.
- The large superwetting/membrane mechanism and constraint ranges remain wrong-source candidates requiring Yao approval before removal.

## PDA/Mussel OpenClaw Acceptance Checkpoint

OpenClaw produced `review-full-audit-openclaw-pda-mussel-overlap.md`, and Codex accepted decision-ready findings after spot-checking duplicate structure and representative extraction quotes.

Key accepted findings:

- `polydopamine-coating` and `mussel-foot-adhesion` share 32 exact duplicate performance rows.
- The duplicate rows are PDA-coated adsorbent/composite evidence. They should not be counted twice in ranking/provenance; final ownership requires Yao scope approval.
- PDA-side path normalization and pollutant fills are viable Package A candidates; mussel-side metadata changes should wait for ownership decisions.
- Yuan2024 is a tannic-acid/cellulose/PEI composite with PDA-modified montmorillonite, so its extreme qmax values need a material-class caveat or reassignment.
- Enrichment causal chains are empty evidence shells and include wrong-source hydrophobic/superhydrophobic membrane mirrors.

## Package A7 Cleanup Checkpoint

The seventh applied Package A batch made PDA-side metadata-only changes:

- `polydopamine-coating`: normalized performance-row `source_file` values to confirmed local PDF paths for CN115055171A, Shi2021, Yan2022, Xiao2021, Zhang2021, Godiya2022, Yuan2024, Foroutan2021, Xiang2023, and Jin2023 source families.
- `polydopamine-coating`: filled six empty pollutant fields for Yan2022 MB/MG/CV and Xiao2021 Fe/Co/Ni rows.

This checkpoint deliberately did not edit `mussel-foot-adhesion`, because its overlapping PDA-derived rows require Yao ownership/scope approval. It did not change verification status, apply boundaries, remove wrong-source rows, or run `tools/build_prototypes_db.py`.

The eighth applied Package A batch accepted the targeted PDA/mussel patent OCR audit:

- `polydopamine-coating`: normalized CN113244898A rows [17-19] and CN114570339A rows [26-32] from bare filenames to confirmed local `仿生文献库/3rd/第三波-仿生吸附专利/` PDF paths.
- `mussel-foot-adhesion`: normalized Tang2023 row [0] to the confirmed ` 2.pdf` local PDF path.
- Decision queue now records that the prior `missing_pdf` concern is mostly resolved, but CN114570339A figure-estimated values and CN113244898A Pb percentage discrepancy remain approval-gated.

This checkpoint did not edit duplicated mussel CN114570339A rows, because their PDA/mussel ownership is still unresolved. It did not change verification status, apply boundaries, remove wrong-source rows, correct disputed values, or run `tools/build_prototypes_db.py`.

The ninth applied Package A batch accepted Batch 08 remaining-core preflight:

- `pitcher-plant-slippery-surface`: normalized performance_data[0] source_file to the confirmed local Zeng2021 ` 2.pdf` path.
- `spider-silk`: normalized the four Zhou2021 performance source_file values to the confirmed local ` 2.pdf` path; Codex verified the ` 2.pdf` and ` 3.pdf` copies have identical SHA-1 hashes.
- `coral-skeleton` and `magnetic-bacteria` remain zero-performance knowledge gaps.
- `lobster-exoskeleton` Vo path normalization was not applied because the proposed `2023-Vo... 2.pdf` PDF was not found locally.
- Enrichment mirroring candidates were not applied because enrichment sync remains blocked until wrong-source/scope cleanup decisions are approved.

This checkpoint did not change verification status, apply boundaries, remove wrong-source rows, recompute provenance, correct values, or run `tools/build_prototypes_db.py`.

Approval is still needed before:

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

OpenClaw Batch 07 parked/registry consistency and the targeted MOF verification-semantics audit are complete and accepted into the decision queue after Codex spot-checking. No prototype JSON files were edited and `tools/build_prototypes_db.py` was not run.

| area | latest result |
|---|---|
| execution model | OpenClaw owns bulk evidence verification; Codex owns stage acceptance, spot checks, queue curation, boundaries, and GitHub checkpoints. |
| Batch 07 parked/registry | `namib-beetle` remains a no-performance, duplicated-scope parked item. It should not be promoted without dedicated Namib beetle source evidence. |
| Batch 07 source mapping | `2022-Progress-review` extraction/PDF variants and `missing_26_pdf_dir` vs ` 2.pdf`/` 3.pdf` variants need provenance resolution before automated path normalization. |
| MOF semantics | `verification=single_source` is a source-presence/review-summary signal, not quote+locator verification; `n_verified=252` should not be treated as fully verified. |
| MOF wrong-source rows | Aramesh chitosan rows, Cheng membrane/BPA rows, and Yan polydopamine rows are queued for removal/reassignment decisions. |
| MOF scope boundary | MOF-5 H2 storage is valid MOF material-property evidence but should be excluded from water-treatment adsorption ranking unless the database keeps gas-storage properties separately. |
| DNA aptamer | Targeted evidence build accepted: 9/11 sources are biosensor-only; Bilibana2022 RNA-GO and CN121588773A DNA-GC are the only adsorption/capture evidence sources. |
| diatom path/dedup | Targeted cleanup accepted: 7 source path families need normalization, 22 exact duplicate rows should be removed after approval, and one Pb XPS mechanism cites the wrong DOI/source. |
| starch extreme values | Targeted sanity check accepted: CV 24,375 mg/g is concentration-derived, Khoo2023 abstract maxima are cross-material review summaries, and oil/aerogel values should not drive starch-granule aqueous ranking. |
| next OpenClaw tasks | No currently running OpenClaw worker. Prepare next-stage decision summary and await Yao approval for queued cleanup categories, or start another targeted source family if requested. |

## Starch Extreme-Value OpenClaw Acceptance - 2026-06-16

File accepted:

- `docs/optimization-v1/review-full-audit-openclaw-starch-extreme-values.md`

Codex spot checks:

- Confirmed `prototypes_db/materials_reference/starch-granule.json` has 121 performance rows and zero verified provenance in its summary.
- Confirmed high-risk JSON rows: Pb2+ 2000 mg/g, mmol/g rows, Ihsanullah concentration-dependent dye rows, Khoo review maxima, oil/chloroform sorbent rows, missing-source row 77, and Chen2021 STAH20 2967.66 mg/g.
- Confirmed Ihsanullah2022 PDF text supports CV uptake increasing from 4999 to 24,375 mg/g and MB uptake increasing from 1455.76 to 1918.81 mg/g with initial concentration changes, so these are not generic qmax values.
- Confirmed Khoo2023 abstract text lists review-wide maxima of 13,000, 66, 2000, 25,000, and 782 mg/g across pollutant classes, not starch-granule-specific performance.
- Confirmed Khoo2023 Table 3 contains rice straw-cationic starch aerogel oil adsorption at 13,000 mg/g, which is an oil/superhydrophobic sorbent class.

Accepted queue impact:

- Added F10 starch decision items to `review-full-audit-decision-queue.md`.
- Added B10 starch DO-NOT/boundary candidates to `review-boundary-do-not-register.md`.
- No database JSON edits were made.

## Diatom Path/Dedup OpenClaw Acceptance - 2026-06-16

File accepted:

- `docs/optimization-v1/review-full-audit-openclaw-diatom-path-dedup.md`

Codex spot checks:

- Confirmed `prototypes_db/diatom-frustule.json` currently has 42 performance rows, 15 mechanisms, 16 engineering constraints, and 13 narrative entries.
- Confirmed performance duplicates in Qin2024, Guo2022, Abou-Elanwar2025, and Sriram2022 groups.
- Confirmed duplicate mechanism, engineering-constraint, and narrative entries by row content and paper IDs.
- Confirmed local PDFs exist for the Du2021 ` 2.pdf` path and Sriram2022 C1-folder path.
- Confirmed `mechanisms[0]` cites Guo2022 DOI/source while the row text is Pb2+/MPTS/XPS evidence that belongs to Du2021.
- Confirmed `mechanisms[1]` and `mechanisms[3]` use microalgae cell-wall template text even though the rows are diatomite mineral-surface chemistry.
- Confirmed duplicated Arachnoidiscus narrative entries are wheel-hub structural-mechanics biomimicry, not adsorption evidence.

Accepted queue impact:

- Added F09 diatom path/dedup decision items to `review-full-audit-decision-queue.md`.
- Added B09 diatom DO-NOT/boundary candidates to `review-boundary-do-not-register.md`.
- No database JSON edits were made.

## DNA Aptamer OpenClaw Acceptance - 2026-06-16

File accepted:

- `docs/optimization-v1/review-full-audit-openclaw-dna-aptamer-evidence-build.md`

Codex spot checks:

- Confirmed `prototypes_db/dna-aptamer.json` has zero `performance_data`, one mechanism, and `provenance_summary` counts at zero; enrichment mirror is `{}`.
- Confirmed current mechanism has contradictory metadata: `source: llm_inference` with `verification: verified`, while boundary conditions remain llm-inferred placeholders.
- Confirmed Bilibana2022 text supports RNA-GO MC-LR adsorption qmax 1.44 mg/g, removal >95%, large surface area, and five-cycle regeneration with about 10% efficiency loss.
- Confirmed CN121588773A visual cache/text supports DNA-GC AFB1 Kd 0.25 nM and qualitative largest adsorption capacity. Visual figure cache suggests an approximate adsorption capacity around 35 mg/g, but this remains figure-derived and needs human approval before use as a numeric qmax.
- Confirmed the rest of the aptamer literature pool is mainly biosensor/detection/mechanism evidence and must not be converted into adsorption performance rows.

Accepted queue impact:

- Added F08 DNA decision items to `review-full-audit-decision-queue.md`.
- Added B08 DNA DO-NOT/boundary candidates to `review-boundary-do-not-register.md`.
- No database JSON edits were made.

## Batch 07 / MOF OpenClaw Acceptance - 2026-06-16

Files accepted:

- `docs/optimization-v1/review-full-audit-openclaw-batch-07-parked-registry.md`
- `docs/optimization-v1/review-full-audit-openclaw-mof-verification-semantics.md`

Codex spot checks:

- Confirmed `prototypes_db/parked/namib-beetle.json` has zero `performance_data`, 16 mechanisms, 4 engineering constraints, and 2 narrative entries.
- Confirmed MOF `performance_data[23-36]` are Aramesh2021 chitosan-source rows; `performance_data[31-32]` are MOF-containing hybrids needing a human decision, while the other Aramesh rows are wrong-source for MOF.
- Confirmed MOF `performance_data[77-80]` are activated-carbon/NF/MF/UF-AOP BPA rows with empty material fields from Cheng2024 membrane review.
- Confirmed MOF `performance_data[88]` is H2 storage at 78 K, not water-treatment adsorption.
- Confirmed MOF `performance_data[252-253]` are PDA/MGO/CA-CD polydopamine composite rows from Yan2022.

Accepted queue impact:

- Added F07 registry and MOF decision items to `review-full-audit-decision-queue.md`.
- Added B07 knowledge-gap, soft-boundary, and hard-DO-NOT candidates to `review-boundary-do-not-register.md`.
- No database JSON edits were made.

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
