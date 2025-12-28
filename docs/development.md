# Development Setup

Quick start guide for developers working on CheckMarK RAI Lint.

## Quick Setup

```bash
bash setup.sh
```

This will:

1. Install Node.js dependencies
2. Create Python virtual environment
3. Install Python dependencies
4. Build the Node.js package
5. Run all tests

## Manual Setup

### Node.js Setup

```bash
npm install
cd packages/node-commitlint
npm run build
npm test
```

### Python Setup

```bash
cd packages/python-gitlint
uv sync --locked --group dev
uv run pytest tests
```

## Development Workflow

### Node.js Development

```bash
cd packages/node-commitlint

npm test
npm run test:watch
npm run build
npm run lint
```

### Python Development

```bash
source .venv/bin/activate
cd packages/python-gitlint

pytest tests/ -v
pytest tests/ --cov=gitlint_rai

black gitlint_rai/
isort gitlint_rai/
```

## Running Benchmarks

```bash
npm test benchmarks/
python benchmarks/python_benchmark.py
```

## Installing Git Hooks

```bash
npx lefthook install
```

## Testing Your Changes

### Unit Tests

```bash
npm test
pytest packages/python-gitlint/tests
```

### Integration Tests

```bash
cd packages/node-commitlint
npm test src/integration.test.ts

cd packages/python-gitlint
pytest tests/test_integration.py
```

### Manual Testing

Create a test commit:

```bash
git commit -m "test: manual verification

Testing the RAI lint implementation.

Assisted-by: GitHub Copilot <copilot@github.com>"
```

## Local Package Testing

To test your changes by building and installing the packages locally, follow these
steps. This allows you to verify that the packages work correctly in a real
environment before publishing.

### Node.js Package (using Volta)

1. **Build the package:**

   ```bash
   cd packages/node-commitlint
   volta run npm run build
   ```

2. **Package the build:**

   ```bash
   volta run npm pack
   ```

   This creates a tarball file like `rai-plugin-0.0.0.tgz`.

3. **Install locally in a test project:**

   In a separate test directory (not this repo), create a new project or use an
   existing one:

   ```bash
   mkdir test-project && cd test-project
   volta run npm init -y
   volta run npm install <path-to-tarball>
   ```

   Replace `<path-to-tarball>` with the actual path to the generated tarball file.

4. **Configure and test:**

   Create a `commitlint.config.js` in your test project:

   ```javascript
   export default {
     extends: ['@commitlint/config-conventional'],
     plugins: ['@checkmarkdevtools/commitlint-plugin-rai'],
     rules: {
       'rai-footer-exists': [2, 'always'],
     },
   };
   ```

   Test with a commit:

   ```bash
   git add .
   git commit -m "test: local package test

   Assisted-by: GitHub Copilot <copilot@github.com>"
   ```

5. **Remove the local package:**

   ```bash
   volta run npm uninstall @checkmarkdevtools/commitlint-plugin-rai
   ```

### Python Package (using uv)

1. **Build the package:**

   ```bash
   cd packages/python-gitlint
   uv build
   ```

   This creates distribution files in the `dist/` directory (e.g., `.whl` and `.tar.gz`).

2. **Install locally in a test environment:**

   In a separate test directory (not this repo), create a new virtual environment:

   ```bash
   mkdir test-project && cd test-project
   uv init
   uv add gitlint  # or any other dependencies
   uv pip install <path-to-wheel>
   ```

   Replace `<path-to-wheel>` with the actual path to the generated wheel file.

3. **Configure and test:**

   Create a `.gitlint` file in your test project:

   ```ini
   [general]
   contrib = gitlint_rai.rules.RaiFooterExists
   ```

   Test with a commit:

   ```bash
   git add .
   git commit -m "test: local package test

   Assisted-by: GitHub Copilot <copilot@github.com>"
   ```

4. **Remove the local package:**

   ```bash
   uv pip uninstall checkmarkdevtools-gitlint-plugin-rai
   ```

## VS Code Setup

Open the workspace file:

```bash
code rai-lint.code-workspace
```

Recommended extensions will be suggested automatically.

## Troubleshooting Setup

### Node.js Issues

```bash
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

### Python Issues

```bash
cd packages/python-gitlint
uv sync --locked --group dev
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for full contribution guidelines.
