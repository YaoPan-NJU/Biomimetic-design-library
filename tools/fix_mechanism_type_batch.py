#!/usr/bin/env python3
"""
批量修正 mechanism_type (mechanisms[0].name) 字段
基于 BMDL_mechanism_type_fix_report_20260721.md
"""
import json
import os
from pathlib import Path

# 34 条 FIX 映射
FIXES = {
    "algae-polysaccharide": {
        "old": "Alginate gel bead adsorption",
        "new": "褐藻多糖羧基螯合配位与离子交换",
    },
    "bacterial-cellulose": {
        "old": "3D nanofiber network filtration",
        "new": "细菌纤维素纳米纤维网物理筛分与表面羟基吸附",
    },
    "bird-feather-keratin": {
        "old": "",
        "new": "羽毛角蛋白巯基/氨基软酸重金属配位",
    },
    "bone-structure": {
        "old": "HAp膜重金属去除性能",
        "new": "骨羟基磷灰石钙离子交换与表面配位",
    },
    "cactus-spine": {
        "old": "仿荷叶PS纳米纤维/微球复合超疏水表面接触角",
        "new": "仙人掌刺锥形梯度润湿定向集水",
    },
    "cell-membrane-ion-channel": {
        "old": "C14lyso脂质体vs DOPC脂质体结构差异 Structure difference C14lyso vs DOPC liposomes",
        "new": "脂质双层酰基链密度调控水渗透选择性",
    },
    "chitosan": {
        "old": "吸附机制-内球配合物 Adsorption mechanism - inner-sphere complexation",
        "new": "壳聚糖氨基/羟基多齿螯合与静电吸附",
    },
    "chlorella-cell-wall": {
        "old": "pH对藻类染料吸附的影响 Effect of pH on algal dye adsorption",
        "new": "小球藻细胞壁含氧含氮官能团络合与静电吸附",
    },
    "coral-skeleton": {
        "old": "珊瑚文石结构重金属固定",
        "new": "珊瑚文石碳酸钙钙位点吸附与重金属碳酸盐共沉淀",
    },
    "diatom-frustule": {
        "old": "热处理——550°C表面Si-OH暴露",
        "new": "硅藻壳多尺度孔限域筛分与表面硅羟基配位",
    },
    "fish-scale-hydroxyapatite": {
        "old": "八重协同吸附机制",
        "new": "鱼鳞羟基磷灰石纳米晶钙离子交换与磷酸盐共沉淀",
    },
    "fungal-biosorption": {
        "old": "",
        "new": "真菌细胞壁几丁质/葡聚糖官能团配位生物吸附",
    },
    "insect-chitin": {
        "old": "",
        "new": "昆虫外骨骼几丁质乙酰胺基/羟基配位",
    },
    "iron-oxidizing-bacteria": {
        "old": "MICP化学反应机理",
        "new": "亚铁氧化驱动铁氢氧化物共沉淀",
    },
    "lobster-exoskeleton": {
        "old": "Chitosan beads的六种吸附机制",
        "new": "龙虾外骨骼几丁质氨基/羟基螯合吸附",
    },
    "lotus-leaf": {
        "old": "超疏水材料构建基本原理 - Young方程/Wenzel模型/Cassie-Baxter模型",
        "new": "荷叶微纳层级结构蜡质层空气截留超疏水效应",
    },
    "mangrove-root": {
        "old": "人工湿地净化机制途径 Constructed wetland purification mechanisms",
        "new": "红树林根盐排斥选择性离子输运与根际微生物降解",
    },
    "metal-organic-framework": {
        "old": "MOF高比表面积孔道吸附",
        "new": "金属有机框架高比表面积孔道限域与配位吸附",
    },
    "microbial-exopolysaccharide": {
        "old": "",
        "new": "微生物胞外多糖羧基/羟基/硫酸基配位",
    },
    "mussel-foot-adhesion": {
        "old": "两性离子水合能力 vs PEG Zwitterion hydration capacity vs PEG",
        "new": "贻贝足丝DOPA儿茶酚-金属多齿配位与胺基静电黏附",
    },
    "oyster-shell": {
        "old": "牡蛎壳改性吸附机制",
        "new": "牡蛎壳文石碳酸钙离子交换与煅烧钙氧化物碱性沉淀",
    },
    "pitcher-plant-slippery-surface": {
        "old": "仿荷叶PS纳米纤维/微球复合超疏水表面接触角",
        "new": "猪笼草唇缘润湿超滑液层定向滑移(SLIPS)",
    },
    "plant-lignocellulosic-architecture": {
        "old": "Ion exchange Cd adsorption",
        "new": "植物木质纤维素羧基/硅酸盐基离子交换与络合",
    },
    "plant-tannin": {
        "old": "吸附机制",
        "new": "植物单宁芳香环π-π堆积与酚羟基氢键静电吸附",
    },
    "plant-wax-cuticle": {
        "old": "",
        "new": "植物表皮蜡质微纳层级晶体超疏水",
    },
    "polydopamine-coating": {
        "old": "超疏水抗菌表面'双重保险'原理",
        "new": "聚多巴胺儿茶酚/胺基多价协同表面黏附",
    },
    "rice-husk-phytolith": {
        "old": "",
        "new": "稻壳植硅体硅醇基络合与离子交换",
    },
    "scallop-shell": {
        "old": "钝化机理",
        "new": "扇贝壳文石碳酸钙离子交换与碳酸盐沉淀",
    },
    "shark-skin": {
        "old": "表面润湿性对细菌粘附的影响规律",
        "new": "鲨鱼皮盾鳞riblet微结构减阻抗污",
    },
    "silk-fibroin": {
        "old": "MO吸附机制",
        "new": "丝素蛋白氨基酸残基氨基/羧基配位与氢键吸附",
    },
    "spider-silk": {
        "old": "蜘蛛丝增强策略：金属掺杂和CNT/石墨烯复合",
        "new": "蜘蛛丝蛋白β-折叠与氨基酸残基配位吸附",
    },
    "superhydrophobic-artificial": {
        "old": "超疏水材料构建基本原理 - Young方程/Wenzel模型/Cassie-Baxter模型",
        "new": "Cassie-Baxter空气层截留超疏水(人工仿生)",
    },
    "water-strider-leg": {
        "old": "超疏水材料构建基本原理 - Young方程/Wenzel模型/Cassie-Baxter模型",
        "new": "水黾腿微纳刚毛疏水蜡质层气垫超疏水承载",
    },
    "wood-xylem": {
        "old": "吸附机制——分子态酚+静电排斥",
        "new": "木质部多级孔道木质素芳香结构π-π堆积与氢键选择性吸附",
    },
}

# 1 条 organism FIX
ORGANISM_FIX = {
    "chitosan": {
        "old": "Crustacea",
        "new": "Crustacea (甲壳类外骨骼几丁质)",
    }
}

# 2 条 DELETE (deprecated)
DELETES = [
    "diatom-inspired-porous",
    "silkworm-silk",
]


def find_json_file(prototype_id: str) -> Path:
    """查找原型 JSON 文件（主目录或 quarantined）"""
    main_path = Path(f"prototypes_db/{prototype_id}.json")
    if main_path.exists():
        return main_path
    quarantined_path = Path(f"prototypes_db/quarantined/{prototype_id}.json")
    if quarantined_path.exists():
        return quarantined_path
    return None


def fix_mechanism_type():
    """批量修正 mechanism_type"""
    fixed = []
    skipped = []
    
    for pid, fix in FIXES.items():
        json_path = find_json_file(pid)
        if not json_path:
            print(f"[SKIP] {pid}: JSON 文件不存在")
            skipped.append(pid)
            continue
        
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
        
        mechs = data.get("mechanisms", [])
        if not mechs:
            print(f"[SKIP] {pid}: 无 mechanisms 数组")
            skipped.append(pid)
            continue
        
        current = mechs[0].get("name", "")
        expected_old = fix["old"]
        new_val = fix["new"]
        
        # 验证当前值是否匹配
        if current != expected_old:
            print(f"[SKIP] {pid}: 当前值 '{current}' 不匹配预期 '{expected_old}'")
            skipped.append(pid)
            continue
        
        # 执行修改
        mechs[0]["name"] = new_val
        
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"[FIXED] {pid}: {expected_old} -> {new_val}")
        fixed.append(pid)
    
    print(f"\n=== mechanism_type FIX 完成: {len(fixed)} 已修复, {len(skipped)} 跳过 ===")
    return fixed, skipped


def fix_organism():
    """修正 organism 字段"""
    fixed = []
    
    for pid, fix in ORGANISM_FIX.items():
        json_path = find_json_file(pid)
        if not json_path:
            print(f"[SKIP] {pid}: JSON 文件不存在")
            continue
        
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
        
        organism = data.get("organism", {})
        current = organism.get("scientific", "")
        expected_old = fix["old"]
        new_val = fix["new"]
        
        if current != expected_old:
            print(f"[SKIP] {pid}: organism.scientific 当前值 '{current}' 不匹配预期 '{expected_old}'")
            continue
        
        organism["scientific"] = new_val
        
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"[FIXED] {pid} organism: {expected_old} -> {new_val}")
        fixed.append(pid)
    
    print(f"\n=== organism FIX 完成: {len(fixed)} 已修复 ===")
    return fixed


def delete_deprecated():
    """删除 deprecated 原型"""
    deleted = []
    
    for pid in DELETES:
        json_path = find_json_file(pid)
        if not json_path:
            print(f"[SKIP] {pid}: JSON 文件不存在")
            continue
        
        # 验证 lifecycle 是否为 deprecated
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
        
        lifecycle = data.get("lifecycle_status", data.get("status", ""))
        if lifecycle != "deprecated":
            print(f"[SKIP] {pid}: lifecycle 为 '{lifecycle}'，非 deprecated")
            continue
        
        os.remove(json_path)
        print(f"[DELETED] {pid}")
        deleted.append(pid)
    
    print(f"\n=== DELETE 完成: {len(deleted)} 已删除 ===")
    return deleted


if __name__ == "__main__":
    print("=" * 80)
    print("BMDL mechanism_type 批量修正")
    print("=" * 80)
    
    print("\n[1/3] 修正 mechanism_type (34 条)...")
    fix_mechanism_type()
    
    print("\n[2/3] 修正 organism (1 条)...")
    fix_organism()
    
    print("\n[3/3] 删除 deprecated 原型 (2 条)...")
    delete_deprecated()
    
    print("\n" + "=" * 80)
    print("全部完成")
    print("=" * 80)
