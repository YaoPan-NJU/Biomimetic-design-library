#!/bin/bash
# Extract only the 26 missing papers (normalized stem matching)
# This script handles the " 2" suffix mismatch between PDFs and JSONs

set -u

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

LITEXTRACT_DIR="$REPO_DIR/tools/litextract"
PROMPT_FILE="$LITEXTRACT_DIR/prompts/biomimetic_extraction_prompt_v2.md"
OUT_DIR="$LITEXTRACT_DIR/outputs/extractions"
PDF_DIR="$REPO_DIR/仿生文献库/论文"
PYTHON_BIN="${PYTHON_BIN:-python3}"

# Load env
if [[ -f "$LITEXTRACT_DIR/.env" ]]; then
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line%$'\r'}"
    [[ -z "$line" || "$line" == \#* || "$line" != *=* ]] && continue
    key="${line%%=*}"; value="${line#*=}"
    [[ "$key" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]] || continue
    export "$key=$value"
  done < "$LITEXTRACT_DIR/.env"
fi
export OPENCLAW_CONFIG_PATH="$LITEXTRACT_DIR/openclaw.json"

# Find missing papers (normalized stem matching)
echo "=== Finding missing papers ==="
MISSING_LIST=$("$PYTHON_BIN" -c "
import os, json

pdf_dir = '$PDF_DIR'
json_dir = '$OUT_DIR/论文/json'

json_stems = set()
for fn in os.listdir(json_dir):
    if fn.endswith('.json'):
        stem = fn[:-5]
        if stem.endswith(' 2') or stem.endswith(' 3'):
            stem = stem[:-2]
        json_stems.add(stem)

missing = []
for dp, _, fns in os.walk(pdf_dir):
    for fn in fns:
        if fn.lower().endswith('.pdf'):
            stem = fn[:-4]
            normalized = stem
            if normalized.endswith(' 2') or normalized.endswith(' 3'):
                normalized = normalized[:-2]
            if normalized not in json_stems:
                missing.append(os.path.join(dp, fn))

for p in sorted(set(missing)):
    print(p)
")

MISSING_COUNT=$(echo "$MISSING_LIST" | grep -c . || echo 0)
echo "Found $MISSING_COUNT missing papers"

if [[ "$MISSING_COUNT" -eq 0 ]]; then
    echo "No missing papers. All extracted!"
    exit 0
fi

# Extract each missing paper
echo ""
echo "=== Extracting missing papers ==="
SUCCESS=0
FAIL=0

while IFS= read -r pdf; do
    [[ -z "$pdf" ]] && continue
    basename_pdf="$(basename "$pdf")"
    stem="${basename_pdf%.[Pp][Dd][Ff]}"

    # Determine output path (normalized stem)
    normalized="$stem"
    if [[ "$normalized" == *" 2" ]] || [[ "$normalized" == *" 3" ]]; then
        normalized="${normalized% ??}"
    fi
    json_path="$OUT_DIR/论文/json/${normalized}.json"

    echo ""
    echo "--- Extracting: $basename_pdf ---"
    echo "  Output: ${normalized}.json"

    # Preprocess visual cache
    visual_cache="${pdf%.[Pp][Dd][Ff]}_visual_cache.json"
    if [[ ! -f "$visual_cache" ]]; then
        echo "  Preprocessing visual cache..."
        "$PYTHON_BIN" "$LITEXTRACT_DIR/scripts/preprocess.py" "$pdf" --max-workers 4 -o "$visual_cache" 2>&1 | tail -3
    fi

    # Build multimodal context
    tmp_prompt="/tmp/openclaw/extract_prompt_$$.txt"
    tmp_raw="/tmp/openclaw/extract_raw_$$.txt"

    {
        echo "以下内容来自同一篇 PDF 的多模态预处理结果：文本页来自本地 PDF 文本层，数据页/图表页来自视觉模型读取后的 Markdown 缓存。"
        echo "请不要重新调用 PDF 工具；请依据下面的多模态合并上下文提取结构化 JSON。"
        echo "$pdf"
        echo
        echo "----- MULTIMODAL_CONTEXT_BEGIN -----"
        # Extract text from PDF
        "$PYTHON_BIN" -c "
import fitz
doc = fitz.open('$pdf')
for i, page in enumerate(doc):
    text = page.get_text()
    if text.strip():
        print(f'[Page {i+1} - text]')
        print(text[:5000])
" 2>/dev/null
        echo "----- MULTIMODAL_CONTEXT_END -----"
        echo
        echo "【重要约束】不要使用任何工具，不要写文件，不要创建文件。你必须直接在回复中输出完整 JSON 字符串。回复以 { 开头，以 } 结尾。"
        echo
        cat "$PROMPT_FILE"
        echo
        echo "【再次提醒】不要使用工具写文件。直接输出 JSON，不要用代码块包裹。"
    } > "$tmp_prompt"

    # Run extraction
    echo "  Running LLM extraction..."
    start_ts=$(date +%s)
    if (cd "$LITEXTRACT_DIR" && openclaw agent --local --agent lit-extract \
        --session-id "missing-$(date +%s)-$$" \
        --model "bailian/qwen3.6-plus" \
        --timeout 1800 \
        --message "$(cat "$tmp_prompt")" \
        > "$tmp_raw" 2>/dev/null); then

        # Extract JSON from raw output
        "$PYTHON_BIN" -c "
import json, re, sys

raw = open('$tmp_raw').read()
# Try to find JSON object
start = raw.find('{')
end = raw.rfind('}')
if start >= 0 and end > start:
    json_str = raw[start:end+1]
    try:
        d = json.loads(json_str)
        json.dump(d, open('$json_path', 'w'), ensure_ascii=False, indent=2)
        print('  OK: JSON extracted')
        sys.exit(0)
    except:
        pass
print('  FAIL: no valid JSON found')
sys.exit(1)
" 2>/dev/null

        if [[ $? -eq 0 ]]; then
            end_ts=$(date +%s)
            elapsed=$((end_ts - start_ts))
            echo "  Completed in ${elapsed}s"
            SUCCESS=$((SUCCESS + 1))
        else
            echo "  FAIL: JSON extraction failed"
            FAIL=$((FAIL + 1))
        fi
    else
        echo "  FAIL: openclaw agent failed"
        FAIL=$((FAIL + 1))
    fi

    rm -f "$tmp_prompt" "$tmp_raw"

done <<< "$MISSING_LIST"

echo ""
echo "=== Summary ==="
echo "Success: $SUCCESS"
echo "Failed: $FAIL"
echo "Total JSONs: $(ls "$OUT_DIR/论文/json/"*.json | wc -l | tr -d ' ')"
