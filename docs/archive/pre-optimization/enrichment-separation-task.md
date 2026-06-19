# 继续上次未完成的任务：chimera 保护 + enrichment 层分离

> 上次的步骤 1（修 chimera、恢复富化数据）你已经完成并 commit 了，很好。现在继续做步骤 2 和步骤 3。

---

## 步骤 2：在 merge 逻辑中加入 chimera 过滤

当前 `tools/build_prototypes_db.py` 的 `merge_with_existing` 函数只保留富化字段，但不会阻止脏数据写入。如果以后有人重跑重建，chimera 会再次出现。

在 `merge_with_existing` 函数中，合并完 mechanisms 之后、返回之前，加入以下过滤逻辑：

```python
# === chimera 过滤：阻止已知污染源写入 ===
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
    kw_list = CHIMERA_BLOCKLIST[proto_id].get("mechanism_keywords", [])
    filtered = []
    for m in new_result.get("mechanisms", []):
        text = f'{m.get("name", "")} {m.get("description", "")}'
        if any(kw.lower() in text.lower() for kw in kw_list):
            continue
        filtered.append(m)
    new_result["mechanisms"] = filtered
```

改完后跑一次 `python3 tools/check_chimera.py` 确认仍然是 0 违规。

---

## 步骤 3：enrichment 层分离

### 3.1 创建目录

```
prototypes_db/enrichment/
```

### 3.2 给 `build_prototypes_db.py` 加 `--export-enrichment` 参数

跑 `python3 tools/build_prototypes_db.py --export-enrichment` 时：

1. 遍历 `prototypes_db/*.json`（跳过 `separation/` 和 `enrichment/`）
2. 从每个原型 JSON 中提取富化字段
3. 写入 `prototypes_db/enrichment/<id>.json`

提取范围：

| 来源 | 提取字段 | 条件 |
|------|----------|------|
| mechanisms | `基本原理` | 存在且非空 |
| mechanisms | `active_features` | 存在且非空 |
| mechanisms | `verification` | 不为 `unverified` |
| performance_data | `verification` | 不为 `unverified` |
| performance_data | `confidence` | 不为默认值 0.8 |

enrichment JSON 格式：

```json
{
  "prototype_id": "metal-organic-framework",
  "enrichment_version": 1,
  "last_updated": "2026-06-10",
  "mechanisms": [
    {
      "_match_key": "<与 _mech_key 函数一致的 key>",
      "基本原理": "...",
      "active_features": {},
      "verification": "single_source"
    }
  ],
  "performance_data": [
    {
      "_match_key": "<与 _perf_key 函数一致的 key>",
      "verification": "single_source",
      "confidence": 0.9
    }
  ]
}
```

注意：
- `_match_key` 必须与脚本中现有的 `_mech_key` / `_perf_key` 函数逻辑完全一致
- 只存非默认值的条目，保持文件精简

### 3.3 修改 `merge_with_existing` 的读取来源

当前 merge 从 `prototypes_db/<id>.json` 读旧数据做合并。改为从 `prototypes_db/enrichment/<id>.json` 读取。

具体来说，`merge_with_existing` 的参数 `existing_path` 改为指向 enrichment 文件：

```python
# 在 main() 的循环中：
enrichment_path = output_dir / "enrichment" / f"{pid}.json"
result = merge_with_existing(result, str(enrichment_path))
```

`merge_with_existing` 内部按 `_match_key` 匹配 enrichment 中的条目，把富化字段写回到 new_result 的 mechanisms 和 performance_data 中。

新的数据流：
```
原始提取 JSON
    ↓ 聚合
中间结果（纯原始提取，无富化）
    ↓ 从 enrichment/<id>.json 加载富化数据并 merge
最终 prototypes_db/<id>.json
```

### 3.4 执行首次拆分并验证

```bash
# 1. 导出 enrichment
python3 tools/build_prototypes_db.py --export-enrichment

# 2. 确认 enrichment 文件数量
ls prototypes_db/enrichment/*.json | wc -l   # 目标：31

# 3. 备份当前 JSON
cp -r prototypes_db prototypes_db_backup

# 4. 重跑重建（用 enrichment 做 merge）
python3 tools/build_prototypes_db.py

# 5. 对比验证
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
        print(f'MISMATCH {pid}: 基本原理 {old_bp}->{new_bp}, verified {old_v}->{new_v}')
        mismatches += 1
if mismatches == 0:
    print('PASS: 所有原型富化字段重建前后一致')
else:
    print(f'FAIL: {mismatches} 个原型不一致')
"

# 6. 跑校验
python3 tools/validate_consistency.py   # 目标：0 错误
python3 tools/check_chimera.py          # 目标：0 违规

# 7. 清理备份
rm -rf prototypes_db_backup
```

---

## 完成标准

全部满足后 commit，commit message 建议：`feat: enrichment 层架构分离 + chimera merge 保护`

- [ ] `check_chimera.py`：0 违规
- [ ] `validate_consistency.py`：0 错误
- [ ] 带 `基本原理` 的原型：21 个
- [ ] 全库 non-unverified：252 条
- [ ] `prototypes_db/enrichment/` 下有 31 个 JSON 文件
- [ ] 重跑重建后富化字段零丢失 + chimera 零违规
- [ ] `build_prototypes_db.py` 中有 `CHIMERA_BLOCKLIST` 和 `--export-enrichment`
