# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
