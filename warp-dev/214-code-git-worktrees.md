---
title: Git Worktrees | Warp
url: https://docs.warp.dev/code/git-worktrees
source: sitemap
fetched_at: 2026-04-29T15:03:25.804856411-03:00
rendered_js: false
word_count: 370
summary: This document explains how the Warp terminal integrates with Git worktrees, enabling users to manage multiple branches simultaneously across different directories with full terminal feature support.
tags:
    - git-worktrees
    - terminal-productivity
    - version-control
    - warp-terminal
    - workflow-optimization
    - git-integration
category: concept
optimized: true
optimized_at: 2026-04-29T15:04:00Z
---
Warp natively supports [Git worktrees](https://git-scm.com/docs/git-worktree) — a Git feature that lets you check out multiple branches simultaneously in separate directories, all backed by the same repository. Unlike switching branches, worktrees let you have `~/project` on `main` and `~/project-wt/feature-x` on `feature-x` at the same time with no stashing or context-switching.

## How worktrees work in Warp

Warp automatically detects worktree checkouts. When you open a terminal in a worktree directory, Warp recognizes the `.git` file that points back to the main repository and treats the worktree as a fully functional repository:

- **Code Review panel** — Each worktree has its own Code Review panel showing uncommitted changes for that worktree's branch. Review diffs, revert hunks, and discard changes independently in each worktree.
- **Git Status chip** — The Git diff chip and branch indicator in the input bar reflect the correct branch and change counts for whichever worktree your terminal is in.
- **File watching** — Warp watches both the worktree's working directory and the shared `.git` directory. Changes to shared Git state (such as new commits pushed to the remote) are detected and propagated across all open worktrees.
- **Codebase Context** — Each worktree is indexed independently for [Codebase Context](https://docs.warp.dev/agent-platform/warp-agents/codebase-context), so Agents have accurate context for whichever worktree you're working in.
- **Repository-scoped features** — Project rules (`AGENTS.md`, `WARP.md`), ignore files, and other repository-scoped settings work correctly within each worktree.

## When to use worktrees

- **Reviewing a PR while working on your own branch** — Open the PR branch in a separate worktree without disrupting in-progress work.
- **Running tests on one branch while coding on another** — Keep a long test suite running in one worktree while continuing development in another.
- **Parallel local agent work** — When orchestrating multiple local agents on the same repository, each agent can operate in its own worktree to avoid file conflicts.

## Creating a worktree

To create a new worktree from your terminal:

```bash
git worktree add <path> <branch>
```

Once created, open the worktree directory in a new Warp tab or pane. Warp detects it automatically — no additional configuration needed.

> [!info]
> Commit state change notifications (e.g. detecting new commits) may be slightly delayed in worktrees compared to standard repositories. Warp is actively improving this.