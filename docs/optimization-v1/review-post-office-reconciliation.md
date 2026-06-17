# Post-Office Audit Reconciliation

status: codex_accepted_baseline
reviewed_at: 2026-06-17 Asia/Shanghai
branch_head: ef5defe

## Scope And Guardrails

This checkpoint reconciles office-side commits `69bf698`, `2e181bf`, `8efea83`, and `ef5defe` with the current canonical JSON and review records. It changes documentation status only. No `prototypes_db/**/*.json` file is changed, no verification grade is upgraded, and `tools/build_prototypes_db.py` is not run.

OpenClaw Batch 10 performed the bulk comparison, but Codex rejected its first report because of reproducible count and ID errors. The accepted results below come from direct JSON parsing, commit-diff inspection, and targeted PDF checks.

## Baseline Validation

| check | result | interpretation |
|---|---:|---|
| JSON parse | 58/58 pass | No malformed canonical/enrichment/reference JSON. |
| `validate_consistency.py` | 0 errors, 132 warnings | Structural consistency passes; warnings remain substantive review work. |
| `check_chimera.py` | 0 reported violations | The checker has a limited keyword scope and is not proof of full source correctness. |
| `check_causal_chain.py` | 27/432 qualified cards; 1 active prototype without a card | `diatom-frustule` is the only active prototype with no qualified causal-chain card. The script also writes `phase5-chains.md`; sandbox blocked that write during this baseline run. |
| `check_boundary_guardrail.py` | fail | 60 soft boundaries, 0 hard boundaries; `diatom-frustule` has no qualified boundary. |
| `check_translation_specificity.py` | 25/25 pass | All active prototypes have a structurally valid translation. |
| `check_repo_hygiene.py` | fail | Root `CLAUDE.md` is intentional but absent from the checker allowlist. |

Current active-canon counts are 24 prototypes, 432 mechanisms (`18 verified`, `414 needs_review`) and 390 performance rows (`172 needs_review`, `218 unverified`). There are currently no active performance rows at `verified` grade. These counts show that the full evidence audit is not complete even though several cleanup packages are complete.

## Boundary Register Reconciliation

Direct parsing gives 105 unique boundary IDs: 43 `soft_boundary`, 40 `knowledge_gap`, and 22 `hard_do_not`. Before this checkpoint all 105 table rows still said `pending_yao`.

Commit `8efea83` claims 47 written rules, but its actual JSON diff adds exactly 45 IDs. Current JSON also contains exactly those 45 IDs across 24 files: 37 soft, 6 hard, and 2 gap rules. Therefore the difference is a commit-message/report counting error, not two rules lost later.

The accepted status split is:

| status | count | meaning |
|---|---:|---|
| `applied_boundary_2026_06_17` | 45 | Exact boundary ID is present in current JSON. |
| `guard_rule_2026_06_17` | 14 | Contaminating target data was removed; the rule prevents reintroduction. |
| `acknowledged_knowledge_gap_2026_06_17` | 38 | Yao-approved acknowledgement; intentionally no JSON rule. |
| `approved_unapplied_2026_06_17` | 8 | Approved category, but no matching JSON representation exists; requires targeted resolution. |

The eight approved-but-unapplied items are `B01-CHI-002`, `B13-PDA-OCR-002`, `B03-CMIC-001`, `B04-SHART-003`, `B05-MATREF-001`, `B07-REG-002`, `B01-PDA-003`, and `B03-CHL-001`. The previous footer incorrectly listed `B03-CHL-001` as a guard rule; its mechanism is still present. `B03-CHL-002` is the actual removed Chlorella performance block and is the guard rule.

## Queue Reconciliation

The queue contains 148 unique IDs. This checkpoint updates only actions proven by current JSON or exact commit diffs. Important partial/superseded cases are preserved rather than counted twice:

- MOF `F05-MOF-002` is partial: 12 pure-chitosan rows were removed, while two MOF-chitosan hybrids were retained for a separate decision.
- Fish-scale `F02-FISH-007` is partial: shell rows and wrong-source mechanisms were removed, while MICP performance rows remain under their separate decision.
- Plant-tannin `F01-PLT-001` is partial: main JSON contamination was removed, but the enrichment mirror still contains the six membrane mechanism keys.
- `F08-DNA-005` was approved in the scope-decision summary, but commit `2e181bf` did not edit DNA JSON; it is `approved_pending_application`, not applied.
- `F02-BMT-001` changed `source` and `n_verified`, which is an evidence-grade change rather than mechanical metadata. It is moved to `needs_codex_evidence_recheck` pending source-scope adjudication.

## Targeted Source Checks

### CN114887602A

The PDF is absent from the current ignored literature worktree, but it is not irrecoverable:

- visual cache exists under `仿生文献库/专利/`;
- extraction JSON exists under `tools/litextract/outputs/extractions/专利/json/`;
- Git object `9ee5da0:仿生文献库/专利/2022-CN114887602A-聚多巴胺-纤维素-吸附-除磷.pdf` contains the original 15-page PDF.

Codex extracted that object to a temporary path and confirmed patent paragraphs `[0147]-[0149]`: 12.6, 91.2, and 159.8 mg/g comparison values; more than 110 mg/g across five cycles; and 143.4 mg/g in real water. The correct operational state is `source_file_missing_from_current_worktree_but_recoverable`, not an unsupported claim and not a reproducible current-path resolution.

### Biomineralization Template

Wang2025 is a real local PDF and supports LanM@ZIF-8 rare-earth adsorption, protein encapsulation, pore-structure change, and 787.93 mg/g Nd capacity. However, the current mechanism text generalizes this to organic-template-controlled inorganic crystal growth direction/morphology. The quoted sentence alone does not fully support that broader mechanism wording. The office change from `llm_inference` to `literature-backed` and `n_verified: 0 -> 1` therefore requires evidence-scope review before final acceptance.

## Remaining Immediate Work

1. Resolve the eight approved-but-unapplied boundary representations without broad JSON writes.
2. Build one source-grounded causal-chain card and boundary for `diatom-frustule`.
3. Repair the root `CLAUDE.md` hygiene-check conflict without removing project instructions.
4. Continue row-level PDF audit: 414 active mechanisms remain `needs_review`; 218 active performance rows remain `unverified`.
5. Recompute the decision package after removing applied, superseded, accepted-no-change, and acknowledged-gap records.

## Commands Used

```bash
python3 -X utf8 -m json.tool <each prototypes_db/**/*.json>
python3 -X utf8 tools/validate_consistency.py
python3 -X utf8 tools/check_chimera.py
python3 -X utf8 tools/check_causal_chain.py
python3 -X utf8 tools/check_boundary_guardrail.py
python3 -X utf8 tools/check_translation_specificity.py
python3 -X utf8 tools/check_repo_hygiene.py
git show --format= --unified=0 8efea83 -- 'prototypes_db/**/*.json' 'prototypes_db/*.json'
git show '9ee5da0:仿生文献库/专利/2022-CN114887602A-聚多巴胺-纤维素-吸附-除磷.pdf'
```
