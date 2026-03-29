---
title: ForgeCode
url: https://forgecode.dev/docs/sandbox-feature/
source: sitemap
fetched_at: 2026-03-29T14:52:16.39015138-03:00
rendered_js: false
word_count: 376
summary: This document explains how ForgeCode's Sandbox feature creates isolated development environments using Git worktrees, allowing agents to work on parallel tasks without interfering with each other or the main codebase.
tags:
    - forgecode
    - sandbox
    - git-worktrees
    - isolation
    - parallel-development
    - agent-workflow
    - version-control
category: guide
---

The Sandbox feature in ForgeCode creates isolated development environments using Git worktrees. This allows agents to work on different tasks, experiments, or features in parallel without interfering with each other or your main codebase.

- **Git Repository**: Must be inside a Git repository
- **Parent Directory Access**: Sandboxes are created in the parent directory of the repo root
- **Unique Names**: Each sandbox name must be unique

Learn More About Git Worktrees

ForgeCode sandboxes are built on [Git worktrees](https://git-scm.com/docs/git-worktree). For advanced worktree management, error handling, and low-level details, refer to the official Git documentation.

Sandboxes help agents avoid file conflicts and enable true parallel execution by giving each agent task its own isolated environment without interfering with ongoing work.

Traditional single-workspace approach:

Sandbox workflow with agents:

With sandboxes, each agent task gets its own isolated directory, no conflicts, no waiting, no interference between parallel operations.

Each sandbox is a **Git worktree** - a separate working directory that shares the same `.git` repository but allows independent changes and branches.

### Creating a New Sandbox for Agent Work[​](#creating-a-new-sandbox-for-agent-work "Direct link to Creating a New Sandbox for Agent Work")

This command:

1. Checks if you're in a Git repository (required)
2. Creates a new worktree in `../feature-auth/`
3. Creates or reuses a branch named `feature-auth`
4. Starts the ForgeCode agent in the isolated sandbox directory
5. The agent works exclusively in this environment

### Reusing an Existing Sandbox[​](#reusing-an-existing-sandbox "Direct link to Reusing an Existing Sandbox")

If a sandbox already exists, ForgeCode will detect it and let the agent continue work there:

The system will show:

The agent resumes work in the existing sandbox.

### Parallel Feature Development[​](#parallel-feature-development "Direct link to Parallel Feature Development")

Run multiple agents simultaneously on different features:

Each agent operates independently without interfering with others.

### Safe Experimentation[​](#safe-experimentation "Direct link to Safe Experimentation")

Let agents try different approaches without conflicts:

### Incremental Refactoring[​](#incremental-refactoring "Direct link to Incremental Refactoring")

Break large refactoring tasks into isolated sandbox sessions:

### Bug Investigation and Fixes[​](#bug-investigation-and-fixes "Direct link to Bug Investigation and Fixes")

Isolate bug fixes from ongoing feature work:

### Viewing Active Sandboxes[​](#viewing-active-sandboxes "Direct link to Viewing Active Sandboxes")

Shows all sandboxes where agents have been working.

### Cleanup After Agent Work[​](#cleanup-after-agent-work "Direct link to Cleanup After Agent Work")

Sandboxes persist after the agent completes work. Clean up regularly to keep your workspace organized:

Best Practice

Clean up sandboxes after merging changes to keep your workspace organized. The branch remains in your repository even after removing the worktree.

Uncommitted Changes

If you have uncommitted changes in a sandbox, `git worktree remove` will fail by default. Either commit your changes first or use `git worktree remove --force` to discard them.