# Phase 0: 基线确认

> 预计工作量：0.5 小时  
> 目的：确认当前分支、当前数据状态和验收基线。  
> 停止点：输出基线统计和验收结果，不修改代码。

---

## 1. 要做什么

### 1.1 确认分支和 HEAD

```powershell
git status --short --branch
git rev-parse --short HEAD
```

期望：

- 当前分支是 `feature/extraction-results`。
- 工作区没有未解释的本地改动。
- 记录当前 HEAD，用于后续交接报告。

### 1.2 跑现有验收

```powershell
python -X utf8 tools\verify_adrmats_delivery.py
python -X utf8 tools\validate_consistency.py
python -X utf8 tools\check_chimera.py
python -X utf8 tools\check_repo_hygiene.py
```

期望：

- `verify_adrmats_delivery.py` 通过。
- `validate_consistency.py` 为 0 error。
- `check_chimera.py` 为 0 violation。
- `check_repo_hygiene.py` 通过。

### 1.3 统计关键数据

统计以下项目：

- `prototypes_db/*.json` 数量。
- `prototypes_db/separation/*.json` 数量。
- performance 总数。
- mechanism 总数。
- engineering constraints 总数。
- MOF non-unverified performance 数量。
- 有 `基本原理` 的原型数量。
- `prototypes_db/enrichment/` 是否存在。

---

## 2. 验收标准

- [ ] 工作区干净。
- [ ] 当前 HEAD 已记录。
- [ ] `verify_adrmats_delivery.py` 通过。
- [ ] `validate_consistency.py` 为 0 error。
- [ ] `check_chimera.py` 为 0 violation。
- [ ] `check_repo_hygiene.py` 通过。
- [ ] 已输出关键数据统计。

---

## 3. 输出格式

Phase 0 完成后输出：

```text
Phase 0 完成
HEAD: <commit>
验收结果:
- verify_adrmats_delivery.py: <结果>
- validate_consistency.py: <结果>
- check_chimera.py: <结果>
- check_repo_hygiene.py: <结果>

关键统计:
- top-level prototypes_db JSON: <n>
- separation JSON: <n>
- performance total: <n>
- mechanism total: <n>
- MOF non-unverified: <n>
- prototypes with 基本原理: <n>
- enrichment dir: exists / missing
```
