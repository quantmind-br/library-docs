---
title: Codex app commands
url: https://developers.openai.com/codex/app/commands.md
source: llms
fetched_at: 2026-04-30T10:15:04.606230274-03:00
rendered_js: false
word_count: 373
summary: This document provides a reference for the Codex application, detailing available keyboard shortcuts, slash commands for the thread composer, and URL-based deeplinking schemes.
tags:
    - keyboard-shortcuts
    - slash-commands
    - deeplinks
    - app-navigation
    - codex-interface
category: reference
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Codex app commands

## Keyboard shortcuts

| Category | Action | macOS shortcut |
|----------|--------|----------------|
| **General** | Command menu | `Cmd+Shift+P` or `Cmd+K` |
| | Settings | `Cmd+,` |
| | Open folder | `Cmd+O` |
| | Navigate back | `Cmd+[` |
| | Navigate forward | `Cmd+]` |
| | Increase font size | `Cmd++` or `Cmd+=` |
| | Decrease font size | `Cmd+-` or `Cmd+_` |
| | Toggle sidebar | `Cmd+B` |
| | Toggle diff panel | `Cmd+Option+B` |
| | Toggle terminal | `Cmd+J` |
| | Clear terminal | `Ctrl+L` |
| **Thread** | New thread | `Cmd+N` or `Cmd+Shift+O` |
| | Find in thread | `Cmd+F` |
| | Previous thread | `Cmd+Shift+[` |
| | Next thread | `Cmd+Shift+]` |
| | Dictation | `Ctrl+M` |

## Slash commands

Control Codex without leaving the thread composer. Available commands vary based on environment and access.

**Usage:** In thread composer, type `/`, select from list or keep typing to filter (e.g., `/status`).

Explicitly invoke skills by typing `$`. See [[037-skills|Skills]]. Enabled skills also appear in the slash command list.

### Available slash commands

| Command | Description |
|---------|-------------|
| `/feedback` | Open feedback dialog, optionally include logs |
| `/mcp` | Open MCP status to view connected servers |
| `/plan-mode` | Toggle plan mode for multi-step planning |
| `/review` | Start code review mode (uncommitted changes or compare against base branch) |
| `/status` | Show thread ID, context usage, and rate limits |

## Deeplinks

`codex://` URL scheme opens specific parts of the app directly.

| Deeplink | Opens | Query parameters |
|----------|-------|------------------|
| `codex://settings` | Settings | None |
| `codex://skills` | Skills | None |
| `codex://automations` | Inbox in automation create mode | None |
| `codex://threads/<thread-id>` | Local thread (UUID) | None |
| `codex://new` | New thread | `prompt`, `originUrl`, `path` (optional) |

New-thread deeplinks:
- `prompt` — initial composer text
- `path` — absolute path to local directory; makes it active workspace
- `originUrl` — matches current workspace root by Git remote URL. `path` takes precedence if both present

## See also

- [[005-app-features|Features]]
- [[051-app-settings|Settings]]

#shortcuts #slash-commands #deeplinks #codex-app