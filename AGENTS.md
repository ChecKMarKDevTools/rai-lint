# Agent Operating Instructions

## Primary Goals

1. **Follow KISS and YAGNI Principles**: Keep implementations simple and avoid unnecessary features. Breaking changes during this prerelease patch-only development stage are not only permissible but encouraged. Do not indicate breaking changes in commits or changelogs until a stable release exists.

2. **Minimum Viable Product Focus**: Aim for the simplest working solution. Documentation should be concise and practical, not exhaustive. Avoid over-engineering for edge cases.

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

Use Release Please for automated versioning.

- On push to `main`, the action opens a Release PR ("proposed release").
- Only after that PR is merged, an actual GitHub Release and semantic tag are created.
- Monorepo outputs are path-prefixed (use bracket syntax: `steps.release.outputs['packages/node-commitlint--release_created']`).

### Token Policy

- No Personal Access Tokens (PAT) are used.
- Use `GITHUB_TOKEN` for Release Please operations and attaching artifacts.
- PyPI publishing uses Trusted Publishing (OIDC) — no `PYPI_TOKEN`.
- npm publishing uses Trusted Publishing (OIDC) — no `NPM_TOKEN`.

### Trusted Publishing (OIDC) — npm and PyPI

- permissions: `id-token: write` is required in workflows.
- npm: configure the package as a Trusted Publisher (link repo/branch); then `npm publish` works with OIDC.
- PyPI: enable Trusted Publishing for the project; then `gh-action-pypi-publish` works with OIDC.
- Attach artifacts to the GitHub Release (e.g., tarballs, wheels, SBOMs) for provenance and distribution.

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

- Prefer `uv` instead of `pip`

## Rules for Implementation

- Consider alternatives before starting work
- Always execute validation step before returning to the user, which means run `make ai-checks` to perform full environment cleanup, re-installation, and all validations; ensure it passes without failures
- Before returning final response to the user, look for the @commit subagent and follow rules to update the `commit.tmp` file and include valid attribution
