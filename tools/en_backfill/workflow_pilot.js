export const meta = {
  name: 'bmdl-en-pilot',
  description: 'Pilot: translate 3 prototypes (oat4/cactus/chitosan) to /tmp parts',
  phases: [{ title: 'Translate', detail: '3 agents, one per prototype' }],
}

const SPEC = `你是 BMDL（仿生设计库, Biomimetic Design Library）的忠实翻译引擎。你的任务是把指定原型的 4 类中文字段翻译成英文，并按协议写入 part 文件。

【只翻译这些字段】（绝不翻译/改动其他内容）：
1. organism.scientific（中文物种名）→ organism_scientific_en
2. mechanisms[i].name（中文机制名）→ name_en
3. mechanisms[i].description（中文机制描述）→ description_en
4. mechanisms[i].causal_chain.transferable_principle（中文可转译原理）→ transferable_principle_en

【翻译铁律】：
- 忠实翻译，绝不虚构：原文没有的信息绝不添加、不夸大、不臆测。
- 源字段为空字符串、null 或缺失 → 对应英文翻译字段必须输出空字符串 ""。
- 输出中不允许任何中文字符（也不允许全角标点【】（）；，。等），一律用英文标点。
- 保留并正确使用专业术语：生物化学、分子生物学、微生物学、材料科学、环境工程的学术术语。
- 专有名词原样保留：PDB ID（如 9U5A）、基因名（如 SLC22A11）、物种学名（斜体名如 Homo sapiens）、化学式、数字、单位、文献引用（如 Cha 2000）、缩写（如 E1S、PFAS、Km）。
- 中文人名/文献引用不要在英文里。

【各字段风格】：
- name_en：简洁英文名词短语（一个短语，如 "Two-point recognition of anionic head group by an aromatic-cationic substrate pocket"）。
- description_en：忠实英文摘要，2-4 句，覆盖原文关键信息（对象、机制、关键数据、结论），不添加原文没有的细节。
- transferable_principle_en：忠实英文摘要，2-3 句。
- organism_scientific_en：英文物种名（拉丁学名 + 通俗名，如 "OAT4 (SLC22A11) organic anion transporter"）；若原文是描述性文本（非纯物种），忠实翻译即可。

【大原型分批铁律】：
- 源文件内容是 mechanisms 数组。输出时把机制按每批最多 8 个切分，写成多个 part 文件。
- 每个 part 文件的 "idx" 必须与源文件机制的数组下标完全一致（0-based），顺序必须与源文件一致。
- 切分点按 idx 连续取：part_000 覆盖 idx 0..7，part_001 覆盖 idx 8..15，依此类推，最后一批可以不足 8 个。

【输出协议】：
- 输出目录：/tmp/bmdl_en_backfill/parts/<proto_id>/
- 每个 part 一个文件，命名 part_000.json、part_001.json、...（三位数字序号）。
- 每个 part 文件内容（严格 JSON）：
{
  "proto_id": "<proto_id>",
  "part": 0,
  "idx_start": 0,
  "organism_scientific_en": "..." | null,
  "mechanisms": [
    {"idx": 0, "name_en": "...", "description_en": "...", "transferable_principle_en": "..."},
    ...
  ]
}
- "organism_scientific_en" 只在 part_000 里填真实翻译，其他 part 一律填 null。
- 用 Write 工具逐个写入 part 文件（每个 part 一次 Write 完成，不要用 Edit 追加）。
- 全部 part 写完后，返回统计 JSON。`;

const RESULT_SCHEMA = {
  type: 'object',
  required: ['proto_id', 'status', 'parts_written', 'mechanisms_translated'],
  properties: {
    proto_id: { type: 'string' },
    status: { type: 'string', enum: ['ok', 'error'] },
    parts_written: { type: 'integer' },
    mechanisms_translated: { type: 'integer' },
    note: { type: 'string' },
  },
}

phase('Translate')
const results = await parallel(args.protos.map(p => () =>
  agent(
    `${SPEC}\n\n【本次待翻译原型】\n- proto_id: ${p.id}\n- 源文件路径: ${p.src}\n- 输出目录: ${p.parts_dir}\n\n请先 Read 源文件，核对其 proto_id 与 mechanisms 数量（${p.n_mech} 个），然后翻译并 Write 全部 part 文件，最后返回统计 JSON。`,
    { label: `translate:${p.id}`, phase: 'Translate', schema: RESULT_SCHEMA }
  )
))

return results.filter(Boolean)