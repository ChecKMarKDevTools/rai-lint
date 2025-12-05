from unittest.mock import Mock

from checkmark_rai_lint.rules import RaiFooterExists


def create_commit(message: str):
    """
    Creates a Mock commit object with the given message and parsed trailers.

    This simulates the behavior of gitlint, which parses commit messages and
    provides a 'trailers' dictionary (key-value pairs from the footer) to the rules.
    Since we are testing the rule in isolation, we need to manually parse the
    trailers from the message string and populate the Mock object.
    """
    commit = Mock()
    commit.message.full = message

    trailers = {}
    lines = message.split("\n")
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key and value:
                if key not in trailers:
                    trailers[key] = []
                trailers[key].append(value)

    commit.message.trailers = trailers
    return commit


def test_valid_generated_by():
    rule = RaiFooterExists()
    commit = create_commit("feat: add feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>")
    violations = rule.validate(commit)
    assert len(violations) == 0, f"Expected no violations but got: {violations}"


def test_valid_assisted_by():
    rule = RaiFooterExists()
    commit = create_commit("fix: resolve bug\n\nAssisted-by: Verdent AI <verdent@verdent.ai>")
    violations = rule.validate(commit)
    assert len(violations) == 0


def test_valid_verdent_ai():
    rule = RaiFooterExists()
    commit = create_commit("chore: update\n\nGenerated-by: Verdent AI <verdent@verdent.ai>")
    violations = rule.validate(commit)
    assert len(violations) == 0


def test_invalid_no_footer():
    rule = RaiFooterExists()
    commit = create_commit("feat: add feature\n\nNo footer")
    violations = rule.validate(commit)
    assert len(violations) == 1
    assert "AI attribution" in violations[0].message


def test_invalid_malformed():
    rule = RaiFooterExists()
    commit = create_commit("feat: add feature\n\nGenerated-by: Invalid Format")
    violations = rule.validate(commit)
    assert len(violations) == 1


def test_case_insensitive():
    rule = RaiFooterExists()
    commit = create_commit("feat: add feature\n\ngenerated-by: GitHub Copilot <copilot@github.com>")
    violations = rule.validate(commit)
    assert len(violations) == 0


def test_with_additional_footers():
    rule = RaiFooterExists()
    commit = create_commit(
        "feat: add feature\n\nDescription\n\nCloses #123\n\nAssisted-by: GitHub Copilot <copilot@github.com>"
    )
    violations = rule.validate(commit)
    assert len(violations) == 0
