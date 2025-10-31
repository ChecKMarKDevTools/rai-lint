# @checkmark/commitlint-plugin-rai

Commitlint plugin for enforcing RAI (Responsible AI) footer validation in commit messages.

## Installation

```bash
npm install --save-dev @checkmark/commitlint-plugin-rai
```

## Usage

Add to your `commitlint.config.js`:

```javascript
export default {
  extends: ['@commitlint/config-conventional'],
  plugins: ['@checkmark/commitlint-plugin-rai'],
  rules: {
    'rai-footer-exists': [2, 'always'],
  },
};
```

## Valid Footer Formats

- `🛡️ RAI: AI-Generated`
- `🛡️ RAI: AI-Assisted`
- `Generated-by: Verdent AI <verdent@verdent.ai>`

All patterns are case-insensitive.

## Requirements

- Node.js >= 16.0.0
- @commitlint/cli >= 19.0.0

## License

MIT
