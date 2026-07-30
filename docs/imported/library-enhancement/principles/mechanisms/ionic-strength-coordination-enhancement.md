# Ionic Strength Enhancement of Coordination at Moderate Salinity

> Rule ID: CM-010 | Confidence: 0.75 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

At moderate ionic strength (I = 0.01-0.5 M), charge screening reduces electrostatic repulsion between similarly-charged coordination sites, potentially increasing adsorption capacity by 10-20% compared to deionized water.

## Detailed Explanation

The effect of ionic strength on coordination adsorption involves competing mechanisms:

**Mechanism 1: Activity coefficient effect (Debye-Huckel theory)**

The activity coefficient of charged species decreases with increasing ionic strength according to the extended Debye-Huckel equation:

log(gamma) = -A * z^2 * sqrt(I) / (1 + B * a * sqrt(I))

For the coordination reaction M^n+ + L^m- <-> ML^(n-m), the thermodynamic equilibrium constant K is related to the concentration-based constant Kc by:

K = Kc * (gamma_ML / (gamma_M * gamma_L))

As ionic strength increases, the activity coefficients of charged species decrease, which can shift the equilibrium toward the (less charged or neutral) complex, effectively increasing Kc.

**Mechanism 2: Charge screening**

In adsorbents with high density of charged functional groups (e.g., alginate with many -COO- groups, chitosan at pH < 6.5 with many -NH3+ groups), electrostatic repulsion between like-charged sites limits the accessibility of coordination sites. Added electrolyte screens this repulsion:

- Debye length (kappa^-1) at I = 0.001 M: ~10 nm
- Debye length at I = 0.01 M: ~3 nm  
- Debye length at I = 0.1 M: ~1 nm
- Debye length at I = 0.5 M: ~0.4 nm

Shorter Debye lengths mean that charged sites are more effectively screened, allowing metal ions to approach and coordinate without electrostatic barrier.

**Mechanism 3: Polymer conformation**

For polyelectrolyte adsorbents (alginate, chitosan), ionic strength controls chain conformation:
- Low I: Extended chains (electrostatic repulsion), open structure, accessible sites
- Moderate I: Moderately collapsed chains, some sites become more concentrated locally
- High I: Collapsed chains, reduced site accessibility

The net effect at moderate ionic strength (0.01-0.5 M) is typically a modest increase (10-20%) in adsorption capacity, primarily due to charge screening. The effect is most pronounced for:
- Highly charged adsorbents (high functional group density)
- Multivalent metal ions (higher charge = stronger Debye-Huckel effect)
- Rigid substrates where polymer conformation changes are minimal

## Positive Example

Polydopamine-coated substrates show 10-15% higher Cu2+ adsorption capacity in 0.1 M NaCl compared to deionized water at the same pH. The ionic strength screens repulsion between partially oxidized (negatively charged) quinone sites and incoming Cu2+ ions.

## Counter-Example / Boundary Condition

For low-charge-density adsorbents (sparse functional group coverage), the ionic strength enhancement effect is negligible because there is minimal electrostatic repulsion to screen. In such cases, any ionic strength effect is dominated by competitive binding of Na+/K+ ions, which is always negative.

## Applicable Prototypes

- **mussel-foot-adhesion**: DOPA-containing proteins operate in seawater (I ~ 0.7 M); moderate ionic strength is near-optimal
- **polydopamine-coating**: PDA films have mixed positive/negative charges; ionic strength screens internal repulsion
- **alginate**: Highly charged polyanion; moderate salt concentrations screen inter-chain repulsion
- **chitosan**: Polycation at acidic pH; salt screens amino-amino repulsion

## Literature Sources

- Record et al. (1978): Ion effects on polyelectrolyte-ligand interactions
- van de Steeg et al. (1992): Ionic strength effects on polyelectrolyte adsorption
- *Note: References require verification during cross-validation phase*
