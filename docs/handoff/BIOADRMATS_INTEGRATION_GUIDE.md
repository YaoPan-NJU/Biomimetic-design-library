# BioADRMATS 集成指南

本文只描述 BioADRMATS 消费 BMDL 数据时需要实施的代码改动。BMDL 的权威输入是：

```text
adrmats_export/match_export.json
```

不要复制出第二套 `bioadrmats_export/`，也不要从 `feature_matching_rules.json` 重新推导匹配；否则查询语义、证据分级和导入数据会再次漂移。

## 输入契约

每条 `rows[]` 至少消费以下字段：

| 字段 | 含义 |
|---|---|
| `pollutant_id` | 规范化污染物名 |
| `prototype_id` | BMDL 根原型 ID |
| `weight` | 同一证据 lane 内的相关性排序信号，不是置信度 |
| `lane` | `fact / lead / exploratory` |
| `direct_evidence` | 仅严格核验的污染物特异材料去除性能为 `true` |
| `performance_evidence_tier` | `fact / lead / none` |
| `candidate_honesty` | `fact / lead / inference` |
| `bound_mechanism_id` | 本次查询实际选中的机制 ID；有值时优先使用 |
| `bound_mechanism` | 机制名称；旧机制没有 ID 时作为精确绑定键 |

## 必须修复 1：导入路径与原子性

涉及文件：`scripts/import_bmdl_to_rds.py`。

当前导入器查找 `bioadrmats_export/match_export.json`，应改为读取 `adrmats_export/match_export.json`。如果必须兼容旧包，只允许把旧路径作为回退并记录 warning，不能维护两套导出。

在执行任何 `DELETE`、`TRUNCATE` 或覆盖写入之前完成以下预检：

1. 文件存在且 JSON 可解析；
2. `meta.total_rows == len(rows)` 且 `rows` 非空；
3. 必填字段存在，`lane` 和 `performance_evidence_tier` 取值合法；
4. `direct_evidence=true` 时必须满足 `performance_evidence_tier=fact`；若绑定机制仍待核验，候选整体可保守地处于 `lane=lead`；
5. `prototype_id` 能在本次导入的原型集合中解析；
6. `bound_mechanism_id` 与 `bound_mechanism` 至少一个非空；有 ID 时按 ID 解析，否则按名称精确解析。

推荐的最小执行顺序：

```python
export = load_and_validate(export_path)   # 失败时数据库保持不变
with connection.transaction():
    import_prototypes(export)
    replace_match_rows(export["rows"])
    assert_foreign_keys_resolve(connection)
```

不要先清表再判断导出是否存在。若当前数据库客户端不支持事务，先导入 staging 表，通过计数和外键检查后再交换表。

验收测试：导出文件缺失、空 rows、非法 lane 或无法解析的原型/机制 ID 均应在首次删除之前失败，原表行数保持不变。

## 必须修复 2：使用查询绑定的机制

涉及文件：

- `src/adapters/bmdl_repository.py`
- `src/adapters/bmdl_models.py`
- `src/adapters/bmdl_adapter.py`

模型和 repository 增加并透传 `bound_mechanism_id`。适配器生成 brief 时优先按 ID、否则按完整名称选机制，不能再默认取原型的第一条机制。

```python
mechanism = next(
    (m for m in prototype.mechanisms if m.mechanism_id == match.bound_mechanism_id),
    None,
)
if mechanism is None and match.bound_mechanism:
    mechanism = next((m for m in prototype.mechanisms if m.name == match.bound_mechanism), None)
if mechanism is None:
    raise BmdlContractError("bound mechanism does not resolve")
```

部分正典机制尚无 `mechanism_id`，因此名称回退仍是当前契约的一部分；但新快照有 ID 却解析失败时必须报契约错误，不能静默回退到名称或第一条机制。

验收测试：构造一个第一条机制与 `bound_mechanism_id` 不同的原型，最终 brief 必须展示被绑定机制；不存在的 ID 必须失败。

## 必须修复 3：把相关性与置信度分开

涉及文件：`src/adapters/bmdl_adapter.py`，以及合并候选的 `BiomimeticMatchingAgent._merge_briefs`。

`weight` 只能用于同一 lane 内排序，不能参与证据置信度计算。建议直接使用固定、可解释的证据基线：

```python
LANE_CONFIDENCE = {
    "fact": 0.90,
    "lead": 0.65,
    "exploratory": 0.25,
}
confidence = LANE_CONFIDENCE.get(match.lane, 0.25)
```

合并排序先比较证据 lane，再在 lane 内比较相关性：

```python
LANE_PRIORITY = {"fact": 2, "lead": 1, "exploratory": 0}
key = (LANE_PRIORITY.get(candidate.lane, 0), candidate.confidence, candidate.match_weight)
```

LLM 自行生成且没有可核验来源的候选按 `exploratory` 处理。不要让 `weight=0.95` 的 exploratory 候选压过 `weight=0.55` 的 lead，也不要把 `candidate_honesty=inference` 显示成“高置信候选”。

验收测试：

- fact 必须排在 lead 之前，lead 必须排在 exploratory 之前；
- exploratory 的高 weight 不能跨 lane 超过 lead；
- 缺失或未知 lane 安全降级为 exploratory，并记录契约 warning。

## 建议同时修复：多污染物输入

当前适配器能提取多个污染物名，但只查询第一个。应逐个污染物查询，再以 `(pollutant_id, prototype_id, bound_mechanism_id)` 去重；不要把不同污染物的证据 lane 合并成一个无来源的综合分数。

```python
rows = []
for pollutant in extract_pollutant_names(constraints):
    rows.extend(repository.find_matches(pollutant))
rows = deduplicate(rows, key=lambda r: (r.pollutant_id, r.prototype_id, r.bound_mechanism_id))
```

验收测试：输入两个污染物时必须保留两组查询结果和各自的证据 lane，不能只出现第一个污染物。

## 完成定义

BioADRMATS 侧达到以下条件才算适配完成：

- 导入读取 `adrmats_export/match_export.json`，失败不会清空已有数据；
- 数据库和模型保留 `lane`、`performance_evidence_tier`、`bound_mechanism_id` 与 `bound_mechanism`；
- brief 展示的是 BMDL 查询绑定的机制；
- 排序不再把 `weight` 当置信度；
- 上述失败场景和排序规则均有自动化测试。
