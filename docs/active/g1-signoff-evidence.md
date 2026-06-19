---
title: G1 Signoff Evidence Package
status: ready_for_review
date: 2026-06-19
author: claude-code (coordinator)
baseline_commit: 8578ff3
---

# G1 Signoff Evidence Package

## Section 1: R1-D Semantic Diff Analysis

### Intended Change
R1-D (commit `382bb91`) was intended to downgrade 9+1 mechanisms in `diatom-frustule.json`
from `partial` to `needs_review`, with no other semantic changes.

### Actual Changes (CRITICAL FINDING)

**9 verification downgrades confirmed** — the intended changes were applied:
- mechanisms[4]-[12] (by index in R1-C parent): `partial` → `needs_review`
- All 9 had `scope_note` added: "R1-D corrective downgrade"

**UNINTENDED side effects introduced by R1-D:**

| Issue | Count | Description |
|-------|-------|-------------|
| Mechanism duplicates | 2 pairs | "吸附机制（物理吸附为主）" and "离子强度影响" each appear twice |
| Performance row duplicates | 13 groups | 13 perf row key combinations now have 2 copies each |
| Mechanism count increase | +2 | 13 → 15 mechanisms (due to duplicates) |
| Perf count increase | +13 | 29 → 42 performance rows (due to duplicates) |

**Root cause**: The R1-D commit rewrote the entire `diatom-frustule.json` via
`json.dump()`. The Python script used `mechs[i]` index-based access which matched
the WRONG mechanisms after the array was reordered during serialization. This caused
content to be written to wrong positions, creating duplicates.

### Verification Commands

```bash
# Check mechanism duplicates
python3 -c "
import json, subprocess
r = subprocess.run(['git', 'show', 'HEAD:prototypes_db/diatom-frustule.json'], capture_output=True, text=True)
d = json.loads(r.stdout)
from collections import Counter
names = [m.get('name','') for m in d.get('mechanisms',[])]
dupes = {n:c for n,c in Counter(names).items() if c>1}
print(f'Duplicates: {dupes}')
"

# Expected: {'吸附机制（物理吸附为主）': 2, '离子强度影响': 2}

# Check perf duplicates
python3 -c "
import json, subprocess
r = subprocess.run(['git', 'show', 'HEAD:prototypes_db/diatom-frustule.json'], capture_output=True, text=True)
d = json.loads(r.stdout)
from collections import Counter
keys = [(p.get('parameter',''), p.get('value',''), p.get('material','')) for p in d.get('performance_data',[])]
dupes = sum(1 for k,v in Counter(keys).items() if v>1)
print(f'Perf duplicate groups: {dupes}')
"

# Expected: 13
```

### Impact Assessment
- The 9 verification downgrades are correct in intent
- The 2 mechanism duplicates and 13 perf duplicates are **data corruption**
- This must be corrected before G1 can pass
- Recommended: revert diatom-frustule.json to R1-C state, then re-apply ONLY verification changes

---

## Section 2: Ledger v2 628 Warnings Attribution

The 628 warnings from `validate_ledger_v2.py` are all **v1 migration artifacts**:

| Warning Type | Count | v1 Value | v2 Equivalent | Status |
|-------------|-------|----------|---------------|--------|
| Invalid disposition | 248 | `replaced` | `restored` | Migration gap |
| Invalid basis | 326 | `review` | `extraction` | Migration gap |
| Invalid level | 54 | `exact_fingerprint` | `perf_3` / `mech_3` | Migration gap |
| **Total** | **628** | | | All v1 migration |

**All 1,204 entries have `applied_commit=PENDING`** — none have been applied.
These are untrusted v1 migration input, not active ledger entries.

**0 actual schema errors** — the entries are structurally valid JSON with correct
required fields; only enum values need mapping.

---

## Section 3: validate_consistency 1 Error Attribution

The single error is:
```
❌ 错误:
  - 断链: ['cactus-spine', 'lotus-leaf', 'shark-skin', 'superhydrophobic-artificial', 'water-strider-leg']
```

**This is a pre-existing issue**, not caused by R1:
- These 5 separation prototypes have render directories disconnected from
  `prototypes/separation/`
- The error was present at the baseline before any R1 commits
- It is a documentation/rendering issue, not a canon data issue

---

## Section 4: Recommended G1 Disposition

**G1 CANNOT PASS in current state** due to the R1-D data corruption (Section 1).

**Required corrective action before G1:**
1. Revert `diatom-frustule.json` to the R1-C state (commit `ff98818`)
2. Re-apply ONLY the 9 verification downgrades using index-safe matching
3. Verify no duplicates are introduced
4. Re-run `canon_metrics.py --guard`

**Alternative**: Accept the duplicates as a known issue to be fixed in P1, with
the understanding that diatom-frustule is excluded from brief generation until fixed.
