import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "knowledge_tool", ROOT / "scripts" / "knowledge.py"
)
knowledge = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(knowledge)


class KnowledgeGraphTests(unittest.TestCase):
    def setUp(self):
        errors, warnings, entities, relations = knowledge.validate_graph()
        self.errors = errors
        self.warnings = warnings
        self.entities = entities
        self.relations = relations

    def test_graph_is_valid(self):
        self.assertEqual([], self.errors)

    def test_a2o_assembly_spans_microbial_reactor_and_control(self):
        index = knowledge.outgoing(self.relations)
        module_ids = knowledge.related_ids(
            index, "assembly_adaptive_a2o_reactor", "composes"
        )
        layers = {self.entities[item]["properties"]["layer"] for item in module_ids}
        self.assertEqual({"microbial", "reactor", "control"}, layers)

    def test_a2o_design_query_dimensions(self):
        index = knowledge.outgoing(self.relations)
        design = knowledge.design_record(
            self.entities, index, "assembly_adaptive_a2o_reactor"
        )
        self.assertIn("reactor_design", design["consumers"])
        self.assertIn("A2O", design["processes"])
        self.assertIn("low_cn", design["problems"])
        self.assertEqual("unverified", design["verification_status"])

    def test_cli_can_emit_a2o_design_as_utf8(self):
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "knowledge.py"),
                "design",
                "--consumer",
                "reactor_design",
                "--process",
                "A2O",
                "--problem",
                "low_cn",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout.decode("utf-8"))
        self.assertEqual(2, len(payload))
        self.assertIn("A²/O", payload[1]["name"])


if __name__ == "__main__":
    unittest.main()
