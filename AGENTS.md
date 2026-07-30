# BMDL repository instructions

These rules apply to the whole repository.

## Repository contract

- Start with `README.md`, then use `docs/design.md` and `docs/references/definitions.md` for the data contract.
- `prototypes_db/*.json` is the canonical prototype and mechanism data. `prototypes/` is the human-readable representation.
- `feature-mapping.json`, `feature_matching_rules.json`, `pollutant_profiles.json`, and `pollutant_aliases.json` define retrieval behavior.
- `adrmats_export/match_export.json` is the supported downstream snapshot.

## Evidence and mapping rules

- Keep biological mechanism, material translation, and material removal performance as separate claims.
- A source-grounded claim needs a resolvable source identifier, a precise locator, a short supporting quote, and a matching scope.
- Do not upgrade inferred or partial evidence to verified evidence merely because a rule or mapping matched.
- Treat `fact`, `lead`, and `exploratory` as different evidence lanes. `weight` ranks relevance only within a lane; it is not confidence.
- Preserve negative findings, scope conflicts, missing evidence, and boundary conditions instead of silently rewriting them as facts.
- A root prototype must represent a biological source, transferable natural structure, or biomimetic mechanism. Generic engineering materials belong under realization examples or performance evidence.

## Change safety

- Prefer the smallest change that preserves the current schema and audit trail.
- Do not run `tools/build_prototypes_db.py` as a routine repair step; it can rebuild canonical data from older extraction outputs.
- Do not modify `tools/litextract`, `*_doi_map.json`, or `docs/optimization-v1` unless the task explicitly requires it.
- Never commit local settings, credentials, session transcripts, generated caches, or machine-specific absolute paths.
- Keep historical reports under `docs/archive/`; do not use archived documents as current instructions.

## Required validation

Run the checks relevant to the change. Before a release or canonical-data update, run the full set:

```bash
python -X utf8 -m pytest
python -X utf8 tools/validate_consistency.py --strict
python -X utf8 tools/check_chimera.py --strict
python -X utf8 tools/check_causal_chain.py
python -X utf8 tools/check_source_authenticity.py
python -X utf8 tools/check_from_source_integrity.py
python -X utf8 tools/check_translation_specificity.py
python -X utf8 tools/check_boundary_guardrail.py
python -X utf8 tools/check_repo_hygiene.py
python -X utf8 tools/verify_adrmats_delivery.py
```

`check_source_authenticity.py` validates source-identifier hygiene, not every scientific claim or locator.

## Git discipline

- Stage explicit paths; do not use `git add -A`.
- Do not force-push or rewrite shared history.
- Preserve unrelated user changes and the audit history of rejected or superseded decisions.
