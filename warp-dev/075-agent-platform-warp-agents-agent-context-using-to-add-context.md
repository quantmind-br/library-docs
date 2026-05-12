---
title: Using @ to add context | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/agent-context/using-to-add-context
source: sitemap
fetched_at: 2026-04-29T15:04:13.337294001-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-29T18:15:00.000Z
tags:
    - warp-terminal
    - context-menu
    - ai-agents
    - codebase-reference
    - terminal-productivity
    - git-integration
category: guide
word_count: 275
---
Use the `@` context menu to attach files, folders, code symbols, Warp Drive objects, and terminal session blocks as context to a prompt. Typing `@` inside a Git repository opens a context menu for searching and selecting items.

> [!note]
> Works in both natural language mode (Agents) and classic terminal commands for referencing file paths. No codebase indexing required.

## How @ context works

- Search is always relative to the Git repository root, even when working in a subdirectory
- File search is available immediately in any Git-initialized directory
- Search respects `.gitignore` rules and excludes ignored files

## Referencing code symbols

The `@` menu fuzzy-searches for code symbols: functions, classes, interfaces, etc.

Type `@main` to surface a matching `main()` function. Warp inserts the symbol into your prompt with the line number, giving the Agent targeted context for edits or explanations.

## Referencing Warp Drive objects

Reference [[150-knowledge-and-collaboration-warp-drive-prompts|Workflows]], [[149-knowledge-and-collaboration-warp-drive-notebooks|Notebooks]], and [[041-agent-platform-warp-agents-capabilities-overview-rules|Rules]] from Warp Drive.

Selecting an object inserts a reference token into your prompt; the contents are automatically passed as context to the Agent.

## Referencing blocks from other sessions

Bring in output blocks from earlier sessions. Typing `@cargo clippy` surfaces the relevant block, which you can insert into your prompt. The Agent parses the output and generates fixes or explanations.

You can also reference live blocks, not just completed ones.

## Why use @ to reference context?

- Reference exact outputs without copy-pasting entire logs
- Attach relevant files or directories without leaving Warp
- Reuse existing context and knowledge from Warp Drive

## Related pages

- [[212-agent-platform-warp-agents-agent-context|Agent Context]]
- [[037-agent-platform-warp-agents-capabilities-overview-codebase-context|Codebase Context]]
- [[150-knowledge-and-collaboration-warp-drive-prompts|Warp Drive Workflows]]
- [[149-knowledge-and-collaboration-warp-drive-notebooks|Warp Drive Notebooks]]
- [[041-agent-platform-warp-agents-capabilities-overview-rules|Rules]]
