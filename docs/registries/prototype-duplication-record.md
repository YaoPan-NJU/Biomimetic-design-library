---
status: record_only_pending_decision
date: 2026-06-19
owner: claude-code (coordinator)
---

# Prototype Duplication Record (root vs subdirectory)

Observed same-name prototype JSONs in multiple `prototypes_db/` locations. This is a
**record only** — no delete/merge/demote is performed. Per directive, these
relationships are documented for a Yao decision; M3-partial assigns tiers/lifecycle
but does not collapse the duplicates.

`prototypes_db/*.json` is the frozen canon (current). `enrichment/` is the object-keyed
mirror. `separation/`, `materials_reference/`, `parked/` are distinct collections with
their own historical purpose.

## Observed root/subdir duplicates

| prototype | root (e4dc2d0 copy) | subdir original | relationship |
|---|---|---|---|
| cactus-spine | root @ `e4dc2d0` | `separation/cactus-spine.json` @ `b6ab7df` (2026-06-07) | root is a Task 69-73 copy of the separation original |
| lotus-leaf | root @ `e4dc2d0` | `separation/lotus-leaf.json` @ `b6ab7df` | copy of separation original |
| shark-skin | root @ `e4dc2d0` | `separation/shark-skin.json` @ `b6ab7df` | copy of separation original |
| superhydrophobic-artificial | root @ `e4dc2d0` | `separation/superhydrophobic-artificial.json` @ `b6ab7df` | copy of separation original |
| water-strider-leg | root @ `e4dc2d0` | `separation/water-strider-leg.json` @ `b6ab7df` | copy of separation original |
| alginate | root @ `e4dc2d0` | `materials_reference/alginate.json` | both present; generation relationship unconfirmed |
| cellulose-nanocrystal | root @ `e4dc2d0` | `materials_reference/cellulose-nanocrystal.json` | both present; unconfirmed |
| metal-organic-framework | root @ `e4dc2d0` | `materials_reference/metal-organic-framework.json` | both present; unconfirmed |
| starch-granule | root @ `e4dc2d0` | `materials_reference/starch-granule.json` | both present; unconfirmed |
| namib-beetle | root @ `e4dc2d0` | `parked/namib-beetle.json` | both present; unconfirmed |

## DEDUP targets (PLAN §3, decision pending execution)

| deprecated (root) | canonical target | note |
|---|---|---|
| silkworm-silk | silk-fibroin | PLAN DEDUP; not yet merged; `dedup_note` set |
| diatom-inspired-porous | diatom-frustule | PLAN DEDUP; not yet merged; `dedup_note` set |

## Decision needed (Yao)

1. For the 5 separation + 4 materials_reference + namib-beetle duplicates: confirm which
   location is canonical and whether the other is removed or retained as a legacy alias.
2. Authorize the 2 PLAN DEDUP merges (content into target, source retired) — this is a
   data delete operation, outside autonomous scope.

Until decided, both copies remain; the count-guard tracks only root-level canon.
