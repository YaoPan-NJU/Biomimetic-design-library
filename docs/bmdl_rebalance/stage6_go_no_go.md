# Stage 6 Go/No-Go for Stage 7

**日期：** 2026-07-05

---

## 一、ADRMATS Compatibility

### bmdl_repository.py

| 检查项 | 状态 | 说明 |
|--------|------|------|
| SCHEMA 硬编码 | ⚠️ | `SCHEMA = "bmdl"` (L214) — 不支持 staging schema 切换 |
| query_candidates SQL | ✅ | `source_category='primary'` 过滤已生效 |
| 字段消费 | ✅ | lane/direct_evidence/candidate_honesty/bound_mechanism 字段在 SQL 中查询 |
| 环境变量切换 | ❌ | 不支持 `BMDL_SCHEMA=bmdl_staging` 环境变量 |

### 兼容性风险评估

**风险**：`bmdl_repository.py` 的 `SCHEMA = "bmdl"` 是硬编码，Stage 7 切换正式库时需要：
1. 要么修改代码支持环境变量 `BMDL_SCHEMA`
2. 要么直接在 RDS 上用 `bmdl` schema 导入 stage5 数据（覆盖正式库）

**建议方案**（Stage 7 执行）：
1. 修改 `bmdl_repository.py` L214: `SCHEMA = os.environ.get("BMDL_SCHEMA", "bmdl")`
2. 或者：直接在 `bmdl` schema 上 `--drop` + 导入 stage5 数据（因为 staging 验证已通过）

**当前判断**：不影响 Stage 6 go/no-go，但 Stage 7 需要处理。

---

## 二、Go/No-Go 判断

### ✅ GO 条件

| 条件 | 状态 |
|------|------|
| Staging import 成功 (132 match_weights, 48 protos, 1020 pd) | ✅ |
| Quarantined 不参与 | ✅ |
| source_category='primary' 过滤生效 | ✅ |
| BPA/PFOA 有 direct evidence #1 | ✅ |
| bone/oyster 不再高权重霸榜 | ✅ |
| chitosan 重金属 evidence-based 高排 | ✅ |
| PDA/mussel 不双算 | ✅ |
| Validator 0 errors | ✅ |
| Top-5 concentration 下降 (70%→61.8%) | ✅ |
| ETL 幂等性验证 | ✅ |

### ⚠️ 已知缺口

| 缺口 | 影响 | 建议 |
|------|------|------|
| PFOS 无 direct evidence | PFOS 场景信号弱 | Stage 7 后补充 |
| bmdl_repository SCHEMA 硬编码 | Stage 7 需改代码 | 改 `SCHEMA = os.environ.get("BMDL_SCHEMA", "bmdl")` |
| chitosan 仍 21.8% share | 偏高但 evidence-based | 可接受，Stage 7 后观察 |
| AC+BC 7.2% (未达 15%) | 证据已耗尽 | 接受为 Stage 4 最终值 |

---

## 三、Recommendation

### **GO for Stage 7**

理由：
1. Staging 验证全部通过
2. 4 个风险项已解决
3. BPA/PFOA 获得了 direct evidence 候选
4. MOF/exploratory 偏向已消除
5. 无 regression

### Stage 7 执行前需要：
1. 修改 `bmdl_repository.py` 支持 `BMDL_SCHEMA` 环境变量（或直接覆盖 `bmdl` schema）
2. 在 `bmdl` schema 上做 final import
3. 更新 `adrmats_export/match_export.json` = stage5 内容
4. 更新 `match_weights.csv`
5. 跑 ADRMATS E2E 回归测试
6. commit + push
