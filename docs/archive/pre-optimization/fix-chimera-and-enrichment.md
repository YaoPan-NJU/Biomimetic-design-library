# 补充指令：修复 chimera 回退 + 完成 enrichment 层分离

> 你上次修好了 `_perf_key` bug 并恢复了 MOF 的 verification（252/252），这很好。但重跑 `build_prototypes_db.py` 之后 chimera 又回来了，现在需要补修。然后继续做 enrichment 层分离。
>
> **重要约束：以下所有步骤中，不要重跑 `build_prototypes_db.py`。所有数据修改都直接编辑 `prototypes_db/*.json` 文件完成。**

---

## 步骤 1：修复 chimera 回退（直接编辑 JSON）

`check_chimera.py` 又报了 2 个原型 5 处违规：

### polydopamine-coating（3 处违规）

问题：organism 字段混入了 Stenocara beetle（沙漠甲虫）的数据。

修复方法——直接编辑 `prototypes_db/polydopamine-coating.json`：

1. `organism` 字段：如果 `scientific` 或 `category` 中出现 Stenocara / beetle / 沙漠甲虫相关内容，修正为 polydopamine 的正确描述（如 `"scientific": "mussel-inspired synthetic polydopamine"` 或保持原值，确保不含甲虫）
2. `mechanisms` 数组：找到 description 或 name 中包含 "Stenocara"、"沙漠甲虫"、"Desert beetle" 的条目，删除它们
3. `narrative.entries` 中如果有 Stenocara / desert beetle 相关的叙事条目，也一并删除

### spider-silk（2 处违规）

问题：organism 字段混入了 Nelumbo（荷叶）和 Nepenthes（猪笼草）的数据。

修复方法——直接编辑 `prototypes_db/spider-silk.json`：

1. `organism` 字段：`scientific` 应为 "Araneidae (spiders)" 或类似蜘蛛相关描述，不应包含 Nelumbo / Collembola / Nepenthes
2. `mechanisms` 数组：找到 name 或 description 中包含 "Nelumbo"、"荷叶"、"Nepenthes"、"猪笼草"、"Collembola"、"弹尾虫" 的条目，删除它们

### 验证

```bash
python3 tools/check_chimera.py
```

目标输出：`违规原型: 0`，`总违规数: 0`。

---

## 步骤 2：修改 merge 逻辑，保护 chimera 修复结果

上次 chimera 回退的原因是：重跑 `build_prototypes_db.py` 时，merge 函数只保留"已有富化字段"，但不会阻止脏数据被重新写入。

需要在 `merge_with_existing` 中增加一个 **chimera 过滤层**：

```python
# 在 merge_with_existing 函数中，合并完 mechanisms 之后，增加：

# === 过滤 chimera 污染 ===
CHIMERA_BLOCKLIST = {
    "polydopamine-coating": {
        "mechanism_keywords": ["Stenocara", "沙漠甲虫", "Desert beetle", "desert beetle"],
    },
    "spider-silk": {
        "mechanism_keywords": ["Nelumbo", "荷叶", "Nepenthes", "猪笼草", "Collembola", "弹尾虫"],
    },
}

proto_id = new_result.get("id", "")
if proto_id in CHIMERA_BLOCKLIST:
    block = CHIMERA_BLOCKLIST[proto_id]
    kw_list = block.get("mechanism_keywords", [])
    filtered_mechs = []
    for m in new_result.get("mechanisms", []):
        text = f'{m.get("name","")} {m.get("description","")}'
        if any(kw.lower() in text.lower() for kw in kw_list):
            continue  # 丢弃 chimera 条目
        filtered_mechs.append(m)
    new_result["mechanisms"] = filtered_mechs
```

这样即使以后有人重跑 `build_prototypes_db.py`，chimera 条目也会在 merge 阶段被自动过滤掉。

---

## 步骤 3：enrichment 层分离

### 3.1 创建目录

```
prototypes_db/enrichment/
```

### 3.2 enrichment JSON 结构

每个活跃原型对应一个 `prototypes_db/enrichment/<id>.json`：

```json
{
  "prototype_id": "metal-organic-framework",
  "enrichment_version": 1,
  "last_updated": "2026-06-10",
  "mechanisms": [
    {
      "_match_key": "<name>|<description前80字符>",
      "基本原理": "...",
      "active_features": {},
      "verification": "single_source"
    }
  ],
  "performance_data": [
    {
      "_match_key": "<parameter>|<value>|<material>|<source_file>",
      "verification": "single_source",
      "confidence": 0.9
    }
  ]
}
```

注意：
- `_match_key` 必须与 `build_prototypes_db.py` 中 `_perf_key` / `_mech_key` 函数的逻辑完全一致
- 只存非默认值（`verification != "unverified"` 或 `confidence != 0.8` 时才记录）
- `基本原理` 字段保持中文 key 名

### 3.3 给 `build_prototypes_db.py` 加 `--export-enrichment` 参数

功能：遍历当前 `prototypes_db/*.json`，把富化字段提取出来写入 `prototypes_db/enrichment/<id>.json`。

提取范围：
- mechanisms 中的：`基本原理`、`active_features`、`verification`（非 unverified 时）
- performance_data 中的：`verification`（非 unverified 时）、`confidence`（非 0.8 时）
- 顶层 `mechanism_instances`（如果存在）

### 3.4 修改 `merge_with_existing` 的读取来源

改完之后 merge 不再从 `prototypes_db/<id>.json` 读旧数据（重建后那就是新结果了），而是从 `prototypes_db/enrichment/<id>.json` 读取富化数据并合并。

新的数据流：
```
原始提取 JSON → 聚合 → 中间结果（无富化）
                            ↓
                    enrichment/<id>.json 加载富化数据
                            ↓
                    merge 合并 → 最终 prototypes_db/<id>.json
```

### 3.5 执行首次拆分

```bash
python3 tools/build_prototypes_db.py --export-enrichment
```

从当前 JSON（chimera 已修、verification 已恢复的版本）中提取富化数据，生成 31 个 enrichment 文件。

### 3.6 验证拆分正确性

```bash
# 1. 备份当前 JSON
cp -r prototypes_db prototypes_db_backup

# 2. 重跑重建（这次可以跑，因为有 enrichment 兜底了）
python3 tools/build_prototypes_db.py

# 3. 对比富化字段是否一致
python3 -c "
import json, glob, os
mismatches = 0
for f in sorted(glob.glob('prototypes_db/*.json')):
    pid = os.path.basename(f).replace('.json','')
    with open(f) as fh: new = json.load(fh)
    bp = f.replace('prototypes_db/', 'prototypes_db_backup/')
    if not os.path.exists(bp): continue
    with open(bp) as fh: old = json.load(fh)
    old_bp = sum(1 for m in old.get('mechanisms',[]) if m.get('基本原理'))
    new_bp = sum(1 for m in new.get('mechanisms',[]) if m.get('基本原理'))
    old_v = sum(1 for p in old.get('performance_data',[]) if p.get('verification','unverified') != 'unverified')
    new_v = sum(1 for p in new.get('performance_data',[]) if p.get('verification','unverified') != 'unverified')
    if old_bp != new_bp or old_v != new_v:
        print(f'MISMATCH {pid}: 基本原理 {old_bp}→{new_bp}, verified {old_v}→{new_v}')
        mismatches += 1
if mismatches == 0:
    print('PASS: 所有原型富化字段重建前后一致')
else:
    print(f'FAIL: {mismatches} 个原型不一致')
"

# 4. 跑校验
python3 tools/validate_consistency.py   # 目标：0 错误
python3 tools/check_chimera.py          # 目标：0 违规（chimera 过滤层应生效）

# 5. 清理备份
rm -rf prototypes_db_backup
```

---

## 完成标准

全部满足后停下，不要 commit，输出所有验证结果等我确认：

- [ ] `check_chimera.py`：0 违规
- [ ] `validate_consistency.py`：0 错误
- [ ] 带 `基本原理` 的原型：21 个
- [ ] MOF non-unverified：252 条
- [ ] 全库 non-unverified：252 条
- [ ] `prototypes_db/enrichment/` 下有 31 个 JSON 文件
- [ ] 重跑重建后，富化字段零丢失 + chimera 零违规
