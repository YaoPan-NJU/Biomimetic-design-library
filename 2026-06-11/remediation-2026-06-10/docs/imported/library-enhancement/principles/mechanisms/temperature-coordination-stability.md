# Temperature Effect on Exothermic Coordination Adsorption

> Rule ID: CM-009 | Confidence: 0.8 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

Most coordination-based adsorption processes are exothermic; above 50 degrees C, thermal disruption of metal-ligand bonds reduces adsorption capacity by approximately 10-30% per 10 degrees C increase, while moderate heating (20-40 degrees C) may improve kinetics.

## Detailed Explanation

The thermodynamics of coordination adsorption involves the equilibrium:

M^n+ (aq) + n L (adsorbent) <-> MLn (adsorbed complex)

The enthalpy change (delta-H) for this process is typically negative (exothermic) for the following reasons:

1. **Bond formation**: Formation of metal-ligand coordinate bonds releases energy (exothermic).
2. **Desolvation cost**: Stripping hydration water from the metal ion costs energy (endothermic), but this is typically less than the bond formation energy for strongly coordinating ligands.
3. **Net exothermicity**: The balance is typically delta-H ~ -20 to -60 kJ/mol for coordination adsorption.

**Van't Hoff relationship:**
ln(K2/K1) = -(delta-H/R) * (1/T2 - 1/T1)

For an exothermic reaction (delta-H < 0), increasing temperature (T2 > T1) decreases the equilibrium constant (K2 < K1), reducing adsorption capacity.

**Temperature regimes:**

| Temperature Range | Effect on Adsorption | Dominant Mechanism |
|---|---|---|
| 5-20 degrees C | Slow kinetics, high equilibrium capacity | Low diffusion rate limits kinetics |
| 20-40 degrees C | Optimal kinetics, near-maximum capacity | Balance of kinetics and thermodynamics |
| 40-60 degrees C | Moderate capacity decrease (~10-20%) | Thermal bond disruption begins |
| 60-80 degrees C | Significant capacity decrease (~20-40%) | Thermal energy comparable to coordination bond energy |
| >80 degrees C | Major capacity loss (>40%) | Coordination complex destabilization |

**Kinetics vs. thermodynamics trade-off:**
- Below 40 degrees C: Increasing temperature accelerates pore diffusion and reaction kinetics, so the initial adsorption rate increases even though equilibrium capacity slightly decreases.
- Above 50 degrees C: The thermodynamic penalty dominates, and both the rate and capacity decrease.

**Exceptions:** Some coordination reactions are endothermic (delta-H > 0), driven by the entropy gain from displacing ordered water molecules. These show increased adsorption with temperature. This is more common for large, highly hydrated metal ions where the desolvation entropy is large.

## Positive Example

Chitosan-Cu2+ adsorption at pH 5 shows a maximum adsorption capacity of ~150 mg/g at 25 degrees C, decreasing to ~110 mg/g at 45 degrees C and ~75 mg/g at 65 degrees C. However, the time to reach equilibrium decreases from ~6 hours at 15 degrees C to ~2 hours at 35 degrees C.

## Counter-Example / Boundary Condition

Alginate-Ca2+ egg-box crosslinking shows increased stability with moderate heating (up to 40 degrees C) because the crosslinking reaction is entropically driven (release of ordered water). Similarly, MOF-based adsorption may show endothermic behavior if the adsorption involves displacement of strongly bound solvent molecules from the pores.

## Applicable Prototypes

- **chitosan**: Amino-metal coordination is exothermic; optimal performance at 20-40 degrees C
- **alginate**: Carboxyl-metal coordination is generally exothermic, though egg-box crosslinking has complex thermodynamics
- **mussel-foot-adhesion**: Catechol-metal coordination in natural mussel habitat (5-20 degrees C) is well-adapted to moderate temperatures
- **polydopamine-coating**: PDA-metal coordination follows typical exothermic adsorption pattern
- **plant-tannin**: Tannin-metal chelation is exothermic
- **chlorella-cell-wall**: Mixed functional group coordination is exothermic overall

## Literature Sources

- Varma et al. (2004): Temperature-dependent adsorption of heavy metals on chitosan
- Ho & McKay (1999): Pseudo-second-order kinetics and temperature effects
- *Note: References require verification during cross-validation phase*
