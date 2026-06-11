"""Tests for generate_prototype_md.py."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from generate_prototype_md import (
    generate_frontmatter,
    generate_section1_intro,
    generate_section2_mechanisms,
    generate_section3_structure,
    generate_section4_performance,
    generate_section5_narrative,
    generate_section6_scenarios,
    generate_section7_related,
    generate_references,
    generate_prototype_md,
)


@pytest.fixture
def aggregated_mussel():
    """Sample aggregated data for mussel-foot-adhesion."""
    return {
        "performance_data": [
            {
                "pollutant": "Pb2+",
                "material_form": "PDA-coated Fe3O4 nanoparticles",
                "qmax_mg_g": 185.2,
                "removal_rate_pct": 96.5,
                "pH": 5.0,
                "temperature_C": 25,
                "kinetics_model": "pseudo-second-order",
                "isotherm_model": "Langmuir",
                "data_source": "experimental",
                "reference": "Table 2, Zhang 2025",
                "confidence": "high",
            },
        ],
        "mechanism_analysis": [
            {
                "mechanism_name": "配位螯合",
                "phenomenon": "PDA strongly binds heavy metal ions",
                "molecular_basis": ["Catechol groups form bidentate ligands"],
                "key_functional_groups": [
                    {"group": "catechol (-OH)", "role": "Primary coordination site"},
                ],
                "biomimetic_inspiration": "DOPA-rich coatings for universal metal capture",
                "supporting_evidence": "XPS O 1s peak shift after Pb2+ adsorption",
            },
        ],
        "biomimetic_design_chains": [
            {
                "paper_id": "zhang_2025_mussel",
                "chain": {
                    "nature_challenge": "Mussels must adhere to wet surfaces in turbulent intertidal zones",
                    "evolutionary_strategy": "Secrete DOPA-rich foot proteins",
                    "key_mechanisms": ["Catechol-metal coordination"],
                    "key_functional_groups": [
                        {"group": "catechol", "function": "Bidentate metal coordination"},
                    ],
                    "bio_to_material_mapping": [
                        {
                            "bio_feature": "DOPA catechol group",
                            "material_design": "PDA coating on substrates",
                            "confidence": "high",
                        },
                    ],
                    "must_keep_features": [
                        {"feature": "catechol group", "reason": "Essential for metal coordination"},
                    ],
                    "adjustable_features": [
                        {"feature": "coating thickness", "adjustment_range": "10-200 nm"},
                    ],
                    "one_line_story": "Mimicking mussel DOPA for adhesive coatings",
                    "design_traceability": "From Mytilus edulis to PDA dip-coating",
                },
            },
        ],
        "structural_features": [
            {
                "paper_id": "zhang_2025_mussel",
                "features": {
                    "macro_scale": {"feature": "Aggregated clusters", "size_range": "50-200 nm", "function": "Easy recovery"},
                    "meso_scale": {"feature": "Mesoporous PDA shell", "size_range": "2-10 nm", "function": "High surface area"},
                    "micro_scale": {"feature": "Core-shell structure", "size_range": "20-50 nm shell", "function": "Magnetic + adsorption"},
                    "nano_scale": {"feature": "Catechol groups", "size_range": "<1 nm", "function": "Coordination sites"},
                    "structure_function_relationship": "Core-shell combines magnetic recovery with catechol sites",
                },
            },
        ],
        "engineering_constraints": [
            {"constraint": "高吸附容量", "assessment": "high", "explanation": "qmax=185.2 mg/g"},
        ],
        "papers": [
            {"paper_id": "zhang_2025_mussel", "confidence": "high"},
        ],
    }


class TestGenerateFrontmatter:
    def test_contains_required_yaml_fields(self, aggregated_mussel):
        fm = generate_frontmatter("mussel-foot-adhesion", aggregated_mussel)
        assert "id: mussel-foot-adhesion" in fm
        assert "features:" in fm
        assert "pollutants:" in fm
        assert "adsorption_mechanisms:" in fm

    def test_includes_pollutant_from_performance(self, aggregated_mussel):
        fm = generate_frontmatter("mussel-foot-adhesion", aggregated_mussel)
        assert "Pb2+" in fm

    def test_includes_mechanism(self, aggregated_mussel):
        fm = generate_frontmatter("mussel-foot-adhesion", aggregated_mussel)
        assert "配位螯合" in fm


class TestGenerateSections:
    def test_section1_intro_not_empty(self, aggregated_mussel):
        section = generate_section1_intro("mussel-foot-adhesion", aggregated_mussel)
        assert len(section) > 50

    def test_section2_mechanisms_includes_mechanism_name(self, aggregated_mussel):
        section = generate_section2_mechanisms(aggregated_mussel)
        assert "配位螯合" in section
        assert "现象" in section

    def test_section3_structure_includes_table(self, aggregated_mussel):
        section = generate_section3_structure(aggregated_mussel)
        assert "宏观" in section
        assert "纳米" in section

    def test_section4_performance_includes_data_table(self, aggregated_mussel):
        section = generate_section4_performance(aggregated_mussel)
        assert "185.2" in section
        assert "Pb2+" in section

    def test_section5_narrative_has_subsections(self, aggregated_mussel):
        section = generate_section5_narrative(aggregated_mussel)
        assert "5.1" in section
        assert "5.2" in section
        assert "5.3" in section

    def test_section4_empty_when_no_data(self):
        section = generate_section4_performance({"performance_data": []})
        assert "暂无" in section or "待补充" in section or len(section.strip()) < 200


class TestGenerateFullPrototype:
    def test_full_md_generation(self, aggregated_mussel):
        md = generate_prototype_md("mussel-foot-adhesion", aggregated_mussel)
        assert "---" in md  # frontmatter
        assert "## 1." in md
        assert "## 2." in md
        assert "## 5." in md
        assert "mussel" in md.lower() or "贻贝" in md

    def test_references_section(self, aggregated_mussel):
        section = generate_references(aggregated_mussel)
        assert "zhang_2025_mussel" in section
