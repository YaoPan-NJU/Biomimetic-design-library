"""Tests for update_feature_mapping.py."""

import copy
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from update_feature_mapping import (
    compute_evidence_weight,
    update_pollutant_weights,
    update_feature_weights,
    update_feature_mapping,
)


class TestComputeEvidenceWeight:
    def test_high_confidence_experimental(self):
        w = compute_evidence_weight(
            confidence="high", data_source="experimental", match_confidence="high"
        )
        assert 0.5 <= w <= 1.0

    def test_low_confidence_estimated(self):
        w = compute_evidence_weight(
            confidence="low", data_source="estimated", match_confidence="low"
        )
        assert 0.0 < w < 0.5

    def test_none_inputs_returns_minimum(self):
        w = compute_evidence_weight(None, None, None)
        assert w == 0.1


class TestUpdatePollutantWeights:
    def test_adds_new_prototype_entry(self):
        fm = {
            "pollutant_prototype_map": {
                "重金属": {
                    "Pb2+": {
                        "prototypes": [
                            {"id": "chitosan", "weight": 0.9, "mechanism_summary": "", "design_hint": ""}
                        ]
                    }
                }
            }
        }
        perf = [{"pollutant": "Pb2+", "qmax_mg_g": 200, "confidence": "high", "data_source": "experimental"}]
        updated = update_pollutant_weights(fm, "mussel-foot-adhesion", perf, "配位螯合")
        proto_list = updated["pollutant_prototype_map"]["重金属"]["Pb2+"]["prototypes"]
        ids = [p["id"] for p in proto_list]
        assert "mussel-foot-adhesion" in ids

    def test_does_not_overwrite_higher_weight(self):
        fm = {
            "pollutant_prototype_map": {
                "重金属": {
                    "Pb2+": {
                        "prototypes": [
                            {"id": "mussel-foot-adhesion", "weight": 0.95, "mechanism_summary": "", "design_hint": ""}
                        ]
                    }
                }
            }
        }
        perf = [{"pollutant": "Pb2+", "qmax_mg_g": 100, "confidence": "medium", "data_source": "reported"}]
        updated = update_pollutant_weights(fm, "mussel-foot-adhesion", perf, "配位螯合")
        proto_list = updated["pollutant_prototype_map"]["重金属"]["Pb2+"]["prototypes"]
        mussel = [p for p in proto_list if p["id"] == "mussel-foot-adhesion"][0]
        assert mussel["weight"] == 0.95  # not overwritten


class TestUpdateFeatureWeights:
    def test_updates_existing_feature_weight(self):
        fm = {
            "feature_prototype_map": {
                "邻苯二酚基团": {
                    "dimension": "化学性质",
                    "description": "catechol",
                    "prototypes": [
                        {"id": "mussel-foot-adhesion", "weight": 0.8}
                    ]
                }
            }
        }
        updated = update_feature_weights(fm, "mussel-foot-adhesion", ["邻苯二酚基团"], 0.9)
        proto = updated["feature_prototype_map"]["邻苯二酚基团"]["prototypes"][0]
        assert proto["weight"] == 0.9

    def test_adds_new_prototype_to_feature(self):
        fm = {
            "feature_prototype_map": {
                "邻苯二酚基团": {
                    "dimension": "化学性质",
                    "description": "catechol",
                    "prototypes": []
                }
            }
        }
        updated = update_feature_weights(fm, "polydopamine-coating", ["邻苯二酚基团"], 0.85)
        protos = updated["feature_prototype_map"]["邻苯二酚基团"]["prototypes"]
        assert any(p["id"] == "polydopamine-coating" for p in protos)


class TestUpdateFeatureMapping:
    def test_full_update_returns_dict(self):
        fm = {
            "pollutant_prototype_map": {"重金属": {"Pb2+": {"prototypes": []}}},
            "feature_prototype_map": {"邻苯二酚基团": {"dimension": "化学性质", "description": "", "prototypes": []}},
            "prototype_metadata": {},
            "mechanism_feature_bridge": {},
            "constraint_prototype_map": {},
        }
        aggregated = {
            "mussel-foot-adhesion": {
                "performance_data": [
                    {"pollutant": "Pb2+", "qmax_mg_g": 200, "confidence": "high", "data_source": "experimental"}
                ],
                "mechanism_analysis": [
                    {"mechanism_name": "配位螯合", "key_functional_groups": [{"group": "邻苯二酚基团", "role": "coordination"}]}
                ],
                "engineering_constraints": [],
                "papers": [{"paper_id": "test", "confidence": "high"}],
            }
        }
        result = update_feature_mapping(fm, aggregated)
        assert isinstance(result, dict)
        assert "pollutant_prototype_map" in result
