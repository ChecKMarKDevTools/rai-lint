# Troubleshooting Guide

## Common Issues and Solutions

### Node.js / Commitlint Issues

#### Issue: "Cannot find module '@checkmark/commitlint-plugin-rai'"

**Cause**: Package not installed or not in node_modules

**Solution**:
```bash
npm install --save-dev @checkmark/commitlint-plugin-rai
rm -rf node_modules package-lock.json
npm install
```

---

#### Issue: "Plugin not found: @checkmark/commitlint-plugin-rai"

**Cause**: Plugin not added to `commitlint.config.js`

**Solution**:
Ensure your config includes:
```javascript
export default {
  plugins: ['@checkmark/commitlint-plugin-rai'],
  rules: {
    'rai-footer-exists': [2, 'always'],
  },
};
```

---

#### Issue: Hook not running on commit

**Cause**: Git hooks not installed

**Solution for Lefthook**:
```bash
npx lefthook install
```

**Solution for Husky**:
```bash
npx husky install
npx husky add .husky/commit-msg 'npx commitlint --edit $1'
```

**Verify**:
```bash
ls -la .git/hooks/commit-msg
cat .git/hooks/commit-msg
```

---

#### Issue: "ReferenceError: require is not defined"

**Cause**: Using CommonJS require in ESM module

**Solution**: Convert to ESM syntax
```javascript
// ❌ CommonJS
module.exports = { ... }

// ✅ ESM
export default { ... }
```

---

### Python / Gitlint Issues

#### Issue: "ModuleNotFoundError: No module named 'checkmark_rai_lint'"

**Cause**: Package not installed

**Solution**:
```bash
pip install checkmark-rai-lint
pip list | grep checkmark
```

For development:
```bash
cd packages/python-gitlint
pip install -e .
```

---

#### Issue: "gitlint.exceptions.GitLintError: No such contrib rule"

**Cause**: Incorrect contrib path in `.gitlint`

**Solution**: Verify `.gitlint` configuration:
```ini
[general]
contrib = checkmark_rai_lint.rules.RaiFooterExists
```

**Debug**:
```bash
gitlint --debug
python -c "from checkmark_rai_lint.rules import RaiFooterExists; print(RaiFooterExists)"
```

---

#### Issue: pre-commit hook not running

**Cause**: Hooks not installed

**Solution**:
```bash
pre-commit install --hook-type commit-msg
pre-commit run --hook-stage commit-msg --commit-msg-filename .git/COMMIT_EDITMSG
```

**Verify**:
```bash
ls -la .git/hooks/commit-msg
```

---

### Footer Validation Issues

#### Issue: Valid footer rejected

**Symptoms**: Commit with footer still fails validation

**Common Causes**:

1. **Extra whitespace**
   ```bash
   # ❌ Extra space before footer
   " Generated-by: GitHub Copilot <copilot@github.com>"

   # ✅ No leading space
   "Generated-by: GitHub Copilot <copilot@github.com>"
   ```

2. **Wrong keyword**
   ```bash
   # ❌ Invalid keyword
   "Created-by: GitHub Copilot <copilot@github.com>"

   # ✅ Valid keyword
   "Generated-by: GitHub Copilot <copilot@github.com>"
   ```

3. **Typo in text**
   ```bash
   # ❌ Typo
   "Generatedby: GitHub Copilot <copilot@github.com>"

   # ✅ Correct
   "Generated-by: GitHub Copilot <copilot@github.com>"
   ```

4. **Email format**
   ```bash
   # ❌ Missing angle brackets
   "Generated-by: GitHub Copilot copilot@github.com"

   # ✅ With angle brackets
   "Generated-by: GitHub Copilot <copilot@github.com>"
   ```

**Debug**:
```bash
# Check exact bytes
echo "Generated-by: GitHub Copilot <copilot@github.com>" | xxd

# Test pattern
echo "feat: test\n\nGenerated-by: GitHub Copilot <copilot@github.com>" | npx commitlint
```

---

#### Issue: Footer appears but still fails

**Cause**: Footer might not be on its own line

**Solution**: Ensure footer is separated by blank line
```bash
# ❌ No blank line
feat: add feature
Generated-by: GitHub Copilot <copilot@github.com>

# ✅ Blank line before footer
feat: add feature

Generated-by: GitHub Copilot <copilot@github.com>
```

---

### CI/CD Issues

#### Issue: GitHub Actions failing on commitlint

**Cause**: Shallow clone missing commit history

**Solution**: Use `fetch-depth: 0`
```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
```

---

#### Issue: Python tests failing in CI

**Cause**: gitlint not installed

**Solution**: Install with test dependencies
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -e "packages/python-gitlint[dev]"
```

---

### Performance Issues

#### Issue: Slow commit validation

**Symptoms**: Commits take several seconds

**Solution**: Run benchmarks
```bash
# Node
cd packages/node-commitlint
npm test benchmarks/

# Python
cd packages/python-gitlint
python ../../benchmarks/python_benchmark.py
```

**Expected Performance**:
- Node.js: < 1ms per validation
- Python: < 5ms per validation

If slower, check for:
- Large commit messages (> 10KB)
- Network issues (if plugins are fetching remote configs)

---

### IDE Integration Issues

#### Issue: VS Code not showing commit errors

**Cause**: Conventional Commits extension not configured

**Solution**: Install extension and configure
```json
{
  "conventionalCommits.autoCommit": false,
  "conventionalCommits.promptFooter": true
}
```

---

#### Issue: JetBrains IDE not running hook

**Cause**: Git hooks not enabled in IDE

**Solution**:
1. Go to Settings → Version Control → Git
2. Enable "Run Git hooks"
3. Restart IDE

---

## Debugging Commands

### Node.js

```bash
# Test commit message
echo "feat: test\n\nGenerated-by: GitHub Copilot <copilot@github.com>" | npx commitlint

# Verbose output
npx commitlint --verbose --edit .git/COMMIT_EDITMSG

# Debug mode
DEBUG=* npx commitlint --edit .git/COMMIT_EDITMSG

# Check config
npx commitlint --print-config
```

### Python

```bash
# Test commit message
echo "feat: test\n\nGenerated-by: GitHub Copilot <copilot@github.com>" | gitlint

# Verbose output
gitlint --verbose

# Debug mode
gitlint --debug

# Check config
gitlint --config
```

---

## Getting Help

If you're still experiencing issues:

1. Check [GitHub Issues](https://github.com/your-org/checkmark-rai-lint/issues)
2. Run with `--debug` or `--verbose` flags
3. Verify versions:
   ```bash
   # Node
   node --version
   npm list @checkmark/commitlint-plugin-rai

   # Python
   python --version
   pip show checkmark-rai-lint
   ```
4. Create a minimal reproduction case
5. Open a new issue with debug output
