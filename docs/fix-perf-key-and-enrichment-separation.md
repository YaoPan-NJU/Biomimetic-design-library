# 任务：完成 canon 修复 + 富化层架构分离

> 分两个阶段执行，每个阶段完成后停下等我确认，不要跳步。

---

## 阶段 A：修复 merge key bug，完成 Step 1（修 canon）

### 背景

你之前写的 `merge_with_existing` 函数用 `_perf_key` 匹配新旧 performance_data 条目，key 包含 `pollutant` 字段。但重建后 pollutant 的命名格式变了（举几个实际例子）：

- `Pb(II)` → `Pb2+`
- `Hg(II)` → `Hg²⁺`
- `RhB (Rhodamine B)` → `RhB` 或 `Rhodamine B (RhB)`
- `PO₄³⁻` → `磷(P)和氟(F)`
- `MB (Methylene Blue)` → `Methylene blue MB`
- `Cr(VI)` → 空串

这导致 87 条 MOF 性能数据匹配不上，verification 状态没恢复。全库只有 MOF 受影响（其他原型要么没有 performance_data 要么 key 恰好没变），但 MOF 一个原型就丢了 87 条。

### 要做的事

1. **修改 `_perf_key`**：去掉 `pollutant`，改成只用 `parameter|value|material`。如果你担心有重复 key，加上 `page` 辅助去重：`parameter|value|material|page`。

2. **重跑重建**：跑一次 `build_prototypes_db.py`，让它用新的 key 重新 merge。

3. **验证**：
   ```bash
   python3 tools/validate_consistency.py   # 目标：0 错误
   python3 tools/check_chimera.py          # 目标：0 违规
   ```
   然后跑这段脚本确认 MOF verification 恢复情况：
   ```python
   import json
   with open('prototypes_db/metal-organic-framework.json') as f:
       d = json.load(f)
   perf = d['performance_data']
   non_unv = sum(1 for p in perf if p.get('verification', 'unverified') != 'unverified')
   print(f'MOF performance: {len(perf)} total, {non_unv} non-unverified')
   # 目标：non_unverified = 252（与 9dcb3a0 重建前一致）
   ```

4. **全库统计**：确认全库 non-unverified 性能条目恢复到接近 252（重建前的值），带 `基本原理` 的原型仍为 21 个。

### 阶段 A 完成标准

- `validate_consistency.py`：0 错误
- `check_chimera.py`：0 违规
- 带 `基本原理` 的原型：21 个
- MOF non-unverified 性能条目：252 条（全部恢复）
- 全库 non-unverified：≥ 252

**完成后停下来，输出所有验证结果，等我确认后再进入阶段 B。**

---

## 阶段 B：富化层架构分离（同事 review 的门槛 2）

### 背景

当前 `prototypes_db/*.json` 同时包含"原始提取数据"和"二次加工富化数据"。每次重跑 `build_prototypes_db.py`，哪怕你写了 merge 逻辑，仍然存在风险——如果某个 merge key 匹配失败（就像阶段 A 的 bug），富化数据就丢了。

根本解法是把富化数据拆出来，存到独立文件中，重建脚本永远不碰富化文件。

### 富化数据的定义

以下字段属于富化层，不属于原始提取：

**机制层富化字段**：
- `基本原理`（中文 key，注意不是 `basic_principle`）
- `active_features`

**性能数据层富化字段**：
- `verification`（当值不为 `unverified` 时）
- `confidence`（当值不为默认 0.8 时）

**顶层富化字段**：
- `mechanism_instances`（如果有）
- `provenance_summary.n_verified` / `n_unverified` 统计

### 要做的事

#### 1. 创建 `prototypes_db/enrichment/` 目录

每个活跃原型对应一个 `prototypes_db/enrichment/<id>.json`。

#### 2. 设计 enrichment JSON 结构

```json
{
  "prototype_id": "metal-organic-framework",
  "enrichment_version": 1,
  "last_updated": "2026-06-09",
  "mechanisms": [
    {
      "_match_key": "<name>|<description前80字符>",
      "基本原理": "...",
      "active_features": { ... },
      "verification": "single_source"
    }
  ],
  "performance_data": [
    {
      "_match_key": "<parameter>|<value>|<material>|<page>",
      "verification": "single_source",
      "confidence": 0.9
    }
  ]
}
```

关键设计点：
- 用 `_match_key` 做匹配，和 `merge_with_existing` 中的 key 函数保持一致
- 只存储非默认值的富化字段（`verification=unverified` 或 `confidence=0.8` 的不存，节省体积）
- 文件体积小、可读性好，方便人工 review 和 git 追踪

#### 3. 给 `build_prototypes_db.py` 加 `--export-enrichment` 参数

功能：从当前 `prototypes_db/*.json` 中提取富化字段，导出到 `prototypes_db/enrichment/<id>.json`。

这是首次拆分用的，只跑一次。

#### 4. 修改 `merge_with_existing` 的加载逻辑

改完之后 merge 不再从 `prototypes_db/<id>.json` 读取旧数据（因为重建后旧 JSON 就是新结果，自己 merge 自己没意义），而是从 `prototypes_db/enrichment/<id>.json` 读取富化数据并合并。

新的数据流：
```
原始提取 JSON (litextract/) 
    → build_prototypes_db.py 聚合 
    → 中间结果（纯原始提取，无富化）
    → merge_with_existing 从 enrichment/<id>.json 加载富化数据合并
    → 最终 prototypes_db/<id>.json
```

#### 5. 执行首次拆分

跑一次：
```bash
python3 tools/build_prototypes_db.py --export-enrichment
```

这应该从当前的 `prototypes_db/*.json`（阶段 A 修好的、包含完整富化数据的版本）中提取富化字段，生成 31 个 enrichment JSON。

#### 6. 验证拆分正确性

跑一次完整重建（不带 `--export-enrichment`），然后对比重建前后的 `prototypes_db/*.json`。富化字段应该完全一致（因为 merge 从 enrichment 加载并合并了）。

具体验证：
```bash
# 1. 先备份当前 JSON
cp -r prototypes_db prototypes_db_backup

# 2. 重跑重建
python3 tools/build_prototypes_db.py

# 3. 对比每个原型的关键富化字段
python3 -c "
import json, glob, os
mismatches = 0
for f in sorted(glob.glob('prototypes_db/*.json')):
    pid = os.path.basename(f).replace('.json','')
    with open(f) as fh: new = json.load(fh)
    backup_path = f.replace('prototypes_db/', 'prototypes_db_backup/')
    if not os.path.exists(backup_path): continue
    with open(backup_path) as fh: old = json.load(fh)
    
    # 比较 基本原理 数量
    old_bp = sum(1 for m in old.get('mechanisms',[]) if m.get('基本原理'))
    new_bp = sum(1 for m in new.get('mechanisms',[]) if m.get('基本原理'))
    
    # 比较 non-unverified 数量
    old_v = sum(1 for p in old.get('performance_data',[]) if p.get('verification','unverified') != 'unverified')
    new_v = sum(1 for p in new.get('performance_data',[]) if p.get('verification','unverified') != 'unverified')
    
    if old_bp != new_bp or old_v != new_v:
        print(f'MISMATCH {pid}: bp {old_bp}→{new_bp}, ver {old_v}→{new_v}')
        mismatches += 1

if mismatches == 0:
    print('✅ 所有原型富化字段重建前后一致')
else:
    print(f'❌ {mismatches} 个原型不一致')
"

# 4. 跑校验
python3 tools/validate_consistency.py   # 0 错误
python3 tools/check_chimera.py          # 0 违规

# 5. 清理备份
rm -rf prototypes_db_backup
```

### 阶段 B 完成标准

- `prototypes_db/enrichment/` 下有 31 个 JSON 文件（每个活跃原型一个）
- 重跑完整重建后，所有原型的 `基本原理` 数量和 non-unverified 数量与重建前完全一致
- `validate_consistency.py`：0 错误
- `check_chimera.py`：0 违规
- enrichment JSON 体积小、可读，方便 git 追踪

**完成后输出所有验证结果，不要 commit，等我 review。**
