import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LISTING_JSON = REPO_ROOT / "socialblade-creator-stats" / "mcpize-listing.json"
LISTING_RESEARCH = REPO_ROOT / "socialblade-creator-stats" / "docs" / "listing-research.md"
LAUNCH_PLAN = REPO_ROOT / "socialblade-creator-stats" / "docs" / "launch-plan.md"
README_MD = REPO_ROOT / "README.md"


class SocialBladeListingSeoTests(unittest.TestCase):
    def setUp(self) -> None:
        self.listing = json.loads(LISTING_JSON.read_text(encoding="utf-8"))

    def test_title_and_seo_title_preserved(self) -> None:
        self.assertEqual(
            self.listing["name"],
            "SocialBlade Creator Stats: Influencer Vetting & Creator Analytics",
        )
        self.assertEqual(
            self.listing["seo_title"],
            "Influencer Vetting MCP: SocialBlade Creator Analytics",
        )

    def test_top_summary_word_count_and_x402_terms(self) -> None:
        first_para = self.listing["long_description"].split("\n\n", 1)[0].strip()
        words = first_para.split()
        self.assertGreaterEqual(len(words), 45, f"Top summary too short ({len(words)} words)")
        self.assertLessEqual(len(words), 60, f"Top summary too long ({len(words)} words)")
        lower = first_para.lower()
        for required in ("x402", "pay-per-call", "$0.01 usdc on base", "free", "$9", "$29"):
            self.assertIn(required, lower)

    def test_short_description_and_tags_cover_core_and_x402_terms(self) -> None:
        desc_lower = self.listing["description"].lower()
        for required in ("socialblade", "creator", "influencer", "x402", "pay-per-call", "$0.01 usdc on base"):
            self.assertIn(required, desc_lower)
        tags_lower = {t.lower() for t in self.listing["tags"]}
        for required_tag in ("socialblade", "influencer", "x402", "pay-per-call", "usdc", "base"):
            self.assertIn(required_tag, tags_lower)

    def test_four_geo_faq_questions_present_in_listing_and_readme(self) -> None:
        expected_questions = [
            "How can an AI agent pull SocialBlade creator stats without an API key?",
            "How much does each x402 tool call cost?",
            "How does this compare to the SocialBlade Business API or HypeAuditor?",
            "What if a creator is untracked or Instagram history is requested?",
        ]
        long_desc = self.listing["long_description"]
        readme = README_MD.read_text(encoding="utf-8")
        for q in expected_questions:
            self.assertIn(q, long_desc, f"Missing FAQ in mcpize-listing.json: {q}")
            self.assertIn(q, readme, f"Missing FAQ in README.md: {q}")

    def test_no_em_or_en_dashes_in_listing_copy(self) -> None:
        for field in ("description", "seo_description", "long_description"):
            text = self.listing[field]
            self.assertNotIn("\u2014", text, f"Em dash found in {field}")
            self.assertNotIn("\u2013", text, f"En dash found in {field}")

    def test_listing_research_and_launch_plan_exist(self) -> None:
        research = LISTING_RESEARCH.read_text(encoding="utf-8")
        for heading in ("## Search terms", "## Rivals", "## Applied", "## Feature baseline", "## AI search (GEO/AEO)", "## Rank after live"):
            self.assertIn(heading, research)
        plan = LAUNCH_PLAN.read_text(encoding="utf-8")
        for heading in ("## Day 1", "## Day 2-3", "## Day 4-7", "## Measure"):
            self.assertIn(heading, plan)


if __name__ == "__main__":
    unittest.main()
