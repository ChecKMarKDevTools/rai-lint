# Changelog

All notable changes to `gitlint-rai` are documented here so I don’t have to reconstruct my own intent later from commit archaeology and vibes.

> [!TIP]
> If you want the long-form reasoning behind this whole thing, that lives over here:
> ["Did AI Erase Attribution?"](https://dev.to/anchildress1/did-ai-erase-attribution-your-git-history-is-missing-a-co-author-1m2l) on dev.to. This file is the practical follow-through.

---

## [0.1.2](https://github.com/ChecKMarKDevTools/rai-lint/compare/v0.1.5...v0.1.2) (2026-01-18)


### :seedling: New Capabilities

* add development setup automation and documentation ([521a327](https://github.com/ChecKMarKDevTools/rai-lint/commit/521a3273054c343792194de6ad107bf1afd89b71))
* add GitHub issue and PR templates ([cc6ea4f](https://github.com/ChecKMarKDevTools/rai-lint/commit/cc6ea4f7aff00a63b3be67d25297d9b7f8970b32))
* add hook integration examples for Lefthook, Husky, and pre-commit ([6cc87ca](https://github.com/ChecKMarKDevTools/rai-lint/commit/6cc87ca91b0e1dc7e4befde98b29681555653d6f))
* add shared test fixtures for cross-language validation ([b3444fc](https://github.com/ChecKMarKDevTools/rai-lint/commit/b3444fc69ed2dd296e522e1c9241931ce1facf9c))
* add VS Code workspace configuration ([8fc0b99](https://github.com/ChecKMarKDevTools/rai-lint/commit/8fc0b99c29b4e6671f23bfab2cd39aca0b5eb7eb))
* **ci:** enable test-and-build workflow on main branch pushes ([1d5e6d7](https://github.com/ChecKMarKDevTools/rai-lint/commit/1d5e6d7a37b6eb13c295ac1a604a2692737a31f4))
* configure CI/CD matrix for multi-version testing ([f9aa7f5](https://github.com/ChecKMarKDevTools/rai-lint/commit/f9aa7f52938a2d3c1dad32dd5bc804f414afd740))
* implement Node.js commitlint plugin for RAI footer validation ([7845d05](https://github.com/ChecKMarKDevTools/rai-lint/commit/7845d05218a5164f41e6c7e4361812c7adb92c95))
* implement Python gitlint plugin for RAI footer validation ([42ad6ee](https://github.com/ChecKMarKDevTools/rai-lint/commit/42ad6ee35a18db726e0505bf1513fd5fb32d31dd))
* initialize CheckMarK RAI Lint monorepo structure ([b79ed34](https://github.com/ChecKMarKDevTools/rai-lint/commit/b79ed343002a7448743a9e56b6aecfe2f1079c88))
* update AI attribution rules to enforce standard Git trailers ([2fbeed8](https://github.com/ChecKMarKDevTools/rai-lint/commit/2fbeed88527892b4fe505396a7a4e80753fac061))
* update AI attribution rules to enforce standard Git trailers ([9d8f7c2](https://github.com/ChecKMarKDevTools/rai-lint/commit/9d8f7c2835b7efd1ff748f1132e9983480cb4be3))


### :beetle: Things That Were Broken

* **ci:** configure release-please for linked versioning and label handling ([091db31](https://github.com/ChecKMarKDevTools/rai-lint/commit/091db31c0c050b67c5743f49ea22c24750b7e6b4))
* **ci:** consolidate release artifacts and auto-commit locks ([#13](https://github.com/ChecKMarKDevTools/rai-lint/issues/13)) ([184f751](https://github.com/ChecKMarKDevTools/rai-lint/commit/184f7519998153c3df3937a5b599413a978d85aa))
* **ci:** fix release please and security workflows ([dd88903](https://github.com/ChecKMarKDevTools/rai-lint/commit/dd88903228da519b49b41cacbf1dc727bf1f3be3))
* **ci:** fix sonar organization case ([8c8aea2](https://github.com/ChecKMarKDevTools/rai-lint/commit/8c8aea2757e8b2949d90a4c88258fb70937cf946))
* **ci:** remove root package from linked versions in release-please ([b46943d](https://github.com/ChecKMarKDevTools/rai-lint/commit/b46943daa8ffdcf075a87d991d33094c35c84663))
* **ci:** remove root package from linked versions in release-please ([47d0367](https://github.com/ChecKMarKDevTools/rai-lint/commit/47d03672f5e3b5845fa8e493ac86553f590a96f0))
* **ci:** update changelog paths to root level ([1caa865](https://github.com/ChecKMarKDevTools/rai-lint/commit/1caa865702c4f28428a9722f1fd2f63c3978c48b))
* **commitlint-plugin:** relax peer deps to restore install ([5587ade](https://github.com/ChecKMarKDevTools/rai-lint/commit/5587ade044f26dc7c0f451f7f0dc6f0d9eec0b84))
* correct AI attribution footer definitions per article spec ([caf793d](https://github.com/ChecKMarKDevTools/rai-lint/commit/caf793d2cccbbe494cfcdca6a9ee1888f5e1ba99))
* correct AI attribution footer definitions per article spec ([104cc3e](https://github.com/ChecKMarKDevTools/rai-lint/commit/104cc3e349add355a50a6807235db0278a057d8d))
* correct AI attribution footer patterns per Git trailer spec ([c517864](https://github.com/ChecKMarKDevTools/rai-lint/commit/c517864d106417220f96b46e773c20ea2db9c106))
* coverage paths, Codecov actions, SonarCloud artifacts ([bd23a22](https://github.com/ChecKMarKDevTools/rai-lint/commit/bd23a22ba3517e41e8efecbe76c3fdff07b33f0a))
* remove develop branch refs and update all license references ([ee7957e](https://github.com/ChecKMarKDevTools/rai-lint/commit/ee7957e5b1c9df566f7dcc1b9baac91d026e3657))
* restrict lockfile-refresh workflow execution ([378d988](https://github.com/ChecKMarKDevTools/rai-lint/commit/378d988366e6902a1d4f3db4438984d5d4b7a1ec))
* standardize AI attribution trailers ([23900c3](https://github.com/ChecKMarKDevTools/rai-lint/commit/23900c31fb0bf563b6a81859a93801274da0bc78))
* update release-please config for correct package names and settings ([c59206b](https://github.com/ChecKMarKDevTools/rai-lint/commit/c59206b1116804708644ca3ce0d4d5474c9c20a4))


### :zap: Faster or Lighter

* add performance benchmarks for Node and Python ([1fe18f8](https://github.com/ChecKMarKDevTools/rai-lint/commit/1fe18f863810fdc902cc7080cb92e3a61e8361e6))


### :wrench: Structural Cleanup

* **ci:** Dynamically pull Node version from Volta in workflows ([a5897e2](https://github.com/ChecKMarKDevTools/rai-lint/commit/a5897e296f8c5975805a126243c0d724e4f7b07e))
* **ci:** Extract license checking to dedicated script ([09501b9](https://github.com/ChecKMarKDevTools/rai-lint/commit/09501b9993a87942ae4ab34d89f235959fc96d31))
* **deps:** simplify license validation and add Python-2.0 license ([af7e7ca](https://github.com/ChecKMarKDevTools/rai-lint/commit/af7e7ca96c8810682a4db690498693a27834bb14))
* remove check commands from lefthook example files ([821a822](https://github.com/ChecKMarKDevTools/rai-lint/commit/821a822c8a7f9bb4b1bd1f17300b7b5e74e30ba7))
* restructure CI/CD workflow and add comprehensive tests ([#22](https://github.com/ChecKMarKDevTools/rai-lint/issues/22)) ([c5b5cec](https://github.com/ChecKMarKDevTools/rai-lint/commit/c5b5cecffa8c47ad87edf517738bb7b44d80e45e))
* simplify trailer parsing and fix dupe code to omit tests ([39dfda6](https://github.com/ChecKMarKDevTools/rai-lint/commit/39dfda6c0f387db973ea7ab0f980c05cd388ac1d))


### :book: Words and Explanations

* add advanced configuration examples ([49b270b](https://github.com/ChecKMarKDevTools/rai-lint/commit/49b270b9693ac5b98458a85c0b540caa223e4043))
* add API reference and troubleshooting guide ([fd662f2](https://github.com/ChecKMarKDevTools/rai-lint/commit/fd662f23dbb1fee5127b4e2a3d04c5d1cfb19eb6))
* add changelog rewrite style instructions ([8e29b87](https://github.com/ChecKMarKDevTools/rai-lint/commit/8e29b87be4c1e189f006bca7e13f3240709483ba))
* add comprehensive documentation for CheckMarK RAI Lint ([f0e33e9](https://github.com/ChecKMarKDevTools/rai-lint/commit/f0e33e9d68551c857b69a73161105246f1af4b77))
* Add comprehensive project implementation summary ([0d4a4ee](https://github.com/ChecKMarKDevTools/rai-lint/commit/0d4a4ee0fbf379e4145411bd05f2f195b2e8a0c2))
* enhance documentation with Signed-off-by guidance ([1a8d29c](https://github.com/ChecKMarKDevTools/rai-lint/commit/1a8d29c681a3aa14e2c7f392bf96e85fce67e39d))


### :test_tube: Guardrails

* add assertions to performance tests ([5a26344](https://github.com/ChecKMarKDevTools/rai-lint/commit/5a263442688b4c8fc4c6cb082c3b05e8f4340621))
* add integration tests for end-to-end validation ([9112748](https://github.com/ChecKMarKDevTools/rai-lint/commit/911274892285884dcd01ad8a7bf9e307eb1b40ac))


### :hammer_and_wrench: Tooling Changes

* Configure Release Please for monorepo with linked versions ([c4f883e](https://github.com/ChecKMarKDevTools/rai-lint/commit/c4f883ea567425b7822a6370b68f51303deb7a79))
* **deps-dev:** bump @types/node ([#16](https://github.com/ChecKMarKDevTools/rai-lint/issues/16)) ([95ef100](https://github.com/ChecKMarKDevTools/rai-lint/commit/95ef100ceac35b429fd279b554c753bee913cde0))
* **deps-dev:** bump the dependencies group across 1 directory with 5 updates ([#32](https://github.com/ChecKMarKDevTools/rai-lint/issues/32)) ([09dae6e](https://github.com/ChecKMarKDevTools/rai-lint/commit/09dae6e1e630414c261fb2c0929a71bf2a0463b3))
* **deps-dev:** bump the dependencies group with 2 updates ([#24](https://github.com/ChecKMarKDevTools/rai-lint/issues/24)) ([7c70efa](https://github.com/ChecKMarKDevTools/rai-lint/commit/7c70efa29b1976031b22dd45bfddb6c07fa5ab19))
* **deps-dev:** bump the dependencies group with 3 updates ([#17](https://github.com/ChecKMarKDevTools/rai-lint/issues/17)) ([6deff7b](https://github.com/ChecKMarKDevTools/rai-lint/commit/6deff7b1fb6815925ae2ddabf68c54926f66d274))
* **deps:** bump actions/download-artifact in the dependencies group ([#25](https://github.com/ChecKMarKDevTools/rai-lint/issues/25)) ([affdf7a](https://github.com/ChecKMarKDevTools/rai-lint/commit/affdf7ac9e3291018d3f45de5b1a2e99d64abbad))
* **deps:** bump astral-sh/setup-uv in the dependencies group ([#33](https://github.com/ChecKMarKDevTools/rai-lint/issues/33)) ([d38753a](https://github.com/ChecKMarKDevTools/rai-lint/commit/d38753a33584d1f8411bca0467546868f0c4cdf4))
* **deps:** bump the dependencies group across 1 directory with 3 updates ([#19](https://github.com/ChecKMarKDevTools/rai-lint/issues/19)) ([14657d9](https://github.com/ChecKMarKDevTools/rai-lint/commit/14657d98d0c7dc48710bd9ead95986a8f3b92ec2))
* revert package versions to 0.1.1 ([9fd042c](https://github.com/ChecKMarKDevTools/rai-lint/commit/9fd042ce77744ce6a88fab56cda0d682bc658643))


### :robot: Automation

* add release, quality, and dependency review workflows ([90ad802](https://github.com/ChecKMarKDevTools/rai-lint/commit/90ad8021c181d44343c9e76c43be0c2d160c810e))
* enhance security audit workflow and release configuration ([0c4ae07](https://github.com/ChecKMarKDevTools/rai-lint/commit/0c4ae07368dd9b45cabebc29de37b90d19196bf8))
* fix release-please single-tag release wiring ([#34](https://github.com/ChecKMarKDevTools/rai-lint/issues/34)) ([e567c11](https://github.com/ChecKMarKDevTools/rai-lint/commit/e567c11d0ecd444289ca3ae1cb20844684a45b6d))
* force lockfile update to execute sequentially ([e2a96e9](https://github.com/ChecKMarKDevTools/rai-lint/commit/e2a96e995e277adefb4999c022267ee8d346e87d))
* **release-please:** fix release gating to detect merge commits ([f5025d7](https://github.com/ChecKMarKDevTools/rai-lint/commit/f5025d79c76af499cd206d122098a1dfb3c581b6))
* **release:** fix gating for manifest mode ([8fbb490](https://github.com/ChecKMarKDevTools/rai-lint/commit/8fbb490873c2103a570415039719051e08fe7ef6))
* **release:** fix manifest-mode gating for publish jobs ([141024b](https://github.com/ChecKMarKDevTools/rai-lint/commit/141024b26f5811c6080d9e7e49dd32a1906b122e))
* skip build and test jobs on release-please branches ([1ea803e](https://github.com/ChecKMarKDevTools/rai-lint/commit/1ea803e0fab352d6132935f8995cf2e78b412c4e))
* update codecov actions, add env vars, and fix doc link ([6a58cb0](https://github.com/ChecKMarKDevTools/rai-lint/commit/6a58cb09d26b6f9f14bb9b40577c2d31bff372c6))
* update release-please configuration ([6e0988a](https://github.com/ChecKMarKDevTools/rai-lint/commit/6e0988a990f1c033409ba7604de3164d777c2025))
* update security audit workflow and clean up ([fd28d62](https://github.com/ChecKMarKDevTools/rai-lint/commit/fd28d62299edd68b7ea02539041a9be3fe7f8d61))
* update security audit workflow and standardize license format ([c4af288](https://github.com/ChecKMarKDevTools/rai-lint/commit/c4af288c79ff04d9a08a786d3559cec39ac90b3a))
* **workflows:** add git pull after checkout in lockfile refresh jobs ([ae35118](https://github.com/ChecKMarKDevTools/rai-lint/commit/ae3511866e9b46fb1e5e1d3b016105f05147d011))
* **workflows:** fix release please workflow to combine versions ([4abe7ac](https://github.com/ChecKMarKDevTools/rai-lint/commit/4abe7acf3ea3c7c8f274d9a468b45c781f56fd93))
* **workflows:** refactor lockfile refresh to use shared branch resolver ([e8782fc](https://github.com/ChecKMarKDevTools/rai-lint/commit/e8782fca21b3ff82b2d8af1b5e34bbead349d9d3))


### :broom: Tending the Edges

* add eslint-comments plugin and enforce style rules ([63ce7de](https://github.com/ChecKMarKDevTools/rai-lint/commit/63ce7defcb6863b010a6a1c8a1c2e3bdb3c4a85c))
* add eslint-comments plugin and enforce style rules ([19ef2e9](https://github.com/ChecKMarKDevTools/rai-lint/commit/19ef2e982fc333fe974fc2aa9dcad8fd559aa809))
* add explicit pr pattern ([edc0d41](https://github.com/ChecKMarKDevTools/rai-lint/commit/edc0d41ab328ea7f8e97f819aa4b46be1f2bda8e))
* add LICENSE, CONTRIBUTING, and CHANGELOG ([0caa139](https://github.com/ChecKMarKDevTools/rai-lint/commit/0caa139f9ce98dffd9d96d755bbdce9c4dcc2fea))
* Clean up project structure and add agent documentation ([2bf1479](https://github.com/ChecKMarKDevTools/rai-lint/commit/2bf14794d87cfbad669476d8be3f7998f5be910f))
* decrease dependabot frequency ([e5ca7d9](https://github.com/ChecKMarKDevTools/rai-lint/commit/e5ca7d96e55ab51518c638ba9fd2d9b6178a05aa))
* **deps:** Bump dependencies and migrate to ESLint flat config ([a4f9baf](https://github.com/ChecKMarKDevTools/rai-lint/commit/a4f9baf4390128ed33c310f2c5f5c6cac32f4296))
* **deps:** Complete ESLint 9 migration and update major Python tooling ([1703ff6](https://github.com/ChecKMarKDevTools/rai-lint/commit/1703ff66589904853a6c2510ca3ab5e15be9f4b6))
* enforce 120 char line length and disable inline comments ([ca7b10f](https://github.com/ChecKMarKDevTools/rai-lint/commit/ca7b10f5f60f61ed97ac2ad136b3628d94052d87))
* fix commitlint package version ([#37](https://github.com/ChecKMarKDevTools/rai-lint/issues/37)) ([1a6ee58](https://github.com/ChecKMarKDevTools/rai-lint/commit/1a6ee58705690f9c30e1e46929aa1a69508ce932))
* fix label on release-please ([ded9ea2](https://github.com/ChecKMarKDevTools/rai-lint/commit/ded9ea2f646684ddedcdbafda4dc6b079ad6333c))
* fix lockfile workflow; add GitHub funding file ([73e19d1](https://github.com/ChecKMarKDevTools/rai-lint/commit/73e19d14c9bf749c1ecf3500bcbb684ba8ecd0f0))
* fix missing python version directive ([7880811](https://github.com/ChecKMarKDevTools/rai-lint/commit/788081102f0e39821aabd5c22eb3ef77e9ea2a2e))
* Fix releases again still ([#15](https://github.com/ChecKMarKDevTools/rai-lint/issues/15)) ([115edc0](https://github.com/ChecKMarKDevTools/rai-lint/commit/115edc027e4496b4f8c449fb2c30544da080e72b))
* introduce Makefile for project automation and validation ([67b83ad](https://github.com/ChecKMarKDevTools/rai-lint/commit/67b83ad1a52ce8db90aad38788b69166b05e797e))
* release ([#29](https://github.com/ChecKMarKDevTools/rai-lint/issues/29)) ([7d61bb1](https://github.com/ChecKMarKDevTools/rai-lint/commit/7d61bb14bdf557a81d00401ab7bd62f5456e5e7d))
* release ([#30](https://github.com/ChecKMarKDevTools/rai-lint/issues/30)) ([28688fa](https://github.com/ChecKMarKDevTools/rai-lint/commit/28688fa92c49177a73345f8a2e68bfac1f0e3ae9))
* release main ([#11](https://github.com/ChecKMarKDevTools/rai-lint/issues/11)) ([6ef7fe5](https://github.com/ChecKMarKDevTools/rai-lint/commit/6ef7fe549bcdf8260d7bd6206db504e2d4a45606))
* release main ([#20](https://github.com/ChecKMarKDevTools/rai-lint/issues/20)) ([0628967](https://github.com/ChecKMarKDevTools/rai-lint/commit/0628967fa5de5454e4032f1b2ce09861a6b60ab7))
* release main ([#23](https://github.com/ChecKMarKDevTools/rai-lint/issues/23)) ([2cf6b6f](https://github.com/ChecKMarKDevTools/rai-lint/commit/2cf6b6f74ab1b25d79c810f316e03d3697b5bbe0))
* release main ([#26](https://github.com/ChecKMarKDevTools/rai-lint/issues/26)) ([8ed8e9d](https://github.com/ChecKMarKDevTools/rai-lint/commit/8ed8e9de5878de69bb960e4b91b22216378a469f))
* release main ([#27](https://github.com/ChecKMarKDevTools/rai-lint/issues/27)) ([5465640](https://github.com/ChecKMarKDevTools/rai-lint/commit/5465640a02a8643cd42fbf80852ae992d37209ad))
* release main ([#35](https://github.com/ChecKMarKDevTools/rai-lint/issues/35)) ([7811c83](https://github.com/ChecKMarKDevTools/rai-lint/commit/7811c83f76325a2b9693cbb8444a3781ddbbd6af))
* release main ([#36](https://github.com/ChecKMarKDevTools/rai-lint/issues/36)) ([7ba5e11](https://github.com/ChecKMarKDevTools/rai-lint/commit/7ba5e11f531178caa809c2e6df9fa44002a404df))
* release main ([#38](https://github.com/ChecKMarKDevTools/rai-lint/issues/38)) ([90220e4](https://github.com/ChecKMarKDevTools/rai-lint/commit/90220e42cd280eb91437075546a2b5529fdefc27))
* release main ([#39](https://github.com/ChecKMarKDevTools/rai-lint/issues/39)) ([712570f](https://github.com/ChecKMarKDevTools/rai-lint/commit/712570fa8e84d23720bf3838a9cde23ce4b98d9e))
* Release prep ([#12](https://github.com/ChecKMarKDevTools/rai-lint/issues/12)) ([25c940b](https://github.com/ChecKMarKDevTools/rai-lint/commit/25c940bd8b970225843f09bd8c434e31c37ed600))
* reset release please versions ([be10e8f](https://github.com/ChecKMarKDevTools/rai-lint/commit/be10e8f127891577e2844811c892e10f35a37829))
* streamline CI/CD workflows and modernize package configs ([ea38de7](https://github.com/ChecKMarKDevTools/rai-lint/commit/ea38de73d42e88a09bce5f3b30993a769d71768d))
* tweaks for merge ([#3](https://github.com/ChecKMarKDevTools/rai-lint/issues/3)) ([777d583](https://github.com/ChecKMarKDevTools/rai-lint/commit/777d583227b66daece190767e1bc066c984fbd28))
* update project structure and configurations ([c30020d](https://github.com/ChecKMarKDevTools/rai-lint/commit/c30020d484c35adece8d76323cd9677168012a0f))

## [0.1.5](https://github.com/ChecKMarKDevTools/rai-lint/compare/v0.1.4...v0.1.5) (2026-01-18) 🧯

> _A small patch with very little drama, which is exactly the point._

Docs got tweaked (again) to be more explicit about `Signed-off-by` guidance, and yes: I’m still trying to make the commitlint plugin install stop exploding under strict peer dependency enforcement. That’s the whole release. _Aside:_ if Release Please changes its mind again and decides this release never happened, I cannot be held accountable; Git can take the stand.

## [0.1.4](https://github.com/ChecKMarKDevTools/rai-lint/compare/v0.1.3...v0.1.4) (2026-01-14) 🧹

> _Because even the tiniest version bump deserves a drumroll, or at least a polite cough._

A quick patch to fix the commitlint package version that was apparently auditioning for a game of hide-and-seek. No user-facing changes, just the machinery getting its act together.

## [0.1.3](https://github.com/ChecKMarKDevTools/rai-lint/compare/v0.1.2...v0.1.3) (2026-01-08) 📡📡📡

> _A boring release, in the best possible way:_ this one is about making CI/release automation less fragile and keeping dependencies current.

No user-facing rule behavior changes in either package. If you linted commits yesterday, you’re linting commits today — just with fewer ways for the release machinery to hurt itself.

### Highlights

- **Release automation is harder to derail.** Release Please configuration and “single-tag” wiring were fixed so tags/versions line up cleanly across this monorepo instead of drifting into “wait, which package did we publish?” territory.
- **Security + supply chain posture got a tune-up.** The security audit workflow was improved, and the `astral-sh/setup-uv` action was bumped so the Python toolchain setup stays aligned with the ecosystem.
- **Paper cuts were removed.** A couple of small-but-annoying config fixes landed (explicit PR pattern, missing Python version directive), and versions were normalized after an earlier mismatch.

## [0.1.2](https://github.com/ChecKMarKDevTools/rai-lint/compare/v0.1.1...v0.1.2) (2025-12-30) 📡 📡

> _Ok, I lied._ No pottery. This turned into cleanup, config alignment, and wrestling CI until it stopped freelancing.

No user-facing behavior changes in either package, but this release is a realignment: workflows were restructured, release logic was consolidated, and the surrounding machinery now matches how these plugins actually work instead of how it used to pretend to.

## [0.1.1](https://github.com/ChecKMarKDevTools/rai-lint/compare/v0.1.0...v0.1.1) (2025-12-29) 📡

> _Because the releases technically worked on GitHub, then immediately fell apart when asked to do literally anything else, prompting a debugging session I would describe as "character-building."_

The plugins were fine. The release workflow, however, decided that "working" was negotiable.

This release corrects the automated publishing setup that was theoretically correct last time but demonstrably wasn't even close.

If this doesn't work, I'm learning pottery.

---

### What This Is 📦

This is a single-purpose Python plugin for gitlint that exists to enforce one extremely reasonable thing: if AI helped write the code, say so in the commit message.

It validates commit messages for **exactly one** AI attribution trailer and absolutely does not care which one you pick, as long as you pick one and stop pretending nothing happened.

It recognizes five trailers:

- `Authored-by` — you wrote it, AI did not touch the keyboard, congratulations
- `Commit-generated-by` — AI wrote the commit message, you wrote the code, extremely normal behavior
- `Assisted-by` — AI helped some, maybe a third of the work, you were still making decisions
- `Co-authored-by` — roughly a 50/50 split, like actual pair programming but quieter
- `Generated-by` — AI did most of the work, you steered, which is still work

Choose one and move on. If you try to sneak past without attribution, the commit fails immediately and without commentary.

There are no network calls, no telemetry, no tracking, and no debates about formatting or emojis. It’s just a regex, a rule, and a non-zero exit code when you’re being evasive about who or what wrote the code.

If this feels boring, that’s intentional. Small tools that do one thing and get out of the way are the entire point.

Status: **Shipped.** Hopefully. 😄

---

### Why This Exists 🔧

Because “we’ll remember who helped” turns out to be a lie Git history tells very convincingly.

This plugin exists to make attribution boring, consistent, and unavoidable, not because people are malicious, but because humans are busy and memory is optional once a commit is merged.

Git already supports trailers. Commits already support attribution. This just closes the gap between “technically possible” and “actually happens,” without turning it into a values debate every time someone opens a PR.

Tools are better at being annoying in exactly the same way every time. So I let the tool do it.

---

### The Short, Honest Timeline 🗓️

This started with a single burst of energy where I built both the Node and Python versions in one go, because apparently I like my projects symmetrical and my timelines questionable.

That initial push included the plugin itself, tests, docs, CI, release workflows, examples, and enough scaffolding to mildly regret my choices. Everything landed on October 31, which is either poetic or concerning.

After that came the predictable phase where things were fixed, then fixed again, then fixed correctly once I stopped trying to parse Git trailers by intuition and actually read the spec.

November was cleanup and modernization, December was release prep, and eventually I stopped touching it long enough to ship.

If you want the blow-by-blow, Git has it. This is the version you read without sighing.

---

### December 28, 2025: v0.1.0 🚀

The plugin runs locally, enforces attribution, and stays out of your way once you comply.

Everything else will evolve from here, including future improvements and the inevitable bugs I haven’t met yet.
