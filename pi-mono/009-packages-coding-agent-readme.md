---
title: README
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/README.md
source: git
fetched_at: 2026-05-03T09:31:04.457283186-03:00
rendered_js: false
word_count: 2217
summary: Pi is a minimalist, extensible terminal-based coding agent integrating LLMs via customizable extensions, skills, prompt templates, and themes.
tags:
    - coding-agent
    - terminal-tool
    - llm-integration
    - cli-utility
    - developer-tools
    - ai-assistant
category: guide
optimized: true
optimized_at: 2026-05-03T12:32:00Z
---
# Pi Coding Agent

Minimal terminal coding harness. Adapt pi to your workflows via TypeScript [Extensions](#extensions), [Skills](#skills), [Prompt Templates](#prompt-templates), and [Themes](#themes) without forking pi internals. Share via [Pi Packages](#pi-packages) on npm or git.

> New issues/PRs from new contributors are auto-closed. Maintainers review daily. See [[116-contributing.md|Contributing]].

## Quick Start

```bash
npm install -g @mariozechner/pi-coding-agent
export ANTHROPIC_API_KEY=sk-ant-...  # or use /login for OAuth
pi
```

By default, pi gives the model four tools: `read`, `write`, `edit`, `bash`. Add capabilities via [skills](#skills), [prompt templates](#prompt-templates), [extensions](#extensions), or [pi packages](#pi-packages).

**Platform notes:** [[056-packages-coding-agent-docs-windows|Windows]] | [[030-packages-coding-agent-docs-termux|Termux (Android)]] | [[055-packages-coding-agent-docs-tmux|tmux]] | [[049-packages-coding-agent-docs-terminal-setup|Terminal setup]] | [[054-packages-coding-agent-docs-shell-aliases|Shell aliases]]

## Providers & Models

pi maintains tool-capable model lists per built-in provider, updated per release. Authenticate via `/login` or API key, select via `/model` (Ctrl+L).

**Subscriptions:** Anthropic Claude Pro/Max, OpenAI ChatGPT Plus/Pro (Codex), GitHub Copilot

**API keys:** Anthropic, OpenAI, Azure OpenAI, DeepSeek, Google Gemini/Vertex, Amazon Bedrock, Mistral, Groq, Cerebras, Cloudflare AI Gateway/Workers AI, xAI, OpenRouter, Vercel AI Gateway, ZAI, OpenCode Zen/Go, Hugging Face, Fireworks, Kimi For Coding, MiniMax, Xiaomi MiMo

See [[053-packages-coding-agent-docs-providers|Providers]] for detailed setup. **Custom providers:** Add via `~/.pi/agent/models.json` for OpenAI/Anthropic/Google APIs, or use extensions for custom APIs/OAuth. See [[052-packages-coding-agent-docs-models|Models]] and [[022-packages-coding-agent-docs-custom-provider|Custom Providers]].

## Interactive Mode

Interface layout:

- **Startup header** — shortcuts (`/hotkeys`), loaded AGENTS.md, prompt templates, skills, extensions
- **Messages** — your messages, assistant responses, tool calls/results, notifications, errors, extension UI
- **Editor** — type here; border color indicates thinking level
- **Footer** — working directory, session name, token/cache usage, cost, context, current model

The editor can be replaced by other UI (built-in `/settings` or custom extension UI). Extensions can also add widgets, status lines, footers, or overlays.

### Editor

| Feature | How |
|---------|-----|
| File reference | Type `@` to fuzzy-search project files |
| Path completion | Tab to complete paths |
| Multi-line | Shift+Enter (or Ctrl+Enter on Windows Terminal) |
| Images | Ctrl+V to paste (Alt+V on Windows), or drag onto terminal |
| Bash commands | `!command` runs and sends output to LLM, `!!command` runs without sending |

See [[099-packages-coding-agent-docs-keybindings|Keybindings]] for standard editing keybindings.

### Commands

Type `/` to trigger commands. Extensions register custom commands, skills are `/skill:name`, prompt templates expand via `/templatename`.

| Command | Description |
|---------|-------------|
| `/login`, `/logout` | OAuth authentication |
| `/model` | Switch models |
| `/scoped-models` | Enable/disable models for Ctrl+P cycling |
| `/settings` | Thinking level, theme, message delivery, transport |
| `/resume` | Pick from previous sessions |
| `/new` | Start a new session |
| `/name <name>` | Set session display name |
| `/session` | Show session info (file, ID, messages, tokens, cost) |
| `/tree` | Jump to any point in the session and continue from there |
| `/fork` | Create a new session from a previous user message |
| `/clone` | Duplicate the current active branch into a new session |
| `/compact [prompt]` | Manually compact context, optional custom instructions |
| `/copy` | Copy last assistant message to clipboard |
| `/export [file]` | Export session to HTML file |
| `/share` | Upload as private GitHub gist with shareable HTML link |
| `/reload` | Reload keybindings, extensions, skills, prompts, context files |
| `/hotkeys` | Show all keyboard shortcuts |
| `/changelog` | Display version history |
| `/quit` | Quit pi |

### Keyboard Shortcuts

See `/hotkeys` for the full list. Customize via `~/.pi/agent/keybindings.json`. Common shortcuts:

| Key | Action |
|-----|--------|
| Ctrl+C | Clear editor |
| Ctrl+C twice | Quit |
| Escape | Cancel/abort |
| Escape twice | Open `/tree` |
| Ctrl+L | Open model selector |
| Ctrl+P / Shift+Ctrl+P | Cycle scoped models forward/backward |
| Shift+Tab | Cycle thinking level |
| Ctrl+O | Collapse/expand tool output |
| Ctrl+T | Collapse/expand thinking blocks |

### Message Queue

Submit messages while the agent is working:

- **Enter** queues a *steering* message, delivered after current assistant turn finishes
- **Alt+Enter** queues a *follow-up* message, delivered only after agent finishes all work
- **Escape** aborts and restores queued messages to editor
- **Alt+Up** retrieves queued messages back to editor

> [!warning]
> On Windows Terminal, `Alt+Enter` is fullscreen by default. Remap it in [[049-packages-coding-agent-docs-terminal-setup|Terminal setup]].

Configure delivery in [[103-packages-coding-agent-docs-settings|Settings]]: `steeringMode` and `followUpMode` can be `"one-at-a-time"` (default) or `"all"`. `transport` selects provider transport (`"sse"`, `"websocket"`, or `"auto"`).

## Sessions

Sessions stored as JSONL files with tree structure (each entry has `id` and `parentId`). See [[102-packages-coding-agent-docs-session-format|Session File Format]].

### Management

Sessions auto-save to `~/.pi/agent/sessions/` organized by working directory.

| Command | Description |
|---------|-------------|
| `pi -c` | Continue most recent session |
| `pi -r` | Browse and select from past sessions |
| `pi --no-session` | Ephemeral mode (don't save) |
| `pi --session <path\|id>` | Use specific session file or ID |
| `pi --fork <path\|id>` | Fork specific session into a new session |

Use `/session` to see the current session ID before reusing with `--session` or `--fork`.

### Branching

**`/tree`** — Navigate the session tree in-place. Select any previous point, continue from there, switch between branches. All history preserved in a single file.

- Search by typing, fold/unfold and jump between branches with Ctrl+←/Ctrl+→ or Alt+←/Alt+→
- Filter modes (Ctrl+O): default → no-tools → user-only → labeled-only → all
- Shift+L to label entries as bookmarks, Shift+T to toggle label timestamps

**`/fork`** — Create a new session file from a previous user message. Opens a selector, copies the active path up to that point, places the selected prompt in the editor.

**`/clone`** — Duplicate the current active branch into a new session file. Keeps full active-path history, opens with empty editor.

**`--fork <path|id>`** — Fork an existing session file or partial session UUID from CLI. Copies full source session into a new session file.

### Compaction

Long sessions exhaust context windows. Compaction summarizes older messages while keeping recent ones.

- **Manual:** `/compact` or `/compact <custom instructions>`
- **Automatic:** Enabled by default. Triggers on context overflow or when approaching limit. Configure via `/settings` or `settings.json`.

Compaction is lossy. Full history remains in the JSONL file; use `/tree` to revisit. Customize via [extensions](#extensions). See [[037-packages-coding-agent-docs-compaction|Compaction]].

## Settings

Use `/settings` or edit JSON files directly:

| Location | Scope |
|----------|-------|
| `~/.pi/agent/settings.json` | Global (all projects) |
| `.pi/settings.json` | Project (overrides global) |

See [[103-packages-coding-agent-docs-settings|Settings]] for all options.

### Telemetry and Update Checks

Two separate startup features:

- **Update check:** Fetches `https://pi.dev/api/latest-version`. Disable with `PI_SKIP_VERSION_CHECK=1`.
- **Install/update telemetry:** After first install or changelog-detected update, sends anonymous version ping to `https://pi.dev/api/report-install`. Opt out with `enableInstallTelemetry: false` in `settings.json` or `PI_TELEMETRY=0`.

Use `--offline` or `PI_OFFLINE=1` to disable all startup network operations.

## Context Files

Pi loads `AGENTS.md` (or `CLAUDE.md`) at startup from `~/.pi/agent/AGENTS.md`, parent directories, and current directory. All matching files are concatenated. Disable with `--no-context-files` (`-nc`).

### System Prompt

Replace default with `.pi/SYSTEM.md` (project) or `~/.pi/agent/SYSTEM.md` (global). Append without replacing via `APPEND_SYSTEM.md`.

## Customization

### Prompt Templates

Reusable prompts as Markdown files. Type `/name` to expand.

```markdown
<!-- ~/.pi/agent/prompts/review.md -->
Review this code for bugs, security issues, and performance problems.
Focus on: {{focus}}
```

Place in `~/.pi/agent/prompts/`, `.pi/prompts/`, or a [pi package](#pi-packages). See [[028-packages-coding-agent-docs-prompt-templates|Prompt Templates]].

### Skills

On-demand capability packages following the [Agent Skills standard](https://agentskills.io). Invoke via `/skill:name` or let the agent auto-load.

```markdown
<!-- ~/.pi/agent/skills/my-skill/SKILL.md -->
# My Skill
Use this skill when the user asks about X.

## Steps
1. Do this
2. Then that
```

Place in `~/.pi/agent/skills/`, `~/.agents/skills/`, `.pi/skills/`, `.agents/skills/`, or a [pi package](#pi-packages). See [[038-packages-coding-agent-docs-skills|Skills]].

### Extensions

TypeScript modules extending pi with custom tools, commands, keyboard shortcuts, event handlers, and UI components.

```typescript
export default function (pi: ExtensionAPI) {
  pi.registerTool({ name: "deploy", ... });
  pi.registerCommand("stats", { ... });
  pi.on("tool_call", async (event, ctx) => { ... });
}
```

The default export can be `async` for one-time initialization (e.g., fetching remote model lists before `pi.registerProvider()`).

**Capabilities:**
- Custom tools (or replace built-in tools)
- Sub-agents and plan mode
- Custom compaction and summarization
- Permission gates and path protection
- Custom editors and UI components
- Status lines, headers, footers
- Git checkpointing and auto-commit
- SSH and sandbox execution
- MCP server integration
- Make pi look like Claude Code
- Games while waiting (yes, Doom runs)

Place in `~/.pi/agent/extensions/`, `.pi/extensions/`, or a [pi package](#pi-packages). See [[025-packages-coding-agent-docs-extensions|Extensions]] and [[005-packages-coding-agent-examples-extensions-readme|Extension Examples]].

### Themes

Built-in: `dark`, `light`. Themes hot-reload: modify the active theme file and pi immediately applies changes.

Place in `~/.pi/agent/themes/`, `.pi/themes/`, or a [pi package](#pi-packages). See [[031-packages-coding-agent-docs-themes|Themes]].

### Pi Packages

Bundle and share extensions, skills, prompts, and themes via npm or git. Find packages on [npmjs.com](https://www.npmjs.com/search?q=keywords%3Api-package) or [Discord](https://discord.com/channels/1456806362351669492/1457744485428629628).

> **Security:** Pi packages run with full system access. Review source code before installing third-party packages.

```bash
pi install npm:@foo/pi-tools
pi install npm:@foo/pi-tools@1.2.3      # pinned version
pi install git:github.com/user/repo
pi install git:github.com/user/repo@v1  # tag or commit
pi install git:git@github.com:user/repo
pi install https://github.com/user/repo
pi install ssh://git@github.com/user/repo
pi remove npm:@foo/pi-tools
pi uninstall npm:@foo/pi-tools          # alias for remove
pi list
pi update                               # update pi and packages
pi update --extensions                  # packages only
pi update --self                        # pi only
pi update --self --force                # reinstall even if current
pi update npm:@foo/pi-tools             # one package
pi config                               # enable/disable extensions, skills, prompts, themes
```

Packages install to `~/.pi/agent/git/` (git) or global npm. Use `-l` for project-local installs (`.pi/git/`, `.pi/npm/`). Git packages install dependencies with `npm install --omit=dev` by default. Set `npmCommand` in `settings.json` for compatibility with wrappers (e.g., `["mise", "exec", "node@20", "--", "npm"]`).

Create a package by adding a `pi` key to `package.json`:

```json
{
  "name": "my-pi-package",
  "keywords": ["pi-package"],
  "pi": {
    "extensions": ["./extensions"],
    "skills": ["./skills"],
    "prompts": ["./prompts"],
    "themes": ["./themes"]
  }
}
```

Without a `pi` manifest, pi auto-discovers from conventional directories. See [[026-packages-coding-agent-docs-packages|Pi Packages]].

## Programmatic Usage

### SDK

```typescript
import { AuthStorage, createAgentSession, ModelRegistry, SessionManager } from "@mariozechner/pi-coding-agent";

const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);
const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage,
  modelRegistry,
});

await session.prompt("What files are in the current directory?");
```

For advanced multi-session runtime replacement, use `createAgentSessionRuntime()` and `AgentSessionRuntime`. See [[101-packages-coding-agent-docs-sdk|SDK]] and [[008-packages-coding-agent-examples-sdk-readme|SDK Examples]].

### RPC Mode

For non-Node.js integrations:

```bash
pi --mode rpc
```

RPC mode uses strict LF-delimited JSONL framing. Do not use generic line readers like Node `readline`, which also splits on Unicode separators. See [[100-packages-coding-agent-docs-rpc|RPC Mode]].

## Philosophy

Pi is aggressively extensible so it doesn't dictate your workflow. Features that other tools bake in can be built with extensions, skills, or third-party pi packages.

- **No MCP.** Build CLI tools with READMEs (see [Skills](#skills)), or build an extension that adds MCP support. [Why?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/)
- **No sub-agents.** Spawn pi instances via tmux, or build your own with extensions.
- **No permission popups.** Run in a container, or build your own confirmation flow with extensions.
- **No plan mode.** Write plans to files, or build it with extensions.
- **No built-in to-dos.** Use a TODO.md file, or build your own with extensions.
- **No background bash.** Use tmux. Full observability, direct interaction.

Read the [blog post](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) for the full rationale.

## Share Your OSS Sessions

If you use pi for open source work, please share your coding agent sessions. Public data helps improve models, prompts, tools, and evaluations.

Use [`badlogic/pi-share-hf`](https://github.com/badlogic/pi-share-hf). Read its README for setup (needs Hugging Face account, CLI, and `pi-share-hf`). Also see [this video](https://x.com/badlogicgames/status/2041151967695634619).

My own `pi-mono` sessions: [badlogicgames/pi-mono on Hugging Face](https://huggingface.co/datasets/badlogicgames/pi-mono)

## CLI Reference

```bash
pi [options] [@files...] [messages...]
```

### Package Commands

```bash
pi install <source> [-l]     # Install package, -l for project-local
pi remove <source> [-l]       # Remove package
pi uninstall <source> [-l]     # Alias for remove
pi update [source|self|pi]    # Update pi and packages (skips pinned)
pi update --extensions        # packages only
pi update --self              # pi only
pi update --self --force      # reinstall even if current
pi update --extension <src>   # update one package
pi list                       # List installed packages
pi config                     # enable/disable package resources
```

### Modes

| Flag | Description |
|------|-------------|
| (default) | Interactive mode |
| `-p`, `--print` | Print response and exit |
| `--mode json` | Output all events as JSON lines (see [[098-packages-coding-agent-docs-json|JSON Mode]]) |
| `--mode rpc` | RPC mode for process integration (see [[100-packages-coding-agent-docs-rpc|RPC Mode]]) |
| `--export <in> [out]` | Export session to HTML |

In print mode, pi reads piped stdin and merges into the initial prompt:

```bash
cat README.md | pi -p "Summarize this text"
```

### Model Options

| Option | Description |
|--------|-------------|
| `--provider <name>` | Provider (anthropic, openai, google, etc.) |
| `--model <pattern>` | Model pattern or ID (supports `provider/id` and optional `:<thinking>`) |
| `--api-key <key>` | API key (overrides env vars) |
| `--thinking <level>` | `off`, `minimal`, `low`, `medium`, `high`, `xhigh` |
| `--models <patterns>` | Comma-separated patterns for Ctrl+P cycling |
| `--list-models [search]` | List available models |

### Session Options

| Option | Description |
|--------|-------------|
| `-c`, `--continue` | Continue most recent session |
| `-r`, `--resume` | Browse and select session |
| `--session <path\|id>` | Use specific session file or partial UUID |
| `--fork <path\|id>` | Fork specific session file or partial UUID into a new session |
| `--session-dir <dir>` | Custom session storage directory |
| `--no-session` | Ephemeral mode (don't save) |

### Tool Options

| Option | Description |
|--------|-------------|
| `--tools <list>`, `-t <list>` | Allowlist specific tool names |
| `--no-builtin-tools`, `-nbt` | Disable built-in tools but keep extension/custom tools |
| `--no-tools`, `-nt` | Disable all tools by default |

Available built-in tools: `read`, `bash`, `edit`, `write`, `grep`, `find`, `ls`

### Resource Options

| Option | Description |
|--------|-------------|
| `-e`, `--extension <source>` | Load extension from path, npm, or git (repeatable) |
| `--no-extensions` | Disable extension discovery |
| `--skill <path>` | Load skill (repeatable) |
| `--no-skills` | Disable skill discovery |
| `--prompt-template <path>` | Load prompt template (repeatable) |
| `--no-prompt-templates` | Disable prompt template discovery |
| `--theme <path>` | Load theme (repeatable) |
| `--no-themes` | Disable theme discovery |
| `--no-context-files`, `-nc` | Disable AGENTS.md and CLAUDE.md discovery |

Combine `--no-*` with explicit flags to load exactly what you need (e.g., `--no-extensions -e ./my-ext.ts`).

### Other Options

| Option | Description |
|--------|-------------|
| `--system-prompt <text>` | Replace default prompt (context files and skills still appended) |
| `--append-system-prompt <text>` | Append to system prompt |
| `--verbose` | Force verbose startup |
| `-h`, `--help` | Show help |
| `-v`, `--version` | Show version |

### File Arguments

Prefix files with `@` to include in the message:

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

# Different model
pi --provider openai --model gpt-4o "Help me refactor"
pi --model openai/gpt-4o "Help me refactor"
pi --model sonnet:high "Solve this complex problem"

# Limit model cycling
pi --models "claude-*,gpt-4o"

# Read-only mode
pi --tools read,grep,find,ls -p "Review the code"

# High thinking level
pi --thinking high "Solve this complex problem"
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| `PI_CODING_AGENT_DIR` | Override config directory (default: `~/.pi/agent`) |
| `PI_CODING_AGENT_SESSION_DIR` | Override session storage directory |
| `PI_PACKAGE_DIR` | Override package directory (useful for Nix/Guix) |
| `PI_OFFLINE` | Disable all startup network operations |
| `PI_SKIP_VERSION_CHECK` | Skip the Pi version update check |
| `PI_TELEMETRY` | Override install/update telemetry (`1`/`0`) |
| `PI_CACHE_RETENTION` | Set to `long` for extended prompt cache (Anthropic: 1h, OpenAI: 24h) |
| `VISUAL`, `EDITOR` | External editor for Ctrl+G |

## Contributing & Development

See [[116-contributing.md|Contributing]] and [[023-packages-coding-agent-docs-development|Development]].

## Related Packages

- [[001-packages-agent-readme|@mariozechner/pi-agent-core]] — Agent framework
- [[002-packages-ai-readme|@mariozechner/pi-ai]] — Core LLM toolkit
- [[011-packages-tui-readme|@mariozechner/pi-tui]] — Terminal UI components

#coding-agent #terminal-tool #llm-integration #developer-tools
