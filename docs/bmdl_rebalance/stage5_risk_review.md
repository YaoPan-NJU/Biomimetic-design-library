# Stage 5 Risk Review

**日期：** 2026-07-05
**状态：** Dry-run 风险审查

---

## 一、Dry-run 前后对比

### 权重变化统计

| 指标 | Before | After |
|------|--------|-------|
| 总条数 | 130 | 130 |
| 变化条数 | - | 84 (64.6%) |
| quarantined 参与 | 0 | 0 ✅ |
| exploratory >0.3 | 68 | 0 ✅ |
| high weight (≥0.8) non-direct | 38 | 0 ✅ |

### Top-10 原型权重变化

| Prototype | Before avg | After avg | 变化 | 风险 |
|-----------|-----------|-----------|------|------|
| sulfate-reducing-bacteria | 0.879 | 0.393 | ↓55% | 7条全exploratory除1fact → 大幅降权合理 |
| bone-structure | 0.860 | 0.482 | ↓44% | 17条中14lead/2exploratory → lead也被cap 0.5 |
| oyster-shell | 0.840 | 0.371 | ↓56% | 14条中12exploratory → 大幅降权合理 |
| mussel-foot-adhesion | 0.837 | 0.837 | = | 4条全lead+direct → 保留合理 |
| chitosan | 0.764 | 0.517 | ↓32% | 27条中15exploratory → 降权但仍霸榜 |
| polydopamine-coating | 0.684 | 0.530 | ↓23% | 19条中12exploratory → 降权 |
| chlorella-cell-wall | 0.800 | 0.425 | ↓47% | 4条全exploratory → 大幅降权 |
| diatom-frustule | 0.700 | 0.460 | ↓34% | 5条中3exploratory → 降权 |

### Top-5 集中度

| 指标 | Before | After |
|------|--------|-------|
| Top-5 集中度 | ~70% | 63.8% |
| #1 chitosan | ~25% | 21.8% |
| #2 polydopamine-coating | ~15% | 13.0% |
| #3 bone-structure | ~18% | 12.8% |

**集中度下降但仍偏高**：chitosan 21.8% + polydopamine 13% = 34.8%，PDA/mussel 去重后可能进一步降低。

### PFOA/BPA 候选

| Prototype | Pollutant | Before | After |
|-----------|-----------|--------|-------|
| chitosan | BPA | 0.75 | 0.3 |
| plant-tannin | BPA | 0.7 | 0.3 |
| polydopamine-coating | BPA | 0.67 | 0.3 |
| chitosan | PFOA | 0.75 | 0.3 |
| diatom-frustule | PFOA | 0.7 | 0.3 |
| polydopamine-coating | PFOA | 0.6 | 0.3 |

**PFOA/BPA 全部被 cap 到 0.3** — 因为全部是 exploratory_no_source_evidence。这意味着 Stage 4 写入的 9 条 capacity（plant-lignocellulosic PFOA/BPA）在 match_weights 中没有对应条目。Stage 5 正式版需要为这些新 capacity 新增 match_weights。

---

## 二、风险项

### 风险1：bone-structure 过度降权
- Before: 17 条, avg 0.860
- After: 17 条, avg 0.482
- 14 条是 lead lane（非 exploratory），但 non-direct → cap 0.5
- **风险**：bone-structure 有 1 条 fact + direct evidence（weight 0.9），不应被批量降权
- **建议**：Stage 5 正式版对 lead lane + molecular_feature_inference 的条目做逐条评估，而非批量 cap

### 风险2：chitosan 仍霸榜
- After: 27 条, 21.8% total weight
- 15 条 exploratory 被 cap 0.3，但 12 条 lead 仍保留
- **风险**：即使降权后 chitosan 仍是 #1
- **建议**：Stage 5 正式版考虑将部分 chitosan match 迁移到 lobster-exoskeleton

### 风险3：PFOA/BPA 全被 cap 0.3
- 6 条 PFOA/BPA match 全是 exploratory_no_source_evidence
- Stage 4 写入的 9 条 capacity 在 match_weights 中无对应
- **风险**：dry-run 后 PFOA/BPA 的材料候选全部低权重
- **建议**：Stage 5 正式版为 plant-lignocellulosic-architecture 新增 PFOA/BPA match_weights（基于 9 条 capacity evidence）

### 风险4：PDA/mussel 未去重
- polydopamine-coating 19 条 + mussel-foot-adhesion 4 条 = 23 条
- 两者数据重叠（同源贻贝仿生）
- **风险**：双重计算
- **建议**：Stage 5 正式版合并

---

## 三、结论

Dry-run 规则有效消除了：
- ✅ quarantined 参与（0）
- ✅ exploratory 高权重（0 条 >0.3）
- ✅ non-direct 高权重（0 条 >0.5）

但存在 3 个需 Stage 5 正式版处理的问题：
1. bone-structure lead lane 不应批量 cap（需逐条评估）
2. PFOA/BPA 需新增 match_weights（基于 Stage 4 capacity）
3. PDA/mussel + chitosan/chitin 需去重

**建议**：dry-run 规则方向正确，但正式版需要更细粒度的权重调整，不能只靠 lane + direct_evidence 两个维度批量 cap。
