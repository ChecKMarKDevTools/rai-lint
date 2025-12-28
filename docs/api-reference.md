# API Reference

## Node.js (@checkmarkdevtools/commitlint-plugin-rai)

### Plugin Interface

```typescript
import type { Plugin } from '@commitlint/types';

const plugin: Plugin = {
  rules: {
    'rai-footer-exists': raiFooterExists,
  },
};
```

### Rule: rai-footer-exists

**Type**: `Rule`

**Description**: Validates that a commit message contains a valid AI attribution footer.

**Return Type**: `[boolean, string]`

**Parameters**:

- `parsed` (CommitMessage): Parsed commit message object
  - `parsed.raw` (string): Full commit message text

**Return Value**:

- Tuple of `[isValid, errorMessage]`
- `isValid`: `true` if footer is present and valid, `false` otherwise
- `errorMessage`: Empty string on success, error description on failure

**Example**:

```typescript
import raiFooterExists from '@checkmarkdevtools/commitlint-plugin-rai/rules/rai-footer-exists';

const parsed = {
  raw: 'feat: add feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>',
};

const [isValid, message] = raiFooterExists(parsed);
// isValid: true
// message: ''
```

### Supported Patterns

The plugin validates commit messages for the presence of one of these footer patterns (case-insensitive):

- `Authored-by: [Name] <contact>`
- `Commit-generated-by: [AI Tool] <contact>`
- `Assisted-by: [AI Tool] <contact>`
- `Co-authored-by: [AI Tool] <contact>`
- `Generated-by: [AI Tool] <contact>`

Where `<contact>` can be an email address or any identifier (email format is encouraged but not required).

---

## Python (checkmarkdevtools-gitlint-plugin-rai)

### Rule Class: RaiFooterExists

**Base Class**: `gitlint.rules.CommitRule`

**Class Attributes**:

- `name` (str): `"rai-footer-exists"`
- `id` (str): `"UC1"`
- `target` (str): `"commit"`

**Methods**:

#### validate(commit)

**Parameters**:

- `commit` (GitCommit): Gitlint commit object
  - `commit.message.full` (str): Full commit message text

**Return Type**: `list[RuleViolation]`

**Return Value**:

- Empty list if validation passes
- List with one `RuleViolation` if validation fails

**Example**:

```python
from gitlint_rai.rules import RaiFooterExists
from gitlint.tests.base import BaseTestCase

class TestCase(BaseTestCase):
    def test_valid_footer(self):
        rule = RaiFooterExists()
        commit = self.gitcommit("feat: add feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>")
        violations = rule.validate(commit)
        assert len(violations) == 0  # Valid
```

### Supported Patterns

The plugin validates commit messages for the presence of one of these footer patterns (case-insensitive):

- `Authored-by: [Name] <contact>`
- `Commit-generated-by: [AI Tool] <contact>`
- `Assisted-by: [AI Tool] <contact>`
- `Co-authored-by: [AI Tool] <contact>`
- `Generated-by: [AI Tool] <contact>`

Where `<contact>` can be an email address or any identifier (email format is encouraged but not required).

---

## Configuration

### Node.js Configuration

**File**: `commitlint.config.js`

```javascript
export default {
  extends: ['@commitlint/config-conventional'],
  plugins: ['@checkmarkdevtools/commitlint-plugin-rai'],
  rules: {
    'rai-footer-exists': [2, 'always'],
  },
};
```

**Rule Configuration**:

- `[0, 'always']`: Disabled
- `[1, 'always']`: Warning
- `[2, 'always']`: Error (recommended)

### Python Configuration

**File**: `.gitlint`

```ini
[general]
contrib = gitlint_rai.rules.RaiFooterExists

[rai-footer-exists]
# No additional configuration needed
```

---

## Programmatic Usage

### Node.js

```javascript
import { execSync } from 'child_process';

function validateCommitMessage(message) {
  try {
    // Safe: This is example code for documentation
    execSync('npx commitlint', {
      input: message,
      encoding: 'utf-8',
    });
    return { valid: true };
  } catch (error) {
    return { valid: false, error: error.message };
  }
}

const result = validateCommitMessage('feat: test\n\nGenerated-by: GitHub Copilot <copilot@github.com>');
console.log(result); // { valid: true }
```

### Python

```python
from gitlint.cli import cli
from click.testing import CliRunner

def validate_commit_message(message):
    runner = CliRunner()
    result = runner.invoke(cli, ['--msg-filename', '-'], input=message)
    return result.exit_code == 0

valid = validate_commit_message("feat: test\n\nGenerated-by: GitHub Copilot <copilot@github.com>")
print(valid)  # True
```

---

## Error Messages

### Invalid Footer Error

When validation fails, both Node.js (commitlint) and Python (gitlint) plugins display similar error messages listing the required footer formats. The exact wording varies slightly between implementations but conveys the same information about required AI attribution footers.

---

## Type Definitions

### Node.js Types

```typescript
interface ParsedCommit {
  raw: string;
  header: string;
  body: string | null;
  footer: string | null;
  type: string | null;
  scope: string | null;
  subject: string | null;
}

type RuleOutcome = [boolean, string?];

type Rule = (parsed: ParsedCommit, when?: string, value?: any) => RuleOutcome;
```

### Python Types

```python
from typing import List
from gitlint.rules import CommitRule, RuleViolation
from gitlint.git import GitCommit

class RaiFooterExists(CommitRule):
    def validate(self, commit: GitCommit) -> List[RuleViolation]:
        ...
```
