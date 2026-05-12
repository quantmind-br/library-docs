---
title: Feature support over SSH | Warp
url: https://docs.warp.dev/code/ssh-feature-support
source: sitemap
fetched_at: 2026-04-29T15:03:27.182694523-03:00
rendered_js: false
word_count: 163
summary: This document outlines the capabilities and limitations of Warp's terminal features and AI agent functionality when operating within remote SSH sessions.
tags:
    - warp-terminal
    - ssh-sessions
    - remote-development
    - ai-agent
    - terminal-features
category: guide
optimized: true
optimized_at: 2026-04-29T15:03:27.182694523-03:00
---
When [Warpifying an SSH session](https://docs.warp.dev/terminal/warpify/ssh), core terminal features work locally. Coding-specific features requiring local filesystem access are **not yet available**.

> [!info]
> When a native tool is unavailable, the Agent falls back to terminal commands (`cat`, `sed`, `grep`) to read and edit files.

## Features That Work Over SSH

- **Agent Mode conversations** — chat, request code changes
- **Running shell commands** — execute on remote machine
- **Grep and file glob** — search files/patterns
- **MCP tools** — Model Context Protocol integrations
- **Terminal features** — input editor, completions, autosuggestions, command history, blocks

## Features Not Available Over SSH

| Feature | Fallback |
|---------|----------|
| Codebase Context (indexing/search) | terminal-based search |
| Native file reading | `cat` command |
| Code diffs | `sed` command |
| [[181-code-code-editor|Native code editor]] | — |
| [[178-code-code-editor-file-tree|File tree]] | — |
| [[182-code-code-review|Code Review panel]] | — |
| Computer use | — |

Feature request for codebase context: [GitHub #6831](https://github.com/warpdotdev/Warp/issues/6831)
