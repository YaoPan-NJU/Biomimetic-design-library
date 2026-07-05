# Stage 7 Rollback Plan

**日期：** 2026-07-05

---

## 回滚场景

### 场景1：Production import 后查询异常

**步骤**：
1. 设置 ADRMATS 环境变量切回旧 schema：
   ```bash
   export BMDL_SCHEMA=bmdl_pre_stage7_backup
   ```
2. 重启 ADRMATS 服务
3. 验证查询恢复正常
4. 如果旧 schema 不可用（rename 方式），从逻辑备份恢复：
   ```bash
   # 从 stage7_production_backup.json 恢复
   env -i HOME="$HOME" PATH="/usr/bin:/bin:/opt/homebrew/bin" .venv/bin/python -c "
   import psycopg2, os, json
   from dotenv import load_dotenv
   load_dotenv('.env')
   conn = psycopg2.connect(...)
   # 重建 bmdl schema from backup JSON
   "
   ```

### 场景2：match_export.json 需要回滚

**步骤**：
1. BMDL repo 中恢复旧 baseline：
   ```bash
   cd /Users/panyao/Desktop/Biomimetic-design-library
   cp docs/bmdl_rebalance/stage7_match_export_baseline_20260705.json adrmats_export/match_export.json
   git checkout -- adrmats_export/match_export.json  # 或从 git 历史恢复
   ```
2. 重新生成 CSV
3. 重新 import 到 staging 验证

### 场景3：ADRMATS bmdl_repository.py 回滚

**步骤**：
```bash
cd /Users/panyao/Documents/ADRMATS
git revert 5cb5902  # 回滚 BMDL_SCHEMA 环境变量补丁
git push origin main
```

## 需要保留的文件/commit/tag

| 文件/Tag | 用途 |
|----------|------|
| `docs/bmdl_rebalance/stage7_match_export_baseline_20260705.json` | 旧 match_export baseline |
| `adrmats_export/match_export_stage5.json` | Stage 5 候选（与 RC 相同） |
| git tag `bmdl-pre-rebalance-20260704` | BMDL 重平衡前的 git tag |
| ADRMATS commit `5cb5902` | BMDL_SCHEMA 补丁（可 revert） |
| BMDL commit (pending) | Release candidate commit |

## 回滚验证

回滚后执行：
1. `tools/validate_consistency.py` — 0 errors
2. BPA query — 应返回旧的 exploratory 候选（无 plant-lignocellulosic）
3. `match_weights` count — 应为 130（旧值）
