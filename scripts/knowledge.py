#!/usr/bin/env python3
"""Validate and query the repository's dependency-free knowledge graph."""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "knowledge" / "graph.jsonl"
SCHEMA_PATH = ROOT / "knowledge" / "schema.json"
GENERATED_DIR = ROOT / "generated"
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")


def load_schema() -> dict[str, Any]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def load_graph() -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]], list[str]]:
    entities: dict[str, dict[str, Any]] = {}
    relations: list[dict[str, Any]] = []
    errors: list[str] = []

    for line_number, raw in enumerate(GRAPH_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON: {exc}")
            continue

        operation = record.get("op")
        if operation == "create":
            entity_id = record.get("id")
            if entity_id in entities:
                errors.append(f"line {line_number}: duplicate create id {entity_id}")
                continue
            entities[entity_id] = {
                "id": entity_id,
                "type": record.get("type"),
                "properties": record.get("properties", {}),
                "source": record.get("source"),
            }
        elif operation == "update":
            entity_id = record.get("id")
            if entity_id not in entities:
                errors.append(f"line {line_number}: update before create for {entity_id}")
                continue
            entities[entity_id]["properties"].update(record.get("properties", {}))
        elif operation == "relate":
            relations.append({**record, "line": line_number})
        else:
            errors.append(f"line {line_number}: unsupported op {operation!r}")

    return entities, relations, errors


def outgoing(relations: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for relation in relations:
        result[relation["from"]].append(relation)
    return result


def related_ids(
    relation_index: dict[str, list[dict[str, Any]]], entity_id: str, relation_name: str
) -> list[str]:
    return [
        relation["to"]
        for relation in relation_index.get(entity_id, [])
        if relation["rel"] == relation_name
    ]


def validate_graph() -> tuple[list[str], list[str], dict[str, dict[str, Any]], list[dict[str, Any]]]:
    schema = load_schema()
    entities, relations, errors = load_graph()
    warnings: list[str] = []
    entity_types = schema["entity_types"]
    relation_types = schema["relation_types"]
    controlled = schema["controlled_values"]

    for entity_id, entity in entities.items():
        if not ID_PATTERN.fullmatch(entity_id or ""):
            errors.append(f"entity {entity_id!r}: id must use lowercase snake_case")
        entity_type = entity["type"]
        if entity_type not in entity_types:
            errors.append(f"entity {entity_id}: unknown type {entity_type!r}")
            continue
        properties = entity["properties"]
        missing = [
            field
            for field in entity_types[entity_type]["required_properties"]
            if field not in properties
        ]
        if missing:
            errors.append(f"entity {entity_id}: missing properties {', '.join(missing)}")

        checks = {
            "consumer": controlled["consumer"],
            "layer": controlled["module_layer"],
            "verification_status": controlled["verification_status"],
            "status": (
                controlled["claim_status"]
                if entity_type == "EvidenceClaim"
                else controlled["validation_status"]
                if entity_type == "ValidationPlan"
                else None
            ),
            "value_status": controlled["value_status"],
            "retrofit_level": controlled["retrofit_level"],
            "severity": controlled["constraint_severity"],
        }
        for field, allowed in checks.items():
            if field in properties and allowed is not None and properties[field] not in allowed:
                errors.append(
                    f"entity {entity_id}: invalid {field}={properties[field]!r}; "
                    f"allowed: {', '.join(allowed)}"
                )
        for scale in properties.get("applicable_scales", []):
            if scale not in controlled["scale"]:
                errors.append(f"entity {entity_id}: invalid scale {scale!r}")

    relation_keys: set[tuple[str, str, str]] = set()
    for relation in relations:
        line_number = relation["line"]
        source_id = relation.get("from")
        target_id = relation.get("to")
        relation_name = relation.get("rel")
        key = (source_id, relation_name, target_id)
        if key in relation_keys:
            errors.append(f"line {line_number}: duplicate relation {key}")
        relation_keys.add(key)

        if source_id not in entities:
            errors.append(f"line {line_number}: missing relation source {source_id}")
        if target_id not in entities:
            errors.append(f"line {line_number}: missing relation target {target_id}")
        if relation_name not in relation_types:
            errors.append(f"line {line_number}: unknown relation {relation_name!r}")
            continue
        if source_id not in entities or target_id not in entities:
            continue
        rule = relation_types[relation_name]
        source_type = entities[source_id]["type"]
        target_type = entities[target_id]["type"]
        if source_type not in rule["from"]:
            errors.append(
                f"line {line_number}: {relation_name} cannot start at {source_type}"
            )
        if target_type not in rule["to"]:
            errors.append(
                f"line {line_number}: {relation_name} cannot end at {target_type}"
            )

    relation_index = outgoing(relations)
    required_links = {
        "DesignMapping": [
            "addresses",
            "for_context",
            "derives_from",
            "realized_by",
            "constrained_by",
            "supported_by",
            "evaluated_by",
        ],
        "AssemblyPattern": [
            "addresses",
            "for_context",
            "implements",
            "composes",
            "constrained_by",
            "supported_by",
            "evaluated_by",
        ],
        "EvidenceClaim": ["cites"],
    }
    for entity_id, entity in entities.items():
        actual = {relation["rel"] for relation in relation_index.get(entity_id, [])}
        for relation_name in required_links.get(entity["type"], []):
            if relation_name not in actual:
                errors.append(f"entity {entity_id}: missing required relation {relation_name}")

        if entity["type"] == "AssemblyPattern":
            module_ids = related_ids(relation_index, entity_id, "composes")
            layers = {entities[module_id]["properties"]["layer"] for module_id in module_ids}
            if "reactor" not in layers:
                errors.append(f"entity {entity_id}: assembly must compose a reactor module")
            if len(layers) < 2:
                errors.append(f"entity {entity_id}: assembly must span at least two module layers")

        verification = entity["properties"].get("verification_status")
        if verification in {"partially_verified", "verified"}:
            claim_ids = related_ids(relation_index, entity_id, "supported_by")
            claim_statuses = {
                entities[claim_id]["properties"].get("status") for claim_id in claim_ids
            }
            if verification == "verified" and "verified" not in claim_statuses:
                errors.append(
                    f"entity {entity_id}: verified entity requires a verified evidence claim"
                )
            if verification == "partially_verified" and not claim_statuses.intersection(
                {"supported", "verified"}
            ):
                errors.append(
                    f"entity {entity_id}: partially_verified entity requires supported evidence"
                )

    for entity_id, entity in entities.items():
        if entity["type"] == "DesignParameter" and entity["properties"]["value_status"] == "unknown":
            warnings.append(f"parameter {entity_id}: value is intentionally unknown")

    return errors, warnings, entities, relations


def entity_name(entities: dict[str, dict[str, Any]], entity_id: str) -> str:
    return entities[entity_id]["properties"].get("name", entity_id)


def names_for(
    entities: dict[str, dict[str, Any]],
    relation_index: dict[str, list[dict[str, Any]]],
    entity_id: str,
    relation_name: str,
) -> list[str]:
    return [
        entity_name(entities, target_id)
        for target_id in related_ids(relation_index, entity_id, relation_name)
    ]


def design_record(
    entities: dict[str, dict[str, Any]],
    relation_index: dict[str, list[dict[str, Any]]],
    entity_id: str,
) -> dict[str, Any]:
    entity = entities[entity_id]
    properties = entity["properties"]
    module_ids = related_ids(relation_index, entity_id, "composes")
    if entity["type"] == "DesignMapping":
        module_ids = related_ids(relation_index, entity_id, "realized_by")

    mapping_ids = [entity_id] if entity["type"] == "DesignMapping" else related_ids(
        relation_index, entity_id, "implements"
    )
    prototype_ids: set[str] = set()
    mechanism_ids: set[str] = set()
    lever_ids: set[str] = set()
    parameter_ids: set[str] = set()
    for source_id in [*mapping_ids, *module_ids]:
        prototype_ids.update(related_ids(relation_index, source_id, "inspired_by"))
        mechanism_ids.update(related_ids(relation_index, source_id, "derives_from"))
        lever_ids.update(related_ids(relation_index, source_id, "uses_lever"))
        parameter_ids.update(related_ids(relation_index, source_id, "parameterized_by"))

    contexts = [entities[target_id] for target_id in related_ids(relation_index, entity_id, "for_context")]
    consumers = [
        entities[target_id]["properties"]["consumer"]
        for target_id in related_ids(relation_index, entity_id, "addresses")
    ]
    claims = [
        entities[target_id]["properties"]["status"]
        for target_id in related_ids(relation_index, entity_id, "supported_by")
    ]

    modules_by_layer: dict[str, list[str]] = defaultdict(list)
    for module_id in module_ids:
        module = entities[module_id]
        modules_by_layer[module["properties"]["layer"]].append(
            module["properties"]["name"]
        )

    return {
        "id": entity_id,
        "type": entity["type"],
        "name": properties["name"],
        "summary": properties["summary"],
        "consumers": consumers,
        "processes": sorted(
            {process for context in contexts for process in context["properties"]["processes"]}
        ),
        "problems": sorted(
            {problem for context in contexts for problem in context["properties"]["problems"]}
        ),
        "targets": names_for(entities, relation_index, entity_id, "optimizes"),
        "biological_prototypes": sorted(entity_name(entities, item) for item in prototype_ids),
        "biological_mechanisms": sorted(entity_name(entities, item) for item in mechanism_ids),
        "modules_by_layer": dict(sorted(modules_by_layer.items())),
        "engineering_levers": sorted(entity_name(entities, item) for item in lever_ids),
        "parameters": sorted(entity_name(entities, item) for item in parameter_ids),
        "constraints": names_for(entities, relation_index, entity_id, "constrained_by"),
        "evidence_statuses": claims,
        "verification_status": properties["verification_status"],
        "validation_plans": names_for(entities, relation_index, entity_id, "evaluated_by"),
    }


def generate_views(
    entities: dict[str, dict[str, Any]], relations: list[dict[str, Any]]
) -> list[Path]:
    relation_index = outgoing(relations)
    design_ids = [
        entity_id
        for entity_id, entity in entities.items()
        if entity["type"] in {"DesignMapping", "AssemblyPattern"}
    ]
    designs = [design_record(entities, relation_index, entity_id) for entity_id in design_ids]

    GENERATED_DIR.mkdir(exist_ok=True)
    design_space_path = GENERATED_DIR / "design-space.json"
    design_space_path.write_text(
        json.dumps(
            {
                "description": "由 knowledge/graph.jsonl 自动生成的多维设计视图；请勿手工编辑。",
                "designs": designs,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    type_counts = Counter(entity["type"] for entity in entities.values())
    status_counts = Counter(
        entity["properties"].get("verification_status")
        for entity in entities.values()
        if "verification_status" in entity["properties"]
    )
    layer_counts = Counter(
        entity["properties"]["layer"]
        for entity in entities.values()
        if entity["type"] == "DesignModule"
    )
    consumers_covered = sorted(
        {
            consumer
            for design in designs
            for consumer in design["consumers"]
        }
    )
    coverage_path = GENERATED_DIR / "coverage-report.json"
    coverage_path.write_text(
        json.dumps(
            {
                "description": "由知识图自动生成的内容覆盖与成熟度报告。",
                "entity_counts": dict(sorted(type_counts.items())),
                "relation_count": len(relations),
                "verification_status_counts": dict(sorted(status_counts.items())),
                "module_layer_counts": dict(sorted(layer_counts.items())),
                "consumers_covered_by_designs": consumers_covered,
                "known_gaps": {
                    "consumers_without_designs": sorted(
                        set(load_schema()["controlled_values"]["consumer"])
                        - set(consumers_covered)
                    ),
                    "module_layers_without_examples": sorted(
                        set(load_schema()["controlled_values"]["module_layer"])
                        - set(layer_counts)
                    ),
                    "verified_design_count": sum(
                        design["verification_status"] == "verified" for design in designs
                    ),
                },
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    matrix_lines = [
        "# 设计空间矩阵（自动生成）",
        "",
        "> 来源：`knowledge/graph.jsonl`。请勿手工编辑本文件。",
        "",
        "| 设计候选 | 消费者 | 工艺/问题 | 模块层 | 生物机制 | 状态 |",
        "|---|---|---|---|---|---|",
    ]
    for design in designs:
        context = ", ".join([*design["processes"], *design["problems"]])
        layers = ", ".join(design["modules_by_layer"].keys())
        mechanisms = ", ".join(design["biological_mechanisms"])
        matrix_lines.append(
            f"| `{design['id']}` | {', '.join(design['consumers'])} | {context} | "
            f"{layers} | {mechanisms} | {design['verification_status']} |"
        )
    matrix_path = GENERATED_DIR / "design-matrix.md"
    matrix_path.write_text("\n".join(matrix_lines) + "\n", encoding="utf-8")
    return [design_space_path, coverage_path, matrix_path]


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def parse_where(values: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for item in values:
        if "=" not in item:
            raise ValueError(f"--where expects key=value, got {item!r}")
        key, value = item.split("=", 1)
        result[key] = value
    return result


def matches_value(actual: Any, expected: str) -> bool:
    if isinstance(actual, list):
        return any(str(item).casefold() == expected.casefold() for item in actual)
    return str(actual).casefold() == expected.casefold()


def command_validate() -> int:
    errors, warnings, entities, relations = validate_graph()
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(
        f"Validation passed: {len(entities)} entities, {len(relations)} relations, "
        f"{len(warnings)} warning(s)"
    )
    return 0


def command_query(entity_type: str | None, where_values: list[str]) -> int:
    errors, _, entities, _ = validate_graph()
    if errors:
        print("Graph is invalid; run validate for details.", file=sys.stderr)
        return 1
    filters = parse_where(where_values)
    results = []
    for entity in entities.values():
        if entity_type and entity["type"] != entity_type:
            continue
        if all(matches_value(entity["properties"].get(key), value) for key, value in filters.items()):
            results.append(entity)
    print_json(results)
    return 0


def command_show(entity_id: str) -> int:
    errors, _, entities, relations = validate_graph()
    if errors:
        print("Graph is invalid; run validate for details.", file=sys.stderr)
        return 1
    if entity_id not in entities:
        print(f"Unknown entity id: {entity_id}", file=sys.stderr)
        return 1
    neighborhood = [
        {key: value for key, value in relation.items() if key != "line"}
        for relation in relations
        if relation["from"] == entity_id or relation["to"] == entity_id
    ]
    print_json({"entity": entities[entity_id], "relations": neighborhood})
    return 0


def command_design(consumer: str | None, process: str | None, problem: str | None) -> int:
    errors, _, entities, relations = validate_graph()
    if errors:
        print("Graph is invalid; run validate for details.", file=sys.stderr)
        return 1
    relation_index = outgoing(relations)
    candidates = []
    for entity_id, entity in entities.items():
        if entity["type"] not in {"DesignMapping", "AssemblyPattern"}:
            continue
        record = design_record(entities, relation_index, entity_id)
        if consumer and consumer not in record["consumers"]:
            continue
        if process and not any(item.casefold() == process.casefold() for item in record["processes"]):
            continue
        if problem and not any(item.casefold() == problem.casefold() for item in record["problems"]):
            continue
        candidates.append(record)
    print_json(candidates)
    return 0


def command_generate() -> int:
    errors, warnings, entities, relations = validate_graph()
    if errors:
        print("Graph is invalid; run validate for details.", file=sys.stderr)
        return 1
    paths = generate_views(entities, relations)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for path in paths:
        print(path.relative_to(ROOT).as_posix())
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="validate graph structure and evidence discipline")

    query_parser = subparsers.add_parser("query", help="filter entities by type and properties")
    query_parser.add_argument("--type", dest="entity_type")
    query_parser.add_argument("--where", action="append", default=[], metavar="KEY=VALUE")

    show_parser = subparsers.add_parser("show", help="show one entity and its direct relations")
    show_parser.add_argument("--id", required=True, dest="entity_id")

    design_parser = subparsers.add_parser("design", help="find design mappings and assemblies")
    design_parser.add_argument("--consumer")
    design_parser.add_argument("--process")
    design_parser.add_argument("--problem")

    subparsers.add_parser("generate", help="generate matrix and coverage views")
    return parser


def configure_stdio() -> None:
    """Keep Chinese names and symbols such as A²/O portable on Windows consoles."""
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
        elif hasattr(stream, "buffer"):
            setattr(sys, stream_name, io.TextIOWrapper(stream.buffer, encoding="utf-8"))


def main() -> int:
    configure_stdio()
    args = build_parser().parse_args()
    if args.command == "validate":
        return command_validate()
    if args.command == "query":
        return command_query(args.entity_type, args.where)
    if args.command == "show":
        return command_show(args.entity_id)
    if args.command == "design":
        return command_design(args.consumer, args.process, args.problem)
    if args.command == "generate":
        return command_generate()
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
