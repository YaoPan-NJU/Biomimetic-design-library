# Stage 6 Query Regression Report

**日期：** 2026-07-05
**Staging schema：** `bmdl_staging`

---

## 一、Query Results（Top-5 per pollutant）

### BPA

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | **plant-lignocellulosic-architecture** | **0.65** | **lead** | **True** |
| 2 | chitosan | 0.3 | exploratory | False |
| 3 | plant-tannin | 0.3 | exploratory | False |
| 4 | polydopamine-coating | 0.3 | exploratory | False |

✅ **plant-lignocellulosic 以 direct evidence 排名 #1**，不再只返回 exploratory 旧候选。

### PFOA

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | **plant-lignocellulosic-architecture** | **0.6** | **lead** | **True** |
| 2 | chitosan | 0.3 | exploratory | False |
| 3 | diatom-frustule | 0.3 | exploratory | False |
| 4 | polydopamine-coating | 0.3 | exploratory | False |

✅ **plant-lignocellulosic 以 direct evidence 排名 #1**。

### PFOS

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | chitosan | 0.3 | exploratory | False |
| 2 | diatom-frustule | 0.3 | exploratory | False |
| 3 | lotus-leaf | 0.3 | exploratory | False |
| 4 | polydopamine-coating | 0.3 | exploratory | False |

⚠️ PFOS 无 direct evidence 候选——Stage 4 未写入 PFOS capacity（PFOS ≠ PFOA，严格分桶）。所有 PFOS match 都是 exploratory cap 0.3。

### Cd(II)

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | chitosan | 0.9 | lead | True |
| 2 | fish-scale-hydroxyapatite | 0.8 | fact | True |
| 3 | diatom-frustule | 0.7 | lead | True |
| 4 | silk-fibroin | 0.7 | lead | True |
| 5 | bone-structure | 0.5 | lead | False |

✅ chitosan 对重金属高排是 evidence-based (direct=True)。bone-structure 降权到 0.5。

### Pb(II)

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | fish-scale-hydroxyapatite | 0.9 | fact | True |
| 2 | mussel-foot-adhesion | 0.9 | lead | True |
| 3 | chitosan | 0.8 | lead | True |
| 4 | oyster-shell | 0.8 | lead | True |
| 5 | diatom-frustule | 0.7 | lead | True |

✅ 多原型竞争，无单原型霸榜。oyster-shell 的 direct match 保留 0.8。

### Cr(VI)

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | chitosan | 0.85 | lead | True |
| 2 | iron-oxidizing-bacteria | 0.8 | lead | True |
| 3 | polydopamine-coating | 0.7 | lead | True |
| 4 | bone-structure | 0.5 | lead | False |
| 5 | oyster-shell | 0.3 | exploratory | False |

✅ bone-structure 降到 0.5，oyster-shell 降到 0.3。PDA 保留 0.7 (direct, 不与 mussel 重叠)。

### PO43-

| Rank | Prototype | Weight | Lane | Direct |
|------|-----------|--------|------|--------|
| 1 | oyster-shell | 0.8 | lead | True |
| 2 | iron-oxidizing-bacteria | 0.75 | fact | True |
| 3 | bone-structure | 0.5 | lead | False |
| 4 | sulfate-reducing-bacteria | 0.3 | exploratory | False |
| 5 | chitosan | 0.3 | exploratory | False |

✅ oyster-shell direct match 保留 0.8。bone-structure 降到 0.5。

### Hospital wastewater / 医院废水

无 BPA/PFOA 匹配——医院废水不是污染物 ID，而是水质类型。BMDL match_weights 按 pollutant_id 索引，不按废水类型。水质 fallback 行为在 `adaptive_constraining_task.py` 中处理（Axl 已在 Stage -1 修复了三种场景触发逻辑）。

---

## 二、断言检查

| 断言 | 结果 | 说明 |
|------|------|------|
| BPA/PFOA 不再只返回 exploratory | ✅ | plant-lignocellulosic direct #1 |
| MOF/quarantined 不出现 | ✅ | 0 quarantined in match_weights |
| bone/oyster 不高权重泛化霸榜 | ✅ | bone avg 0.482 (was 0.86), oyster 0.371 (was 0.84) |
| chitosan 重金属可高排 | ✅ | Cd 0.9, Cr 0.85, Pb 0.8 (all direct) |
| chitosan 有机物不靠 exploratory 高排 | ✅ | BPA/PFOA cap 0.3 |
| PDA/mussel 不重复双算 | ✅ | Cu/Hg/U: mussel retain, PDA cap 0.3 |
| 无库类目 fallback | N/A | 水质 fallback 在 task 层，非 BMDL 层 |

## 三、PFOS 缺口

PFOS 无 direct evidence 候选——Stage 4 严格区分 PFOA ≠ PFOS，未写入 PFOS capacity。所有 PFOS match 都是 exploratory cap 0.3。这是正确行为（严格分桶），但意味着 PFOS 场景下 BMDL 信号较弱。

**建议**：Stage 7 后可考虑补充 PFOS-specific capacity 数据（如果有文献支持）。
