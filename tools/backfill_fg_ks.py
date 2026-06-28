#!/usr/bin/env python3
"""Backfill functional_groups and key_structures for all mechanisms."""
import json, glob, re, sys
from pathlib import Path

FG_PATTERNS = [
    (r'[-‐]?OH|羟基|hydroxyl', '-OH（羟基）'),
    (r'[-‐]?COOH|羧基|carboxyl', '-COOH（羧基）'),
    (r'[-‐]?COO[⁻\-]|羧基阴离子|carboxylate|COO-', '-COO⁻（羧基阴离子）'),
    (r'[-‐]?C=O|羰基|carbonyl', '-C=O（羰基）'),
    (r'[-‐]?O[-‐]?|醚键|ether', '-O-（醚键）'),
    (r'醛基|aldehyde', '-CHO（醛基）'),
    (r'酯基|ester', '-COO-（酯基）'),
    (r'[-‐]?NH2|氨基|amine|amino', '-NH₂（氨基）'),
    (r'[-‐]?NH3[⁺\+]|质子化氨基|protonated amino', '-NH₃⁺（质子化氨基）'),
    (r'亚氨基|imine', '-NH-（亚氨基）'),
    (r'季铵|quaternary ammonium', '季铵基团'),
    (r'酰胺|amide|[-‐]?CONH', '-CONH-（酰胺键）'),
    (r'脲基|urea', '脲基'),
    (r'[-‐]?SH|巯基|thiol|sulfhydryl', '-SH（巯基）'),
    (r'二硫键|disulfide', '-S-S-（二硫键）'),
    (r'磺酸|sulfonate', '-SO₃⁻（磺酸基）'),
    (r'磷酸|phosphate|PO4|磷酰基', '-PO₄³⁻（磷酸基）'),
    (r'膦酸|phosphonate', '膦酸基'),
    (r'邻苯二酚|catechol|DOPA', '邻苯二酚（catechol）'),
    (r'芳香环|苯环|aromatic|phenyl', '芳香环'),
    (r'吲哚|indole', '吲哚环'),
    (r'咪唑|imidazole', '咪唑环'),
    (r'胍基|guanidinium|guanidine', '胍基'),
    (r'静电.*吸引|静电.*作用|electrostatic', '静电作用位点'),
    (r'π.*π.*堆积|pi.*pi.*stack', 'π-π堆积位点'),
    (r'氢键|hydrogen bond', '氢键位点'),
    (r'范德华|van der Waals', '范德华力'),
    (r'离子交换|ion.exchange', '离子交换位点'),
    (r'配位|coordination|chelat|螯合', '配位/螯合位点'),
    (r'疏水.*相互作用|hydrophobic.*interaction', '疏水相互作用'),
    (r'氧化还原|redox', '氧化还原位点'),
    # Superhydrophobic materials
    (r'氟化|fluorin|FAS|氟烷基硅烷', '氟化表面基团'),
    (r'硅烷|silane|silaniz', '硅烷偶联剂'),
    (r'PDMS|聚二甲基硅氧烷|dimethylsiloxane', 'PDMS硅氧烷'),
    (r'PTFE|聚四氟乙烯|polytetrafluoroethylene', 'PTFE氟碳基团'),
    (r'低表面能|low.surface.energy', '低表面能化学物质'),
    (r'蜡管|wax.tubu', '蜡质疏水层'),
    (r'硬脂酸|stearic', '硬脂酸疏水层'),
    (r'油酸|oleic', '油酸疏水层'),
    # Common polymers
    (r'PDA|聚多巴胺|polydopamine', '聚多巴胺（PDA）邻苯二酚/胺基'),
    (r'PNIPAM|聚N-异丙基丙烯酰胺', 'PNIPAM酰胺基'),
    (r'PFMA|聚全氟甲基丙烯酸酯', 'PFMA氟碳基团'),
    (r'PLA|聚乳酸|polylactic', 'PLA酯基'),
    (r'PPFEMA|聚全氟乙基甲基丙烯酸酯', 'PPFEMA氟碳基团'),
    (r'PVDF|聚偏氟乙烯', 'PVDF氟碳基团'),
    (r'PVA|聚乙烯醇|polyvinyl alcohol', 'PVA羟基'),
    (r'PEI|聚乙烯亚胺|polyethyleneimine', 'PEI胺基'),
    (r'PAM|聚丙烯酰胺|polyacrylamide', 'PAM酰胺基'),
    (r'PEG|聚乙二醇|polyethylene glycol', 'PEG醚键'),
    (r'GO|氧化石墨烯|graphene oxide', 'GO羧基/羟基/环氧基'),
    (r'MXene|MXene', 'MXene表面官能团'),
    (r'MWCNT|多壁碳纳米管|multi.wall.*carbon.*nanotube', 'MWCNT表面基团'),
    (r'碳纳米管|carbon.*nanotube|CNT', '碳纳米管表面基团'),
    (r'石墨烯|graphene', '石墨烯表面基团'),
    (r'壳聚糖|chitosan', '壳聚糖氨基/羟基'),
    (r'海藻酸|alginate', '海藻酸羧基/羟基'),
    (r'纤维素|cellulose', '纤维素羟基'),
    (r'丝素蛋白|silk.fibroin', '丝素蛋白酰胺基'),
    (r'角蛋白|keratin', '角蛋白酰胺基/巯基'),
    (r'几丁质|chitin', '几丁质乙酰胺基/羟基'),
]

KS_PATTERNS = [
    (r'[Hh]Ap|羟基磷灰石|hydroxyapatite', 'HAp羟基磷灰石晶体'),
    (r'方解石|calcite', '方解石晶体'),
    (r'文石|aragonite', '文石晶体'),
    (r'[Zz][Ii][Ff]|沸石咪唑', 'ZIF框架'),
    (r'MOF|金属有机框架', '金属有机框架（MOF）'),
    (r'β.*折叠|beta.sheet', 'β-折叠'),
    (r'α.*螺旋|alpha.helix', 'α-螺旋'),
    (r'胶原.*三螺旋|collagen.*triple', '胶原三螺旋'),
    (r'纳米纤维|nanofiber', '纳米纤维网络'),
    (r'纳米管|nanotube', '纳米管'),
    (r'纳米粒子|nanoparticle', '纳米粒子'),
    (r'纳米粗糙度|nano.?rough', '纳米粗糙度'),
    (r'微纳.*双重|micro.nano.*dual|hierarchical.*rough', '微纳双重结构'),
    (r'分级.*多孔|hierarchical.*porous', '分级多孔结构'),
    (r'介孔|mesoporous', '介孔结构'),
    (r'超疏水|superhydrophobic', '超疏水表面'),
    (r'超亲水|superhydrophilic', '超亲水表面'),
    (r'疏水.*表面|hydrophobic.*surface', '疏水表面'),
    (r'亲水.*表面|hydrophilic.*surface', '亲水表面'),
    (r'两亲|amphiphilic', '两亲性表面'),
    (r'滑移表面|slippery.*surface|SLIPS', '滑移表面（SLIPS）'),
    (r'水下超疏油|underwater.*superoleophobic', '水下超疏油表面'),
    (r'Cassie|cassie', 'Cassie-Baxter润湿态'),
    (r'荷叶效应|lotus.effect', '荷叶自清洁效应'),
    (r'乳突|papilla', '微乳突结构'),
    (r'蛋盒|egg.box', '蛋盒凝胶结构'),
    (r'水凝胶|hydrogel', '水凝胶网络'),
    (r'气凝胶|aerogel', '气凝胶'),
    (r'交联|cross.?link', '交联网络'),
    (r'3D.*互连|三维.*网络', '3D互连网络'),
    (r'细胞壁|cell.wall', '细胞壁结构'),
    (r'细胞膜|cell.membrane|bilayer|脂质双层', '细胞膜双层'),
    (r'离子通道|ion.channel', '离子通道'),
    (r'静电纺丝|electrospun', '静电纺丝纤维'),
    (r'Janus|janus', 'Janus双面结构'),
    (r'自清洁|self.?clean', '自清洁表面'),
    (r'油水分离|oil.?water.*separation', '油水分离结构'),
    (r'吸附|adsorption|adsorb', '吸附结构'),
    (r'生物矿化|biomineralization', '生物矿化模板'),
    (r'润湿|wetting', '润湿结构'),
    (r'滚动角|sliding.angle|roll.off', '滚动角特征'),
    (r'接触角|contact.angle|WCA', '接触角特征'),
    (r'表面能|surface.energy', '表面能特征'),
    (r'粗糙度|roughness', '表面粗糙度'),
    (r'微米级|micron.scale', '微米级结构'),
    (r'纳米级|nano.scale', '纳米级结构'),
    (r'乳突|papillae|papilla', '微乳突结构'),
    (r'层次结构|hierarchical', '层次结构'),
    (r'涂层|coating', '涂层结构'),
    (r'膜|membrane', '膜结构'),
    (r'纤维|fiber', '纤维结构'),
    (r'凝胶|gel', '凝胶结构'),
    (r'粉末|powder', '粉末结构'),
    (r'颗粒|particle|granule', '颗粒结构'),
]

def safe_str(val):
    if val is None: return ''
    if isinstance(val, list): return ' '.join(str(x) for x in val)
    if isinstance(val, dict): return json.dumps(val, ensure_ascii=False)
    return str(val)

def extract(text, patterns):
    if not text: return []
    results, seen = [], set()
    for pattern, label in patterns:
        if re.search(pattern, text, re.IGNORECASE) and label not in seen:
            results.append(label)
            seen.add(label)
    return results

DB_DIR = Path(__file__).resolve().parents[1] / 'prototypes_db'
SKIP = {'biomineralization-template', 'coral-skeleton', 'dna-aptamer', 'magnetic-bacteria', 'mycelium'}
updated = 0

for jp in sorted(glob.glob(str(DB_DIR / '*.json')) + glob.glob(str(DB_DIR / '**' / '*.json'))):
    if '_visual_cache' in jp or 'enrichment' in jp or 'materials_reference' in jp:
        continue
    try:
        with open(jp, encoding='utf-8') as f:
            data = json.load(f)
    except:
        continue
    pid = data.get('id', Path(jp).stem)
    if pid in SKIP:
        continue
    changed = False
    for m in data.get('mechanisms', []):
        combined = f"{safe_str(m.get('name'))} {safe_str(m.get('description'))} {safe_str((m.get('causal_chain') or {}).get('transferable_principle'))}"
        fg = extract(combined, FG_PATTERNS)
        ks = extract(combined, KS_PATTERNS)
        old_fg = m.get('functional_groups') or []
        old_ks = m.get('key_structures') or []
        if isinstance(old_fg, str):
            old_fg = [old_fg]
        if isinstance(old_ks, str):
            old_ks = [old_ks]
        new_fg = list(set(old_fg + fg)) if fg else old_fg
        new_ks = list(set(old_ks + ks)) if ks else old_ks
        if new_fg != old_fg or new_ks != old_ks:
            m['functional_groups'] = new_fg
            m['key_structures'] = new_ks
            changed = True
            updated += 1
    if changed:
        with open(jp, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

print(f"Updated: {updated}")

# Verify
no_fg = no_ks = total = 0
for jp in sorted(glob.glob(str(DB_DIR / '*.json')) + glob.glob(str(DB_DIR / '**' / '*.json'))):
    if '_visual_cache' in jp or 'enrichment' in jp or 'materials_reference' in jp:
        continue
    try:
        with open(jp, encoding='utf-8') as f:
            data = json.load(f)
    except:
        continue
    if 'placeholder' in (data.get('scope_note') or '').lower():
        continue
    for m in data.get('mechanisms', []):
        total += 1
        if not m.get('functional_groups'): no_fg += 1
        if not m.get('key_structures'): no_ks += 1

print(f"\nResults:")
print(f"  functional_groups: {no_fg}/{total} missing ({no_fg/total*100:.0f}%)")
print(f"  key_structures: {no_ks}/{total} missing ({no_ks/total*100:.0f}%)")
