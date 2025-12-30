# Changelog

All notable changes to `gitlint-rai` are documented here so I don’t have to reconstruct my own intent later from commit archaeology and vibes.

> [!TIP]
> If you want the long-form reasoning behind this whole thing, that lives over here:
> ["Did AI Erase Attribution?"](https://dev.to/anchildress1/did-ai-erase-attribution-your-git-history-is-missing-a-co-author-1m2l) on dev.to. This file is the practical follow-through.

---

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
