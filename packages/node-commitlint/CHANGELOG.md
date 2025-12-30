# Changelog

All notable changes to `@checkmarkdevtools/commitlint-plugin-rai` are documented here so I don’t have to rely on vibes, memory, or aggressively scrolling Git history later, because I promise you I will not remember why I did this six months from now.

> [!TIP]
> I did write about it some in ["Did AI Erase Attribution?"](https://dev.to/anchildress1/did-ai-erase-attribution-your-git-history-is-missing-a-co-author-1m2l). Though... it probably deserves a follow-up after this—I might think about that.

---

## [0.1.2](https://github.com/ChecKMarKDevTools/rai-lint/compare/node-commitlint-v0.1.2...v0.1.2) (2025-12-30) 📡 📡

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
