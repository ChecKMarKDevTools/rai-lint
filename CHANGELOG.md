# Changelog

All notable changes to `gitlint-rai` are documented here so I don’t have to reconstruct my own intent later from commit archaeology and vibes.

> [!TIP]
> If you want the long-form reasoning behind this whole thing, that lives over here:
> ["Did AI Erase Attribution?"](https://dev.to/anchildress1/did-ai-erase-attribution-your-git-history-is-missing-a-co-author-1m2l) on dev.to. This file is the practical follow-through.

---

## [0.1.3](https://github.com/ChecKMarKDevTools/rai-lint/compare/v0.1.2...v0.1.3) (2026-01-08) 📡📡📡

> _A boring release, in the best possible way:_ this one is about making CI/release automation less fragile and keeping dependencies current.

No user-facing rule behavior changes in either package. If you linted commits yesterday, you’re linting commits today — just with fewer ways for the release machinery to hurt itself.

### Highlights

- **Release automation is harder to derail.** Release Please configuration and “single-tag” wiring were fixed so tags/versions line up cleanly across this monorepo instead of drifting into “wait, which package did we publish?” territory.
- **Security + supply chain posture got a tune-up.** The security audit workflow was improved, and the `astral-sh/setup-uv` action was bumped so the Python toolchain setup stays aligned with the ecosystem.
- **Paper cuts were removed.** A couple of small-but-annoying config fixes landed (explicit PR pattern, missing Python version directive), and versions were normalized after an earlier mismatch.

<details>
<summary><strong>Full commit / PR list (raw)</strong></summary>

### :hammer_and_wrench: Tooling Changes

- **deps-dev:** bump the dependencies group across 1 directory with 5 updates ([#32](https://github.com/ChecKMarKDevTools/rai-lint/issues/32)) ([09dae6e](https://github.com/ChecKMarKDevTools/rai-lint/commit/09dae6e1e630414c261fb2c0929a71bf2a0463b3))
- **deps:** bump astral-sh/setup-uv in the dependencies group ([#33](https://github.com/ChecKMarKDevTools/rai-lint/issues/33)) ([d38753a](https://github.com/ChecKMarKDevTools/rai-lint/commit/d38753a33584d1f8411bca0467546868f0c4cdf4))
- revert package versions to 0.1.1 ([9fd042c](https://github.com/ChecKMarKDevTools/rai-lint/commit/9fd042ce77744ce6a88fab56cda0d682bc658643)) and then later put back

### :robot: Automation

- enhance security audit workflow and release configuration ([0c4ae07](https://github.com/ChecKMarKDevTools/rai-lint/commit/0c4ae07368dd9b45cabebc29de37b90d19196bf8))
- fix release-please single-tag release wiring ([#34](https://github.com/ChecKMarKDevTools/rai-lint/issues/34)) ([e567c11](https://github.com/ChecKMarKDevTools/rai-lint/commit/e567c11d0ecd444289ca3ae1cb20844684a45b6d))
- update release-please configuration ([6e0988a](https://github.com/ChecKMarKDevTools/rai-lint/commit/6e0988a990f1c033409ba7604de3164d777c2025))

</details>

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
