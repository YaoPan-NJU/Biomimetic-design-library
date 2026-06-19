# Phase 2 附录：策展后的 direct evidence 覆盖缺口

> 策展移除 7 个原型（4 DEMOTE + 1 PARK + 2 DEDUP）后，`pollutant_prototype_map` 中部分污染物的 direct evidence 通道关闭。本文档分两类登记。

---

## ① 真实缺口（去重后无 active 原型直接证据，待 Phase 5 决定补原型）

| 污染物 | 原承载原型（已移除） | 现有 active 覆盖 | 建议候选 |
|--------|---------------------|-----------------|---------|
| Boron | metal-organic-framework | 0 | 待补（需含硼吸附机制的原型） |
| Co(II) / Co2+ | starch-granule | 0 | 待补（可考虑钴配合物/钴沉淀机制） |
| Cr(VI) 专属 | cellulose-nanocrystal（flat key "Cr6+"） | "Cr³⁺/Cr⁶⁺" 合并键下有 chitosan, iron-oxidizing-bacteria, polydopamine-coating（不区分价态） | Phase 4 归一后由合并键覆盖，但 Cr(VI) 的专属机制（还原 Cr(VI)→Cr(III)）需确认是否在现有原型中 |
| As(V) 专属 | metal-organic-framework（flat key "As(V)"） | "As³⁺/As⁵⁺" 合并键下有 iron-oxidizing-bacteria, chitosan（不区分价态） | 同上，As(V) 的专属吸附机制（砷酸盐配位）需确认 |

> 注：Hg(II) 经核实仍有 active 覆盖（"重金属.Hg(II)" → sulfate-reducing-bacteria, mussel-foot-adhesion, polydopamine-coating, plant-tannin），**非缺口**。

---

## ② 伪缺口（仅 pollutant 键未归一造成，Phase 4 归一时合并键即可恢复）

以下污染物在 HEAD 基线中就有多个拼写键，策展只清空了部分键，其他键下仍有 active 覆盖：

| 污染物 | 已清空的键（无 active） | 仍有 active 覆盖的键 | 覆盖原型 |
|--------|----------------------|---------------------|---------|
| 亚甲基蓝 (MB) | 亚甲基蓝(MB), 亚甲基蓝(MB)阳离子染料, 亚甲基蓝 (MB), MB (methylene blue) | MB, methylene blue (MB) | silk-fibroin |
| 刚果红 (CR) | 刚果红(CR), CR (congo red) | —（阴离子染料类别键下有 chitosan, chlorella-cell-wall） | chitosan, chlorella-cell-wall（类别级） |
| 孔雀石绿 (MG) | 孔雀石绿(MG), MG (malachite green) | —（阳离子染料类别键下有 chlorella-cell-wall） | chlorella-cell-wall（类别级） |
| 四环素 (TC) | tetracycline, tetracycline hydrochloride | 抗生素（类别键） | polydopamine-coating（类别级） |
| 环丙沙星 (CIP) | ciprofloxacin (CIP), Ciprofloxacin (CIP) | 抗生素（类别键） | polydopamine-coating（类别级） |
| 磷酸盐 | Phosphate, PO43-, PO43- (磷酸根) | PO₄³⁻ | oyster-shell, iron-oxidizing-bacteria |
| Methyl Blue | Methyl Blue (MB) | — | 需确认是否为 MB 的别名 |

> **Phase 4 行动**：将同义键合并到 canonical key 下，恢复 direct evidence 通道。例如"亚甲基蓝(MB)" → "MB"，"刚果红(CR)" → "CR (congo red)" 等。

---

## ③ 补充说明

### 重金属合并键的价态模糊问题

当前 `重金属.Cr³⁺/Cr⁶⁺` 和 `重金属.As³⁺/As⁵⁺` 使用合并键，不区分价态。这对 Phase 4 有影响：
- Cr(III) 和 Cr(VI) 的吸附机制完全不同（Cr(III) 是配位/沉淀，Cr(VI) 是还原吸附）
- As(III) 和 As(V) 的吸附机制也不同（As(III) 是中性分子疏水分配，As(V) 是阴离子配位）

建议 Phase 4 归一时拆分为独立价态键，或至少在 prototype 的 mechanism 中标注价态特异性。

### 污染物键重复现状

HEAD 基线中同一污染物有大量重复键，仅举几例：
- 亚甲基蓝：MB, MB (methylene blue), methylene blue (MB), 亚甲基蓝(MB), 亚甲基蓝 (MB), 亚甲基蓝(MB)阳离子染料（6 个键）
- 磷酸盐：PO43-, PO43- (磷酸根), Phosphate, phosphorus (PO₄³⁻, 以KH₂PO₄配制), 磷酸盐(以P计)（5 个键）
- 刚果红：刚果红(CR), CR (congo red)（2 个键）

这是 Phase 4 需要系统清理的问题。
