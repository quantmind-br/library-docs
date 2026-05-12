---
title: Coding in Warp | Warp
url: https://docs.warp.dev/getting-started/coding-in-warp
source: sitemap
fetched_at: 2026-04-29T15:01:59.553559663-03:00
rendered_js: false
word_count: 303
summary: Configure and utilize codebase context, indexing, Warp Drive, and Rules to improve AI-driven code generation in Warp.
tags:
    - warp-terminal
    - ai-code-generation
    - codebase-indexing
    - context-management
    - agents-config
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
When you enter a Git repo for the first time, Warp indexes your codebase and generates an `AGENTS.md` file. Warp supports single-line and multi-file changes when it detects an opportunity to write code.

Example prompts:

- **Code creation**: "Write a function in JavaScript to debounce an input"
- **Fix errors**: "Fix this TypeScript error."
- **Edit a single file**: "Update all instances of 'var' to 'let' in this file."
- **Batch changes**: "Add headers to all .py files in this directory"

## Context

### Codebase Context

Warp indexes Git-tracked codebases to help agents understand your code and generate accurate, context-aware responses. **No code is stored on Warp servers.**

Manage indexed codebases in **Settings** → **Code** → **Indexing and projects** under "Initialized/indexed folders." You can also toggle automatic indexing for new folders.

Exclude large files by adding them to a `.warpindexingignore` file.

### Warp Drive as Context

Agents pull directly from your [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive) contents — **Workflows**, **Notebooks**, **Prompts**, and **Environment Variables** — to generate more accurate responses.

- Context appears under the "References" or "Derived from" section in the conversation.
- Enabled by default; manage via **Settings** → **Agents** → **Knowledge** → **Warp Drive as Agent Mode Context**.

### Rules

Rules provide persistent context to Agents for smarter, personalized responses.

| Rule Type | Access |
|---|---|
| **Global rules** | [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive) → **Personal** → **Rules** or **Settings** → **Agents** → **Knowledge** → **Manage Rules** |
| **Project-scoped rules** | `AGENTS.md` file in the repo root (filename must be all caps) |

Access project-scoped rules via:
1. File-searcher: `Cmd+O` → search "AGENTS.md"
2. File tree: click the "code" icon when in a repo

From the macOS Menu: `AI > Open Rules`

**Rule examples:**

- Coding standards and best practices
- Project- or workspace-specific guidelines
- Personal preferences for tools, formatting, or behavior
