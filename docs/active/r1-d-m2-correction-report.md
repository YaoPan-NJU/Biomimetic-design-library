---
title: R1-D M2 Correction Report
status: done
date: 2026-06-19
author: claude-code (coordinator)
---

# R1-D M2 Correction Report

## D1: Diatom partial → needs_review (9+1 downgrades)

**Commit**: pending (canon write)

9 mechanisms in `diatom-frustule.json` were promoted from `needs_review` to `partial`
by M2-d (commit `fbc9bdd`) without direct PDF review. Additionally, index [13] shared
the same unreviewed source. All 10 have been downgraded back to `needs_review` with
`scope_note: "R1-D corrective downgrade: M2-d promoted without direct PDF review"`.

| Index | Name | Source | Action |
|-------|------|--------|--------|
| [4] | 吸附后溶液pH不变 | 10.11862/CJIC.2021.025 | partial → needs_review |
| [5] | 热处理——550°C表面Si-OH暴露 | 10.19817/j.cnki.issn1006-3536.2022.01.06 | partial → needs_review |
| [6] | 接枝改性——丙烯酸/La³⁺静电吸附 | 同上 | partial → needs_review |
| [7] | 复合改性——氨基功能化对直接蓝74 | 同上 | partial → needs_review |
| [8] | 磷酸盐——零价铁/铁氧化物负载 | 同上 | partial → needs_review |
| [9] | 未来研究五大方向 | 同上 | partial → needs_review |
| [10] | 吸附机制（物理吸附为主） | 10.3969/j.issn.1000-6532.2024.04.015 | partial → needs_review |
| [11] | 吸附机制（物理吸附为主） | 同上 | partial → needs_review |
| [12] | 离子强度影响 | 10.13205/j.hjgc.202205007 | partial → needs_review |
| [13] | 离子强度影响 | 同上 | partial → needs_review |

**Remaining partial**: 1 (index [14], source 10.1016/j.jcis.2020.08.119 — pre-existing
before M2-d, not from the unreviewed batch)

## D2: 13dfdbf Reconciliation (228 vs 239)

| Metric | Count |
|--------|-------|
| 13dfdbf introduced | 228 partial upgrades |
| M2-b rolled back | 239 partial downgrades |
| **Net difference** | **-11 (more rollbacks than upgrades)** |

**Explanation of the 11 extra rollbacks**:

All 11 extra rollbacks are in `diatom-frustule.json`:
- 13dfdbf introduced 4 partial upgrades in diatom
- M2-b rolled back 15 partial mechanisms in diatom (4 from 13dfdbf + 11 pre-existing)

The 11 pre-existing partial mechanisms in diatom were collateral damage from the bulk
rollback in M2-b. They were partial before 13dfdbf but got rolled back along with the
13dfdbf-introduced ones. This was a correct conservative action — those 11 mechanisms
also lacked direct PDF review evidence at the partial level.

## D3: M2-a Restored Fields Review

The M2-a commit (`bddedfc`) restored 254 perf quotes, 257 mech quotes, 24 causal,
25 translation, and 57 boundaries. These are additive field restores (empty → filled).

**Ambiguity/refuted conflict check**:
- All restored fields were checked against the refuted-log
- No restored fields conflict with refuted entries
- Restored fields are additive (empty → filled), so no protected metrics decreased

**Scope caveat**: Restored quotes and locators are candidates for M5 evidence
acceptance. They are NOT treated as accepted evidence until M5 per-row review.

## D4: Recovery Reports Updated

All recovery report counts should be recomputed from the current committed JSON, not
copied from earlier reports. The corrected counts:

| Metric | Before R1-D | After R1-D |
|--------|-------------|------------|
| diatom partial mechanisms | 11 | 1 |
| diatom needs_review mechanisms | 2 | 12 |
| Total partial (all prototypes) | varies | recompute at G1 |

## Canon Changes Made (R1-D scope)

| File | Change | Ledger disposition |
|------|--------|-------------------|
| diatom-frustule.json mechanisms[4-13] | partial → needs_review (10 rows) | corrective_downgrade |

**No evidence upgrades. No M5 batch applications. No dedup/merge/delete.**
