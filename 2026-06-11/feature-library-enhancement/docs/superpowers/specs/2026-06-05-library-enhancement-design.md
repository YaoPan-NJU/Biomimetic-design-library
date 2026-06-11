# Biomimetic Design Library Enhancement Spec

> Date: 2026-06-05
> Branch: feature/biomimetic-story-v2
> Status: Draft
> Related Projects: ADRMATS, Literature-extracting (biomimetic-extraction branch)

---

## 1. Goals and Constraints

### 1.1 Primary Goal

Transform the biomimetic design library from a 33-prototype skeleton into a research-grade knowledge base with approximately 100 high-quality prototypes, enriched with condition-mechanism design rules and biomimetic design principles. The library must serve as the biomimetic retrieval module in the ADRMATS multi-agent system, providing structured biomimetic context to the adversarial design engine.

### 1.2 Quality Targets

Each prototype must meet the following quality baseline:

- Biomimetic narrative sections (5.1-5.5): at least 3 of 5 subsections have substantive content
- Quantitative performance data: at least 3 pollutants with qmax or removal rate values
- Mechanism analysis: at least 2 mechanisms with full descriptions (phenomenon, molecular basis, functional groups, biomimetic inspiration)
- Structural features: at least 2 of 4 scales (macro/meso/micro/nano) described
- Engineering constraints: at least 5 of 11 constraints assessed with explanations

### 1.3 Non-Goals

- The library does not perform reasoning or combination — constraint identification belongs to ADRMATS's AdaptiveConstrainingAgent, combination reasoning belongs to the adversarial design engine.
- The library does not replace LLM domain knowledge — it supplements it with curated, evidence-backed rules that LLMs may not reliably recall.

---

## 2. Dual-Track Architecture

### 2.1 Overview

Two tracks run in parallel with periodic cross-validation:

**Track 1 (Rules Framework):** LLM generates condition-mechanism rules and biomimetic design principles top-down, producing a structured index (design-rules.json) and detailed Markdown explanations (principles/ directory).

**Track 2 (Prototype Deepening):** Full-text extraction and manual curation of 5 exemplar prototypes bottom-up, producing high-quality prototype.md files that serve as quality benchmarks.

### 2.2 Cross-Validation Protocol

**Round 1:** After Track 1 produces rule drafts and Track 2 completes the first 2 exemplars. Validate: do rules predict exemplar data correctly? Are exemplar phenomena covered by rules? Output: rule calibration report with confidence adjustments.

**Round 2:** After all 5 exemplars complete. Systematically calibrate all rules against real data. Identify rule conflicts (two rules giving contradictory advice for the same condition) and rule blind spots (important phenomena in exemplars without corresponding rules).

**Ongoing:** As new prototypes are added during expansion, each new prototype serves as additional validation data for existing rules.

---

## 3. Rules Framework Design

### 3.1 Storage Architecture (Dual-Layer)

**Index layer:** `design-rules.json` at the library root, alongside `feature-mapping.json`. Used for programmatic filtering and ADRMATS integration.

**Detail layer:** `principles/` directory tree with Markdown files. Used for agent deep-reading and prompt injection.

### 3.2 design-rules.json Schema

```json
{
  "version": "1.0",
  "last_updated": "2026-06-XX",
  "condition_mechanism_rules": [
    {
      "rule_id": "CM-001",
      "rule_type": "condition_mechanism",
      "title": "Catechol pH-dependent coordination",
      "condition": {
        "parameter": "pH",
        "operator": "range",
        "value": [3, 7],
        "target_feature": "catechol"
      },
      "behavior": "At pH 3-7, catechol hydroxyl groups progressively deprotonate, forming stable bidentate coordination bonds with metal ions. Below pH 3, protonation causes sharp decline in coordination capacity. Above pH 8, excessive oxidation to quinone form.",
      "behavior_zh": "pH 3-7范围内邻苯二酚的两个羟基逐步去质子化，与金属离子形成稳定的双齿配位键；pH < 3时质子化导致配位能力骤降；pH > 8时过度氧化为醌式结构",
      "affected_prototypes": ["mussel-foot-adhesion", "polydopamine-coating", "plant-tannin"],
      "scope": {
        "pollutants": ["heavy_metals"],
        "pH_range": [1, 14],
        "temperature_range": [0, 100]
      },
      "confidence": 0.9,
      "evidence_refs": ["mussel-foot-adhesion#performance_data", "polydopamine-coating#mechanism"],
      "detail_ref": "principles/mechanisms/catechol-ph-dependence.md"
    }
  ],
  "design_principle_rules": [
    {
      "rule_id": "DP-001",
      "rule_type": "design_principle",
      "title": "Multivalent Synergy in Bioadhesion",
      "context": "When designing mussel-inspired or tannin-inspired adsorbents for metal ion removal",
      "core_claim": "Bioadhesion strength depends not on a single functional group but on multivalent synergy between catechol, amine, and crosslinking mechanisms",
      "core_claim_zh": "生物粘附强度不取决于单一官能团，而取决于邻苯二酚、氨基和交联机制的多价协同效应",
      "affected_prototypes": ["mussel-foot-adhesion", "polydopamine-coating", "plant-tannin"],
      "scope": {
        "biomimetic_dimensions": ["molecular_biomimetic"],
        "mechanisms": ["coordination_chelation", "hydrogen_bonding"]
      },
      "confidence": 0.85,
      "evidence_refs": ["mussel-foot-adhesion#biomimetic_narrative"],
      "detail_ref": "principles/design-strategies/multivalent-synergy.md"
    }
  ],
  "rule_metadata": {
    "total_rules": 0,
    "cm_rules_count": 0,
    "dp_rules_count": 0,
    "avg_confidence": 0,
    "validated_against_exemplars": false
  }
}
```

### 3.3 Principles Directory Structure

```
principles/
├── mechanisms/
│   ├── catechol-ph-dependence.md
│   ├── electrostatic-charge-switching.md
│   ├── pore-size-selectivity.md
│   └── ...
├── design-strategies/
│   ├── multivalent-synergy.md
│   ├── hierarchical-structure-advantage.md
│   ├── bio-to-synthetic-feature-mapping.md
│   └── ...
└── trade-offs/
    ├── acid-resistance-vs-carboxyl-coordination.md
    ├── high-capacity-vs-fast-kinetics.md
    ├── selectivity-vs-broad-spectrum.md
    └── ...
```

### 3.4 Principle Markdown Template

Each principle file follows this structure:

```markdown
# [Principle Title]

> Rule ID: DP-XXX | Confidence: X.X | Last validated: YYYY-MM-DD

## Core Claim

One-sentence statement of the principle.

## Detailed Explanation

Why this principle holds. Include the underlying physics/chemistry/biology.

## Positive Example

A case where following this principle led to a successful biomimetic design.

## Counter-Example / Boundary Condition

A case where this principle does NOT apply, or where violating it was acceptable.

## Applicable Prototypes

- prototype-id-1: how this principle manifests
- prototype-id-2: how this principle manifests

## Literature Sources

- Author (Year): key finding supporting this principle
```

### 3.5 Rule Generation Strategy

**Track 1a — Condition-Mechanism Rules:** LLM generates rules in batches organized by mechanism dimension. Each batch covers one of: (1) coordination/chelation, (2) electrostatic, (3) pore adsorption, (4) structural mechanisms, (5) biological processes. Target: 15-25 rules per batch, total ~80-120 rules.

Generation prompt approach: "You are a materials science professor. For [mechanism type], list all important condition-dependent behaviors that a materials designer should know. For each, specify the condition parameter, the behavior change, which functional groups/structures are affected, and the pH/temperature range."

**Track 1b — Design Principles:** LLM generates principles using a "textbook author" prompt: "If you were writing a textbook chapter on designing [biomimetic dimension] adsorbents, what are the 5 most important design principles students must understand? For each principle, explain why it matters, give a positive example and a boundary condition." Target: ~30-50 principles total.

**Validation against feature-mapping.json:** After generation, each rule is checked against existing weight values and applicability ranges. Consistent rules get confidence boost (+0.05); inconsistent rules are flagged for manual review.

---

## 4. Exemplar Prototype Deepening

### 4.1 Five Exemplar Prototypes

| Prototype | Biomimetic Dimension | Key Mechanisms | Rationale |
|-----------|---------------------|----------------|-----------|
| mussel-foot-adhesion | Molecular | Coordination, pi-pi, H-bond | Most referenced prototype (6 pollutants, 5 features) |
| lotus-leaf | Morphological | Superhydrophobic separation | Core structural mechanism prototype |
| metal-organic-framework | Structural | Pore adsorption, catalytic, sieving | Most referenced non-biological prototype |
| sulfate-reducing-bacteria | Process | Bioprecipitation (sulfide) | Unique mechanism not covered by others |
| chitosan | Molecular | Electrostatic, coordination | Referenced by 8 pollutants, amphoteric behavior |

### 4.2 Deepening Workflow per Exemplar

**Phase A — Full-Text Extraction:**

For each exemplar, select 10-15 core papers (prioritizing review articles and high-impact experimental studies). Use Literature-extracting's new biomimetic schema (when available) or manual extraction to obtain:

- Complete biomimetic design chain (nature_challenge → evolutionary_strategy → key_mechanisms → bio_to_material_mapping)
- Quantitative performance data for at least 5 pollutant types with full experimental conditions
- Mechanism analysis with molecular basis, functional groups, and supporting evidence
- Multi-scale structural features (all 4 scales where data available)
- Engineering constraint assessments (all 11 constraints)

**Phase B — LLM Synthesis + Manual Curation:**

Feed extracted data to LLM to draft complete prototype.md content for all sections. Human expert reviews and:
- Verifies quantitative data against original papers
- Ensures biomimetic narrative tells a coherent story
- Extracts design principles specific to this prototype (feeds into Track 1)
- Identifies cross-prototype patterns (e.g., "catechol appears in mussel, PDA, and tannin — is there a unifying principle?")

**Phase C — Cross-Validation:**

Compare exemplar data against Track 1 rules. Document:
- Rules confirmed by exemplar data (confidence → increase)
- Rules contradicted by exemplar data (flag for review)
- Phenomena in exemplar not covered by any rule (new rule candidate)

### 4.3 Naming Reconciliation

Before deepening begins, resolve the prototype ID inconsistency between the 33 original directory IDs and the 30 pipeline-generated IDs. Strategy:

- Establish a canonical ID mapping table in `docs/prototype-id-mapping.md`
- Prefer shorter, more general IDs (e.g., `chitosan` over `chitosan-adsorbent`) to allow future expansion beyond adsorption
- For pipeline-generated IDs that represent genuinely different concepts (e.g., `diatom-microspheres` vs `diatom-frustule`), keep both as separate prototypes
- Merge duplicate content into canonical directories

---

## 5. Expansion Strategy: 33 → 100 Prototypes

### 5.1 Expansion Phases

**Phase 1 (Current 33):** Deepen all existing prototypes to quality baseline using rules-guided extraction. Priority order: exemplars first, then by feature-mapping.json reference frequency.

**Phase 2 (34-60):** Add prototypes in underrepresented biomimetic dimensions. Current coverage is heavy on molecular biomimetics (8 prototypes) and light on system biomimetics (1 prototype: mangrove-root). Target additions include:

- Additional microbial systems: biofilm communities, quorum-sensing bacteria, extremophile archaea
- Plant-based systems beyond current 6: bamboo vascular bundles, pitcher plant variants, carnivorous plant enzymes
- Animal systems: gecko adhesion, barnacle cement, squid beak gradient structure, abalone shell nacre
- Bio-inspired synthetic: molecularly imprinted polymers, DNA-origami scaffolds, peptide amphiphiles

**Phase 3 (61-100):** Rule-gap-driven expansion. After rules framework is mature (~100+ rules), identify systematic blind spots — pollutants, mechanisms, or design dimensions with no prototype coverage. Add prototypes specifically to fill these gaps.

### 5.2 Detailed Search Strategy for Literature Supplementation

Each expansion phase requires systematic literature searching. The following search strategies are organized by purpose.

#### Strategy Group A: Exemplar Deepening (5 exemplars × 10-15 papers each)

**mussel-foot-adhesion:**

```
WoS: TS=("mussel-inspired" OR "mussel adhesion" OR "DOPA" OR "polydopamine" OR "byssus" OR "mussel foot protein") AND TS=("adsorption" OR "heavy metal removal" OR "water treatment")
CNKI: SU=('贻贝'+'仿贻贝'+'多巴胺'+'聚多巴胺'+'足丝蛋白') AND SU=('吸附'+'水处理'+'重金属')
Google Scholar: mussel-inspired adsorbent heavy metal removal mechanism review
Target: 5 review articles + 5 high-impact experimental + 5 mechanism-focused
```

**lotus-leaf:**

```
WoS: TS=("lotus leaf" OR "superhydrophobic" OR "Cassie-Baxter" OR "self-cleaning surface" OR "papilla structure") AND TS=("oil-water separation" OR "water treatment" OR "adsorption")
CNKI: SU=('荷叶'+'超疏水'+'自清洁'+'微纳结构') AND SU=('油水分离'+'水处理'+'吸附')
Google Scholar: lotus leaf inspired superhydrophobic oil water separation review
Target: 5 review + 5 experimental + 5 on micro-nano structure characterization
```

**metal-organic-framework:**

```
WoS: TS=("metal-organic framework" OR "MOF" OR "ZIF" OR "UiO" OR "MIL") AND TS=("water treatment" OR "heavy metal adsorption" OR "dye removal" OR "antibiotic adsorption")
CNKI: SU=('金属有机框架'+'MOF'+'配位聚合物') AND SU=('水处理'+'吸附'+'重金属'+'染料')
Google Scholar: MOF water treatment adsorption review 2020-2026
Target: 5 review + 5 comparative studies + 5 mechanism investigations
```

**sulfate-reducing-bacteria:**

```
WoS: TS=("sulfate-reducing bacteria" OR "SRB" OR "Desulfovibrio" OR "biogenic sulfide" OR "metal sulfide precipitation") AND TS=("heavy metal" OR "water treatment" OR "bioremediation")
CNKI: SU=('硫酸盐还原菌'+'SRB'+'硫化物沉淀') AND SU=('重金属'+'水处理'+'生物修复')
Google Scholar: sulfate reducing bacteria heavy metal removal mechanism
Target: 5 review + 5 experimental + 5 on sulfide precipitation mechanism
```

**chitosan:**

```
WoS: TS=("chitosan" OR "chitin" OR "deacetylated chitin") AND TS=("adsorption" OR "heavy metal removal" OR "dye removal" OR "water treatment") AND TS=("mechanism" OR "amino group" OR "crosslinking")
CNKI: SU=('壳聚糖'+'甲壳素'+'氨基多糖') AND SU=('吸附'+'水处理'+'重金属'+'染料'+'机理')
Google Scholar: chitosan adsorption mechanism review amino group coordination
Target: 5 review + 5 mechanism studies + 5 comparative (chitosan vs modified chitosan)
```

#### Strategy Group B: Phase 2 Expansion Candidates (~27 new prototypes)

Each candidate prototype below includes a primary search query:

**Microbial systems:**
```
biofilm-adsorbent: TS=("biofilm" OR "extracellular polymeric substance" OR "EPS") AND TS=("heavy metal" OR "adsorption" OR "biosorption")
extremophile-archaea: TS=("extremophile" OR "acidophile" OR "halophile" OR "archaea") AND TS=("metal adsorption" OR "biosorption" OR "bioremediation")
cyanobacteria: TS=("cyanobacteria" OR "blue-green algae" OR "Spirulina") AND TS=("biosorption" OR "heavy metal" OR "water treatment")
actinomycetes: TS=("actinomycetes" OR "Streptomyces") AND TS=("biosorption" OR "heavy metal" OR "antibiotic degradation")
```

**Plant systems:**
```
bamboo-vascular: TS=("bamboo" OR "vascular bundle" OR "bamboo fiber") AND TS=("adsorption" OR "water treatment" OR "porous carbon")
carnivorous-plant: TS=("carnivorous plant" OR "Venus flytrap" OR "pitcher plant enzyme") AND TS=("selective capture" OR "digestion mechanism")
pine-needle: TS=("pine needle" OR "conifer needle" OR "stomata array") AND TS=("air filtration" OR "particulate capture" OR "surface structure")
rice-husk: TS=("rice husk" OR "rice straw" OR "agricultural waste") AND TS=("adsorption" OR "biosorbent" OR "silica" OR "activated carbon")
tea-polyphenol: TS=("tea polyphenol" OR "epigallocatechin" OR "EGCG" OR "green tea extract") AND TS=("adsorption" OR "metal chelation" OR "water treatment")
```

**Animal systems:**
```
gecko-adhesion: TS=("gecko" OR "setae" OR "van der Waals adhesion") AND TS=("dry adhesion" OR "reversible adhesion" OR "surface attachment")
barnacle-cement: TS=("barnacle" OR "barnacle cement protein" OR "underwater adhesion") AND TS=("biofouling" OR "adhesive protein" OR "crosslinking")
squid-beak: TS=("squid beak" OR "cephalopod" OR "gradient structure" OR "histidine-rich protein") AND TS=("mechanical gradient" OR "crosslinking gradient")
abalone-nacre: TS=("abalone" OR "nacre" OR "mother of pearl" OR "brick-and-mortar structure") AND TS=("biomineralization" OR "mechanical property" OR "composite")
silkworm-cocoon: TS=("silkworm cocoon" OR "sericin" OR "cocoon shell") AND TS=("adsorption" OR "filtration" OR "protective structure")
earthworm-gut: TS=("earthworm" OR "vermicompost" OR "earthworm gut") AND TS=("heavy metal" OR "soil remediation" OR "bioaccumulation")
```

**Bio-inspired synthetic:**
```
molecularly-imprinted-polymer: TS=("molecularly imprinted polymer" OR "MIP" OR "molecular imprinting") AND TS=("selective adsorption" OR "water treatment" OR "template molecule")
peptide-amphiphile: TS=("peptide amphiphile" OR "self-assembling peptide" OR "peptide nanofiber") AND TS=("metal binding" OR "water treatment" OR "biomaterial")
dna-origami: TS=("DNA origami" OR "DNA scaffold" OR "DNA nanostructure") AND TS=("metal binding" OR "template" OR "nanomaterial assembly")
enzyme-mimetic: TS=("nanozyme" OR "enzyme mimic" OR "artificial enzyme") AND TS=("catalytic degradation" OR "pollutant removal" OR "water treatment")
aquaporin-membrane: TS=("aquaporin" OR "biomimetic membrane" OR "water channel protein") AND TS=("water purification" OR "desalination" OR "selective transport")
```

#### Strategy Group C: Phase 3 Gap-Driven Expansion

After rules framework reaches maturity, identify gaps through automated analysis:

```
Gap Analysis Query:
1. List all pollutants in taxonomy/pollutants.md with < 2 prototype matches
2. List all mechanisms in taxonomy/mechanisms.md with < 2 prototype matches
3. List all biomimetic dimensions with < 3 prototypes
4. Identify emerging pollutants (PFAS, microplastics, antibiotic resistance genes, rare earth elements) with zero prototype coverage
```

Each identified gap triggers a targeted literature search using the template:

```
WoS: TS=([biological_source] OR [biomimetic_keyword]) AND TS=([target_pollutant] OR [target_mechanism]) AND TS=("water treatment" OR "adsorption" OR "remediation")
CNKI: SU=('[中文生物名]'+'[仿生关键词]') AND SU=('[目标污染物]'+'[目标机制]'+'水处理')
Google Scholar: [biological source] [target application] biomimetic adsorption
```

#### Strategy Group D: Cross-Cutting Methodology Papers

These papers inform rule generation rather than specific prototypes:

```
biomimetic-design-review: TS=("biomimetic" OR "bio-inspired") AND TS=("water treatment" OR "adsorbent design") AND TS=("review" OR "state of the art")
structure-function-relationship: TS=("structure-function" OR "structure-activity") AND TS=("adsorption" OR "adsorbent") AND TS=("review" OR "mechanism")
adsorption-mechanism-review: TS=("adsorption mechanism" OR "adsorption thermodynamics" OR "adsorption kinetics") AND TS=("review" OR "fundamental")
green-synthesis: TS=("green synthesis" OR "biosynthesis" OR "biogenic") AND TS=("adsorbent" OR "nanoparticle") AND TS=("water treatment")
```

---

## 6. ADRMATS Integration

### 6.1 Module Position

```
User Input → AdaptiveConstrainingAgent → [BiomimeticRetrievalTool] → AdversarialDesignFlow → ...
```

The biomimetic module sits between constraint generation and adversarial design, receiving structured constraint output and producing structured biomimetic context.

### 6.2 BiomimeticContext Model

```python
class BiomimeticContext(BaseModel):
    candidate_prototypes: List[PrototypeMatch]
    applicable_rules: List[RuleSummary]
    design_principles: List[PrincipleSummary]
    biomimetic_suggestions: List[str]

class PrototypeMatch(BaseModel):
    prototype_id: str
    match_weight: float
    match_reason: str
    key_features: List[str]
    key_mechanisms: List[str]

class RuleSummary(BaseModel):
    rule_id: str
    title: str
    behavior: str
    relevance: str  # why this rule matters for the current design

class PrincipleSummary(BaseModel):
    rule_id: str
    title: str
    core_claim: str
    design_implication: str  # how to apply this principle to current design
```

### 6.3 Retrieval Flow

1. Receive `ConstraintPreprocessOutput` from constraint agent (pollutant, pH, temperature, salinity, design guidelines)
2. Query `feature-mapping.json` Layer 1 (applicability filter) + Layer 2 (pollutant/feature match) → top 5 prototypes
3. Query `design-rules.json` with candidate prototype features + current water quality conditions → applicable rules
4. For each applicable rule, read `detail_ref` Markdown → extract key paragraphs
5. Package as `BiomimeticContext` and inject into design flow's `global_context`

### 6.4 Injection Point

The `BiomimeticContext` is added to `global_context["biomimetic_context"]` in the ADRMATS orchestrator, accessible to:

- **Proposer A/B:** via prompt injection (JSON serialized biomimetic context appended to constraint payload)
- **Design Explaining Agent:** via global context (can trace design decisions back to specific biomimetic rules/principles)

---

## 7. Implementation Sequencing

### Phase 0: Foundation (Week 1)

- [ ] Resolve prototype naming inconsistency (create ID mapping table)
- [ ] Create `principles/` directory structure and templates
- [ ] Create `design-rules.json` skeleton with schema
- [ ] Begin Literature-extracting biomimetic-extraction branch implementation (T1-T5)

### Phase 1a: Track 1 — Rule Generation (Week 1-2)

- [ ] Generate condition-mechanism rules batch 1: coordination/chelation (~20 rules)
- [ ] Generate condition-mechanism rules batch 2: electrostatic + pore (~20 rules)
- [ ] Generate condition-mechanism rules batch 3: structural + biological (~20 rules)
- [ ] Generate design principles batch 1: molecular biomimetic (~15 principles)
- [ ] Generate design principles batch 2: structural + morphological (~15 principles)
- [ ] Validate generated rules against feature-mapping.json consistency

### Phase 1b: Track 2 — Exemplar Deepening (Week 1-3, parallel with 1a)

- [ ] Literature search for mussel-foot-adhesion (15 papers)
- [ ] Literature search for lotus-leaf (15 papers)
- [ ] Full-text extraction for mussel + lotus-leaf
- [ ] Manual curation of mussel + lotus-leaf prototype.md
- [ ] **Cross-validation Round 1** (first 2 exemplars vs rules)
- [ ] Literature search for MOF + SRB + chitosan (45 papers total)
- [ ] Full-text extraction for remaining 3 exemplars
- [ ] Manual curation of MOF + SRB + chitosan prototype.md

### Phase 2: Cross-Validation + Calibration (Week 3-4)

- [ ] **Cross-validation Round 2** (all 5 exemplars vs all rules)
- [ ] Rule calibration report
- [ ] Identify and resolve rule conflicts
- [ ] Identify rule blind spots → queue new rules
- [ ] Update feature-mapping.json weights based on exemplar data

### Phase 3: Batch Deepening (Week 4-8)

- [ ] Deepen remaining 28 prototypes using rules-guided extraction
- [ ] For each prototype: literature search → extraction → prototype.md drafting → manual review
- [ ] Continuous rule validation as each prototype is deepened
- [ ] All 33 original prototypes reach quality baseline

### Phase 4: Expansion (Week 8-16+)

- [ ] Phase 2 expansion: ~27 new prototypes (search strategies in Section 5.2 Group B)
- [ ] Phase 3 expansion: gap-driven additions (search strategies in Section 5.2 Group C)
- [ ] Target: ~100 prototypes total
- [ ] Ongoing rule refinement with each new prototype

---

## 8. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Prototype count | ~100 | Count of prototype directories with quality-baseline prototype.md |
| Rule count | 80-120 CM rules + 30-50 principles | Count in design-rules.json |
| Rule confidence | avg > 0.8 | Mean confidence across all rules |
| Prototype quality | 100% meet baseline | Automated quality check script |
| ADRMATS integration | BiomimeticContext consumed in design flow | End-to-end test |
| Literature coverage | 15+ papers per exemplar, 5+ per remaining prototype | Bibliography count |
| Rule exemplar validation | > 80% rules validated by ≥ 1 exemplar | Cross-validation report |
