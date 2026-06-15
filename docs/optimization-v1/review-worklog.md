# Evidence Review Worklog

status: active_coordination

## Protocol

- Local AI writes batch files and records progress here.
- Codex reads completed batches, checks evidence quality, and writes decisions to `review-decision-queue.md`.
- Do not modify `prototypes_db/*.json` until Yao approves a queued decision.
- Do not run `tools/build_prototypes_db.py`.

## Entries

| time | actor | file | status | notes |
|---|---|---|---|---|
| 2026-06-15 23:35 | Codex | docs/optimization-v1/evidence-review-report.md | reviewed_initial | Use as candidate index only; PDF paths require spot-checking. |
| 2026-06-16 00:10 | OpenClaw/mimo-v2.5 | docs/optimization-v1/review-batch-pitcher-plant.md | ready_for_codex_review | 5 claims checked (4 upgrade_candidate, 1 wrong_source). 0 unresolved issues. All quotes verbatim from Zeng2021 PDF. |
| 2026-06-16 00:07 | Codex | docs/optimization-v1/review-batch-pitcher-plant.md | codex_spot_checked | Spot-checked Zeng2021 quotes against PDF text layer and queued 5 items in review-decision-queue.md; no prototypes_db edits. |
| 2026-06-16 00:07 | OpenClaw/mimo-v2.5 | docs/optimization-v1/review-batch-pitcher-plant.md | ready_for_codex_review | Rewrite v2: corrected source_pdf_path to workspace copy, added original library path in notes. 5 claims checked (4 upgrade_candidate, 1 wrong_source). 0 unresolved issues. All quotes verbatim from Zeng2021 PDF text layer. |
| 2026-06-16 01:15 | OpenClaw/mimo-v2.5 | docs/optimization-v1/review-batch-spider-silk.md | ready_for_codex_review | 8 claims checked (8 upgrade_candidate). 1 unresolved: mech-2 "elastic" component not supported by Zhang2021; may need Li2021 for elasticity evidence. All quotes verbatim from Zhou2021/Zhang2021 PDFs. XPS values extracted via multimodal. |
| 2026-06-16 00:10 | Codex | docs/optimization-v1/review-batch-spider-silk.md | codex_spot_checked | Spot-checked Zhang2021/Zhou2021 text-layer quotes; queued 8 items in review-decision-queue.md with mech-2 caveat and XPS figure-reading caveat; no prototypes_db edits. |
| 2026-06-16 01:30 | OpenClaw/mimo-v2.5 | docs/optimization-v1/review-batch-spider-silk.md | ready_for_codex_review | Rewrite v3: corrected source_pdf_path to workspace copies, added original library paths in notes. 8 claims checked (7 upgrade_candidate, 1 needs_human_decision). mech-2 flagged: Zhang2021 supports superhydrophilic membrane antifouling but NOT spider silk protein elasticity+hydrophilic biological antifouling; Li2021 covers elasticity but not antifouling. All other quotes verbatim from Zhou2021/Zhang2021 PDF text layers. |
| 2026-06-16 02:00 | OpenClaw/mimo-v2.5 | docs/optimization-v1/review-batch-coral-skeleton.md | ready_for_codex_review | 2 claims checked (1 missing_pdf, 1 wrong_source). mech-1: no source PDF; 100% LLM-inferred, needs C-class download. narr-1: 2020-Han-antifouling-review is antifouling coatings topic, NOT coral CaCO3 adsorption — wrong_source. PDF search: 0 coral/coralline/CaCO3/aragonite PDFs in library. |
| 2026-06-16 02:10 | OpenClaw/mimo-v2.5 | docs/optimization-v1/review-batch-magnetic-bacteria.md | ready_for_codex_review | 9 claims checked (all keep_soft). PDF is Goswami2022 review — MTB background only, no engineered adsorbent data. mech-1: magnetosome chain + magnetic separation supported but organismal, not functionalized adsorbent. Performance claims (Cd/Co/Se/Te) are culture-based organismal results. No upgrade_candidate; C-class experimental paper needed for mech-1 upgrade. |
| 2026-06-16 07:45 | OpenClaw/mimo-v2.5 | docs/optimization-v1/review-batch-lobster-exoskeleton.md | ready_for_codex_review | 3 claims checked (2 missing_pdf, 1 wrong_source). Vo2023 PDF not in library (第1组-配位螯合 dir missing). 2024-Vo-wastewater-review 2.pdf is microalgae paper, not chitosan beads. mech-1 DOI 10.1016/j.polymer.2020.123316 is Lei2021 (mussel-chitosan aerogel), wrong source for chitosan beads mechanisms. Extraction JSON exists but all unverified; treat as extraction-only evidence. |
| 2026-06-16 07:57 | Codex | docs/optimization-v1/review-batch-lobster-exoskeleton.md | codex_spot_checked | Confirmed missing Vo2023 PDF and wrong DOI/source for lobster mechanism; queued 2 decision items; no prototypes_db edits. |
| 2026-06-16 07:57 | Codex | docs/optimization-v1/review-batch-magnetic-bacteria.md | codex_spot_checked | Spot-checked Goswami2022 text-layer quotes; queued keep_soft decisions for MTB mechanism/narrative; no verified upgrade proposed. |
| 2026-06-16 07:57 | Codex | docs/optimization-v1/review-batch-coral-skeleton.md | codex_spot_checked | Confirmed coral adsorption source missing and Han2020 antifouling review wrong_source; queued 2 decision items; no prototypes_db edits. |
