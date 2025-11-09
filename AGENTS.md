# Agent Operating Instructions

## AI Attribution Footer

When committing changes in this project, I must include one of these five footer formats:

1. `Authored-by: [Human] <email>` - When human did all the work, no AI involved
2. `Commit-generated-by: [AI Tool] <email>` - For trivial AI work (docs, messages, advice only)
3. `Assisted-by: [AI Tool] <email>` - When AI helped but human did the primary work
4. `Co-authored-by: [AI Tool] <email>` - When AI/human split work 50/50 (40-60 leeway)
5. `Generated-by: [AI Tool] <email>` - When AI generated the majority of the commit

The commitlint rule enforces this via regex patterns (case-insensitive). All commits without a valid footer are rejected.

**Default:** Use `Generated-by: Verdent AI <verdent@verdent.ai>` for code I generate.

## Release Process

The project currently uses a manual release workflow (`.github/workflows/release.yml`). This is **not ideal** but is the current system:

- Manual `workflow_dispatch` trigger required
- Manual version input (semver format)
- Manual release-type selection (patch/minor/major)
- Separate workflows for Node.js (NPM) and Python (PyPI) packages
- Dry-run publishing (not actual releases)

## Custom Commitlint Plugin

The AI attribution validation is currently defined inline in `commitlint.config.js` (lines 7-32). This rule is not installed as an npm package—it's embedded in the config file. This is temporary and should be extracted to a proper package if used across projects.

## Project Structure

- `/packages/node-commitlint` - Node.js/ESM commitlint plugin
- `/packages/python-gitlint` - Python gitlint plugin
- Monorepo with separate versioning per package

## Environment Variables

Monorepo uses isolated virtual environments per package—**NEVER** install globally:

**.env** (root level, gitignored)
- Contains shared secrets: `NPM_TOKEN`, `PYPI_TOKEN` for release workflows

**Node.js Environment** (`/packages/node-commitlint`)
- Use `node_modules/.bin` or `npx` (do not use global npm)
- Install with `npm ci` or `npm install` in package directory only
- Never install to global npm registry or modify system node_modules

**Python Environment** (`/packages/python-gitlint`)
- Create isolated venv: `python3 -m venv venv`
- Activate: `source venv/bin/activate`
- Install with `pip install -e ".[dev]"` within venv only
- **NEVER** use `pip install --global-site-packages` or install to system Python
- Use `.env.python` for package-specific vars if needed

Both packages must have zero impact on global pyenv or npm installations.
