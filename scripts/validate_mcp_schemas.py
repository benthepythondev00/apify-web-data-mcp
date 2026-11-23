#!/usr/bin/env python3
"""Strict MCP tool-schema and Official MCP Registry metadata validator.

Enforces OpenAI, Claude, and Cursor strict tool-schema compatibility rules:
- Tool names match ^[a-zA-Z0-9_-]{1,64}$ and contain no double-dash ('--').
- Tool descriptions are non-empty strings.
- Root inputSchema is type="object" with a properties dict and no top-level
  oneOf/anyOf/allOf/not combinators.
- Every key in `required` exists in `properties`.
- Every schema node with type="array" (anywhere recursively, including inside
  anyOf/allOf/oneOf) defines an `items` schema object (Apify MCP issue #36).
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any

TOOL_NAME_RE = re.compile(r"^[a-zA-Z0-9_-]{1,64}$")
FORBIDDEN_ROOT_KEYS = ("oneOf", "anyOf", "allOf", "not")


def _walk_schema(node: Any, path: str, errors: list[str]) -> None:
    if not isinstance(node, dict):
        return

    node_type = node.get("type")
    is_array = node_type == "array" or (
        isinstance(node_type, list) and "array" in node_type
    )
    if is_array:
        items = node.get("items")
        if not isinstance(items, dict) or not items:
            errors.append(f"{path}: array schema missing non-empty 'items' object")
        else:
            _walk_schema(items, f"{path}.items", errors)

    props = node.get("properties")
    if isinstance(props, dict):
        for prop_name, prop_schema in props.items():
            _walk_schema(prop_schema, f"{path}.properties.{prop_name}", errors)

    required = node.get("required")
    if isinstance(required, list) and isinstance(props, dict):
        for req in required:
            if req not in props:
                errors.append(
                    f"{path}: required key '{req}' is not declared in properties"
                )

    for comb in ("anyOf", "allOf", "oneOf"):
        variants = node.get(comb)
        if isinstance(variants, list):
            for idx, variant in enumerate(variants):
                _walk_schema(variant, f"{path}.{comb}[{idx}]", errors)

    addl = node.get("additionalProperties")
    if isinstance(addl, dict):
        _walk_schema(addl, f"{path}.additionalProperties", errors)


def validate_tool(tool: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    name = tool.get("name")
    if not isinstance(name, str) or not name:
        return ["tool missing non-empty string 'name'"]

    if not TOOL_NAME_RE.match(name):
        errors.append(
            f"{name}: tool name must match {TOOL_NAME_RE.pattern} (1-64 chars, alphanumeric/_/-)"
        )
    if "--" in name:
        errors.append(f"{name}: tool name must not contain double-dash '--'")

    desc = tool.get("description")
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{name}: missing non-empty description")

    input_schema = tool.get("inputSchema")
    if not isinstance(input_schema, dict):
        errors.append(f"{name}: missing inputSchema object")
    else:
        if input_schema.get("type") != "object":
            errors.append(
                f"{name}: root inputSchema.type must be 'object', got {input_schema.get('type')!r}"
            )
        if not isinstance(input_schema.get("properties"), dict):
            errors.append(f"{name}: root inputSchema must declare a 'properties' object")
        for forbidden in FORBIDDEN_ROOT_KEYS:
            if forbidden in input_schema:
                errors.append(
                    f"{name}: root inputSchema must not contain top-level '{forbidden}'"
                )
        _walk_schema(input_schema, f"{name}.inputSchema", errors)

    output_schema = tool.get("outputSchema")
    if isinstance(output_schema, dict):
        _walk_schema(output_schema, f"{name}.outputSchema", errors)

    return errors


def validate_tools_list(tools: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if not isinstance(tools, list) or not tools:
        return ["tools list is empty or not a list"]
    seen: set[str] = set()
    for tool in tools:
        name = tool.get("name") if isinstance(tool, dict) else None
        if isinstance(name, str):
            if name in seen:
                errors.append(f"{name}: duplicate tool name")
            seen.add(name)
        errors.extend(validate_tool(tool))
    return errors


def validate_server_json(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    for req in ("$schema", "name", "description", "version"):
        if not data.get(req):
            errors.append(f"{path}: missing required field '{req}'")
    desc = data.get("description", "")
    if isinstance(desc, str) and len(desc) > 100:
        errors.append(
            f"{path}: description length {len(desc)} exceeds MCP Registry 100-char maxLength"
        )
    remotes = data.get("remotes", [])
    if not isinstance(remotes, list) or not remotes:
        errors.append(f"{path}: must define at least one remote")
    for idx, remote in enumerate(remotes):
        url = remote.get("url", "")
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"{path}: remotes[{idx}].url must be https://")
    return errors


def parse_mcp_response(raw: str) -> dict[str, Any]:
    text = raw.strip()
    if text.startswith("{"):
        return json.loads(text)
    for line in text.splitlines():
        if line.startswith("data:"):
            return json.loads(line[len("data:") :].strip())
    raise ValueError("Unable to parse JSON or SSE data payload from MCP response")


def fetch_tools_list(url: str, timeout: int = 20) -> list[dict[str, Any]]:
    body = json.dumps(
        {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}
    ).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "User-Agent": "mcp-schema-validator/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        if resp.status != 200:
            raise RuntimeError(f"Expected HTTP 200 from tools/list, got {resp.status}")
        payload = parse_mcp_response(resp.read().decode("utf-8"))
    return payload["result"]["tools"]


def main(argv: list[str]) -> int:
    url = argv[1] if len(argv) > 1 else "https://socialblade-creator-stats.mcpize.run/mcp"
    tools = fetch_tools_list(url)
    errors = validate_tools_list(tools)
    if errors:
        for err in errors:
            print(f"FAIL: {err}", file=sys.stderr)
        return 1
    print(f"OK: {len(tools)} tools validated cleanly against strict OpenAI/Claude/Cursor rules:")
    for t in tools:
        print(f"  - {t['name']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
