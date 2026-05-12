---
title: Code Review panel | Warp
url: https://docs.warp.dev/code/code-review
source: sitemap
fetched_at: 2026-04-29T15:03:25.83015349-03:00
rendered_js: false
word_count: 376
summary: This document explains how to utilize the Code Review panel in Warp to inspect, manage, revert, and iterate on uncommitted Git changes while collaborating with AI agents.
tags:
    - warp-terminal
    - git-integration
    - code-review
    - version-control
    - ai-agent
    - developer-tools
    - diff-management
category: guide
optimized: true
optimized_at: 2026-04-29T15:03:25.83015349-03:00
---
Inspect, edit, and manage code changes directly in Warp. Integrates with Git and Warp's Agents. Any uncommitted changes appear automatically; switching branches or saving files updates the panel instantly.

## Open the Code Review Panel

| Method | Description |
|--------|-------------|
| `CMD – SHIFT – +` / `CTRL – SHIFT – +` | keyboard shortcut |
| Git diff chip | terminal mode shows modified files count. Click to open. |
| "Review changes" button | appears in Agent conversations after code edits |
| Toolbelt chips | view changed files at bottom right during Agent conversation |
| Tab bar button | "Code review" button next to avatar in any Git repo |

> [!tip]
> Default position is right pane; drag to reposition.

## Viewing Changed Files

Open the file sidebar to browse all changed files. Click a file to scroll to it.

## Review Diffs

Default view: **uncommitted changes** on current branch, excluding `.gitignore` files.

Switch between:
1. **Uncommitted changes** — local edits on current branch
2. **Changes vs. main** — compare against `main`/`master` for PR preview
3. **Changes vs. another branch** — arbitrary branch comparison for stacked PRs

Warp auto-detects the target branch.

## Attach Diffs as Context

Attach entire diffs to Agent prompts for context-aware feedback or explanations. See [Selection as Context](https://docs.warp.dev/agent-platform/warp-agents/agent-context/selection-as-context).

## Revert Diffs

Click the revert option in the gutter next to each diff hunk. Changes apply immediately to the working directory.

## Open Files from Code Review

Click the **expand button** (right-most on header) to open in a new editor tab:
- View full file beyond changed lines
- Scroll, edit, search, save
- Changes sync back to Code Review pane

From the file header, attach file diff as context or discard all changes on that file.

## Directly Edit Diffs

Edit diffs directly in the Code Review pane.

## Send Comments to Running Agent

Leave inline comments and send to any supported CLI agent (Claude Code, Codex, etc.) via [Interactive Code Review](https://docs.warp.dev/agent-platform/warp-agents/interactive-code-review). See [Third-Party CLI Agents](https://docs.warp.dev/agent-platform/cli-agents/overview).

## Discard All Changes

Click "Discard all" to restore every file to its base branch state.

> [!warning]
> Confirm before discarding. Back up anything you want to keep.

> [!info]
> Warp natively supports Git worktrees. See [[183-code-ssh-feature-support|Git worktrees]].
