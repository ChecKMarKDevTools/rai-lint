import re
from gitlint.rules import CommitRule, RuleViolation


class RaiFooterExists(CommitRule):
    name = "rai-footer-exists"
    id = "UC1"
    target = "commit"

    AI_ATTRIBUTION_PATTERNS = [
        re.compile(r"^Co-authored-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^Assisted-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^Generated-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^Commit-generated-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^Authored-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
    ]

    def validate(self, commit):
        message = commit.message.full

        has_valid_footer = any(
            pattern.search(message) for pattern in self.AI_ATTRIBUTION_PATTERNS
        )

        if not has_valid_footer:
            return [
                RuleViolation(
                    self.id,
                    'Commit message must include AI attribution footer:\n'
                    '  - "Co-authored-by: [AI Tool] <email>" (~34-66% AI contribution)\n'
                    '  - "Assisted-by: [AI Tool] <email>" (~minimal AI contribution)\n'
                    '  - "Generated-by: [AI Tool] <email>" (~67-100% AI contribution)\n'
                    '  - "Commit-generated-by: [AI Tool] <email>" (AI-generated commit message only)\n'
                    '  - "Authored-by: [Human] <email>" (human author attribution)\n'
                    '\n'
                    'Note: Percentages are guidance, not strict requirements.\n'
                    '\n'
                    'Examples:\n'
                    '  - "Generated-by: GitHub Copilot <copilot@github.com>"\n'
                    '  - "Assisted-by: Verdent AI <verdent@verdent.ai>"\n'
                    '  - "Authored-by: Jane Doe <jane@example.com>"',
                )
            ]

        return []
