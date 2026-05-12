---
title: Review AI-Generated Code | Guides | Warp
url: https://docs.warp.dev/guides/agent-workflows/how-to-review-ai-generated-code
source: sitemap
fetched_at: 2026-04-29T15:06:20.383262933-03:00
rendered_js: false
word_count: 565
summary: This guide outlines a structured workflow for reviewing, providing feedback on, and validating code changes produced by CLI-based AI coding agents within the Warp environment.
tags:
    - ai-coding-agents
    - code-review
    - warp-terminal
    - developer-workflow
    - git-diff
    - best-practices
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Review AI-Generated Code

A structured workflow for reviewing and validating code produced by CLI-based AI coding agents. Estimated time: 10 minutes.

## Prerequisites

- **Git-tracked project** — Code review works on any Git repository

## Why Review Matters

AI agents are fast but imperfect. Common issues in AI-generated code:

- **Hallucinated imports** — referencing packages or modules that don't exist
- **Redundant logic** — duplicating existing functionality instead of reusing
- **Questionable architectural decisions** — adding new patterns instead of following existing ones
- **Security gaps** — hardcoded credentials, missing input validation, overly permissive permissions
- **Style drift** — ignoring project conventions for naming, error handling, or file structure
- **Incomplete error handling** — happy-path code that crashes on edge cases

## Step 1: Give the Agent a Task

Start by giving your agent a task (Claude Code, Codex, or Warp's built-in agent). The agent will modify one or more files.

## Step 2: Open the Code Review Panel

Open Warp's [Code Review panel](https://docs.warp.dev/code/code-review) to see every file that changed:

| Method | Shortcut/Location |
|--------|-------------------|
| Keyboard | `⌘+Shift++` (macOS) / `Ctrl+Shift++` (Windows/Linux) |
| Git diff chip | Click the diff chip in the terminal input |
| Review changes button | Click **Review changes** at bottom of conversation |
| Tab bar | Code Review button in top-right corner |

The panel shows uncommitted changes as a visual diff, grouped by file. Additions in green (`+`), removals in red (`-`).

## Step 3: Review Diffs by File

Review changes file-by-file:

- **Browse all changed files** using the file sidebar
- **Switch diff views** — compare against uncommitted changes or against `main`/`master`
- **Click anywhere in the code** to edit diffs directly in the panel

Focus on imports, error handling, and anything touching security or authentication.

Click **Add comment** on any line or block to describe what needs to change. Warp anchors comments to the exact file and line. Add multiple comments, then submit the batch — the agent receives all feedback at once and returns an updated diff.

## Step 4: Submit Feedback and Verify

1. Review updated diff to verify fixes
2. Repeat the cycle until code meets standards: comment → submit → review

> [!info]
> This workflow applies to **any CLI agent** running in Warp — Claude Code, Codex, OpenCode, or Warp's built-in agent.

## Step 5: Run Project Checks Before Committing

Before accepting changes, run your project's test suite, linter, and type checker. Agent-generated code might pass visual review but fail automated checks.

If checks fail, fix issues manually in the Code Review panel or send error output back to the agent as context for another iteration.

> [!info]
> **Quick review checklist**: imports resolve, new code doesn't duplicate existing functionality, credentials aren't hardcoded, error handling covers failure cases, style matches project, tests still pass, and the agent only changed what was asked.

## Productivity Tips

- **Attach diffs as context** — Select a diff hunk in the Code Review panel and attach to your next prompt. See [Selection as context](https://docs.warp.dev/agent-platform/local-agents/agent-context/selection-as-context) for details.
- **Revert individual hunks** — Revert just that hunk from the Code Review panel without undoing the rest
- **Compare against main** — Switch diff view to "Changes vs. main" to see the full scope
- **Use rules to prevent recurring issues** — Add a [Rule](https://docs.warp.dev/agent-platform/capabilities/rules) if the agent repeatedly makes the same mistake
