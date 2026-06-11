# ADRMATS Integration Specification

> Generated: 2026-06-05
> Status: Draft
> Reference: docs/superpowers/specs/2026-06-05-library-enhancement-design.md Sections 6.1-6.4

---

## 1. Module Position in ADRMATS Multi-Agent System

The biomimetic-design-library serves as the **biomimetic retrieval module** within the ADRMATS (Adversarial Design of Reactive Materials Through Autonomous Testing and Simulation) multi-agent pipeline. It sits between the constraint generation agent and the adversarial design engine:

```
User Input
    |
    v
AdaptiveConstrainingAgent
    |
    | (ConstraintPreprocessOutput)
    v
[BiomimeticRetrievalTool]  <-- this library
    |
    | (BiomimeticContext)
    v
AdversarialDesignFlow
    |
    v
... (Proposer A/B, Design Explaining Agent, etc.)
```

### Role Definition

- **Upstream:** The `AdaptiveConstrainingAgent` identifies engineering constraints from the user's design problem (target pollutant, pH range, temperature, salinity, design guidelines).
- **This module:** Receives structured constraint output, queries the biomimetic knowledge base, and returns structured biomimetic context.
- **Downstream:** The `AdversarialDesignFlow` consumes the biomimetic context to propose material designs informed by biological strategies.

### Boundary Declaration

**This library does NOT contain ADRMATS code.** It provides:

1. **Knowledge base data:** `feature-mapping.json` (pollutant/feature-to-prototype mappings, prototype metadata), `design-rules.json` (condition-mechanism rules, design principles), and per-prototype `prototype.md` files.
2. **Integration interface definitions:** Pydantic models and retrieval flow specification that ADRMATS implements.

The actual `BiomimeticRetrievalTool` class implementation lives in the ADRMATS codebase. This repository supplies only the data and the contract.

---

## 2. Data Flow

```
ConstraintPreprocessOutput
        |
        v
  BiomimeticRetrievalTool
        |
        |  1. Applicability filter (pH, temp, salinity)
        |  2. Pollutant/feature matching
        |  3. Rule query
        |  4. Detail extraction
        |  5. Packaging
        v
  BiomimeticContext
        |
        v
  Inject into global_context["biomimetic_context"]
```

### Input: ConstraintPreprocessOutput

Produced by `AdaptiveConstrainingAgent`. Contains at minimum:

- `pollutant`: target pollutant species and concentration
- `ph_range`: operating pH range
- `temperature_range`: operating temperature range
- `salinity`: salinity level (low / moderate / high / any)
- `design_guidelines`: user-specified design priorities (e.g., "low cost", "high selectivity")

### Output: BiomimeticContext

A structured context object injected into the design flow's global context, providing the adversarial design engine with biomimetic inspiration data.

---

## 3. BiomimeticContext Pydantic Model

```python
from pydantic import BaseModel
from typing import List


class PrototypeMatch(BaseModel):
    """A single biomimetic prototype matched to the current design problem."""
    prototype_id: str           # Canonical ID, e.g., "mussel-foot-adhesion"
    match_weight: float         # Match confidence score (0-1)
    match_reason: str           # Why this prototype was selected
    key_features: List[str]     # Relevant features, e.g., ["catechol", "metal_coordination"]
    key_mechanisms: List[str]   # Relevant mechanisms, e.g., ["coordination_chelation", "pi_pi_stacking"]


class RuleSummary(BaseModel):
    """A condition-mechanism rule relevant to the current design context."""
    rule_id: str                # Rule ID, e.g., "CM-001"
    title: str                  # Short title
    behavior: str               # Core behavior description
    relevance: str              # Why this rule matters for the current design problem


class PrincipleSummary(BaseModel):
    """A design principle applicable to the current biomimetic design task."""
    rule_id: str                # Principle ID, e.g., "DP-001"
    title: str                  # Short title
    core_claim: str             # One-sentence statement of the principle
    design_implication: str     # How to apply this principle to the current design


class BiomimeticContext(BaseModel):
    """Complete biomimetic context for injection into ADRMATS design flow."""
    candidate_prototypes: List[PrototypeMatch]     # Top 5 matched prototypes
    applicable_rules: List[RuleSummary]             # Condition-mechanism rules for current water quality
    design_principles: List[PrincipleSummary]       # Relevant design principles
    biomimetic_suggestions: List[str]               # Free-form biomimetic design suggestions
```

---

## 4. Retrieval Flow (5 Steps)

### Step 1: Receive Constraint Input

Receive `ConstraintPreprocessOutput` from the `AdaptiveConstrainingAgent`. Extract key parameters: pollutant type, pH range, temperature range, salinity, and design guideline priorities.

### Step 2: Prototype Matching

Query `feature-mapping.json` using a two-layer filter:

- **Layer 1 -- Applicability filter:** For each prototype in `prototype_metadata`, check if the current pH, temperature, and salinity fall within the prototype's `applicability` ranges. Eliminate prototypes outside range.
- **Layer 2 -- Pollutant/feature match:** Query `pollutant_prototype_map` for the target pollutant and `feature_prototype_map` for relevant features. Score each surviving prototype by weighted match count.
- **Output:** Top 5 prototypes ranked by composite score (applicability pass + match weight).

### Step 3: Rule Query

Query `design-rules.json` using the candidate prototype features and current water quality conditions:

- Match `condition_mechanism_rules` where `affected_prototypes` overlap with candidate prototypes AND `scope.pollutants` / `scope.pH_range` / `scope.temperature_range` overlap with current conditions.
- Match `design_principle_rules` where `affected_prototypes` overlap with candidate prototypes AND `scope.biomimetic_dimensions` / `scope.mechanisms` are relevant.
- **Output:** List of applicable rules and principles.

### Step 4: Detail Extraction

For each applicable rule from Step 3:

- Read the Markdown file referenced by `detail_ref` (e.g., `principles/mechanisms/catechol-ph-dependence.md`).
- Extract the "Core Claim", "Detailed Explanation", and "Applicable Prototypes" sections.
- Compose a `RuleSummary` or `PrincipleSummary` with a `relevance` / `design_implication` field tailored to the current design problem.

### Step 5: Package and Inject

- Assemble all matched prototypes, rule summaries, principle summaries, and free-form biomimetic suggestions into a `BiomimeticContext` object.
- Serialize to JSON.
- Inject into `global_context["biomimetic_context"]` in the ADRMATS orchestrator.

---

## 5. Injection Points

The `BiomimeticContext` is made available to downstream ADRMATS agents through the `global_context` dictionary:

### 5.1 Proposer A/B (Design Generation)

- **Access method:** Prompt injection. The JSON-serialized `BiomimeticContext` is appended to the constraint payload sent to each proposer agent.
- **Effect:** Each proposer receives biomimetic inspiration (candidate prototypes, applicable rules, design principles) alongside the engineering constraints, enabling bio-informed material design proposals.

### 5.2 Design Explaining Agent (Rationale Tracing)

- **Access method:** Global context. The agent reads `global_context["biomimetic_context"]` to trace design decisions back to specific biomimetic rules and principles.
- **Effect:** The explaining agent can articulate *why* a particular design was proposed by referencing the underlying biological strategy (e.g., "This design was inspired by mussel foot protein's catechol-metal coordination mechanism, as described in rule CM-001").

### 5.3 Injection Format

```json
{
  "biomimetic_context": {
    "candidate_prototypes": [
      {
        "prototype_id": "mussel-foot-adhesion",
        "match_weight": 0.9,
        "match_reason": "DOPA catechol groups provide strong Pb2+ chelation at pH 5-7",
        "key_features": ["catechol", "metal_coordination", "pi_electron", "wet_adhesion"],
        "key_mechanisms": ["coordination_chelation", "pi_pi_stacking"]
      }
    ],
    "applicable_rules": [
      {
        "rule_id": "CM-001",
        "title": "Catechol pH-dependent coordination",
        "behavior": "At pH 3-7, catechol hydroxyls progressively deprotonate, forming stable bidentate coordination bonds with metal ions",
        "relevance": "Current pH 5-6 is optimal for catechol-Pb coordination"
      }
    ],
    "design_principles": [
      {
        "rule_id": "DP-001",
        "title": "Multivalent Synergy in Bioadhesion",
        "core_claim": "Bioadhesion strength depends on multivalent synergy between catechol, amine, and crosslinking mechanisms",
        "design_implication": "Design adsorbent with both catechol and amine functional groups for maximum Pb2+ capture"
      }
    ],
    "biomimetic_suggestions": [
      "Consider introducing catechol groups via polydopamine coating on a porous substrate",
      "Combine with amine-rich chitosan for multivalent coordination synergy",
      "Maintain pH 4-7 operating window to preserve catechol coordination activity"
    ]
  }
}
```

---

## 6. Data Files Referenced

| File | Purpose | Location |
|------|---------|----------|
| `feature-mapping.json` | Pollutant/feature-to-prototype mappings, prototype metadata (applicability ranges, features) | Library root |
| `design-rules.json` | Condition-mechanism rules and design principle rules with confidence scores | Library root |
| `principles/mechanisms/*.md` | Detailed mechanism explanations | Library root/principles/mechanisms/ |
| `principles/design-strategies/*.md` | Design strategy explanations | Library root/principles/design-strategies/ |
| `principles/trade-offs/*.md` | Trade-off analysis between competing design goals | Library root/principles/trade-offs/ |
| `prototypes/*/prototype.md` | Per-prototype detailed biomimetic design files | Library root/prototypes/ |

---

## 7. Scope and Limitations

### What this library provides:
- Curated biomimetic knowledge base (33+ prototypes, expanding to ~100)
- Structured feature-prototype mapping with quantitative weights
- Condition-mechanism rules with confidence scores and evidence references
- Design principles with literature backing
- Pydantic model definitions for integration contracts

### What this library does NOT provide:
- ADRMATS agent implementations (those live in the ADRMATS repository)
- Reasoning or combination logic (constraint identification belongs to `AdaptiveConstrainingAgent`; material combination reasoning belongs to `AdversarialDesignFlow`)
- LLM domain knowledge replacement (the library supplements LLM knowledge with curated, evidence-backed data that LLMs may not reliably recall)
- Runtime execution environment (the library is a static data repository consumed at query time)
