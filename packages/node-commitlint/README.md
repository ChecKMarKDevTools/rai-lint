# @checkmarkdevtools/commitlint-plugin-rai

Commitlint plugin for enforcing AI attribution in commit messages using standard Git trailers.

## Installation

```bash
npm install --save-dev @checkmarkdevtools/commitlint-plugin-rai
```

## Usage

Add to your `commitlint.config.js`:

```javascript
export default {
  extends: ['@commitlint/config-conventional'],
  plugins: ['@checkmarkdevtools/commitlint-plugin-rai'],
  rules: {
    'rai-footer-exists': [2, 'always'],
  },
};
```

## Valid Footer Formats

1. **`Authored-by: [Human] <email>`** - Human only, no AI
2. **`Commit-generated-by: [AI Tool] <email>`** - Trivial AI (docs, commit msg, advice, reviews)
3. **`Assisted-by: [AI Tool] <email>`** - AI helped, but primarily human code
4. **`Co-authored-by: [AI Tool] <email>`** - Roughly 50/50 AI and human (40-60 leeway)
5. **`Generated-by: [AI Tool] <email>`** - Majority of code was AI generated

All patterns are case-insensitive.

## Requirements

- Node.js >= 20.0.0
- @commitlint/cli >= 19.0.0

## License

PolyForm Shield License 1.0.0
