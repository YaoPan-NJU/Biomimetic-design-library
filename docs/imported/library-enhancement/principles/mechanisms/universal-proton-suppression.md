# Universal Proton Suppression of All Coordination Below pH 3

> Rule ID: CM-019 | Confidence: 0.9 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

At pH < 3, excess H+ ions outcompete all metal cations for coordination sites on all functional groups, effectively suppressing coordination-based adsorption of heavy metals.

## Detailed Explanation

Below pH 3, the H+ concentration exceeds 10^-3 M, which is comparable to or higher than typical heavy metal concentrations in wastewater (10^-5 to 10^-3 M). This creates overwhelming proton competition for all coordination functional groups:

**Protonation state of all functional groups at pH < 3:**

| Functional Group | pKa | State at pH 3 | State at pH 2 | State at pH 1 | Coordination Ability |
|---|---|---|---|---|---|
| Carboxyl (-COOH) | 3.5-4.5 | ~80% protonated | ~97% protonated | >99% protonated | Severely suppressed |
| Catechol (-OH) | ~9.2 (free) | ~100% protonated | 100% protonated | 100% protonated | Essentially zero |
| Amino (-NH2) | ~6.5 (chitosan) | ~99.9% protonated | 100% protonated | 100% protonated | Zero (for metals) |
| Thiol (-SH) | ~8-10 | ~100% protonated | 100% protonated | 100% protonated | Reduced but not zero |

**Mechanism of suppression:**

1. **Thermodynamic displacement**: For the equilibrium M-L + H+ <-> M^2+ + H-L, the extremely high H+ concentration drives the equilibrium toward the right (protonated ligand + free metal), displacing metal ions from coordination sites.

2. **Kinetic competition**: At [H+] > [M^2+] by 10-1000x, protons reach and occupy coordination sites faster than metal ions, creating a kinetic barrier to metal coordination even if the metal-ligand bond would be thermodynamically preferred.

3. **Surface charge effects**: Protonation of all functional groups creates a uniformly positively charged surface that electrostatically repels approaching metal cations, adding an electrostatic barrier to coordination.

**What still works at pH < 3:**

Not all adsorption mechanisms are suppressed at low pH. The following remain effective:

1. **Electrostatic anion adsorption**: Protonated amino groups (-NH3+) strongly adsorb anionic species (Cr2O7^2-, HCrO4^-, AsO4^3-, anionic dyes). This is actually the dominant mechanism for Cr(VI) removal by chitosan at pH 2-3.

2. **Ion exchange**: Mineral-based adsorbents (hydroxyapatite, CaCO3) can exchange structural Ca2+ for heavy metals regardless of pH, though the exchange rate may slow in acid due to mineral dissolution.

3. **Physical adsorption**: Van der Waals and pore-filling mechanisms in high-surface-area materials (activated carbon, MOFs) are largely pH-independent.

4. **Thiol-metal coordination (partial)**: Thiol groups, due to their extremely high soft metal selectivity, can retain some Hg2+ coordination even at pH 2. The Hg-S bond (log K ~ 30-50) is so strong that even with proton competition, some coordination persists.

## Positive Example

Chitosan at pH 2 achieves Cr(VI) removal of 80-200 mg/g via electrostatic adsorption of HCrO4^- on protonated amino groups. However, Cu2+ and Pb2+ adsorption at pH 2 is <5 mg/g, confirming that coordination is suppressed while electrostatic anion adsorption is enhanced.

## Counter-Example / Boundary Condition

Thiol-functionalized adsorbents can maintain partial Hg2+ adsorption (20-40% of maximum capacity) even at pH 1-2 due to the extraordinary Hg-S bond strength. This makes thiol-based adsorbents uniquely suited for Hg removal from strongly acidic industrial waste (e.g., chlor-alkali process effluent at pH 1-2).

## Applicable Prototypes

- **chitosan**: At pH < 3, switches from metal coordination to anion electrostatic adsorption
- **alginate**: Carboxyl coordination essentially eliminated; alginate may dissolve below pH 3
- **mussel-foot-adhesion**: Catechol coordination suppressed; natural mussels do not encounter pH < 3
- **polydopamine-coating**: Catechol coordination suppressed; PDA film may partially dissolve
- **plant-tannin**: Catechol coordination suppressed; tannin may leach
- **chlorella-cell-wall**: Mixed functional groups all protonated
- **cellulose-nanocrystal**: Carboxyl coordination suppressed; cellulose backbone stable
- **sulfate-reducing-bacteria**: Sulfide precipitation still possible if H2S is present (not oxidized)

## Literature Sources

- Guibal (2004): pH effects on chitosan metal adsorption -- complete suppression below pH 3
- Volesky (2007): Biosorption pH dependence across multiple functional groups
- *Note: References require verification during cross-validation phase*
