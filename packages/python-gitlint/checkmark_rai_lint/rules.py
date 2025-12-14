import re

from gitlint.rules import CommitRule, RuleViolation


class RaiFooterExists(CommitRule):
    name = "rai-footer-exists"
    id = "UC1"
    target = "commit"

    AI_ATTRIBUTION_KEYS = {
        "Authored-by",
        "Commit-generated-by",
        "Assisted-by",
        "Co-authored-by",
        "Generated-by",
    }

    # Value must be: Name <email>
    # Use a safe regex to avoid ReDoS: Name (no <) <email (no >)>
    AI_ATTRIBUTION_VALUE_PATTERN = re.compile(r"^[^<]+ <[^>]+>$")

    def validate(self, commit):
        # gitlint >= 0.15.0 provides parsed trailers
        trailers = getattr(commit.message, "trailers", {})

        # Normalize trailers keys to lowercase for comparison
        normalized_trailers = {k.lower(): v for k, v in trailers.items()}

        for key in self.AI_ATTRIBUTION_KEYS:
            if key.lower() in normalized_trailers:
                for value in normalized_trailers[key.lower()]:
                    if self.AI_ATTRIBUTION_VALUE_PATTERN.match(value):
                        return []

        return [
            RuleViolation(
                self.id,
                "Commit message must include AI attribution footer:\n"
                '  1. "Authored-by: [Human] <contact>" - Human only, no AI\n'
                '  2. "Commit-generated-by: [AI Tool] <contact>" - Trivial AI (docs, commit msg, advice)\n'
                '  3. "Assisted-by: [AI Tool] <contact>" - AI helped, but primarily human code\n'
                '  4. "Co-authored-by: [AI Tool] <contact>" - Roughly 50/50 AI and human (40-60 leeway)\n'
                '  5. "Generated-by: [AI Tool] <contact>" - Majority of code was AI generated\n'
                "\n"
                "Examples:\n"
                '  - "Authored-by: Jane Doe <jane@example.com>"\n'
                '  - "Commit-generated-by: ChatGPT <chatgpt@openai.com>"\n'
                '  - "Assisted-by: GitHub Copilot <copilot@github.com>"\n'
                '  - "Co-authored-by: Verdent AI <verdent@verdent.ai>"\n'
                '  - "Generated-by: GitHub Copilot <copilot@github.com>"',
            )
        ]
