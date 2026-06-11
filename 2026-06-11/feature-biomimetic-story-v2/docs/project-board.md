# 仿生设计库 -- 项目管理看板

> 最后更新: 2026-06-04
> 活跃分支: feature/biomimetic-story-v2

---

## 任务状态总览

| 状态 | 数量 |
|------|------|
| 已完成 | 8 |
| 进行中 | 0 |
| 待办 | 7 |

---

## 已完成任务

### DONE-001: 项目脚手架搭建
- 27个文件, 4465行代码, 31个测试
- 4阶段流水线架构 + 3 API provider支持
- 完成时间: 2026-06-04

### DONE-002: 多API负载均衡改造
- MODEL_ROUTING 支持列表式 round-robin 路由
- LLMClient.from_task_type() 增加 exclude_provider 参数
- 429重试时自动切换 provider
- 完成时间: 2026-06-04

### DONE-003: Phase 1 粗扫执行
- 302篇文献 -> 30个原型 -> 149次LLM调用
- 100%成功率, 0错误, 33次重试
- 耗时: 324秒
- 完成时间: 2026-06-04

### DONE-004: Phase 2 差距分析执行
- 30个原型并发深度评估
- 识别335个补充需求
- 耗时: 777秒
- 完成时间: 2026-06-04

### DONE-005: Phase 3 补充计划生成
- 336条搜索查询 (WoS/CNKI/Google Scholar)
- 3个方向: 方法论/仿生综述/跨原型比较
- 完成时间: 2026-06-04

### DONE-006: Phase 4 深度提取执行
- 30个原型全部生成 prototype.md
- 113个权重赋值, 156/156 feature-mapping条目已更新
- 耗时: 1158秒
- 完成时间: 2026-06-04

### DONE-007: Phase 2/4 并发改造
- Phase 2: 加ThreadPoolExecutor (6路并发)
- Phase 4: 加并发 (4路) + None安全访问 + qmax数值解析
- writer.py: feature-mapping.json不存在时优雅跳过
- 完成时间: 2026-06-04

### DONE-008: 执行报告与管理看板
- 完整的 Phase 1-4 执行监控报告
- 项目管理看板 (本文档)
- 完成时间: 2026-06-04

---

## 待办任务

### TODO-001 [P0]: 文献补充 -- 零覆盖原型
- 目标: 为5个零覆盖原型下载文献 (bone-structure, cactus-spine, cell-membrane-ion-channel, coral-skeleton, lobster-exoskeleton)
- 方法: 使用Phase 3生成的搜索查询, 每个原型至少下载5-10篇
- 预期产出: 新增5个原型的粗扫profile
- 验收标准: Phase 1重跑后覆盖原型数 >= 33

### TODO-002 [P0]: 统一原型命名体系
- 问题: 30个粗扫原型ID vs 51个目录ID 存在命名差异
- 方案: 建立ID映射表, 或合并/拆分原型目录
- 涉及原型: chitosan vs chitosan-adsorbent, diatom-frustule vs diatom-microspheres 等
- 预期产出: 统一的原型ID规范文档

### TODO-003 [P0]: 补充文献后重跑 Phase 4
- 前提: TODO-001 完成
- 目标: 填充仿生叙事章节 (5.1-5.5)
- 方法: 将补充文献放入 supplemented-papers/<id>/ 目录, 重跑Phase 4
- 验收标准: 叙事章节填充率 > 50%

### TODO-004 [P1]: 优化间接映射逻辑
- 问题: 间接映射"贪婪"分配导致噪音 (dna-aptamer/magnetic-bacteria论文完全重叠)
- 方案: 增加论文内容与原型的相关性评分阈值
- 涉及文件: prototype_mapper.py
- 预期产出: 映射精度提升, 减少不相关映射

### TODO-005 [P1]: 扩展原型数量
- 当前: 30个有效原型 (51个目录)
- 目标: 50+个原型
- 方法: 从现有目录中选取未覆盖的21个, 补充文献后纳入流水线
- 预期产出: 更完整的仿生知识覆盖

### TODO-006 [P2]: 增加全文深度提取比例
- 当前: Phase 4仅取前5篇论文的全文前8000字
- 目标: 扩展到10-15篇, 全文不限字数
- 涉及文件: phase4_deep_extract.py
- 预期产出: 定量数据填充率从~5%提升到>30%

### TODO-007 [P2]: 新兴污染物补充
- 缺失类型: 微塑料(microplastics), PFAS/PFOA, 抗生素耐药基因
- 方法: 定向搜索相关文献, 更新prototype_mapper.py关键词
- 预期产出: 污染物覆盖增加3-5个重要类型

---

## 技术债务

| 编号 | 描述 | 优先级 |
|------|------|--------|
| TD-001 | coding_plan API 调用比例偏低 (12.1%), 需调查并发配额限制 | 低 |
| TD-002 | 验证告警 (30个) 需排查: qmax格式含单位, evidence_level格式 | 低 |
| TD-003 | extraction/prototypes/ 目录是Phase 4误写到extraction下的副本, 应清理 | 低 |
| TD-004 | 测试覆盖不足: Phase 2-4 无单元测试 | 中 |

---

## 里程碑规划

```
M1: 流水线搭建 + Phase 1 首跑          [2026-06-04] DONE
M2: Phase 2-4 全流程完成               [2026-06-04] DONE
M3: 文献补充 + 原型命名统一            [待启动]
M4: 仿生叙事填充 + 映射优化            [待启动]
M5: 原型扩展至50+ + 全流程回归测试     [待启动]
M6: 交付准备 + 合并到main              [待启动]
```

---

## 快速接力指南

在新设备上继续工作:
1. `git clone` 或 `git pull` 到最新
2. 切换到 `feature/biomimetic-story-v2` 分支
3. 在 `extraction/.env` 中填入三个API key
4. 查看本文档的 "待办任务" 部分选择下一个任务
5. 运行流水线: `cd extraction && python3 run_pipeline.py phase1 phase2 phase3 phase4`
