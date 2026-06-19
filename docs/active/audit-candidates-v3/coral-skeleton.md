# Audit: coral-skeleton

## Summary
- Total mechanisms: 0
- Total performance_data: 0
- Total design_translation: 1
- Total engineering_constraints: 0
- Total narrative entries: 1
- Issues found: 1

## Findings

### [F1] Narrative entry is wrong-topic (antifouling, not adsorption)
- **Type**: translation-scope
- **Severity**: medium
- **Location**: narrative.entries[0] (lines 23-35)
- **Evidence**: The single narrative entry cites Han2020 antifouling review (2020-Han-antifouling-review.json). The content describes marine biofouling prevention strategies (Sharklet microstructure, zwitterionic hydrogels, PDMS coatings), not coral skeleton CaCO3 adsorption. The sections describe antifouling mechanisms and membrane surface engineering, which is unrelated to coral skeleton as an adsorption material.
- **Cross-ref**: B15-CORAL-001 (acknowledged_knowledge_gap_2026_06_17): "No local coral/CaCO3 adsorption PDF/cache/json was found; Han extraction is wrong-topic antifouling material."
- **Recommended disposition**: Remove this narrative entry or replace with actual coral/CaCO3 adsorption literature when available

## Clean areas
- mechanisms: empty (no contamination possible)
- performance_data: empty (no contamination possible)
- design_translation[0]: LLM-inference (correctly labeled, scope = coral skeleton CaCO3 adsorption)
- engineering_constraints: empty
