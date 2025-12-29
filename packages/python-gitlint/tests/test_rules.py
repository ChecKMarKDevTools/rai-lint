from unittest.mock import Mock

import pytest

from gitlint_rai.rules import RaiFooterExists


@pytest.fixture
def rule():
    return RaiFooterExists()


def create_commit(message: str):
    commit = Mock()
    commit.message.full = message

    lines = message.split("\n")
    commit.message.title = lines[0] if lines else ""
    commit.message.body = lines[1:] if len(lines) > 1 else []

    return commit


class TestRaiFooterExists:
    @pytest.mark.parametrize(
        "footer",
        [
            "Generated-by: GitHub Copilot <copilot@github.com>",
            "Assisted-by: Verdent AI <verdent@verdent.ai>",
            "Co-authored-by: GitHub Copilot <copilot@github.com>",
            "Commit-generated-by: Claude AI <claude@anthropic.com>",
            "Authored-by: Jane Doe <jane@example.com>",
            "generated-by: GitHub Copilot <copilot@github.com>",  # case insensitive
        ],
    )
    def test_valid_footers(self, rule, footer):
        commit = create_commit(f"feat: add feature\n\n{footer}")
        violations = rule.validate(commit)
        assert len(violations) == 0, f"Expected no violations for {footer}"

    def test_generated_by_footer_no_email(self, rule):
        commit = create_commit("feat: add new feature\n\nGenerated-by: GitHub Copilot")
        violations = rule.validate(commit)
        assert len(violations) == 1
        assert "AI attribution" in violations[0].message

    def test_missing_ai_attribution(self, rule):
        commit = create_commit("feat: add new feature\n\nSome other footer")
        violations = rule.validate(commit)
        assert len(violations) == 1
        assert "AI attribution" in violations[0].message

    def test_malformed_footer_empty_value(self, rule):
        commit = create_commit("feat: add feature\n\nGenerated-by: ")
        violations = rule.validate(commit)
        assert len(violations) == 1

    def test_multiple_ai_tools(self, rule):
        commit = create_commit(
            "feat: complex feature\n\nGenerated-by: ChatGPT <chatgpt@openai.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_redos_resistance_long_trailer_value(self, rule):
        long_value = "A" * 10000
        commit = create_commit(
            f"feat: add feature\n\nGenerated-by: {long_value} <test@example.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_redos_resistance_pathological_input(self, rule):
        pathological = "A" * 5000 + ":" + "B" * 5000
        commit = create_commit(f"feat: add feature\n\n{pathological}")
        violations = rule.validate(commit)
        assert len(violations) == 1

    def test_empty_body(self, rule):
        commit = Mock()
        commit.message.full = "feat: add feature"
        commit.message.title = "feat: add feature"
        commit.message.body = []
        violations = rule.validate(commit)
        assert len(violations) == 1

    @pytest.mark.parametrize(
        "malformed",
        [
            ": value only",
            "123-key: value",
        ],
    )
    def test_malformed_trailers(self, rule, malformed):
        commit = create_commit(f"feat: add feature\n\n{malformed}")
        violations = rule.validate(commit)
        assert len(violations) == 1

    def test_trailer_block_stops_on_blank_line(self, rule):
        commit = create_commit(
            "feat: add feature\n\nKey: value\n\nGenerated-by: AI <ai@example.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_non_trailer_stops_trailer_block(self, rule):
        commit = create_commit("feat: add feature\n\nSome text\nKey: value")
        violations = rule.validate(commit)
        assert len(violations) == 1

    def test_all_blank_body_lines(self, rule):
        """If message.body contains only blank lines, the trailer block finder
        should return empty and parsing should report missing attribution."""
        # Title followed by two blank lines -> body becomes ['', '']
        commit = create_commit("feat: add feature\n\n\n")
        violations = rule.validate(commit)
        assert len(violations) == 1
