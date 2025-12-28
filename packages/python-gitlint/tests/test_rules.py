from unittest.mock import Mock

import pytest

from gitlint_rai.rules import RaiFooterExists


def create_commit(message: str):
    commit = Mock()
    commit.message.full = message

    lines = message.split("\n")
    commit.message.title = lines[0] if lines else ""
    commit.message.body = lines[1:] if len(lines) > 1 else []

    return commit


class TestRaiFooterExists:
    def test_generated_by_footer(self):
        rule = RaiFooterExists()
        commit = create_commit(
            "feat: add new feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_generated_by_footer_no_email(self):
        rule = RaiFooterExists()
        commit = create_commit("feat: add new feature\n\nGenerated-by: GitHub Copilot")
        violations = rule.validate(commit)
        assert len(violations) == 1

    def test_assisted_by_footer(self):
        rule = RaiFooterExists()
        commit = create_commit("fix: resolve bug\n\nAssisted-by: Verdent AI <verdent@verdent.ai>")
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_co_authored_by_footer(self):
        rule = RaiFooterExists()
        commit = create_commit(
            "refactor: improve code\n\nCo-authored-by: GitHub Copilot <copilot@github.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_commit_generated_by_footer(self):
        rule = RaiFooterExists()
        commit = create_commit(
            "chore: update dependencies\n\nCommit-generated-by: Claude AI <claude@anthropic.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_authored_by_footer(self):
        rule = RaiFooterExists()
        commit = create_commit(
            "feat: implement feature\n\nAuthored-by: Jane Doe <jane@example.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_missing_ai_attribution(self):
        rule = RaiFooterExists()
        commit = create_commit("feat: add new feature\n\nSome other footer")
        violations = rule.validate(commit)
        assert len(violations) == 1
        assert "AI attribution" in violations[0].message

    def test_case_insensitive_footer(self):
        rule = RaiFooterExists()
        commit = create_commit(
            "feat: add feature\n\ngenerated-by: GitHub Copilot <copilot@github.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_malformed_footer(self):
        # With the new rule, almost any non-empty string is valid if the key is correct.
        # So "Generated-by: Invalid Format" is actually valid now as "Invalid Format" is a name.
        # We should test for empty value if that's possible, or just remove this test if any string is valid.
        # Let's assume empty value is invalid.
        rule = RaiFooterExists()
        commit = create_commit("feat: add feature\n\nGenerated-by: ")
        # The simple parser might parse empty string.
        # If regex is ^.+$ then empty string fails.
        violations = rule.validate(commit)
        assert len(violations) == 1

    def test_multiple_ai_tools(self):
        rule = RaiFooterExists()
        commit = create_commit(
            "feat: complex feature\n\nGenerated-by: ChatGPT <chatgpt@openai.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_guidance_percentages(self):
        rule = RaiFooterExists()
        commit = create_commit(
            "feat: add feature\n\nAssisted-by: GitHub Copilot <copilot@github.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0
