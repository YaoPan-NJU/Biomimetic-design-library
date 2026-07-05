# Stage 5 Formal Delta Report

**日期：** 2026-07-05
**文件：** `adrmats_export/match_export_stage5.json`（132 rows）

---

## Before / After 对比

| 指标 | Before | After |
|------|--------|-------|
| Total rows | 130 | 132 (+2 new) |
| Active (weight>0) | 130 | 132 |
| Changed | - | 87 |
| Added | - | 2 |
| Removed (quarantined) | 0 | 0 |
| Quarantined active | 0 | **0** ✅ |
| Exploratory >0.3 | 68 | **0** ✅ |
| Non-direct >0.5 | 38 | **0** ✅ |
| Top-5 concentration | ~70% | **61.8%** ↓ |

## Top-10 原型权重变化

| Prototype | Before (share) | After (share) | 变化 |
|-----------|---------------|--------------|------|
| chitosan | 20.64 (20.6%) | 13.95 (21.8%) | ↓ weight but ↑ share |
| bone-structure | 14.62 (14.6%) | 8.20 (12.8%) | ↓ |
| polydopamine-coating | 12.99 (13.0%) | 6.90 (10.8%) | ↓ |
| oyster-shell | 11.77 (11.8%) | 5.20 (8.1%) | ↓ |
| plant-tannin | 8.98 (9.0%) | 4.35 (6.8%) | ↓ |
| sulfate-reducing-bacteria | 6.15 (6.1%) | 2.75 (4.3%) | ↓ |
| silk-fibroin | 5.50 (5.5%) | 5.20 (8.1%) | = weight, ↑ share |
| iron-oxidizing-bacteria | 4.15 (4.1%) | 4.15 (6.5%) | = |
| plant-lignocellulosic | 0 (0%) | 1.25 (2.0%) | **NEW** |
| mussel-foot-adhesion | 3.35 (3.3%) | 3.35 (5.2%) | = |

## PFOA/BPA 候选

| Prototype | Pollutant | Before | After | Rule |
|-----------|-----------|--------|-------|------|
| plant-lignocellulosic | PFOA | (none) | **0.6** | NEW (Stage4 capacity) |
| plant-lignocellulosic | BPA | (none) | **0.65** | NEW (Stage4 capacity) |
| chitosan | BPA | 0.75 | 0.3 | capped |
| chitosan | PFOA | 0.75 | 0.3 | capped |
| plant-tannin | BPA | 0.7 | 0.3 | capped |
| polydopamine-coating | BPA | 0.67 | 0.3 | dedup+capped |
| polydopamine-coating | PFOA | 0.6 | 0.3 | dedup+capped |
| diatom-frustule | PFOA | 0.7 | 0.3 | capped |

## PDA/Mussel 去重

| Pollutant | Mussel (retained) | PDA (dedup) |
|-----------|-------------------|-------------|
| Cu(II) | 0.8 | 0.3 (was 0.75) |
| Hg(II) | 0.85 | 0.3 (was 0.8) |
| Pb(II) | 0.9 | (no PDA match) |
| U(VI) | 0.8 | 0.3 (was 0.75) |

## bone-structure 逐条处理

| Pollutant | Before | After | Rule |
|-----------|--------|-------|------|
| F- | 0.8 | 0.8 | retained (fact+direct) |
| Cd(II) | 0.85 | 0.5 | capped (lead non-direct) |
| Cr(VI) | 0.9 | 0.5 | capped |
| Cu(II) | 0.85 | 0.5 | capped |
| Hg(II) | 0.85 | 0.5 | capped |
| Pb(II) | 0.85 | 0.5 | capped |
| Zn(II) | 0.85 | 0.5 | capped |
| Ni(II) | 0.85 | 0.5 | capped |
| U(VI) | 0.825 | 0.5 | capped |
| As(III) | 0.9 | 0.5 | capped |
| As(V) | 0.9 | 0.5 | capped |
| PO43- | 0.9 | 0.5 | capped |
| NH4+ | 0.8 | 0.5 | capped |
| NO3- | 0.8 | 0.5 | capped |
| CIP | 0.9 | 0.3 | capped (no_source) |
| CR | 0.9 | 0.3 | capped (no_source) |
| TC | 0.9 | 0.3 | capped (no_source) |
