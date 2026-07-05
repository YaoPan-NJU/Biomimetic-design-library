# Stage 5 Risk Resolution Report

**日期：** 2026-07-05

---

## 风险A: bone-structure / oyster-shell

### bone-structure
- **Before**: 17 matches, avg 0.860, top-2 (14.6%)
- **After**: 17 matches, avg 0.482, top-3 (12.8%)
- **处理方式**: 逐条评估
  - 1 条 fact+direct (F-) → 保留 0.8
  - 3 条 exploratory_no_source (CIP/CR/TC) → cap 0.3
  - 13 条 lead non-direct (重金属/营养盐) → cap 0.5
- **理由**: bone-structure 只有 2 条 performance_data，17 条 match 中 16 条是 molecular_feature_inference，不应高权重。fact+direct 的 F- 保留，其余降权合理。

### oyster-shell
- **Before**: 14 matches, avg 0.840, top-4 (11.8%)
- **After**: 14 matches, avg 0.371, top-5 (8.1%)
- **处理方式**: 逐条评估
  - 2 条 direct (PO43-/Pb(II)) → 保留 0.8
  - 12 条 exploratory non-direct → cap 0.3 或 0.5
- **理由**: oyster-shell 有 6 条 performance_data（主要是磷和重金属），direct evidence 的保留，其余降权。

**结论**: ✅ 已解决。不再有 high weight low evidence 条目。

---

## 风险B: chitosan 霸榜

- **Before**: 27 matches, 20.6% share
- **After**: 27 matches, 21.8% share (weight 下降但 share 上升因总量缩小)
- **处理方式**: 不机械迁移
  - 12 条 lead+direct (重金属: Cd/Cr/Cu/Pb/Hg/As/Ni/Zn/U + MO/NO3-/CR) → 保留原权重
  - 15 条 exploratory (有机: BPA/PFOA/CIP/MB/MO/NH4+/NO3- 等) → cap 0.3
- **理由**: chitosan 对重金属的霸榜是 evidence-based（direct_evidence + 102 条 performance_data）。氨基螯合金属是 chitosan 的核心机制，不应人为降权。有机污染物的 match 已被 cap 0.3，合理降权。
- **风险**: chitosan share 21.8% 仍偏高，但在 evidence-based 前提下可接受。如 Stage 6 检验发现问题，可再考虑将部分重金属 match 关联到 lobster-exoskeleton。

**结论**: ✅ 可接受。evidence-based 霸榜，不做机械迁移。

---

## 风险C: PFOA/BPA 新增 match_weights

- **Before**: PFOA/BPA 全是 exploratory_no_source (0.6-0.75 → cap 0.3)
- **After**: 新增 2 条 plant-lignocellulosic-architecture match
  - PFOA: weight 0.6 (direct_source_evidence, 3 条 Stage4 PDF-verified capacity)
  - BPA: weight 0.65 (direct_source_evidence, 6 条 Stage4 PDF-verified capacity)
- **理由**: Stage 4 写入了 9 条 PDF-verified capacity (PDB-P003~P012)，这些是有 source_page + verification_quote 的直接证据。plant-lignocellulosic 对 PFOA/BPA 的 match 应反映这些证据。
- **权重设定**: 0.6/0.65 — 高于 exploratory (0.3) 但不霸榜（plant-lignocellulosic 总 share 仅 2.0%）

**结论**: ✅ 已解决。PFOA/BPA 不再全靠 exploratory。

---

## 风险D: PDA / mussel 去重

- **Before**: PDA 19 matches + mussel 4 matches = 23 matches（重叠 3 个污染物）
- **After**: PDA 重叠条目 cap 0.3，mussel 保留原权重
  - Cu(II): mussel 0.8 retain, PDA 0.3 (was 0.75)
  - Hg(II): mussel 0.85 retain, PDA 0.3 (was 0.8)
  - U(VI): mussel 0.8 retain, PDA 0.3 (was 0.75)
- **理由**: mussel-foot-adhesion 作为生物机制 root 保留高权重；PDA 作为材料实现/涂层工艺降权。避免同一贻贝仿生证据双重计算。
- **PDA 非重叠条目**: 16 条保留（其中 exploratory 被 cap 0.3，lead+direct 保留）

**结论**: ✅ 已解决。3 个重叠污染物不再双重计算。

---

## 总结

| 风险 | 状态 | 处理方式 |
|------|------|---------|
| A: bone/oyster | ✅ 解决 | 逐条评估，fact+direct 保留，non-direct cap |
| B: chitosan | ✅ 可接受 | evidence-based 霸榜，不机械迁移 |
| C: PFOA/BPA | ✅ 解决 | 新增 plant-lignocellulosic direct match |
| D: PDA/mussel | ✅ 解决 | 重叠条目 PDA cap 0.3，mussel retain |
