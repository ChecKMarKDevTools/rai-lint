# checkmarkdevtools-gitlint-plugin-rai

Gitlint plugin for enforcing AI attribution in commit messages using standard Git trailers.

## Installation

```bash
uv add checkmarkdevtools-gitlint-plugin-rai
```

## Usage

Install the plugin via uv:

```bash
uv add checkmarkdevtools-gitlint-plugin-rai
```

The plugin will be auto-discovered by gitlint (>=0.19.1) via entry points. No additional configuration is required in your `.gitlint` file. To verify the rule is loaded, run:

```bash
gitlint --list-rules | grep rai-footer-exists
```

If auto-discovery is not working in your environment, configure gitlint to explicitly load the plugin:

```ini
[general]
extra-paths = /path/to/site-packages
```

Then list and validate rules as above.

## Valid Footer Formats

1. **`Authored-by: [Human] <email>`** - Human only, no AI involvement
2. **`Commit-generated-by: [AI Tool] <email>`** - Trivial AI (docs, commit msg, reviews, advice, etc)
3. **`Assisted-by: [AI Tool] <email>`** - AI helped, but primarily human code
4. **`Co-authored-by: [AI Tool] <email>`** - Roughly half is AI generated and half human-authored content
5. **`Generated-by: [AI Tool] <email>`** - Majority of code was AI generated

All patterns are case-insensitive.

## Requirements

- Python >= 3.10, < 3.13
- gitlint >= 0.19.1

## Development

```bash
uv sync --locked --group dev
make test
make lint
make test-coverage
```

## License

Polyform Shield 1.0.0
