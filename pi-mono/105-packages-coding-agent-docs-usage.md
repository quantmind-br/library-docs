---
title: Using Pi
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/usage.md
source: git
fetched_at: 2026-05-03T09:31:30.859390414-03:00
rendered_js: false
word_count: 1177
summary: This document provides a comprehensive overview of daily usage for the Pi tool, covering its interactive interface, slash commands, session management, context configuration, and CLI options.
tags:
    - pi
    - cli-tools
    - session-management
    - command-reference
    - developer-productivity
    - terminal-interface
category: reference
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Using Pi

Day-to-day usage details beyond the quickstart.

## Interactive Mode

![Interactive Mode](images/interactive-mode.png)

Four main areas:

- **Startup header** — shortcuts, loaded context, prompt templates, skills, extensions
- **Messages** — user messages, responses, tool calls/results, notifications, errors, extension UI
- **Editor** — input; border color indicates thinking level
- **Footer** — working directory, session name, tokens/cache, cost, context usage, current model

The editor can be temporarily replaced by built-in UI (`/settings`) or custom extension UI.

### Editor Features

| Feature | How |
|---------|-----|
| File reference | Type `@` to fuzzy-search project files |
| Path completion | Press Tab |
| Multi-line input | Shift+Enter, or Ctrl+Enter on Windows Terminal |
| Images | Paste with Ctrl+V, Alt+V on Windows, or drag into terminal |
| Shell command | `!command` runs and sends output to model |
| Hidden shell command | `!!command` runs without sending output |
| External editor | Ctrl+G opens `$VISUAL` or `$EDITOR` |

See [[099-packages-coding-agent-docs-keybindings|Keybindings]] for all shortcuts.

## Slash Commands

Type `/` to open command completion. Extensions register custom commands, skills as `/skill:name`, prompt templates via `/templatename`.

| Command | Description |
|---------|-------------|
| `/login`, `/logout` | Manage OAuth or API-key credentials |
| `/model` | Switch models |
| `/scoped-models` | Enable/disable models for Ctrl+P cycling |
| `/settings` | Thinking level, theme, message delivery, transport |
| `/resume` | Pick from previous sessions |
| `/new` | Start a new session |
| `/name <name>` | Set session display name |
| `/session` | Show session file, ID, messages, tokens, cost |
| `/tree` | Jump to any point in session and continue |
| `/fork` | Create new session from previous user message |
| `/clone` | Duplicate current active branch into new session |
| `/compact [prompt]` | Manually compact context |
| `/copy` | Copy last assistant message to clipboard |
| `/export [file]` | Export session to HTML |
| `/share` | Upload as private GitHub gist with shareable HTML |
| `/reload` | Reload keybindings, extensions, skills, prompts, context files |
| `/hotkeys` | Show all keyboard shortcuts |
| `/changelog` | Display version history |
| `/quit` | Quit pi |

## Message Queue

Submit messages while the agent is working:

| Key | Action |
|-----|--------|
| Enter | Queue steering message, delivered after current turn |
| Alt+Enter | Queue follow-up message, delivered after agent finishes |
| Escape | Abort and restore queued messages to editor |
| Alt+Up | Retrieve queued messages back to editor |

> [!warning]
> On Windows Terminal, Alt+Enter is fullscreen by default. Remap as described in [[049-packages-coding-agent-docs-terminal-setup|Terminal Setup]].

Configure delivery in [[103-packages-coding-agent-docs-settings|Settings]] with `steeringMode` and `followUpMode`.

## Sessions

Sessions saved automatically to `~/.pi/agent/sessions/`, organized by working directory.

| Option | Description |
|--------|-------------|
| `pi -c` | Continue most recent session |
| `pi -r` | Browse and select a session |
| `pi --no-session` | Ephemeral mode; do not save |
| `pi --session <path\|id>` | Use specific session file or UUID |
| `pi --fork <path\|id>` | Fork a session into new file |

See [[029-packages-coding-agent-docs-sessions|Sessions]] and [[037-packages-coding-agent-docs-compaction|Compaction]] for details.

## Context Files

Pi loads `AGENTS.md` or `CLAUDE.md` from:
- `~/.pi/agent/AGENTS.md` (global)
- parent directories (walking up from CWD)
- current directory

Disable with `--no-context-files` or `-nc`.

### System Prompt Files

Replace default system prompt:
- `.pi/SYSTEM.md` (project)
- `~/.pi/agent/SYSTEM.md` (global)

Append without replacing: `APPEND_SYSTEM.md` in either location.

## Exporting & Sharing

| Command | Description |
|---------|-------------|
| `/export [file]` | Write session to HTML |
| `/share` | Upload as private GitHub gist |

For publishing sessions to Hugging Face datasets, see [`badlogic/pi-share-hf`](https://github.com/badlogic/pi-share-hf).

## CLI Reference

```bash
pi [options] [@files...] [messages...]
```

### Package Commands

```bash
pi install <source> [-l]     # Install package, -l for project-local
pi remove <source> [-l]       # Remove package
pi uninstall <source> [-l]    # Alias for remove
pi update [source|self|pi]   # Update pi and packages; skips pinned
pi update --extensions       # Update packages only
pi update --self             # Update pi only
pi update --extension <src>  # Update one package
pi list                      # List installed packages
pi config                    # Enable/disable package resources
```

See [[026-packages-coding-agent-docs-packages|Pi Packages]] for package sources and security notes.

### Modes

| Flag | Description |
|------|-------------|
| default | Interactive mode |
| `-p`, `--print` | Print response and exit |
| `--mode json` | Output all events as JSON lines (see [[098-packages-coding-agent-docs-json|JSON mode]]) |
| `--mode rpc` | RPC mode over stdin/stdout (see [[100-packages-coding-agent-docs-rpc|RPC mode]]) |
| `--export <in> [out]` | Export session to HTML |

In print mode, pi reads piped stdin and merges into initial prompt:

```bash
cat README.md | pi -p "Summarize this text"
```

### Model Options

| Option | Description |
|--------|-------------|
| `--provider <name>` | Provider: `anthropic`, `openai`, `google`, etc. |
| `--model <pattern>` | Model pattern or ID; supports `provider/id` and `:<thinking>` |
| `--api-key <key>` | API key, overriding environment variables |
| `--thinking <level>` | `off`, `minimal`, `low`, `medium`, `high`, `xhigh` |
| `--models <patterns>` | Comma-separated patterns for Ctrl+P cycling |
| `--list-models [search]` | List available models |

### Session Options

| Option | Description |
|--------|-------------|
| `-c`, `--continue` | Continue most recent session |
| `-r`, `--resume` | Browse and select a session |
| `--session <path\|id>` | Use specific session file or UUID |
| `--fork <path\|id>` | Fork into new session |
| `--session-dir <dir>` | Custom session storage directory |
| `--no-session` | Ephemeral mode; do not save |

### Tool Options

| Option | Description |
|--------|-------------|
| `--tools <list>`, `-t <list>` | Allowlist specific tools |
| `--no-builtin-tools`, `-nbt` | Disable built-in tools |
| `--no-tools`, `-nt` | Disable all tools |

Built-in tools: `read`, `bash`, `edit`, `write`, `grep`, `find`, `ls`.

### Resource Options

| Option | Description |
|--------|-------------|
| `-e`, `--extension <source>` | Load extension from path, npm, or git |
| `--no-extensions` | Disable extension discovery |
| `--skill <path>` | Load skill |
| `--no-skills` | Disable skill discovery |
| `--prompt-template <path>` | Load prompt template |
| `--no-prompt-templates` | Disable template discovery |
| `--theme <path>` | Load theme |
| `--no-themes` | Disable theme discovery |
| `--no-context-files`, `-nc` | Disable `AGENTS.md`/`CLAUDE.md` discovery |

Combine `--no-*` with explicit flags to load exactly what you need:

```bash
pi --no-extensions -e ./my-extension.ts
```

### Other Options

| Option | Description |
|--------|-------------|
| `--system-prompt <text>` | Replace default prompt |
| `--append-system-prompt <text>` | Append to system prompt |
| `--verbose` | Force verbose startup |
| `-h`, `--help` | Show help |
| `-v`, `--version` | Show version |

### File Arguments

Prefix files with `@` to include in message:

```bash
pi @prompt.md "Answer this"
pi -p @screenshot.png "What's in this image?"
pi @code.ts @test.ts "Review these files"
```

### Examples

```bash
# Interactive with initial prompt
pi "List all .ts files in src/"

# Non-interactive
pi -p "Summarize this codebase"

# Non-interactive with piped stdin
cat README.md | pi -p "Summarize this text"

# Different model
pi --provider openai --model gpt-4o "Help me refactor"

# Model with thinking level shorthand
pi --model sonnet:high "Solve this complex problem"

# Limit model cycling
pi --models "claude-*,gpt-4o"

# Read-only mode
pi --tools read,grep,find,ls -p "Review the code"
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| `PI_CODING_AGENT_DIR` | Override config directory (default: `~/.pi/agent`) |
| `PI_CODING_AGENT_SESSION_DIR` | Override session storage directory |
| `PI_PACKAGE_DIR` | Override package directory (useful for Nix/Guix) |
| `PI_OFFLINE` | Disable all startup network operations |
| `PI_SKIP_VERSION_CHECK` | Skip version update check |
| `PI_TELEMETRY` | Override telemetry: `1`/`true`/`yes` or `0`/`false`/`no` |
| `PI_CACHE_RETENTION` | Set to `long` for extended prompt cache |
| `VISUAL`, `EDITOR` | External editor for Ctrl+G |

## Design Principles

Pi keeps the core small and pushes workflow-specific behavior into extensions, skills, prompt templates, and packages.

It intentionally does not include built-in MCP, sub-agents, permission popups, plan mode, to-dos, or background bash. Build or install those workflows as extensions/packages, or use external tools like containers and tmux.

For the full rationale, read the [blog post](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/).

#pi #cli-tools #session-management #command-reference #developer-productivity #terminal-interface