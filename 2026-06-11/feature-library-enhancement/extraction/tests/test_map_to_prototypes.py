"""Tests for map_to_prototypes.py."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from map_to_prototypes import (
    load_vocabulary,
    load_prototype_routing,
    normalize_feature,
    normalize_mechanism,
    normalize_pollutant,
    match_prototypes,
    aggregate_by_prototype,
)


class TestLoadConfigs:
    def test_load_vocabulary(self, repo_root):
        vocab = load_vocabulary(repo_root / "config" / "vocabulary_mapping.json")
        assert "feature_mapping" in vocab
        assert "mechanism_mapping" in vocab
        assert "pollutant_mapping" in vocab

    def test_load_prototype_routing(self, repo_root):
        routing = load_prototype_routing(repo_root / "config" / "prototype_routing.json")
        assert "prototypes" in routing
        assert "mussel-foot-adhesion" in routing["prototypes"]


class TestNormalize:
    @pytest.fixture
    def vocab(self, repo_root):
        return load_vocabulary(repo_root / "config" / "vocabulary_mapping.json")

    def test_normalize_feature_exact_match(self, vocab):
        assert normalize_feature("catechol group", vocab) == "邻苯二酚基团"

    def test_normalize_feature_case_insensitive(self, vocab):
        assert normalize_feature("DOPA", vocab) == "邻苯二酚基团"

    def test_normalize_feature_unknown_returns_original(self, vocab):
        assert normalize_feature("unknown_feature_xyz", vocab) == "unknown_feature_xyz"

    def test_normalize_mechanism(self, vocab):
        assert normalize_mechanism("coordination chelation", vocab) == "配位螯合"

    def test_normalize_pollutant(self, vocab):
        assert normalize_pollutant("methylene blue", vocab) == "阳离子染料"

    def test_normalize_pollutant_cd(self, vocab):
        assert normalize_pollutant("Cd(II)", vocab) == "Cd2+"


class TestMatchPrototypes:
    @pytest.fixture
    def routing(self, repo_root):
        return load_prototype_routing(repo_root / "config" / "prototype_routing.json")

    def test_match_mussel_keywords(self, routing):
        text = "mussel-inspired polydopamine coating for DOPA-mediated heavy metal removal"
        matches = match_prototypes(text, routing)
        ids = [m["prototype_id"] for m in matches]
        assert "mussel-foot-adhesion" in ids

    def test_match_lotus_keywords(self, routing):
        text = "superhydrophobic surface inspired by lotus leaf with Cassie-Baxter state"
        matches = match_prototypes(text, routing)
        ids = [m["prototype_id"] for m in matches]
        assert "lotus-leaf" in ids

    def test_match_threshold_filters_weak(self, routing):
        text = "a generic paper about water treatment"
        matches = match_prototypes(text, routing)
        assert len(matches) == 0

    def test_max_prototypes_limit(self, routing):
        text = "mussel DOPA lotus superhydrophobic chitosan alginate MOF diatom"
        matches = match_prototypes(text, routing)
        assert len(matches) <= routing["routing_rules"]["max_prototypes_per_paper"]


class TestAggregateByPrototype:
    def test_aggregate_groups_results(self, sample_extraction_result):
        results = [sample_extraction_result]
        aggregated = aggregate_by_prototype(results)
        assert "mussel-foot-adhesion" in aggregated
        assert "polydopamine-coating" in aggregated

    def test_aggregate_empty_list(self):
        aggregated = aggregate_by_prototype([])
        assert aggregated == {}

    def test_aggregate_normalizes_performance_data(self, sample_extraction_result, repo_root):
        vocab = load_vocabulary(repo_root / "config" / "vocabulary_mapping.json")
        results = [sample_extraction_result]
        aggregated = aggregate_by_prototype(results, vocab=vocab)
        mussel_data = aggregated.get("mussel-foot-adhesion", {})
        perf = mussel_data.get("performance_data", [])
        if perf:
            assert perf[0]["pollutant"] == "Pb2+"
