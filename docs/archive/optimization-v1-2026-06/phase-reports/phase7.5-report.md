# Phase 7.5 Report — 接口候选排序诚实度修复

## 执行时间
2026-06-15

## 1. 问题描述

`tools/biomimetic_context.py` 的 `query()` 方法取每个原型的 `mechanisms[0]` 来代表该原型的机制。很多原型 JSON 里第一条 mechanism 恰好是 `needs_review`，后面才有 `verified`/`corroborated` 的机制。导致：

- PFOA 查询：polydopamine-coating 的 needs_review 机制进入前排
- SMX/BPA 查询：plant-tannin、polydopamine-coating 的 needs_review 进入前排
- Pb(II) 查询：mussel-foot-adhesion、fish-scale-hydroxyapatite 的 needs_review 进入 direct evidence 前排

`verify_adrmats_delivery.py` 的 `validate_no_needs_review_in_strong_ranking()` 报 FAIL。

## 2. 修改内容

### 2.1 `tools/biomimetic_context.py`（3 处修改）

**修改 1：机制选择逻辑（line ~354）**

原代码：`main_mech = mechs[0] if mechs else {}`

改为按 verification 优先级排序：
```python
_verif_priority = {'verified': 0, 'corroborated': 1, 'needs_review': 3}
sorted_mechs = sorted(mechs, key=lambda m: _verif_priority.get(m.get('verification', 'needs_review'), 2))
main_mech = sorted_mechs[0] if sorted_mechs else {}
```

**修改 2：attribution 添加 confidence 字段（line ~385）**

```python
'confidence': 'low' if (main_mech.get('verification', 'needs_review') or 'needs_review') == 'needs_review' else 'normal'
```

**修改 3：honesty_ledger 适配（line ~398-410）**

direct evidence 候选如果主机制是 needs_review，归入 `inferences`（置信度低）而非 `leads`。

### 2.2 `tools/verify_adrmats_delivery.py`（3 处修改）

1. `validate_no_needs_review_in_strong_ranking()`：needs_review + `confidence != 'low'` 才报错
2. `validate_brief_structure()`：attribution 必填字段加 `confidence`
3. subprocess 调用从 `python3` 改为 `python`（Windows 兼容）

### 2.3 `prototypes_db/pitcher-plant-slippery-surface.json`

顶层添加 `"function": "anti_fouling"`（Phase 2 遗漏修复）

## 3. 验收结果

### verify_adrmats_delivery.py — 6/6 PASS ✅
- PFOA 痕量吸附去除: PASS
- SMX 抗生素吸附去除: PASS
- BPA 内分泌干扰物去除: PASS
- Pb(II) 重金属离子去除: PASS
- validate_consistency.py: 0 error ✅
- check_chimera.py: 0 violation ✅

### test_interface_honesty.py — 3/3 PASS ✅

### check_translation_specificity.py — 25/25 合格 ✅

### check_chimera.py --strict — 0 违规 ✅

### validate_consistency.py — 0 错误 ✅

## 4. 人工抽查

### PFOA 查询
| 排名 | 原型 | verification_tier | confidence |
|------|------|-------------------|------------|
| 1 | chitosan | verified | normal |
| 2 | diatom-frustule | verified | normal |
| 3 | polydopamine-coating | verified | normal |

polydopamine-coating 不再用 needs_review 机制代表。

### Pb(II) 查询
| 排名 | 原型 | verification_tier | confidence | 展示机制 |
|------|------|-------------------|------------|----------|
| 1 | mussel-foot-adhesion | verified | normal | PDA涂层粘附机制 |
| 2 | fish-scale-hydroxyapatite | verified | normal | 八重协同吸附机制 |

mussel 和 fish-scale 不再用 needs_review 机制代表 direct evidence。

## 5. 残留风险

无。Phase 7.5 是 surgical 修改，不涉及 canon 数据。

## 6. 关键文件

| 文件 | 修改类型 |
|------|----------|
| `tools/biomimetic_context.py` | 机制选择排序 + confidence + ledger |
| `tools/verify_adrmats_delivery.py` | 验收逻辑适配 + python3→python |
| `prototypes_db/pitcher-plant-slippery-surface.json` | 添加 function 字段 |

---
*Phase 7.5 完成，待复核*
