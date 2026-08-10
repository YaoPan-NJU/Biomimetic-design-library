# BMDL 英文标量字段补全 — Hand-off 交接文档

> 供 Claude Code（或任何后续维护者）无缝接手。最后更新：2026-08-10。
> 维护人：YaoPan (BMDL 负责人)；任务协作者：AXL (BioADRMATS 代码)。

## 1. 任务背景与目标

BioADRMATS 下游消费 BMDL 时，机制层 `name` / `description` / `transferable_principle` 以及 `organism.scientific` 均为中文，导致 RDS `mechanism_type`（取 `mechanisms[0].name`）、`match_export.json` 的 `bound_mechanism`、brief/4.5 机制文本全为中文。

本任务为 BMDL canon 补**英文标量字段**（纯新增，不破坏现有 schema/审计）：

| 位置 | 新增英文字段 | 说明 |
|---|---|---|
| `organism` | `scientific_en` | 英文物种名（拉丁/纯英文） |
| `mechanism` | `name_en` | 英文机制名 |
| `mechanism` | `description_en` | 英文机制描述摘要 |
| `mechanism.causal_chain` | `transferable_principle_en` | 英文可转译原理摘要 |

**已与用户确认的实施决策：**
1. 补英文范围 = **全部 102 个原型**
2. 第 3 条范围 = **3 条全做**（name_en + scientific_en + description/transferable_principle 英文）
3. 落地方式 = **dry-run 预览 → 用户确认 → `--write` 写入**（符合 BMDL 铁律"先 dry-run 再写入"）

## 2. 工作目录与环境

- 仓库本地路径：`/Users/panyao/Qoder/Biomimetic_Design_Library/仿生文献库/Biomimetic-design-library`
- 头部：`git log -1` = `6ac8f15 Curate massive prototype intake`（102 原型、86 active、632 机制）
- **BMDL 无 `.venv`、无 `.env`**。LLM 调用复用 BioADRMATS 的配置：
  - Python：`/Users/panyao/Qoder/ADRMATS-3/.venv/bin/python`（Python 3.12，含 `openai` SDK）
  - 密钥：`/Users/panyao/Qoder/ADRMATS-3/.env`（`DASHSCOPE_API_KEY` / `DASHSCOPE_BASE_URL`）
  - 模型：`qwen3.7-max`；base_url 默认 `https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1`

## 3. 核心脚本（已创建，未提交）

`tools/backfill_mechanism_name_en.py` —— 为所有 `prototypes_db/*.json` 添加英文标量字段。

**用法：**
```bash
cd /Users/panyao/Qoder/Biomimetic_Design_Library/仿生文献库/Biomimetic-design-library
# 1) dry-run 预览（默认，不写盘）
/Users/panyao/Qoder/ADRMATS-3/.venv/bin/python -X utf8 -u tools/backfill_mechanism_name_en.py \
    --env /Users/panyao/Qoder/ADRMATS-3/.env --chunk-size 8
# 2) 确认后写入
... --write
# 3) 局部/small 测试
... --only oatp-intestinal-hepatic-uptake        # 只处理指定原型
... --limit 5                                    # 只处理前 N 个
```

**关键参数：**
- `--write`：落盘（默认 dry-run）
- `--chunk-size N`：**大原型按 N 个机制切片翻译后合并**（chitosan 110 机制必须用，默认 0=不切片会截断）
- `--only / --limit`：局部处理
- `--env`：指向含 `DASHSCOPE_API_KEY` 的 .env

**重要：大量 LLM 调用耗时，务必 `python -u`（无缓冲）+ 输出重定向，否则看不到实时进度：**
```bash
... python -X utf8 -u ... > /tmp/bmdl_en_dryrun_20260810.log 2>&1
```

## 4. 已完成的工作与验证

### 4.1 字段形态确认
- 机制完整 keys：`mechanism_id/name/description/基本原理/source/ref_doi/verification/verification_quote/causal_chain/source_doi/source_page/source_locator/source_file/functional_groups/key_structures`
- `causal_chain` 各要素（pollutant_feature/bio_structure/interaction/why_it_works）为 dict `{text,basis,evidence_label,source,locator,quote,scope_match}`
- `transferable_principle` 是 **str**（中文）
- `organism` 是 dict `{common, scientific, category}`（均中文）
- 机制层原本**无任何 `*_en` 字段**；顶层原型 `name_en` 102/102 已有

### 4.2 Pilot 已验证（5+1 原型）
- oatp(2 mech)、alginate(1)、spider-silk(23)、chlorella-cell-wall(13)、chitosan(110)
- 翻译质量高：专业术语保留、无中文残留、不虚构、空输入→空输出

### 4.3 已修复的 3 个问题
1. **506/632 机制缺 `mechanism_id`**（32 个原型）→ 原按 id 匹配失效，改为按 `idx`（输入输出顺序）匹配；`_diff_summary` 同步改按位置对齐
2. **超大原型输出截断**（chitosan 110 机制输出 ~59K 字符 > 8192 token）→ 加 `--chunk-size` 切片翻译后合并
3. **JSON 截断容错弱** → `_parse_json` 增强：last-valid-boundary + `_extract_objects` 逐对象提取兜底

## 5. 当前进度（截至 2026-08-10）

- t1 字段形态确认 ✅
- t2 脚本搭建 ✅
- t3 pilot 验证 ✅
- **t4 全量 dry-run 生成：进行中**（后台进程，日志 `/tmp/bmdl_en_dryrun_20260810.log`，已处理 ~16/102，无 LLM ERROR）
- t5 用户确认后写入 ⏳
- t6 BMDL 验证脚本 ⏳

## 6. 下一步（Claude Code 接手清单）

1. **等待/检查全量 dry-run 完成**：`grep -c "prototypes changed" /tmp/bmdl_en_dryrun_20260810.log` 应输出 `1`，末尾 `== Done. 102/102 prototypes changed. dry-run only ... ==`
   - 检查是否有 `LLM ERROR`：`grep -c "LLM ERROR" /tmp/bmdl_en_dryrun_20260810.log`
2. **汇总 dry-run 变更预览给用户审阅**（统计：102 原型、多少机制加了哪些字段、有无缺字段需复核）
3. **用户确认后 `--write` 写入**全部 102 原型
4. **运行 BMDL Required validation**（见 AGENTS.md）：
   - `validate_consistency.py --strict`
   - `check_chimera.py --strict`
   - `check_causal_chain.py`
   - `check_source_authenticity.py`
   - `check_translation_specificity.py`
   - `check_boundary_guardrail.py`
   - `check_repo_hygiene.py`
   - `verify_adrmats_delivery.py`
   - （确认哪些脚本在 tools/ 下，逐个跑）
5. **git 提交**（脚本 + 102 个 JSON 改动），遵守 BMDL git discipline

## 7. BMDL 铁律（必须遵守）

来自 `docs/references/definitions.md` 总纲"宁可少而真，不可多而假"：
1. 不许把推断当事实
2. 不许夸大证据
3. 先 dry-run 再写入
4. 每阶段产报告
5. 不许跳验收
6. surgical 改动（只动该动的）
7. **canon 唯一真源 = `prototypes_db/*.json`，严禁运行 `build_prototypes_db.py`**
8. 不确定就停
9. 全程 `python -X utf8`

来自 `AGENTS.md`：
- 最小改动，preserve schema/audit trail
- 不修 `tools/litextract`、不改 `*_doi_map.json`
- 不提交本地设置/凭证/绝对路径
- Required validation 必须跑

## 8. 已知注意事项

- **速度**：串行逐原型调用 LLM，约 1 原型/分钟，全量 ~100 分钟。如嫌慢可改并行（如 ThreadPool/并发调 DashScope），但需注意 Dashboard 限流（429）。当前脚本是串行的，改写并行需谨慎验证。
- **非生物实体的 organism**（如 beta-cyclodextrin 仿生材料）：`scientific_en` 可能是描述性翻译而非纯物种名，忠实翻译即可，属正常。
- **超大原型**（chitosan 110 / water-strider 52 / mussel 55）：必须 `--chunk-size 8`，否则截断。
- 脚本 `--write` 用 `json.dump(ensure_ascii=False, indent=2)` 重写整个文件；会改变文件格式/行尾为统一风格，属可接受（不改语义，纯加字段）。写入前建议先 git diff 抽查 1-2 个文件确认纯新增。