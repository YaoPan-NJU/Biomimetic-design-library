# M9b Evidence Extraction: Superwetting / Oil-Water Separation Mechanisms

**Target Mechanism:** 超疏水材料构建基本原理 - Young方程/Wenzel模型/Cassie-Baxter模型
**Basis:** llm_inferred (all three prototypes)
**Extraction Date:** 2026-06-21

---

## 1. lotus-leaf

### Current State
- **verification:** unverified
- **ref_doi:** 10.16865/j.cnki.1000-7555.2020.0282
- **description:** 超疏水材料是指水的接触角超过150°，滞后角低于10°的表面材料

### Extracted Evidence

#### Evidence 1 (Best match)
- **source_doi:** 10.1021/acsami.0c19733
- **source_file:** 仿生文献库/论文/第2组-超疏水/2020-Zheng-self-cleaning-separation-wastewater-water-treatment-review 2.pdf
- **source_locator:** Page 3, Section "Wetting Theory"
- **verification_quote:** "The wetting behavior of a liquid droplet on a solid surface can be understood through the Young's model, Wenzel and Cassie model. Among them, the Young's model is an ideal model, deeming the contact angle (ICA) is confirmed by Young's equation... However, the Young's model fails to explain the wetting behavior of all surfaces for almost all solid surfaces are rough in reality. Subsequently, the modified Young's model was proposed by Wenzel... where θw is the contact angle (CA) of the liquid on a rough solid... In the Wenzel state, the liquid unreservedly occupies... Furthermore, the Cassie−Baxter model was proposed to explicate the wetting behavior on the surface with porous... obtained via the Cassie−Baxter equation."

#### Evidence 2
- **source_doi:** 10.1016/j.jmrt.2021.02.068
- **source_file:** 仿生文献库/论文/第2组-超疏水/2021-Usman-superhydrophobic-hydrophobic-oil-water-separation-review_visual_cache 2.json (corresponding PDF: 2021-Usman-superhydrophobic-hydrophobic-oil-water-separation-review.pdf)
- **source_locator:** Page 9, Section on wetting models
- **verification_quote:** "In 1805, Young [116] formulated an equation with which shape of a fluid droplet on a smooth solid substrate surface can be evaluated... γSV = γSL + γLV cos θY... For this, Wenzel formulated a relationship between contact angle and roughness. He modified the Young's equation thereby introducing a roughness factor, rs, which is the ratio of rough and smooth surfaces... Wenzel model was able to only discuss rough solid surface without addressing porous solid surfaces, for this, Cassie and Baxter extended the model in order to accommodate porous surfaces... cos θ' = f1 cos θY − f2... Existence of pores on a solid surface will at all times increase the contact angle. Hence, an apparent contact angle of 90° can be transformed to 150° by introducing pores on the same solid substrate surface."

---

## 2. superhydrophobic-artificial

### Current State
- **verification:** unverified
- **ref_doi:** 10.16865/j.cnki.1000-7555.2020.0282
- **description:** 超疏水材料是指水的接触角超过150°，滞后角低于10°的表面材料

### Extracted Evidence

#### Evidence 1 (Best match)
- **source_doi:** 10.1080/10643389.2021.1877032
- **source_file:** 仿生文献库/论文/第2组-超疏水/2021-Gontarek-castro-superhydrophobic-hydrophobic-membrane-review 2.pdf
- **source_locator:** Page 12, Section on wetting theory
- **verification_quote:** "The roughness enhances the contact angle of hydrophobic surfaces well beyond that possible to achieve by chemistry itself (McHale et al., 2004). This was well described by Wenzel equation (11) (Wenzel, 1936): cos θr = r cos θe where r is a roughness factor, θr is a contact angle on a rough surface, and θe is Young's equilibrium contact angle. According to the Wenzel's equation, the surface roughness amplifies the effect of the surface chemistry... Nevertheless, the Wenzel equation is limited to the homogeneous rough surface, and it was extended by Cassie and Baxter in 1944 (Cassie & Baxter, 1944). Cassie-Baxter equation applies for the porous membrane with a heterogeneous surface. In this case, the presence of the air in the pores of the material prevents the pores from being filled with liquid and liquid only bridges between the solid surface... cos θCB = f1 cos θe − (1 − f1)... According to Cassie-Baxter equation, θCB will increase with..."

#### Evidence 2
- **source_doi:** 10.1007/s42242-021-00133-8
- **source_file:** 仿生文献库/论文/第2组-超疏水/2021-Zeng-antifouling-porous-review 2.pdf
- **source_locator:** Pages 3–4, Section 1 "Wettability"
- **verification_quote:** "Wenzel's equation was originally designed to reveal the wetting mechanism of a liquid with a single uniform solid surface... the Wenzel equation is further modified... cos θ = f1 cos θ1 + f2 cos θ2... When the solid–liquid interface replaces the solid–air interface, the voids on the rough surface may not be completely filled with liquid... A solid–liquid–air composite interface is formed... the Cassie–Baxter equation can be expressed as [34]: where θ0 is the contact angle for a smooth surface of the solid material, r is the roughness factor, and fLA is the fractional flat geometric area of the liquid–air interfaces under the droplet. According to the above formula, even if a solid surface is hydrophilic, as the value of fLA gradually increases to a sufficiently large value, the surface can still be changed from hydrophilic to hydrophobic... In summary, Young's equation, Wenzel's equation, and the Cassie–Baxter model describe the static wettability of..."

---

## 3. water-strider-leg

### Current State
- **verification:** unverified
- **ref_doi:** 10.16865/j.cnki.1000-7555.2020.0282
- **description:** 超疏水材料是指水的接触角超过150°，滞后角低于10°的表面材料

### Extracted Evidence

#### Evidence 1 (Best match — Chinese source, aligning with prototype's Chinese DOI)
- **source_doi:** (Chinese journal, no standard DOI) — 闫德峰等, 表面技术, 2021, 50(5): 1-19
- **source_file:** 仿生文献库/论文/第2组-超疏水/2021-闫-超疏水-油水分离-综述 2.pdf
- **source_locator:** Pages 2–3, Sections 1.1–1.3 "经典润湿性理论"
- **verification_quote:** "1.1 Young 模型 — Young[5]认为液体在理想的光滑固体表面上时，其接触角只与固-气、固-液、液-气界面的表面张力有关（图3a），而理想固体表面的接触角称为本征接触角θY，本征接触角满足Young 方程... 1.2 Wenzel 模型 — 由于实际固体表面并非是理想的光滑表面，其表面通常具有微观粗糙结构（图3b）。因此Wenzel[6]对Young 模型进行修正并提出了Wenzel 模型，此时液滴接触角方程为：cos θW = r(γSG−γSL)/γLG = r cos θY... 式中：θW 为Wenzel 模型下的表观接触角；r 为粗糙度因子... 1.3 Cassie-Baxter 模型 — Cassie 和Baxter[7]发现天然超疏水表面具有微观粗糙结构，但液滴并不是完全充满表面的粗糙结构，因此提出了一种新的润湿模型，即Cassie-Baxter 模型（图3c）。该模型中，液滴底部并未与固体的粗糙结构底部接触，而是被粗糙结构内部的空气垫隔开，液滴底部同时与固体、气体接触，形成由固-液-气三相组成的复合接触面。在Cassie-Baxter 润湿模型下，液滴的接触角方程如下：cos θC-B = f1 cos θY − f2..."

#### Evidence 2
- **source_doi:** 10.16490/j.cnki.issn.1001-3660.2023.02.015
- **source_file:** 仿生文献库/论文/第2组-超疏水/2023-景-超疏水-油水分离-膜-综述 2.pdf
- **source_locator:** Pages 1–3, Section 1 "基础理论"
- **verification_quote:** "受到自然界中动植物表面超疏水/超亲水特性的启发，仿生超浸润膜材料作为一种新兴的油水分离材料引起了科研人员的广泛关注。首先通过对影响膜材料表面润湿性的基础模型进行分析，包括Young 方程、Wenzel 模型和Cassie 模型，总结了制备超浸润膜材料需要调控的2 个关键因素——表面张力和纳微多级结构... 1805 年Thomas Young 首次提出了适用于均匀、光滑的不变形理想固体表面的三相界面张力与接触角θ 之间的关系... Wenzel 模型在Young's 模型的基础上引入粗糙度系数进行修正... 当疏液的固体表面具有一定的粗糙结构时，液体与表面接触会在凹槽结构中截留部分气体，形成气液固三相复合界面（图1c）。针对这一情况，Cassie 和Baxter 引入了固液界面分数f1 和气液界面分数f2..."

#### Evidence 3 (English, broad superhydrophobic review)
- **source_doi:** 10.16865/j.cnki.1000-7555.2020.0282
- **source_file:** 仿生文献库/论文/第2组-超疏水/2022-Finally-superhydrophobic-hydrophobic-porous-review 2.pdf
- **source_locator:** Page 3, Section 2.1
- **verification_quote:** "Most surfaces are not smooth and have roughness. The rough surface microstructure has an essential effect on the wettability of the solid surface. Wenzel pointed out that the rough structure can significantly increase the contact area between liquid and the solid surface when the solid surface is wetted by the liquid... He improved Young's formula by introducing the roughness factor (R, the ratio of total surface area to projected area). In Wenzel state, the CA (θ*) of droplets on the rough surface can be described as: cos θ* = R(γSA − γSL)/γLA = R cos θ... Because the actual surface area of a rough solid surface is greater than its apparent surface area (R > 1), it can be concluded from this formula that rough microstructure can amplify the intrinsic surface wettability of the solid substrate... Cassie et al. proposed an alternative model that reflects the contact state between a liquid and a rough surface when the liquid cannot penetrate the concave cavity of the rough microstructure... The apparent CA (θ*) of the liquid droplet on the composite interface satisfies the following formula: cos θ* = f cos θ + f − 1... Since the trapped air cushion significantly reduces the solid/gas contact area and disconnects the contact line, the surface in the Cassie state has very low adhesion to the liquid droplet."

---

## Summary of Evidence Sources

| # | DOI | PDF File | Language | Page(s) | Evidence Quality |
|---|-----|----------|----------|---------|-----------------|
| 1 | 10.1021/acsami.0c19733 | 2020-Zheng-self-cleaning-separation...review.pdf | EN | 3 | Strong — full Young/Wenzel/Cassie-Baxter with equations |
| 2 | 10.1016/j.jmrt.2021.02.068 | 2021-Usman-superhydrophobic...review.pdf | EN | 9 | Strong — full equations and definitions |
| 3 | 10.1080/10643389.2021.1877032 | 2021-Gontarek-castro...review.pdf | EN | 12 | Strong — Wenzel and Cassie-Baxter equations with membrane context |
| 4 | 10.1007/s42242-021-00133-8 | 2021-Zeng-antifouling-porous-review.pdf | EN | 3–4 | Strong — full wetting theory with figures |
| 5 | (Chinese journal) | 2021-闫-超疏水-油水分离-综述.pdf | ZH | 2–3 | Strong — complete Chinese-language treatment |
| 6 | 10.16490/j.cnki.issn.1001-3660.2023.02.015 | 2023-景-超疏水-油水分离-膜-综述.pdf | ZH | 1–3 | Strong — complete Chinese-language treatment |
| 7 | (Chinese journal) | 2022-Finally-superhydrophobic...review.pdf | EN | 3 | Strong — clear Wenzel/Cassie-Baxter with formulas |

## Notes

- The original mechanism entry references DOI 10.16865/j.cnki.1000-7555.2020.0282, which is a Chinese journal article (高分子材料科学与工程). No corresponding PDF or visual cache was found in the literature library for this specific DOI. Evidence was therefore sourced from other available PDFs in 仿生文献库/论文/第2组-超疏水/ that contain equivalent content.
- All three prototypes (lotus-leaf, superhydrophobic-artificial, water-strider-leg) share the same mechanism name and description. The same body of literature supports all three.
- The Young equation (γSV = γSL + γLV cos θY), Wenzel model (cos θW = r cos θY), and Cassie-Baxter model (cos θCB = f1 cos θY − f2) are the three foundational wetting models. The key insight is that surface roughness (r > 1) amplifies intrinsic wettability (Wenzel), while trapped air cushions in porous/rough structures create composite interfaces with very low adhesion (Cassie-Baxter). Superhydrophobicity (CA > 150°) requires both micro/nano hierarchical roughness and low surface energy chemistry.
