# Carboxyl pH-Dependent Selectivity Shift Between Hard and Borderline Metals

> Rule ID: CM-022 | Confidence: 0.78 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

In the transitional pH range 3-5, carboxyl groups exhibit a selectivity shift: partially protonated sites near pKa prefer hard metals (Pb2+, Fe3+), while fully deprotonated sites at pH 4.5-5 broaden selectivity to borderline metals (Cu2+, Zn2+, Ni2+, Cd2+).

## Detailed Explanation

The pH range 3-5 is the critical transition zone for carboxyl-based adsorbents, where the protonation state shifts from fully protonated to fully deprotonated. This transition creates distinct metal selectivity regimes:

**Regime 1: pH 3-4 (near pKa, partially deprotonated)**

At pH values close to the carboxyl pKa (3.4-4.5 depending on the specific carboxyl group), the surface contains a mixture of -COOH and -COO- sites. In this regime:

1. **Proton displacement mechanism**: Hard metal ions with high charge density (Pb2+, Fe3+) can displace the remaining proton from -COOH:
   Pb2+ + R-COOH -> R-COO-Pb+ + H+
   This is thermodynamically favorable for Pb2+ because the Pb-O bond is strong enough to compensate for the energy cost of proton displacement.

2. **Selectivity for hard metals**: Hard metals (high charge density, small ionic radius relative to charge) have stronger electrostatic interactions with the carboxyl oxygen, enabling them to compete more effectively with protons for partially protonated sites.

3. **Pb2+ advantage**: Pb2+ (ionic radius 1.19 A, charge +2) has a particularly high affinity for carboxyl groups because its large size provides good orbital overlap with the carboxylate oxygen, and its electron configuration (6s2 lone pair) enables additional covalent character in the Pb-O bond.

**Regime 2: pH 4.5-5 (above pKa, fully deprotonated)**

Once all carboxyl groups are deprotonated to -COO-, the selectivity broadens:

1. **No proton competition**: All sites are available as -COO- ligands without the need to displace protons.
2. **Broader metal compatibility**: Borderline metals (Cu2+, Zn2+, Ni2+, Cd2+) that cannot efficiently displace protons from -COOH can now coordinate with the freely available -COO- sites.
3. **Irving-Williams ordering**: Selectivity among divalent metals follows the Irving-Williams series: Cu2+ > Ni2+ > Zn2+ > Cd2+ > Mn2+.

**Selectivity ratio (Pb2+ / Cu2+) vs pH:**

| pH | Pb2+/Cu2+ Selectivity | Explanation |
|----|----------------------|-------------|
| 3.0 | 5-10:1 | Pb2+ displaces protons much more effectively |
| 3.5 | 3-5:1 | More sites deprotonated, Cu2+ gaining access |
| 4.0 | 2-3:1 | Most sites deprotonated |
| 4.5 | 1-2:1 | Nearly all sites deprotonated |
| 5.0+ | ~1:1 (Irving-Williams favors Cu2+) | No proton effects, Cu2+ slightly preferred |

**Practical application -- selective Pb2+ separation:**

This pH-dependent selectivity shift can be exploited for selective Pb2+ recovery from mixed-metal solutions:

1. Adjust solution to pH 3.5-4.0
2. Contact with alginate or carboxyl-functional adsorbent
3. Pb2+ is preferentially adsorbed (selectivity 3-5x over Cu2+, Zn2+, Cd2+)
4. Remaining metals pass through
5. Elute Pb2+ with dilute acid (pH 2)
6. For remaining metals, raise pH to 5-6 and re-adsorb on fresh adsorbent

## Positive Example

Alginate beads used for selective Pb2+ separation from a Pb2+/Cu2+/Zn2+ mixture at pH 3.8 achieve Pb2+/Cu2+ and Pb2+/Zn2+ selectivity ratios of ~4:1 and ~6:1, respectively. At pH 5.5, the same alginate shows nearly equal adsorption of all three metals (selectivity ratios ~1:1), confirming the pH-dependent selectivity shift.

## Counter-Example / Boundary Condition

For metals that form insoluble hydroxides at low pH (Fe3+ precipitates as Fe(OH)3 above pH 3), the selectivity shift cannot be fully exploited because precipitation interferes with adsorption measurements. Additionally, for very high carboxyl density adsorbents where all sites are easily accessible, the transition between regimes is sharper (narrower pH window), making precise pH control more critical.

## Applicable Prototypes

- **alginate**: The pH 3-5 transition is practically exploitable for selective Pb2+ separation; G-block and M-block carboxyl groups have slightly different pKa values, broadening the transition zone
- **chlorella-cell-wall**: Uronic acid and protein carboxyl groups show similar pH-dependent selectivity
- **cellulose-nanocrystal**: TEMPO-oxidized CNC surface carboxyl groups exhibit this transition; the crystalline surface may provide more uniform site environments, sharpening the selectivity shift

## Literature Sources

- Davis et al. (2003): pH-dependent metal selectivity of alginate carboxyl groups
- Schiewer & Volesky (1995): Proton-metal exchange mechanisms in carboxyl-containing biosorbents
- Pagnanelli et al. (2000): Selectivity shifts in multi-metal biosorption at varying pH
- *Note: References require verification during cross-validation phase*
