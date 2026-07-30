# Stage 7 Production Cutover Runbook

**日期：** 2026-07-05
**状态：** 待潘老师明确授权后执行

---

## ⚠️ 生产切换需要潘老师明确授权

---

## 前置检查

1. 确认 BMDL review 分支已 push 到 GitHub（commit `63cbcbe`）
2. 确认 ADRMATS main 分支已 push（commit `5cb5902`）
3. 确认 `bmdl_staging` schema 导入验证通过
4. 确认 `tools/validate_consistency.py` 0 errors
5. 确认 ADRMATS E2E smoke test 通过（包括医院废水 fallback 场景）

## 推荐方案：Candidate Schema + 环境变量切换（零 drop production）

### Step 1: Fresh backup production `bmdl`

```bash
cd /Users/panyao/Documents/ADRMATS
env -i HOME="$HOME" PATH="/usr/bin:/bin:/opt/homebrew/bin" .venv/bin/python -c "
import psycopg2, os, json
from dotenv import load_dotenv
load_dotenv('.env')
conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'],port=os.environ['POSTGRES_PORT'],dbname=os.environ['POSTGRES_DB'],user=os.environ['POSTGRES_USER'],password=os.environ['POSTGRES_PASSWORD'])
cur = conn.cursor()
backup = {}
for table in ['biological_prototypes','performance_data','match_weights','pollutant_profiles','pollutant_aliases']:
    cur.execute(f'SELECT * FROM bmdl.{table}')
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    backup[table] = {'columns': cols, 'rows': [list(r) for r in rows]}
with open('/Users/panyao/Desktop/Biomimetic-design-library/docs/bmdl_rebalance/stage7_production_backup.json', 'w') as f:
    json.dump(backup, f, ensure_ascii=False, indent=2, default=str)
print(f'Backup saved: {sum(len(v[\"rows\"]) for v in backup.values())} total rows')
conn.close()
"
```

### Step 2: Import release candidate into new timestamped schema

```bash
cd /Users/panyao/Documents/ADRMATS
env -i HOME="$HOME" PATH="/usr/bin:/bin:/opt/homebrew/bin" .venv/bin/python \
  scripts/import_bmdl_to_rds.py \
  --schema bmdl_stage7_rc \
  --drop \
  --source /Users/panyao/Desktop/Biomimetic-design-library
```

> 注：`bmdl_stage7_rc` 不含 `_staging`，ETL 安全锁会阻止 `--drop`。
> 需要在 RDS 手动创建 schema 后用不带 `--drop` 导入，或临时使用 `bmdl_staging`。
> 推荐：直接用已验证通过的 `bmdl_staging` schema（Step 3 切环境变量即可）。

### Step 3: Set ADRMATS production env

在 ADRMATS 的 `.env` 或系统环境中设置：

```bash
BMDL_SCHEMA=bmdl_staging
```

### Step 4: Restart ADRMATS

```bash
# 重启 ADRMATS 服务
# 具体命令取决于部署方式
```

### Step 5: Run E2E smoke tests

必须覆盖：
- BPA 设计流程
- PFOA 设计流程
- 医院废水 fallback 场景（`_get_relevant_water_data` 三种场景）
- MOF/quarantined 不出现
- bone/oyster 不高权重霸榜

### Step 6: Verify

```sql
SELECT count(*) FROM bmdl_staging.match_weights;  -- should be 132
SELECT count(*) FROM bmdl_staging.biological_prototypes WHERE source_category='primary';  -- 40
SELECT count(*) FROM bmdl_staging.match_weights WHERE lane='exploratory' AND weight::numeric > 0.3;  -- 0
```

### Rollback

```bash
# 切回旧 bmdl schema
unset BMDL_SCHEMA
# 或
BMDL_SCHEMA=bmdl
# 重启 ADRMATS
```

---

## 可选方案：Schema Rename（更高风险，需人工确认）

> ⚠️ 此方案涉及 schema rename，是不可逆操作，必须由潘老师明确授权。

```sql
-- 1. 重命名当前 production schema
ALTER SCHEMA bmdl RENAME TO bmdl_pre_stage7_backup;

-- 2. 重命名 staging 为 production
ALTER SCHEMA bmdl_staging RENAME TO bmdl;

-- 3. 验证
SELECT count(*) FROM bmdl.match_weights;  -- 132
```

**风险**：rename 后如果发现问题，需要反向 rename 恢复。所有连接 bmdl schema的服务需要重启。

---

## ADRMATS 环境变量

| 场景 | 设置 | 说明 |
|------|------|------|
| Production (推荐) | `BMDL_SCHEMA=bmdl_staging` | 指向 release candidate schema |
| Rollback | 不设 或 `BMDL_SCHEMA=bmdl` | 切回旧 production schema |
| 保持旧默认 | 不设 `BMDL_SCHEMA` | 默认读 `bmdl`（旧数据） |

路径说明：所有路径使用 canonical `/Users/panyao/Documents/ADRMATS`。
