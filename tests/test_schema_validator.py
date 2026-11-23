import json
import unittest
from pathlib import Path

from scripts.validate_mcp_schemas import (
    validate_server_json,
    validate_tool,
    validate_tools_list,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


class StrictToolSchemaValidatorTests(unittest.TestCase):
    def test_valid_tool_passes(self) -> None:
        tool = {
            "name": "get_creator_stats",
            "description": "Fetch SocialBlade stats.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "profiles": {"type": "array", "items": {"type": "string"}},
                    "handles": {
                        "anyOf": [
                            {"type": "array", "items": {"type": "string"}},
                            {"type": "null"},
                        ]
                    },
                },
                "required": ["profiles"],
            },
        }
        self.assertEqual(validate_tool(tool), [])

    def test_rejects_array_missing_items(self) -> None:
        tool = {
            "name": "bad_array_tool",
            "description": "Broken array.",
            "inputSchema": {
                "type": "object",
                "properties": {"ids": {"type": "array"}},
            },
        }
        errors = validate_tool(tool)
        self.assertTrue(any("missing non-empty 'items'" in e for e in errors), errors)

    def test_rejects_nested_anyof_array_missing_items(self) -> None:
        tool = {
            "name": "bad_anyof_array",
            "description": "Broken nested array.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "handles": {"anyOf": [{"type": "array"}, {"type": "null"}]}
                },
            },
        }
        errors = validate_tool(tool)
        self.assertTrue(any("missing non-empty 'items'" in e for e in errors), errors)

    def test_rejects_double_dash_tool_name(self) -> None:
        tool = {
            "name": "socialblade--creator_stats",
            "description": "Double dash name.",
            "inputSchema": {"type": "object", "properties": {}},
        }
        errors = validate_tool(tool)
        self.assertTrue(any("double-dash" in e for e in errors), errors)

    def test_rejects_invalid_characters_and_long_name(self) -> None:
        tool = {
            "name": "a" * 65,
            "description": "Too long.",
            "inputSchema": {"type": "object", "properties": {}},
        }
        errors = validate_tool(tool)
        self.assertTrue(any("tool name must match" in e for e in errors), errors)

    def test_rejects_root_combinator_and_missing_required_prop(self) -> None:
        tool = {
            "name": "bad_root",
            "description": "Root anyOf.",
            "inputSchema": {
                "type": "object",
                "properties": {},
                "required": ["missing_field"],
                "anyOf": [{"type": "object"}],
            },
        }
        errors = validate_tool(tool)
        self.assertTrue(any("top-level 'anyOf'" in e for e in errors), errors)
        self.assertTrue(any("missing_field" in e for e in errors), errors)

    def test_rejects_duplicate_tool_names(self) -> None:
        t = {
            "name": "dup_tool",
            "description": "Desc",
            "inputSchema": {"type": "object", "properties": {}},
        }
        errors = validate_tools_list([t, t])
        self.assertTrue(any("duplicate tool name" in e for e in errors), errors)


class RegistryServerJsonTests(unittest.TestCase):
    def test_all_server_json_files_valid(self) -> None:
        files = sorted(REPO_ROOT.glob("*/server.json"))
        self.assertGreater(len(files), 0)
        for path in files:
            self.assertEqual(validate_server_json(path), [], f"Errors in {path}")

    def test_socialblade_authorization_is_optional_for_x402(self) -> None:
        path = REPO_ROOT / "socialblade-creator-stats" / "server.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(
            data["name"], "io.github.benthepythondev00/socialblade-creator-stats"
        )
        self.assertEqual(data["version"], "1.0.2")
        self.assertLessEqual(len(data["description"]), 100)
        self.assertIn("x402", data["description"].lower())

        headers = data["remotes"][0]["headers"]
        auth_headers = [h for h in headers if h.get("name") == "Authorization"]
        self.assertEqual(len(auth_headers), 1)
        auth = auth_headers[0]
        self.assertIs(auth["isRequired"], False)
        self.assertIs(auth["isSecret"], True)
        self.assertIn("x402", auth["description"].lower())
        self.assertIn("optional", auth["description"].lower())

    def test_readme_documents_http_402_base_usdc_example(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("HTTP 402 -> Base USDC", readme)
        self.assertIn("X-PAYMENT", readme)
        self.assertIn("0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", readme)
        self.assertIn("eip3009", readme)
        self.assertIn("10000", readme)


if __name__ == "__main__":
    unittest.main()
