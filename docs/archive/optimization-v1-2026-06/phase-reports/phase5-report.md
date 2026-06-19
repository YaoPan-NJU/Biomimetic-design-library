# Phase 5 — 因果链补全 · 报告

## ① 修改文件列表

| 文件 | 操作 |
|------|------|
| `prototypes_db/mussel-foot-adhesion.json` | 3 条因果链（PDA粘附、PDA自聚、铀酰配位） |
| `prototypes_db/chitosan.json` | 2 条因果链（pH效应、金属络合） |
| `prototypes_db/chlorella-cell-wall.json` | 1 条因果链（藻类染料吸附） |
| `prototypes_db/diatom-frustule.json` | 1 条因果链（Pb²⁺ XPS证据） |
| `prototypes_db/polydopamine-coating.json` | 1 条因果链（PDA π-π+配位） |
| `prototypes_db/sulfate-reducing-bacteria.json` | 1 条因果链（SRB硫化物沉淀） |
| `prototypes_db/iron-oxidizing-bacteria.json` | 1 条因果链（施氏矿物除砷） |
| `prototypes_db/plant-tannin.json` | 1 条因果链（单宁酸金属配位） |
| `prototypes_db/cell-membrane-ion-channel.json` | 1 条因果链（离子通道选择性） |
| `prototypes_db/bone-structure.json` | 1 条因果链（HAp重金属） |
| `prototypes_db/oyster-shell.json` | 1 条因果链（牡蛎壳吸附） |
| `prototypes_db/scallop-shell.json` | 1 条因果链（扇贝壳吸附） |
| `prototypes_db/lobster-exoskeleton.json` | 1 条因果链（几丁质吸附） |
| `prototypes_db/mangrove-root.json` | 1 条因果链（人工湿地） |
| `prototypes_db/mycelium.json` | 1 条因果链（CMC水凝胶） |
| `prototypes_db/wood-xylem.json` | 1 条因果链（酚类吸附） |
| `prototypes_db/silk-fibroin.json` | 2 条因果链（吸附机制、丝素蛋白） |
| `prototypes_db/spider-silk.json` | 1 条因果链（抗污机制） |
| `prototypes_db/fish-scale-hydroxyapatite.json` | 1 条因果链（HAp协同吸附） |
| `prototypes_db/pitcher-plant-slippery-surface.json` | 1 条新机制+因果链（SLIPS抗污） |
| `prototypes_db/biomineralization-template.json` | 1 条（llm_inferred + placeholder boundary） |
| `prototypes_db/coral-skeleton.json` | 1 条（llm_inferred + placeholder boundary） |
| `prototypes_db/dna-aptamer.json` | 1 条（llm_inferred + placeholder boundary） |
| `prototypes_db/magnetic-bacteria.json` | 1 条（llm_inferred + placeholder boundary） |
| `tools/check_causal_chain.py` | 新建验收脚本 |
| `docs/optimization-v1/phase5-chains.md` | 新建合格率报告 |

## ② 验收实际输出

```
已填合格卡: 28 / 总机制 534
每个 active 原型 ≥1 张合格卡: 24/24 ✅
剩余 causal_chain 空 basis 要素数: 0 ✅
from_source 无来源: 0 ✅
空壳原型全 llm_inferred: 4/4 ✅
check_causal_chain.py 输出已存 phase5-chains.md
```

## ③ 因果链覆盖统计

粒度：每原型 1–几张核心可迁移原理卡，碎片机制不建卡（骨架已清空）。

| 原型 | 总机制 | 合格卡 | 来源 |
|------|--------|--------|------|
| mussel-foot-adhesion | 88 | 3 | from_source + llm_inferred |
| chitosan | 132 | 2 | from_source + llm_inferred |
| silk-fibroin | 20 | 2 | from_source + llm_inferred |
| 其他 21 个原型 | 各1-89 | 各1 | 混合 |
| **总计** | **534** | **28** | |

## ④ 残留风险

1. **空壳因果链全为 llm_inferred**：biomineralization-template、coral-skeleton、dna-aptamer、magnetic-bacteria 的因果链全部由模型推断，无文献支撑，boundary_conditions 为 placeholder。Phase 6 需开 PDF 核验或入待裁决。
2. **pitcher-plant 新增机制待核验**：Nepenthes SLIPS 抗污机制由模型构建，需文献确认。
3. **大量 R14 噪声机制未清理**：mussel(52)、polydopamine(~60)、fish-scale(~80)、spider(~25) 等原型中大量机制是超疏水/油水分离的 R14 噪声，causal_chain 骨架为空。Phase 7 设计转译时需批量清理。

---

**Phase 5 验收：全绿 ✅，等待 Yao 确认后进入 Phase 6。**
