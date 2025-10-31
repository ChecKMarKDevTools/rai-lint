# API Reference

## Node.js (@checkmark/commitlint-plugin-rai)

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

**Description**: Validates that a commit message contains a valid RAI footer.

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
import raiFooterExists from '@checkmark/commitlint-plugin-rai/rules/rai-footer-exists';

const parsed = {
  raw: 'feat: add feature\n\n🛡️ RAI: AI-Generated'
};

const [isValid, message] = raiFooterExists(parsed);
// isValid: true
// message: ''
```

### Supported Patterns

```typescript
const RAI_FOOTER_PATTERNS = [
  /^🛡️\s+RAI:\s+AI-Generated$/im,
  /^🛡️\s+RAI:\s+AI-Assisted$/im,
  /^Generated-by:\s+Verdent AI\s+<verdent@verdent\.ai>$/im,
];
```

**Flags**:
- `i`: Case-insensitive
- `m`: Multiline (^ and $ match line boundaries)

---

## Python (checkmark-rai-lint)

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
from checkmark_rai_lint.rules import RaiFooterExists
from gitlint.tests.base import BaseTestCase

class TestCase(BaseTestCase):
    def test_valid_footer(self):
        rule = RaiFooterExists()
        commit = self.gitcommit("feat: add feature\n\n🛡️ RAI: AI-Generated")
        violations = rule.validate(commit)
        assert len(violations) == 0  # Valid
```

### Supported Patterns

```python
RAI_FOOTER_PATTERNS = [
    re.compile(r"^🛡️\s+RAI:\s+AI-Generated$", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^🛡️\s+RAI:\s+AI-Assisted$", re.IGNORECASE | re.MULTILINE),
    re.compile(
        r"^Generated-by:\s+Verdent AI\s+<verdent@verdent\.ai>$",
        re.IGNORECASE | re.MULTILINE,
    ),
]
```

**Flags**:
- `re.IGNORECASE`: Case-insensitive matching
- `re.MULTILINE`: ^ and $ match line boundaries

---

## Configuration

### Node.js Configuration

**File**: `commitlint.config.js`

```javascript
export default {
  extends: ['@commitlint/config-conventional'],
  plugins: ['@checkmark/commitlint-plugin-rai'],
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
contrib = checkmark_rai_lint.rules.RaiFooterExists

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
    execSync('npx commitlint', {
      input: message,
      encoding: 'utf-8',
    });
    return { valid: true };
  } catch (error) {
    return { valid: false, error: error.message };
  }
}

const result = validateCommitMessage('feat: test\n\n🛡️ RAI: AI-Generated');
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

valid = validate_commit_message("feat: test\n\n🛡️ RAI: AI-Generated")
print(valid)  # True
```

---

## Error Messages

### Invalid Footer Error

**Node.js**:
```
Commit message must include a valid RAI footer:
  - "🛡️ RAI: AI-Generated"
  - "🛡️ RAI: AI-Assisted"
  - "Generated-by: Verdent AI <verdent@verdent.ai>"
```

**Python**:
```
UC1 Commit message must include a valid RAI footer:
  - "🛡️ RAI: AI-Generated"
  - "🛡️ RAI: AI-Assisted"
  - "Generated-by: Verdent AI <verdent@verdent.ai>"
```

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
