# M12-C: Chitosan Prototype Mechanism Evidence Validation Report

**Date:** 2026-06-22
**Source:** prototypes_db/chitosan.json (110 mechanisms)
**Validated:** 10 top-priority mechanisms

## Summary

| Verdict | Count |
|---------|-------|
| VALIDATED | 3 |
| PARTIAL | 3 |
| INVALID | 2 |
| MISSING_PDF | 2 |

## Critical Issues

1. **Mislabeled PDFs**: 2019-张-壳聚糖-吸附.pdf contains Upadhyay2021 (not Zhang2019)
2. **DOI mismatches**: Mechanism 1 cites DOI 10.1016/j.carbpol.2020.117000 but source_file is Lei2021 (DOI 10.1016/j.polymer.2020.123316)
3. **Missing PDFs**: DOIs 10.1016/j.molliq.2020.114523, 10.1016/j.scitotenv.2021.150606, 10.1016/j.chemosphere.2021.130927, 10.1016/j.jece.2022.108048 not in library
4. **Unsupported data**: pHpzc values (5.74, 4.85) attributed to Upadhyay2021 which doesn't contain them

## Validation Table

| Index | Mechanism | Verdict | Issue |
|-------|-----------|---------|-------|
| 1 | Metal ion complexation | PARTIAL | DOI mismatch |
| 17 | pH N-pollutants | PARTIAL | DOI mismatch |
| 0 | Inner-sphere | PARTIAL | PDF mislabeled |
| 2 | pHpzc effect | INVALID | Values not in cited source |
| 3 | Surface precipitation | VALIDATED | |
| 7 | Comprehensive mechanism | MISSING_PDF | |
| 13 | Arsenic adsorption | VALIDATED | |
| 24 | Three main mechanisms | MISSING_PDF | |
| 29 | Heavy metal mechanism | MISSING_PDF | |
| 59 | Complexation/chelation | PARTIAL | |

## Recommendations

1. Downgrade mechanism 2 (pHpzc) from needs_review to knowledge_gap (unsupported data)
2. Correct DOI mismatches for mechanisms 1 and 17
3. Mark 4 MISSING_PDF mechanisms with missing_pdf evidence_label
