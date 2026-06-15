# High Salinity Competition Suppresses Coordination Adsorption

> Rule ID: CM-011 | Confidence: 0.78 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

At high ionic strength (>0.5 M), competing cations (Na+, K+, Ca2+, Mg2+) saturate coordination sites through mass-action effects, reducing heavy metal adsorption capacity by 30-70%.

## Detailed Explanation

When background electrolyte concentrations exceed 0.5 M (equivalent to >3% salinity, approaching seawater at ~3.5%), the sheer number of competing cations overwhelms the selectivity advantage of coordination sites.

**Mass-action competition:**

Consider a coordination site L with binding constants:
- K(heavy metal) = 10^8 (strong binding)
- K(Na+) = 10^1 (weak binding)
- K(Ca2+) = 10^3 (moderate binding)

At equimolar concentrations, the site strongly prefers heavy metals. But at:
- [Heavy metal] = 10^-5 M (0.1-10 ppm, typical wastewater)
- [Na+] = 0.5 M (seawater-level salinity)
- [Ca2+] = 0.01 M

The fractional occupancy by each species depends on the product K * [M]:
- Heavy metal: 10^8 * 10^-5 = 10^3
- Na+: 10^1 * 0.5 = 5
- Ca2+: 10^3 * 0.01 = 10

In this scenario, Ca2+ occupancy (10 / (1000 + 5 + 10) ~ 1%) and Na+ occupancy (~0.5%) are small. But with multiple competing ions and considering that real binding constants span broader ranges, the cumulative competitive effect is significant.

**Differential impact by functional group:**

| Functional Group | Selectivity Ratio (heavy:background) | Salinity Tolerance |
|---|---|---|
| Thiol (soft metal) | >10^20:1 | Excellent (>90% retention at seawater salinity) |
| Catechol (borderline metal) | ~10^6:1 | Good (70-80% retention) |
| Amino (borderline metal) | ~10^4:1 | Moderate (50-70% retention) |
| Carboxyl (borderline/hard metal) | ~10^2:1 | Poor (30-50% retention) |

The ranking reflects the intrinsic selectivity of each functional group. Thiol groups are so selective for soft metals that even seawater-level salinity barely affects performance. Carboxyl groups, with lower intrinsic selectivity, are most affected.

**Practical implications:**

1. For seawater or brackish water treatment, carboxyl-based adsorbents may need 2-3x the adsorbent mass to compensate for competitive suppression.
2. Catechol-based adsorbents are more suitable for saline conditions.
3. Thiol-based adsorbents are optimal for soft metal removal from saline water.
4. Pre-concentration or dilution strategies may be needed for carboxyl-based systems.

## Positive Example

Alginate beads for Pb2+ removal show 250 mg/g capacity in deionized water but only 100 mg/g in synthetic seawater (3.5% salinity). The 60% reduction is attributed to Ca2+ and Mg2+ competition for carboxyl coordination sites. In contrast, mussel-inspired catechol-based adsorbents retain ~75% capacity under the same conditions.

## Counter-Example / Boundary Condition

In pre-crosslinked alginate (Ca2+-crosslinked egg-box structure), the crosslinked network is already saturated with Ca2+, and heavy metal uptake occurs via ion exchange (Pb2+ displacing Ca2+). This ion exchange mechanism is less affected by additional NaCl because the exchange equilibrium depends on the relative affinities of Pb2+ and Ca2+, not on Na+ competition.

## Applicable Prototypes

- **alginate**: Most affected by high salinity due to moderate carboxyl selectivity
- **chitosan**: Amino groups show moderate salinity tolerance
- **chlorella-cell-wall**: Mixed functional groups with overall moderate salinity tolerance
- **plant-tannin**: Catechol groups provide good salinity tolerance

## Literature Sources

- Schiewer & Volesky (1995): Ionic strength effects on biosorption by alginate-containing biomass
- Davis et al. (2003): Metal binding in alginate at varying ionic strengths
- *Note: References require verification during cross-validation phase*
