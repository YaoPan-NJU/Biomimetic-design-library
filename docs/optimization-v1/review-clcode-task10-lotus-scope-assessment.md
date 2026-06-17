# Task 10 — Lotus-Leaf Scope Assessment Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Overview

Classified 346 remaining mechanisms in `prototypes_db/separation/lotus-leaf.json` by source domain.

## Classification Results

| category | count | percentage | source domain |
|---|---|---|---|
| superhydrophobic-general | 112 | 32.4% | General superhydrophobic coatings, fabrics, surfaces |
| membrane | 107 | 30.9% | Membrane distillation, PTFE membranes, separation membranes |
| antibacterial | 33 | 9.5% | Antibacterial/antifouling coatings, SLIPS |
| **lotus-specific** | **32** | **9.2%** | **Lotus effect, natural wax, Nelumbo surfaces** |
| wetting-theory | 24 | 6.9% | Young/Wenzel/Cassie-Baxter models, capillary theory |
| oil-water-separation | 18 | 5.2% | Oil spill sorption, superhydrophobic foams |
| other | 10 | 2.9% | General preparation methods, silane chemistry |
| rose-petal | 5 | 1.4% | Rose petal high-adhesion superhydrophobic |
| beetle-namib | 2 | 0.6% | Namib beetle Janus wetting, fog harvesting |
| gecko | 1 | 0.3% | Gecko foot biomimicry |
| water-strider | 1 | 0.3% | Water strider leg biomimicry |
| cactus-spine | 1 | 0.3% | Cactus fog collection |
| **Total** | **346** | **100%** | |

## Key Finding

**Only 32/346 mechanisms (9.2%) are lotus-specific.** The remaining 314 (90.8%) are from other superhydrophobic/wetting/separation domains.

## Scope Split Recommendation

### Option A: Keep Only Lotus-Specific (Recommended)
- Keep 32 lotus-specific mechanisms
- Move 107 membrane mechanisms → new `membrane-separation` or existing prototype
- Move 33 antibacterial mechanisms → new `antibacterial-coating` prototype
- Move 18 oil-water-separation → existing `superhydrophobic-artificial`
- Move 24 wetting-theory → shared reference pool
- Move 112 superhydrophobic-general → shared reference pool
- Move 5 rose-petal, 2 beetle, 1 gecko, 1 water-strider, 1 cactus → respective prototypes
- Move 10 other → shared reference pool

**Result:** lotus-leaf has 32 mechanisms, all lotus-specific.

### Option B: Keep Lotus + Wetting Theory
- Keep 32 lotus-specific + 24 wetting-theory = 56 mechanisms
- Relocate everything else

**Result:** lotus-leaf has 56 mechanisms with theoretical foundation.

### Option C: Full Scope Split
- Split all 346 into domain-specific prototypes
- lotus-leaf retains only lotus-specific evidence

## Performance Data Assessment

The 4 remaining performance rows need verification:
| index | source | issue |
|---|---|---|
| [0] | missing PDF | Zheng2024 silk superhydrophobic review |
| [1] | missing PDF | Usman2021 superhydrophobic oil-water review |
| [2] | missing PDF | Li2023 oil-water separation review |
| [3] | Khan2022 | Scallop-shell template 3D graphene foam, not lotus |

**Recommendation:** Demote [0-2] to knowledge_gap (missing PDFs), reassign [3] to superhydrophobic-artificial.

## Engineering Constraints Assessment

22 constraints exist. Need to verify which are lotus-specific vs general superhydrophobic.

## Narrative Entries Assessment

33 narrative entries exist. Need to verify lotus-specificity.

## Recommended Next Steps

1. Yao selects scope split option (A, B, or C)
2. Claude Code executes the split
3. Verify lotus-specific mechanisms have source quotes/locators
4. Demote or reassign non-lotus rows
