# Task 6 — Remaining Wrong-Source Clearing Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Fix 1: lotus-leaf — Membrane/Distillation Mechanisms Removed

**File:** `prototypes_db/separation/lotus-leaf.json`

- Removed **9 membrane/distillation mechanisms** (DOI: 10.3390/membranes13080727)
- Added scope review note: "All remaining mechanisms are from general superhydrophobic/wetting/separation reviews. Zero lotus-specific mechanisms identified. Requires scope split before ranking."
- Remaining: **346 mechanisms** (all need scope review)

**Status:** Partial cleanup. The 346 remaining mechanisms are from general superhydrophobic/wetting/separation reviews (not lotus-specific). A full scope split is needed before these can be used for ranking. This requires Yao decision on how to partition the evidence.

## Fix 2: polydopamine-coating Enrichment — Wrong-Source Mechanisms Removed

**File:** `prototypes_db/enrichment/polydopamine-coating.json`

Removed **21 wrong-source mechanisms** including:
- Teflon/PVDF membrane distillation mechanisms (6)
- Lotus/gecko/rose petal biomimicry mechanisms (4)
- Superhydrophobic surface preparation methods (5)
- Oil/water droplet capture mechanisms (2)
- Janus/antibacterial membrane mechanisms (4)

Before: 65 mechanisms → After: **44 mechanisms**

Remaining enrichment mechanisms are PDA-specific or general adsorption chemistry.

## Fix 3: dna-aptamer — Biosensor Scope Annotation

**File:** `prototypes_db/dna-aptamer.json`

- Added biosensor scope note to `mechanisms[0]`: "Most aptamer literature is detection/biosensor-only. Only Bilibana2022 RNA-GO and CN121588773A DNA-GC have adsorption evidence."
- Added prototype-level scope note: "Zero performance_data. Most sources are biosensor-only."
- No rows removed (prototype has zero performance_data)

**Status:** Annotation complete. No data to remove.

## Summary

| fix | file | action | count |
|---|---|---|---|
| lotus-leaf | separation/lotus-leaf.json | Removed membrane/distillation mechanisms | -9 |
| PDA enrichment | enrichment/polydopamine-coating.json | Removed wrong-source mechanisms | -21 |
| DNA aptamer | dna-aptamer.json | Added biosensor scope notes | +2 notes |

## Remaining Work

| item | issue | next step |
|---|---|---|
| lotus-leaf 346 remaining mechanisms | All from general wetting/separation reviews, not lotus-specific | Yao decision: scope split or full reassignment |
| lotus-leaf 4 performance rows | Need source verification | Verify or demote |
| PDA enrichment 44 remaining mechanisms | Need content verification | Verify PDA-specific mechanisms |
