# Stage 7 Regression Report

**日期：** 2026-07-05
**Candidate schema：** `bmdl_staging`
**BMDL_SCHEMA env：** `bmdl_staging`

---

## Query Results (Top-5 per pollutant)

### BPA

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | **plant-lignocellulosic-architecture** | **0.65** | **lead** | **True** |
| 2 | chitosan | 0.3 | exploratory | False |
| 3 | plant-tannin | 0.3 | exploratory | False |
| 4 | polydopamine-coating | 0.3 | exploratory | False |

✅ **plant-lignocellulosic direct evidence #1**

### PFOA

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | **plant-lignocellulosic-architecture** | **0.6** | **lead** | **True** |
| 2 | chitosan | 0.3 | exploratory | False |
| 3 | diatom-frustule | 0.3 | exploratory | False |
| 4 | polydopamine-coating | 0.3 | exploratory | False |

✅ **plant-lignocellulosic direct evidence #1**

### PFOS

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | chitosan | 0.3 | exploratory | False |
| 2 | diatom-frustule | 0.3 | exploratory | False |
| 3 | lotus-leaf | 0.3 | exploratory | False |
| 4 | polydopamine-coating | 0.3 | exploratory | False |

⚠️ No direct evidence — strict bucketing (PFOS ≠ PFOA). All exploratory ≤0.3. Acceptable.

### Cd(II)

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | chitosan | 0.9 | lead | True |
| 2 | fish-scale-hydroxyapatite | 0.8 | fact | True |
| 3 | diatom-frustule | 0.7 | lead | True |
| 4 | silk-fibroin | 0.7 | lead | True |
| 5 | bone-structure | 0.5 | lead | False |

✅ chitosan evidence-based (direct=True). bone-structure capped to 0.5.

### Pb(II)

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | fish-scale-hydroxyapatite | 0.9 | fact | True |
| 2 | mussel-foot-adhesion | 0.9 | lead | True |
| 3 | chitosan | 0.8 | lead | True |
| 4 | oyster-shell | 0.8 | lead | True |
| 5 | diatom-frustule | 0.7 | lead | True |

✅ Multi-prototype competition. No single prototype霸榜.

### Cr(VI)

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | chitosan | 0.85 | lead | True |
| 2 | iron-oxidizing-bacteria | 0.8 | lead | True |
| 3 | polydopamine-coating | 0.7 | lead | True |
| 4 | bone-structure | 0.5 | lead | False |
| 5 | oyster-shell | 0.3 | exploratory | False |

✅ bone-structure 0.5 (was 0.9), oyster-shell 0.3 (was 0.9). PDA 0.7 retained (direct, no mussel overlap for Cr(VI)).

### PO43-

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | oyster-shell | 0.8 | lead | True |
| 2 | iron-oxidizing-bacteria | 0.75 | fact | True |
| 3 | bone-structure | 0.5 | lead | False |
| 4 | sulfate-reducing-bacteria | 0.3 | exploratory | False |
| 5 | chitosan | 0.3 | exploratory | False |

✅ oyster-shell direct retained. bone-structure capped.

### Hospital wastewater / 医院废水

**Not applicable at BMDL layer.** Hospital wastewater is a water-quality type, not a pollutant ID. BMDL match_weights are indexed by `pollutant_id`. The hospital wastewater fallback behavior is handled in `src/tasks/adaptive_constraining_task.py` (`_get_relevant_water_data()`), which was fixed by Axl in Stage -1 to support three scenarios: ① municipal WWTP → query DB, ② no water type → default lab environment, ③ other water type → LLM knowledge reasoning. This assertion belongs to ADRMATS fallback layer, not BMDL match_weights layer.

---

## Assertion Summary

| Assertion | Result |
|-----------|--------|
| BPA/PFOA: plant-lignocellulosic direct #1 | ✅ |
| PFOS: no direct, all exploratory ≤0.3 | ✅ |
| MOF/quarantined not appearing | ✅ |
| bone/oyster not high-weight霸榜 | ✅ |
| chitosan heavy metal evidence-based | ✅ |
| chitosan organic not exploratory high | ✅ |
| PDA/mussel no double-counting | ✅ |
| Hospital wastewater fallback | N/A (ADRMATS task layer) |
