# Stage 7 Rollback Plan

**日期：** 2026-07-05

---

## 回滚优先级

### 一级回滚：环境变量切换（立即生效，零数据操作）

如果 production cutover 后查询异常：

```bash
# 切回旧 bmdl schema
unset BMDL_SCHEMA
# 或显式设置
BMDL_SCHEMA=bmdl
# 重启 ADRMATS 服务
```

验证：
```sql
SELECT count(*) FROM bmdl.match_weights;  -- 应为 130（旧值）
```

### 二级回滚：从逻辑备份恢复

如果旧 `bmdl` schema 也被意外修改或损坏：

```bash
cd /Users/panyao/Documents/ADRMATS
env -i HOME="$HOME" PATH="/usr/bin:/bin:/opt/homebrew/bin" .venv/bin/python -c "
import psycopg2, os, json
from dotenv import load_dotenv
load_dotenv('.env')
conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'],port=os.environ['POSTGRES_PORT'],dbname=os.environ['POSTGRES_DB'],user=os.environ['POSTGRES_USER'],password=os.environ['POSTGRES_PASSWORD'])
cur = conn.cursor()

with open('/Users/panyao/Desktop/Biomimetic-design-library/docs/bmdl_rebalance/stage7_production_backup.json') as f:
    backup = json.load(f)

# 逐表恢复
for table, data in backup.items():
    cols = data['columns']
    rows = data['rows']
    if not rows: continue
    placeholders = ','.join(['%s'] * len(cols))
    col_str = ','.join(cols)
    cur.execute(f'DELETE FROM bmdl.{table}')
    for row in rows:
        cur.execute(f'INSERT INTO bmdl.{table} ({col_str}) VALUES ({placeholders})', row)
    conn.commit()
    print(f'  {table}: {len(rows)} rows restored')
conn.close()
"
```

### 三级回滚：Git revert + 重新 import

如果需要完全回滚到 Stage 7 之前的状态：

```bash
# BMDL repo
cd /Users/panyao/Desktop/Biomimetic-design-library
git revert 63cbcbe  # 回滚 release candidate export
git push origin review

# 从 git tag 恢复
git checkout bmdl-pre-rebalance-20260704 -- adrmats_export/match_export.json

# ADRMATS repo
cd /Users/panyao/Documents/ADRMATS
git revert 5cb5902  # 回滚 BMDL_SCHEMA 补丁
git push origin main

# 重新 import 到 bmdl_staging 验证
cd /Users/panyao/Documents/ADRMATS
env -i HOME="$HOME" PATH="/usr/bin:/bin:/opt/homebrew/bin" .venv/bin/python \
  scripts/import_bmdl_to_rds.py --schema bmdl_staging --drop \
  --source /Users/panyao/Desktop/Biomimetic-design-library
```

## 需要保留的文件/commit/tag

| 资源 | 用途 |
|------|------|
| `docs/bmdl_rebalance/stage7_match_export_baseline_20260705.json` | 旧 match_export baseline (130 rows, SHA256[:16]=`4c5ab4773e1d70e8`) |
| `docs/bmdl_rebalance/stage7_production_backup.json` | production bmdl schema 逻辑备份（cutover 前生成） |
| `adrmats_export/match_export_stage5.json` | Stage 5 候选 (SHA256[:16]=`f5585e72b0d8a320`) |
| git tag `bmdl-pre-rebalance-20260704` | BMDL 重平衡前的 git tag |
| ADRMATS commit `5cb5902` | BMDL_SCHEMA 补丁（可 revert） |
| BMDL commit `4f420f5` | Release candidate export commit |
| BMDL commit `63cbcbe` | Final report commit |

## 回滚验证

回滚后执行：
1. `tools/validate_consistency.py` — 0 errors
2. BPA query — 应返回旧的 exploratory 候选（无 plant-lignocellulosic）
3. `match_weights` count — 应为 130（旧值）
4. `BMDL_SCHEMA` 环境变量 — 未设置或设为 `bmdl`
