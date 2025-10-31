# Contributing to CheckMarK RAI Lint

Thank you for your interest in contributing to CheckMarK RAI Lint!

## RAI Attribution Policy

All commits to this repository must include an RAI footer indicating AI involvement:

- Use `🛡️ RAI: AI-Generated` when AI generated the entire commit
- Use `🛡️ RAI: AI-Assisted` when AI helped but you made the final decisions
- Use `Generated-by: Verdent AI <verdent@verdent.ai>` for Verdent AI contributions

## Development Setup

### Node.js Development

```bash
npm install
cd packages/node-commitlint
npm test
npm run lint
```

### Python Development

```bash
pip install -e "packages/python-gitlint[dev]"
cd packages/python-gitlint
pytest tests/
black checkmark_rai_lint/
isort checkmark_rai_lint/
```

## Running Tests

### Node.js Tests

```bash
cd packages/node-commitlint
npm test
npm run test:watch
```

### Python Tests

```bash
cd packages/python-gitlint
pytest tests/ -v
pytest tests/ --cov=checkmark_rai_lint
```

## Code Style

### Node.js

- Follow Airbnb JavaScript Style Guide
- Use ESLint for linting: `npm run lint`
- Format with Prettier: `npm run format`

### Python

- Follow PEP 8
- Use Black for formatting (line length: 100)
- Use isort for import sorting
- Run all checks before committing

## Commit Message Format

Follow Conventional Commits specification:

```
<type>(<scope>): <subject>

<body>

<footer>

<rai-footer>
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Commit with proper RAI footer
6. Push to your fork
7. Open a pull request

## Testing Requirements

- All new features must include tests
- Maintain or improve code coverage
- Tests must pass in CI across all Node/Python versions

## Documentation

- Update relevant documentation for new features
- Add examples for new functionality
- Keep architecture diagrams current

## Questions?

Open an issue for any questions or concerns.
