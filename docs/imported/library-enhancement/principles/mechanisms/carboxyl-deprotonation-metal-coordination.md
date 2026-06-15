# Carboxyl Deproteination Threshold for Metal Coordination

> Rule ID: CM-006 | Confidence: 0.87 | Last validated: 2026-06-05 (LLM draft, pending literature validation)

## Core Claim

Above pH ~4, carboxyl groups deprotonate from -COOH to -COO-, becoming effective ligands for heavy metal cation coordination.

## Detailed Explanation

Carboxyl groups (-COOH) are weak acids with pKa values that depend on the chemical environment:

- Alginate guluronic acid (G-block): pKa ~ 3.6
- Alginate mannuronic acid (M-block): pKa ~ 3.4
- Cellulose nanocrystal surface -COOH (TEMPO-oxidized): pKa ~ 3.5-4.5
- Chlorella cell wall protein -COOH: pKa ~ 3.8-4.5

The deprotonation equilibrium is:

R-COOH <-> R-COO^- + H+

Below the pKa, the carboxyl is protonated and neutral, unable to electrostatically attract or coordinate metal cations. Above the pKa, the carboxylate anion (-COO^-) provides:

1. **Negative charge**: Electrostatic attraction of metal cations to the negatively charged surface.

2. **Oxygen donors**: Two equivalent oxygen atoms that can serve as Lewis base donors. The carboxylate can coordinate metals in multiple modes:
   - **Monodentate**: One oxygen coordinates the metal (M-O-C=O)
   - **Bidentate chelating**: Both oxygens coordinate the same metal (forming a 4-membered ring)
   - **Bridging bidentate**: Each oxygen coordinates a different metal (crosslinking)

3. **Sharp transition**: Because the pKa is relatively low (3.4-4.5), the transition from non-coordinating to coordinating occurs over a narrow pH window (~2 pH units). At pH 3, <10% of carboxyl groups are deprotonated; at pH 5, >90% are deprotonated.

4. **Egg-box crosslinking**: In alginate, deprotonated carboxyl groups on adjacent chains can coordinate a single Ca2+ ion, forming the characteristic "egg-box" junction zone. This crosslinks the polymer into a stable hydrogel, which is the basis for alginate bead adsorbents.

The practical implication is that alginate-based and carboxyl-functional adsorbents require pH > 4 for effective heavy metal adsorption, but this threshold is lower than for amino-based adsorbents (which require pH > 6.5 for coordination).

## Positive Example

Alginate beads achieve Pb2+ adsorption capacities of 200-500 mg/g at pH 5-6, where carboxyl groups are fully deprotonated. The adsorption drops sharply below pH 4, with <50 mg/g at pH 3. Ion-exchange mechanism is confirmed by release of Na+ or Ca2+ during Pb2+ uptake.

## Counter-Example / Boundary Condition

In alginate gels pre-crosslinked with Ca2+ (egg-box structure), some carboxyl groups are already occupied by Ca2+. These pre-coordinated sites must undergo ion exchange (Ca2+ replaced by heavy metal), which has different thermodynamics than direct coordination to free -COO- sites. The effective pH threshold may shift slightly for pre-crosslinked vs. uncrosslinked alginate.

## Applicable Prototypes

- **alginate**: Guluronic and mannuronic acid carboxyl groups; the pH-dependent deprotonation is the primary control on metal adsorption capacity
- **chlorella-cell-wall**: Cell wall polysaccharides and proteins contain carboxyl groups from uronic acids and aspartic/glutamic acid residues
- **cellulose-nanocrystal**: TEMPO-oxidized cellulose nanocrystals have surface carboxyl groups with pH-dependent coordination behavior

## Literature Sources

- Davis et al. (2003): Alginate metal binding mechanisms, including pH-dependent carboxyl coordination
- Haug (1961): Classical study on alginate pKa values for G and M blocks
- Jang et al. (2005): TEMPO-oxidized cellulose nanocrystal metal adsorption
- *Note: References require verification during cross-validation phase*
