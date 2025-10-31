import re
from gitlint.rules import CommitRule, RuleViolation

class RaiFooterExists(CommitRule):
    name = "rai-footer-exists"
    id = "UC1"
    target = "commit"

    RAI_FOOTER_PATTERNS = [
        re.compile(r"^🛡️\s+RAI:\s+AI-Generated$", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^🛡️\s+RAI:\s+AI-Assisted$", re.IGNORECASE | re.MULTILINE),
        re.compile(
            r"^Generated-by:\s+Verdent AI\s+<verdent@verdent\.ai>$",
            re.IGNORECASE | re.MULTILINE,
        ),
    ]

    def validate(self, commit):
        message = commit.message.full

        has_valid_footer = any(pattern.search(message) for pattern in self.RAI_FOOTER_PATTERNS)

        if not has_valid_footer:
            return [
                RuleViolation(
                    self.id,
                    'Commit message must include a valid RAI footer:\n'
                    '  - "🛡️ RAI: AI-Generated"\n'
                    '  - "🛡️ RAI: AI-Assisted"\n'
                    '  - "Generated-by: Verdent AI <verdent@verdent.ai>"',
                )
            ]

        return []
