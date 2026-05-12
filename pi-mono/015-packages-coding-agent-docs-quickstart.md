---
title: Quickstart
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/quickstart.md
source: git
fetched_at: 2026-05-03T09:31:17.372241964-03:00
rendered_js: false
word_count: 343
summary: Install, authenticate, and use the Pi coding agent to interact with codebases via interactive and non-interactive CLI sessions.
tags:
    - coding-agent
    - cli-tool
    - developer-productivity
    - ai-assistant
    - terminal-application
    - software-development
category: tutorial
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Quickstart

Get from install to a useful first pi session.

## Install

```bash
npm install -g @mariozechner/pi-coding-agent
cd /path/to/project
pi
```

## Authenticate

### Option 1: subscription login

Start pi and run `/login`, then select a provider (Claude Pro/Max, ChatGPT Plus/Pro, GitHub Copilot).

### Option 2: API key

Set an API key before launching:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pi
```

Or run `/login` and select an API-key provider to store the key in `~/.pi/agent/auth.json`.

See [[053-packages-coding-agent-docs-providers|Providers]] for all supported providers, environment variables, and cloud-provider setup.

## First session

Type a request and press Enter:

```
Summarize this repository and tell me how to run its checks.
```

Default tools:

| Tool | Purpose |
|------|---------|
| `read` | Read files |
| `write` | Create or overwrite files |
| `edit` | Patch files |
| `bash` | Run shell commands |

Additional read-only tools (`grep`, `find`, `ls`) available through tool options. Pi runs in the current working directory. Use git or another checkpointing workflow for easy rollback.

## Give pi project instructions

Pi loads context files at startup. Add an `AGENTS.md` file:

```markdown
# Project Instructions

- Run `npm run check` after code changes.
- Do not run production migrations locally.
- Keep responses concise.
```

Pi loads:
- `~/.pi/agent/AGENTS.md` — global instructions
- `AGENTS.md` or `CLAUDE.md` from parent/current directory

Restart pi or run `/reload` after changing context files.

## Common things to try

### Reference files

Type `@` in the editor to fuzzy-search files, or pass on the command line:

```bash
pi @README.md "Summarize this"
pi @src/app.ts @src/app.test.ts "Review these together"
```

Images: paste with Ctrl+V (Alt+V on Windows) or drag into supported terminals.

### Run shell commands

```
!npm run lint
```

Command output is sent to the model. Use `!!command` to run without adding output to context.

### Switch models

- `/model` or Ctrl+L to choose a model
- Shift+Tab to cycle thinking level
- Ctrl+P / Shift+Ctrl+P to cycle through scoped models

### Continue later

```bash
pi -c                  # Continue most recent session
pi -r                  # Browse previous sessions
pi --session <path|id> # Open a specific session
```

Inside pi: `/resume`, `/new`, `/tree`, `/fork`, `/clone`.

### Non-interactive mode

```bash
pi -p "Summarize this codebase"
cat README.md | pi -p "Summarize this text"
pi -p @screenshot.png "What's in this image?"
```

Use `--mode json` for JSON event output or `--mode rpc` for process integration.

## Next steps

- [[105-packages-coding-agent-docs-usage|Using Pi]] — interactive mode, slash commands, sessions, context files, CLI reference
- [[053-packages-coding-agent-docs-providers|Providers]] — authentication and model setup
- [[103-packages-coding-agent-docs-settings|Settings]] — global and project configuration
- [[099-packages-coding-agent-docs-keybindings|Keybindings]] — shortcuts and customization
- [[026-packages-coding-agent-docs-packages|Pi Packages]] — install shared extensions, skills, prompts, themes

Platform notes: [[056-packages-coding-agent-docs-windows|Windows]], [[030-packages-coding-agent-docs-termux|Termux]], [[055-packages-coding-agent-docs-tmux|tmux]], [[049-packages-coding-agent-docs-terminal-setup|Terminal setup]], [[054-packages-coding-agent-docs-shell-aliases|Shell aliases]]

#coding-agent #cli-tool #ai-assistant
