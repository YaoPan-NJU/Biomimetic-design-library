#!/usr/bin/env python3
"""
Tests for R1-B apply_recovery.py — stable identity matching, ambiguity gate, deterministic IDs.

Tests cover:
- zero target: no match → skip (no crash)
- two targets same value: reject (ambiguous)
- two targets different value: reject (ambiguous)
- exactly one target: accept (apply)
- deterministic ID: two independent processes produce same ID
- mechanism must NOT write perf_1 (correct identity level per type)
"""
import os
import sys
import json
import hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _make_perf_row(parameter="qmax", value="100", material="M", unit="mg/g",
                   ref_doi="10.1/test", source_file="test.pdf",
                   verification_quote=None, locator=None, pollutant=None):
    row = {
        "parameter": parameter, "value": value, "material": material, "unit": unit,
        "ref_doi": ref_doi, "source_file": source_file,
    }
    if verification_quote:
        row["verification_quote"] = verification_quote
    if locator:
        row["locator"] = locator
    if pollutant:
        row["pollutant"] = pollutant
    return row


def _make_mech_row(name="test mechanism", description="test desc",
                   ref_doi="10.1/test", source_file="test.pdf",
                   verification_quote=None, source_file_field=None):
    row = {
        "name": name, "description": description,
        "ref_doi": ref_doi, "source_file": source_file,
    }
    if verification_quote:
        row["verification_quote"] = verification_quote
    if source_file_field:
        row["source_file"] = source_file_field
    return row


def test_identity_match_zero():
    """Zero matches: should return None for all identity levels."""
    from canon_recovery_lib import perf_fingerprint, mech_fingerprint
    from apply_recovery import _identity_match

    head = _make_perf_row(parameter="qmax", value="100", material="M")
    hist = _make_perf_row(parameter="adsorption", value="200", material="N")
    result = _identity_match(head, hist, "perf")
    assert result is None, f"Expected None for zero match, got {result}"
    print("PASS: zero match returns None")


def test_identity_match_exact_one():
    """Exactly one match: should return the correct level."""
    from apply_recovery import _identity_match

    head = _make_perf_row(parameter="qmax", value="100", material="M", ref_doi="10.1/test")
    hist = _make_perf_row(parameter="qmax", value="100", material="M", ref_doi="10.1/test")
    result = _identity_match(head, hist, "perf")
    assert result == "perf_1", f"Expected perf_1, got {result}"
    print("PASS: exact match returns perf_1")


def test_identity_match_two_same_value():
    """Two targets with same value: apply_row should reject as ambiguous."""
    from apply_recovery import apply_row

    head = _make_perf_row(parameter="qmax", value="100", material="M")
    hist1 = _make_perf_row(parameter="qmax", value="100", material="M", ref_doi="10.1/a",
                            verification_quote="qmax 100 mg/g from source A")
    hist2 = _make_perf_row(parameter="qmax", value="100", material="M", ref_doi="10.1/b",
                            verification_quote="qmax 100 mg/g from source A")
    hist1["_commit"] = "aaa"; hist2["_commit"] = "bbb"

    changes, ambiguous = apply_row("test", head, [hist1, hist2], "perf", set())
    assert len(changes) == 0, f"Expected 0 changes, got {len(changes)}"
    assert len(ambiguous) > 0, f"Expected ambiguous fields, got {len(ambiguous)}"
    print("PASS: two targets same value → ambiguous, no changes")


def test_identity_match_two_different_values():
    """Two targets with different values: should reject as ambiguous."""
    from apply_recovery import apply_row

    head = _make_perf_row(parameter="qmax", value="100", material="M")
    hist1 = _make_perf_row(parameter="qmax", value="100", material="M", ref_doi="10.1/a",
                            verification_quote="qmax 100 from A")
    hist2 = _make_perf_row(parameter="qmax", value="100", material="M", ref_doi="10.1/b",
                            verification_quote="qmax 200 from B")
    hist1["_commit"] = "aaa"; hist2["_commit"] = "bbb"

    changes, ambiguous = apply_row("test", head, [hist1, hist2], "perf", set())
    assert len(changes) == 0, f"Expected 0 changes, got {len(changes)}"
    assert len(ambiguous) > 0, f"Expected ambiguous fields, got {len(ambiguous)}"
    print("PASS: two targets different values → ambiguous, no changes")


def test_identity_match_exactly_one():
    """Exactly one target: should apply."""
    from apply_recovery import apply_row

    head = _make_perf_row(parameter="qmax", value="100", material="M")
    hist = _make_perf_row(parameter="qmax", value="100", material="M", ref_doi="10.1/test",
                           verification_quote="qmax 100 mg/g confirmed", locator="p7")
    hist["_commit"] = "aaa"

    changes, ambiguous = apply_row("test", head, [hist], "perf", set())
    assert len(changes) == 2, f"Expected 2 changes (verification_quote + locator), got {len(changes)}"
    assert len(ambiguous) == 0, f"Expected 0 ambiguous, got {len(ambiguous)}"
    assert changes[0]["level"] == "perf_1", f"Expected perf_1, got {changes[0]['level']}"
    print("PASS: exactly one target → applied with correct level")


def test_mech_identity_level():
    """Mechanism identity must use mech_1/mech_2/mech_3, never perf_1."""
    from apply_recovery import apply_row

    head = _make_mech_row(name="test", description="desc", ref_doi="10.1/test")
    hist = _make_mech_row(name="test", description="desc", ref_doi="10.1/test",
                          verification_quote="test mechanism confirmed")
    hist["_commit"] = "aaa"

    changes, ambiguous = apply_row("test", head, [hist], "mech", set())
    assert len(changes) >= 1, f"Expected at least 1 change, got {len(changes)}"
    for c in changes:
        assert c["level"].startswith("mech_"), f"Expected mech_*, got {c['level']}"
    print("PASS: mechanism uses mech_* level, never perf_1")


def test_deterministic_id():
    """Ledger ID must be deterministic across processes (SHA-256, not hash())."""
    from apply_recovery import _stable_ledger_id

    id1 = _stable_ledger_id("test-pid", "performance_data[0].qmax", "perf_1:10.1/test:qmax")
    id2 = _stable_ledger_id("test-pid", "performance_data[0].qmax", "perf_1:10.1/test:qmax")
    assert id1 == id2, f"IDs should be identical: {id1} vs {id2}"
    assert id1.startswith("R-test-pid-"), f"ID format wrong: {id1}"
    # Verify it's SHA-256 based, not Python hash()
    content = "test-pid|performance_data[0].qmax|perf_1:10.1/test:qmax"
    expected_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()[:12]
    assert expected_hash in id1, f"Expected SHA-256 hash in ID: {id1}"
    print("PASS: deterministic ID uses SHA-256")


def test_no_pending_in_ledger():
    """Ledger entries must not have applied_commit=PENDING."""
    from apply_recovery import main, _current_commit
    # This is a structural check: verify the code doesn't produce PENDING
    import inspect
    source = inspect.getsource(main)
    assert "PENDING" not in source, "main() should not produce PENDING entries"
    print("PASS: no PENDING in main()")


def test_no_array_index_identity():
    """Array index must never be used as identity."""
    import inspect
    from apply_recovery import apply_row
    source = inspect.getsource(apply_row)
    # Check that no array index is used in identity matching
    assert "[i]" not in source.split("_identity_match")[0], "Array index used before identity match"
    print("PASS: no array index in identity matching")


TESTS = [
    test_identity_match_zero,
    test_identity_match_exact_one,
    test_identity_match_two_same_value,
    test_identity_match_two_different_values,
    test_identity_match_exactly_one,
    test_mech_identity_level,
    test_deterministic_id,
    test_no_pending_in_ledger,
    test_no_array_index_identity,
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
    print(f"\nAll {len(TESTS)} apply-recovery tests PASSED")
