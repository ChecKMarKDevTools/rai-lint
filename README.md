# CheckMarK RAI Lint

A dual-language commit-message validation framework designed to enforce consistent, AI-responsible development practices across repositories.

## Overview

CheckMarK RAI Lint introduces a standardized RAI (Responsible AI) footer rule that ensures every commit explicitly signals AI-assisted or AI-generated content under clearly documented guidelines.

The project is implemented as a monorepo containing two native packages:

- **Node/ESM plugin** for @commitlint (JavaScript and multi-language projects)
- **Python plugin** for Gitlint (Python ecosystems)

## Supported AI Attribution Formats

All commits must include one of the following Git trailer footers:

```
Co-authored-by: GitHub Copilot <copilot@github.com>
```
**Use when**: AI contributes 34-66% of the code

```
Assisted-by: Verdent AI <verdent@verdent.ai>
```
**Use when**: AI contributes up to 33% of the code

```
Generated-by: GitHub Copilot <copilot@github.com>
```
**Use when**: AI generates 67-100% of the code

```
Commit-generated-by: Claude AI <claude@anthropic.com>
```
**Use when**: AI only generated the commit message

All patterns are case-insensitive and follow the [Git trailer format](https://git-scm.com/docs/git-interpret-trailers).

## Installation

### Node.js / Commitlint

```bash
npm install --save-dev @checkmark/commitlint-plugin-rai
```

Configure in `commitlint.config.js`:

```javascript
export default {
  extends: ['@commitlint/config-conventional'],
  plugins: ['@checkmark/commitlint-plugin-rai'],
  rules: {
    'rai-footer-exists': [2, 'always'],
  },
};
```

### Python / Gitlint

```bash
pip install checkmark-rai-lint
```

Configure in `.gitlint`:

```ini
[general]
contrib = checkmark_rai_lint.rules.RaiFooterExists
```

## Hook Integration

### Lefthook

```yaml
commit-msg:
  commands:
    commitlint:
      run: npx commitlint --edit {1}
```

### Husky

```bash
npx husky add .husky/commit-msg 'npx commitlint --edit $1'
```

### pre-commit

```yaml
repos:
  - repo: local
    hooks:
      - id: gitlint
        name: gitlint
        entry: gitlint
        args: [--msg-filename]
        language: python
        stages: [commit-msg]
```

## Requirements

- **Node**: 16.0.0 or higher (tested up to 24.x)
- **Python**: 3.9 – 3.12

## Development

```bash
npm install
npm test
npm run lint
```

For Python:

```bash
pip install -e "packages/python-gitlint[dev]"
pytest packages/python-gitlint/tests
black packages/python-gitlint
isort packages/python-gitlint
```

## License

MIT
