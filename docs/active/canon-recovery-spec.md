---
status: active
owner: claude-code (coordinator)
date: 2026-06-19
schema_file: canon-recovery-ledger.schema.json
---

# Canon Recovery Specification

Field-level recovery rules for `prototypes_db/*.json`. `prototypes_db/**` is **frozen
canon**: never reconstructed, never replaced wholesale, never matched by array index.

## 1. Record identities (match in order; zero/multiple = ambiguity, never guess)

**Performance row:**
1. prototype ID + normalized DOI/patent/standard + normalized parameter + value + material;
2. source basename + parameter + value + material;
3. normalized fingerprint excluding mutable evidence fields.

**Mechanism:**
1. prototype ID + DOI + normalized name + description fingerprint;
2. source basename + normalized name;
3. normalized name + description fingerprint.

Array index is never an identity.

## 2. Field precedence (for a matched row)

1. accepted direct PDF/visual evidence with quote + locator;
2. accepted human / Claude Code review;
3. accepted OpenClaw candidate reviewed by the coordinator;
4. unreviewed automated extraction;
5. empty or inferred data.

An empty field **never** overwrites a non-empty field. A later `partial` label does not
override an earlier accepted `needs_review` unless the later record includes
claim-supporting evidence. Status is **recomputed** from accepted evidence, never copied.

## 3. The recovery ledger

Every field-level change writes one ledger entry to
`docs/registries/canon-recovery-ledger.jsonl` (append-only). Schema:
`canon-recovery-ledger.schema.json`. One entry per restored/replaced/rejected/ambiguous
field, keyed by stable identity. The ledger is the audit trail; without an entry, no
canon field changes.

Entry shape: `id`, `prototype_id`, `field_path`, `record_identity`, `disposition`
(restored | replaced | rejected | ambiguous | kept), `from_source_commit`,
`evidence_precedence`, `basis` (from_source | review | openclaw_candidate |
extraction | inferred), `quote`, `locator`, `local_file`, `notes`, `applied_commit`,
`applied_at`.

## 4. Required corrections (design §6.4)

- Restore accepted performance quotes + locators lost at `82fa2c0`.
- Restore translations, causal chains, boundary structures, accepted top-level fields.
- Return core diatom row set to accepted dedup state.
- Roll back `13dfdbf` upgrades except independently accepted rows (chitosan 0, mussel 6).
- Retain accepted Task 52–73 evidence where it improves — never replaces — stronger evidence.
- Retain the 12 expanded root prototypes; assign tiers + lifecycle states.
- Add all root prototypes to the authoritative mapping (M3; no rebuild overwrites manual entries).

## 5. Build safety (enforced at M1, operational here)

`build_prototypes_db.py` becomes staging-only by default; canon writes require explicit
guarded mode + clean tree. Pre/post invariants reject drops in rows/quotes/locators/
causal/translation/boundary/scope_note/tier unless a reviewed allowlist explains each.
Stable matching refuses ambiguous merges. `pending_extraction` / manually-activated
prototypes cannot be overwritten by absent extraction data. Until M1 lands the guard,
the build is **forbidden for canon writes**.

## 6. Stop-and-escalate conditions

- stable identity ambiguous (zero or multiple matches);
- a source contradicts an accepted claim;
- a change would restore a refuted row;
- a worker used the wrong model modality;
- a protected count falls without an approved ledger entry;
- prototype ownership/scope needs Yao judgment;
- a required source cannot be obtained;
- a proposed operation needs whole-file canon replacement.
