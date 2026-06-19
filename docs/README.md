# Documentation Index — Biomimetic Design Library

> Entry point for all project documentation. Read this first.
> For the ADRMATS calling interface see [`ADRMATS_CALL_GUIDE.md`](ADRMATS_CALL_GUIDE.md).
> For the recovery programme see [`active/PROJECT-RECOVERY-DESIGN.md`](active/PROJECT-RECOVERY-DESIGN.md).

This library is a biomimetic **water-treatment design reference** for ADRMATS. It
provides biological mechanisms, transferable design principles, evidence, and failure
boundaries. It does **not** design or prescribe materials. `prototypes_db/*.json` is the
frozen canon; everything under `docs/` is non-authoritative documentation that describes
or audits the canon.

---

## Directory layout

```
docs/
├── README.md                  ← this file (index)
├── design.md                  # library positioning & brief structure (hygiene-required)
├── ADRMATS_CALL_GUIDE.md      # how to call the interface (hygiene-required)
├── ADRMATS_DELIVERY_PLAN.md   # milestones (hygiene-required)
├── ADRMATS_INTEGRATION.md     # ADRMATS integration (hygiene-required)
├── SUPPORT_SCOPE_AND_RISKS.md # capability boundary (hygiene-required)
├── REPOSITORY_HYGIENE.md      # file-admission & branch policy (hygiene-required)
├── DEFINITIONS.md             # legacy root-level definitions (kept)
├── adrmats-integration-analysis.md
├── active/                    ← CURRENT operational documents (recovery programme)
├── registries/                ← live, machine-readable ledgers
├── references/                ← standards, plans, judgment criteria
├── imported/                  ← runtime assets read by tools/biomimetic_context.py
└── archive/                   ← historical (read-only; non-operational)
```

`check_repo_hygiene.py` mandates the six `docs/*.md` files above stay at the docs root.
Do not move them or the hygiene check fails.

---

## active/ — current operational documents

The recovery programme lives here. These are the **only** documents that direct current work.

- `PROJECT-RECOVERY-DESIGN.md` — the approved recovery architecture (milestones, tier
  model, canon-recovery rules, validation/stop conditions). **Authoritative for the
  recovery programme.**
- `CLAUDE-CODE-TAKEOVER.md` — the coordinator handoff (roles, model routing, dispatch
  contract, decision playbook).
- `phase0-archive-manifest-dryrun.md` — the executed Phase 0 documentation-archive
  manifest (every tracked docs file's disposition).
- `phase0-dispositions.json` — the machine-readable source of that manifest.
- (M-stage operational documents are added in separate commits: recovery master plan,
  commit-audit/root-cause report, canon recovery spec + ledger schema, evidence quality
  standard, model-routing protocol, execution roadmap + acceptance runbook.)

---

## registries/ — live ledgers

These are read during canon recovery. They are **not** historical reports — they record
decisions that constrain future canon writes.

- `decision-queue.md` — every audit finding awaiting or post-disposition (148 items;
  status tracks applied/pending/superseded).
- `boundary-do-not-register.md` — every DO-NOT / soft-boundary / knowledge-gap
  registration (105 IDs; includes guard-rules for already-removed data).
- `refuted-log.md` — rows removed as wrong-source. **Must never be resurrected.**
- `decision-queue-legacy.md` — the older per-task decision queue (historic).

---

## references/ — standards & plans

Judgment criteria and methodology that govern how evidence is graded and how the canon
is audited.

- `definitions.md` — evidence tiers, `basis` markers, causal-chain schema, boundary
  gate, nine iron rules. (The single-page judgment standard.)
- `optimization-plan-v1.md` — the original 9-phase optimization plan.
- `full-audit-plan.md` — the full-evidence-audit methodology.
- `next-stage-approval-summary.md` — approval summary.

---

## imported/ — runtime assets (do not move)

`docs/imported/library-enhancement/` is read at runtime by
`tools/biomimetic_context.py` (boundary-reuse principle library + `design-rules.json`).
These stay in place; moving them requires updating the tool, which is out of Phase 0
scope.

---

## archive/ — historical (read-only)

Historical phase reports, evidence audits, task history, old handoffs, and generated
logs. Archived with `git mv`; original paths are recorded in
[`active/phase0-dispositions.json`](active/phase0-dispositions.json). Archived files may
retain internal historical links but are **non-operational** — do not follow them as
current instructions.

- `archive/pre-optimization/` — pre-optimization-v1 docs (original curation plan,
  early phase completion reports, post-mortems, superpowers plans).
- `archive/optimization-v1-2026-06/` — the optimization-v1 era:
  - `phase-reports/` — Phase 0–8 reports, FINAL-report, coverage-gaps, phase5-chains.
  - `task-history/` — CLAUDE-CODE-TASK-*, review-clcode-task*, coordination & worker prompts.
  - `evidence-reports/` — review-full-audit-batch-*, review-openclaw-*, review-qoderwork-*,
    review-batch-*, reconciliation & R01 structured-recovery.
  - `old-handoffs/` — COLLAB-*, CODEX-HANDOFF-PROMPT, session-handoff, worklogs.
  - `generated-logs/` — per-prototype verify-logs, missing-sources, literature-requests.

---

## Where things live outside docs/

| Path | What |
|------|------|
| `prototypes_db/*.json` | **frozen canon** (24 Core + expansion; never edit without approved ledger entry) |
| `prototypes_db/enrichment/` | enrichment mirror (object-keyed schema) |
| `prototypes_db/separation/`, `materials_reference/`, `parked/` | tier/scope sub-collections |
| `feature-mapping.json` | pollutant→prototype + `prototype_metadata` (canon-adjacent config) |
| `tools/` | build / validation / verification scripts |
| `examples/adrmats_briefs/` | real interface output samples |

For the recovery programme, **start at** [`active/PROJECT-RECOVERY-DESIGN.md`](active/PROJECT-RECOVERY-DESIGN.md).
