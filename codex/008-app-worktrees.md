---
title: Worktrees
url: https://developers.openai.com/codex/app/worktrees.md
source: llms
fetched_at: 2026-04-30T10:15:10.750976228-03:00
rendered_js: false
word_count: 939
summary: This document explains how to use worktrees in the Codex app to manage parallel Git tasks and transition code between background worktrees and local development environments.
tags:
    - git
    - worktrees
    - codex
    - version-control
    - development-workflow
    - handoff
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Worktrees

Run multiple independent tasks in the same project without interfering with each other. For Git repositories, [[002-app-automations|automations]] run on dedicated background worktrees. In non-version-controlled projects, automations run directly in the project directory. You can also start threads on a worktree manually and use Handoff to move a thread between Local and Worktree.

## What's a worktree

Uses [Git worktrees](https://git-scm.com/docs/git-worktree) under the hood. A worktree is a second copy (checkout) of your repository. Each worktree has its own copy of every file but shares the same `.git` metadata. This lets you check out and work on multiple branches in parallel.

## Terminology

| Term | Meaning |
|------|---------|
| Local checkout | The repository you created; referred to as **Local** in the app |
| Worktree | A Git worktree created from your local checkout in the Codex app |
| Handoff | The flow that moves a thread between Local and Worktree; Codex handles the required Git operations |

## Why use a worktree

1. Work in parallel with Codex without disturbing your current Local setup.
2. Queue up background work while you stay focused on the foreground.
3. Move a thread into Local later when you're ready to inspect, test, or collaborate more directly.

## Getting started

Requires a Git repository.

1. **Select "Worktree"** in the new thread view. Optionally choose a [[050-app-local-environments|local environment]] to run setup scripts.
2. **Select the starting branch** below the composer — `main`/`master`, a feature branch, or your current branch with unstaged changes.
3. **Submit your prompt.** Codex creates a Git worktree based on the selected branch. By default, works in a [detached HEAD](https://git-scm.com/docs/git-checkout#_detached_head).
4. **Choose where to keep working.** Keep working on the worktree, or hand the thread off to your local checkout.

## Working between Local and Worktree

Local = foreground, Worktree = background. Handoff moves threads between them.

Under the hood, Handoff handles Git operations to move work safely. **Git only allows a branch to be checked out in one place at a time.** If you check out a branch on a worktree, you **can't** check it out in Local at the same time, and vice versa.

### Option 1: Working exclusively on the worktree

Turn your worktree into a branch using the **Create branch here** button in the thread header. From there you can commit, push, and open a pull request on GitHub.

Open your IDE to the worktree using the **Open** button, use the integrated terminal, or anything else from the worktree directory.

If you create a branch on a worktree, you can't check it out in any other worktree, including Local.

### Option 2: Handing a thread off to Local

Click **Hand off** in the thread header and move it to **Local**. Use this when you want to read changes in your usual IDE, run your existing dev server, or validate work in your day-to-day environment.

Each thread keeps the same associated worktree over time. If you hand it back later, Codex returns it to that same background environment.

You can also go the other direction: if you're working in Local and want to free up the foreground, use **Hand off** to move the thread to a worktree.

Since Handoff uses Git operations, `.gitignore`d files won't move with the thread.

## Advanced details

### Codex-managed vs permanent worktrees

| Type | Behavior |
|------|----------|
| **Codex-managed** (default) | Lightweight, disposable; dedicated to one thread; Codex returns the thread to the same worktree if handed back |
| **Permanent** | Long-lived; created from the three-dot menu on a project in the sidebar; not automatically deleted; multiple threads can start from the same worktree |

### How Codex manages worktrees

Created in `$CODEX_HOME/worktrees`. Starting commit = `HEAD` of the selected branch. If you chose a branch with local changes, uncommitted changes are applied. The worktree starts in detached HEAD so Codex can create several worktrees without polluting branches.

### Branch limitations

If you create `feature/a` on a worktree and then try to check it out in Local:
```text
fatal: 'feature/a' is already used by worktree at '<WORKTREE_PATH>'
```

To resolve, check out another branch on the worktree, or use Handoff to move the thread to Local instead.

> [!note]
> Git prevents the same branch from being checked out in multiple worktrees because a branch is a single mutable reference whose meaning is "the current checked-out state." Multiple checkouts would create ambiguity and race conditions around commits, resets, rebases, and merges. Detached HEADs or separate branches avoid this.

### Worktree cleanup

Worktrees can consume significant disk space (repo files, dependencies, build caches). Codex keeps your most recent 15 Codex-managed worktrees by default. Change this limit or turn off automatic deletion in settings.

Codex-managed worktrees **won't** be deleted if:
- A pinned conversation is tied to it
- The thread is still in progress
- It's a permanent worktree

Codex-managed worktrees **are** deleted when:
- You archive the associated thread
- Codex needs to delete older worktrees to stay within the configured limit

Before deleting, Codex saves a snapshot. If you open a conversation after deletion, you'll see the option to restore it.

## FAQ

**Can I control where worktrees are created?**
Not today. Codex creates them under `$CODEX_HOME/worktrees`.

**Can I move a thread between Local and Worktree?**
Yes. Use **Hand off** in the thread header. Codex handles the Git operations. If you hand a thread back to a worktree later, it returns to the same associated worktree.

**What happens to threads if a worktree is deleted?**
Threads remain in history. For Codex-managed worktrees, Codex saves a snapshot before deletion and offers to restore if you reopen the thread. Permanent worktrees are not automatically deleted.

#git #worktrees #parallel-tasks #handoff