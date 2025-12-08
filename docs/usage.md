# Usage Guide

## Valid RAI Footer Formats

CheckMarK RAI Lint accepts five footer formats. All patterns are **case-insensitive**.

### 1. Authored-by Footer

Use when the work was done entirely by a human with no AI involvement:

```
feat: implement user authentication

Add JWT-based authentication with refresh tokens and secure session management.

Authored-by: Jane Doe <jane@example.com>
```

### 2. Commit-generated-by Footer

Use when AI contributed only trivially (docs, messages, advice - not code):

```
docs: update README installation instructions

Improved clarity and added troubleshooting section.

Commit-generated-by: GitHub Copilot <copilot@github.com>
```

### 3. Assisted-by Footer

Use when AI helped but the work was primarily human-driven:

```
fix: resolve race condition in payment processing

Added mutex locks to prevent concurrent payment processing issues.

Assisted-by: GitHub Copilot <copilot@github.com>
```

### 4. Co-authored-by Footer

Use when AI and human contributed roughly equally (40-60 range):

```
feat: add data validation pipeline

Implemented validation logic with custom rules and error handling.

Co-authored-by: GitHub Copilot <copilot@github.com>
```

### 5. Generated-by Footer

Use when the majority of the work was AI-generated:

```
chore: update dependencies to latest versions

Updated all npm packages to latest compatible versions.

Generated-by: GitHub Copilot <copilot@github.com>
```

## Commit Message Structure

RAI footers should be placed at the end of the commit message, after the description and any other footers:

```
<type>(<scope>): <subject>

<body>

<other-footers>

<rai-footer>
```

Example with multiple footers:

```
feat(auth): add OAuth2 integration

Implemented OAuth2 authentication flow with Google and GitHub providers.
Added automatic account linking for existing users.

BREAKING CHANGE: Removed legacy session-based authentication
Closes #123
Assisted-by: GitHub Copilot <copilot@github.com>
```

## CLI Usage

### Node.js / Commitlint

Test commit message from stdin:

```bash
echo "feat: add feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>" | npx commitlint
```

Validate last commit:

```bash
npx commitlint --from HEAD~1
```

Validate specific commit:

```bash
npx commitlint --from abc123f
```

Validate range:

```bash
npx commitlint --from main --to develop
```

### Python / Gitlint

Lint last commit:

```bash
gitlint
```

Lint specific commit:

```bash
gitlint --commit abc123f
```

Lint commit message from file:

```bash
gitlint --msg-filename .git/COMMIT_EDITMSG
```

Test message from stdin:

```bash
echo "feat: add feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>" | gitlint
```

## IDE Integration

### VS Code

Install the Conventional Commits extension and add this to `.vscode/settings.json`:

```json
{
  "conventionalCommits.autoCommit": false,
  "conventionalCommits.promptFooter": true,
  "conventionalCommits.footerPrefix": "Assisted-by: ",
  "conventionalCommits.footerType": [
    "Authored-by: [Human] <email@example.com>",
    "Commit-generated-by: [AI Tool] <email@example.com>",
    "Assisted-by: GitHub Copilot <copilot@github.com>",
    "Co-authored-by: GitHub Copilot <copilot@github.com>",
    "Generated-by: GitHub Copilot <copilot@github.com>"
  ]
}
```

### JetBrains IDEs

Configure commit template in Settings → Version Control → Commit:

```
<type>(<scope>): <subject>

<body>

Assisted-by: GitHub Copilot <copilot@github.com>
```

## CI/CD Integration

### GitHub Actions

Add validation to your workflow:

```yaml
name: Lint Commits

on: [push, pull_request]

jobs:
  commitlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v6
        with:
          node-version: 20

      - run: npm ci

      - run: npx commitlint --from ${{ github.event.pull_request.base.sha }} --to ${{ github.sha }}
```

### GitLab CI

```yaml
commitlint:
  stage: test
  image: node:20
  script:
    - npm ci
    - npx commitlint --from $CI_MERGE_REQUEST_TARGET_BRANCH_SHA --to HEAD
  only:
    - merge_requests
```

### Jenkins

```groovy
stage('Commit Lint') {
  steps {
    sh 'npm ci'
    sh 'npx commitlint --from origin/main --to HEAD'
  }
}
```

## Best Practices

### 1. Choose the Right Footer

- **Authored-by**: Human only, no AI involvement
- **Commit-generated-by**: Trivial AI work (docs, messages, advice)
- **Assisted-by**: AI helped, but primarily human work
- **Co-authored-by**: Roughly 50/50 AI and human contribution
- **Generated-by**: Majority AI-generated content

### 2. Be Consistent

Use the same footer format across your team/organization for consistency.

### 3. Automate Footer Addition

Create Git aliases to automatically add footers:

```bash
git config alias.cai '!git commit -e -m "$(cat)" -m "" -m "Assisted-by: GitHub Copilot <copilot@github.com>"'
```

Usage:

```bash
echo "feat: add new feature" | git cai
```

## 4. AI Attribution Policy

All commits must include an RAI footer:

```markdown
- Use `Authored-by: [Name] <email>` when no AI was involved
- Use `Commit-generated-by: [AI Tool] <email>` for trivial AI help (docs, messages)
- Use `Assisted-by: [AI Tool] <email>` when AI helped but you did primary work
- Use `Co-authored-by: [AI Tool] <email>` when AI and human contributed equally
- Use `Generated-by: [AI Tool] <email>` when AI generated most of the commit
```

## Common Issues

### Footer Not Detected

**Problem**: Commit rejected even with footer present

**Solutions**:

1. Check for extra whitespace around the footer
2. Ensure footer is on its own line
3. Verify the footer keyword is spelled correctly
4. Check for typos in the email format

### Multiple Footers

**Problem**: Can I include multiple RAI footers?

**Answer**: No, only one RAI footer is needed per commit. Choose the most accurate one.

### Amending Commits

To add footer to previous commit:

```bash
git commit --amend -m "$(git log -1 --pretty=%B)" -m "" -m "Assisted-by: GitHub Copilot <copilot@github.com>"
```

> [!WARN]
> Amending commits requires force push permissions on the repository. If force pushes are disabled, you must create new commits instead.

### Rebasing

When rebasing, ensure all commits include RAI footers:

```bash
git rebase -i HEAD~5
```

For each commit without a footer, use `edit` and add the footer:

```bash
git commit --amend -m "$(git log -1 --pretty=%B)" -m "" -m "Assisted-by: GitHub Copilot <copilot@github.com>"
git rebase --continue
```

> [!WARN]
> Rebasing and amending commits requires force push permissions on the repository. If force pushes are disabled, you must create new commits instead.
