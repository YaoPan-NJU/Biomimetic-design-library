# Phase 2: 富化层分离

> 预计工作量：4-6 小时  
> 目的：让重建不会再次冲掉 `基本原理 / active_features / verification / confidence`。  
> 停止点：完成 enrichment 导出后停下，不立刻重建。

---

## 1. 修改文件

- `tools/build_prototypes_db.py`
- 新建目录：`prototypes_db/enrichment/`

---

## 2. 问题背景

当前 `build_prototypes_db.py` 的 merge 逻辑仍然从 `prototypes_db/<id>.json` 读取旧富化字段，再写回同一个 JSON。这个做法仍然脆弱：

- key 匹配失败会丢富化数据；
- 重建脚本跑错会覆盖 canon；
- chimera 脏数据可能从原始提取再次进入结果。

本阶段目标是把富化字段物理分离到 `prototypes_db/enrichment/`，重建时只从 enrichment 合并富化数据。

---

## 3. 具体任务

### 3.1 增加 `--export-enrichment`

为 `tools/build_prototypes_db.py` 增加命令：

```powershell
python -X utf8 tools\build_prototypes_db.py --export-enrichment
```

功能：

- 遍历当前 `prototypes_db/*.json`。
- 提取富化字段。
- 写入 `prototypes_db/enrichment/<prototype_id>.json`。

### 3.2 enrichment 文件结构

每个原型一个文件：

```text
prototypes_db/enrichment/<prototype_id>.json
```

建议结构：

```json
{
  "prototype_id": "metal-organic-framework",
  "enrichment_version": 1,
  "last_updated": "2026-06-10",
  "mechanisms": [],
  "performance_data": [],
  "mechanism_instances": []
}
```

### 3.3 mechanism enrichment

每条 mechanism enrichment 至少包含：

```json
{
  "_match_key": "<由 _mech_key() 生成>",
  "基本原理": "...",
  "active_features": [],
  "verification": "single_source"
}
```

保存规则：

- `_match_key` 必须与 `_mech_key()` 一致。
- 只保存非空 `基本原理`。
- 保存 `active_features`。
- 保存非默认 `verification`。

### 3.4 performance enrichment

每条 performance enrichment 至少包含：

```json
{
  "_match_key": "<由 _perf_key() 生成>",
  "verification": "single_source",
  "confidence": 0.8
}
```

保存规则：

- `_match_key` 必须与 `_perf_key()` 一致。
- 保存非 `unverified` 的 `verification`。
- 保存非默认 `confidence`。

### 3.5 修改 merge 逻辑

修改 `merge_with_existing()`：

- 不再从 `prototypes_db/<id>.json` 读取旧数据。
- 改为从 `prototypes_db/enrichment/<id>.json` 读取富化数据。
- enrichment 文件不存在时，输出 warning。
- 不允许静默丢富化字段。

### 3.6 加 chimera blocklist

在 merge 阶段过滤明显 chimera 关键词。

`polydopamine-coating` 过滤：

- `Stenocara`
- `desert beetle`
- `Desert beetle`
- `沙漠甲虫`

`spider-silk` 过滤：

- `Nelumbo`
- `Nepenthes`
- `Collembola`
- `荷叶`
- `猪笼草`
- `弹尾虫`

过滤范围：

- mechanism `name`
- mechanism `description`
- narrative entries 中明显不相关条目

---

## 4. 执行命令

```powershell
python -X utf8 tools\build_prototypes_db.py --export-enrichment
```

---

## 5. 验收标准

- [ ] `prototypes_db/enrichment/` 存在。
- [ ] enrichment JSON 数量为 31。
- [ ] MOF enrichment 中包含 performance verification 记录。
- [ ] 有 `基本原理` 的原型富化已导出。
- [ ] `merge_with_existing()` 改为读取 enrichment 文件。
- [ ] chimera blocklist 已实现。
- [ ] 此阶段完成后停下，不立刻重建。

---

## 6. 输出格式

```text
Phase 2 完成
修改文件:
- tools/build_prototypes_db.py
- prototypes_db/enrichment/*.json

导出结果:
- enrichment files: <n>
- MOF enrichment performance records: <n>
- mechanisms with 基本原理 exported: <n>

注意:
- 是否已实现 chimera blocklist: 是 / 否
- 是否已改为从 enrichment merge: 是 / 否
```
