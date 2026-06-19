# Phase 1 — 修接口诚实度 P0 bug · 报告

## ① 修改文件列表

| 文件 | 操作 |
|------|------|
| `tools/biomimetic_context.py` | 修改（3 处） |
| `tools/test_interface_honesty.py` | 新建 |

## ② 执行的命令

```bash
python3 -X utf8 tools/test_interface_honesty.py     # 3/3 PASS
python3 -X utf8 tools/verify_adrmats_delivery.py    # 6/6 PASS（回归）
```

## ③ 修复明细

### Fix 1: 去硬编码 verification_tier（line 385）

**Before:**
```python
'verification_tier': 'single_source'
```

**After:**
```python
'verification_tier': main_mech.get('verification', 'needs_review') or 'needs_review'
```

效果：brief 中每个候选的 `attribution.verification_tier` 现在反映机制真实状态，缺省为 `needs_review`（不再默认夸大为 `single_source`）。

### Fix 2: 空 pollutant 不匹配（_get_performance_leads, line 454）

**Before:**
```python
pol = p.get('pollutant', '')
if pollutant.lower() in pol.lower() or pol.lower() in pollutant.lower():
```

**After:**
```python
pol = p.get('pollutant', '')
if not pol or not pol.strip():
    continue  # 空 pollutant 不参与匹配
if pollutant.lower() in pol.lower() or pol.lower() in pollutant.lower():
```

效果：50-70% 的空 pollutant 条目不再"匹配一切"污染 performance_leads。

### Fix 3: main() 笔误修复（line 478）

**Before:**
```python
brief['candidates']   # KeyError: 'candidates'（顶层只有 'brief' 键）
```

**After:**
```python
brief['brief']['candidates']
```

## ④ 验收实际输出

```
PASS: 空 pollutant 不匹配
PASS: verification_tier 读取机制真实值 (found needs_review mechanisms: False)
PASS: main() 正常运行
All 3 tests PASSED

verify_adrmats_delivery.py: 6/6 PASS
```

## ⑤ 残留风险

1. **Phase 4/6 后需回归测试**：当 mechanism 的 `verification` 字段被 Phase 6 核验更新后，brief 的 `verification_tier` 会自动反映新值。需在 Phase 6 后重跑 `test_interface_honesty.py` 确认行为一致。
2. **`_get_applicability` 的 IndexError 风险**（单元素 `tested_ph_range`）未在本 Phase 修复——方案要求 Phase 1 只改 2 处，此 bug 留给后续 Phase。

---

**Phase 1 验收：全绿 ✅，等待 Yao 确认后进入 Phase 2。**
