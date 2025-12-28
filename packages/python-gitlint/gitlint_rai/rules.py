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

    AI_ATTRIBUTION_VALUE_PATTERN = re.compile(r"^[^<]+ <[^>]+>$")
    TRAILER_PATTERN = re.compile(r"^([A-Za-z][\w-]*)\s*:\s*(.+)$")

    def _parse_trailers(self, message_body):
        if not message_body:
            return {}

        lines = message_body if isinstance(message_body, list) else message_body.split("\n")
        trailers = {}
        in_trailer_block = False
        trailer_lines = []

        for i in range(len(lines) - 1, -1, -1):
            line = lines[i].strip()
            if not line:
                if in_trailer_block:
                    break
                continue

            match = self.TRAILER_PATTERN.match(line)
            if match:
                in_trailer_block = True
                trailer_lines.insert(0, (match.group(1), match.group(2)))
            elif in_trailer_block:
                break

        for key, value in trailer_lines:
            normalized_key = key.lower()
            if normalized_key not in trailers:
                trailers[normalized_key] = []
            trailers[normalized_key].append(value.strip())

        return trailers

    def validate(self, commit):
        trailers = self._parse_trailers(commit.message.body)

        for key in self.AI_ATTRIBUTION_KEYS:
            normalized_key = key.lower()
            if normalized_key in trailers:
                for value in trailers[normalized_key]:
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
