# checkmark-rai-lint

Gitlint plugin for enforcing AI attribution in commit messages using standard Git trailers.

## Installation

```bash
pip install checkmark-rai-lint
```

## Usage

Add to your `.gitlint`:

```ini
[general]
contrib = checkmark_rai_lint.rules.RaiFooterExists
```

## Valid Footer Formats

1. **`Authored-by: [Human] <email>`** - Human only, no AI
2. **`Commit-generated-by: [AI Tool] <email>`** - Trivial AI (docs, commit msg, advice, reviews)
3. **`Assisted-by: [AI Tool] <email>`** - AI helped, but primarily human code
4. **`Co-authored-by: [AI Tool] <email>`** - Roughly 50/50 AI and human (40-60 leeway)
5. **`Generated-by: [AI Tool] <email>`** - Majority of code was AI generated

All patterns are case-insensitive.

## Requirements

- Python >= 3.9, < 3.13
- gitlint >= 0.19.0

## Development

```bash
pip install -e ".[dev]"
pytest tests/
black checkmark_rai_lint/
isort checkmark_rai_lint/
```

## License

Polyform Shield 1.0.0
