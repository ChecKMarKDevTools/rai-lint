import re
from gitlint.rules import CommitRule, RuleViolation


class RaiFooterExists(CommitRule):
    name = "rai-footer-exists"
    id = "UC1"
    target = "commit"

    AI_ATTRIBUTION_PATTERNS = [
        re.compile(r"^Authored-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^Commit-generated-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^Assisted-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^Co-authored-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^Generated-by:\s+.+\s+<.+@.+>$", re.IGNORECASE | re.MULTILINE),
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
                    '  1. "Authored-by: [Human] <email>" - Human only, no AI\n'
                    '  2. "Commit-generated-by: [AI Tool] <email>" - Trivial AI (docs, commit msg, advice)\n'
                    '  3. "Assisted-by: [AI Tool] <email>" - AI helped, but primarily human code\n'
                    '  4. "Co-authored-by: [AI Tool] <email>" - Roughly 50/50 AI and human (40-60 leeway)\n'
                    '  5. "Generated-by: [AI Tool] <email>" - Majority of code was AI generated\n'
                    '\n'
                    'Examples:\n'
                    '  - "Authored-by: Jane Doe <jane@example.com>"\n'
                    '  - "Commit-generated-by: ChatGPT <chatgpt@openai.com>"\n'
                    '  - "Assisted-by: GitHub Copilot <copilot@github.com>"\n'
                    '  - "Co-authored-by: Verdent AI <verdent@verdent.ai>"\n'
                    '  - "Generated-by: GitHub Copilot <copilot@github.com>"',
                )
            ]

        return []
