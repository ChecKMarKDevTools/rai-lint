# Changelog

All notable changes to `@checkmarkdevtools/commitlint-plugin-rai` are documented here so I don’t have to rely on vibes, memory, or aggressively scrolling Git history later, because I promise you I will not remember why I did this six months from now.

> [!TIP]
> I did write about it some in ["Did AI Erase Attribution?"](https://dev.to/anchildress1/did-ai-erase-attribution-your-git-history-is-missing-a-co-author-1m2l). Though... it probably deserves a follow-up after this—I might think about that.

---

## [0.1.2](https://github.com/ChecKMarKDevTools/rai-lint/compare/node-commitlint-v0.1.2...node-commitlint-v0.1.2) (2025-12-30)


### :seedling: New Capabilities

* implement Node.js commitlint plugin for RAI footer validation ([7845d05](https://github.com/ChecKMarKDevTools/rai-lint/commit/7845d05218a5164f41e6c7e4361812c7adb92c95))
* update AI attribution rules to enforce standard Git trailers ([2fbeed8](https://github.com/ChecKMarKDevTools/rai-lint/commit/2fbeed88527892b4fe505396a7a4e80753fac061))


### :beetle: Things That Were Broken

* **ci:** remove root package from linked versions in release-please ([b46943d](https://github.com/ChecKMarKDevTools/rai-lint/commit/b46943daa8ffdcf075a87d991d33094c35c84663))
* correct AI attribution footer definitions per article spec ([caf793d](https://github.com/ChecKMarKDevTools/rai-lint/commit/caf793d2cccbbe494cfcdca6a9ee1888f5e1ba99))
* correct AI attribution footer definitions per article spec ([104cc3e](https://github.com/ChecKMarKDevTools/rai-lint/commit/104cc3e349add355a50a6807235db0278a057d8d))
* correct AI attribution footer patterns per Git trailer spec ([c517864](https://github.com/ChecKMarKDevTools/rai-lint/commit/c517864d106417220f96b46e773c20ea2db9c106))
* remove develop branch refs and update all license references ([ee7957e](https://github.com/ChecKMarKDevTools/rai-lint/commit/ee7957e5b1c9df566f7dcc1b9baac91d026e3657))
* restrict lockfile-refresh workflow execution ([378d988](https://github.com/ChecKMarKDevTools/rai-lint/commit/378d988366e6902a1d4f3db4438984d5d4b7a1ec))


### :wrench: Structural Cleanup

* remove check commands from lefthook example files ([821a822](https://github.com/ChecKMarKDevTools/rai-lint/commit/821a822c8a7f9bb4b1bd1f17300b7b5e74e30ba7))
* restructure CI/CD workflow and add comprehensive tests ([#22](https://github.com/ChecKMarKDevTools/rai-lint/issues/22)) ([c5b5cec](https://github.com/ChecKMarKDevTools/rai-lint/commit/c5b5cecffa8c47ad87edf517738bb7b44d80e45e))


### :test_tube: Guardrails

* add integration tests for end-to-end validation ([9112748](https://github.com/ChecKMarKDevTools/rai-lint/commit/911274892285884dcd01ad8a7bf9e307eb1b40ac))


### :hammer_and_wrench: Tooling Changes

* **deps-dev:** bump @types/node ([#16](https://github.com/ChecKMarKDevTools/rai-lint/issues/16)) ([95ef100](https://github.com/ChecKMarKDevTools/rai-lint/commit/95ef100ceac35b429fd279b554c753bee913cde0))


### :robot: Automation

* update security audit workflow and standardize license format ([c4af288](https://github.com/ChecKMarKDevTools/rai-lint/commit/c4af288c79ff04d9a08a786d3559cec39ac90b3a))
* **workflows:** fix release please workflow to combine versions ([4abe7ac](https://github.com/ChecKMarKDevTools/rai-lint/commit/4abe7acf3ea3c7c8f274d9a468b45c781f56fd93))


### :broom: Tending the Edges

* add LICENSE, CONTRIBUTING, and CHANGELOG ([0caa139](https://github.com/ChecKMarKDevTools/rai-lint/commit/0caa139f9ce98dffd9d96d755bbdce9c4dcc2fea))
* Clean up project structure and add agent documentation ([2bf1479](https://github.com/ChecKMarKDevTools/rai-lint/commit/2bf14794d87cfbad669476d8be3f7998f5be910f))
* **deps:** Bump dependencies and migrate to ESLint flat config ([a4f9baf](https://github.com/ChecKMarKDevTools/rai-lint/commit/a4f9baf4390128ed33c310f2c5f5c6cac32f4296))
* **deps:** Complete ESLint 9 migration and update major Python tooling ([1703ff6](https://github.com/ChecKMarKDevTools/rai-lint/commit/1703ff66589904853a6c2510ca3ab5e15be9f4b6))
* Fix releases again still ([#15](https://github.com/ChecKMarKDevTools/rai-lint/issues/15)) ([115edc0](https://github.com/ChecKMarKDevTools/rai-lint/commit/115edc027e4496b4f8c449fb2c30544da080e72b))
* release main ([#11](https://github.com/ChecKMarKDevTools/rai-lint/issues/11)) ([6ef7fe5](https://github.com/ChecKMarKDevTools/rai-lint/commit/6ef7fe549bcdf8260d7bd6206db504e2d4a45606))
* release main ([#20](https://github.com/ChecKMarKDevTools/rai-lint/issues/20)) ([0628967](https://github.com/ChecKMarKDevTools/rai-lint/commit/0628967fa5de5454e4032f1b2ce09861a6b60ab7))
* release main ([#23](https://github.com/ChecKMarKDevTools/rai-lint/issues/23)) ([2cf6b6f](https://github.com/ChecKMarKDevTools/rai-lint/commit/2cf6b6f74ab1b25d79c810f316e03d3697b5bbe0))
* release main ([#26](https://github.com/ChecKMarKDevTools/rai-lint/issues/26)) ([8ed8e9d](https://github.com/ChecKMarKDevTools/rai-lint/commit/8ed8e9de5878de69bb960e4b91b22216378a469f))
* Release prep ([#12](https://github.com/ChecKMarKDevTools/rai-lint/issues/12)) ([25c940b](https://github.com/ChecKMarKDevTools/rai-lint/commit/25c940bd8b970225843f09bd8c434e31c37ed600))
* reset release please versions ([be10e8f](https://github.com/ChecKMarKDevTools/rai-lint/commit/be10e8f127891577e2844811c892e10f35a37829))
* streamline CI/CD workflows and modernize package configs ([ea38de7](https://github.com/ChecKMarKDevTools/rai-lint/commit/ea38de73d42e88a09bce5f3b30993a769d71768d))
* tweaks for merge ([#3](https://github.com/ChecKMarKDevTools/rai-lint/issues/3)) ([777d583](https://github.com/ChecKMarKDevTools/rai-lint/commit/777d583227b66daece190767e1bc066c984fbd28))

## [0.1.2](https://github.com/ChecKMarKDevTools/rai-lint/compare/commitlint-plugin-rai-v0.1.1...commitlint-plugin-rai-v0.1.2) (2025-12-29) 📡 📡

> _Ok, I lied._ No pottery. This turned into cleanup, config alignment, and wrestling CI until it stopped freelancing.

No user-facing behavior changes, but under the hood this is a realignment release. Core workflows were restructured, release logic was consolidated, and the surrounding machinery now matches how the plugin actually works instead of how it used to pretend to.

---

## [0.1.1](https://github.com/ChecKMarKDevTools/rai-lint/compare/commitlint-plugin-rai-v0.1.0...commitlint-plugin-rai-v0.1.1) (2025-12-29) 📡

> _Because the releases technically worked on GitHub, then immediately fell apart when asked to do literally anything else, prompting a debugging session I would describe as "character-building."_

The plugin is stable. It does its job. It has been doing its job since I initially wrote it, unbothered and consistent.

The CI workflows responsible for publishing it to npm, however, decided that "working" was negotiable and that sometimes lockfiles should refresh themselves mid-release for reasons they declined to explain.

This release corrects the automated publishing setup that was theoretically correct last time but demonstrably wasn't even close. It also bumps `@types/node` because Dependabot has opinions and I'm inclined to agree.

If this doesn't work, I'm learning pottery.

---

### What This Is 📦

This is a commitlint plugin that will not let you commit until you say who actually helped write the code, which feels like a low bar and yet here we are.

It’s not a lecture, it’s not a manifesto, and it’s definitely not trying to solve the entire “AI ethics” discourse in a footer. It just wants you to be honest and move on with your day.

It understands five Git trailers:

- `Authored-by` — all you, no AI involved, pure human effort and probably caffeine
- `Commit-generated-by` — AI wrote the commit message, you wrote the code, a perfectly reasonable division of labor
- `Assisted-by` — AI helped a bit, but you were still driving and making the calls
- `Co-authored-by` — you and the AI paired, roughly fifty-fifty, everyone gets credit
- `Generated-by` — AI did most of the work, you supervised, still valid, just say so

Pick one and you’re done. Skip it and the commit fails immediately, calmly, and without entering into negotiations about how busy you are.

There’s no telemetry, no tracking, no network calls, and no opinions about formatting or workflow. It doesn’t care how you work, it just wants the attribution written down so future humans aren’t guessing.

Status: **Shipped.** Hopefully. 😄

---

### Why This Exists 🔧

If two humans pair program, both names go on the commit. If an AI helps and we pretend it didn’t happen, that’s a choice, but it’s a weird one.

Git already supports trailers. Commits already support attribution. This plugin just closes the gap between “we could do this” and “we actually do this,” because enforcement turns philosophy into muscle memory.

I got tired of debating it and built the boring solution instead.

---

### The Extremely Short Version of Events 🗓️

I built this, plus the Python version, in a burst of enthusiasm and questionable time awareness, then spent the following weeks fixing things, cleaning things up, and making the tooling stop yelling at me long enough to ship something usable.

If you want the gritty details, Git is right there and very thorough. This is just the overview.

---

### December 28, 2025: v0.1.0 🚀

It enforces attribution without overthinking it, it stays out of your way once you comply, and it does exactly one job on purpose.

Everything else will evolve from here, along with the inevitable future mistakes and fixing the mistakes I missed this round.
