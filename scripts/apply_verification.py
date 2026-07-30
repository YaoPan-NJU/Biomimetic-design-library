#!/usr/bin/env python3
"""
Targeted PDA-coating performance_data verification updater.
Uses pre-extracted quotes from PDF analysis.
"""

import json
import os

PROJECT = "/Users/panyao/Desktop/Biomimetic-design-library"
JSON_PATH = os.path.join(PROJECT, "prototypes_db/polydopamine-coating.json")

# Verification quotes mapped by (source_file_pattern, value_pattern)
# Each entry: (row_index, verification_quote, source_locator, verification_status)

UPDATES = {
    # === CN114887602A (4 rows) - missing PDF ===
    0: ("PDF not available locally", "N/A", "missing_pdf"),
    1: ("PDF not available locally", "N/A", "missing_pdf"),
    2: ("PDF not available locally", "N/A", "missing_pdf"),
    3: ("PDF not available locally", "N/A", "missing_pdf"),

    # === CN115055171A (1 row) ===
    4: (
        "Fe3O4@PDA@CSH复合磁性吸附材料对上述重金属去除率仍能保持在72％以上(特别是对镍离子的去除率仍能保持在78％以上)，材料回收率82％以上",
        "p.8, 说明书第[0036]段",
        "partial"
    ),

    # === CN113244898A (3 rows) ===
    5: (
        "在吸附剂剂量为5mg、pH为6、吸附时间为5h、Pb2+初始浓度为4mg/L条件下，PDA/KA/Fe3O4复合材料对Pb2+的去除率可以达到96.31%",
        "p.1 (摘要) / p.5 (说明书第[0037]段)",
        "partial"
    ),
    6: (
        "Pb2+浓度在4~70mg/L范围内时，随着浓度的增加，PDA/KA/Fe3O4对Pb2+的吸附容量迅速升高。当Pb2+浓度超过30mg/L以后，吸附容量基本保持不变，表明材料表面吸附位点已经基本达到饱和吸附。同时，随着Pb2+浓度的增加，材料对Pb2+的去除率明显降低",
        "p.10, 说明书第[0101]段",
        "partial"
    ),
    7: (
        "随着PDA/KA/Fe3O4剂量的增加，Pb2+的去除率也随着增大，当PDA/KA/Fe3O4剂量为5mg时，去除率达到最大为95.68%。当PDA/KA/Fe3O4剂量继续增大时，去除率基本不再发生变化",
        "p.10, 说明书第[0106]段",
        "partial"
    ),

    # === Group 1: Foroutan (9 rows) ===
    8: (
        "The highest elimination capacity (qm) for Hg(II), Co(II), and Ni(II) was set at 51.73 mg/g, 49.32 mg/g, and 48.09 mg/g, respectively",
        "p.1 (Abstract) / p.8 (Section 3.3)",
        "partial"
    ),
    9: (
        "The highest elimination capacity (qm) for Hg(II), Co(II), and Ni(II) was set at 51.73 mg/g, 49.32 mg/g, and 48.09 mg/g, respectively",
        "p.1 (Abstract) / p.8 (Section 3.3)",
        "partial"
    ),
    10: (
        "The highest elimination capacity (qm) for Hg(II), Co(II), and Ni(II) was set at 51.73 mg/g, 49.32 mg/g, and 48.09 mg/g, respectively",
        "p.1 (Abstract) / p.8 (Section 3.3)",
        "partial"
    ),
    11: (
        "As our findings show, with increasing water temperature from 25 °C to 50 °C, the elimination of Hg(II), Co(II), and Ni(II) are diminished from 94.36%, 93.66%, and 92.36% to 90.14%, 88.84%, and 87.46%, respectively",
        "p.7 (Section 3.4 Temperature and thermodynamic study)",
        "partial"
    ),
    12: (
        "As our findings show, with increasing water temperature from 25 °C to 50 °C, the elimination of Hg(II), Co(II), and Ni(II) are diminished from 94.36%, 93.66%, and 92.36% to 90.14%, 88.84%, and 87.46%, respectively",
        "p.7 (Section 3.4 Temperature and thermodynamic study)",
        "partial"
    ),
    13: (
        "As our findings show, with increasing water temperature from 25 °C to 50 °C, the elimination of Hg(II), Co(II), and Ni(II) are diminished from 94.36%, 93.66%, and 92.36% to 90.14%, 88.84%, and 87.46%, respectively",
        "p.7 (Section 3.4 Temperature and thermodynamic study)",
        "partial"
    ),
    14: (
        "As our findings show, with increasing water temperature from 25 °C to 50 °C, the elimination of Hg(II), Co(II), and Ni(II) are diminished from 94.36%, 93.66%, and 92.36% to 90.14%, 88.84%, and 87.46%, respectively",
        "p.7 (Section 3.4 Temperature and thermodynamic study)",
        "partial"
    ),
    15: (
        "As our findings show, with increasing water temperature from 25 °C to 50 °C, the elimination of Hg(II), Co(II), and Ni(II) are diminished from 94.36%, 93.66%, and 92.36% to 90.14%, 88.84%, and 87.46%, respectively",
        "p.7 (Section 3.4 Temperature and thermodynamic study)",
        "partial"
    ),
    16: (
        "As our findings show, with increasing water temperature from 25 °C to 50 °C, the elimination of Hg(II), Co(II), and Ni(II) are diminished from 94.36%, 93.66%, and 92.36% to 90.14%, 88.84%, and 87.46%, respectively",
        "p.7 (Section 3.4 Temperature and thermodynamic study)",
        "partial"
    ),

    # === Group 4: Shi Pb(II) (3 rows) ===
    17: (
        "The maximum Pb(II) adsorption capacity at 300 K, 308 K and 318 K calculated by Langmuir model could reach 196.67, 200.45 and 205.07 mg/g, respectively",
        "p.1 (Abstract) / p.4 (Section 3.3.3)",
        "partial"
    ),
    18: (
        "The maximum adsorption capacity (Qm) was 196.67, 200.45 and 205.07 mg/g at 300 K, 308 K and 318 K, respectively",
        "p.4 (Section 3.3.3) / Table 2 (p.7)",
        "partial"
    ),
    19: (
        "The maximum adsorption capacity (Qm) was 196.67, 200.45 and 205.07 mg/g at 300 K, 308 K and 318 K, respectively",
        "p.4 (Section 3.3.3) / Table 2 (p.7)",
        "partial"
    ),

    # === Group 2: Xiao COF (7 rows) ===
    20: (
        "According to the Langmuir fitting, the calculated capture capacities of COF@PDA for Fe2+, Co2+ and Ni2+ equal 204.9, 194.2, and 207.5 mg/g, respectively",
        "p.1 (Abstract) / p.8 (Section 3.2.3, Langmuir fitting)",
        "partial"
    ),
    21: (
        "According to the Langmuir fitting, the calculated capture capacities of COF@PDA for Fe2+, Co2+ and Ni2+ equal 204.9, 194.2, and 207.5 mg/g, respectively",
        "p.1 (Abstract) / p.8 (Section 3.2.3, Langmuir fitting)",
        "partial"
    ),
    22: (
        "According to the Langmuir fitting, the calculated capture capacities of COF@PDA for Fe2+, Co2+ and Ni2+ equal 204.9, 194.2, and 207.5 mg/g, respectively",
        "p.1 (Abstract) / p.8 (Section 3.2.3, Langmuir fitting)",
        "partial"
    ),
    23: (
        "The adsorption capacities of COF@PDA were still well-maintained with only a 2% decrease for Fe2+, a 2.9% decrease for Co2+ and a 2.7% decrease for Ni2+",
        "p.8 (Section 3.2.5 Desorption and reusability)",
        "partial"
    ),
    24: (
        "The maximum adsorption capacities of COF towards Fe2+, Co2+ and Ni2+ are only 55.4, 31.4 and 56.5 mg g−1, respectively",
        "p.7 (Section 3.2.3)",
        "partial"
    ),
    25: (
        "The maximum adsorption capacities of COF towards Fe2+, Co2+ and Ni2+ are only 55.4, 31.4 and 56.5 mg g−1, respectively",
        "p.7 (Section 3.2.3)",
        "partial"
    ),
    26: (
        "The maximum adsorption capacities of COF towards Fe2+, Co2+ and Ni2+ are only 55.4, 31.4 and 56.5 mg g−1, respectively",
        "p.7 (Section 3.2.3)",
        "partial"
    ),

    # === Zhang Gd(III) (1 row) ===
    27: (
        "At pH 7.0, the maximum adsorption capacity of aerogel for Gd(III) reached 150.86 mg g−1",
        "p.1 (Abstract) / p.6 / Table 5 (p.9)",
        "partial"
    ),

    # === Group 3: CN114570339A Uranium (7 rows) ===
    28: (
        "H-PDA-SO制备仅需130min，将其应用于水溶液中的U（VI）溶液吸附，40-50min内可达到平衡，室温下最大吸附容量96.5mg•g-1",
        "p.1 (摘要)",
        "partial"
    ),
    29: (
        "25℃室温条件下其最大吸附容量可达103mg g⁻¹",
        "p.4, 说明书第[0023]段（有益效果(2)）",
        "partial"
    ),
    30: (
        "其在288K时最大吸附容量为81.25mg g⁻¹，298K时最大吸附容量为96.5mg g⁻¹，308K时最大吸附容量为132.25mg g⁻¹",
        "p.7 (实施例10, 图6描述)",
        "partial"
    ),
    31: (
        "其在288K时最大吸附容量为81.25mg g⁻¹，298K时最大吸附容量为96.5mg g⁻¹，308K时最大吸附容量为132.25mg g⁻¹",
        "p.7 (实施例10, 图6描述)",
        "partial"
    ),
    32: (
        "[Figure description] 图4b: H-PDA-SO在不同pH下的吸附容量，pH 6.0时约38 mg/g",
        "p.10 (图4b描述, visual cache OCR)",
        "needs_review"
    ),
    33: (
        "[Figure description] 图4a: H-PDA在不同pH下的吸附容量，pH 6.0时约36 mg/g",
        "p.10 (图4a描述, visual cache OCR)",
        "needs_review"
    ),
    34: (
        "图表横坐标标注了金属离子元素符号：U, V, Fe, Co, Ni, Zn, Pb... U：约 8.2 mg·g⁻¹",
        "p.12 (图7描述, visual cache OCR, selectivity figure)",
        "needs_review"
    ),

    # === Godiya Cu (2 rows) ===
    35: (
        "MCC-PDA-PEI/CS-PDA-PEI hydrogel showed excellent Cu2+, Zn2+, and Ni2+ adsorbabilities of ~434.8, ~277.7, and ~261.8 mg/g, respectively",
        "p.1 (Abstract) / p.5 (Section 3.3)",
        "partial"
    ),
    36: (
        "The −NH2 bilayer functionalized MCC/CS hydrogels demonstrated significantly higher adsorbability (i.e., MCC10: 434.8, 277.7, and 261.8 mg/g for Cu2+, Zn2+, and Ni2+ cations, respectively) as compared to the unmodified MCC/CS hydrogel (158.7, 161.2, and 172.4, respectively)",
        "p.5 (Section 3.3)",
        "partial"
    ),

    # === Group 6: Yan MB/MG/CV (2 rows) ===
    37: (
        "Under optimal conditions, the maximum adsorption capacities of PDA/MGO/CA-CD towards MB, MG, and CV were 1372.32, 822.39, and 570.79 mg/g, respectively",
        "p.1 (Abstract) / p.11 (Section 3.3.2) / p.17 (Conclusions)",
        "partial"
    ),
    38: (
        "The maximum equilibrium adsorption capacities of PDA/MGO/CA-CD adsorbent for MB, MG, and CV were as high as 1372.32, 822.39, and 570.79 mg/g at 298 K, respectively",
        "p.11 (Section 3.3.2)",
        "partial"
    ),

    # === Group 7: Jin Carmine (1 row) ===
    39: (
        "PDA/DCS 呈现较密集的多孔结构。DCS 和PDA/DCS 对胭脂红的吸附过程均遵循准二级动力学模型和Langmuir 等温模型；PDA/DCS 的吸附速率及吸附量明显提升，当染料初始质量浓度为700 mg/L 时，PDA/DCS 最大单分子层吸附量可达到1194.4 mg/g",
        "p.1 (摘要) / p.7 (正文)",
        "partial"
    ),

    # === Xiang Ge(IV) (1 row) ===
    40: (
        "吸附等温线结果表明，Fe3O4@PDA-PEI对Ge（Ⅳ）的吸附过程符合Sips等温吸附模型；吸附动力学更符合准二级动力学模型，表面化学吸附是关键的限速步骤。Langmuir模型qm,cal = 0.349 mmol·g⁻¹",
        "p.1 (摘要) / p.8 (Table, Langmuir qm = 0.349 mmol/g)",
        "needs_review"
    ),

    # === Group 5: Yuan Cr/Cu/CR (3 rows) ===
    41: (
        "CNF-TA-PMMT-PEI has a honeycomb-like pore structure, high porosity (98.29 %), abundant functional groups, and showed rapid and excellent adsorption performance for Cr(VI), Cu(II), and Congo red (CR), with the Qm of 456.62, 289.86, and 3429.23 mg/g, respectively",
        "p.1 (Abstract) / p.10 (Section 3.4.3) / p.17 (Conclusions)",
        "partial"
    ),
    42: (
        "The maximum adsorption of Cr(VI), Cu(II), and CR by the CNF-TA-PMMT-PEI was calculated to be 456.62 mg/g, 289.86 mg/g and 3429.23 mg/g, respectively, according to the Langmuir model",
        "p.10 (Section 3.4.3 Comparison with relevant works)",
        "partial"
    ),
    43: (
        "The Qm capacities of the CNF-TA-PMMT-TA for Cr(VI), Cu(II) and CR were 456.62, 289.86 and 3429.23 mg/g, and the aerogel had excellent anti-interference performance. CAVEAT: CR 3429.23 mg/g is an extreme value — likely reflects multilayer/dye-aggregate adsorption rather than monolayer capacity",
        "p.17 (Conclusions)",
        "needs_review"
    ),
}


def main():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    perf_data = data["performance_data"]
    print(f"Total performance_data rows: {len(perf_data)}")

    updated = 0
    for idx, (quote, locator, status) in UPDATES.items():
        if idx < len(perf_data):
            row = perf_data[idx]
            row["verification_quote"] = quote
            row["source_locator"] = locator
            row["verification"] = status
            updated += 1
            print(f"  [{idx}] {row.get('parameter', '')[:50]} → {status}")
        else:
            print(f"  [WARN] Index {idx} out of range")

    # Write back
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nUpdated {updated} rows.")

    # Summary
    from collections import Counter
    statuses = Counter(row.get("verification", "") for row in perf_data)
    print(f"\nVerification status summary:")
    for status, count in statuses.most_common():
        print(f"  {status}: {count}")


if __name__ == "__main__":
    main()
