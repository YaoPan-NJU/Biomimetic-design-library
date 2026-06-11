#!/usr/bin/env bash
# End-to-end biomimetic extraction pipeline.
#
# Stages:
#   0. PDF preprocessing (reuse preprocess.py)
#   1. OpenClaw batch extraction (reuse multi_worker_extract.sh)
#   2. Prototype mapping & aggregation (map_to_prototypes.py)
#   3. Library file generation (generate_prototype_md.py + update_feature_mapping.py)
#   4. Quality report
#
# Usage:
#   ./scripts/biomimetic_pipeline.sh --pdf-dir /path/to/pdfs --stage 0-4
#   ./scripts/biomimetic_pipeline.sh --pdf-dir /path/to/pdfs --stage 2-4  # skip extraction

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXTRACTION_DIR="$(cd "${SCRIPTS}/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

BIOMIMETIC_LIB="${BIOMIMETIC_LIB:-$REPO_DIR}"
OUTPUT_DIR="$EXTRACTION_DIR/outputs"
EXTRACTIONS_DIR="$OUTPUT_DIR/extractions"
AGGREGATED_DIR="$OUTPUT_DIR/aggregated"

# -- Args -----------------------------------------------------------------
PDF_DIR=""
STAGE_START=0
STAGE_END=4
WORKERS=3

while [[ $# -gt 0 ]]; do
  case "$1" in
    --pdf-dir)    PDF_DIR="$2"; shift 2 ;;
    --stage)
      IFS='-' read -r STAGE_START STAGE_END <<< "$2"
      shift 2 ;;
    --workers)    WORKERS="$2"; shift 2 ;;
    --output-dir) OUTPUT_DIR="$2"; shift 2 ;;
    --biomimetic-lib) BIOMIMETIC_LIB="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

if [[ -z "$PDF_DIR" ]]; then
  echo "Usage: $0 --pdf-dir /path/to/pdfs [--stage 0-4] [--workers 3]"
  exit 1
fi

echo "=== Biomimetic Extraction Pipeline ==="
echo "  PDF dir:     $PDF_DIR"
echo "  Output dir:  $OUTPUT_DIR"
echo "  Biomim lib:  $BIOMIMETIC_LIB"
echo "  Stages:      $STAGE_START - $STAGE_END"
echo "  Workers:     $WORKERS"
echo ""

mkdir -p "$OUTPUT_DIR" "$EXTRACTIONS_DIR" "$AGGREGATED_DIR"

# -- Stage 0: Preprocessing -----------------------------------------------
if [[ "$STAGE_START" -le 0 ]]; then
  echo "--- Stage 0: PDF Preprocessing ---"
  "$PYTHON_BIN" "$SCRIPTS/preprocess.py" \
    --pdf-dir "$PDF_DIR" \
    --output-dir "$OUTPUT_DIR/preprocessed" \
    2>&1 || echo "[WARN] Preprocessing had errors (continuing)"
  echo "  Done."
fi

# -- Stage 1: OpenClaw Extraction -----------------------------------------
if [[ "$STAGE_START" -le 1 && "$STAGE_END" -ge 1 ]]; then
  echo "--- Stage 1: OpenClaw Batch Extraction ---"
  MULTI_EXTRACT_RUN_DIR="/tmp/openclaw/biomimetic_runs/$(date +%Y%m%d%H%M%S)" \
  MULTIMODAL=1 \
  WORKERS="$WORKERS" \
  bash "$SCRIPTS/multi_worker_extract.sh" \
    "$PDF_DIR" \
    "$EXTRACTIONS_DIR" \
    "$EXTRACTION_DIR/prompts/biomimetic_extraction_prompt.md" \
    2>&1 || echo "[WARN] Extraction had errors (continuing)"
  echo "  Done."
fi

# -- Stage 2: Prototype Mapping & Aggregation -----------------------------
if [[ "$STAGE_START" -le 2 && "$STAGE_END" -ge 2 ]]; then
  echo "--- Stage 2: Prototype Mapping & Aggregation ---"
  "$PYTHON_BIN" "$SCRIPTS/map_to_prototypes.py" \
    --input-dir "$EXTRACTIONS_DIR" \
    --output-dir "$AGGREGATED_DIR" \
    --vocab "$EXTRACTION_DIR/config/vocabulary_mapping.json" \
    --routing "$EXTRACTION_DIR/config/prototype_routing.json" \
    2>&1
  echo "  Done."
fi

# -- Stage 3: Library File Generation -------------------------------------
if [[ "$STAGE_START" -le 3 && "$STAGE_END" -ge 3 ]]; then
  echo "--- Stage 3: Library File Generation ---"

  echo "  3a. Generating prototype.md files..."
  "$PYTHON_BIN" "$SCRIPTS/generate_prototype_md.py" \
    --input-dir "$AGGREGATED_DIR" \
    --biomimetic-lib "$BIOMIMETIC_LIB" \
    2>&1

  echo "  3b. Updating feature-mapping.json..."
  "$PYTHON_BIN" "$SCRIPTS/update_feature_mapping.py" \
    --input-dir "$AGGREGATED_DIR" \
    --biomimetic-lib "$BIOMIMETIC_LIB" \
    2>&1

  echo "  Done."
fi

# -- Stage 4: Quality Report ----------------------------------------------
if [[ "$STAGE_END" -ge 4 ]]; then
  echo "--- Stage 4: Quality Report ---"

  TOTAL_PAPERS=$(find "$EXTRACTIONS_DIR" -name "*.json" 2>/dev/null | wc -l | tr -d ' ')
  TOTAL_PROTOS=$(ls "$AGGREGATED_DIR"/*.json 2>/dev/null | wc -l | tr -d ' ')
  TOTAL_PROTO_MD=$(find "$BIOMIMETIC_LIB/prototypes" -name "prototype.md" 2>/dev/null | wc -l | tr -d ' ')

  PERF_COUNT=0
  NARRATIVE_COUNT=0
  for f in "$AGGREGATED_DIR"/*.json; do
    [[ -f "$f" ]] || continue
    PC=$("$PYTHON_BIN" -c "import json; d=json.load(open('$f')); print(len(d.get('performance_data',[])))" 2>/dev/null || echo 0)
    PERF_COUNT=$((PERF_COUNT + PC))
    NC=$("$PYTHON_BIN" -c "import json; d=json.load(open('$f')); print(len(d.get('biomimetic_design_chains',[])))" 2>/dev/null || echo 0)
    NARRATIVE_COUNT=$((NARRATIVE_COUNT + NC))
  done

  REPORT="$OUTPUT_DIR/quality-report-$(date +%Y-%m-%d).md"
  cat > "$REPORT" << EOF
# Biomimetic Extraction Quality Report

Date: $(date +%Y-%m-%d %H:%M:%S)

## Summary

| Metric | Count |
|--------|-------|
| Papers processed | $TOTAL_PAPERS |
| Prototypes with data | $TOTAL_PROTOS |
| prototype.md files in library | $TOTAL_PROTO_MD |
| Performance data records | $PERF_COUNT |
| Biomimetic design chains | $NARRATIVE_COUNT |

## Coverage

Prototypes with data: $(ls "$AGGREGATED_DIR"/*.json 2>/dev/null | xargs -I{} basename {} .json | tr '\n' ', ')

## Next Steps

- Review prototype.md files for quality
- Check feature-mapping.json weight updates
- Supplement literature for zero-coverage prototypes
EOF

  echo "  Report saved: $REPORT"
fi

echo ""
echo "=== Pipeline Complete ==="
