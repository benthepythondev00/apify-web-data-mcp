import json
import unittest
import urllib.error
import urllib.request

from scripts.validate_mcp_schemas import fetch_tools_list, validate_tools_list

MCP_URL = "https://socialblade-creator-stats.mcpize.run/mcp"
EXPECTED_TOOLS = {
    "get_creator_stats",
    "get_top_creators",
    "get_twitch_channels",
    "get_bluesky",
    "get_instagram_videos",
}
BASE_USDC_CONTRACT = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"


class SocialBladeMcpContractTests(unittest.TestCase):
    def test_keyless_tools_list_passes_strict_schema_validation(self) -> None:
        tools = fetch_tools_list(MCP_URL)
        names = {t["name"] for t in tools}
        self.assertEqual(names, EXPECTED_TOOLS)
        errors = validate_tools_list(tools)
        self.assertEqual(errors, [], f"Strict schema errors: {errors}")

    def test_keyless_tools_call_returns_http_402_base_usdc_challenge(self) -> None:
        body = json.dumps(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "tools/call",
                "params": {
                    "name": "get_creator_stats",
                    "arguments": {"profiles": ["@mkbhd"]},
                },
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            MCP_URL,
            data=body,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
                "User-Agent": "mcp-schema-validator/1.0",
            },
            method="POST",
        )
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            urllib.request.urlopen(req, timeout=20)

        err = ctx.exception
        self.assertEqual(err.code, 402)
        payload = json.loads(err.read().decode("utf-8"))
        self.assertEqual(payload.get("x402Version"), 1)
        accepts = payload.get("accepts")
        self.assertIsInstance(accepts, list)
        self.assertGreaterEqual(len(accepts), 1)
        offer = accepts[0]
        self.assertEqual(offer.get("scheme"), "exact")
        self.assertEqual(offer.get("network"), "base")
        self.assertEqual(offer.get("maxAmountRequired"), "10000")
        self.assertEqual(offer.get("asset"), BASE_USDC_CONTRACT)
        self.assertEqual(offer.get("extra", {}).get("assetTransferMethod"), "eip3009")


if __name__ == "__main__":
    unittest.main()
