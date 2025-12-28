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

    def _parse_trailers(self, message_body):
        # Top-level orchestration using small helpers to reduce complexity
        lines = self._normalize_lines(message_body)
        raw_trailer_lines = self._find_trailer_block(lines)

        trailers = {}
        for line in raw_trailer_lines:
            parsed = self._parse_trailer_line(line)
            if not parsed:
                continue
            key, value = parsed
            trailers.setdefault(key, []).append(value)

        return trailers

    def _normalize_lines(self, message_body):
        """Return message_body as a list of lines (may be empty)."""
        if not message_body:
            return []
        return message_body if isinstance(message_body, list) else message_body.split("\n")

    def _find_trailer_block(self, lines):
        """Return a list of trailer lines in correct order (top-down).

        Trailers are defined as an unbroken block of non-empty lines at the
        end of the message. This returns [] if no such block exists.
        """
        if not lines:
            return []

        last_non_empty = None
        for idx in range(len(lines) - 1, -1, -1):
            if lines[idx].strip():
                last_non_empty = idx
                break

        if last_non_empty is None:
            return []

        raw = []
        for idx in range(last_non_empty, -1, -1):
            line = lines[idx].strip()
            if not line:
                break
            raw.append(line)

        raw.reverse()
        return raw

    def _parse_trailer_line(self, line):
        """Parse a single trailer line into (normalized_key, value) or None.

        Conditions:
        - Must contain ':'
        - key and value must be non-empty after strip
        - key must start with an alphabetic character
        - key is normalized to lower-case
        """
        if ":" not in line:
            return None

        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if not key or not value:
            return None
        if not key[0].isalpha():
            return None

        return key.lower(), value

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
