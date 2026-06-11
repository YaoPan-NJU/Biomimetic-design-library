# extraction/writer.py
"""Write extraction results to prototype.md and feature-mapping.json."""

import json
import re
from pathlib import Path
from datetime import date

from config import PROJECT_DIR


def generate_prototype_md(
    prototype_id: str,
    performance: dict,
    narrative: dict,
    applicability: dict,
    coarse_coverage: dict = None,
    routing_info: dict = None,
) -> str:
    """Generate a prototype.md file from extraction results.

    Args:
        prototype_id: Canonical prototype identifier.
        performance: Merged performance data from extract_performance().
        narrative: Biomimetic narrative sections from extract_narrative().
        applicability: Applicability data (pH, temp, salinity).
        coarse_coverage: coverage dict from Phase 1 coarse profile
                         (pollutants, mechanisms, materials).
        routing_info: Prototype metadata from prototype_routing.json
                      (category, biomimetic_dimension).
    """
    coarse_coverage = coarse_coverage or {}
    routing_info = routing_info or {}

    # --- Pollutants: merge coarse coverage + LLM results + performance data ---
    pollutants = list(coarse_coverage.get("pollutants", []))
    for p in performance.get("target_pollutants", []):
        if p not in pollutants:
            pollutants.append(p)
    # Also check qmax.pollutant field
    qmax_data = performance.get("qmax")
    if isinstance(qmax_data, dict) and qmax_data.get("pollutant"):
        pol = qmax_data["pollutant"]
        if pol not in pollutants:
            pollutants.append(pol)

    # --- Features: material characterization (NOT mechanisms) ---
    mat_char = performance.get("material_characterization", {})
    features = list(mat_char.get("functional_groups", []))
    morphology = mat_char.get("morphology", "")
    if morphology and morphology not in features:
        features.append(morphology)
    surface_area = mat_char.get("surface_area")
    pore_size = mat_char.get("pore_size")
    if surface_area:
        features.append(f"surface area: {surface_area}")
    if pore_size:
        features.append(f"pore size: {pore_size}")

    # --- Evidence level: from LLM or calculate from source count ---
    evidence_level = performance.get("evidence_level")
    if not evidence_level or evidence_level not in ("high", "medium", "low"):
        n_sources = performance.get("_source_count", 0)
        if n_sources >= 5:
            evidence_level = "high"
        elif n_sources >= 2:
            evidence_level = "medium"
        else:
            evidence_level = "low"

    # --- Routing metadata ---
    category = routing_info.get("category", "未分类")
    biomimetic_dimension = routing_info.get("biomimetic_dimension", "未分类")

    # --- Prototype name: prefer routing config, fallback to ID ---
    proto_name = routing_info.get("_display_name") or _id_to_name(prototype_id)

    fm_fields = {
        "id": prototype_id,
        "name": proto_name,
        "category": category,
        "biomimetic_dimension": biomimetic_dimension,
        "features": features,
        "pollutants": pollutants,
        "adsorption_mechanisms": performance.get("mechanisms_identified", []),
        "qmax_range": _extract_numeric(performance.get("qmax")),
        "removal_rate": _extract_numeric(performance.get("removal_rate")),
        "applicability": {
            "ph": applicability.get("ph_range"),
            "temperature": applicability.get("temperature_range"),
            "salinity": applicability.get("salinity_tolerance"),
        },
        "evidence_level": evidence_level,
        "last_updated": str(date.today()),
    }

    # --- YAML front matter ---
    yaml_lines = ["---"]
    for key, value in fm_fields.items():
        if isinstance(value, dict):
            yaml_lines.append(f"{key}:")
            for k, v in value.items():
                yaml_lines.append(
                    f"  {k}: {json.dumps(v, ensure_ascii=False) if v is not None else 'null'}"
                )
        elif isinstance(value, list):
            yaml_lines.append(f"{key}:")
            for item in value:
                yaml_lines.append(f"  - {item}")
        else:
            yaml_lines.append(
                f"{key}: {json.dumps(value, ensure_ascii=False) if value is not None else 'null'}"
            )
    yaml_lines.append("---")

    # --- Performance summary for body text (unit-safe) ---
    qmax_val = _get_val(performance, "qmax")
    qmax_text = _strip_known_units(qmax_val)
    removal_val = _get_val(performance, "removal_rate")
    removal_text = _strip_known_units(removal_val)

    # --- Mechanism detail section ---
    mechanisms = performance.get("mechanisms_identified", ["[待补充]"])
    mech_lines = []
    for m in mechanisms:
        mech_lines.append(f"\n### {m}\n")
        mech_lines.append("[待补充详细机制描述]")

    # --- Structural features table ---
    struct_lines = _build_structural_table(mat_char)

    # --- Pollutant performance table ---
    pollutant_table = _build_pollutant_table(performance, coarse_coverage)

    body_lines = [
        f"\n# {proto_name}\n",
        f"**Category**: {category} | **Biomimetic Dimension**: {biomimetic_dimension}\n",
        "## 1. Biological Prototype Introduction\n",
        narrative.get("problem_definition", {}).get(
            "nature_challenge", "[待补充：生物原型介绍]"
        ),
        "\n## 2. Adsorption Mechanism Details\n",
        *mech_lines,
        "\n## 3. Structural Features\n",
        *struct_lines,
        "\n## 4. Reported Performance Data\n",
        *pollutant_table,
        f"\nqmax: {qmax_text} mg/g",
        f"Removal rate: {removal_text}%",
        f"Evidence level: {evidence_level}",
        "\n## 5. Biomimetic Design Narrative\n",
        "\n### 5.1 Problem Definition\n",
        narrative.get("problem_definition", {}).get(
            "water_treatment_mapping", "[待补充]"
        ),
        "\n### 5.2 Biological Solution\n",
        narrative.get("biological_solution", {}).get(
            "evolutionary_strategy", "[待补充]"
        ),
        "\n### 5.3 Key Feature Extraction\n",
        "Must-keep: "
        + json.dumps(
            narrative.get("key_feature_extraction", {}).get(
                "must_keep_features", []
            ),
            ensure_ascii=False,
        ),
        "Adjustable: "
        + json.dumps(
            narrative.get("key_feature_extraction", {}).get(
                "adjustable_features", []
            ),
            ensure_ascii=False,
        ),
        "\n### 5.4 Design Mapping\n",
        narrative.get("design_mapping", {}).get("bio_to_material", "[待补充]"),
        "\n### 5.5 Explainability Anchors\n",
        narrative.get("explainability_anchors", {}).get(
            "one_line_story", "[待补充]"
        ),
        "\n## 6. Applicable Scenarios\n\n[待补充]",
        "\n## 7. Related Prototypes\n\n[待补充]",
        "\n## 8. References\n\n[待补充]",
    ]

    return "\n".join(yaml_lines) + "\n".join(body_lines)


# ──────────────────────────── helpers ────────────────────────────


def _id_to_name(prototype_id: str) -> str:
    """Convert prototype ID to a display-friendly name.

    Preserves common acronyms (MOF, SLIPS, PDA, etc.) instead of
    mangling them with naive .title().
    """
    ACRONYMS = {
        "mof": "MOF",
        "slips": "SLIPS",
        "pda": "PDA",
        "dna": "DNA",
        "srb": "SRB",
        "hap": "HAP",
    }
    words = prototype_id.replace("-", " ").split()
    result = []
    for w in words:
        if w.lower() in ACRONYMS:
            result.append(ACRONYMS[w.lower()])
        else:
            result.append(w.capitalize())
    return " ".join(result)


def _get_val(data: dict, key: str) -> str:
    """Extract a displayable value from a dict, handling nested dicts."""
    val = data.get(key)
    if isinstance(val, dict):
        return str(val.get("value", "[待补充]"))
    return str(val) if val is not None else "[待补充]"


def _strip_known_units(val: str) -> str:
    """Remove trailing units like 'mg/g', '%' so the template can add them cleanly."""
    if not val:
        return "[待补充]"
    val = str(val).strip()
    val = re.sub(r"\s*mg\s*(?:\w+\s*)?[/／]\s*g\s*$", "", val, flags=re.IGNORECASE).strip()
    val = re.sub(r"\s*%\s*$", "", val).strip()
    return val if val else "[待补充]"


def _extract_numeric(data) -> str:
    """Safely extract a numeric value from dict or scalar, stripping units."""
    if isinstance(data, dict):
        raw = data.get("value", "")
    else:
        raw = data
    return _strip_known_units(str(raw)) if raw is not None else None


def _build_structural_table(mat_char: dict) -> list[str]:
    """Build a markdown table of structural characterisation data."""
    rows = []
    surface_area = mat_char.get("surface_area")
    pore_size = mat_char.get("pore_size")
    morphology = mat_char.get("morphology")
    functional_groups = mat_char.get("functional_groups", [])

    rows.append("| Property | Value |")
    rows.append("|----------|-------|")
    rows.append(f"| Surface Area | {surface_area or '[待补充]'} |")
    rows.append(f"| Pore Size | {pore_size or '[待补充]'} |")
    rows.append(f"| Morphology | {morphology or '[待补充]'} |")
    rows.append(
        f"| Functional Groups | {', '.join(functional_groups) if functional_groups else '[待补充]'} |"
    )
    return rows


def _build_pollutant_table(performance: dict, coarse_coverage: dict) -> list[str]:
    """Build a markdown summary of per-pollutant performance if available."""
    lines = []
    # If the LLM returned qmax with a pollutant field, show it
    qmax = performance.get("qmax")
    if isinstance(qmax, dict) and qmax.get("pollutant"):
        pollutant = qmax["pollutant"]
        val = qmax.get("value", "[待补充]")
        conditions = qmax.get("conditions", "")
        lines.append(
            f"Best qmax: **{_strip_known_units(str(val))} mg/g** for {pollutant}"
        )
        if conditions:
            lines.append(f"  (conditions: {conditions})")

    # List all known pollutants from coarse coverage
    all_pollutants = coarse_coverage.get("pollutants", [])
    if all_pollutants:
        lines.append(f"\nStudied pollutants ({len(all_pollutants)}): {', '.join(all_pollutants)}")
    return lines


# ──────────────────────────── file I/O ────────────────────────────

_OVERWRITE_THRESHOLD = 5000  # bytes – hand-curated files are typically >20 KB


def write_prototype_file(prototype_id: str, content: str, project_dir: Path = None) -> Path:
    """Write prototype.md with overwrite protection.

    If the existing file is larger than _OVERWRITE_THRESHOLD bytes (i.e. it
    was hand-curated or from a previous high-quality run), the pipeline
    output is written to ``prototype.md.pipeline`` instead and a warning is
    printed.  The original file is left untouched.
    """
    project_dir = project_dir or PROJECT_DIR
    proto_dir = project_dir / "prototypes" / prototype_id
    proto_dir.mkdir(parents=True, exist_ok=True)
    output_path = proto_dir / "prototype.md"

    if output_path.exists():
        existing_size = output_path.stat().st_size
        if existing_size > _OVERWRITE_THRESHOLD:
            # Existing file is substantial → do NOT overwrite
            pipeline_path = proto_dir / "prototype.md.pipeline"
            pipeline_path.write_text(content, encoding="utf-8")
            print(
                f"  WARNING: existing {prototype_id}/prototype.md ({existing_size:,} bytes) "
                f"preserved; pipeline output → prototype.md.pipeline"
            )
            return pipeline_path

    output_path.write_text(content, encoding="utf-8")
    return output_path


# ──────────────────────── feature-mapping updates ─────────────────


def update_feature_mapping(prototype_id: str, weight_assignments: list[dict], project_dir: Path = None) -> None:
    project_dir = project_dir or PROJECT_DIR
    mapping_path = project_dir / "feature-mapping.json"

    if not mapping_path.exists():
        return  # silently skip if feature-mapping.json doesn't exist

    with open(mapping_path, encoding="utf-8") as f:
        mapping = json.load(f)

    for wa in weight_assignments:
        mapping_type = wa.get("mapping_type")
        entry_key = wa.get("entry_key")
        weight = wa.get("weight")

        if mapping_type == "pollutant_prototype_map":
            section = mapping.get("pollutant_prototype_map", {})
            if entry_key in section:
                _update_entries(section[entry_key], prototype_id, wa, weight)

        elif mapping_type == "feature_prototype_map":
            section = mapping.get("feature_prototype_map", {})
            if entry_key in section:
                _update_feature_entries(section[entry_key], prototype_id, wa, weight)

    with open(mapping_path, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)


def _update_entries(entries, prototype_id, wa, weight):
    if isinstance(entries, dict):
        for sub_key, sub_entries in entries.items():
            if isinstance(sub_entries, list):
                for entry in sub_entries:
                    if isinstance(entry, dict) and entry.get("id") == prototype_id:
                        entry["weight"] = weight
                        if wa.get("mechanism_summary"):
                            entry["mechanism_summary"] = wa["mechanism_summary"]
                        if wa.get("design_hint"):
                            entry["design_hint"] = wa["design_hint"]
    elif isinstance(entries, list):
        for entry in entries:
            if isinstance(entry, dict) and entry.get("id") == prototype_id:
                entry["weight"] = weight


def _update_feature_entries(entries, prototype_id, wa, weight):
    if isinstance(entries, list):
        for entry in entries:
            if isinstance(entry, dict) and entry.get("id") == prototype_id:
                entry["weight"] = weight
