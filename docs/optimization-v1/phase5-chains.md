# Phase 5 — Causal Chain 覆盖与合格率

## 粒度决定

Phase 5 采用"每原型 1–几张核心可迁移原理卡"的粒度：
- **建卡对象**：该原型的 1–3 条最核心的吸附/功能机制（可迁移、可证伪、有边界条件）
- **碎片机制**：作为证据/实例保留，不建 causal_chain（causal_chain 骨架已清空）
- **空壳原型**：从零建 1 条 llm_inferred 卡，边界为 placeholder（待 Phase 6/8 核验）

## 覆盖统计

| 原型 | 总机制 | 合格卡 | 来源类型 |
|------|--------|--------|---------|
| mussel-foot-adhesion | 88 | 3 | from_source + llm_inferred |
| chitosan | 132 | 2 | from_source + llm_inferred |
| silk-fibroin | 20 | 2 | from_source + llm_inferred |
| bone-structure | 5 | 1 | from_source + llm_inferred |
| cell-membrane-ion-channel | 13 | 1 | from_source + llm_inferred |
| chlorella-cell-wall | 13 | 1 | from_source + llm_inferred |
| diatom-frustule | 15 | 1 | from_source + llm_inferred |
| fish-scale-hydroxyapatite | 89 | 1 | from_source + llm_inferred |
| iron-oxidizing-bacteria | 6 | 1 | from_source + llm_inferred |
| lobster-exoskeleton | 1 | 1 | from_source + llm_inferred |
| mangrove-root | 1 | 1 | from_source + llm_inferred |
| mycelium | 4 | 1 | from_source + llm_inferred |
| oyster-shell | 3 | 1 | from_source + llm_inferred |
| plant-tannin | 14 | 1 | llm_inferred |
| polydopamine-coating | 65 | 1 | from_source + llm_inferred |
| scallop-shell | 3 | 1 | from_source + llm_inferred |
| spider-silk | 31 | 1 | from_source + llm_inferred |
| sulfate-reducing-bacteria | 1 | 1 | from_source + llm_inferred |
| wood-xylem | 4 | 1 | from_source + llm_inferred |
| pitcher-plant-slippery-surface | 22 | 1 | llm_inferred |
| biomineralization-template | 1 | 1 | llm_inferred（空壳） |
| coral-skeleton | 1 | 1 | llm_inferred（空壳） |
| dna-aptamer | 1 | 1 | llm_inferred（空壳） |
| magnetic-bacteria | 1 | 1 | llm_inferred（空壳） |
| **总计** | **534** | **28** | |

## 质量检查

- 空 causal_chain 骨架（未建卡机制）已全部清空：506 条删除
- 剩余 causal_chain 空 basis 要素：0
- from_source 无来源：0（5 处已降为 llm_inferred）
- 4 个空壳原型：全 llm_inferred
