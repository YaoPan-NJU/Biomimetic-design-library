# Redox-Sensitive Loss of Catechol Coordination Under Oxidizing Conditions

> Rule ID: CM-013 | Confidence: 0.85 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

Under oxidizing conditions (Eh > +0.3 V at neutral pH), catechol is irreversibly oxidized to ortho-quinone, permanently eliminating its metal coordination capacity.

## Detailed Explanation

Catechol is a redox-active functional group that participates in the following reversible oxidation:

**Catechol <-> ortho-Quinone + 2H+ + 2e-**

The formal redox potential depends on pH (Nernst equation):
E(pH) = E0 - (59 mV) * pH (at 25 degrees C)

At pH 7, E ~ +0.2 V vs. SHE; at pH 4, E ~ +0.38 V vs. SHE.

**Oxidant thresholds:**

| Oxidant | E0 (V vs SHE) | Can oxidize catechol at pH 7? |
|---------|---------------|-------------------------------|
| Dissolved O2 | +0.815 | Yes (slow without catalyst) |
| Cr(VI)/Cr(III) | +1.33 | Yes (rapid) |
| MnO2/Mn2+ | +1.23 | Yes (rapid) |
| Fe3+/Fe2+ | +0.77 | Yes (moderate) |
| H2O2 | +1.78 | Yes (very rapid) |
| Cl2/HOCl | +1.36 | Yes (very rapid) |

**Mechanism of capacity loss:**

1. **Direct coordination loss**: Quinone (C6H4O2) has two carbonyl oxygens instead of two hydroxyl oxygens. Carbonyl oxygens are much poorer Lewis bases than hydroxyl oxygens (pKa of conjugate acid: quinone ~ -6 vs. catechol ~ 9.2). Metal-quinone coordination is 2-3 orders of magnitude weaker than metal-catechol coordination.

2. **Secondary reactions**: Quinones undergo rapid Michael addition with nucleophiles (amines, thiols, other catechols), leading to covalent crosslinks and polymerization. This is the basis of PDA film formation (dopamine oxidation at pH 8.5 produces quinone intermediates that crosslink). Once crosslinked, the original catechol groups cannot be regenerated.

3. **Catalytic cycle**: Trace metals (Cu2+, Fe3+) can catalyze catechol oxidation through a redox cycle:
   - Catechol + M^(n+) -> semiquinone radical + M^(n-1)+
   - M^(n-1)+ + O2 -> M^(n+) + superoxide
   This cycle means that even low concentrations of catalytic metals can accelerate oxidation.

**Implications for different environments:**

- **Reducing environments** (anoxic groundwater, deep sediments): Catechol is stable; coordination capacity is maintained indefinitely.
- **Mildly oxidizing** (aerated surface water, Eh ~ +0.3 to +0.5 V): Slow oxidation over days to weeks; gradual capacity loss.
- **Strongly oxidizing** (Cr(VI)-contaminated water, chlorinated water): Rapid oxidation within minutes to hours; near-total capacity loss.

## Positive Example

Polydopamine-coated adsorbents show excellent Cr(VI) removal that is attributed to a combined reduction-adsorption mechanism: PDA's catechol groups reduce Cr(VI) to Cr(III), which is then coordinated by remaining catechol groups. However, this consumes catechol groups irreversibly, and the adsorbent cannot be regenerated for repeated Cr(VI) treatment cycles.

## Counter-Example / Boundary Condition

In mussel foot proteins, thiol-containing antioxidant molecules (cysteine-rich decapeptides) protect catechol groups from oxidation, maintaining the reduced catechol form even in aerated seawater. Biomimetic designs that incorporate antioxidant co-factors (e.g., co-grafting thiols or ascorbic acid) can extend catechol-based adsorbent lifetime in oxidizing conditions.

## Applicable Prototypes

- **mussel-foot-adhesion**: Natural DOPA is protected by antioxidant thiols in foot proteins; synthetic DOPA-analogues without protection are vulnerable
- **polydopamine-coating**: PDA inherently contains a mix of catechol, quinone, and crosslinked structures; residual catechol is the active coordination component
- **plant-tannin**: Tannin oxidation in alkaline, aerated conditions reduces chelation capacity

## Literature Sources

- Waite & Birkedal (2002): Redox cycling of DOPA in mussel adhesive
- Lee et al. (2007): Dopamine oxidation mechanism in PDA formation
- Shi et al. (2019): Cr(VI) reduction by polydopamine
- *Note: References require verification during cross-validation phase*
