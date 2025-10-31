# Contributing to CheckMarK RAI Lint

Thank you for your interest in contributing to CheckMarK RAI Lint!

## AI Attribution Policy

All commits to this repository must include an AI attribution footer using standard Git trailer format:

- `Co-authored-by: [AI Tool] <email>` - Roughly 34-66% AI contribution
- `Assisted-by: [AI Tool] <email>` - Minimal AI contribution
- `Generated-by: [AI Tool] <email>` - Roughly 67-100% AI contribution
- `Commit-generated-by: [AI Tool] <email>` - AI-generated commit message only
- `Authored-by: [Human] <email>` - Human author attribution

**Note**: Percentages are guidance to help you choose, not strict requirements. Use your judgment.

Examples:
```
Generated-by: GitHub Copilot <copilot@github.com>
Assisted-by: Verdent AI <verdent@verdent.ai>
Co-authored-by: Claude AI <claude@anthropic.com>
Authored-by: Jane Doe <jane@example.com>
```

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
