# Phase 1: 修接口可信度 P0 bug

> 预计工作量：2-3 小时  
> 目的：让 ADRMATS 拿到的 brief 不再误标证据等级、不再混入空污染物证据。  
> 停止点：接口验收通过后停下，不进入 enrichment 分离。

---

## 1. 修改文件

- `tools/biomimetic_context.py`
- `tools/verify_adrmats_delivery.py`

---

## 2. 问题背景

当前 `ctx.query()` 能调通，但有三个可信度问题：

1. `performance_leads` 会把 `pollutant=""` 的记录误匹配给任意污染物。
2. candidate 的 `mechanism.attribution.verification_tier` 存在硬编码 `single_source` 风险。
3. `honesty_ledger` 主要按 direct evidence / feature inference 分桶，没有严格读取真实 verification tier。

这些问题不是 PG 能解决的，必须先在 JSON 接口层修掉。

---

## 3. 具体任务

### 3.1 修 `_get_performance_leads()`

要求：

- 如果 `performance_data[].pollutant` 为空，必须跳过。
- 不允许空字符串参与 `pollutant in pol or pol in pollutant` 匹配。
- 优先使用 canonical name 和 aliases 做匹配。

建议行为：

```python
pol = str(p.get("pollutant", "") or "").strip()
if not pol:
    continue
```

### 3.2 修 candidate 的 `verification_tier`

禁止硬编码：

```python
"verification_tier": "single_source"
```

应读取机制条目真实字段：

```python
"verification_tier": main_mech.get("verification", "unverified")
```

如果机制没有 verification，则保守标为 `unverified`。

### 3.3 修机制选择逻辑

不要永远取：

```python
main_mech = mechs[0] if mechs else {}
```

改为优先选择：

1. 有非空 `基本原理`；
2. `基本原理` 不是 `needs_review`；
3. verification tier 尽量不为 `needs_review`。

如果没有合格机制，再退回第一个机制或空机制。

### 3.4 修 `honesty_ledger`

分桶规则：

| verification tier | ledger bucket |
|---|---|
| `verified` | facts |
| `corroborated` | facts |
| `single_source` | leads |
| `unverified` | inferences |
| `needs_review` | inferences |

注意：

- 不要把“有 direct evidence”自动写成 facts。
- direct evidence 只能说明“有直接污染物匹配线索”，不能等同于 verified fact。

### 3.5 强化验收脚本

在 `tools/verify_adrmats_delivery.py` 中增加检查：

- `performance_leads` 不得出现 `pollutant=""`。
- candidate 的 `verification_tier` 不得全部硬编码为 `single_source`。
- 前 5 个候选如果出现 `基本原理=needs_review`，验收输出必须明确 warning。

---

## 4. 验收命令

```powershell
python -X utf8 tools\verify_adrmats_delivery.py
python -X utf8 tools\validate_consistency.py
python -X utf8 tools\check_chimera.py
```

---

## 5. 验收标准

- [ ] 四个 ADRMATS 查询仍通过。
- [ ] PFOA / SMX / BPA 仍全部 `direct_evidence=false`。
- [ ] `performance_leads` 无空污染物记录。
- [ ] `verification_tier` 来自真实数据，不是硬编码。
- [ ] `honesty_ledger` 按真实 verification tier 分桶。
- [ ] `validate_consistency.py` 仍为 0 error。
- [ ] `check_chimera.py` 仍为 0 violation。

---

## 6. 输出格式

```text
Phase 1 完成
修改文件:
- tools/biomimetic_context.py
- tools/verify_adrmats_delivery.py

修复项:
- performance_leads 空污染物匹配: 已修 / 未修
- verification_tier 硬编码: 已修 / 未修
- mechanism 选择逻辑: 已修 / 未修
- honesty_ledger 分桶: 已修 / 未修

验收结果:
- verify_adrmats_delivery.py: <结果>
- validate_consistency.py: <结果>
- check_chimera.py: <结果>
```
