export const meta = {
  name: 'bmdl-en-review',
  description: 'Adversarial quality review of English translations vs Chinese sources',
  phases: [{ title: 'Review', detail: 'one reviewer per batch of prototypes' }],
}

const REVIEW_PROMPT = `你是资深审稿人，具备生物化学、分子生物学、材料科学、环境工程背景。任务是**对抗式审查** BMDL（仿生设计库）中文机制内容到英文的翻译质量，逐原型逐机制对照中英，找出**事实性错误**和**术语错用**。

【输入文件】对每个待审原型，读取两个文件：
- 中文源: /tmp/bmdl_en_backfill/sources/<id>.json （含 organism_scientific、mechanisms[i].name/description/transferable_principle）
- 英文翻译: /tmp/bmdl_en_backfill/translations/<id>.json （含 organism_scientific_en、mechanisms[i].name_en/description_en/transferable_principle_en）

【审查维度】（按优先级）：
1. **事实一致性（最高优先）**：英文翻译是否与中文源的科学事实冲突或曲解——
   - 数字/数值：Km、IC50、含量、浓度、距离（Å）、温度、尺寸等是否一致
   - 单位、化学式、分子式、元素、残基编号（如 Phe211）、PDB ID、基因名、物种名
   - 方向与归属：如"顶端膜/基底侧"、"摄取/外排"、"抑制/激活"、"A 抑制 B"是否被译反
   - 机理因果逻辑：条件-结果关系是否被改写
   - 把"部分/可能/定性"译成"全部/一定/定量"等程度变更
2. **术语准确性**：专业术语是否翻译准确、标准。常见核对点：
   - 跨膜域→transmembrane domain；钠离子非依赖→sodium-independent
   - 芳香笼→aromatic cage；阳离子锚→cationic anchor；edge-to-face 相互作用
   - 主客体包结→host-guest inclusion；螯合→chelation；离子交换→ion exchange
   - 超疏水→superhydrophobic；接触角滞后→contact angle hysteresis
   - 若发现更标准/更准确的术语译法，报告并给出建议
3. **虚构**：英文翻译里是否出现了中文源完全没有的信息（新增的事实、数字、结论）
4. **严重遗漏**：源的关键信息（关键数据、关键机理步骤、限定条件）是否在翻译中丢失

【判定纪律】：
- 只报告**确定或很可能**的问题；不确定的标 medium 并说明理由，不要臆断。
- 中文源本身简短/质量低（如 description 就一个数字、tp 是"基于机制: xxx"复述）→ 翻译忠实转译**不算错误**。
- 源字段为空 → 翻译为空串是正确行为，不算问题。
- 忠实保留专有名词/原文已英文内容是正确行为。
- high = 事实错误或术语错用（必须修正）；medium = 表述不准确、易误导或遗漏；low = 可读性/风格（一般不报）。

【输出】对每个待审原型给出一个 JSON。若该原型无问题，findings 为空数组。`;

const REVIEW_ITEM_SCHEMA = {
  type: 'object',
  required: ['proto_id', 'n_mechanisms', 'findings'],
  properties: {
    proto_id: { type: 'string' },
    n_mechanisms: { type: 'integer' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['idx', 'field', 'severity', 'issue'],
        properties: {
          idx: { type: 'integer' },
          field: { type: 'string', enum: ['name_en', 'description_en', 'transferable_principle_en', 'organism_scientific_en'] },
          severity: { type: 'string', enum: ['high', 'medium', 'low'] },
          issue: { type: 'string', description: '具体问题描述' },
          zh: { type: 'string', description: '中文源对应片段' },
          en: { type: 'string', description: '英文翻译对应片段' },
          suggestion: { type: 'string', description: '建议修正' },
        },
      },
    },
    summary_note: { type: 'string' },
  },
}

const REVIEW_SCHEMA = {
  type: 'object',
  required: ['reviews'],
  properties: {
    reviews: {
      type: 'array',
      items: REVIEW_ITEM_SCHEMA,
    },
  },
}

phase('Review')
const results = await parallel(args.batches.map((ids, bi) => () =>
  agent(
    `${REVIEW_PROMPT}\n\n【本次待审原型】${ids.map(i => `\n- ${i}（源 /tmp/bmdl_en_backfill/sources/${i}.json，译 /tmp/bmdl_en_backfill/translations/${i}.json）`).join('')}\n\n请逐个原型读取并审查，在 reviews 数组里为每个原型输出一个审查对象（findings 为空数组表示该原型无问题）。`,
    { label: `review:batch${bi + 1}`, phase: 'Review', schema: REVIEW_SCHEMA }
  )
))

return results.filter(Boolean)