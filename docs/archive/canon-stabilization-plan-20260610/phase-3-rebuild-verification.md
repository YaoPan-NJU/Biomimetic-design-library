# Phase 3: 模拟重建验证

> 预计工作量：1-2 小时  
> 目的：证明 enrichment 分离后，重建不会丢富化字段。  
> 停止点：输出重建前后对比结果和验收结果。

---

## 1. 前置条件

必须已经完成 Phase 2：

- `prototypes_db/enrichment/` 存在。
- enrichment JSON 数量为 31。
- `build_prototypes_db.py` 已支持从 enrichment 合并富化字段。
- 已实现 chimera blocklist。

如果以上任一条件不满足，不要执行本阶段。

---

## 2. 要做什么

### 2.1 备份当前 `prototypes_db`

```powershell
New-Item -ItemType Directory -Force -Path tmp
Copy-Item -Recurse -Force prototypes_db tmp\prototypes_db_before_rebuild
```

### 2.2 重跑重建

```powershell
python -X utf8 tools\build_prototypes_db.py
```

### 2.3 对比重建前后

必须检查：

- 每个原型 `基本原理` 数量一致。
- 每个原型 non-unverified performance 数量一致。
- MOF non-unverified performance 仍为 252。
- chimera 仍为 0。

建议输出：

```text
PASS: 所有原型富化字段重建前后一致
```

如果有差异，必须输出：

```text
MISMATCH <prototype_id>: 基本原理 <old> -> <new>, non-unverified <old> -> <new>
```

并立即停止，不要继续 Phase 4。

### 2.4 跑总体验收

```powershell
python -X utf8 tools\verify_adrmats_delivery.py
python -X utf8 tools\validate_consistency.py
python -X utf8 tools\check_chimera.py
python -X utf8 tools\check_repo_hygiene.py
```

---

## 3. 验收标准

- [ ] 重建前后 `基本原理` 数量无损。
- [ ] 重建前后 non-unverified performance 数量无损。
- [ ] MOF non-unverified performance 仍为 252。
- [ ] `verify_adrmats_delivery.py` 通过。
- [ ] `validate_consistency.py` 为 0 error。
- [ ] `check_chimera.py` 为 0 violation。
- [ ] `check_repo_hygiene.py` 通过。
- [ ] git diff 中不能出现大规模富化字段丢失。

---

## 4. 正式对接节点

完成 Phase 3 后，可以向 PG 同事正式同步：

> JSON canon 已完成富化层分离，并通过模拟重建验证。当前重建不会丢 `基本原理`、verification 和 chimera 清洗结果。可以开始 PG schema / ETL 讨论，但正式灌库前仍建议先做 Phase 4 的 mapping sync 检查。

---

## 5. 输出格式

```text
Phase 3 完成
重建验证:
- 富化字段是否无损: 是 / 否
- MOF non-unverified: <n>
- chimera: <n> violation

验收结果:
- verify_adrmats_delivery.py: <结果>
- validate_consistency.py: <结果>
- check_chimera.py: <结果>
- check_repo_hygiene.py: <结果>

是否建议进入 Phase 4: 是 / 否
```
