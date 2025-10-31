# checkmark-rai-lint

Gitlint plugin for enforcing RAI (Responsible AI) footer validation in commit messages.

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

- `🛡️ RAI: AI-Generated`
- `🛡️ RAI: AI-Assisted`
- `Generated-by: Verdent AI <verdent@verdent.ai>`

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

MIT
