---
status: active
owner: claude-code (coordinator)
date: 2026-06-19
---

# Collaboration & Model-Routing Protocol

Claude Code is the sole coordinator (planning, model routing, branch/worktree control,
conflict decisions, evidence acceptance, validation, commits, merges, pushes).
OpenClaw (or the local equivalent) is a controlled worker: it may inspect sources,
extract evidence, produce candidate patches, and write reports in an isolated worktree.
It may **not** independently accept evidence grades, merge, push `review`, run the
destructive build, or replace whole canon files.

> 2026-06-19 note: the earlier `OpenClaw` worker is distinct from Claude Code's own
> subagents. Internal subagents may help with pure-text work but do **not** replace
> OpenClaw's MIMO multimodal model routing and evidence tasks.

## 1. Concurrency & write isolation

- Maximum concurrency: **3** workers.
- Only **one** worker may write a given JSON file at a time.
- Use isolated worktrees for any worker that mutates files; auto-removed if unchanged.

## 2. Mandatory model routing

**Use `mimo-v2.5` for anything that may require visual information:**
scanned PDFs; images/tables/curves/captions/layout; visual_cache or uncertain OCR;
patent figures; multimodal file inspection.

**Use `mimo-v2.5-pro` only when the task is certainly text-only:**
JSON/code/Git analysis; Markdown synthesis; structured text comparison; planning/report
synthesis without visual evidence.

**Split mixed tasks.** If a pro worker discovers a visual requirement, it stops that
evidence item and dispatches a `mimo-v2.5` worker. **Never infer visual content.**

## 3. Worker report contract (a routing violation = acceptance failure)

Every worker report declares: `model`, `modality_required`, `input_types`,
`routing_reason`, `baseline_commit`, `changed_files`, `validation`, `unresolved_items`.
Workers must report unchanged, rejected, ambiguous, and failed items — success-only
reports conceal risk.

## 4. Dispatch contract (every task specifies)

task ID + objective; success criteria; baseline commit + isolated worktree; exact
allowed/prohibited files; selected model + routing reason; input sources + exact field
paths; report path + machine-readable artifacts; validation commands + stop conditions;
no-push rule. **Never issue vague tasks** like "verify these prototypes".

## 5. Coordinator decision playbook (five-question test — see evidence-quality-standard.md)

Operational heuristics: latest ≠ healthiest; a report is not proof (re-run against the
named commit); DOI equality + keyword overlap identify candidates, not evidence; keep
biological inspiration separate from measured material performance; exact duplicates +
shared PDA/mussel or shell/HAp evidence need one ranking owner or explicit exclusion;
hard DO-NOT only for directly supported failure constraints; **pilot 3–10 rows before a
batch**; recompute statistics from committed JSON; review semantic field counts before
line diffs; validate after serialization and against the commit object; stage explicit
files (no `git add -A` near concurrent workers); keep recovery, evidence upgrades, schema
changes, and documentation moves in separate commits.

## 6. OpenClaw two-stage acceptance

1. **Contract gate**: baseline, model, allowed files, report schema, changed paths, clean diff.
2. **Evidence gate**: reproduce every hard DO-NOT, top-ranking value, scanned/visual claim,
   cross-prototype ownership decision, and unsupported status upgrade, plus a risk-based sample.

When uncertain → **no canon change** + a precise decision-queue entry. Progress is measured
by trustworthy dispositions, not upgraded-row count.
