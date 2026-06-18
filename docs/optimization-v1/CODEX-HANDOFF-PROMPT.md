你是 Codex/QoderWork，即将接手仿生设计库项目的持续推进工作。

== 项目概况 ==
- 仓库: Biomimetic-design-library, review 分支
- 定位: 仿生水处理设计参考库 (ADRMATS 系统)，不设计材料，只提供仿生设计灵感
- 当前规模: 36 个活跃原型 (其中 6 个 pending_extraction)

== 最近完成的工作 ==
Task 64-68: 修复 build merge_with_existing 保留 verification_quote; 修复 multimodal_verify (增量保存+API重试+missing_pdf); 13 原型多模态验证
Task 69-73: 原型扩展 24->36; 激活 5 分离+1 停放原型; 6 个 skeleton entry; 新原型验证; 文档更新

== 当前数据状态 ==
- active prototypes: 36 (6 pending_extraction)
- performance_data: 397/431 verified (92%)
- mechanisms: 265/773 verified (34%)
- chimera: 0 violations
- consistency: 12 errors (feature-mapping missing for new prototypes)

== 待推进工作 ==
P0:
- 对 6 个 pending_extraction 原型执行 litextract 提取 (tools/litextract/)
  文献库: 仿生文献库/ 下 626 篇 PDF
  需要: MIMO_API_KEY 配置在 tools/litextract/.env
- 解决 mechanisms 无 PDF 匹配: 检查 source_file 路径 / 用 DOI+Sci-Hub 下载

P1:
- mechanisms 覆盖率从 34% 继续推高 (multimodal_verify.py)
- 边界条件从 soft caution 升级为 hard DO-NOT (需 PDF 提取阈值)

P2:
- check_causal_chain.py / check_boundary_guardrail.py 24 原型未达标

== 关键脚本 ==
- python -X utf8 tools/build_prototypes_db.py
- python -X utf8 tools/multimodal_verify.py {prototype_name}
- python -X utf8 tools/check_chimera.py --strict
- python -X utf8 tools/validate_consistency.py

== 关键约束 ==
- 所有 Python 命令加 -X utf8
- build 会重新生成所有 JSON, merge_with_existing 保留 verification_quote/source_locator
- multimodal_verify.py 使用 mimo-v2.5 (max_tokens>=4096, 双 key 轮询)
- canon 冻结原则: 不直接编辑已由 litextract 填充的字段
- review 分支, push 到 origin/review

== 文件位置 ==
- 交接文档: docs/optimization-v1/COLLAB-HANDOFF.md
- 任务指令: docs/optimization-v1/CLAUDE-CODE-TASK-*.md
- 文献库: 仿生文献库/ (626 篇)
