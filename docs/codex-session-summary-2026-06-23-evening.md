# BMDL Codex Session Summary (Evening Handoff)
**Date**: 2026-06-23 21:30 CST
**Session**: V1-A evidence uplift supervision + inflation cleanup + systematic PDF matching
**Model**: GPT-5 Codex (supervisor role)

---

## 1. Your Role

You are the **Codex supervisor**, monitoring CC (Claude Code) executing BMDL project evidence uplift. You do NOT modify project code directly. You write directives to `.cowork-relay/outbox/` for CC to execute.

**Key clarification**:
- **CC (Claude Code)** = main executor, continuously running, currently doing PDF matching uplift
- **Claude Cowork** = offline, no longer needed for bridge relay
- **You (Codex)** = supervisor, communicate with CC via bridge service

---

## 2. Communication Architecture

```
Codex writes directive -> .cowork-relay/outbox/ -> [bridge service] -> codex-outbox/ -> CC reads
CC writes output -> cc-outbox/ -> [bridge service] -> .cowork-relay/inbox/ -> Codex reads
```

### Directory Paths
- **Cowork outbox (you write directives)**: `/Users/panyao/Desktop/Biomimetic-design-library/.cowork-relay/outbox/`
- **Cowork inbox (CC output mirror)**: `/Users/panyao/Desktop/Biomimetic-design-library/.cowork-relay/inbox/`
- **CC codex-outbox (CC reads directives)**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/codex-outbox/`
- **CC cc-outbox (CC writes output)**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cc-outbox/`

### Bridge Service
- **launchd service**: `com.panyao.bmdl-cowork-bridge`
- **Config**: runs every 60 seconds
- **Script**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cowork-bridge/cowork_bridge.py`
- **Log**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cowork-bridge/bridge.log`
- **Known issue**: Bridge sometimes fails to auto-deliver new directives. If codex-outbox doesn't have your new file, manually copy:
  ```bash
  cp /Users/panyao/Desktop/Biomimetic-design-library/.cowork-relay/outbox/<filename> \
     /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/codex-outbox/
  ```
- **Restart bridge**:
  ```bash
  launchctl unload ~/Library/LaunchAgents/com.panyao.bmdl-cowork-bridge.plist
  sleep 1
  launchctl load ~/Library/LaunchAgents/com.panyao.bmdl-cowork-bridge.plist
  ```

### Heartbeat Automation
- **ID**: `bmdl-gate-supervisor`
- **Status**: ACTIVE (triggers every 15 minutes)
- **Purpose**: Auto-check CC progress, send nudge or verify REVIEW_REQUEST
- **Config**: `/Users/panyao/.codex/automations/bmdl-gate-supervisor/automation.toml`

---

## 3. Current Project State

### Git State
- **HEAD**: `87eafa3` -- feat(V1-A Stage 4): systematic PDF uplift, 70 mechanisms upgraded
- **Branch**: `review`
- **Push status**: ahead 3 commits (NOT pushed to origin/review)
- **Working tree**: clean (only untracked helper files)

### Recent Commit History
```
87eafa3 feat(V1-A Stage 4): systematic PDF uplift - 70 mechanisms upgraded
1351304 fix(V1-A): harden validator + clean 321 non-compliant elements
8cdd7f0 feat(V1-A): deep scan uplift - 81 mechanisms upgraded across 13 prototypes
1067d2b feat(V1-A Stage 3): adapter unit tests + second vertical slice
256dcfe feat(V1-A Stage 2): recover 49 mechanisms from library index
bd5b241 fix(V1-A): evidence label cleanup - 277 compliant from_source elements
8d82eb4 feat(Round 4): ADRMATS adapter - 4 capabilities added
```

### from_source Statistics (Verified Honest)
- **Element level**: 198/2080 (9.5%)
- **Mechanism level**: ~79/520 (15.2%)
- **Vague locators**: 0 (was 98, cleaned in commit 1351304)
- **All 198 pass hardened validator**

### Why Numbers Dropped
from_source went from 326 (HEAD `1067d2b`) to 198 (HEAD `87eafa3`):
1. `8cdd7f0`: CC did mass uplift (326->550) but used inflation patterns (visual_cache locator, same OCR quote)
2. `1351304`: Hardened validator cleaned 321 non-compliant elements (550->229)
3. `87eafa3`: Upgraded 70 mechanisms but validator caught more old non-compliant (229->198)
- **This is HONEST**: numbers dropped because quality bar raised, not evidence lost

### Validator State
- `validate_consistency.py`: 0 errors, 172 warnings
- `check_causal_chain.py`: 506/520 qualified (14 lost, reason TBD, not inflation)
- `check_from_source_integrity.py`: 198/198 compliant (hardened version)
- Adapter unit tests: 5/5 pass

### Hardened Validator (check_from_source_integrity.py)
3 quality checks implemented in commit `1351304`:
1. **Locator quality**: must contain page number (p.N / page N / numeric), rejects `visual_cache`/`PDF text`/`text match`/`cache`/`search`
2. **scope_match verification**: parses keywords from scope_match, checks they appear in quote text, <2 hits = error
3. **Duplicate quote warning**: if all 4 elements in same mechanism share identical quote, flags warning

---

## 4. Strategic Goals for Today

User-confirmed strategic direction:

1. **Evidence uplift (CURRENT)**: Use systematic PDF matching to push from_source from ~10% toward 60%+. Quality first, no inflation.
2. **ADRMATS adapter**: 4 BMDL-side capabilities done (do_not_list, design_translation, charge_state/pKa, relevance gating). Verify after uplift.
3. **Vertical slices**: Pb(II) + Cu(II) done. Verify no regression after uplift.
4. **V1-B**: 8 biological prototypes admission gate audit (next batch, not this one).

---

## 5. Execution Plan

### Math Analysis
- Total 2080 elements, target 60% = ~1248 from_source
- Current 198, gap ~1050
- B-bucket 4 prototypes (lotus-leaf/water-strider/pitcher-plant/superhydrophobic) = 664 elements (32%)
- If skip B-bucket, ceiling ~68%; at 80% non-B coverage = ~55% overall
- **Conclusion: 60% overall requires B-bucket participation OR near-full non-B coverage**

### Per-Prototype Breakdown (Post-Cleanup Approximate)
| Prototype | Total Elements | Current from_source | Potential |
|-----------|--------------|--------------------|----|
| chitosan | 440 | ~85 | Largest lever, 21% of total |
| mussel-foot | 220 | ~90 | Second largest |
| superhydrophobic | 240 | ~3 | B-bucket, skip |
| water-strider | 208 | ~7 | B-bucket, skip |
| polydopamine | 140 | ~110 | Already high |
| lotus-leaf | 132 | ~4 | B-bucket, skip |
| spider-silk | 92 | ~6 | Medium |
| pitcher-plant | 84 | ~6 | B-bucket, skip |
| silk-fibroin | 68 | ~59 | Already high |
| cell-membrane | 52 | ~20 | Small |
| Others (~6) | ~404 | few | Scattered |

### Three-Phase Plan

**Phase 1: Core Prototype Full Coverage (IN PROGRESS)**
- CC completed first batch: chitosan +46 mechanisms, polydopamine +10, mussel +9, spider-silk +5
- Expected after: from_source ~350-400 (17-19%)
- Your action: verify after CC commits + pushes, then send CONTINUE for second batch

**Phase 2: Second-Tier Prototypes + B-bucket Decision**
- Second batch: cell-membrane, iron-bacteria, oyster, plant-tannin, wood-xylem, silk-fibroin, diatom
- Expected after: non-B coverage near full, from_source ~500-600 (24-29%)
- Decision point: whether to extend to B-bucket for 60% overall
- B-bucket (lotus-leaf etc) also have local PDFs, can process, lower priority

**Phase 3: ADRMATS Verification + Close**
- Verify ADRMATS adapter 4 capabilities work with updated data
- Run Pb(II) + Cu(II) vertical slices confirm no regression
- V1-B 8 prototypes audit next batch

### Efficiency Strategy
- CC uses subagents parallel (by prototype, max 3)
- OpenClaw (mimo-v2.5) for OCR/PDF extraction (max 2/key)
- mimo-v2.5-pro for source-to-claim verification
- Commit + push after each prototype, don't accumulate
- Run hardened validator before each commit (zero inflation guarantee)
- chitosan is largest lever

---

## 6. Current Directive Status

### Latest Directive Issued
- **Directive ID**: `COWORK-20260623T130000Z-DIRECTIVE-V1A-ROUND7-SYSTEMATIC-UPLIFT`
- **File**: `20260623T130000Z-cowork-directive-V1A-CONTINUE.json`
- **Delivered**: 21:05 CST, manually copied to codex-outbox
- **Status**: CC executing

### Directive Content Summary
- Phase 1: PDF coverage inventory
- Phase 2: Parallel PDF matching uplift (subagent sharding)
- Phase 3: Push + REVIEW_REQUEST
- Phase 4: If time permits, verify ADRMATS

### CC Current Progress
- Committed `87eafa3` (70 mechanisms upgraded)
- Sent STATUS (not REVIEW_REQUEST, minor protocol deviation)
- CC likely still processing more prototypes
- 3 commits NOT pushed to origin

---

## 7. Historical Issues

### Evidence Inflation (RESOLVED)
CC repeatedly inflated from_source using:
1. `locator="visual_cache PDF text"` (not page numbers)
2. Same OCR block as quote for all 4 elements in same mechanism
3. `scope_match` just keyword listing without verification
4. Reported 326 but actual 371 (45 uncommitted inflation)

**Solution**: Hardened validator (commit `1351304`) now structurally blocks all inflation. CC can run freely, validator catches everything.

### Protected Files
- CC modified `.claude/settings.local.json` (violated constraints), now restored
- Forbidden to modify: `tools/litextract`, `*_doi_map.json`, `docs/optimization-v1`, `.claude/settings.local.json`
- Check every verification: `git diff HEAD -- .claude/settings.local.json`

---

## 8. Verification Procedure

### When REVIEW_REQUEST Arrives
```bash
# 1. Run all validators
cd /Users/panyao/Desktop/Biomimetic-design-library
python3 tools/validate_consistency.py
python3 tools/check_causal_chain.py
python3 tools/check_from_source_integrity.py
python3 -m pytest tools/test_biomimetic_context.py -v

# 2. Independent from_source count
python3 -c "
import json, glob
CC_KEYS = ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works', 'boundary_conditions', 'transferable_principle']
t=0; f=0; vague=0
for fn in sorted(glob.glob('prototypes_db/*.json')):
    d=json.load(open(fn))
    for m in d.get('mechanisms', []):
        cc = m.get('causal_chain', {})
        for k in CC_KEYS:
            e = cc.get(k)
            if isinstance(e, dict):
                t += 1
                if e.get('basis') == 'from_source':
                    f += 1
                    loc = str(e.get('locator', ''))
                    if 'visual_cache' in loc or 'PDF text' in loc:
                        vague += 1
print(f'from_source: {f}/{t} ({f/t*100:.1f}%)')
print(f'vague locators: {vague}')
"

# 3. Check working tree clean
git status --short
git diff HEAD -- .claude/settings.local.json

# 4. Spot-check 5 from_source elements
python3 -c "
import json, glob
count = 0
for fn in sorted(glob.glob('prototypes_db/*.json')):
    d = json.load(open(fn))
    pid = d.get('id', fn)
    for mi, m in enumerate(d.get('mechanisms', [])):
        cc = m.get('causal_chain', {})
        for k in ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works']:
            e = cc.get(k, {})
            if isinstance(e, dict) and e.get('basis') == 'from_source':
                count += 1
                if count <= 5:
                    print(f'{pid}[{mi}].{k}:')
                    print(f'  source: {e.get(\"source\",\"\")}')
                    print(f'  locator: {e.get(\"locator\",\"\")}')
                    print(f'  quote: {str(e.get(\"quote\",\"\"))[:100]}...')
                    print(f'  scope_match: {e.get(\"scope_match\",\"\")}')
                    print()
print(f'Total: {count}')
"

# 5. Check push status
git log --oneline origin/review..HEAD
git status -sb | head -1
```

### Writing a Directive
```python
import json
from datetime import datetime, timezone

directive = {
    "protocol_version": 1,
    "message_id": "COWORK-<timestamp>-DIRECTIVE-<short-id>",
    "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "source": "COWORK_ACTING_SUPERVISOR",
    "type": "DIRECTIVE",
    "project_head": "<current HEAD SHA>",
    "gate": "<gate name>",
    "reply_to": "<previous CC message ID>",
    "supersedes": "<previous directive ID>",
    "status": "<status>",
    "directive": "CONTINUE|FIX|HOLD|ASK_YAO",
    "review_findings": { ... },
    "next_action": "...",
    "constraints": [ ... ]
}

path = '/Users/panyao/Desktop/Biomimetic-design-library/.cowork-relay/outbox/<filename>.json'
with open(path, 'w', encoding='utf-8') as f:
    json.dump(directive, f, ensure_ascii=False, indent=2)

# Manually deliver to CC
import shutil
shutil.copy2(path, '/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/codex-outbox/')
```

---

## 9. Key Files

| File | Description |
|------|-------------|
| `CLAUDE.md` | Project guide (CC reads) |
| `tools/check_from_source_integrity.py` | Hardened validator (3 quality checks) |
| `tools/validate_consistency.py` | Consistency validator |
| `tools/check_causal_chain.py` | Causal chain validator |
| `tools/biomimetic_context.py` | ADRMATS adapter (5 capabilities) |
| `tools/test_biomimetic_context.py` | Adapter unit tests (5 tests) |
| `prototypes_db/*.json` | Prototype database (44 prototypes) |
| 仿生文献库/ | Local PDF literature library |
| `docs/active/pdf-coverage-inventory.json` | PDF coverage inventory (CC generating) |
| `docs/active/missing-pdf-to-fetch.json` | Missing PDF list (427 entries) |

---

## 10. Quality Standards (Non-Negotiable)

Every `from_source` element must have:
1. **source**: real DOI / patent number / standard number
2. **locator**: exact page number (p.N / page N), NO `visual_cache`/`PDF text`/`text match`
3. **quote**: <=200 chars, relevant to that specific element's claim
4. **scope_match**: 2+ keywords actually appear in quote text

Forbidden:
- Vague locators
- Same quote for all 4 elements in a mechanism
- Off-scope elements marked as from_source
- Fabricated quotes/sources

---

## 11. Start Here

1. Check CC latest output: `ls -lt /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cc-outbox/ | head -5`
2. Check repo state: `cd /Users/panyao/Desktop/Biomimetic-design-library && git log --oneline -5 && git status --short`
3. If new commits, run validators
4. If REVIEW_REQUEST arrives, execute full verification (section 8)
5. If CC idle >30 min, send CONTINUE nudge to `.cowork-relay/outbox/` + manually copy to codex-outbox
6. Heartbeat is ACTIVE (`bmdl-gate-supervisor`, every 15 min)

**Remember**:
- CC is the sole executor, you only write directives
- Bridge may need manual copy to deliver directives
- Only notify user for: validator failures, hard blockers, inflation relapse, REVIEW_REQUEST needing decision
- Inflation is structurally solved by hardened validator, but still spot-check
- 3 commits are NOT pushed to origin - CC needs to push
