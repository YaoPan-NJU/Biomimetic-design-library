---
status: active
owner: claude-code (coordinator)
date: 2026-06-19
---

# Execution Roadmap & Acceptance Runbook

Milestone order with the checks each must pass. M0 is done; M1+ require tool/canon work
outside this goal and are listed to set up the next authorization.

## Milestone status

| Milestone | Status |
|---|---|
| M0 Docs | ✅ done (`4987c0a`) |
| M1 Tool safety | pending authorization (implements tooling) |
| M2 Canon recovery | blocked on M1 |
| M3 Expansion & tiering | blocked on M2 |
| M4 v1 acceptance | blocked on M2/M3 |
| M5 Full audit | blocked on M4 |

## New report / audit-output location (runbook-defined)

`docs/archive/**` is **historical traceability only** — never the output directory for new
audit/evidence reports, and never the primary startup read. New audit and worker evidence
reports go to a **staging area under `docs/active/`**, not the archive:

- **Worker candidate evidence:** `docs/active/audit-candidates/<worker>-<scope>-<date>.md`
  (one per dispatch; declared per the worker-report contract in `model-routing-protocol.md`).
- **Coordinator acceptance records:** `docs/active/acceptance/<item-id>-<date>.md`.
- **Canon-recovery ledger entries:** `docs/registries/canon-recovery-ledger.jsonl` (append-only;
  schema `docs/active/canon-recovery-ledger.schema.json`).

Only after a report is no longer current (superseded by a later milestone or a canon
write) is it *moved* into `docs/archive/...` as historical traceability — and only then.
Until that runbook rule is overridden, **nothing is written under `docs/archive/`** as new output.

## M1 — Tool safety (recommended next; REQUIRES implementing tools, not in-goal)

1. Write **failing regression tests** reproducing destructive-build behaviour:
   - a rebuild must not drop quotes/locators/causal/translations/boundaries on canon;
   - the `13dfdbf` keyword-matching path must not auto-upgrade verification from DOI/keyword alone.
2. Add **commit-audit metrics** (`tools/` count guards for rows/quotes/locators/causal/
   translation/boundary/scope_note/tier) that fail on unexplained drops.
3. Add **stable-identity matching** + **ambiguity gates** (zero/multiple → record + escalate).
4. Add the **recovery ledger** writer conforming to
   `canon-recovery-ledger.schema.json`.
5. Make `build_prototypes_db.py` **staging-only by default**; guard any canon write with
   clean-tree + guarded-mode + invariant checks.

**Acceptance:** regression tests red-on-damage; build writes staging only; invariant
guards green on a no-op re-run; `check_repo_hygiene` unchanged from baseline.

## M2 — Canon recovery (field-level)

1. Core 24 field-by-field restore from the historical input set (design §6.1) via stable
   identity + ledger; **never** whole-file replace.
2. Roll back `13dfdbf` 228-mechanism upgrades except the 6 accepted mussel-v3 rows.
3. Restore lost quotes/locators/translations/causal chains/boundaries (priority: the 82fa2c0 losses).
4. Return diatom row set to the accepted dedup state.

**Acceptance:** `validate_consistency` 0 errors; `check_chimera --strict` 0; causal-chain
+ boundary-guardrail pass; count guards green (every drop explained by a ledger entry);
ledger is append-only and internally consistent.

## M3 — Expansion & tiering

1. Assign `library_tier` (core|extended|exploratory) + `lifecycle_status`
   (active|pending_extraction|parked|deprecated) to all root prototypes.
2. Resolve the 12 missing `prototype_metadata` entries (commit-audit §5).
3. Record root/subdir duplication; propose merge/demote per promotion gates (Yao approval).
4. Expand toward 60–80 under the same gates.

**Acceptance:** mapping complete; promotion-gate checks pass; no prototype tier inferred
from its strongest row.

## M4 — v1 acceptance (ADRMATS-safe)

**Acceptance runbook:**
```
python3 -X utf8 tools/validate_consistency.py            # 0 errors
python3 -X utf8 tools/check_chimera.py --strict          # 0 violations
python3 -X utf8 tools/check_causal_chain.py              # active ≥1 qualified card each
python3 -X utf8 tools/check_translation_specificity.py    # no unqualified
python3 -X utf8 tools/check_boundary_guardrail.py          # numeric-rail 0; gate consistent
python3 -X utf8 tools/verify_adrmats_delivery.py          # 6/6 PASS
python3 -X utf8 tools/check_repo_hygiene.py                # ≤ baseline failures
git diff --check                                         # clean
```
Plus: ADRMATS results restricted to Core; every ranked value source-backed; every hard
DO-NOT evidence-backed; unresolved rows downgraded + excluded.

## M5 — Full audit

Every residual performance row, mechanism, boundary, source gap, exploratory prototype
has disposition accepted | soft background | parked knowledge gap | removed/refuted. No
unresolved row can reach ADRMATS recommendation, ranking, causal explanation, or DO-NOT.

## Validation per checkpoint (all Python `-X utf8`)

JSON parse → ledger completeness + ambiguity → count guards → `validate_consistency` →
`check_chimera --strict` → causal-chain + boundary-guardrail → ADRMATS interface/ranking-honesty →
doc-link checks → `git diff --check`. Re-run validation against the **commit object**,
not only the working tree.
