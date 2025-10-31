import pytest
from gitlint.tests.base import BaseTestCase
from checkmark_rai_lint.rules import RaiFooterExists


class TestRaiFooterExists(BaseTestCase):
    def test_ai_generated_footer(self):
        rule = RaiFooterExists()
        commit = self.gitcommit("feat: add new feature\n\n🛡️ RAI: AI-Generated")
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_ai_assisted_footer(self):
        rule = RaiFooterExists()
        commit = self.gitcommit("fix: resolve bug\n\n🛡️ RAI: AI-Assisted")
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_verdent_ai_footer(self):
        rule = RaiFooterExists()
        commit = self.gitcommit(
            "chore: update dependencies\n\nGenerated-by: Verdent AI <verdent@verdent.ai>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_missing_rai_footer(self):
        rule = RaiFooterExists()
        commit = self.gitcommit("feat: add new feature\n\nSome other footer")
        violations = rule.validate(commit)
        assert len(violations) == 1
        assert "RAI footer" in violations[0].message

    def test_case_insensitive_footer(self):
        rule = RaiFooterExists()
        commit = self.gitcommit("feat: add feature\n\n🛡️ rai: ai-generated")
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_malformed_footer(self):
        rule = RaiFooterExists()
        commit = self.gitcommit("feat: add feature\n\n🛡️ RAI: AI-Something")
        violations = rule.validate(commit)
        assert len(violations) == 1
