VALID_COMMIT_MESSAGES = [
    "feat: add new feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>",
    "fix: resolve critical bug\n\nAssisted-by: Verdent AI <verdent@verdent.ai>",
    "refactor: improve code quality\n\nCo-authored-by: GitHub Copilot <copilot@github.com>",
    "chore: update dependencies\n\nCommit-generated-by: Claude AI <claude@anthropic.com>",
    "docs: update README\n\nSome description\n\nGenerated-by: ChatGPT <chatgpt@openai.com>",
    "perf: optimize database queries\n\ngenerated-by: GitHub Copilot <copilot@github.com>",
]

INVALID_COMMIT_MESSAGES = [
    "feat: add new feature",
    "fix: resolve bug\n\nSome footer without AI attribution",
    "chore: update deps\n\nInvalid-footer: Something",
    "docs: update\n\nGenerated-by: Invalid Format",
]
