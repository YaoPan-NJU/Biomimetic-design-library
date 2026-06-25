# PFOA Honest Failure Slice (2026-06-25)

## Purpose
Demonstrate correct behavior for weak-domain queries: all candidates should be inference/exploratory with caveat, no fact/lead冒充.

## PFOA Query: `pfoa_痕量吸附去除`
- Water quality: pH 7, temperature 25, salinity medium
- Constraints: 水稳定性, 可再生, 低二次污染

## Results

| Candidate | honesty | lane | caveat |
|-----------|---------|------|--------|
| chitosan | inference | exploratory | organic micropollutant evidence weak |
| diatom-frustule | inference | exploratory | organic micropollutant evidence weak |
| polydopamine-coating | inference | exploratory | organic micropollutant evidence weak |

**3/3 inference/exploratory** ✓ — no fact/lead冒充

## Key Fixes Applied
1. **Organic domain gating**: `domain=organic` + `direct_evidence=False` → forced `candidate_honesty=inference`, `lane=exploratory`
2. **domain_caveat**: auto-added "organic micropollutant evidence weak" for organic pollutants without direct evidence
3. **Lane field**: added to all candidates (fact/lead/exploratory/blocked)

## Verification
- `verify_adrmats_delivery.py`: 6/6 PASS (PFOA now passes)
- `check_brief_do_not_behavior.py`: PASS
- `check_brief_usefulness.py`: 7/7 PASS
