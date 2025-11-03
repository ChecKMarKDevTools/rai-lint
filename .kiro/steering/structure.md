# Project Structure & Organization

## Monorepo Layout

```
rai-lint/
├── packages/                    # Core implementations
│   ├── node-commitlint/        # TypeScript/Node.js package
│   └── python-gitlint/         # Python package
├── docs/                       # Comprehensive documentation
├── examples/                   # Integration examples & configs
├── fixtures/                   # Shared test data
├── benchmarks/                 # Performance tests
├── .github/                    # CI/CD workflows & templates
├── .kiro/                      # Kiro steering rules
└── .vscode/                    # VS Code workspace config
```

## Package Structure

### Node.js Package (`packages/node-commitlint/`)
```
node-commitlint/
├── src/
│   ├── index.ts               # Main plugin export
│   ├── rules/                 # Commitlint rule implementations
│   │   ├── rai-footer-exists.ts
│   │   └── rai-footer-exists.test.ts
│   └── integration.test.ts    # End-to-end tests
├── dist/                      # TypeScript build output
├── package.json               # ESM package config
├── tsconfig.json              # TypeScript config
├── vitest.config.ts           # Test configuration
└── README.md                  # Package-specific docs
```

### Python Package (`packages/python-gitlint/`)
```
python-gitlint/
├── checkmark_rai_lint/        # Python package
│   ├── __init__.py
│   └── rules.py               # Gitlint rule implementations
├── tests/
│   ├── test_rules.py          # Unit tests
│   └── test_integration.py    # Integration tests
├── pyproject.toml             # Python package config
├── .gitlint                   # Gitlint config for testing
└── README.md                  # Package-specific docs
```

## Shared Resources

### Documentation (`docs/`)
- `architecture.md` - System design with Mermaid diagrams
- `installation.md` - Setup guides for both languages
- `usage.md` - Usage examples and integration
- `api-reference.md` - API documentation
- `troubleshooting.md` - Common issues and solutions
- `development.md` - Development setup and contribution guide

### Examples (`examples/`)
- Git hook configurations (Lefthook, Husky, pre-commit)
- Commitlint configs (strict, warning modes)
- Gitlint configurations

### Test Data (`fixtures/`)
- `commit-messages.ts` - TypeScript test fixtures
- `commit_messages.py` - Python test fixtures
- Shared between both implementations for consistency

### Benchmarks (`benchmarks/`)
- `node-benchmark.test.ts` - Node.js performance tests
- `python_benchmark.py` - Python performance tests

## Configuration Files

### Root Level
- `package.json` - Monorepo workspace configuration
- `pyproject.toml` - Python project metadata and tool configs
- `Makefile` - Build automation and common commands
- `commitlint.config.js` - Project's own commit validation
- `.eslintrc.json` - ESLint configuration (Airbnb + TypeScript)
- `.prettierrc` - Code formatting rules

### CI/CD (`.github/`)
```
.github/
├── workflows/
│   ├── ci.yml                 # Multi-version testing matrix
│   ├── quality.yml            # Code quality checks
│   ├── release.yml            # Release automation
│   └── dependency-review.yml  # Security scanning
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   └── feature_request.md
└── PULL_REQUEST_TEMPLATE.md
```

## Naming Conventions

### Files & Directories
- **Kebab-case**: For file names (`rai-footer-exists.ts`)
- **Snake_case**: For Python modules (`checkmark_rai_lint`)
- **PascalCase**: For TypeScript classes and interfaces
- **camelCase**: For TypeScript functions and variables

### Packages
- **Node.js**: `@checkmark/commitlint-plugin-rai`
- **Python**: `checkmark-rai-lint`

### Git Branches
- `main` - Production branch
- `feature/description` - Feature branches
- `fix/description` - Bug fix branches
- `docs/description` - Documentation updates

## Import/Export Patterns

### TypeScript (ESM)
```typescript
// Named exports preferred
export { raiFooterExists } from './rules/rai-footer-exists.js';

// Default export for main plugin
export default { rules: { 'rai-footer-exists': raiFooterExists } };
```

### Python
```python
# Standard Python imports
from .rules import RaiFooterExists

# Gitlint contrib pattern
__all__ = ['RaiFooterExists']
```

## Testing Organization

### Test File Naming
- **Node.js**: `*.test.ts` (co-located with source)
- **Python**: `test_*.py` (in separate `tests/` directory)

### Test Categories
- **Unit Tests**: Individual rule validation logic
- **Integration Tests**: End-to-end CLI workflows
- **Benchmarks**: Performance and memory usage

## Build Artifacts

### Generated Files (Ignored by Git)
- `packages/node-commitlint/dist/` - TypeScript compilation output
- `packages/python-gitlint/build/` - Python build artifacts
- `node_modules/` - Node.js dependencies
- `__pycache__/` - Python bytecode cache
- `.pytest_cache/` - Pytest cache