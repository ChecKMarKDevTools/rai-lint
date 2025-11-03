# CheckMarK RAI Lint - Product Overview

CheckMarK RAI Lint is a dual-language commit-message validation framework that enforces consistent AI attribution in development workflows. The project ensures every commit explicitly signals AI involvement through standardized Git trailer footers.

## Core Purpose

- **AI Attribution Enforcement**: Requires one of five specific footer formats in every commit
- **Dual-Language Support**: Native implementations for both Node.js (@commitlint) and Python (Gitlint) ecosystems
- **Responsible AI Development**: Promotes transparency in AI-assisted coding practices

## Supported Attribution Formats

1. `Authored-by: [Human] <email>` - Human only, no AI involvement
2. `Commit-generated-by: [AI Tool] <email>` - Trivial AI (docs, messages, advice)
3. `Assisted-by: [AI Tool] <email>` - AI helped, primarily human-written
4. `Co-authored-by: [AI Tool] <email>` - 50/50 AI/human split (40-60% leeway)
5. `Generated-by: [AI Tool] <email>` - Majority AI-generated content

## Target Users

- Development teams adopting AI tools (GitHub Copilot, ChatGPT, etc.)
- Organizations requiring AI transparency and compliance
- Projects needing consistent attribution across JavaScript/TypeScript and Python codebases

## Integration Points

- Git hooks (Lefthook, Husky, pre-commit)
- CI/CD pipelines
- IDE extensions (future)
- Multi-language monorepos
- Use `git --no-pager` for all commands