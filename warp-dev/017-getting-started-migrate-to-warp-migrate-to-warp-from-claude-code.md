---
title: Migrate to Warp from Claude Code | Warp
url: https://docs.warp.dev/getting-started/migrate-to-warp/migrate-to-warp-from-claude-code
source: sitemap
fetched_at: 2026-04-29T15:02:03.679319584-03:00
rendered_js: false
word_count: 665
summary: This document details how to use Claude Code within the Warp terminal and provides instructions for transitioning from Claude Code to Warp's native agentic development environment.
tags:
    - warp-terminal
    - claude-code
    - agentic-workflow
    - cli-agents
    - migration-guide
    - developer-productivity
category: guide
optimized: true
optimized_at: 2026-04-29T20:15:00Z
---
# Migrate to Warp from Claude Code

Claude Code is a CLI agent (not a terminal emulator) that runs inside any terminal. Warp is an agentic development environment with a built-in [[181-code-code-editor|code editor]], [[182-code-code-review|Code Review]], [[144-knowledge-and-collaboration-warp-drive|Warp Drive]], and [[072-agent-platform-warp-agents-agent-context-mcp|MCP]] support.

Choose your path:

1. **Use Claude Code inside Warp** — keep Claude Code as your coding agent and run it in Warp's terminal.
2. **Switch to Warp's Agent Mode** — replace Claude Code with Warp's built-in agent.

---

## Path 1: Use Claude Code Inside Warp

Warp provides first-class support for Claude Code through its [third-party CLI agents](https://docs.warp.dev/agent-platform/cli-agents) integration. Open a new tab and run `claude` to begin.

Warp auto-detects Claude Code and unlocks IDE-level features:

- **Agent notifications** — in-app and desktop alerts when Claude Code needs input. Requires a one-time plugin install (Warp prompts you).
- **Inline code review** — send review comments directly to the agent from Warp's [[182-code-code-review|Code Review]] panel.
- **Tab Configs** — save and reopen Claude Code session layouts.

See [Claude Code in Warp](https://docs.warp.dev/agent-platform/cli-agents/claude-code) and the [How to set up Claude Code](https://docs.warp.dev/guides/integrations/how-to-set-up-claude-code) guide for full setup steps.

### Tips

- **Terminal mode, not Agent Mode.** Press `⌘+I` (macOS) or `Ctrl+I` (Linux/Windows) to toggle modes if you're in Agent Mode by accident.
- **`Shift+Enter` for newlines.** If it submits instead, verify you're in terminal mode and on a recent Warp version.
- **Copy/paste.** Warp enables bracketed paste by default — multi-line pastes into Claude Code work without extra config.
- **Resuming after restart.** Warp's [[247-terminal-sessions-session-restoration|session restoration]] preserves tabs/panes, but not running processes. Use Claude Code's built-in resume (`claude --resume`) to continue.

### API Keys and Authentication

Claude Code handles its own authentication. Warp does not proxy its network calls. Configure `ANTHROPIC_API_KEY` via [[148-knowledge-and-collaboration-warp-drive-environment-variables|Warp Drive environment variables]] to share across sessions without committing to shell config files.

---

## Path 2: Switch to Agent Mode from Claude Code

1. Open a new tab in Warp.
2. Press `⌘+Enter` (macOS) or `Ctrl+Shift+Enter` (Linux/Windows) to switch to [[198-agent-platform-warp-agents-capabilities-overview|Agent Mode]].
3. Describe what you want in natural language.

Warp's agent reads your codebase, runs commands, and edits files like Claude Code.

### What Transfers: Context and Rules

| Claude Code | Warp Equivalent |
|-------------|-----------------|
| `CLAUDE.md` | `AGENTS.md` or `WARP.md` (repo root) |
| `CLAUDE.md` scoped | [[041-agent-platform-warp-agents-capabilities-overview-rules|Rules]] in Warp Drive |
| Implicit file context | [[037-agent-platform-warp-agents-capabilities-overview-codebase-context|Codebase Context]] (Git-tracked files indexed on directory open) |

**To migrate:** rename `CLAUDE.md` to `AGENTS.md`, or run `/init` in Agent Mode to generate one.

Additional context sources:

- **[[037-agent-platform-warp-agents-capabilities-overview-codebase-context|Codebase Context]]** — Warp indexes Git-tracked files on directory open.
- **[[041-agent-platform-warp-agents-capabilities-overview-rules|Rules]]** — global and project-scoped, auto-picked from repo root.
- **[[144-knowledge-and-collaboration-warp-drive|Warp Drive]]** — notebooks, workflows, environment variables.
- **[[220-knowledge-and-collaboration-warp-drive-agent-mode-context|Agent Mode context]]** — pin specific files/notebooks to a conversation.
- **[[072-agent-platform-warp-agents-agent-context-mcp|MCP]]** — configured servers give agent access to external tools.

### What to Reconfigure

| Item | Action |
|------|--------|
| `CLAUDE.md` | Rename to `AGENTS.md` (or copy into a [[041-agent-platform-warp-agents-capabilities-overview-rules|Rule]] for project scoping) |
| Model | Use model selector per conversation. See [[039-agent-platform-warp-agents-capabilities-overview-model-choice|model choice]] (supports Claude, GPT, Gemini, Auto) |

### Key Differences from Claude Code

- **Tight terminal integration** — Agent Mode sees full terminal state (open files, command history, environment variables) without manual context.
- **Parallel agents** — run multiple conversations across tabs, each with independent state.
- **Code Review built in** — diffs open in Warp's [[182-code-code-review|Code Review]] panel.
- **Cloud orchestration** — offload long-running/scheduled work to [Oz](https://docs.warp.dev/agent-platform/cloud-agents/overview).

---

## Warp-Native Equivalents

| Claude Code Feature | Warp Equivalent |
|---------------------|------------------|
| CLI agent in terminal | Warp Agent Mode |
| `CLAUDE.md` | `AGENTS.md` / `WARP.md` |
| Composer/Agent tabs | Agent Mode tabs |
| Tab context files | [[220-knowledge-and-collaboration-warp-drive-agent-mode-context|Agent Mode context]] |
| MCP servers | [[072-agent-platform-warp-agents-agent-context-mcp|MCP]] |
| Model selection | [[039-agent-platform-warp-agents-capabilities-overview-model-choice|Model selector]] |
| Code review in terminal | [[182-code-code-review|Code Review panel]] |
| Cloud agents | [Oz](https://docs.warp.dev/agent-platform/cloud-agents/overview) |

For a deeper tour of Agent Mode, see [[013-getting-started-coding-in-warp|Coding in Warp]] and the [Warp Agents docs](https://docs.warp.dev/agent-platform/warp-agents).

#migration-guide #claude-code #agentic-workflow