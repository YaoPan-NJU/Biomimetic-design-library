# Phase 5: 交接报告

> 预计工作量：1 小时  
> 目的：形成给 Yao Pan 和 PG 同事的稳定状态说明。  
> 停止点：生成交接报告，不开始 PG 实施。

---

## 1. 建议新增文档

```text
docs/archive/canon-stabilization-report-2026-06-10.md
```

注意：不要放到 `docs/` 根目录，避免违反仓库治理规则。

---

## 2. 报告必须包含

### 2.1 基本信息

- 当前分支。
- 当前 HEAD。
- 完成的 Phase。
- 修改文件列表。

### 2.2 关键统计

至少包含：

- top-level `prototypes_db/*.json` 数量。
- `prototypes_db/separation/*.json` 数量。
- performance 总数。
- mechanism 总数。
- MOF non-unverified performance 数量。
- 有 `基本原理` 的原型数。
- enrichment 文件数。

### 2.3 验收结果

列出以下命令和结果：

```powershell
python -X utf8 tools\verify_adrmats_delivery.py
python -X utf8 tools\validate_consistency.py
python -X utf8 tools\check_chimera.py
python -X utf8 tools\check_repo_hygiene.py
```

### 2.4 剩余风险

必须诚实列出：

- R14 warnings 是否仍存在。
- `verified=0` 是否仍存在。
- 非 MOF 性能数据是否大多仍为 `unverified`。
- PG 尚未开始。
- 是否已完成 mapping sync。

### 2.5 给 PG 同事的下一步

建议写清：

- 可以开始 PG schema 讨论。
- 正式 ETL 前必须基于 enrichment 分离后的 canon。
- `ctx.query()` 对外签名保持不变。
- 后续 PG 接入应做 JSON backend 与 PG backend 双跑 diff。
- 如果确认本库只读消费，PG 首期可考虑只读副本 / materialized view；如果确认多 Agent 并发写 canon，再做完整 PG SSoT。

---

## 3. 验收标准

- [ ] 交接报告已生成。
- [ ] 报告位置不违反 `check_repo_hygiene.py`。
- [ ] 报告包含 HEAD、统计、验收结果、剩余风险。
- [ ] 报告没有声称 PG 已完成。
- [ ] 报告明确下一步由谁主导。

---

## 4. 建议交接话术

```text
canon 稳定化已完成到 Phase 3/4：
- 已修接口证据标注问题；
- 已完成富化层分离；
- 已通过模拟重建，证明重建不会丢富化字段；
- ADRMATS 当前 JSON 接口仍通过验收。

现在可以开始 PG schema / ETL 讨论。
正式灌库前建议先确认本库是否存在多 Agent 并发写 canon；如果只是多 Agent 只读消费，首期 PG 可以按只读副本或物化视图设计。
```
