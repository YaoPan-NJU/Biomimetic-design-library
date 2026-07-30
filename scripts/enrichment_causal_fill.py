#!/usr/bin/env python3
"""
Enrichment Causal Chain Batch Fill v2
Structure: enrichment is {mechanisms: {key: {causal_chain: {...}}}}
Main JSON is {mechanisms: [{name, causal_chain, description, ref_doi}, ...]}
Match by exact name key.
"""

import json
import os
import sys
from pathlib import Path

BASE = Path("/Users/panyao/Desktop/Biomimetic-design-library/prototypes_db")
ENRICHMENT_DIR = BASE / "enrichment"

SKIP_FILES = {"biomineralization-template.json", "coral-skeleton.json", "magnetic-bacteria.json"}

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def is_cc_empty(cc):
    """Check if a causal_chain dict is effectively empty."""
    if not cc or not isinstance(cc, dict):
        return True
    for field in ["pollutant_feature", "bio_structure", "interaction", "why_it_works"]:
        val = cc.get(field)
        if isinstance(val, dict):
            if val.get("text", "").strip():
                return False
        elif isinstance(val, str) and val.strip():
            return False
    return True

def is_cc_filled(cc):
    """Check if a causal_chain has actual content."""
    return not is_cc_empty(cc)

def extract_from_description(description, ref_doi, mechanism_idx):
    """Build a causal_chain from mechanism description."""
    if not description or not description.strip():
        return None
    
    basis = "from_source" if ref_doi else "from_mechanism_description"
    desc = description.strip()
    
    # Use full description as basis for extraction
    # Split into sentences/clauses for better extraction
    # Chinese and English mixed text
    
    cc = {
        "pollutant_feature": {"text": "", "basis": basis, "locator": f"mechanism[{mechanism_idx}]"},
        "bio_structure": {"text": "", "basis": basis, "locator": f"mechanism[{mechanism_idx}]"},
        "interaction": {"text": "", "basis": basis, "locator": f"mechanism[{mechanism_idx}]"},
        "why_it_works": {"text": "", "basis": basis, "locator": f"mechanism[{mechanism_idx}]"},
        "boundary_conditions": [],
        "transferable_principle": "",
        "verification_quote": None,
    }
    
    # For short descriptions, put the whole thing in the most relevant field
    # and leave others empty. For longer ones, try to split.
    
    # Heuristic: if description is short (<100 chars), put in interaction
    if len(desc) < 100:
        cc["interaction"]["text"] = desc
        return cc
    
    # For longer descriptions, distribute across fields based on content
    # pollutant_feature: pollutants, contaminants, metals, ions, dyes, etc.
    pollutant_kw = ["重金属", "金属离子", "Pb", "Cd", "Cr", "Cu", "Zn", "Hg", "As", "Ni", "Co", "Mn",
                     "污染物", "染料", "有机物", "PAH", "酚", "油", "石油", "药物", "农药", "抗生素",
                     "磷", "磷酸盐", "砷", "氟", "硝酸盐", "氨氮", "COD", "BOD", "PFAS",
                     "pollutant", "contaminant", "heavy metal", "dye", "organic", "ion"]
    bio_kw = ["壳聚糖", "羟基磷灰石", "HAp", "膜", "细胞", "细菌", "藻", "丝", "纤维",
              "蛋白", "DNA", "RNA", "适配体", "肽", "多糖", "几丁质", "纤维素", "胶原",
              "二氧化硅", "碳酸钙", "珍珠层", "纤丝", "蜘蛛丝", "贻贝", "菌丝", "生物膜",
              "外多糖", "EPS", "单宁", "聚多巴胺", "PDA", "螯合", "MOF", "沸石",
              "chitosan", "hydroxyapatite", "membrane", "cell", "bacteria", "silk", "fiber",
              "protein", "aptamer", "peptide", "polysaccharide", "chitin", "cellulose", "collagen"]
    interaction_kw = ["吸附", "结合", "螯合", "络合", "配位", "交换", "沉淀", "共沉淀",
                      "絮凝", "离子交换", "静电", "氢键", "疏水", "π-π", "物理吸附", "化学吸附",
                      "表面配合", "内球", "外球", "溶解", "再沉淀", "降解", "催化", "氧化", "还原",
                      "adsorption", "binding", "chelation", "complexation", "coordination", "exchange",
                      "precipitation", "electrostatic", "hydrogen bond", "hydrophobic"]
    why_kw = ["因为", "由于", "因此", "从而", "导致", "使得", "可以", "能够", "有效", "高效",
              "选择性", "特异性", "高容量", "快速", "可再生", "可重复", "循环", "稳定性",
              "去除率", "吸附容量", "mg/g", "%", "效率",
              "because", "due to", "therefore", "enabling", "effective", "efficient",
              "selective", "capacity", "removal", "efficiency"]
    
    # Score each sentence/clause
    # Split by common delimiters
    import re
    clauses = re.split(r'[；;。\n]', desc)
    clauses = [c.strip() for c in clauses if c.strip()]
    
    field_texts = {"pollutant_feature": [], "bio_structure": [], "interaction": [], "why_it_works": []}
    
    for clause in clauses:
        cl_lower = clause.lower()
        scores = {
            "pollutant_feature": sum(1 for kw in pollutant_kw if kw.lower() in cl_lower),
            "bio_structure": sum(1 for kw in bio_kw if kw.lower() in cl_lower),
            "interaction": sum(1 for kw in interaction_kw if kw.lower() in cl_lower),
            "why_it_works": sum(1 for kw in why_kw if kw.lower() in cl_lower),
        }
        best = max(scores, key=scores.get)
        if scores[best] > 0:
            field_texts[best].append(clause)
    
    # If no field got anything, put everything in interaction
    if not any(field_texts.values()):
        cc["interaction"]["text"] = desc
        return cc
    
    # Assign texts
    for field in field_texts:
        if field_texts[field]:
            text = "；".join(field_texts[field])
            if len(text) > 500:
                text = text[:500]
            cc[field]["text"] = text
    
    # Ensure at least 2 fields have content
    filled = sum(1 for f in field_texts if field_texts[f])
    if filled < 2:
        # Distribute: put first half in interaction, second half in why_it_works
        mid = len(desc) // 2
        # Find nearest sentence boundary
        for i in range(mid, min(mid+50, len(desc))):
            if desc[i] in '；;。':
                mid = i + 1
                break
        if not cc["interaction"]["text"]:
            cc["interaction"]["text"] = desc[:mid].strip()
        if not cc["why_it_works"]["text"]:
            cc["why_it_works"]["text"] = desc[mid:].strip() if mid < len(desc) else ""
    
    # Final check: at least one field must have content
    if not any(cc[f]["text"] for f in ["pollutant_feature", "bio_structure", "interaction", "why_it_works"]):
        return None
    
    return cc

def main():
    stats = {}
    total_filled = 0
    total_already = 0
    total_no_match = 0
    total_no_data = 0
    total_skipped_file = 0
    total_mechanisms = 0

    enrichment_files = sorted(ENRICHMENT_DIR.glob("*.json"))

    for efile in enrichment_files:
        fname = efile.name
        if fname in SKIP_FILES:
            stats[fname] = {"status": "skipped", "reason": "3 empty files rule"}
            total_skipped_file += 1
            continue

        edata = load_json(efile)
        main_file = BASE / fname
        if not main_file.exists():
            stats[fname] = {"status": "error", "reason": "main JSON not found"}
            continue

        main_data = load_json(main_file)
        main_mechs = main_data.get("mechanisms", [])
        
        # Build name -> mechanism index lookup
        main_by_name = {}
        for idx, m in enumerate(main_mechs):
            name = m.get("name", "")
            main_by_name[name] = idx

        e_mechs = edata.get("mechanisms", {})
        filled = 0
        already = 0
        no_match = 0
        no_data = 0

        for ekey, evalue in e_mechs.items():
            total_mechanisms += 1
            e_cc = evalue.get("causal_chain", {})
            
            # Check if already filled
            if is_cc_filled(e_cc):
                already += 1
                continue
            
            # Match to main mechanism by name
            if ekey in main_by_name:
                m_idx = main_by_name[ekey]
                m_mech = main_mechs[m_idx]
                m_cc = m_mech.get("causal_chain")
                
                if m_cc and is_cc_filled(m_cc):
                    # Direct copy
                    evalue["causal_chain"] = m_cc
                    filled += 1
                elif (m_mech.get("description") or "").strip():
                    # Extract from description
                    cc = extract_from_description(
                        m_mech["description"],
                        m_mech.get("ref_doi", ""),
                        m_idx
                    )
                    if cc:
                        evalue["causal_chain"] = cc
                        filled += 1
                    else:
                        no_data += 1
                else:
                    no_data += 1
            else:
                no_match += 1

        save_json(efile, edata)

        stats[fname] = {
            "status": "processed",
            "total_mechs": len(e_mechs),
            "filled": filled,
            "already_filled": already,
            "no_main_match": no_match,
            "no_data": no_data,
        }
        total_filled += filled
        total_already += already
        total_no_match += no_match
        total_no_data += no_data

    # Print summary
    print("=" * 70)
    print("ENRICHMENT CAUSAL CHAIN FILL SUMMARY")
    print("=" * 70)
    print(f"\nTotal enrichment mechanisms:  {total_mechanisms}")
    print(f"Filled this run:              {total_filled}")
    print(f"Already filled (skipped):     {total_already}")
    print(f"No main JSON match:           {total_no_match}")
    print(f"Main had no data:             {total_no_data}")
    print(f"Files skipped (3 empty):      {total_skipped_file}")
    print()
    print("Per-file breakdown:")
    print("-" * 70)
    for fname, info in sorted(stats.items()):
        if info["status"] == "skipped":
            print(f"  {fname}: SKIPPED ({info['reason']})")
        elif info["status"] == "error":
            print(f"  {fname}: ERROR ({info['reason']})")
        else:
            print(f"  {fname}: {info['filled']} filled, {info['already_filled']} already, {info['no_main_match']} no_match, {info['no_data']} no_data  (total {info['total_mechs']})")

    # Output for report
    print("\n---STATS_JSON---")
    print(json.dumps({
        "total_mechanisms": total_mechanisms,
        "total_filled": total_filled,
        "total_already_filled": total_already,
        "total_no_match": total_no_match,
        "total_main_no_data": total_no_data,
        "total_files_skipped": total_skipped_file,
        "per_file": stats,
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
