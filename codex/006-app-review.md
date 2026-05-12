---
title: Review
url: https://developers.openai.com/codex/app/review.md
source: llms
fetched_at: 2026-04-30T10:15:07.909025041-03:00
rendered_js: false
word_count: 413
summary: This document explains how to use the Codex review pane to manage, inspect, and provide feedback on code changes within a Git repository. It covers navigation, inline commenting, pull request workflows, and Git staging operations.
tags:
    - git-integration
    - code-review
    - version-control
    - workflow-management
    - diff-analysis
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Review

Understand what Codex changed, give targeted feedback, and decide what to keep. Requires a Git repository.

## What changes it shows

Reflects the state of your Git repository, not just Codex edits:
- Changes made by Codex
- Changes you made yourself
- Any other uncommitted changes

Default scope: **uncommitted changes**. Also switch to:
- **All branch changes** — diff against base branch
- **Last turn changes** — most recent assistant turn only

Locally, toggle between **Unstaged** and **Staged** changes.

## Navigating

| Action | Result |
|--------|--------|
| Click file name | Open file in chosen editor |
| Click file name background | Expand/collapse diff |
| `Cmd`+click a line | Open that line in editor |

Stage or revert changes from the review pane.

## Inline comments

Attach feedback directly to specific lines in the diff — often the fastest way to guide Codex.

1. Open the review pane.
2. Hover the target line, click the **+** button.
3. Write feedback and submit.
4. Send a follow-up message to the thread.

After leaving comments, make your intent explicit: "Address the inline comments and keep the scope minimal."

## Code review results

If you use `/review`, comments show up inline in the review pane.

## Pull request reviews

When Codex has GitHub access and the project is on a PR branch, work through PR feedback without leaving the app. The sidebar shows PR context and reviewer feedback; the review pane shows comments alongside the diff.

Install and authenticate the GitHub CLI (`gh auth login`) so Codex can load PR context, review comments, and changed files. If `gh` is missing or unauthenticated, PR details may not appear.

Flow:
1. Open the review pane on the PR branch.
2. Review PR context, comments, and changed files.
3. Ask Codex to fix specific comments.
4. Inspect the resulting diff.
5. Stage, commit, and push when ready.

For GitHub-triggered reviews, see [[026-integrations-github|Use Codex in GitHub]].

## Staging and reverting

Shape the diff before committing:

| Level | Actions |
|-------|---------|
| Entire diff | Stage all / Revert all (review header) |
| Per file | Stage / Unstage / Revert individual file |
| Per hunk | Stage / Unstage / Revert single hunk |

### Staged and unstaged states

Git can represent both staged and unstaged changes in the same file. When this happens, the pane may show "the same file twice" — that's normal Git behavior.

#git #review #code-review #staging