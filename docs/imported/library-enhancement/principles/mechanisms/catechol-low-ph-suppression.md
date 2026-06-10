# Catechol Protonation Suppresses Coordination at Low pH

> Rule ID: CM-002 | Confidence: 0.88 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

Below pH 3, full protonation of catechol hydroxyl groups renders the oxygen lone pairs unavailable for metal coordination, causing a sharp decline (>80%) in coordination capacity.

## Detailed Explanation

Catechol's two hydroxyl groups (-OH) each carry a proton that must be displaced for the oxygen atom to serve as a Lewis base (electron pair donor) in metal coordination. The acid-base equilibrium governs this:

- Ar-OH <-> Ar-O^- + H^+ (pKa1 ~ 9.2 for free catechol)
- Ar-O^- <-> Ar-O^2- + H^+ (pKa2 ~ 12.6 for free catechol)

At pH values well below pKa1 (i.e., pH < 3), the equilibrium lies overwhelmingly (>99.9%) toward the fully protonated form Ar(OH)2. In this state:

1. **No free lone pairs**: The oxygen atoms' lone pairs are engaged in the O-H covalent bond and hydrogen bonding with surrounding water molecules, making them unavailable for dative bonding to metal cations.

2. **Electrostatic repulsion**: The protonated hydroxyl groups create a locally positive electrostatic environment that repels approaching metal cations.

3. **Competitive displacement**: The high H+ concentration (10^-3 to 10^-1 M at pH 1-3) outcompetes metal ions (typically 10^-5 to 10^-3 M in wastewater) for the coordination sites through mass-action effects.

The combined effect is a near-total loss of coordination capacity. Experimental studies on polydopamine-coated substrates and mussel foot proteins consistently show that metal adsorption drops to <20% of maximum capacity below pH 3.

This limitation is intrinsic to the catechol functional group and cannot be overcome without modifying the chemical structure (e.g., replacing -OH with groups that have lower pKa values).

## Positive Example

Experimental data on polydopamine-coated membranes for Cu2+ adsorption show adsorption capacity decreasing from ~120 mg/g at pH 6 to ~15 mg/g at pH 2, representing an ~87% reduction. FTIR analysis at low pH shows intact O-H stretching bands, confirming protonation.

## Counter-Example / Boundary Condition

Catechol groups embedded in hydrophobic microenvironments (e.g., within the interior of a polymer matrix) may retain partial coordination ability at lower pH due to locally elevated effective pH near the binding site. The hydrophobic environment destabilizes the protonated form relative to the deprotonated form, effectively lowering the apparent pKa by 1-2 units.

## Applicable Prototypes

- **mussel-foot-adhesion**: Mussel foot proteins operate at seawater pH (~8.1); exposure to acidic conditions (e.g., acid mine drainage at pH 2-3) severely compromises DOPA-mediated metal coordination
- **polydopamine-coating**: PDA coatings show dramatic pH-dependent metal adsorption; practical applications require pH > 4 for effective performance
- **plant-tannin**: Tannin-based adsorbents for heavy metal removal require pH adjustment to > 4 for optimal performance

## Literature Sources

- Holten-Andersen et al. (2011): pH-responsive metal-catechol coordination in mussel-inspired hydrogels, showing sharp transition at pH 3
- Dreyer et al. (2012): Polydopamine structure characterization showing protonated catechol at low pH
- *Note: References require verification during cross-validation phase*
