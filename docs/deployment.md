# Deployment

## NPM Trusted Publishing

**One-time setup on npmjs.com:**

1. Log in to npmjs.com
2. Navigate to package settings → Publishing
3. Add Trusted Publisher:
   - Provider: GitHub Actions
   - Repository owner: `your-org`
   - Repository name: `rai-lint`
   - Workflow: `.github/workflows/release-please.yml`
   - Environment: (leave empty)

**Workflow configuration:**

```yaml
permissions:
  id-token: write

- name: Publish to NPM
  run: npm publish --provenance --access public
```

**Provenance:** <https://docs.npmjs.com/trusted-publishers/>

## PyPI Trusted Publishing

**One-time setup on PyPI:**

1. Log in to PyPI
2. Navigate to Account Settings → Publishing
3. Add a new pending publisher:
   - PyPI Project Name: `checkmark-rai-lint`
   - Owner: `your-username`
   - Repository: `rai-lint`
   - Workflow: `release-please.yml`
   - Environment: (leave empty)

**Workflow configuration:**

```yaml
permissions:
  id-token: write

- name: Publish to PyPI
  uses: pypa/gh-action-pypi-publish@release/v1
  with:
    packages-dir: packages/python-gitlint/dist/
```

**Provenance:** <https://docs.pypi.org/trusted-publishers/>

## Secrets to Remove

After configuring trusted publishing, remove these from GitHub repository secrets:

- `NPM_TOKEN`
- `PYPI_TOKEN`
