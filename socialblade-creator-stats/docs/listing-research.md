# Listing research: SocialBlade Creator Stats (MCPize)

Date: 2026-11-26
Store: MCPize

## Search terms
- `socialblade`: rank before: #1 of 1
- `creator stats`: rank before: #1 of 1
- `influencer`: rank before: #1 of 2
- `x402`: rank before: not found of 24 (page 1)
- `pay per call`: rank before: not found of 3
- `usdc`: rank before: not found of 24 (page 1)

## Rivals
- [TradeSignal Feed](https://mcpize.com/mcp/tradesignal-feed): Crypto market data and agent-commerce tools for AI agents, paid per call via x402 (USDC on Base); x402 per-call + free tools; leads with explicit "paid per call via x402 (USDC on Base)" in the first sentence and tags `x402`, `usdc`, `base`, `agent-payments`.
- [watch-engine-mcp](https://mcpize.com/mcp/watch-engine-mcp): Currency rates, VAT rates, and tariff lookups for AI agents; $0.01 USDC on Base per call; leads with use cases and ends the short summary with "Pay per call in USDC on Base" plus tag `x402` (ranks #1 for `pay per call`).
- [Stelar Crypto Signals](https://mcpize.com/mcp/stelar-crypto-signals): Live grid and market-regime crypto telemetry; $0.01 to $0.05 USDC on Base per call; leads with production telemetry and states "Pay per call in USDC on Base via x402, no signup, no API key" plus tags `x402`, `usdc`, `base` (ranks #2 for `pay per call`).
- [US Property Deed Records](https://mcpize.com/mcp/us-property-deed-records): Official Broward County property deed lookups; $0.01 USDC on Base per call, 3 subscribers; leads with exact tool names and regional coverage check.
- [x-trend-intelligence-mcp](https://mcpize.com/mcp/x-trend-intelligence-mcp): 8 social intelligence tools for X/Twitter including influencer analysis; subscription tiers; ranks #2 for `influencer` right behind SocialBlade Creator Stats.

## Applied
- Title: Keep `SocialBlade Creator Stats: Influencer Vetting & Creator Analytics` and SEO title `Influencer Vetting MCP: SocialBlade Creator Analytics` unchanged to protect #1 ranks on `socialblade`, `creator stats`, and `influencer`.
- Headline: Add `Keyless x402 pay-per-call at $0.01 USDC on Base, or Free 100/mo & $9 Pro.` to the short description and add `x402`, `pay-per-call`, `usdc`, `base` to `tags`.
- Description: Replace the opening paragraph with a 53-word top summary naming `x402`, `pay-per-call`, and `$0.01 USDC on Base` (no account or API key required) alongside Free / Pro $9 / Business $29 tiers, add an x402 row to the pricing table, and replace the FAQ with 4 self-contained AI-search Q&A blocks covering keyless x402 access, $0.01 per-call pricing, comparison to SocialBlade Business API/HypeAuditor, and structured error/Instagram coverage.
- Why: Top MCPize listings for `x402`, `pay per call`, and `usdc` put those exact phrases in `description` and `tags`; our listing had x402 enabled in `pricing` but zero mentions in text or tags, leaving it invisible in all three x402 searches.

## Feature baseline
- Native x402 HTTP 402 payment challenge on Base USDC: baseline (3 of 4 x402 rivals); ours: yes, tested by `tests/contract/test_socialblade_mcp.py::test_keyless_tools_call_returns_http_402_base_usdc_challenge`.
- Keyless `tools/list` discovery passing strict OpenAI/Claude schema rules: baseline (5 of 5 rivals); ours: yes, tested by `tests/contract/test_socialblade_mcp.py::test_keyless_tools_list_passes_strict_schema_validation`.
- Explicit per-call price and item cap in listing and tool metadata: baseline (4 of 5 rivals); ours: yes, tested by `tests/test_listing_seo.py`.
- Compact default output with structured per-item status (`ok`, `not_tracked`, `blocked`, `bad_link`) and upfront coverage limits: differentiator (fixes 2.5-star complaints on Apify SocialBlade scrapers and Bright Data token bloat); ours: yes, verified in `socialblade-creator-stats/evidence/field-coverage-2026-11-01.txt`.
- Both subscription tiers (Free/$9/$29) and keyless x402 ($0.01 USDC) on the same endpoint: differentiator (most x402 rivals are x402-only); ours: yes, verified by `tests/test_schema_validator.py::test_socialblade_authorization_is_optional_for_x402`.

## AI search (GEO/AEO)
- "How can an AI agent pull SocialBlade creator stats without an API key?": answered by the top 53-word summary and FAQ #1 in `socialblade-creator-stats/mcpize-listing.json` and `README.md`.
- "How much does each x402 tool call cost?": answered by the pricing table and FAQ #2 ($0.01 USDC on Base across all 5 tools, up to 10 creators or 50 records per call).
- "How does this compare to the SocialBlade Business API or HypeAuditor?": answered by the "How it compares" section and FAQ #3 (no prepaid credit packs or $150+/yr contracts; public SocialBlade metrics and spike dates, no private audience demographics).
- "What if a creator is untracked or Instagram history is requested?": answered by "Structured status rows & platform coverage" and FAQ #4 (`ok`, `not_tracked`, `blocked`, `bad_link`; Instagram daily history returns `null` without SocialBlade login).

## Rank after live
(day 7 and day 30 reads are appended here by the engine)
