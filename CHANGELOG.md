# Changelog

## v1.0.0 (2025-12-14) — THE INAUGURAL SERMON 🙌

> _Brothers and sisters, can I get a HALLELUJAH for validated commit messages?!_

**FRIENDS,** we are GATHERED here today to witness the GLORY of **v1.0.0** — a release SO MOMENTOUS that it required not one, not two, but TWO whole programming languages to contain its magnificence! JavaScript couldn't handle it alone. Python had to step in. It's a MIRACLE of modern software development!

### 🎪 THE MAIN EVENT: What Even IS This Thing?

Picture this: You're writing commit messages. Maybe you had a little help from your friendly neighborhood AI assistant. Maybe ChatGPT wrote that whole refactor. Maybe GitHub Copilot autocompleted your entire test suite. And you thought, "Should I... mention that?"

**THE ANSWER IS YES, YOU ABSOLUTELY SHOULD.**

And THAT, my friends, is where **rai-lint** comes swooping in like a BOOSTER PACK flying through a megachurch — unexpected, slightly chaotic, but EXACTLY what you needed to stay honest about AI collaboration!

### ✨ THE FEATURES (That'll Make You SHOUT) ✨

#### 🎯 Node.js Plugin (`@checkmarkdevtools/commitlint-plugin-rai`)

Started at v1.0.0 because we're CONFIDENT like that! This baby validates your commit message footers with FIVE sacred attribution patterns:

- `Authored-by:` — All human, baby! (The endangered species)
- `Commit-generated-by:` — AI did trivial stuff (docs, typos, existential advice)
- `Assisted-by:` — Human-led with AI sidekick energy
- `Co-authored-by:` — The buddy cop movie of code commits (50/50 split, give or take)
- `Generated-by:` — AI did the heavy lifting while you supervised with coffee

**IMPLEMENTED IN:** Pure TypeScript glory, ESLint 9 flat config, tested across Node 20/22/24 like we're running for political office!

#### 🐍 Python Plugin (`checkmarkdevtools-gitlint-plugin-rai`)

Started at v0.1.0 because Python devs are humble like that (or we forgot to bump it, WHO'S COUNTING). Same five glorious patterns, different syntax, SAME ENERGY!

**IMPLEMENTED IN:** Pure Python, type-hinted within an inch of its life, tested on Python 3.11/3.12 because we don't live in 2019 anymore, KAREN.

### 🔥 THE BREAKING CHANGES (They Had to Happen) 🔥

Remember when we tried to use emojis in Git trailers? 😅✨🤖 Remember when "Co-Authored-By" capitalization was all over the place? Remember when we thought separate versioning was a good idea?

**WE WERE YOUNG. WE WERE FOOLISH.**

Now we follow PROPER Git trailer specifications like adults who read documentation! That means:

- Standard trailer keys (no more creative interpretations)
- Case-insensitive matching (because developers have enough to worry about)
- Unified versioning (one version to rule them all!)

### 🏗️ THE INFRASTRUCTURE MIRACLES 🏗️

#### Dual-Language Monorepo

JavaScript and Python living together, sharing test fixtures like ROOMMATES who actually get along! It's a monorepo miracle!

#### CI/CD That Actually Works

- Matrix testing across **Node 20/22/24** and **Python 3.11/3.12**
- OIDC Trusted Publishing (no tokens were harmed in the making of this release)
- Coverage reports that DON'T vanish into the void
- Release Please automation (it even generates changelogs, but clearly not THIS one)
- Artifact attestations and SBOMs because security is SEXY

#### Documentation Written By Humans (Mostly)

- Architecture diagrams with Mermaid (they're GORGEOUS)
- API references that won't put you to sleep
- Troubleshooting guides that assume you're smart but tired
- Integration examples for Lefthook, Husky, and pre-commit

### 🐛 THE BUGS WE FIXED (And How We Found Them) 🐛

Fixed the AI attribution patterns **MULTIPLE TIMES** because apparently reading Git trailer specifications is HARDER than reading ancient Sumerian. Who knew that `Co-authored-by` had specific capitalization rules? WE DO NOW!

Also fixed:

- Branch reference cleanup (goodbye `develop` branch, we hardly knew ye)
- License chaos (MIT almost happened, disaster averted)
- Test workflow directories (YAML indentation is the DEVIL)
- Coverage report generation (they exist now!)
- Empty commit message handling (yes, someone will try it)

### 🎭 THE REFACTORING CHRONICLES 🎭

Removed example check commands from Lefthook configs because we learned that showing people `make check` doesn't mean they'll RUN `make check`. Classic mistake. We're wiser now.

Also EVICTED all legacy ESLint plugins during the Great ESLint 9 Migration of November 2025. It was TRAUMATIC but we're STRONGER for it.

### ✅ THE TESTS (Thousands of Them) ✅

Integration tests for DAYS! We run 10,000 iterations of benchmarks because if you're not PARANOID about performance, are you even trying? Spoiler: Both plugins validate a commit message in under 1ms. FAST AND FURIOUS, baby!

### 🧰 THE QUALITY TOOLS (Or: How We Sleep at Night) 🧰

- **Makefile automation** — Because typing `npm run test && cd ../python-gitlint && poetry run pytest` is for people with TIME
- **SonarCloud scanning** — Weekly, not blocking (we learned our lesson)
- **Codecov integration** — Now with 100% less "where did my coverage report go?"
- **Dependency review** — Supply chain attacks are REAL, people!

### 📦 THE PACKAGES (Now Available for Installation!) 📦

**Node.js:**

```bash
npm install --save-dev @checkmarkdevtools/commitlint-plugin-rai
```

**Python:**

```bash
pip install checkmarkdevtools-gitlint-plugin-rai
# or if you're fancy:
uv add --dev checkmarkdevtools-gitlint-plugin-rai
```

### ⚖️ THE LICENSE (Not MIT This Time) ⚖️

We're using **Polyform Shield 1.0.0** — the license that says "you can use this, fork this, modify this, but you can't wrap it in commercial tooling and sell it back to us." Fair's fair!

---

### 🙏 IN CONCLUSION 🙏

v1.0.0 is HERE, it's TESTED, it's DOCUMENTED, and it's ready to validate your AI collaboration transparency like it's NOBODY'S BUSINESS (except it literally IS your business to disclose AI usage).

Will there be bugs? PROBABLY.  
Will there be patches? ABSOLUTELY.  
Will we keep this changelog format? **THAT DEPENDS ON YOUR FEEDBACK.**

But for NOW, go forth and COMMIT RESPONSIBLY!

**Package Links:**

- [npm: @checkmarkdevtools/commitlint-plugin-rai](https://www.npmjs.com/package/@checkmarkdevtools/commitlint-plugin-rai)
- [PyPI: checkmarkdevtools-gitlint-plugin-rai](https://pypi.org/project/checkmarkdevtools-gitlint-plugin-rai/)
- [GitHub: ChecKMarKDevTools/rai-lint](https://github.com/ChecKMarKDevTools/rai-lint)

---

**Commit Attribution for This Changelog:**  
`Generated-by: Verdent AI <verdent@verdent.ai>` _(with creative direction from a human who REALLY loves The Righteous Gemstones)_
