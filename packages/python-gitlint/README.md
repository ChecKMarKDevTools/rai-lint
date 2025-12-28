# gitlint-rai

Gitlint plugin for enforcing AI attribution in commit messages using Git commit message trailers.

## Installation

```bash
pip install gitlint-rai
```

or with uv:

```bash
uv add gitlint-rai
```

## Usage

After installation, configure gitlint to load the plugin:

**`.gitlint` file:**

```ini
[general]
contrib = gitlint_rai.rules.RaiFooterExists
```

Verify the rule is loaded:

```bash
gitlint --list-rules | grep rai-footer-exists
```

You should see:

```
rai-footer-exists  Commit message must include a valid RAI footer
```

## Valid Footer Formats

1. **`Authored-by: [Human] <email>`** - Human only, no AI involvement
2. **`Commit-generated-by: [AI Tool] <email>`** - Trivial AI (docs, commit msg, reviews, advice, etc)
3. **`Assisted-by: [AI Tool] <email>`** - AI helped, but primarily human code
4. **`Co-authored-by: [AI Tool] <email>`** - Roughly half is AI generated and half human-authored content
5. **`Generated-by: [AI Tool] <email>`** - Majority of code was AI generated

All patterns are case-insensitive.

## Requirements

- Python >= 3.11, < 3.13
- gitlint >= 0.19.1

## License

PolyForm Shield License 1.0.0
