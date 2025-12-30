# Changelog

All notable changes to `gitlint-rai` are documented here so I don’t have to reconstruct my own intent later from commit archaeology and vibes.

> [!TIP]
> If you want the long-form reasoning behind this whole thing, that lives over here:
> ["Did AI Erase Attribution?"](https://dev.to/anchildress1/did-ai-erase-attribution-your-git-history-is-missing-a-co-author-1m2l) on dev.to. This file is the practical follow-through.

---

## [0.1.2](https://github.com/ChecKMarKDevTools/rai-lint/compare/rai-lint-v0.1.2...rai-lint-v0.1.2) (2025-12-30)


### :seedling: New Capabilities

* implement Python gitlint plugin for RAI footer validation ([42ad6ee](https://github.com/ChecKMarKDevTools/rai-lint/commit/42ad6ee35a18db726e0505bf1513fd5fb32d31dd))
* update AI attribution rules to enforce standard Git trailers ([2fbeed8](https://github.com/ChecKMarKDevTools/rai-lint/commit/2fbeed88527892b4fe505396a7a4e80753fac061))


### :beetle: Things That Were Broken

* **ci:** consolidate release artifacts and auto-commit locks ([#13](https://github.com/ChecKMarKDevTools/rai-lint/issues/13)) ([184f751](https://github.com/ChecKMarKDevTools/rai-lint/commit/184f7519998153c3df3937a5b599413a978d85aa))
* **ci:** remove root package from linked versions in release-please ([b46943d](https://github.com/ChecKMarKDevTools/rai-lint/commit/b46943daa8ffdcf075a87d991d33094c35c84663))
* correct AI attribution footer definitions per article spec ([104cc3e](https://github.com/ChecKMarKDevTools/rai-lint/commit/104cc3e349add355a50a6807235db0278a057d8d))
* correct AI attribution footer patterns per Git trailer spec ([c517864](https://github.com/ChecKMarKDevTools/rai-lint/commit/c517864d106417220f96b46e773c20ea2db9c106))
* remove develop branch refs and update all license references ([ee7957e](https://github.com/ChecKMarKDevTools/rai-lint/commit/ee7957e5b1c9df566f7dcc1b9baac91d026e3657))
* standardize AI attribution trailers ([23900c3](https://github.com/ChecKMarKDevTools/rai-lint/commit/23900c31fb0bf563b6a81859a93801274da0bc78))


### :wrench: Structural Cleanup

* remove check commands from lefthook example files ([821a822](https://github.com/ChecKMarKDevTools/rai-lint/commit/821a822c8a7f9bb4b1bd1f17300b7b5e74e30ba7))
* restructure CI/CD workflow and add comprehensive tests ([#22](https://github.com/ChecKMarKDevTools/rai-lint/issues/22)) ([c5b5cec](https://github.com/ChecKMarKDevTools/rai-lint/commit/c5b5cecffa8c47ad87edf517738bb7b44d80e45e))
* simplify trailer parsing and fix dupe code to omit tests ([39dfda6](https://github.com/ChecKMarKDevTools/rai-lint/commit/39dfda6c0f387db973ea7ab0f980c05cd388ac1d))


### :test_tube: Guardrails

* add integration tests for end-to-end validation ([9112748](https://github.com/ChecKMarKDevTools/rai-lint/commit/911274892285884dcd01ad8a7bf9e307eb1b40ac))


### :robot: Automation

* **workflows:** fix release please workflow to combine versions ([4abe7ac](https://github.com/ChecKMarKDevTools/rai-lint/commit/4abe7acf3ea3c7c8f274d9a468b45c781f56fd93))


### :broom: Tending the Edges

* add LICENSE, CONTRIBUTING, and CHANGELOG ([0caa139](https://github.com/ChecKMarKDevTools/rai-lint/commit/0caa139f9ce98dffd9d96d755bbdce9c4dcc2fea))
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

## [0.1.2](https://github.com/ChecKMarKDevTools/rai-lint/compare/gitlint-rai-v0.1.1...gitlint-rai-v0.1.2) (2025-12-29) 📡 📡

> _Update to the previous threat:_ not war. Yet. Just cleanup, alignment, and one more attempt to make releases mean the same thing everywhere.

The plugin’s surface behavior is unchanged, but its internals are not. CI/CD was restructured, test coverage was rebuilt, Release Please was corrected to stop duplicating versions, and the release pipeline was brought back into alignment with reality.

---

## [0.1.1](https://github.com/ChecKMarKDevTools/rai-lint/compare/gitlint-rai-v0.1.0...gitlint-rai-v0.1.1) (2025-12-29) 📡

> _In which the release machinery worked perfectly in GitHub and then aggressively embarrassed itself everywhere else, forcing several rounds of increasingly resigned workflow debugging._

The plugin itself is fine. It was always fine. The release workflow, however, decided to interpret "automated publishing" as a creative writing exercise with variable outcomes.

Release Please created releases. GitHub saw those releases. PyPI did not see those releases, because OIDC token permissions are apparently conditional based on vibes and which YAML indentation the workflow gods favor that day.

This release fixes the workflow setup that was supposed to already be fixed in the previous release. If it's still broken, that means war.

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
