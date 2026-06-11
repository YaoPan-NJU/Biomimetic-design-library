# Amino Coordination Selectivity for Transition Metals

> Rule ID: CM-015 | Confidence: 0.85 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

Amino groups coordinate preferentially with borderline metals per HSAB classification, with selectivity Cu2+ > Ni2+ > Co2+ > Zn2+ > Cd2+ > Mn2+ following the Irving-Williams series.

## Detailed Explanation

The amino group (-NH2) is a borderline Lewis base (intermediate hardness). Per Pearson's HSAB principle, borderline bases preferentially coordinate with borderline acids. Among divalent transition metals:

**HSAB classification of common metals:**
- **Hard**: Ca2+, Mg2+, Fe3+ (but Fe3+ is hard and high-charge, so it binds strongly to all ligands)
- **Borderline**: Cu2+, Ni2+, Co2+, Zn2+, Pb2+
- **Soft**: Cd2+, Hg2+, Ag+

Amino groups show strongest coordination with borderline metals, and within the borderline group, selectivity follows the Irving-Williams series.

**Quantitative binding constants for chitosan amino groups (log K1):**

| Metal | log K1 (chitosan) | Irving-Williams Position |
|-------|-------------------|--------------------------|
| Cu2+ | 8-10 | Highest |
| Ni2+ | 6-8 | Second |
| Co2+ | 5-7 | Third |
| Zn2+ | 5-6 | Fourth |
| Cd2+ | 4-5 | Fifth (borderline-soft) |
| Mn2+ | 3-4 | Lowest |

**Structural basis:**

1. **Cu2+-amino**: Cu2+ forms 4-coordinate square planar or 5/6-coordinate Jahn-Teller distorted octahedral complexes. With chitosan, Cu2+ typically coordinates 2-4 amino groups from adjacent glucosamine units plus water molecules, achieving very stable complexes.

2. **Ni2+-amino**: Ni2+ prefers octahedral geometry and coordinates up to 6 amino groups. The chitosan chain provides sufficient flexibility for this.

3. **Zn2+-amino**: Zn2+ (d10, no CFSE) prefers tetrahedral geometry with 4 amino groups. The lower coordination number and lack of CFSE result in weaker binding than Cu2+ or Ni2+.

**Selectivity in practice:**

In a mixed-metal solution containing Cu2+, Ni2+, Zn2+, and Cd2+ (each at 50 ppm), chitosan at pH 6 will adsorb metals in the order: Cu2+ > Ni2+ > Zn2+ > Cd2+. If Cu2+ is introduced after the other metals are already adsorbed, it can displace Ni2+, Zn2+, and Cd2+ from amino coordination sites.

**Separation applications:**

This selectivity can be exploited for sequential metal recovery:
1. Load chitosan with mixed metals at pH 6
2. Elute with dilute acid (pH 3): Cd2+ and Zn2+ elute first (weakest binding)
3. Elute with stronger acid (pH 1): Ni2+ elutes
4. Elute with complexing agent (EDTA): Cu2+ elutes last (strongest binding)

## Positive Example

Chitosan beads used for selective Cu2+ recovery from electroplating wastewater (containing Cu2+, Ni2+, Zn2+) achieve Cu2+/Ni2+ selectivity ratios of 5-10:1 at pH 6. Sequential elution with decreasing pH enables recovery of each metal in a relatively pure fraction.

## Counter-Example / Boundary Condition

At very high metal loading (approaching saturation of all amino sites), the selectivity diminishes because all available sites are occupied regardless of binding preference. Additionally, at pH < 5, amino groups protonate and coordination selectivity becomes irrelevant as all metal coordination is suppressed.

## Applicable Prototypes

- **chitosan**: C2-amino group is the primary metal coordination site; selectivity follows Irving-Williams series
- **chlorella-cell-wall**: Protein amino groups (lysine, arginine) show similar borderline metal preference
- **mycelium**: Fungal chitosan and cell wall protein amino groups follow similar selectivity

## Literature Sources

- Monteiro & Airoldi (1999): Thermodynamics of chitosan-metal coordination
- Guibal (2004): Metal selectivity on chitosan
- Wan Ngah & Hanafiah (2008): Competitive adsorption of heavy metals on chitosan
- *Note: References require verification during cross-validation phase*
