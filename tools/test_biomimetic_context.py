#!/usr/bin/env python3
"""
Unit tests for BiomimeticContext ADRMATS adapter capabilities.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from biomimetic_context import BiomimeticContext

def test_do_not_list():
    """Test do_not_list gate."""
    ctx = BiomimeticContext()

    # Test with a prototype that has boundary rules
    dns = ctx.get_do_not_list('chitosan')
    assert isinstance(dns, list), "do_not_list should return a list"

    # Test with non-existent prototype
    dns = ctx.get_do_not_list('nonexistent')
    assert dns == [], "Non-existent prototype should return empty list"

    print("✅ test_do_not_list passed")

def test_design_translation():
    """Test design_translation decomposition."""
    ctx = BiomimeticContext()

    # Test with a valid prototype
    dt = ctx.decompose_design_translation('chitosan')
    assert dt['status'] == 'structured', f"Expected 'structured', got {dt['status']}"
    assert 'idea' in dt, "Should have 'idea' field"
    assert 'transferable_principles' in dt, "Should have 'transferable_principles'"
    assert len(dt['transferable_principles']) > 0, "Should have at least 1 transferable principle"

    # Test with non-existent prototype
    dt = ctx.decompose_design_translation('nonexistent')
    assert dt['status'] == 'not_found', "Non-existent should return 'not_found'"

    print("✅ test_design_translation passed")

def test_charge_state():
    """Test charge_state/pKa context."""
    ctx = BiomimeticContext()

    # Chitosan should have charge state (amino groups)
    cs = ctx.get_charge_state_context('chitosan')
    assert cs['has_charge_state'] == True, "Chitosan should have charge state"
    assert cs['ph_sensitive'] == True, "Chitosan should be pH sensitive"

    # Non-existent prototype
    cs = ctx.get_charge_state_context('nonexistent')
    assert cs['has_charge_state'] == False, "Non-existent should return False"

    print("✅ test_charge_state passed")

def test_relevance_gating():
    """Test relevance gating (query-conditioned selection)."""
    ctx = BiomimeticContext()

    # Chitosan should be relevant to Pb(II) adsorption
    rel = ctx.compute_relevance_score('chitosan', 'Pb(II) adsorption heavy metal removal')
    assert rel['is_relevant'] == True, "Chitosan should be relevant to Pb(II)"
    assert rel['score'] > 0, "Score should be > 0"

    # Lotus-leaf should be excluded for adsorption queries (surface physics)
    rel = ctx.compute_relevance_score('lotus-leaf', 'PFOA adsorption removal')
    assert rel['is_relevant'] == False, "Lotus should be excluded for adsorption"

    # Non-existent prototype
    rel = ctx.compute_relevance_score('nonexistent', 'Pb(II)')
    assert rel['score'] == 0, "Non-existent should have score 0"

    print("✅ test_relevance_gating passed")

def test_gate_mechanisms():
    """Test mechanism gating by query."""
    ctx = BiomimeticContext()

    # Gate mussel-foot-adhesion by Pb(II) query
    indices = ctx.gate_mechanisms_by_query('mussel-foot-adhesion', 'Pb(II) lead adsorption')
    assert len(indices) > 0, "Should find relevant mechanisms for Pb(II)"

    # Gate by unrelated query
    indices = ctx.gate_mechanisms_by_query('mussel-foot-adhesion', 'quantum computing')
    assert len(indices) == 0, "Should find no mechanisms for unrelated query"

    print("✅ test_gate_mechanisms passed")

def test_direct_evidence_requires_verified_pollutant_performance():
    """Text-only mappings must not be promoted to direct evidence."""
    ctx = BiomimeticContext()

    assert ctx.find_direct_evidence('PFOA') == [], "PFOA mappings are inspiration-only"
    assert ctx.find_direct_evidence('BPA') == [], "BPA mappings are inspiration-only"

    lead_ids = {item['prototype_id'] for item in ctx.find_direct_evidence('Pb(II)')}
    assert 'mussel-foot-adhesion' in lead_ids, "Verified Pb(II) performance should remain direct"

    print("✅ test_direct_evidence_requires_verified_pollutant_performance passed")

def test_partial_source_backed_performance_is_a_lead():
    """Partial, source-located removal data must survive without becoming a fact."""
    ctx = BiomimeticContext()

    lead_ids = {item['prototype_id'] for item in ctx.find_performance_leads('PFOA')}
    assert 'plant-lignocellulosic-architecture' in lead_ids

    candidates = ctx.query('PFOA', {}, [])['brief']['candidates']
    plant = next(item for item in candidates if item['prototype_id'] == 'plant-lignocellulosic-architecture')
    assert plant['lane'] == 'lead'
    assert plant['candidate_honesty'] == 'lead'
    assert plant['match']['direct_evidence'] is False
    assert plant['match']['performance_evidence_tier'] == 'lead'
    assert plant['evidence_context']['performance_leads'][0]['source']
    assert plant['evidence_context']['performance_leads'][0]['locator']

    print("✅ test_partial_source_backed_performance_is_a_lead passed")

def test_short_pollutant_aliases_do_not_cross_match():
    """CR must not match Cr(VI), and U must not match Cu."""
    ctx = BiomimeticContext()

    cr_ids = {
        item['prototype_id']
        for item in ctx.find_direct_evidence('CR') + ctx.find_performance_leads('CR')
    }
    assert 'chitosan' not in cr_ids
    assert 'plant-tannin' in cr_ids

    uranium_ids = {
        item['prototype_id']
        for item in ctx.find_direct_evidence('U(VI)') + ctx.find_performance_leads('U(VI)')
    }
    assert 'wood-xylem' not in uranium_ids
    chitosan = ctx.prototypes['chitosan']
    assert all('Cr(VI)' not in item['pollutant'] for item in ctx._get_performance_leads(chitosan, 'CR'))

    print("✅ test_short_pollutant_aliases_do_not_cross_match passed")

def test_pollutant_mapping_stays_inspiration():
    """Explicit source-project mappings remain discoverable without evidence inflation."""
    ctx = BiomimeticContext()
    smx = ctx.find_pollutant_inspiration('SMX')

    assert smx and smx[0]['prototype_id'] == 'dhps-dihydropteroate-synthase-paba-recognition'
    assert all(not candidate['direct_evidence'] for candidate in smx)
    assert all(candidate['mapping_source'] == 'pollutant_prototype_map' for candidate in smx)

    print("✅ test_pollutant_mapping_stays_inspiration passed")

def test_pollutant_mapping_requires_source_grounding_and_keeps_lane_diversity():
    """Unrelated verified cards cannot inflate a mapping or crowd out discovery."""
    ctx = BiomimeticContext()
    mapped = ctx.find_pollutant_inspiration('PFOA')

    fabp4 = next(item for item in mapped if item['prototype_id'] == 'fabp4-fatty-acid-pfas-binding')
    assert fabp4['mapping_quality'] == 'source_grounded_inspiration'
    assert mapped[0]['mapping_quality'] == 'source_grounded_inspiration'

    candidates = ctx.query('PFOA', {}, [])['brief']['candidates']
    explicit = [c for c in candidates if c['match']['mapping_source'] == 'pollutant_prototype_map']
    assert len(explicit) <= 8
    assert any(c['match']['match_basis'] == 'mechanism_feature_bridge' for c in candidates)

    print("✅ test_pollutant_mapping_requires_source_grounding_and_keeps_lane_diversity passed")

def test_use_case_can_select_background_mechanisms():
    """Explicit separation queries may use otherwise hidden surface-physics mechanisms."""
    ctx = BiomimeticContext()
    candidates = ctx.query('oil-water', {}, [])['brief']['candidates']

    assert candidates, "Oil-water use case should return separation prototypes"
    assert all(item['match']['match_basis'] == 'use_case_mapping' for item in candidates)
    background_ids = {'lotus-leaf', 'superhydrophobic-artificial', 'water-strider-leg'}
    for item in candidates:
        if item['prototype_id'] in background_ids:
            assert item['prototype_status']['is_background']
    for item in candidates:
        if item['prototype_id'] in {'lotus-leaf', 'superhydrophobic-artificial'}:
            assert '超疏水' in item['mechanism']['name'] or '油水' in item['mechanism']['name']

    print("✅ test_use_case_can_select_background_mechanisms passed")

def test_mechanism_lane_binds_selected_mechanism():
    """A mechanism-lane hit must render one of the mechanisms that caused the hit."""
    ctx = BiomimeticContext()
    candidates = ctx.query('Roxithromycin', {}, [])['brief']['candidates']

    mechanism_hits = [c for c in candidates if c['match']['match_basis'] == 'mechanism_feature_bridge']
    assert mechanism_hits, "Roxithromycin should retain mechanism-based inspiration"
    for candidate in mechanism_hits:
        matched_ids = candidate['match']['matched_mechanism_ids']
        assert matched_ids, f"{candidate['prototype_id']} lacks a concrete mechanism binding"
        assert candidate['mechanism']['mechanism_id'] in matched_ids

    print("✅ test_mechanism_lane_binds_selected_mechanism passed")

def main():
    print("=== BiomimeticContext Unit Tests ===\n")

    try:
        test_do_not_list()
        test_design_translation()
        test_charge_state()
        test_relevance_gating()
        test_gate_mechanisms()
        test_direct_evidence_requires_verified_pollutant_performance()
        test_partial_source_backed_performance_is_a_lead()
        test_short_pollutant_aliases_do_not_cross_match()
        test_pollutant_mapping_stays_inspiration()
        test_pollutant_mapping_requires_source_grounding_and_keeps_lane_diversity()
        test_use_case_can_select_background_mechanisms()
        test_mechanism_lane_binds_selected_mechanism()
        print("\n✅ All tests passed!")
        return 0
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Test error: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
