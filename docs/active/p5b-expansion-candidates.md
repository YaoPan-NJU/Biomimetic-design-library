---
title: P5-B Expansion Candidates
status: preflight
date: 2026-06-20
author: claude-code (coordinator)
---

# P5-B Expansion Candidates

## Current Library (36 root prototypes)

| Tier | Count | Lifecycle |
|------|-------|-----------|
| Core | 26 | active |
| Extended | 10 | active |
| Exploratory | 1 | parked |
| Deprecated | 2 | deprecated |

**Target**: 60-80 total (Core 24 + Extended 24-36 + Exploratory 12-24)

## Evidence Hygiene Status (root only)

| Check | Status |
|-------|--------|
| Refuted entries | 0 ✅ |
| No-quote verified/partial | 0 ✅ |
| Missing honesty_ledger | 0 ✅ |
| Missing design_translation | 0 ✅ |
| Duplicate files | 34 (root + subdir copies, documented) |

## Expansion Strategy

Per V3 plan §5 Phase P3:
- **Extended→Core**: full PDF audit + qualified causal card + ≥1 evidence boundary + per-ranking-value source + Yao approval
- **Exploratory→Extended**: ≥1 direct source + 1 source-linked mechanism + applicable boundary + dedup
- **New Exploratory**: bibliographic discovery sufficient, no deterministic performance claims

### Batch 1 Candidates (Extended → Core promotion)

These Extended prototypes have enough data to potentially promote to Core:

| Prototype | Mechanisms | Performance | Causal Card | Design Translation | Notes |
|-----------|-----------|-------------|-------------|-------------------|-------|
| alginate | 5 | 70 | 0 | ✅ | Large extraction from Dong2025 review |
| lotus-leaf | 33 | 4 | 30 | ✅ | Rich wetting theory data |
| metal-organic-framework | 0 | 15 | 0 | ✅ | Perf from MOF review |
| starch-granule | 0 | 61 | 0 | ✅ | Large extraction from Akinterinwa2022 |
| cellulose-nanocrystal | 0 | 3 | 0 | ✅ | Small extraction |
| cactus-spine | 11 | 0 | 1 | ✅ | Mechanisms only |
| shark-skin | 18 | 0 | 1 | ✅ | Mechanisms only |
| superhydrophobic-artificial | 60 | 0 | 1 | ✅ | Large mechanism set |
| water-strider-leg | 52 | 0 | 1 | ✅ | Large mechanism set |

### Batch 2 Candidates (new Extended or Exploratory)

These could be added from existing literature:

| Candidate | Source | Rationale |
|-----------|--------|-----------|
| biochar (new) | Multiple reviews | Broad adsorption category |
| zeolite (new) | Mineral adsorption | Well-studied adsorbent |
| activated-carbon (new) | Standard adsorbent | Baseline comparison |
| graphene-oxide (new) | 2D material | High-performance adsorbent |

## First Batch Expansion Plan

### Phase 1: Promote 4 Extended → Core
- alginate, lotus-leaf, metal-organic-framework, starch-granule
- Requirements: qualified causal card + honesty_ledger verification + boundary assessment
- Estimated effort: 1-2 hours

### Phase 2: Add 2-3 new Extended from existing literature
- Focus on well-documented adsorbent categories
- Requires: at least 1 direct source + 1 mechanism + applicable boundary

### Phase 3: Promote remaining Extended → Core (if qualified)
- cellulose-nanocrystal, cactus-spine, shark-skin, superhydrophobic-artificial, water-strider-leg
- Need: causal card completion + boundary assessment

## Constraints
- No canon changes without Codex/Yao approval
- Each batch: commit + push + REVIEW_REQUEST
- Do not expand beyond 60-80 target
- Preserve quality > quantity
