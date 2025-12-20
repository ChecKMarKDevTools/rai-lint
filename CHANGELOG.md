# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.0.0 (2025-12-20)


### ✨ New Features

* add development setup automation and documentation ([521a327](https://github.com/ChecKMarKDevTools/rai-lint/commit/521a3273054c343792194de6ad107bf1afd89b71))
* add GitHub issue and PR templates ([cc6ea4f](https://github.com/ChecKMarKDevTools/rai-lint/commit/cc6ea4f7aff00a63b3be67d25297d9b7f8970b32))
* add hook integration examples for Lefthook, Husky, and pre-commit ([6cc87ca](https://github.com/ChecKMarKDevTools/rai-lint/commit/6cc87ca91b0e1dc7e4befde98b29681555653d6f))
* add shared test fixtures for cross-language validation ([b3444fc](https://github.com/ChecKMarKDevTools/rai-lint/commit/b3444fc69ed2dd296e522e1c9241931ce1facf9c))
* add VS Code workspace configuration ([8fc0b99](https://github.com/ChecKMarKDevTools/rai-lint/commit/8fc0b99c29b4e6671f23bfab2cd39aca0b5eb7eb))
* configure CI/CD matrix for multi-version testing ([f9aa7f5](https://github.com/ChecKMarKDevTools/rai-lint/commit/f9aa7f52938a2d3c1dad32dd5bc804f414afd740))
* implement Node.js commitlint plugin for RAI footer validation ([7845d05](https://github.com/ChecKMarKDevTools/rai-lint/commit/7845d05218a5164f41e6c7e4361812c7adb92c95))
* implement Python gitlint plugin for RAI footer validation ([42ad6ee](https://github.com/ChecKMarKDevTools/rai-lint/commit/42ad6ee35a18db726e0505bf1513fd5fb32d31dd))
* initialize CheckMarK RAI Lint monorepo structure ([b79ed34](https://github.com/ChecKMarKDevTools/rai-lint/commit/b79ed343002a7448743a9e56b6aecfe2f1079c88))
* update AI attribution rules to enforce standard Git trailers ([2fbeed8](https://github.com/ChecKMarKDevTools/rai-lint/commit/2fbeed88527892b4fe505396a7a4e80753fac061))
* update AI attribution rules to enforce standard Git trailers ([9d8f7c2](https://github.com/ChecKMarKDevTools/rai-lint/commit/9d8f7c2835b7efd1ff748f1132e9983480cb4be3))


### 🐛 Bug Fixes

* **ci:** configure release-please for linked versioning and label handling ([091db31](https://github.com/ChecKMarKDevTools/rai-lint/commit/091db31c0c050b67c5743f49ea22c24750b7e6b4))
* correct AI attribution footer definitions per article spec ([caf793d](https://github.com/ChecKMarKDevTools/rai-lint/commit/caf793d2cccbbe494cfcdca6a9ee1888f5e1ba99))
* correct AI attribution footer definitions per article spec ([104cc3e](https://github.com/ChecKMarKDevTools/rai-lint/commit/104cc3e349add355a50a6807235db0278a057d8d))
* correct AI attribution footer patterns per Git trailer spec ([c517864](https://github.com/ChecKMarKDevTools/rai-lint/commit/c517864d106417220f96b46e773c20ea2db9c106))
* remove develop branch refs and update all license references ([ee7957e](https://github.com/ChecKMarKDevTools/rai-lint/commit/ee7957e5b1c9df566f7dcc1b9baac91d026e3657))
* standardize AI attribution trailers ([23900c3](https://github.com/ChecKMarKDevTools/rai-lint/commit/23900c31fb0bf563b6a81859a93801274da0bc78))


### ⚡ Performance

* add performance benchmarks for Node and Python ([1fe18f8](https://github.com/ChecKMarKDevTools/rai-lint/commit/1fe18f863810fdc902cc7080cb92e3a61e8361e6))


### 🔨 Refactoring

* **ci:** Dynamically pull Node version from Volta in workflows ([a5897e2](https://github.com/ChecKMarKDevTools/rai-lint/commit/a5897e296f8c5975805a126243c0d724e4f7b07e))
* **ci:** Extract license checking to dedicated script ([09501b9](https://github.com/ChecKMarKDevTools/rai-lint/commit/09501b9993a87942ae4ab34d89f235959fc96d31))
* **deps:** simplify license validation and add Python-2.0 license ([af7e7ca](https://github.com/ChecKMarKDevTools/rai-lint/commit/af7e7ca96c8810682a4db690498693a27834bb14))
* remove check commands from lefthook example files ([821a822](https://github.com/ChecKMarKDevTools/rai-lint/commit/821a822c8a7f9bb4b1bd1f17300b7b5e74e30ba7))


### 📝 Documentation

* add advanced configuration examples ([49b270b](https://github.com/ChecKMarKDevTools/rai-lint/commit/49b270b9693ac5b98458a85c0b540caa223e4043))
* add API reference and troubleshooting guide ([fd662f2](https://github.com/ChecKMarKDevTools/rai-lint/commit/fd662f23dbb1fee5127b4e2a3d04c5d1cfb19eb6))
* add comprehensive documentation for CheckMarK RAI Lint ([f0e33e9](https://github.com/ChecKMarKDevTools/rai-lint/commit/f0e33e9d68551c857b69a73161105246f1af4b77))
* Add comprehensive project implementation summary ([0d4a4ee](https://github.com/ChecKMarKDevTools/rai-lint/commit/0d4a4ee0fbf379e4145411bd05f2f195b2e8a0c2))


### ✅ Tests

* add integration tests for end-to-end validation ([9112748](https://github.com/ChecKMarKDevTools/rai-lint/commit/911274892285884dcd01ad8a7bf9e307eb1b40ac))


### 📦 Build

* Configure Release Please for monorepo with linked versions ([c4f883e](https://github.com/ChecKMarKDevTools/rai-lint/commit/c4f883ea567425b7822a6370b68f51303deb7a79))


### 🔁 CI/CD

* add release, quality, and dependency review workflows ([90ad802](https://github.com/ChecKMarKDevTools/rai-lint/commit/90ad8021c181d44343c9e76c43be0c2d160c810e))
* update security audit workflow and clean up ([fd28d62](https://github.com/ChecKMarKDevTools/rai-lint/commit/fd28d62299edd68b7ea02539041a9be3fe7f8d61))
* update security audit workflow and standardize license format ([c4af288](https://github.com/ChecKMarKDevTools/rai-lint/commit/c4af288c79ff04d9a08a786d3559cec39ac90b3a))


### 🧰 Maintenance

* add eslint-comments plugin and enforce style rules ([63ce7de](https://github.com/ChecKMarKDevTools/rai-lint/commit/63ce7defcb6863b010a6a1c8a1c2e3bdb3c4a85c))
* add eslint-comments plugin and enforce style rules ([19ef2e9](https://github.com/ChecKMarKDevTools/rai-lint/commit/19ef2e982fc333fe974fc2aa9dcad8fd559aa809))
* add LICENSE, CONTRIBUTING, and CHANGELOG ([0caa139](https://github.com/ChecKMarKDevTools/rai-lint/commit/0caa139f9ce98dffd9d96d755bbdce9c4dcc2fea))
* Clean up project structure and add agent documentation ([2bf1479](https://github.com/ChecKMarKDevTools/rai-lint/commit/2bf14794d87cfbad669476d8be3f7998f5be910f))
* **deps:** Bump dependencies and migrate to ESLint flat config ([a4f9baf](https://github.com/ChecKMarKDevTools/rai-lint/commit/a4f9baf4390128ed33c310f2c5f5c6cac32f4296))
* **deps:** Complete ESLint 9 migration and update major Python tooling ([1703ff6](https://github.com/ChecKMarKDevTools/rai-lint/commit/1703ff66589904853a6c2510ca3ab5e15be9f4b6))
* enforce 120 char line length and disable inline comments ([ca7b10f](https://github.com/ChecKMarKDevTools/rai-lint/commit/ca7b10f5f60f61ed97ac2ad136b3628d94052d87))
* fix label on release-please ([ded9ea2](https://github.com/ChecKMarKDevTools/rai-lint/commit/ded9ea2f646684ddedcdbafda4dc6b079ad6333c))
* introduce Makefile for project automation and validation ([67b83ad](https://github.com/ChecKMarKDevTools/rai-lint/commit/67b83ad1a52ce8db90aad38788b69166b05e797e))
* streamline CI/CD workflows and modernize package configs ([ea38de7](https://github.com/ChecKMarKDevTools/rai-lint/commit/ea38de73d42e88a09bce5f3b30993a769d71768d))
* tweaks for merge ([#3](https://github.com/ChecKMarKDevTools/rai-lint/issues/3)) ([777d583](https://github.com/ChecKMarKDevTools/rai-lint/commit/777d583227b66daece190767e1bc066c984fbd28))

## [Unreleased] 🎪

> _Where feature flags go to live rent-free while we nervously watch CI pipelines._

### Recent Plumbing 🔧

> _Dec 2025: Release automation saga and CI dependency hygiene._

**For Maintainers** (you, probably)

- Configured Release Please for monorepo with linked versions (build commit c4f883e)
- Extracted license checking to dedicated Python script (refactor commit 09501b9)
- Workflows now dynamically pull Node version from Volta config (refactor commit a5897e2)
- Added Python-2.0 to allowed license list, simplified validation logic (refactor commit af7e7ca)
- Security audit workflow standardized and cleaned up (ci commit c4af288)
- Fixed release-please label configuration (chore commit ded9ea2)

---

### From align-for-release Branch (Squashed) 🎭

> Your author spent quality time arguing with GitHub Actions. The Actions won.

**Added**

- Codecov uploads now work (finally) — coverage reports no longer vanish into the void like your self-esteem during a failed deploy 📊
- Matrix artifact names now unique per version because apparently GitHub Actions can't count 🎯
- Explicit coverage checks that actually fail CI when files go AWOL (novel concept, we know) ✅
- Unit test for empty commit messages because someone will try it 🪹
- OIDC/Trusted Publishing for npm because managing tokens is for people with free time 🔐

**Changed**

- Bumped Node matrix to 20/22/24 (Node 18 has left the building) 🚀
- Bumped Python matrix to 3.11/3.12 (because Python 3.10 support is _so_ last year) 🐍
- Workflows now pin action refs like we're scared of supply chain attacks (we are) 📌
- CI now runs `npm ci` in workspace mode because root deps are a thing 📦
- LCOV and JUnit reports actually generated now (they weren't before, oops) 📈

**Fixed**

- Test workflow working-directory usage (turns out YAML cares about indentation) 🔧
- Release workflow no longer dry-runs _everything_ forever (sorry, npm) 🎁
- Makefile install modes clarified because "install vs install-locked" was too confusing 📘
- SonarCloud now scans weekly instead of blocking every PR like an overprotective parent 🛡️

**Removed**

- Deploy job you didn't ask for (my bad, I got excited) 🙈
- Local SonarCloud pre-push hook (it was slowing you down) 🏃

---

### From main Branch 🎪

> _October–November 2025: A month-long journey from "what's a Git trailer?" to "oh god, we have 60+ commits."_

**The Big Stuff** 🏗️

- Migrated to ESLint 9 flat config and evicted all legacy plugins (goodbye, `.eslintrc.json`)
- Standardized AI attribution from emoji chaos to proper Git trailers (breaking change, sorry)
- Added Makefile for automation because typing `npm run` gets old
- Created dual-language monorepo with Node.js and Python packages that actually work together

**The CI/CD Theatre** 🎭

- Set up GitHub Actions matrix testing across Node 16-24 and Python 3.9-3.12
- Added release workflows, quality checks, and Codecov reporting
- Configured dependency review because supply chain attacks are real

**The Documentation Era** 📚

- Wrote comprehensive docs with Mermaid diagrams (pretty pictures!)
- Added API reference, troubleshooting guide, and setup automation
- Created hook integration examples for Lefthook, Husky, and pre-commit
- Added issue/PR templates and VS Code workspace config

**The Refinements** ✨

- Performance benchmarks (10k iterations each, for the curious)
- Shared test fixtures to ensure Node/Python parity
- Enforced 120-char line length (brevity is law)
- Fixed trailer definitions approximately 17 times (reading is hard)

**The License Situation** ⚖️

- Copilot tried to license this under MIT, but he was nearly fired for that.
- Fixed proper Polyform Shield 1.0.0 license and all is right with the world.

---

## Release History 🎁

_No releases yet. Waiting for the perfect commit message._
