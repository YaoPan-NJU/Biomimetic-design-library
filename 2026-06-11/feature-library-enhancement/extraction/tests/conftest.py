"""Shared fixtures for biomimetic extraction tests."""

import json
import os
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
BIOMIMETIC_LIB = Path(
    os.environ.get(
        "BIOMIMETIC_LIB",
        REPO_ROOT.parent,
    )
)


@pytest.fixture
def repo_root():
    return REPO_ROOT


@pytest.fixture
def biomimetic_lib():
    return BIOMIMETIC_LIB


@pytest.fixture
def sample_extraction_result():
    """Minimal valid biomimetic extraction JSON (dict form)."""
    return {
        "schema_version": "biomimetic-v1",
        "paper_id": "zhang_2025_mussel",
        "bibliographic_metadata": {
            "title": "Mussel-inspired adsorbent for heavy metal removal",
            "authors": ["Zhang, X.", "Li, Y."],
            "year": 2025,
            "abstract": "We report a PDA-coated adsorbent...",
            "doi": "10.1000/example",
            "language": "en",
            "keywords": ["mussel", "PDA", "heavy metal", "adsorption"],
            "file_name": "zhang_2025_mussel.pdf",
        },
        "prototype_associations": [
            {
                "prototype_id": "mussel-foot-adhesion",
                "match_confidence": "high",
                "match_reason": "Paper directly studies mussel-inspired PDA coating",
            },
            {
                "prototype_id": "polydopamine-coating",
                "match_confidence": "high",
                "match_reason": "PDA coating is the primary material studied",
            },
        ],
        "biomimetic_design_chain": {
            "nature_challenge": "Mussels must adhere to wet surfaces in turbulent intertidal zones",
            "evolutionary_strategy": "Secrete DOPA-rich foot proteins that form strong bonds underwater",
            "key_mechanisms": [
                "Catechol-metal coordination",
                "Oxidative crosslinking of DOPA",
            ],
            "key_functional_groups": [
                {"group": "catechol", "function": "Bidentate metal coordination"},
                {"group": "amine", "function": "Surface anchoring and crosslinking"},
            ],
            "bio_to_material_mapping": [
                {
                    "bio_feature": "DOPA catechol group",
                    "material_design": "Polydopamine coating on substrates",
                    "confidence": "high",
                },
            ],
            "must_keep_features": [
                {"feature": "catechol group", "reason": "Essential for metal coordination"},
            ],
            "adjustable_features": [
                {"feature": "coating thickness", "adjustment_range": "10-200 nm"},
            ],
            "one_line_story": "Mimicking mussel DOPA proteins to create universal adhesive coatings for heavy metal capture",
            "design_traceability": "From Mytilus edulis foot protein chemistry to PDA dip-coating process",
        },
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
                "selectivity": "Preferential for Pb2+ over Cd2+ and Zn2+",
                "reusability_cycles": 5,
                "data_source": "experimental",
                "reference": "Table 2, Zhang 2025",
                "confidence": "high",
            },
        ],
        "structural_features": {
            "macro_scale": {
                "feature": "Spherical nanoparticles aggregated into clusters",
                "size_range": "50-200 nm",
                "function": "Easy dispersion and recovery",
            },
            "meso_scale": {
                "feature": "Mesoporous PDA shell",
                "size_range": "2-10 nm pores",
                "function": "High surface area for metal ion access",
            },
            "micro_scale": {
                "feature": "Core-shell Fe3O4@PDA structure",
                "size_range": "20-50 nm shell",
                "function": "Magnetic recovery + adsorption",
            },
            "nano_scale": {
                "feature": "Catechol groups at molecular level",
                "size_range": "<1 nm",
                "function": "Direct metal coordination sites",
            },
            "structure_function_relationship": "Core-shell architecture combines magnetic recovery with high-density catechol sites; mesoporous shell ensures ion accessibility",
        },
        "mechanism_analysis": [
            {
                "mechanism_name": "配位螯合",
                "phenomenon": "PDA coating strongly binds heavy metal ions in aqueous solution",
                "molecular_basis": [
                    "Catechol hydroxyl groups deprotonate at pH 5, forming bidentate ligands",
                    "Metal-catechol complexes have stability constants log K > 10",
                ],
                "key_functional_groups": [
                    {"group": "catechol (-OH)", "role": "Primary metal coordination site"},
                    {"group": "amine (-NH2)", "role": "Secondary coordination and crosslinking"},
                ],
                "biomimetic_inspiration": "DOPA-rich coatings can be applied to any substrate for universal metal capture",
                "supporting_evidence": "XPS shows shift in O 1s peak after Pb2+ adsorption, confirming catechol involvement",
            },
        ],
        "engineering_constraints": [
            {
                "constraint": "高吸附容量",
                "assessment": "high",
                "explanation": "qmax=185.2 mg/g for Pb2+ is competitive",
            },
            {
                "constraint": "可回收性",
                "assessment": "high",
                "explanation": "Magnetic core enables easy separation; 5 cycles demonstrated",
            },
        ],
        "evidence_tracking": {
            "total_claims": 8,
            "evidence_backed": 7,
            "unsubstantiated": 1,
            "key_evidence": [
                {
                    "claim": "qmax = 185.2 mg/g for Pb2+",
                    "evidence_type": "experimental_data",
                    "location": "Table 2",
                    "quality": "reliable",
                },
            ],
        },
    }


@pytest.fixture
def feature_mapping(biomimetic_lib):
    """Load the real feature-mapping.json."""
    path = biomimetic_lib / "feature-mapping.json"
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return None
