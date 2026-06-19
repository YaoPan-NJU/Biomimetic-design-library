# Phase 2 — 变动记录（修正版）

## PARK（1 个）

| 原型 | 从 | 到 | 说明 |
|------|-----|-----|------|
| namib-beetle | `prototypes_db/namib-beetle.json` | `prototypes_db/parked/namib-beetle.json` | 超出吸附范围（集水），退出检索 |

## DEMOTE（4 个）

| 原型 | 从 | 到 | 标记 |
|------|-----|-----|------|
| metal-organic-framework | `prototypes_db/` | `prototypes_db/materials_reference/` | `status: material_reference` |
| cellulose-nanocrystal | `prototypes_db/` | `prototypes_db/materials_reference/` | `status: material_reference` |
| starch-granule | `prototypes_db/` | `prototypes_db/materials_reference/` | `status: material_reference` |
| alginate | `prototypes_db/` | `prototypes_db/materials_reference/` | `status: material_reference` |

## DEDUP（2 个）

| 原型 | 合并目标 | 操作 | 说明 |
|------|---------|------|------|
| silkworm-silk | silk-fibroin | 删除（空壳，0 mechanism/0 perf） | 同为家蚕丝蛋白 |
| diatom-inspired-porous | diatom-frustule | 删除（空壳，0 mechanism/0 perf） | 非独立生物体 |

## ANTIFOULING（1 个）

| 原型 | 操作 |
|------|------|
| pitcher-plant-slippery-surface | 添加 `"function": "anti_fouling"`，不参与吸附排序 |

## 索引清理（全 section 覆盖）

### feature-mapping.json（204 处引用移除）

清理的 section：
- `pollutant_prototype_map`：从各污染物条目的 prototypes 数组中移除 7 个 ID，清空的条目整体移除
- `feature_prototype_map`：从各特征条目的 prototypes 数组中移除 7 个 ID
- `prototype_metadata`：移除 7 个 key
- `tested_conditions`：移除 6 个 key（silkworm-silk 无 tested_conditions）
- `constraint_prototype_map`：从 stability/regeneration/temperature_sensitivity/pH_sensitivity/salinity_tolerance 中移除相关条目（共 103 条）
- `mechanism_feature_bridge`：检查无引用
- `layer1_scoring`：检查无引用

Active 原型引用数与 HEAD 基线完全一致（0 mismatch）。

### feature_matching_rules.json（41 处引用移除）

移除整条规则（原型清空）：羧酸基团、长链全氟烷基、负电荷、PFASs
从多条规则中移除单个原型：配位、静电吸引、氢键、π-π堆积、疏水分配、孔道限域、离子交换 等

## 验收脚本更新

- `tools/validate_consistency.py`：新增 R15 检查 feature-mapping ↔ prototypes_db 引用完整性
