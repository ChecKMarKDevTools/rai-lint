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
pytest tests/ --cov=checkmark_rai_lint

black checkmark_rai_lint/
isort checkmark_rai_lint/
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
