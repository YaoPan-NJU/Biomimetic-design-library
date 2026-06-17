# OpenClaw Dispatch R01: Structured Field Recovery

status: assigned
model: xiaomi/mimo-v2.5
worker_branch: openclaw/recovery-r01
worker_worktree: /private/tmp/biomimetic-openclaw-r01
baseline_commit: 30481e4
target_commit: ec369a3

## Mission

Recover structured audit fields lost during office-side bulk JSON rewriting while preserving all valid office cleanup. You perform the complete comparison, matching, edits, report, tests, and commit. Codex only evaluates the resulting commit and report.

## Mandatory Rules

- Use `xiaomi/mimo-v2.5` only. Do not use any pro model.
- Work only in `/private/tmp/biomimetic-openclaw-r01`.
- Do not run `tools/build_prototypes_db.py`.
- Do not revert or replace whole JSON files.
- Do not edit `tools/litextract`.
- Do not push GitHub.
- Do not invent quotes, locators, cards, boundaries, or field mappings.
- Do not match records by array index alone.

## Work

1. Independently calculate the structured-field counts at `30481e4` and current HEAD.
2. Recover all baseline `design_translation` entries absent at current HEAD, keyed by prototype id.
3. Recover baseline mechanism `causal_chain` objects using stable matching in this order:
   - normalized DOI + normalized mechanism name;
   - source file basename + normalized mechanism name;
   - normalized name + description fingerprint.
4. If zero or multiple current records match, do not guess. Add the item to an ambiguity table.
5. Preserve all current mechanisms, performance rows, constraints, path fixes, scope removals, and metadata.
6. Do not change verification status unless restoring the exact baseline field attached to an unambiguous matching record.

## Required Report

Create `docs/optimization-v1/review-openclaw-r01-structured-recovery.md` containing:

- `status: ready_for_codex_acceptance`;
- worker/model/timestamps and commit hash;
- before/after counts;
- exact restored field paths;
- stable identity used for each causal-card match;
- ambiguity/unmatched table;
- changed-file list;
- validation commands, exit codes, and concise outputs;
- explicit confirmation that the build script was not run.

## Required Validation

Run, without modifying generated audit documents outside this task:

```bash
git diff --check
python3 -X utf8 -c "import glob,json; [json.load(open(p)) for p in glob.glob('prototypes_db/**/*.json', recursive=True)]"
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/validate_consistency.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_chimera.py --strict
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_causal_chain.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_boundary_guardrail.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_translation_specificity.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/verify_adrmats_delivery.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_repo_hygiene.py
```

Some checks may still fail because R02 owns vocabulary and hygiene repair. Record failures exactly; do not broaden scope.

Commit message:

```text
data: recover structured audit fields after office rewrite
```

