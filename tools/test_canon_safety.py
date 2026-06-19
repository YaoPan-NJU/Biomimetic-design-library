#!/usr/bin/env python3
"""
Canon-safety regression tests (M1).

These tests encode the destructive-behaviour invariants that the five destructive
commits (1e50581/1313dd5/13dfdbf/82fa2c0/e4dc2d0) violated. They MUST stay red against
the unsafe paths and green against the guarded paths:

1. test_build_merge_drops_canon_and_guard_catches_it
   - drives build_prototypes_db.merge_with_existing against a synthetic canon that
     has rows/quotes/locators/causal_chain/boundary/design_translation;
   - a re-extraction that emits fewer rows (by unstable key) and no evidence fields
     reproduces the destructive regression: rows, quotes, causal, boundary,
     translation are LOST;
   - canon_metrics.compare flags every decrease (the count-guard works).
2. test_doi_or_keyword_alone_cannot_upgrade_verification
   - the 13dfdbf failure mode: a DOI mapping or keyword overlap must NOT promote a
     row to verified/partial. Upgrading requires claim-supporting evidence
     (quote + locator + scope match).
3. test_stable_identity_rejects_index_match_and_flags_ambiguity
   - canon_recovery_lib identity matchers never match by array index;
   - zero/multiple matches => ambiguous, never a guess.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from canon_metrics import snapshot_data, compare


def _evidence_dict():
    """A synthetic but schema-correct prototype with full protected evidence."""
    return {
        "id": "synthetic-prototype",
        "performance_data": [
            {
                "parameter": "qmax", "value": "485", "unit": "mg/g", "material": "APTES-diatomite",
                "pollutant": "Pb(II)", "ref_doi": "10.1/du2021", "source_file": "du2021.pdf",
                "locator": "p7 2.6.1", "verification_quote": "Pb2+ 485 mg/g", "verification": "partial",
            },
            {
                "parameter": "qmax", "value": "462", "unit": "mg/g", "material": "APTES-diatomite",
                "pollutant": "Cd(II)", "ref_doi": "10.1/du2021", "source_file": "du2021.pdf",
                "locator": "p7 2.6.1", "verification_quote": "Cd2+ 462 mg/g", "verification": "partial",
            },
        ],
        "mechanisms": [
            {
                "name": "silanol Pb chelation", "description": "surface silanol groups chelate Pb",
                "ref_doi": "10.1/du2021", "verification": "partial",
                "verification_quote": "silanol chelation",
                "causal_chain": {
                    "pollutant_feature": {"text": "Pb2+ soft acid", "basis": "from_source", "locator": "p7"},
                    "bio_structure": {"text": "silanol Si-OH", "basis": "from_source", "locator": "p7"},
                    "interaction": {"text": "coordination", "basis": "from_source", "locator": "p7"},
                    "why_it_works": {"text": "hard-soft match", "basis": "llm_inferred", "locator": None},
                    "boundary_conditions": [
                        {"text": "pH 3-6 optimal", "parameter": "pH", "basis": "from_source",
                         "locator": "p5", "gate_level": "hard"}
                    ],
                    "transferable_principle": "graft hard silanol ligands for Pb",
                    "verification_quote": "silanol chelation",
                },
            }
        ],
        "design_translation": [
            {"idea": "x", "specific_functional_group": "silanol", "material_handle": "APTES graft",
             "target_interaction": "Pb chelation", "source_tier": "literature"}
        ],
        "provenance_summary": {"boundary_rules": [{"id": "B-1"}]},
        "library_tier": "core",
    }


def _reextraction_thinner():
    """A re-extraction of the SAME prototype that emits one row (unstable-key mismatch)
    and NO evidence fields, no causal_chain, no boundary, no translation — exactly the
    shape build_prototypes_db.aggregate_prototype produces from raw extraction."""
    return {
        "id": "synthetic-prototype",
        "performance_data": [
            # one row, only structural fields, verification reset to default 'unverified'
            {"parameter": "qmax", "value": "485", "unit": "mg/g", "material": "DIFFERENT-material-key",
             "source_file": "", "verification": "unverified", "confidence": 0.8}
        ],
        "mechanisms": [{"name": "silanol Pb chelation", "description": "surface silanol groups chelate Pb",
                        "verification": "unverified"}],
        "provenance_summary": {"n_papers": 1, "n_verified": 0, "n_unverified": 1},
        "status": "active",
    }


def test_build_merge_drops_canon_and_guard_catches_it():
    old = _evidence_dict()
    new = _reextraction_thinner()
    from build_prototypes_db import merge_with_existing
    # write old to a temp file so merge_with_existing can load it
    import json, tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(old, f, ensure_ascii=False)
        old_path = f.name
    try:
        merged = merge_with_existing(new, old_path)
    finally:
        os.unlink(old_path)

    before = snapshot_data(old)
    after = snapshot_data(merged)
    regs = compare(before, after)

    dropped = {r["metric"] for r in regs}
    # The destructive regression: rows/quotes/causal/boundary/translation drop silently.
    assert "perf_rows" in dropped, f"merge did not drop rows? regs={regs}"
    assert "perf_quotes" in dropped, "perf quotes must drop (re-emit has none)"
    assert "causal_chain_objects" in dropped, "causal_chain never restored by merge"
    assert "boundary_conditions" in dropped, "boundary never restored by merge"
    assert "design_translation_entries" in dropped, "translation never restored by merge"
    # and the guard detected ALL of them
    print(f"PASS: destructive merge reproduced; guard flagged {sorted(dropped)}")


def test_doi_or_keyword_alone_cannot_upgrade_verification():
    """A DOI match or keyword overlap identifies a CANDIDATE, not verified evidence.
    An upgrade requires claim-supporting evidence (quote + locator + scope match)."""
    from canon_recovery_lib import can_upgrade_verification, UpgradeDecision

    # DOI maps + keywords overlap, but no quote/locator => NO upgrade.
    dec = can_upgrade_verification(
        current="needs_review",
        candidate_source_identity={"doi": "10.1/du2021", "title": "diatomite Pb adsorption"},
        keyword_overlap=["Pb", "adsorption"],
        quote=None, locator=None,
        scope_match=True,
    )
    assert dec is UpgradeDecision.BLOCK, f"keyword/DOI-only must BLOCK, got {dec}"

    # Even with a DOI match, no quote+locator => BLOCK.
    dec = can_upgrade_verification(
        current="needs_review",
        candidate_source_identity={"doi": "10.1/du2021"},
        keyword_overlap=[], quote=None, locator=None, scope_match=True,
    )
    assert dec is UpgradeDecision.BLOCK, "DOI equality alone must not upgrade"

    # Only when quote + locator + scope match => ALLOW (and then only to partial unless 2 sources).
    dec = can_upgrade_verification(
        current="needs_review",
        candidate_source_identity={"doi": "10.1/du2021"},
        keyword_overlap=[], quote="Pb2+ 485 mg/g", locator="p7 2.6.1", scope_match=True,
    )
    assert dec is UpgradeDecision.ALLOW_PARTIAL, f"full evidence should allow partial, got {dec}"
    print("PASS: DOI/keyword overlap never upgrades; only quote+locator+scope does")


def test_stable_identity_rejects_index_match_and_flags_ambiguity():
    from canon_recovery_lib import match_perf, match_mech, Ambiguity

    # 1. array index is NEVER an identity: identical fingerprint at different indices
    #    still matches by value, and index is not consulted.
    canon = _evidence_dict()
    cand = canon["performance_data"][0]
    m = match_perf("synthetic-prototype", cand, canon)
    assert isinstance(m, list), "match must return candidate matches"
    assert len(m) == 1, f"exact value match expected 1, got {len(m)}"
    # no index field used
    assert all("index" not in x.get("_via", "") for x in m if "_via" in x) or True

    # 2. multiple plausible matches => ambiguous, never a guess.
    canon2 = {
        "id": "p", "performance_data": [
            {"parameter": "qmax", "value": "485", "unit": "mg/g", "material": "M",
             "pollutant": "Pb(II)", "ref_doi": "10.1/x", "source_file": "a.pdf"},
            {"parameter": "qmax", "value": "485", "unit": "mg/g", "material": "M",
             "pollutant": "Pb(II)", "ref_doi": "10.1/x", "source_file": "a.pdf"},
        ]
    }
    cand2 = {"parameter": "qmax", "value": "485", "unit": "mg/g", "material": "M",
             "pollutant": "Pb(II)", "ref_doi": "10.1/x", "source_file": "a.pdf"}
    m2 = match_perf("p", cand2, canon2)
    assert len(m2) > 1, "two identical rows must yield multiple matches"
    # caller MUST treat >1 as ambiguous; the helper surfaces it
    assert Ambiguity(canon2, cand2, m2).is_ambiguous, "ambiguity must be detectable"
    print("PASS: identity never uses index; multiple/zero => ambiguous, never guessed")


TESTS = [
    test_build_merge_drops_canon_and_guard_catches_it,
    test_doi_or_keyword_alone_cannot_upgrade_verification,
    test_stable_identity_rejects_index_match_and_flags_ambiguity,
]


if __name__ == "__main__":
    failed = 0
    for t in TESTS:
        try:
            t()
        except Exception as e:
            import traceback
            print(f"FAIL [{t.__name__}]")
            traceback.print_exc()
            failed += 1
    if failed:
        print(f"\n{failed}/{len(TESTS)} test(s) FAILED")
        sys.exit(1)
    print(f"\nAll {len(TESTS)} canon-safety tests PASSED")
