# Stage 7 Production Cutover Runbook

**日期：** 2026-07-05
**状态：** 待潘老师确认后执行

---

## ⚠️ 生产切换需要潘老师明确授权

---

## 前置检查

1. 确认 BMDL review 分支已 push 到 GitHub
2. 确认 ADRMATS main 分支已 push（commit `5cb5902`）
3. 确认 `bmdl_staging` schema 导入验证通过
4. 确认 `tools/validate_consistency.py` 0 errors
5. 确认 production `bmdl` schema 当前状态（逻辑备份）

## Fresh Logical Backup

```bash
cd /Users/panyao/Qoder/ADRMATS
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

## Final Import（需潘老师授权）

```bash
cd /Users/panyao/Qoder/ADRMATS
env -i HOME="$HOME" PATH="/usr/bin:/bin:/opt/homebrew/bin" .venv/bin/python scripts/import_bmdl_to_rds.py --schema bmdl --drop --source /Users/panyao/Desktop/Biomimetic-design-library
```

**注意**：`--schema bmdl --drop` 会被 ETL 安全锁拦截（只有 `_staging` schema 可以 drop）。需要临时修改安全锁或手动执行 SQL。

**推荐方式**：直接在 RDS 上执行 schema rename

```sql
-- 1. 重命名当前 production schema
ALTER SCHEMA bmdl RENAME TO bmdl_pre_stage7_backup;
-- 2. 重命名 staging 为 production
ALTER SCHEMA bmdl_staging RENAME TO bmdl;
-- 3. 验证
SELECT count(*) FROM bmdl.match_weights;  -- should be 132
```

## 验证 SQL

```sql
-- 导入后验证
SELECT count(*) FROM bmdl.biological_prototypes;  -- 48
SELECT count(*) FROM bmdl.match_weights;          -- 132
SELECT count(*) FROM bmdl.performance_data;       -- 1020
SELECT count(*) FROM bmdl.biological_prototypes WHERE source_category='quarantined';  -- 8
SELECT count(*) FROM bmdl.biological_prototypes WHERE source_category='primary';     -- 40
SELECT count(*) FROM bmdl.match_weights WHERE lane='exploratory' AND weight > 0.3;   -- 0
```

## ADRMATS 环境变量

| 场景 | 设置 | 说明 |
|------|------|------|
| Production (默认) | 不设 `BMDL_SCHEMA` | 读 `bmdl` schema |
| Rollback | `BMDL_SCHEMA=bmdl_pre_stage7_backup` | 切回旧 schema |
| Staging | `BMDL_SCHEMA=bmdl_staging` | 读 staging |

在 ADRMATS 的 `.env` 或系统环境中设置：
```
# Production (default)
# BMDL_SCHEMA=bmdl

# Rollback (if needed)
# BMDL_SCHEMA=bmdl_pre_stage7_backup
```

## 潘老师需要确认

- [ ] 逻辑备份已执行
- [ ] Final import / schema rename 授权
- [ ] ADRMATS E2E 回归测试授权
