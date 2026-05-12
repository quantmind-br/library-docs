---
title: "Project Guidelines in ForgeCode"
url: https://forgecode.dev/docs/custom-rules/
source: sitemap
fetched_at: 2026-04-30T14:09:06.319312454-03:00
rendered_js: false
word_count: 70
summary: "Define persistent AI agent instructions for your project using an `AGENTS.md` file."
tags:
  - project-guidelines
  - ai-agents
  - markdown-configuration
  - development-standards
  - instruction-injection
category: configuration
optimized: true
---
# Project Guidelines in ForgeCode

> **TL;DR**
> Use `AGENTS.md` to define persistent AI agent instructions for your project.

## How It Works
- **File**: `AGENTS.md` in project root.
- **Format**: Full Markdown (headings, lists, code blocks).
- **Injection**: Guidelines are added to every AI conversation.

## Example Structure
```markdown
# Project Guidelines

## Runtime Behavior
- Use Node.js 18+.
- Enable strict mode.

## Code Standards
- Follow ESLint `recommended` config.
- Use TypeScript for new files.

## Project Structure
- `src/` for application code.
- `tests/` for all test files.

## Team Conventions
- Commit messages: `<type>(<scope>): <subject>`.
- PRs require 2 approvals.
```

## Benefits
- **Consistency**: AI follows project standards.
- **Persistence**: No need to repeat instructions.
- **Clarity**: Markdown supports detailed documentation.