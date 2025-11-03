# Technology Stack & Build System

## Architecture

**Monorepo Structure**: Dual-language implementation with shared tooling and documentation.

## Node.js Package (`packages/node-commitlint/`)

### Tech Stack
- **Language**: TypeScript 5.3+ with strict mode
- **Module System**: ESM (ES2022 target)
- **Runtime**: Node.js 16.0.0+ (tested up to 24.x)
- **Testing**: Vitest
- **Build**: TypeScript compiler (tsc)

### Code Quality
- **Linting**: ESLint with Airbnb base config + TypeScript rules
- **Formatting**: Prettier (120 char line length, single quotes, trailing commas)
- **Type Checking**: Strict TypeScript with declaration generation

### Dependencies
- **Peer**: @commitlint/types ^19.0.0
- **Dev**: TypeScript, Vitest, ESLint plugins

## Python Package (`packages/python-gitlint/`)

### Tech Stack
- **Language**: Python 3.9-3.12
- **Package Manager**: pip with setuptools
- **Testing**: Pytest
- **Dependencies**: gitlint >=0.19.0

### Code Quality
- **Formatting**: Black (100 char line length)
- **Import Sorting**: isort (black profile)
- **Testing**: Pytest with standard discovery

## Common Commands

### Development Setup
```bash
# Full setup (installs both Node and Python deps)
bash setup.sh

# Manual Node setup
npm install
cd packages/node-commitlint && npm run build

# Manual Python setup
pip install -e "packages/python-gitlint[dev]"
```

### Testing
```bash
# All tests
make test

# Language-specific
make test-node    # Vitest
make test-python  # Pytest
```

### Code Quality
```bash
# All linting and formatting
make validate

# Linting only
make lint         # ESLint + Black/isort check
make lint-node    # ESLint only
make lint-python  # Black + isort check only

# Formatting
make format       # Prettier + Black + isort
make format-node  # Prettier only
make format-python # Black + isort only
```

### Building
```bash
make build        # TypeScript compilation
make build-node   # Same as above
```

### Cleanup
```bash
make clean        # Remove all build artifacts and caches
```

## CI/CD

### GitHub Actions Matrix
- **Node.js**: 16, 18, 20, 24
- **Python**: 3.9, 3.10, 3.11, 3.12
- **OS**: Ubuntu Linux

### Workflows
- `ci.yml`: Multi-version testing matrix
- `quality.yml`: Linting, formatting, type checking
- `release.yml`: Release automation (dry-run)
- `dependency-review.yml`: Security scanning

## Package Configuration

### Node.js ESM Requirements
- `"type": "module"` in package.json
- ESM exports with TypeScript declarations
- ES2022 target for modern Node.js features

### Python Packaging
- setuptools with pyproject.toml
- Optional dev dependencies for testing/formatting
- Gitlint contrib rule architecture