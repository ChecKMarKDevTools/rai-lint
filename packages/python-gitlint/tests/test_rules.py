import pytest
from gitlint.git import GitCommit, GitCommitMessage, GitContext
from checkmark_rai_lint.rules import RaiFooterExists


class TestRaiFooterExists:
    @pytest.fixture
    def context(self):
        return GitContext()
    
    @pytest.fixture
    def rule(self):
        return RaiFooterExists()
    
    def create_commit(self, context, message):
        """Helper method to create GitCommit objects for testing"""
        git_message = GitCommitMessage.from_full_message(context, message)
        return GitCommit(context, git_message)

    def test_generated_by_footer(self, context, rule):
        commit = self.create_commit(
            context,
            "feat: add new feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_assisted_by_footer(self, context, rule):
        commit = self.create_commit(context, "fix: resolve bug\n\nAssisted-by: Verdent AI <verdent@verdent.ai>")
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_co_authored_by_footer(self, context, rule):
        commit = self.create_commit(
            context,
            "refactor: improve code\n\nCo-authored-by: GitHub Copilot <copilot@github.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_commit_generated_by_footer(self, context, rule):
        commit = self.create_commit(
            context,
            "chore: update dependencies\n\nCommit-generated-by: Claude AI <claude@anthropic.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_authored_by_footer(self, context, rule):
        commit = self.create_commit(
            context,
            "feat: implement feature\n\nAuthored-by: Jane Doe <jane@example.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_missing_ai_attribution(self, context, rule):
        commit = self.create_commit(context, "feat: add new feature\n\nSome other footer")
        violations = rule.validate(commit)
        assert len(violations) == 1
        assert "AI attribution" in violations[0].message

    def test_case_insensitive_footer(self, context, rule):
        commit = self.create_commit(
            context,
            "feat: add feature\n\ngenerated-by: GitHub Copilot <copilot@github.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_malformed_footer(self, context, rule):
        commit = self.create_commit(context, "feat: add feature\n\nGenerated-by: Invalid Format")
        violations = rule.validate(commit)
        assert len(violations) == 1

    def test_multiple_ai_tools(self, context, rule):
        commit = self.create_commit(
            context,
            "feat: complex feature\n\nGenerated-by: ChatGPT <chatgpt@openai.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0

    def test_guidance_percentages(self, context, rule):
        commit = self.create_commit(
            context,
            "feat: add feature\n\nAssisted-by: GitHub Copilot <copilot@github.com>"
        )
        violations = rule.validate(commit)
        assert len(violations) == 0
