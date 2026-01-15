---
title: Become a Power User - Factory Documentation
url: https://docs.factory.ai/cli/user-guides/become-a-power-user
source: sitemap
fetched_at: 2026-01-13T19:03:52.524057893-03:00
rendered_js: false
word_count: 468
summary: This guide explains how to optimize an AI coding assistant named Droid using four specific power features to reduce token usage, minimize tool calls, and improve code quality.
tags:
    - ai-workflow
    - ide-plugin
    - code-specification
    - project-configuration
    - developer-tools
    - productivity-tips
category: guide
---

Want Droid to work faster, smarter, and with fewer iterations? These four power features transform good results into exceptional ones. Each technique saves tokens, reduces tool calls, and ships better code.

## Factory IDE Plugin — Real-time context awareness

Make sure to install Factory IDE plugin for Droid. The Factory IDE plugin acts as an MCP server that gives Droid immediate awareness of your development environment. No more explaining what file you’re looking at or copying error messages—Droid sees exactly what you see. **What Droid gets automatically:**

- Open files and selected lines
- VSCode error highlighting and diagnostics
- Project structure and active terminal output
- Your cursor position and recent edits

**Without the plugin:**

```
"Fix 'Property user does not exist on type AuthContext' error in auth.ts"
```

**With the plugin:**

The plugin eliminates entire categories of back-and-forth. Droid knows the context, sees the errors that you see, and understands your intent from minimal input.

## Spec Mode — Explore and plan first, code second

Complex features need exploration before implementation. Spec Mode prevents costly false starts by letting Droid investigate your codebase thoroughly before writing a single line of code.

**Perfect for:**

- Features touching 2+ files
- Architectural changes
- Unfamiliar codebases
- Security-sensitive work

Without Spec Mode, Droid might jump into implementation too early and not do the work in the exact way you would like. With it, you get a detailed specification and a chance to correct the path before too many tokens are wasted.

## AGENTS.md — Your preferences, remembered

AGENTS.md captures your coding standards, project conventions, and personal preferences in one place. Droid reads it automatically for every task. **What to document:**

CategoryExamples**Code style**”Use arrow functions, not function declarations”  
“Prefer early returns over nested conditionals”**Testing**”Every new endpoint needs integration tests”  
“Use factories, not fixtures for test data”**Architecture**”Services go in src/services with matching interfaces”  
“All database queries use the repository pattern”**Tooling**”Run `npm run verify` before marking any task complete”  
“Deploy with `scripts/deploy.sh`, never manual commands”**Mistakes to avoid**”Never commit .env files”  
“Don’t use any! type annotations”

**Start simple, evolve over time:** Create `AGENTS.md` in your project root:

```
# Project Guidelines

## Testing
- Run `npm test` before completing any feature
- New features need unit tests
- API changes need integration tests

## Code Style  
- Use TypeScript strict mode
- Prefer composition over inheritance
- Keep functions under 20 lines

## Common Commands
- Lint: `npm run lint:fix`
- Test: `npm test`
- Build: `npm run build`
```

Every time Droid repeats a mistake or you explain something twice, add it to AGENTS.md. Within weeks, you’ll have a personalized assistant that knows exactly how you work.

Make your project self-correcting. When Droid can run the same verification tools as your CI/CD pipeline, it fixes problems immediately instead of waiting for you to point them out.

## Combining all four for maximum impact

These features compound. IDE plugin provides context → Spec Mode uses that context for better planning → AGENTS.md ensures consistent implementation → Agent readiness catches issues immediately.