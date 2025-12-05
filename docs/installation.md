# Installation Guide

## Prerequisites

### For Node.js Projects

- Node.js >= 18.0.0
- npm or yarn
- Git repository

### For Python Projects

- Python >= 3.10, < 3.13
- uv
- Git repository

## Node.js Installation

### 1. Install the Plugin

```bash
npm install --save-dev @checkmarkdevtools/commitlint-plugin-rai @commitlint/cli @commitlint/config-conventional
```

### 2. Configure Commitlint

Create or update `commitlint.config.js` in your project root:

```javascript
export default {
  extends: ['@commitlint/config-conventional'],
  plugins: ['@checkmarkdevtools/commitlint-plugin-rai'],
  rules: {
    'ai-attribution-exists': [2, 'always'],
  },
};
```

### 3. Set Up Git Hooks

#### Option A: Lefthook (Recommended)

Install Lefthook:

```bash
npm install --save-dev lefthook
```

Create `lefthook.yml`:

```yaml
commit-msg:
  commands:
    commitlint:
      run: npx commitlint --edit {1}
```

Install hooks:

```bash
npx lefthook install
```

#### Option B: Husky

Install Husky:

```bash
npm install --save-dev husky
npx husky install
```

Add commit-msg hook:

```bash
npx husky add .husky/commit-msg 'npx commitlint --edit $1'
```

## Python Installation

### 1. Install the Plugin

```bash
uv add checkmarkdevtools-gitlint-plugin-rai
```

For development:

```bash
uv add checkmarkdevtools-gitlint-plugin-rai --dev
```

### 2. Configure Gitlint

Create or update `.gitlint` in your project root:

```ini
[general]
contrib = checkmark_rai_lint.rules.RaiFooterExists
```

### 3. Set Up Git Hooks

#### Option A: pre-commit (Recommended)

Install pre-commit:

```bash
uv add pre-commit
```

Create `.pre-commit-config.yaml`:

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

Install hooks:

```bash
pre-commit install --hook-type commit-msg
```

#### Option B: Manual Git Hook

Create `.git/hooks/commit-msg`:

```bash
#!/bin/sh
gitlint --msg-filename="$1"
```

Make it executable:

```bash
chmod +x .git/hooks/commit-msg
```

## Verification

Test your setup with a valid commit:

```bash
git commit -m "test: verify RAI lint setup

Assisted-by: GitHub Copilot <copilot@github.com>"
```

This should succeed. Try an invalid commit:

```bash
git commit -m "test: this should fail"
```

This should be rejected with an error message.

## Troubleshooting

### Node.js Issues

**Problem**: `Module not found: @checkmarkdevtools/commitlint-plugin-rai`

**Solution**: Ensure the package is installed and listed in `package.json` devDependencies.

**Problem**: Commitlint not running on commit

**Solution**: Verify hooks are installed:

```bash
ls -la .git/hooks/commit-msg
```

### Python Issues

**Problem**: `ImportError: No module named 'checkmark_rai_lint'`

**Solution**: Reinstall the package:

```bash
uv add --reinstall checkmarkdevtools-gitlint-plugin-rai
```

**Problem**: Gitlint not finding the rule

**Solution**: Check `.gitlint` configuration and ensure the contrib path is correct:

```bash
gitlint --debug
```

## Multi-Language Projects

For projects using both Node.js and Python, you can run both validators:

### Lefthook Configuration

```yaml
commit-msg:
  commands:
    commitlint:
      run: npx commitlint --edit {1}
    gitlint:
      run: gitlint --msg-filename {1}
```

### pre-commit Configuration

```yaml
repos:
  - repo: local
    hooks:
      - id: commitlint
        name: commitlint
        entry: npx commitlint --edit
        language: system
        stages: [commit-msg]

      - id: gitlint
        name: gitlint
        entry: gitlint
        args: [--msg-filename]
        language: python
        stages: [commit-msg]
```
