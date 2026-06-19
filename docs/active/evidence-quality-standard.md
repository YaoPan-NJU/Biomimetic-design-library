---
status: active
owner: claude-code (coordinator)
date: 2026-06-19
supersedes_partial: docs/references/definitions.md (judgment standard), kept as the
  single-page field-card; this doc adds the recovery-time acceptance rules.
---

# Evidence Quality Standard

The grade assigned to a mechanism or performance row is only as good as the
evidence behind it. Grades are **recomputed from accepted evidence**, never copied.

## 1. Row grades

| grade | definition |
|---|---|
| `verified` | claim + metric directly supported by an accepted source; quote + locator present; source identity + scope match; required human approval complete |
| `partial` | a source supports a narrower or condition-specific claim, or only one source; limitation explicit |
| `needs_review` | a source may exist, but the claim has not passed direct review |
| `missing_pdf` | source identity known but file unavailable |
| `unverified` | no accepted evidence review completed |
| `knowledge_gap` | a material question is known to lack sufficient evidence |
| `scope_mismatch` | evidence is real but belongs to another prototype, metric, or domain |

Keyword overlap, DOI presence, a paper title, an abstract-only paraphrase, or an
LLM-generated sentence **cannot by itself** qualify a row as `partial` or `verified`.

## 2. Five-question acceptance test (coordinator; in order)

1. Does the source directly support the **complete** stored claim, not just share keywords?
2. Is it the same prototype, material class, and application domain?
3. Is the metric type exact: qmax, observed uptake, removal %, rejection, system-level
   removal, selectivity, sensor response, or figure estimate?
4. Can another reviewer reproduce the decision from source identity + quote + locator + local file?
5. Are conditions + failure boundaries represented honestly?

Any "no" blocks `verified`. Narrow the claim to `partial` only when the narrower claim is
directly supported; otherwise `needs_review` / `knowledge_gap` / `scope_mismatch`.

## 3. Ranking gate (a row enters quantitative ranking only when all hold)

- source identity, quote, locator present;
- metric type + unit normalized;
- prototype/material ownership explicit;
- duplicate + review-maximum exclusions resolved;
- test conditions represented or row marked condition-specific.

## 4. Boundary gate

- `hard_do_not` requires direct source evidence + locator; gate_level=hard ⟺ basis=from_source
  and verification∈{verified, corroborated}.
- `soft_boundary` may be condition-specific or single-source (no numeric threshold unless A-tier).
- Inferred limits stay `knowledge_gap`; they cannot block a design.

## 5. Non-interchangeable metrics (design §10.3)

Never compare as qmax: review-table maxima, concentration-dependent uptake ranges,
sensor LOD/Kd, removal %, rejection %, or system-level %. Distinguish the metric type
explicitly (`metric_type`) before any ranking or aggregation.

## 6. Source workflow (design §9)

register → deduplicate → tier-prioritized missing queue → acquire (open-access /
publisher / patent DB / institutional) → extract to candidate area → verify → accept
via Claude Code review before canon write. Unavailable sources stay
`missing_pdf` / `knowledge_gap`; secondary summaries must not be represented as the
missing primary.

## 7. Literature gates by tier

- **Core**: ≥2 independent sources for key mechanisms; every ranked value traced to a
  primary paper/patent; direct evidence for hard DO-NOT.
- **Extended**: ≥1 direct source, 1 source-linked mechanism, an applicability boundary;
  unverified values ranking-excluded.
- **Exploratory**: bibliographic discovery sufficient; no deterministic performance claim exposed.
