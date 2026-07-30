---
title: Phase 0 Documentation Archive Manifest (DRY-RUN, NOT EXECUTED)
status: dryrun_pending_authorization
date: 2026-06-19
canonical_source: docs/active/phase0-dispositions.json (validator reads this)
scope: documentation only. NO git mv executed. NO canon edit. NO commit.
---

# Phase 0 Archive Manifest — DRY-RUN (machine-validated)

This Markdown is rendered from `docs/active/phase0-dispositions.json` (single source).
The read-only validator confirmed: 268 tracked docs files each have exactly one
disposition; +1 `create` row for `docs/README.md`. No duplicates, no missing sources,
no target collisions, no targets outside `docs/`, no forbidden paths, no ellipsis or
wildcard or directory-summary rows.

**Status: NOT EXECUTED.** No `git mv`, no canon edit, no commit, no openclaw dispatch.

## Summary
- disposition rows: **269**  (tracked docs files: 268, +1 create)
- git_mv: **176**  |  no_action: **83**  |  keep_at_root: **8**  |  create: **1**  |  update_ref: **1**
- directive_3: `docs/imported/library-enhancement/**` all no_action (runtime assets; tools/biomimetic_context.py NOT modified).
- directive_4: `docs/archive/**` all no_action (already archived; no re-shuffle churn).
- directive_5: NO empty operational docs created in Phase 0 (deferred to later commits).
- directive_6: `docs/active/CLAUDE-CODE-TAKEOVER.md` path fix = update_ref (Yao-authorized).

## Reference updates (action: update_ref)
| target | change |
|---|---|
| `README.md` | update docs/imported/library-enhancement path references (unchanged location; verify links); ADRMATS_* stay; add registries/ references |
| `CLAUDE.md` | update paths for COLLAB-*, review-sync-summary, review-worklog, review-full-audit-worklog, review-openclaw-*, PLAN.md, DEFINITIONS.md, review-full-audit-decision-queue, review-boundary-do-not-register -> registries/ and references/ |
| `docs/active/CLAUDE-CODE-TAKEOVER.md` | Yao-authorized 2026-06-19: work in /Users/panyao/Desktop/Biomimetic-design-library on review; /private/tmp/biomimetic-recovery-docs worktree is OBSOLETE; preserve tools/litextract and _w1/_w2/_w3_doi_map.json |

## create  (1)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/README.md` | `docs/README.md` | design §11 entry point (Phase 0 create) | all | - | create |

## update_ref  (1)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/active/CLAUDE-CODE-TAKEOVER.md` | `docs/active/CLAUDE-CODE-TAKEOVER.md` | active operational doc; references obsolete /private/tmp worktree | recovery design, this manifest | - | update_ref |

## keep_at_root (referenced; stay at docs/ root)  (8)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/design.md` | `docs/design.md` | check_repo_hygiene.py mandatory docs/ root file | README.md, tools/create_clean_branch.sh, tools/check_repo_hygiene.py | - | keep_at_root |
| `docs/ADRMATS_CALL_GUIDE.md` | `docs/ADRMATS_CALL_GUIDE.md` | check_repo_hygiene.py mandatory docs/ root file | README.md, tools/check_repo_hygiene.py | - | keep_at_root |
| `docs/ADRMATS_DELIVERY_PLAN.md` | `docs/ADRMATS_DELIVERY_PLAN.md` | check_repo_hygiene.py mandatory docs/ root file | README.md, tools/check_repo_hygiene.py | - | keep_at_root |
| `docs/ADRMATS_INTEGRATION.md` | `docs/ADRMATS_INTEGRATION.md` | check_repo_hygiene.py mandatory docs/ root file | tools/check_repo_hygiene.py | - | keep_at_root |
| `docs/REPOSITORY_HYGIENE.md` | `docs/REPOSITORY_HYGIENE.md` | check_repo_hygiene.py mandatory docs/ root file | README.md, tools/check_repo_hygiene.py | - | keep_at_root |
| `docs/SUPPORT_SCOPE_AND_RISKS.md` | `docs/SUPPORT_SCOPE_AND_RISKS.md` | check_repo_hygiene.py mandatory docs/ root file | README.md, tools/check_repo_hygiene.py | - | keep_at_root |
| `docs/DEFINITIONS.md` | `docs/DEFINITIONS.md` | root-level definitions, no non-docs refs | none outside docs | - | keep_at_root |
| `docs/adrmats-integration-analysis.md` | `docs/adrmats-integration-analysis.md` | referenced by README | README.md | - | keep_at_root |

## git_mv -> docs/archive/pre-optimization/  (17)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/phase1-completion-report.md` | `docs/archive/pre-optimization/phase1-completion-report.md` | superseded completion report, 0 non-docs refs | none | docs/archive/pre-optimization/FINAL-report.md (kept in archive) | git_mv |
| `docs/phase2-completion-report.md` | `docs/archive/pre-optimization/phase2-completion-report.md` | superseded completion report, 0 non-docs refs | none | FINAL-report.md | git_mv |
| `docs/phase3-completion-report.md` | `docs/archive/pre-optimization/phase3-completion-report.md` | superseded completion report, 0 non-docs refs | none | FINAL-report.md | git_mv |
| `docs/phase4-completion-report.md` | `docs/archive/pre-optimization/phase4-completion-report.md` | superseded completion report, 0 non-docs refs | none | FINAL-report.md | git_mv |
| `docs/phase5-completion-report.md` | `docs/archive/pre-optimization/phase5-completion-report.md` | superseded completion report, 0 non-docs refs | none | FINAL-report.md | git_mv |
| `docs/phase6-completion-report.md` | `docs/archive/pre-optimization/phase6-completion-report.md` | superseded completion report, 0 non-docs refs | none | FINAL-report.md | git_mv |
| `docs/phase7-completion-report.md` | `docs/archive/pre-optimization/phase7-completion-report.md` | superseded completion report, 0 non-docs refs | none | FINAL-report.md | git_mv |
| `docs/post-mortem-20260609.md` | `docs/archive/pre-optimization/post-mortem-20260609.md` | historical post-mortem, 0 non-docs refs | none | future commit-audit-root-cause.md (separate later commit) | git_mv |
| `docs/remediation-summary.md` | `docs/archive/pre-optimization/remediation-summary.md` | historical, 0 non-docs refs | none | - | git_mv |
| `docs/status-and-next-steps-20260614.md` | `docs/archive/pre-optimization/status-and-next-steps-20260614.md` | historical, 0 non-docs refs | none | - | git_mv |
| `docs/baseline-stats-2026-06-10.md` | `docs/archive/pre-optimization/baseline-stats-2026-06-10.md` | historical baseline, 0 non-docs refs | none | - | git_mv |
| `docs/enrichment-separation-task.md` | `docs/archive/pre-optimization/enrichment-separation-task.md` | historical task instruction, 0 non-docs refs | none | - | git_mv |
| `docs/fix-chimera-and-enrichment.md` | `docs/archive/pre-optimization/fix-chimera-and-enrichment.md` | historical fix doc, 0 non-docs refs | none | - | git_mv |
| `docs/fix-perf-key-and-enrichment-separation.md` | `docs/archive/pre-optimization/fix-perf-key-and-enrichment-separation.md` | historical fix doc, 0 non-docs refs | none | - | git_mv |
| `docs/superpowers/plans/2026-06-10-biomimetic-library-remediation.md` | `docs/archive/pre-optimization/superpowers-plans/2026-06-10-biomimetic-library-remediation.md` | historical remediation plan, 0 non-docs refs | none | future recovery-master-plan.md (separate later commit) | git_mv |
| `docs/superpowers/plans/2026-06-17-evidence-audit-final-acceptance.md` | `docs/archive/pre-optimization/superpowers-plans/2026-06-17-evidence-audit-final-acceptance.md` | historical acceptance plan, 0 non-docs refs | none | - | git_mv |
| `docs/optimization-v1/优化方案_仿生库策展与接地_v1.md` | `docs/archive/pre-optimization/优化方案_仿生库策展与接地_v1.md` | original curation plan (pre optimization-v1) | PLAN.md (moving to references/) | optimization-plan-v1.md | git_mv |

## git_mv -> docs/registries/  (4)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/optimization-v1/review-boundary-do-not-register.md` | `docs/registries/boundary-do-not-register.md` | active ledger (105 IDs) | CLAUDE.md | - | git_mv |
| `docs/optimization-v1/review-full-audit-decision-queue.md` | `docs/registries/decision-queue.md` | active ledger (148 items) | CLAUDE.md | - | git_mv |
| `docs/optimization-v1/review-decision-queue.md` | `docs/registries/decision-queue-legacy.md` | legacy decision queue | CLAUDE.md (historic) | decision-queue.md | git_mv |
| `docs/optimization-v1/refuted-log.md` | `docs/registries/refuted-log.md` | active must-not-resurrect ledger | none outside docs | - | git_mv |

## git_mv -> docs/references/  (4)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/optimization-v1/DEFINITIONS.md` | `docs/references/definitions.md` | judgment standard | CLAUDE.md | future evidence-quality-standard.md (separate later commit) | git_mv |
| `docs/optimization-v1/PLAN.md` | `docs/references/optimization-plan-v1.md` | original optimization plan | CLAUDE.md | future recovery-master-plan.md | git_mv |
| `docs/optimization-v1/review-full-audit-plan.md` | `docs/references/full-audit-plan.md` | audit methodology | none outside docs | - | git_mv |
| `docs/optimization-v1/review-next-stage-approval-summary.md` | `docs/references/next-stage-approval-summary.md` | approval summary | none outside docs | - | git_mv |

## git_mv -> archive/.../phase-reports/  (17)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/optimization-v1/phase0-baseline.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase0-baseline.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase0-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase0-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase1-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase1-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase2-moves.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase2-moves.md` | phase moves log | none | - | git_mv |
| `docs/optimization-v1/phase2-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase2-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase3-decontam.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase3-decontam.md` | decontam log | none | - | git_mv |
| `docs/optimization-v1/phase3-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase3-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase4-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase4-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase5-chains.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase5-chains.md` | chains log | none | - | git_mv |
| `docs/optimization-v1/phase5-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase5-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase6-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase6-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase7-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase7-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase7-translation.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase7-translation.md` | translation log | none | - | git_mv |
| `docs/optimization-v1/phase7.5-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase7.5-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/phase8-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/phase8-report.md` | phase report | none | - | git_mv |
| `docs/optimization-v1/FINAL-report.md` | `docs/archive/optimization-v1-2026-06/phase-reports/FINAL-report.md` | final phase report | none | - | git_mv |
| `docs/optimization-v1/coverage-gaps.md` | `docs/archive/optimization-v1-2026-06/phase-reports/coverage-gaps.md` | coverage gap log | none | - | git_mv |

## git_mv -> archive/.../task-history/  (37)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/optimization-v1/CLAUDE-CODE-TASK-64-68.md` | `docs/archive/optimization-v1-2026-06/task-history/CLAUDE-CODE-TASK-64-68.md` | task history | none | - | git_mv |
| `docs/optimization-v1/CLAUDE-CODE-TASK-69-73.md` | `docs/archive/optimization-v1-2026-06/task-history/CLAUDE-CODE-TASK-69-73.md` | task history | none | - | git_mv |
| `docs/optimization-v1/CLAUDE-CODE-WORKER-PROMPT.md` | `docs/archive/optimization-v1-2026-06/task-history/CLAUDE-CODE-WORKER-PROMPT.md` | worker prompt history | none | - | git_mv |
| `docs/optimization-v1/DISPATCH-briefing.md` | `docs/archive/optimization-v1-2026-06/task-history/DISPATCH-briefing.md` | dispatch history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task1-decision-queue-summary.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task1-decision-queue-summary.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task2-boundary-register-summary.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task2-boundary-register-summary.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task3-missing-pdf-analysis.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task3-missing-pdf-analysis.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task4-next-steps-roadmap.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task4-next-steps-roadmap.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task5-metadata-fixes.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task5-metadata-fixes.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task6-remaining-wrongsource.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task6-remaining-wrongsource.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task7-queue-status-update.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task7-queue-status-update.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task8-path-normalization.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task8-path-normalization.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task9-queue-batch-update.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task9-queue-batch-update.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task10-lotus-scope-assessment.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task10-lotus-scope-assessment.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task11-reconciliation.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task11-reconciliation.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task12-verification-batch1.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task12-verification-batch1.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task13-verification-batch2.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task13-verification-batch2.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task14-queue-full-update.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task14-queue-full-update.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task15-lotus-scope-split.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task15-lotus-scope-split.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task16-pda-ocr-fix.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task16-pda-ocr-fix.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task17-scope-caveats-metadata.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task17-scope-caveats-metadata.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task18-lotus-cleanup.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task18-lotus-cleanup.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task19-verification-batch3.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task19-verification-batch3.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task20-verification-batch4.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task20-verification-batch4.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task21-verification-batch5.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task21-verification-batch5.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task22-ocr-patents.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task22-ocr-patents.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task23-validation.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task23-validation.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task27-pending-yao-batch.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task27-pending-yao-batch.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task46-51.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task46-51.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task52-57.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task52-57.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-task58-63.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-task58-63.md` | clcode task history | none | - | git_mv |
| `docs/optimization-v1/review-clcode-infra-fix-and-verify.md` | `docs/archive/optimization-v1-2026-06/task-history/review-clcode-infra-fix-and-verify.md` | infra fix report history | none | - | git_mv |
| `docs/optimization-v1/review-continuous-openclaw-execution-plan.md` | `docs/archive/optimization-v1-2026-06/task-history/review-continuous-openclaw-execution-plan.md` | execution plan history | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-coordination.md` | `docs/archive/optimization-v1-2026-06/task-history/review-openclaw-coordination.md` | coordination history | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-worker-prompts.md` | `docs/archive/optimization-v1-2026-06/task-history/review-openclaw-worker-prompts.md` | worker prompts history | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-next-tasks.md` | `docs/archive/optimization-v1-2026-06/task-history/review-openclaw-next-tasks.md` | next-tasks history | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-dispatch-r01.md` | `docs/archive/optimization-v1-2026-06/task-history/review-openclaw-dispatch-r01.md` | dispatch r01 history | none | - | git_mv |

## git_mv -> archive/.../evidence-reports/  (59)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/optimization-v1/review-full-audit-batch-01-chitosan.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-01-chitosan.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-01-plant-tannin.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-01-plant-tannin.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-01-polydopamine-coating.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-01-polydopamine-coating.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-01-silk-fibroin.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-01-silk-fibroin.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-01-wood-xylem.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-01-wood-xylem.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-02-biomineralization-template.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-02-biomineralization-template.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-02-bone-structure.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-02-bone-structure.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-02-fish-scale-hydroxyapatite-preflight.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-02-fish-scale-hydroxyapatite-preflight.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-02-oyster-shell.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-02-oyster-shell.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-02-scallop-shell.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-02-scallop-shell.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-03-microbes-cells-preflight.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-03-microbes-cells-preflight.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-04-separation-surfaces-preflight.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-04-separation-surfaces-preflight.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-05-selective-materials-preflight.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-05-selective-materials-preflight.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-batch-06-enrichment-crosscheck-preflight.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-batch-06-enrichment-crosscheck-preflight.md` | batch preflight evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-batch-07-parked-registry.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-batch-07-parked-registry.md` | openclaw batch evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-batch-08-remaining-core.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-batch-08-remaining-core.md` | openclaw batch evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-batch-09-core-source-gaps.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-batch-09-core-source-gaps.md` | openclaw batch evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-batch-10-office-reconciliation.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-batch-10-office-reconciliation.md` | openclaw batch evidence report | none | review-post-office-reconciliation.md | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-batch-11-diatom-causal-card.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-batch-11-diatom-causal-card.md` | openclaw batch evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-diatom-path-dedup.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-diatom-path-dedup.md` | dedup evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-dna-aptamer-evidence-build.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-dna-aptamer-evidence-build.md` | evidence build report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-fish-scale-cleanup.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-fish-scale-cleanup.md` | cleanup evidence report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-mof-verification-semantics.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-mof-verification-semantics.md` | mof semantics report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-pda-mussel-overlap.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-pda-mussel-overlap.md` | overlap report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-pda-patent-ocr.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-pda-patent-ocr.md` | OCR report | none | - | git_mv |
| `docs/optimization-v1/review-full-audit-openclaw-starch-extreme-values.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-full-audit-openclaw-starch-extreme-values.md` | extreme values report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-boundary-b1-writes.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-boundary-b1-writes.md` | boundary writes report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-candidate-audit-chitosan-diatom-20260618.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-candidate-audit-chitosan-diatom-20260618.md` | candidate audit report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-chitosan-diatom-verification.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-chitosan-diatom-verification.md` | verification report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-diatom-card-write.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-diatom-card-write.md` | card write report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-enrichment-causal-fill.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-enrichment-causal-fill.md` | enrichment fill report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-iob-verification.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-iob-verification.md` | IOB verification report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-mussel-fish-verification.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-mussel-fish-verification.md` | verification report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-ocr-cn113275374a.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-ocr-cn113275374a.md` | OCR report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-ocr-cn114570339a-cn113244898a.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-ocr-cn114570339a-cn113244898a.md` | OCR report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-oyster-shell-verification.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-oyster-shell-verification.md` | verification report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-pda-verification.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-pda-verification.md` | verification report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-r01-structured-recovery.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-r01-structured-recovery.md` | R01 structured recovery report | none | future commit-audit-root-cause.md | git_mv |
| `docs/optimization-v1/review-openclaw-tier2a-verification.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-tier2a-verification.md` | tier2a verification report | none | - | git_mv |
| `docs/optimization-v1/review-openclaw-zero-perf-scope-notes.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-zero-perf-scope-notes.md` | scope notes report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-acceptance-boundary-b1.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-acceptance-boundary-b1.md` | acceptance report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-acceptance-diatom-card.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-acceptance-diatom-card.md` | acceptance report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-acceptance-iob.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-acceptance-iob.md` | acceptance report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-acceptance-ocr-cn113275374a.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-acceptance-ocr-cn113275374a.md` | acceptance report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-acceptance-ocr-cn114570339a-cn113244898a.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-acceptance-ocr-cn114570339a-cn113244898a.md` | acceptance report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-acceptance-oyster-shell.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-acceptance-oyster-shell.md` | acceptance report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-acceptance-tier2a.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-acceptance-tier2a.md` | acceptance report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-acceptance-tier2b.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-acceptance-tier2b.md` | acceptance report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-full-inventory-20260617.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-full-inventory-20260617.md` | inventory report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-remaining-gaps-20260618.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-remaining-gaps-20260618.md` | gaps report | none | - | git_mv |
| `docs/optimization-v1/review-qoderwork-session-report-20260618.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-session-report-20260618.md` | session report | none | - | git_mv |
| `docs/optimization-v1/review-codex-acceptance-candidate-a-20260618.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-codex-acceptance-candidate-a-20260618.md` | acceptance report | none | - | git_mv |
| `docs/optimization-v1/review-batch-coral-skeleton.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-batch-coral-skeleton.md` | review batch report | none | - | git_mv |
| `docs/optimization-v1/review-batch-lobster-exoskeleton.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-batch-lobster-exoskeleton.md` | review batch report | none | - | git_mv |
| `docs/optimization-v1/review-batch-magnetic-bacteria.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-batch-magnetic-bacteria.md` | review batch report | none | - | git_mv |
| `docs/optimization-v1/review-batch-pitcher-plant.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-batch-pitcher-plant.md` | review batch report | none | - | git_mv |
| `docs/optimization-v1/review-batch-spider-silk.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-batch-spider-silk.md` | review batch report | none | - | git_mv |
| `docs/optimization-v1/evidence-review-report.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/evidence-review-report.md` | evidence review report | none | - | git_mv |
| `docs/optimization-v1/review-post-office-reconciliation.md` | `docs/archive/optimization-v1-2026-06/evidence-reports/review-post-office-reconciliation.md` | reconciliation report | none | future commit-audit-root-cause.md | git_mv |

## git_mv -> archive/.../old-handoffs/  (12)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/optimization-v1/CODEX-HANDOFF-PROMPT.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/CODEX-HANDOFF-PROMPT.md` | old handoff prompt | none | - | git_mv |
| `docs/optimization-v1/COLLAB-BOARD.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/COLLAB-BOARD.md` | superseded board | CLAUDE.md (historic) | future model-routing-protocol.md | git_mv |
| `docs/optimization-v1/COLLAB-HANDOFF.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/COLLAB-HANDOFF.md` | superseded handoff | CLAUDE.md (historic) | claude-code handoff | git_mv |
| `docs/optimization-v1/COLLABORATION-PROTOCOL.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/COLLABORATION-PROTOCOL.md` | superseded protocol | CLAUDE.md (historic) | future model-routing-protocol.md | git_mv |
| `docs/optimization-v1/CROSS_DEVICE_HANDOFF_20260615.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/CROSS_DEVICE_HANDOFF_20260615.md` | old cross-device handoff | none | - | git_mv |
| `docs/optimization-v1/HOME_PHASE9_WORK_PLAN_20260615.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/HOME_PHASE9_WORK_PLAN_20260615.md` | old work plan | none | - | git_mv |
| `docs/optimization-v1/session-handoff-20260615.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/session-handoff-20260615.md` | old session handoff | none | - | git_mv |
| `docs/optimization-v1/交接文档_HANDOFF.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/交接文档_HANDOFF.md` | old handoff | none | - | git_mv |
| `docs/optimization-v1/review-sync-summary.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/review-sync-summary.md` | superseded sync summary | CLAUDE.md (historic) | - | git_mv |
| `docs/optimization-v1/review-worklog.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/review-worklog.md` | superseded worklog | CLAUDE.md (historic) | - | git_mv |
| `docs/optimization-v1/review-full-audit-worklog.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/review-full-audit-worklog.md` | superseded worklog | CLAUDE.md (historic) | - | git_mv |
| `docs/optimization-v1/review-v0.1-delivery-summary.md` | `docs/archive/optimization-v1-2026-06/old-handoffs/review-v0.1-delivery-summary.md` | delivery summary | none | future execution-roadmap.md | git_mv |

## git_mv -> archive/.../generated-logs/  (26)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/optimization-v1/verify-logs/biomineralization-template.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/biomineralization-template.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/bone-structure.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/bone-structure.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/cell-membrane-ion-channel.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/cell-membrane-ion-channel.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/chitosan.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/chitosan.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/chlorella-cell-wall.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/chlorella-cell-wall.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/coral-skeleton.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/coral-skeleton.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/diatom-frustule.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/diatom-frustule.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/dna-aptamer.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/dna-aptamer.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/fish-scale-hydroxyapatite.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/fish-scale-hydroxyapatite.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/iron-oxidizing-bacteria.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/iron-oxidizing-bacteria.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/lobster-exoskeleton.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/lobster-exoskeleton.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/magnetic-bacteria.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/magnetic-bacteria.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/mangrove-root.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/mangrove-root.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/mussel-foot-adhesion.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/mussel-foot-adhesion.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/mycelium.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/mycelium.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/oyster-shell.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/oyster-shell.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/pitcher-plant-slippery-surface.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/pitcher-plant-slippery-surface.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/plant-tannin.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/plant-tannin.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/polydopamine-coating.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/polydopamine-coating.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/scallop-shell.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/scallop-shell.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/silk-fibroin.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/silk-fibroin.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/spider-silk.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/spider-silk.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/sulfate-reducing-bacteria.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/sulfate-reducing-bacteria.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/verify-logs/wood-xylem.md` | `docs/archive/optimization-v1-2026-06/generated-logs/verify-logs/wood-xylem.md` | generated per-prototype verify log | none | - | git_mv |
| `docs/optimization-v1/missing-sources.md` | `docs/archive/optimization-v1-2026-06/generated-logs/missing-sources.md` | generated missing-source list | none | - | git_mv |
| `docs/optimization-v1/literature-requests.md` | `docs/archive/optimization-v1-2026-06/generated-logs/literature-requests.md` | generated literature requests | none | - | git_mv |

## no_action -> docs/archive/** (already archived, directive_4)  (37)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/archive/AI_AGENT_PROGRESS.md` | `docs/archive/AI_AGENT_PROGRESS.md` | already archived; directive_4 no re-shuffle | none | - | no_action |
| `docs/archive/AI_COORDINATION_PROTOCOL.md` | `docs/archive/AI_COORDINATION_PROTOCOL.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/AI_SUPERVISOR_DIRECTIVE.md` | `docs/archive/AI_SUPERVISOR_DIRECTIVE.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/Github management-INSTRUCTIONS.md` | `docs/archive/Github management-INSTRUCTIONS.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/HANDOFF.md` | `docs/archive/HANDOFF.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/README-clean.md` | `docs/archive/README-clean.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/REVIEW-GUIDE.md` | `docs/archive/REVIEW-GUIDE.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/SESSION-CONTEXT.md` | `docs/archive/SESSION-CONTEXT.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/alginate_brief_evaluation.md` | `docs/archive/alginate_brief_evaluation.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/canon-stabilization-plan-20260610.zip` | `docs/archive/canon-stabilization-plan-20260610.zip` | already archived; directive_4 | none | - | no_action |
| `docs/archive/canon-stabilization-plan-20260610/README.md` | `docs/archive/canon-stabilization-plan-20260610/README.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/canon-stabilization-plan-20260610/phase-0-baseline.md` | `docs/archive/canon-stabilization-plan-20260610/phase-0-baseline.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/canon-stabilization-plan-20260610/phase-1-interface-trust.md` | `docs/archive/canon-stabilization-plan-20260610/phase-1-interface-trust.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/canon-stabilization-plan-20260610/phase-2-enrichment-split.md` | `docs/archive/canon-stabilization-plan-20260610/phase-2-enrichment-split.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/canon-stabilization-plan-20260610/phase-3-rebuild-verification.md` | `docs/archive/canon-stabilization-plan-20260610/phase-3-rebuild-verification.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/canon-stabilization-plan-20260610/phase-4-mapping-sync.md` | `docs/archive/canon-stabilization-plan-20260610/phase-4-mapping-sync.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/canon-stabilization-plan-20260610/phase-5-handoff-report.md` | `docs/archive/canon-stabilization-plan-20260610/phase-5-handoff-report.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/chitosan_brief_evaluation.md` | `docs/archive/chitosan_brief_evaluation.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/five_gold_standards_evaluation.md` | `docs/archive/five_gold_standards_evaluation.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/mof_brief_evaluation.md` | `docs/archive/mof_brief_evaluation.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/mof_brief_evaluation_v2.md` | `docs/archive/mof_brief_evaluation_v2.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/quality-audit-2026-06-07.md` | `docs/archive/quality-audit-2026-06-07.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/repo-status-briefing.md` | `docs/archive/repo-status-briefing.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/adrmats_briefs_pre_phase9/bpa_内分泌干扰物去除.json` | `docs/archive/adrmats_briefs_pre_phase9/bpa_内分泌干扰物去除.json` | already archived; directive_4 | none | - | no_action |
| `docs/archive/adrmats_briefs_pre_phase9/pb(ii)_重金属离子去除.json` | `docs/archive/adrmats_briefs_pre_phase9/pb(ii)_重金属离子去除.json` | already archived; directive_4 | none | - | no_action |
| `docs/archive/adrmats_briefs_pre_phase9/pfoa_痕量吸附去除.json` | `docs/archive/adrmats_briefs_pre_phase9/pfoa_痕量吸附去除.json` | already archived; directive_4 | none | - | no_action |
| `docs/archive/adrmats_briefs_pre_phase9/smx_抗生素吸附去除.json` | `docs/archive/adrmats_briefs_pre_phase9/smx_抗生素吸附去除.json` | already archived; directive_4 | none | - | no_action |
| `docs/archive/下一步执行计划_本地AI.md` | `docs/archive/下一步执行计划_本地AI.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/任务布置_brief中心_交本地AI执行.md` | `docs/archive/任务布置_brief中心_交本地AI执行.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/优化方案_v2综合_2026-06-07.md` | `docs/archive/优化方案_v2综合_2026-06-07.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/分层核查标准_交本地AI执行.md` | `docs/archive/分层核查标准_交本地AI执行.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/文献检索指令.md` | `docs/archive/文献检索指令.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/文献检索指令_第三波.md` | `docs/archive/文献检索指令_第三波.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/最新提取质量问题汇总.md` | `docs/archive/最新提取质量问题汇总.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/架构审查与优化建议_2026-06-07.md` | `docs/archive/架构审查与优化建议_2026-06-07.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/路径映射修复指令.md` | `docs/archive/路径映射修复指令.md` | already archived; directive_4 | none | - | no_action |
| `docs/archive/金标准闭环_启发质量评分卡.md` | `docs/archive/金标准闭环_启发质量评分卡.md` | already archived; directive_4 | none | - | no_action |

## no_action -> docs/imported/** (runtime assets, directive_3)  (45)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/imported/library-enhancement/README.md` | `docs/imported/library-enhancement/README.md` | runtime asset; directive_3 keep in place, approved structure | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/design-rules.json` | `docs/imported/library-enhancement/design-rules.json` | runtime asset read by biomimetic_context; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/.gitkeep` | `docs/imported/library-enhancement/principles/mechanisms/.gitkeep` | dir marker; directive_3 | none | - | no_action |
| `docs/imported/library-enhancement/principles/trade-offs/.gitkeep` | `docs/imported/library-enhancement/principles/trade-offs/.gitkeep` | dir marker; directive_3 | none | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/.gitkeep` | `docs/imported/library-enhancement/principles/design-strategies/.gitkeep` | dir marker; directive_3 | none | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/amino-deprotonation-metal-coordination.md` | `docs/imported/library-enhancement/principles/mechanisms/amino-deprotonation-metal-coordination.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/amino-metal-selectivity.md` | `docs/imported/library-enhancement/principles/mechanisms/amino-metal-selectivity.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/amino-protonation-anion-adsorption.md` | `docs/imported/library-enhancement/principles/mechanisms/amino-protonation-anion-adsorption.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/carboxyl-deprotonation-metal-coordination.md` | `docs/imported/library-enhancement/principles/mechanisms/carboxyl-deprotonation-metal-coordination.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/carboxyl-ph-selectivity-shift.md` | `docs/imported/library-enhancement/principles/mechanisms/carboxyl-ph-selectivity-shift.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/catechol-amino-synergy.md` | `docs/imported/library-enhancement/principles/mechanisms/catechol-amino-synergy.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/catechol-low-ph-suppression.md` | `docs/imported/library-enhancement/principles/mechanisms/catechol-low-ph-suppression.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/catechol-metal-selectivity.md` | `docs/imported/library-enhancement/principles/mechanisms/catechol-metal-selectivity.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/catechol-oxidation-quinone.md` | `docs/imported/library-enhancement/principles/mechanisms/catechol-oxidation-quinone.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/catechol-ph-coordination.md` | `docs/imported/library-enhancement/principles/mechanisms/catechol-ph-coordination.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/chelate-effect-multidentate.md` | `docs/imported/library-enhancement/principles/mechanisms/chelate-effect-multidentate.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/competitive-ion-saturation.md` | `docs/imported/library-enhancement/principles/mechanisms/competitive-ion-saturation.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/egg-box-carboxyl-coordination.md` | `docs/imported/library-enhancement/principles/mechanisms/egg-box-carboxyl-coordination.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/high-salinity-coordination-suppression.md` | `docs/imported/library-enhancement/principles/mechanisms/high-salinity-coordination-suppression.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/ionic-strength-coordination-enhancement.md` | `docs/imported/library-enhancement/principles/mechanisms/ionic-strength-coordination-enhancement.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/irving-williams-selectivity.md` | `docs/imported/library-enhancement/principles/mechanisms/irving-williams-selectivity.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/metal-ligand-ratio-stoichiometry.md` | `docs/imported/library-enhancement/principles/mechanisms/metal-ligand-ratio-stoichiometry.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/redox-catechol-degradation.md` | `docs/imported/library-enhancement/principles/mechanisms/redox-catechol-degradation.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/temperature-coordination-stability.md` | `docs/imported/library-enhancement/principles/mechanisms/temperature-coordination-stability.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/thiol-oxidation-degradation.md` | `docs/imported/library-enhancement/principles/mechanisms/thiol-oxidation-degradation.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/thiol-soft-metal-specificity.md` | `docs/imported/library-enhancement/principles/mechanisms/thiol-soft-metal-specificity.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/mechanisms/universal-proton-suppression.md` | `docs/imported/library-enhancement/principles/mechanisms/universal-proton-suppression.md` | boundary-reuse asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/trade-offs/acid-resistance-vs-carboxyl-coordination.md` | `docs/imported/library-enhancement/principles/trade-offs/acid-resistance-vs-carboxyl-coordination.md` | trade-off asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/trade-offs/ease-of-synthesis-vs-structural-control.md` | `docs/imported/library-enhancement/principles/trade-offs/ease-of-synthesis-vs-structural-control.md` | trade-off asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/trade-offs/environmental-friendliness-vs-efficiency.md` | `docs/imported/library-enhancement/principles/trade-offs/environmental-friendliness-vs-efficiency.md` | trade-off asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/trade-offs/high-capacity-vs-fast-kinetics.md` | `docs/imported/library-enhancement/principles/trade-offs/high-capacity-vs-fast-kinetics.md` | trade-off asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/trade-offs/low-cost-vs-high-performance.md` | `docs/imported/library-enhancement/principles/trade-offs/low-cost-vs-high-performance.md` | trade-off asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/trade-offs/mechanical-strength-vs-porosity.md` | `docs/imported/library-enhancement/principles/trade-offs/mechanical-strength-vs-porosity.md` | trade-off asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/trade-offs/selectivity-vs-broad-spectrum.md` | `docs/imported/library-enhancement/principles/trade-offs/selectivity-vs-broad-spectrum.md` | trade-off asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/trade-offs/wet-stability-vs-functional-activity.md` | `docs/imported/library-enhancement/principles/trade-offs/wet-stability-vs-functional-activity.md` | trade-off asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/bio-to-material-feature-mapping.md` | `docs/imported/library-enhancement/principles/design-strategies/bio-to-material-feature-mapping.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/biomineralization-template-strategy.md` | `docs/imported/library-enhancement/principles/design-strategies/biomineralization-template-strategy.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/dynamic-responsive-design.md` | `docs/imported/library-enhancement/principles/design-strategies/dynamic-responsive-design.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/functional-group-density-capacity.md` | `docs/imported/library-enhancement/principles/design-strategies/functional-group-density-capacity.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/hierarchical-structure-advantage.md` | `docs/imported/library-enhancement/principles/design-strategies/hierarchical-structure-advantage.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/multi-pollutant-synergistic-removal.md` | `docs/imported/library-enhancement/principles/design-strategies/multi-pollutant-synergistic-removal.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/multivalent-synergy.md` | `docs/imported/library-enhancement/principles/design-strategies/multivalent-synergy.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/recyclability-design.md` | `docs/imported/library-enhancement/principles/design-strategies/recyclability-design.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/selectivity-design.md` | `docs/imported/library-enhancement/principles/design-strategies/selectivity-design.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |
| `docs/imported/library-enhancement/principles/design-strategies/surface-wettability-tuning.md` | `docs/imported/library-enhancement/principles/design-strategies/surface-wettability-tuning.md` | design-strategy asset; directive_3 | tools/biomimetic_context.py | - | no_action |

## no_action -> docs/active/**  (1)
| original_path | proposed_path | classification_reason | active_references | replacement_document | action |
|---|---|---|---|---|---|
| `docs/active/PROJECT-RECOVERY-DESIGN.md` | `docs/active/PROJECT-RECOVERY-DESIGN.md` | active operational doc, no path edits needed | takeover guide | - | no_action |

