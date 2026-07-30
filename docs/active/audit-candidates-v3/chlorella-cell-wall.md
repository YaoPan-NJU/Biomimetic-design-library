# Audit: chlorella-cell-wall

## Summary
- Total mechanisms: 13
- Total performance_data: 22
- Total design_translation: 1
- Issues found: 2

## Findings

### [F1] Wrong-source performance data from wastewater technology review
- **Type**: wrong-source
- **Severity**: high
- **Location**: performance_data[13-16] (indices 13 through 16)
- **Evidence**: performance_data[13] (chemical precipitation phosphate removal), [14] (algae nitrate/phosphate removal), [15] (nZVI nitrate removal), [16] (magnetic graphene nitrate removal) all cite DOI 10.1007/s10311-021-01239-2 ("Technology for adsorbent wastewater removal review"). These describe chemical/nanotechnology wastewater treatment methods (CaO, nZVI, magnetic graphene, silica nanoparticles) -- not Chlorella cell-wall biosorption.
- **Cross-ref**: Refuted-log lines 171-174 (wrong_source, already refuted for chlorella-cell-wall); Decision-queue B03-CHL-002 (guard_rule, approved_unapplied)
- **Recommended disposition**: Remove performance_data[13-16]. Guard rule B03-CHL-002 already applies but data appears not yet removed from JSON.

### [F2] mechanism[0] uses Pb2+ source for dye-removal claim
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[0] (index 0)
- **Evidence**: mechanism[0] describes "three mechanisms of dye removal by algae" but cites Cheng2021 (DOI 10.19824/j.cnki.cn32-1786/x.2021.0078), which is about Pb2+ biosorption by freshwater microalgae, not dye removal. The causal_chain.locator references "程2021 p.1 / Abstract" and verification_quote mentions "4种淡水微藻对Pb2+的吸附特性" -- confirming the source is about Pb2+, not dyes.
- **Cross-ref**: Decision-queue B03-CHL-001 (hard_do_not, approved_unapplied): "Cheng2021 must not be used as synthetic dye-removal mechanism evidence."
- **Recommended disposition**: Remove mechanism[0] or change its source to a legitimate dye-removal-by-algae reference. B03-CHL-001 is approved but unapplied.

## Clean areas
- performance_data[0-12]: Legitimate algal biochar and biosorption data from Ayele2021, Kartik2021, Singh2021, Peng2022, Touliabah2022, Han2022 with proper verification status and quotes.
- mechanisms[1-12]: Legitimate Chlorella/algal mechanisms (pH effect, electrostatic biosorption, biopolymer composites, magnetic biochar, Chlorella-biochar immobilization, metal removal mechanisms, Pb two-stage adsorption, alginate immobilization, organic pollutant removal, cell-wall functional groups, biosurfactants, dye removal pathways).
- design_translation: Source tier is llm_inference (acceptable). Content about algal cell-wall functional groups aligns with Chlorella biology.
