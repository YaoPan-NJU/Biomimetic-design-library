# Task 22 — OCR Patent Processing Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Method

Used visual_cache.json text extraction (pre-OCR by mimo-v2.5 at extraction time) instead of live multimodal OCR.

## CN113244898A (PDA/KA/Fe₃O₄ Pb adsorption)

**Key findings from visual cache:**
- Pb²⁺ removal rate: 96.31% at pH 6, 4 mg/L initial concentration, 5h adsorption
- Conditions: 5mg adsorbent, 25°C, 300rpm, 4h
- Adsorption mechanism: electrostatic attraction + N-containing functional group coordination
- Isotherm: Freundlich (R²=0.95) better than Langmuir (R²=0.86)
- Kinetics: pseudo-second-order (R²=0.9996)

**Quotes added to:** perf[17], perf[19]

## CN114570339A (H-PDA-SO U(VI) adsorption)

**Key findings from visual cache:**
- H-PDA-SO best pH: 6.0
- At pH 6: adsorption capacity ~36 mg/g
- At pH 3: adsorption capacity ~38 mg/g (human-confirmed)
- Selectivity: U ~8.2 mg/g from Figure 7 (multi-metal competition)
- Equilibrium: 40 min (10 mL), 50 min (50 mL)

**Quotes added to:** perf[32]

## CN113275374A (fish-scale MICP)

**Status:** Not processed — this patent was already marked for removal (F03-IOB-002, F11-FISH-004). No OCR needed.

## Pending Full OCR

The visual_cache text extraction is partial. Full OCR with mimo-v2.5 multimodal model is still recommended for:
- CN113244898A: complete Pb adsorption capacity table
- CN114570339A: Figure 5 adsorption isotherm data, Figure 6 concentration curve
