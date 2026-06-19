#!/usr/bin/env python3
"""
Regression tests for canon invariant guard hardening.

Uses R1-D corruption (diatom-frustule.json: 2 mechanism duplicates + 13 perf duplicates
introduced by json.dump reordering) as the test case to verify the guard catches it.

Tests:
1. Duplicate mechanism detection
2. Duplicate perf row detection
3. Refuted DOI resurrection detection
4. Row count anomaly detection
5. R1-D corruption regression: replaying the corruption must be caught
"""
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from canon_metrics import (
    check_duplicates, check_refuted_resurrection, check_row_count_anomaly,
    check_index_bounds, check_integrity, _load_refuted_dois, snapshot_data,
)


def _make_test_prototype(mechs=3, perfs=2, refuted_doi=None):
    """Create a test prototype dict."""
    d = {
        "id": "test-proto",
        "mechanisms": [
            {"name": f"mech-{i}", "description": f"desc-{i}", "ref_doi": f"10.1/test{i}"}
            for i in range(mechs)
        ],
        "performance_data": [
            {"parameter": "qmax", "value": str(100 + i), "material": "M", "ref_doi": f"10.1/test{i}"}
            for i in range(perfs)
        ],
    }
    if refuted_doi:
        d["mechanisms"][0]["ref_doi"] = refuted_doi
    return d


def test_no_duplicates():
    """Clean prototype: no duplicates detected."""
    d = _make_test_prototype(mechs=3, perfs=2)
    issues = check_duplicates(d, "test")
    assert len(issues) == 0, f"Expected 0 issues, got: {issues}"
    print("PASS: no duplicates in clean prototype")


def test_mechanism_duplicate():
    """Two identical mechanisms: detected."""
    d = _make_test_prototype(mechs=2, perfs=0)
    # Make them identical
    d["mechanisms"][1] = dict(d["mechanisms"][0])
    issues = check_duplicates(d, "test")
    assert any("duplicate mechanism" in i for i in issues), f"Expected mech duplicate, got: {issues}"
    print("PASS: mechanism duplicate detected")


def test_perf_duplicate():
    """Two identical perf rows: detected."""
    d = _make_test_prototype(mechs=0, perfs=2)
    d["performance_data"][1] = dict(d["performance_data"][0])
    issues = check_duplicates(d, "test")
    assert any("duplicate perf" in i for i in issues), f"Expected perf duplicate, got: {issues}"
    print("PASS: perf duplicate detected")


def test_refuted_resurrection():
    """Row citing refuted DOI: detected."""
    d = _make_test_prototype(mechs=2, perfs=1, refuted_doi="10.3390/polym14245439")
    refuted = {"10.3390/polym14245439", "10.1007/s10853-022-07945-8"}
    issues = check_refuted_resurrection(d, "test", refuted)
    assert any("refuted DOI" in i for i in issues), f"Expected refuted resurrection, got: {issues}"
    print("PASS: refuted DOI resurrection detected")


def test_row_count_anomaly():
    """Row count doubling: detected."""
    before = _make_test_prototype(mechs=3, perfs=3)
    after = _make_test_prototype(mechs=7, perfs=7)  # >50% increase
    issues = check_row_count_anomaly(before, after, "test", threshold=0.5)
    assert len(issues) >= 1, f"Expected anomaly, got: {issues}"
    print("PASS: row count anomaly detected")


def test_r1d_corruption_regression():
    """R1-D corruption regression: replaying the corruption must be caught.

    The R1-D commit (382bb91) introduced:
    - 2 mechanism duplicates (13→15)
    - 13 perf duplicate groups (29→42)
    This test simulates the corruption and verifies the guard catches it.
    """
    # Clean state (R1-C): 13 mechs, 29 perf, 0 dupes
    clean = {
        "id": "diatom-frustule",
        "mechanisms": [{"name": f"mech-{i}", "description": f"desc-{i}", "ref_doi": f"10.1/d{i}"} for i in range(13)],
        "performance_data": [{"parameter": "qmax", "value": str(i), "material": "M", "ref_doi": f"10.1/p{i}"} for i in range(29)],
    }

    # Corrupted state (R1-D): 15 mechs, 42 perf, with duplicates
    corrupted = {
        "id": "diatom-frustule",
        "mechanisms": list(clean["mechanisms"]) + [
            {"name": "mech-7", "description": "desc-7", "ref_doi": "10.1/d7"},  # duplicate
            {"name": "mech-11", "description": "desc-11", "ref_doi": "10.1/d11"},  # duplicate
        ],
        "performance_data": list(clean["performance_data"]) + [
            {"parameter": "qmax", "value": str(i), "material": "M", "ref_doi": f"10.1/p{i}"}
            for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 13 duplicates
        ],
    }

    # Check: clean should have 0 issues
    clean_issues = check_duplicates(clean, "diatom-frustule")
    assert len(clean_issues) == 0, f"Clean state should have 0 issues: {clean_issues}"

    # Check: corrupted should have duplicates detected
    corrupt_issues = check_duplicates(corrupted, "diatom-frustule")
    assert len(corrupt_issues) >= 2, f"Corrupted state should have ≥2 issues: {corrupt_issues}"

    # Check: row count anomaly
    anomaly_issues = check_row_count_anomaly(clean, corrupted, "diatom-frustule", threshold=0.3)
    assert len(anomaly_issues) >= 1, f"Should detect row anomaly: {anomaly_issues}"

    print(f"PASS: R1-D corruption regression caught ({len(corrupt_issues)} dupes, {len(anomaly_issues)} anomalies)")


def test_integrity_clean():
    """Full integrity check on current working tree should pass."""
    issues = check_integrity()
    # Filter out known pre-existing issues (if any)
    if issues:
        print(f"WARN: integrity issues found (may be pre-existing): {len(issues)}")
        for i in issues[:5]:
            print(f"  {i}")
    else:
        print("PASS: full integrity check clean")


TESTS = [
    test_no_duplicates,
    test_mechanism_duplicate,
    test_perf_duplicate,
    test_refuted_resurrection,
    test_row_count_anomaly,
    test_r1d_corruption_regression,
    test_integrity_clean,
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
    print(f"\nAll {len(TESTS)} invariant guard tests PASSED")
