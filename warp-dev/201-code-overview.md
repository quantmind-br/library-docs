---
title: Code overview | Warp
url: https://docs.warp.dev/code/overview
source: sitemap
fetched_at: 2026-04-29T15:03:20.455140922-03:00
rendered_js: false
word_count: 666
summary: This document provides an overview of Warp Code, an integrated suite of features that utilizes an AI coding agent to assist developers with code generation, editing, refactoring, and project management directly within the terminal.
tags:
    - warp-code
    - coding-agent
    - ai-development
    - code-generation
    - terminal-productivity
    - codebase-context
    - git-integration
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
> [!info]
> Several coding features—including Codebase Context, code diffs, the code editor, and the file tree—are not yet available in SSH or WSL sessions.

## From prompt to production

Warp Code is a suite of features that helps you take agent-generated code from the initial prompt and project setup all the way to deployment and production. Powered by Warp's dedicated coding agent, which consistently ranks among top results on [SWE-bench Verified](https://www.swebench.com/#verified) and [Terminal-Bench](https://www.tbench.ai/leaderboard).

Includes Warp's modern, [native code editor](https://docs.warp.dev/code/code-editor) and a dedicated [Code Review](https://docs.warp.dev/code/code-review) experience for reviewing and editing diffs.

### Coding Agent

Warp's coding agent helps you generate, edit, and manage code directly in the [Agentic Development Environment](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment). It detects opportunities to apply code diffs and surfaces them inline for review without switching to an external IDE.

### How it works

- **Prompt-driven coding** — write natural language prompts like *"Add a retry mechanism to this API call"* or *"Fix the failing unit test in auth.test.ts."*
- **Inline code diffs** — when the agent proposes changes, they appear as diffs you can inspect, modify, or reject
- **Agent steering** — refine prompts, interrupt and retry, or attach context (file, diff, selection) to guide results

> [!info]
> Warp's coding agent only works on local repositories. The agent can make changes on remote or docker repositories but falls back to using terminal commands (`sed`, `grep`) for changes.

## Examples of coding capabilities

### Code creation
- "Write a function in JavaScript to debounce an input"
- "Generate a Python class for managing user sessions with Redis"

### Error-driven fixes
- "Fix the TypeScript error shown in the last build output"
- "Resolve this merge conflict by keeping backend changes and updating tests accordingly"

### Refactoring
- "Update all instances of var to let in this file"
- "Extract the database logic from app.js into a new db.js module and update imports"

### Multi-file and repo-wide changes
- "Add headers to all .py files in this directory"
- "Replace requests with httpx across the codebase, updating imports and error handling"

### Complex workflows
- "Implement OAuth2 authentication, update affected routes, and add tests"
- "Identify functions without test coverage and create Jest test files for them"
- "Optimize slow SQL queries in queries.sql and regenerate migrations"

---

## Getting started with coding in Warp

Each new tab shows a **zero state** with options to proceed.

### 1. Starting a new project

Select **Create a New Project**. Start directly with a prompt (Warp suggests ideas) or configure manually. Warp sets up the repository with an `AGENTS.md` file containing [project rules](https://docs.warp.dev/agent-platform/warp-agents/rules#project-rules) and enables [codebase indexing](https://docs.warp.dev/agent-platform/warp-agents/codebase-context).

### 2. Open an existing repo

Select **Open Repository** to use your computer's file picker. For Git repositories, Warp automatically changes into the directory and runs the `/init` setup command if not already initialized. Warp detects the repository, indexes the codebase, and prepares it for coding.

- For non-Git folders, Warp changes into the directory without initialization
- If an existing project is not initialized, run `/init` manually to bootstrap with a version-controlled `AGENTS.md` file
- This view shows your three most recently used repositories and AI conversations for quick access

### 3. Clone a repo

Select **Clone Repository** to paste a repo link or clone from GitHub. Warp places you in the cloned folder and automatically runs the `/init` flow to set up project rules and indexing.

---

## Learn more about code features

- [Code Editor](https://docs.warp.dev/code/code-editor) — built-in code editor with syntax highlighting, tabs, find and replace, Vim keybindings, and file tree
  - [Language Server Protocol (LSP)](https://docs.warp.dev/code/code-editor/language-server-protocol) — hover info, go-to-definition, find references, inline diagnostics, and format-on-save for Rust, Go, Python, TypeScript/JavaScript, and C/C++
- [Codebase Context](https://docs.warp.dev/agent-platform/warp-agents/codebase-context) — Warp indexes your Git-tracked codebase; no code is stored on Warp servers
- [Code Review](https://docs.warp.dev/code/code-review) — review, edit, and manage Git diffs in real time with options to attach, revert, or open files directly
- [Code Diffs](https://docs.warp.dev/agent-platform/warp-agents/code-diffs) — learn how to review, refine, and apply code changes using the built-in visual diff editor
