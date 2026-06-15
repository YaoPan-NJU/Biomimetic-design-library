# Alkali/Alkaline Earth Competitive Saturation of Coordination Sites

> Rule ID: CM-018 | Confidence: 0.8 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

When background alkali and alkaline earth ions exceed 100x the target heavy metal concentration, mass-action effects saturate coordination sites, reducing heavy metal uptake by 30-70%, with carboxyl-based coordination most affected.

## Detailed Explanation

Natural waters and industrial wastewaters invariably contain high concentrations of background electrolytes:

| Water Type | Na+ (mM) | K+ (mM) | Ca2+ (mM) | Mg2+ (mM) | Total Ions |
|-----------|----------|---------|-----------|-----------|------------|
| Freshwater | 0.1-1 | 0.01-0.1 | 0.5-3 | 0.2-1 | 1-5 mM |
| Brackish water | 5-50 | 0.5-5 | 2-10 | 1-5 | 10-70 mM |
| Seawater | 470 | 10 | 10 | 53 | ~550 mM |
| Industrial brine | 1000+ | 10-100 | 50-200 | 50-200 | >1000 mM |

Meanwhile, target heavy metals are typically at 0.001-0.1 mM (0.1-10 ppm). The concentration ratio of background:target ions ranges from 10:1 in freshwater to >10000:1 in seawater.

**Mass-action competition:**

The fractional occupancy of a coordination site by metal M is:

theta_M = K_M * [M] / (1 + sum(K_i * [i]))

Even with K(heavy metal) >> K(Na+ or Ca2+), the product K_i * [i] for background ions can be comparable to or exceed K_M * [M] when [i] >> [M].

**Example calculation:**
- Target: Pb2+ at 0.01 mM, K(Pb) = 10^6
- Background: Ca2+ at 10 mM, K(Ca) = 10^2
- Na+ at 100 mM, K(Na) = 10^0

Occupancy products:
- Pb2+: 10^6 * 0.01 = 10^4
- Ca2+: 10^2 * 10 = 10^3
- Na+: 10^0 * 100 = 10^2

Pb2+ fractional occupancy = 10^4 / (1 + 10^4 + 10^3 + 10^2) ~ 90%

This seems acceptable, but in practice:
1. Multiple background species accumulate
2. Binding constants have broader distributions than single-value estimates
3. Some sites have anomalously high Ca2+/Na+ affinity

The net result is 10-30% site occupation by background ions, reducing heavy metal capacity.

**Differential vulnerability by functional group:**

| Functional Group | Typical K(heavy)/K(Ca) Ratio | Vulnerability |
|---|---|---|
| Thiol (for Hg2+) | >10^15 | Minimal (<1% loss) |
| Catechol (for Cu2+) | ~10^5 | Low-moderate (10-20% loss) |
| Amino (for Cu2+) | ~10^3 | Moderate (20-40% loss) |
| Carboxyl (for Pb2+) | ~10^2 | High (30-60% loss) |

The vulnerability ranking reflects the intrinsic selectivity. Carboxyl groups, with the lowest selectivity ratio, are most vulnerable. This is particularly relevant for alginate-based adsorbents in brackish or seawater applications.

**Mitigation strategies:**

1. **Pre-treatment**: Reduce background electrolyte concentration by dilution or partial desalination
2. **Functional group selection**: Use catechol or thiol groups instead of carboxyl for saline conditions
3. **Increased adsorbent dose**: Compensate for capacity loss with more adsorbent
4. **pH optimization**: At higher pH, heavy metal coordination is stronger relative to background ion competition
5. **Pre-saturation**: Pre-load adsorbent with a benign ion (e.g., Na+) that is easily displaced by heavy metals

## Positive Example

Alginate-based adsorbents for Cd2+ removal from brackish water (5000 ppm TDS) show 60% capacity reduction compared to freshwater. By switching to catechol-functionalized adsorbents (mussel-inspired), the capacity reduction is only 25% under the same conditions, demonstrating the advantage of higher-selectivity functional groups.

## Counter-Example / Boundary Condition

In ion-exchange resins with very high functional group density (>5 meq/g), the local concentration of coordination sites can exceed the background electrolyte concentration even in seawater. In such cases, the selectivity coefficient (rather than mass-action competition) dominates, and background ion interference is reduced. This is why synthetic ion-exchange resins often outperform natural biopolymer adsorbents in saline conditions.

## Applicable Prototypes

- **alginate**: Carboxyl groups most vulnerable to background ion competition
- **chitosan**: Amino groups moderately vulnerable
- **chlorella-cell-wall**: Mixed functional groups with moderate vulnerability
- **cellulose-nanocrystal**: Carboxyl groups vulnerable, though TEMPO-oxidized CNC may have higher selectivity due to surface crystallinity

## Literature Sources

- Volesky & Holan (1995): Biosorption in the presence of competing ions
- Schiewer & Volesky (1997): Ionic strength and competition effects on biosorption
- Febrianto et al. (2008): Competitive adsorption in multi-metal systems with background electrolytes
- *Note: References require verification during cross-validation phase*
