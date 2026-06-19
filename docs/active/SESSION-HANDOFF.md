---
title: Session Handoff — restart point
status: live_entry_for_next_session
date: 2026-06-19
author: claude-code (coordinator)
branch: review @ d85852c (12 commits ahead of origin/review, NOT pushed)
workspace: /Users/panyao/Desktop/Biomimetic-design-library (Desktop review worktree)
---

# SESSION HANDOFF — read this first on a new session

You are resuming the Biomimetic Design Library **recovery programme**. This file is the
single durable snapshot. For architecture read `PROJECT-RECOVERY-DESIGN.md`; for the live
entry this supersedes `execution-entry.md` (keep both, this is the fresher state).

## 0. One-line state

M0 (docs archive) → M1 (canon safety net) → M2 (a/b/c/d field-level canon recovery) →
M3 (tiering + 12 metadata gaps) → **M4 (acceptance) DONE**. All committed locally, **not
pushed**. Next is **M5 (per-row verification/disposition)** — freshly unblocked because Yao
added the missing PDFs. **Awaiting Yao's decision on M5 engine + dedup/merges + push.**

## 1. Branch / commit / canon

- Branch `review` @ `d85852c`. **12 commits ahead of `origin/review@e4dc2d0`, NOT pushed.**
- Working tree holds ONLY Yao's assets: `M tools/litextract` (submodule) + empty
  `docs/optimization-v1/` (the 3 `_w1/_w2/_w3_doi_map.json` are Yao's untracked DOI→PDF maps
  — DO NOT stage/commit them).
- `prototypes_db/*.json` is **frozen canon**; recovered field-by-field this session with a
  1,204-entry ledger (`docs/registries/canon-recovery-ledger.jsonl`).
- `canon_metrics --guard` is GREEN (no protected-metric decreases vs HEAD).

## 2. Iron rules learned this session (do not violate)

1. Canon edits are **field-level only** via stable identity + ledger. Never whole-file
   replace, never match by array index, never let empty overwrite non-empty.
2. Never resurrect a `refuted-log.md` row.
3. **Never upgrade `verification` from DOI/keyword overlap alone** (the `13dfdbf` lesson —
   that's why 228 mechanisms were rolled back this session). Use `can_upgrade_verification`:
   quote + locator + scope match → partial; 2 independent sources → verified.
4. `build_prototypes_db.py` is **staging-only by default**; never run it to write canon.
5. `canon_metrics.py --guard` must stay green before any canon commit; explained drops
   (e.g. dedup) need an allowlist.
6. **All Python: `python3 -X utf8`.** Separate commits per concern. No `git add -A`.
   Never touch `tools/litextract`, `_w*_doi_map.json`, `prototypes_db/**`, `feature-mapping.json`
   without authorization. No `git push` without explicit release approval.

## 3. What was done (10 commits, newest last)

| commit | milestone |
|---|---|
| `4987c0a` | M0 Phase 0 docs archive (176 git-mv; registries/references/active/) |
| `63f6471` | M0 7 operational docs (recovery-master-plan, commit-audit, canon-recovery-spec, evidence-quality-standard, model-routing-protocol, execution-roadmap, execution-entry) + ledger schema |
| `ca31a14` | M0 CLAUDE.md startup entry fix (archive not an entry/output) |
| `d194a19` | **M1** canon safety net: `test_canon_safety.py`, `canon_metrics.py`, `canon_recovery_lib.py`, staging-only build |
| `bddedfc` | **M2-a** restore 82fa2c0-stripped evidence (+254 perf quotes, +257 mech quotes, 24 causal, 25 translation, 57 boundaries) |
| `4961fad` | **M2-b** rollback 228 `13dfdbf` keyword-upgrades (6 mussel-v3 kept) |
| `b1e0385` | **M2-c** diatom dedup (42→29 perf) |
| `8c17751` | **M3** tier+lifecycle on 36; 12 prototype_metadata gaps; consistency errors 12→1 |
| `fbc9bdd` | **M2-d** gated verification recompute (9 mech →partial) |
| `d85852c` | **M4** acceptance report (`docs/active/m1-m4-recovery-report.md`) |

## 4. Coverage (root canon, recomputed)

- prototypes 36 (core 24+2 deprecated, extended 9, exploratory 1)
- performance_data: 418 rows, **384 graded (91%)**, 326 with quote (77%)
- mechanisms: 771, graded 35 (4% — honest post-rollback; inflation removed), with quote 266 (34%)
- causal_chain 24, translation 25, boundaries 57, tier 36/36
- ledger: 1,204 entries

## 5. M5 UNBLOCK (Yao added the missing PDFs)

- Local lib now 633 PDFs; Yao's `_w1/_w2/_w3_doi_map.json` (58 DOI→path entries) are filled.
- **416 needs_review/missing rows are now PDF-resolvable** (chitosan 68 mech, mussel 61,
  PDA 58, fish-scale 53, superhydrophobic 34, spider-silk 24, silk-fibroin 20, …). Only
  4 chitosan rows still truly missing.
- **openclaw IS usable** (`/opt/homebrew/bin/openclaw`): agents `main`/`yang-s-clawedbot`/
  `lit-extract`; models mimo-v2.5-pro (text) + mimo-v2.5 (multimodal, for scanned patents).
  **Use `openclaw agent --agent main --local --model ... --message ...`** — the gateway
  (non-`--local`) path has a broken plugin surface (`speech-core/runtime-api.js`).
  Verified: a `--local` turn returns in ~2.4s. Max 3 concurrent workers (shared key → 429).
- Scanned patents (CN113275374A/CN114570339A/CN113244898A/CN114887602A) MUST go via
  mimo-v2.5 multimodal — never infer visual content (directive #4: internal subagents don't
  replace OpenClaw's MIMO routing for evidence).

## 6. DECISION POINTS (need Yao)

| # | decision | why it blocks |
|---|---|---|
| 1 | **M5 engine**: proceed + which (OpenClaw workers [design-aligned] / inline text / workflow subagents). Pilot 3–10 rows first. | new workstream scope + risk (don't repeat 13dfdbf) |
| 2 | **root/subdir duplicates** (5 separation + 4 materials_reference + namib) + **2 PLAN DEDUP merges** (silkworm-silk→silk-fibroin, diatom-inspired-porous→diatom-frustule) | data-delete ops; recorded in `docs/registries/prototype-duplication-record.md` |
| 3 | 4 truly-missing chitosan rows | source or demote |
| 4 | 3 empty-shell causal cards (biomineralization/coral/dna-aptamer/magnetic-bacteria) | need literature |
| 5 | `verify_adrmats_delivery.py` flags `partial` as invalid tier (3/6 fails, pre-existing) | tool change beyond authorization |
| 6 | expansion 24→60 | hard-blocked on literature drop |
| 7 | **push** 12 commits | release approval |

## 7. How to resume (next session)

1. `cd /Users/panyao/Desktop/Biomimetic-design-library` ; `git log --oneline -3` (confirm `d85852c`).
2. `git status --short` — expect only `M tools/litextract` + `?? docs/optimization-v1/`.
3. `python3 -X utf8 tools/canon_metrics.py --guard` — expect green.
4. Read this file + `PROJECT-RECOVERY-DESIGN.md` + `docs/registries/decision-queue.md`.
5. Check with Yao on decision #1 (M5 engine) before dispatching openclaw workers.
6. If Yao authorized M5: pilot 3–10 rows (chitosan + diatom), OpenClaw `--local`, accept via
   two-stage gate (`model-routing-protocol.md`), gated upgrade, ledger, count-guard, commit.

## 8. Tooling built this session (in tools/)

- `canon_metrics.py` — count-guard (`--guard`, `--commit`, `--allowlist`).
- `canon_recovery_lib.py` — stable identity, ambiguity gate, gated upgrade, ledger writer.
- `recovery_engine.py` — enumerate recoverable fields across git history.
- `apply_recovery.py` — apply additive field restores (dry-run supported).
- `test_canon_safety.py` — 3 regression tests (must stay green).
- `build_prototypes_db.py` — now staging-only (guarded `--write-canon`).

## 9. Acceptance baseline (must not regress)

`validate_consistency` 1 error (was 12) · `check_chimera --strict` 0 ·
`check_translation_specificity` pass · `verify_adrmats_delivery` 3/6 (was 1/5, improved;
partial-tier failures pre-existing) · `check_repo_hygiene` 1 (CLAUDE.md root, baseline) ·
canon-safety tests 3/3 · `git diff --check` clean.
