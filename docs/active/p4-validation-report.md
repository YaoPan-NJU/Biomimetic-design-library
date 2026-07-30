---
title: P4 Validation Report
status: complete
date: 2026-06-20
tested_commit: 0f89703
author: claude-code (coordinator)
---

# P4 Validation Report

## Full Validation Suite Results

| Validator | Exit | Result |
|-----------|------|--------|
| validate_consistency.py | 0 | 1 error (pre-existing: 5 separation broken links), 170 warnings |
| check_chimera.py --strict | 0 | 0 violations ✅ |
| test_invariant_guard.py | 0 | 7/7 PASS ✅ |
| canon_metrics.py --guard | 0 | GREEN ✅ |
| canon_metrics.py --check-integrity | 0 | PASS ✅ |
| check_causal_chain.py | 0 | 19 prototypes without qualified causal card |
| check_boundary_guardrail.py | 0 | Issues found (pre-existing) |
| verify_adrmats_delivery.py | 0 | 2 pass, 4 fail (pre-existing: partial-tier validation) |
| check_translation_specificity.py | 0 | 1不合格 (pre-existing) |
| test_interface_honesty.py | 0 | 3/3 PASS ✅ |
| check_repo_hygiene.py | 0 | 2 issues (pre-existing: CLAUDE.md + stale SESSION-HANDOFF) |
| validate_ledger_v2.py | 0 | PASS (0 errors, 0 PENDING) ✅ |
| test_canon_safety.py | 0 | 6/6 PASS ✅ |
| test_apply_recovery.py | 0 | 9/9 PASS ✅ |

## Authoritative Library Statistics

### Tier Distribution (root canon)

| Tier | Count |
|------|-------|
| core | 26 |
| extended | 10 |
| exploratory | 1 |
| unknown (subdirs) | 33 |
| **Total** | **70** |

### Lifecycle Distribution

| Status | Count |
|--------|-------|
| active | 34 |
| deprecated | 2 |
| parked | 1 |
| unknown (subdirs) | 33 |

### Content Totals

| Category | Count |
|----------|-------|
| Mechanisms | 1,419 |
| Performance data | 1,012 |
| Engineering constraints | 326 |
| Design translation | 25 |
| Honesty ledgers | 33 |
| Quotes present | 452 |
| Locators present | 861 |
| Refuted entries remaining | **0** |

### Verification Distribution

| Label | Mechanisms | Performance |
|-------|-----------|-------------|
| verified | 11 | 83 |
| partial | 11 | 207 |
| needs_review | 299 | 354 |
| unverified | 620 | 149 |
| knowledge_gap | — | 6 |
| scope_mismatch | — | 2 |
| single_source | — | 211 |

## Known Issues (deferred, not P4 scope)

1. **verify_adrmats_delivery 4 fails**: partial-tier validation rejects legitimate lead-tier entries — test fix needed
2. **1 separation render consistency error**: pre-existing broken links for 5 separation prototypes
3. **13 boundaries basis=from_source missing locator**: need locator addition or downgrade to soft
4. **19 prototypes without qualified causal card**: extended/exploratory tier, not Core-blocking
5. **1 translation不合格**: pre-existing
6. **2 repo hygiene issues**: CLAUDE.md at root + stale SESSION-HANDOFF.md

## Tier Count Reconciliation

Cowork directive noted discrepancy: "31 core + 12 extended" vs measured "26 core + 9 extended".

**Authoritative counts** (from current HEAD `0f89703`):
- Root canon: 26 core + 10 extended + 1 exploratory = 37 (includes 2 deprecated aliases)
- Subdirectory files: 33 (separation, materials_reference, parked) — these are mirrors/legacy, not additional unique prototypes
- Active unique prototypes: 34 (26 core + 8 extended excluding deprecated)

The "31 core" figure likely counted deprecated aliases (diatom-inspired-porous, silkworm-silk) and parked (namib-beetle) as core.
