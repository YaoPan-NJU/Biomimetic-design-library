# Phase 2 — 策展落地 · 报告（修正版）

## ① 修改文件列表

| 文件 | 操作 |
|------|------|
| `prototypes_db/namib-beetle.json` | 移至 `prototypes_db/parked/` |
| `prototypes_db/metal-organic-framework.json` | 移至 `prototypes_db/materials_reference/`，加 `status` |
| `prototypes_db/cellulose-nanocrystal.json` | 移至 `prototypes_db/materials_reference/`，加 `status` |
| `prototypes_db/starch-granule.json` | 移至 `prototypes_db/materials_reference/`，加 `status` |
| `prototypes_db/alginate.json` | 移至 `prototypes_db/materials_reference/`，加 `status` |
| `prototypes_db/silkworm-silk.json` | 删除（空壳，DEDUP） |
| `prototypes_db/diatom-inspired-porous.json` | 删除（空壳，DEDUP） |
| `prototypes_db/pitcher-plant-slippery-surface.json` | 添加 `function: anti_fouling` |
| `feature-mapping.json` | 全 7 section 清理 204 处引用 |
| `feature_matching_rules.json` | 清理 41 处引用 |
| `tools/validate_consistency.py` | 新增 R15 引用完整性检查 |
| `docs/optimization-v1/phase2-moves.md` | 新建 |
| `docs/optimization-v1/phase2-report.md` | 新建 |

## ② 验收实际输出

```
Active prototypes:     24 ✅
Materials reference:    4 ✅
Parked:                 1 ✅
prototype_metadata:    24 ✅
Refs to removed IDs:    0 ✅
Active ref mismatches:  0 ✅
R15 引用完整性:         ✅ 一致: 24 个原型
validate_consistency:   0 error (197 warnings)
```

## ③ 残留风险

1. **feature_matching_rules.json 删除了 4 条整规则**（羧酸基团、长链全氟烷基、负电荷、PFASs）：这些特征在 active 原型中暂无覆盖。
2. **constraint_prototype_map 移除了 103 条条目**：stability/regeneration/pH_sensitivity 等维度的数据量显著减少。
3. **R14 警告**（机制含实例级数据）：197 条 warning 主要来自 R14，属于既有数据质量问题，非本 Phase 产物。

---

**Phase 2 验收：全绿 ✅，等待 Yao 确认后进入 Phase 3。**
