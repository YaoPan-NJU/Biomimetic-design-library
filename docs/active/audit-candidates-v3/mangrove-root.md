# Audit: mangrove-root

## Summary
- Total mechanisms: 1
- Total performance_data: 5
- Total design_translation: 1
- Total engineering_constraints: 1
- Total narrative entries: 2
- Issues found: 2

## Findings

### [F1] Verification_quote is title fragment, not text excerpt
- **Type**: label-contradiction
- **Severity**: low
- **Location**: mechanisms[0].verification_quote (line 165)
- **Evidence**: verification_quote = "mangrove constructed wetland for pollutant removal". This is a title/topic summary, not a direct text excerpt from the Liu2022 paper. The mechanism is marked verification = "verified" but the quote does not provide verbatim source text.
- **Cross-ref**: None specific
- **Recommended disposition**: Upgrade verification_quote to an actual text excerpt from Liu2022 with page/section locator

### [F2] Multiple performance_data rows have null values
- **Type**: label-contradiction
- **Severity**: low
- **Location**: performance_data[2] (value=null), performance_data[3] (value=null), performance_data[4] (value=null), performance_data[5] (value=null)
- **Evidence**: Four of 5 performance_data entries have null values. While these may represent qualitative findings (e.g., "critical concentration", "K. candel superiority"), null-value rows cannot contribute to quantitative ranking. performance_data[2] describes "25倍浓度处理下NO2--N去除率" but has no numeric value. performance_data[5] describes "红树林人工湿地氮磷去除临界浓度" with no value.
- **Cross-ref**: B05-MANG-001 (applied_boundary_2026_06_17): mangrove evidence is constructed-wetland/system removal percentage, not adsorbent qmax.
- **Recommended disposition**: Either populate with actual values from source PDF or mark as qualitative-only / exclude from ranking

## Clean areas
- mechanisms[0]: Legitimate Liu2022 source (verified, though quote quality is low)
- performance_data[0-1]: Legitimate Liu2022 sources with actual numeric values (62-99% NH4+-N, 80% PO4)
- narrative.entries[0-1]: Legitimate Wu2021 and Liu2022 sources
- engineering_constraints[0]: Legitimate Liu2022 source (NO3--N stability)
- design_translation: LLM-inference (correctly labeled)
- No refuted DOI contamination
- No wrong-source contamination
