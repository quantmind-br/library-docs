---
title: Project Workflow Guides
url: https://docs.bmad-method.org//llms-full.txt
source: llms
fetched_at: 2026-05-19T08:33:05.038451722-03:00
rendered_js: false
summary: Guides for working with established projects, creating project context, quick fixes, and document sharding.
tags:
    - bmad-method
    - project-management
    - existing-projects
    - quick-fixes
category: guide
optimized: true
optimized_at: 2026-05-19T11:33:05Z
word_count: 909
---
# Project Workflow Guides

Use BMad Method effectively when working on existing projects and legacy codebases.

> [!info] Prerequisites
> - BMad Method installed (`npx bmad-method install`)
> - An existing codebase
> - An AI-powered IDE (Claude Code or Cursor)

## Step 1: Clean Up Completed Planning Artifacts

Archive or delete completed PRD epics and stories. Remove them from:
- `docs/`
- `_bmad-output/planning-artifacts/`
- `_bmad-output/implementation-artifacts/`

## Step 2: Create Project Context

> [!tip] Recommended for Existing Projects
> Generate `project-context.md` to capture codebase patterns and conventions. This ensures AI agents follow your established practices.

Run:
```bash
bmad-generate-project-context
```

This scans your codebase for:
- Technology stack and versions
- Code organization patterns
- Naming conventions
- Testing approaches
- Framework-specific patterns

Review and refine the generated file, or create it manually at `_bmad-output/project-context.md`.

[Learn more about project context](../explanation/project-context.md)

## Step 3: Maintain Quality Project Documentation

Your `docs/` folder should contain succinct, well-organized documentation covering:
- Intent and business rationale
- Business rules
- Architecture
- Other relevant project information

For complex projects, use the `bmad-document-project` workflow. It scans your entire project and documents its actual current state.

## Step 4: Get Help

### BMad-Help

**Run `bmad-help` anytime you're unsure what to do next.** It:
- Inspects your project to see what's already been done
- Shows options based on installed modules
- Understands natural language queries

```text
bmad-help I have an existing Rails app, where should I start?
bmad-help What's the difference between quick-flow and full method?
bmad-help Show me what workflows are available
```

BMad-Help also **automatically runs at the end of every workflow**, providing guidance on what to do next.

### Choosing Your Approach

| Scope | Recommended Approach |
| --- | --- |
| Small updates or additions | Run `bmad-quick-dev` to clarify intent, plan, implement, and review in a single workflow. The full four-phase BMad Method is likely overkill. |
| Major changes or additions | Start with the BMad Method, applying as much or as little rigor as needed. |

### During PRD Creation

When creating a brief or jumping directly into the PRD, ensure the agent:
- Finds and analyzes existing project documentation
- Reads proper context about your current system

Guide the agent explicitly if needed, but the goal is ensuring new features integrate well with your existing system.

### UX Considerations

UX work is optional. The decision depends not on whether your project has a UX, but on:
- Whether you will be working on UX changes
- Whether significant new UX designs or patterns are needed

Simple updates to existing screens do not require a full UX process.

### Architecture Considerations

When doing architecture, ensure the architect:
- Uses the proper documented files
- Scans the existing codebase

This prevents reinventing the wheel or making decisions that misalign with your existing architecture.

### More Information

- [Quick Fixes](./quick-fixes.md) - Bug fixes and ad-hoc changes
- [Established Projects FAQ](../explanation/established-projects-faq.md) - Common questions about working on established projects

## Quick Fixes

Use **Quick Dev** for bug fixes, refactorings, or small targeted changes that don't require the full BMad Method.

### When to Use This

- Bug fixes with a clear, known cause
- Small refactorings (rename, extract, restructure) contained within a few files
- Minor feature tweaks or configuration changes
- Dependency updates

> [!info] Prerequisites
> - BMad Method installed (`npx bmad-method install`)
> - An AI-powered IDE (Claude Code, Cursor, or similar)

### Steps

#### 1. Start a Fresh Chat

Open a **fresh chat session** in your AI IDE. Reusing a session from a previous workflow can cause context conflicts.

#### 2. Give It Your Intent

Quick Dev accepts free-form intent — before, with, or after the invocation. Examples:

```text
run quick-dev — Fix the login validation bug that allows empty passwords.
```

```text
run quick-dev — fix https://github.com/org/repo/issues/42
```

```text
run quick-dev — implement the intent in _bmad-output/implementation-artifacts/my-intent.md
```

```text
I think the problem is in the auth middleware, it's not checking token expiry.
Let me look at it... yeah, src/auth/middleware.ts line 47 skips
the exp check entirely. run quick-dev
```

```text
run quick-dev
> What would you like to do?
Refactor UserService to use async/await instead of callbacks.
```

Plain text, file paths, GitHub issue URLs, bug tracker links — anything the LLM can resolve to a concrete intent.

#### 3. Answer Questions and Approve

Quick Dev may ask clarifying questions or present a short spec for approval before implementing. Answer its questions and approve when satisfied.

#### 4. Review and Push

Quick Dev implements the change, reviews its own work, patches issues, and commits locally. When done, it opens the affected files in your editor.

- Skim the diff to confirm the change matches your intent
- If something looks off, tell the agent what to fix — it can iterate in the same session

Once satisfied, push the commit. Quick Dev will offer to push and create a PR for you.

> [!warning] If Something Breaks
> If a pushed change causes unexpected issues, use `git revert HEAD` to undo the last commit cleanly. Then start a fresh chat and run Quick Dev again.

### What You Get

- Modified source files with the fix or refactoring applied
- Passing tests (if your project has a test suite)
- A ready-to-push commit with a conventional commit message

### Deferred Work

Quick Dev keeps each run focused on a single goal. If your request contains multiple independent goals, or if review surfaces pre-existing issues unrelated to your change, Quick Dev defers them to `deferred-work.md` in your implementation artifacts directory.

Check this file after a run — it's your backlog. Each deferred item can be fed into a fresh Quick Dev run later.

### When to Upgrade to Formal Planning

Consider using the full BMad Method when:
- The change affects multiple systems or requires coordinated updates across many files
- You are unsure about the scope and need requirements discovery first
- You need documentation or architectural decisions recorded for the team

See [Quick Dev](../explanation/quick-dev.md) for more on how Quick Dev fits into the BMad Method.

#project-workflow #quick-dev #existing-projects
