# Irving-Williams Stability Series Governs Divalent Metal Selectivity

> Rule ID: CM-008 | Confidence: 0.9 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

For all common biological ligands (N-donor and O-donor), divalent metal complex stability follows the Irving-Williams series: Mn2+ < Fe2+ < Co2+ < Ni2+ < Cu2+ > Zn2+, with Cu2+ consistently forming the most stable complexes.

## Detailed Explanation

The Irving-Williams series (1953) describes the universal order of stability constants for divalent first-row transition metal complexes with any given ligand:

**Mn2+ < Fe2+ < Co2+ < Ni2+ < Cu2+ > Zn2+**

This order is independent of the ligand -- it applies equally to amino, carboxyl, catechol, and other N/O-donor ligands. The physical basis has two components:

1. **Crystal field stabilization energy (CFSE)**: Moving from Mn2+ (d5, zero CFSE) through the series to Ni2+ (d8, maximum octahedral CFSE), the crystal field stabilization energy increases, strengthening metal-ligand bonds. Cu2+ (d9) achieves anomalously high stability through Jahn-Teller distortion, which creates an elongated octahedral geometry with four short, strong equatorial bonds.

2. **Effective nuclear charge**: The effective nuclear charge increases across the period as d-electrons are added (poor shielding), causing a decrease in ionic radius from Mn2+ (0.83 A) to Zn2+ (0.74 A). Smaller ions have higher charge density and form stronger electrostatic interactions with ligand donor atoms.

**Quantitative example** (log K1 for ethylenediamine, a bidentate N-donor):
- Mn2+: 2.7
- Fe2+: 4.3
- Co2+: 5.9
- Ni2+: 7.5
- Cu2+: 10.6
- Zn2+: 5.7

**Implications for competitive adsorption:**

In a multi-metal solution with equimolar concentrations of divalent metals, an adsorbent with amino or carboxyl coordination sites will preferentially adsorb Cu2+ first, then Ni2+, then Zn2+/Co2+, then Mn2+/Fe2+. This has critical implications for:

- **Selectivity design**: If the target pollutant is Cu2+, amino/carboxyl adsorbents are inherently selective
- **Displacement risk**: If the target is Zn2+ or Cd2+, pre-adsorbed metals may be displaced by subsequently introduced Cu2+ or Ni2+
- **Regeneration strategy**: Weaker-binding metals (Mn2+, Fe2+) can be selectively eluted first, while Cu2+ requires stronger eluents

**The Zn2+ anomaly**: Zn2+ (d10, zero CFSE) deviates below the trend despite having the smallest ionic radius. This is because it lacks crystal field stabilization, relying solely on electrostatic interactions.

## Positive Example

Chitosan in mixed-metal wastewater (containing Cu2+, Ni2+, Zn2+, Cd2+ at 50 ppm each) shows selective adsorption order: Cu2+ > Ni2+ > Zn2+ > Cd2+, consistent with Irving-Williams predictions. Cu2+ can displace previously adsorbed Cd2+ from chitosan amino sites.

## Counter-Example / Boundary Condition

The Irving-Williams series applies only to divalent first-row transition metals with N/O-donor ligands. For S-donor ligands (thiol), the selectivity order is different: Hg2+ >> Cd2+ > Pb2+ > Cu2+ > Zn2+ (HSAB-driven). Also, trivalent metals (Fe3+, Cr3+) form much stronger complexes than any divalent metal due to higher charge, and do not follow this series.

## Applicable Prototypes

- **chitosan**: Amino group coordination follows Irving-Williams series
- **alginate**: Carboxyl coordination follows Irving-Williams series
- **mussel-foot-adhesion**: Catechol-O-donor coordination follows Irving-Williams for divalent metals
- **polydopamine-coating**: Catechol and amino coordination in PDA follows Irving-Williams
- **plant-tannin**: Catechol-type O-donor coordination follows Irving-Williams
- **chlorella-cell-wall**: Mixed amino/carboxyl coordination follows Irving-Williams

## Literature Sources

- Irving & Williams (1953): Original paper establishing the stability series
- Burgess (1978): Metal Ions in Solution -- thermodynamic basis of the series
- Hancock & Martell (1989): Ligand design and Irving-Williams selectivity
- *Note: References require verification during cross-validation phase*
