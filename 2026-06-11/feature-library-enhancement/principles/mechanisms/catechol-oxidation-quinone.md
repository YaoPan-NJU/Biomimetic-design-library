# Catechol Oxidation to Quinone at Alkaline pH

> Rule ID: CM-003 | Confidence: 0.85 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

Above pH 8, catechol undergoes autoxidation to ortho-quinone, irreversibly destroying the bidentate coordination capability and eliminating metal chelation capacity.

## Detailed Explanation

Catechol is susceptible to oxidation via a two-electron, two-proton process:

Catechol (Ar(OH)2) -> ortho-Quinone (Ar(=O)2) + 2H+ + 2e-

The oxidation potential of this reaction is pH-dependent. At neutral pH, the standard redox potential is approximately +0.5 V (vs. SHE), but it decreases by approximately 59 mV per pH unit increase (Nernst equation), making catechol progressively easier to oxidize at higher pH.

Key mechanistic details:

1. **Autoxidation pathway**: At pH > 8, dissolved oxygen (E0 = +0.815 V for O2/H2O at pH 7) becomes thermodynamically capable of oxidizing catechol. The reaction is catalyzed by trace transition metals (especially Cu2+ and Fe3+), which form redox-active complexes with catechol that facilitate electron transfer to O2.

2. **Quinone structure**: The resulting ortho-quinone has two carbonyl groups (C=O) in place of the two hydroxyl groups. While quinones can weakly interact with metals through the carbonyl oxygens, the coordination strength is 2-3 orders of magnitude weaker than catechol-metal bidentate coordination.

3. **Irreversibility**: The quinone form is prone to further reactions -- Michael addition with nucleophiles (amines, thiols), polymerization, and ring-opening. These secondary reactions make the oxidation effectively irreversible under environmental conditions.

4. **Kinetics**: Oxidation rate increases approximately 10-fold per pH unit above pH 8. At pH 10, catechol oxidation in aerated solution occurs within minutes to hours. At pH 8-9, the timescale is hours to days.

5. **Implications for PDA**: Polydopamine synthesis itself exploits catechol oxidation at pH 8.5 (Tris buffer). The resulting PDA film contains a mixture of residual catechol, quinone, and crosslinked indole structures. The fraction of intact catechol groups decreases with prolonged alkaline exposure.

## Positive Example

Polydopamine coatings prepared at pH 8.5 retain approximately 30-40% of their catechol groups in the reduced form. These residual catechols still provide significant metal coordination capacity. However, extended exposure to pH > 9 (e.g., in alkaline wastewater) progressively oxidizes the remaining catechols, reducing adsorption capacity over time.

## Counter-Example / Boundary Condition

In anaerobic (oxygen-free) environments, catechol oxidation is greatly suppressed even at pH > 8. Similarly, in the presence of reducing agents (ascorbic acid, sodium borohydride), quinone can be reduced back to catechol, partially restoring coordination capacity. Mussel foot proteins protect catechol groups from oxidation through thiol-containing antioxidant co-factors (e.g., cysteine-rich decapeptides).

## Applicable Prototypes

- **mussel-foot-adhesion**: Natural mussel adhesion operates at seawater pH ~8.1, near the oxidation threshold; mussels mitigate this through antioxidant thiol groups in foot proteins
- **polydopamine-coating**: PDA inherently contains oxidized quinone structures; prolonged alkaline exposure further reduces catechol content
- **plant-tannin**: Tannin-rich materials degrade in alkaline, aerated conditions through catechol oxidation

## Literature Sources

- Lee et al. (2007): Polydopamine deposition mechanism involving catechol oxidation at pH 8.5
- Herlinger et al. (1995): Autoxidation kinetics of catechol in alkaline solution
- Yu et al. (2014): Quantification of catechol vs quinone content in PDA films
- *Note: References require verification during cross-validation phase*
