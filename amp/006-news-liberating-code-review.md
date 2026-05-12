---
title: Liberating Code Review
url: https://ampcode.com/news/liberating-code-review
source: crawler
fetched_at: 2026-02-06T02:07:44.87398788-03:00
rendered_js: false
word_count: 382
summary: This document explains the decoupled Amp review agent's capabilities, including its various invocation methods and the implementation of custom review criteria using scoped Checks.
tags:
    - amp-review
    - code-review
    - ai-agents
    - developer-tools
    - automation
    - custom-checks
category: guide
---

Code review has traditionally been tied to an interface where a human reads diffs. With the original Amp review agent, we moved away from an external review UI into the editor, where comments could be acted on more immediately. Now, we've fully decoupled the review agent completely from any UI, making it a composable and extensible subroutine that can be invoked from many different places where it is useful:

- You can run `amp review` in the CLI to run the review agent directly
- You can request a review in any thread in `smart` mode using natural language like "review the outstanding changes" or "review changes since diverging from main"
- You can kick off multiple reviews in parallel from the editor extension review panel

This composability also means you can more easily close the loop by asking the main agent to automatically fix the issues found or by piping review comments into another command.

Invoking the review agent directly using `amp review`:

Requesting a review from within a thread:

![Review tool](https://static.ampcode.com/news/review-skill/cli_review.png)

Requesting a review from the editor extension diff panel:

![Review tool](https://static.ampcode.com/news/review-skill/review_tool.png?v=2)

## Customizing Review with Checks

You can also define [*Checks*](https://ampcode.com/manual#checks) within your codebase. Checks are user-defined invariants or review criteria scoped to specific parts of your codebase. They are defined in `.agents/checks/` directories.

Here's an example performance check, which you could save to `.agents/checks/perf.md`:

```
---
name: performance
description: Flags common performance anti-patterns
---

Look for these patterns:

- Nested loops over the same collection (O(n²) → O(n) with a Set/Map)
- Repeated `array.includes()` in a loop
- Sorting inside a loop
- String concatenation in a loop (use array + join)

Report the line, why it matters, and how to fix it.
```

The `code_review` tool will kick off a separate agent for each check. This provides a stronger guarantee that each check will actually be checked than if the checks were embedded in a general context file like `AGENTS.md`.

Here are some more examples of useful checks:

- Performance best practices specific to your stack
- Common anti-patterns your team has hit before
- Security best practices or invariants
- Migration reminders for deprecated APIs
- Stylistic conventions that aren't in the linter
- Compliance requirements

Checks are scoped to the directory that contains `.agents/`, so a root `.agents/checks` directory would cover the entire codebase while `api/.agents/checks` would cover files under `api/`.