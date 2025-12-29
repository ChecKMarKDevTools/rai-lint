# Changelog

All notable changes to `@checkmarkdevtools/commitlint-plugin-rai` are documented here so I don’t have to rely on vibes, memory, or aggressively scrolling Git history later, because I promise you I will not remember why I did this six months from now.

I did write about it some in ["Did AI Erase Attribution?"](https://dev.to/anchildress1/did-ai-erase-attribution-your-git-history-is-missing-a-co-author-1m2l). Though... it probably deserves a follow-up after this—I might think about that.

This is the summary version but Git has the receipts if you want the play-by-play.

---

## [0.1.1](https://github.com/ChecKMarKDevTools/rai-lint/compare/commitlint-plugin-rai-v0.1.0...commitlint-plugin-rai-v0.1.1) (2025-12-29)


### :beetle: Things That Were Broken

* restrict lockfile-refresh workflow execution ([378d988](https://github.com/ChecKMarKDevTools/rai-lint/commit/378d988366e6902a1d4f3db4438984d5d4b7a1ec))


### :hammer_and_wrench: Tooling Changes

* **deps-dev:** bump @types/node ([#16](https://github.com/ChecKMarKDevTools/rai-lint/issues/16)) ([95ef100](https://github.com/ChecKMarKDevTools/rai-lint/commit/95ef100ceac35b429fd279b554c753bee913cde0))


### :broom: Tending the Edges

* Fix releases again still ([#15](https://github.com/ChecKMarKDevTools/rai-lint/issues/15)) ([115edc0](https://github.com/ChecKMarKDevTools/rai-lint/commit/115edc027e4496b4f8c449fb2c30544da080e72b))

## 0.1.0 (2025-12-28)

_In which a commitlint plugin exists purely to ask one mildly uncomfortable but extremely reasonable question before you ship code._

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
