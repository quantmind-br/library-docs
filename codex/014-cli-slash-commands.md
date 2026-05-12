---
number: 14
category: reference
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/cli/slash-commands.md
word_count: 1000
---
# Slash Commands Reference

> **BLUF:** Complete reference for Codex CLI slash commands. Use `/` in composer to open the popup and filter commands. Queue commands while running by typing + `Tab`.

## All Built-in Commands

| Command | Purpose | Use Case |
|---------|---------|----------|
| `/permissions` | Set approval policy | Switch between Auto, Read Only, Full Access mid-session |
| `/sandbox-add-read-dir` | Grant sandbox read access (Windows only) | Unblock absolute directory paths outside readable roots |
| `/agent` | Switch active agent thread | Inspect or continue spawned subagent work |
| `/apps` | Browse apps/connectors | Insert `$app-slug` in prompt |
| `/plugins` | Browse installed/discoverable plugins | Install or manage plugin availability |
| `/clear` | Clear terminal + start fresh chat | Reset visible UI and conversation |
| `/compact` | Summarize conversation | Free tokens after long runs (confirm to apply) |
| `/copy` | Copy latest completed output | Grab response without manual selection (`Ctrl+O`) |
| `/diff` | Show Git diff | Review unstaged + untracked files before commit |
| `/exit` | Exit CLI | Same as `/quit` |
| `/experimental` | Toggle experimental features | Enable Apps, Smart Approvals, etc. (restart may be needed) |
| `/feedback` | Send logs to maintainers | Report issues with diagnostics |
| `/init` | Generate `AGENTS.md` scaffold | Capture persistent instructions for repo/directory |
| `/logout` | Sign out | Clear local credentials (shared machine) |
| `/mcp` | List configured MCP tools | Check which external tools are available |
| `/mention` | Attach file to conversation | Point Codex at specific files/folders |
| `/model` | Choose active model | Switch between models mid-session |
| `/fast` | Toggle Fast mode | On/off/status (confirm to persist) |
| `/plan` | Switch to plan mode | Ask Codex to propose plan before implementation |
| `/personality` | Communication style | `friendly`, `pragmatic`, `none` |
| `/ps` | Show background terminals | Check long-running commands without leaving transcript |
| `/stop` | Stop all background terminals | Cancel background work (`/clean` alias) |
| `/fork` | Fork conversation into new thread | Explore approach without losing transcript |
| `/resume` | Resume saved conversation | Pick from session list |
| `/new` | Start new conversation | Reset chat context without leaving CLI |
| `/quit` | Exit CLI | — |
| `/review` | Working tree review | Summarize issues + follow up with `/diff` |
| `/status` | Session configuration + token usage | Confirm model, policy, writable roots, context |
| `/debug-config` | Config layer + requirements diagnostics | Debug precedence, policy sources |
| `/statusline` | Configure footer items | Pick/reorder model/context/limits/git/tokens/session |
| `/title` | Configure window/tab title | Pick/reorder project/status/thread/branch/model/progress |

> `/approvals` works as alias but no longer appears in popup.

## Session Control Commands

### `/model` — Switch Model

1. Start Codex → open composer
2. Type `/model` → Enter
3. Choose model (e.g., `gpt-5.4-mini`)

**Result:** Model confirmed in transcript. Run `/status` to verify.

### `/fast` — Toggle Fast Mode

```bash
/fast on     # Enable
/fast off    # Disable
/fast status # Check current state
```

**Result:** Reports current state. Footer can show Fast mode status via `/statusline`.

### `/personality` — Communication Style

Options: `friendly`, `pragmatic`, `none` (disables personality instructions).

**Result:** Confirmed in transcript; applies to future responses in thread.

### `/plan` — Plan Mode

```bash
/plan                              # Switch to plan mode
/plan Propose a migration plan      # With inline prompt
```

**Result:** Codex enters plan mode. Available while no task is running.

### `/permissions` — Approval Mode

Select preset: `Auto` (default), `Read Only`, `Full Access`.

**Result:** Policy updated. Future actions respect new mode.

### `/status` — Session Info

Shows: active model, approval policy, writable roots, token usage.

### `/debug-config` — Config Diagnostics

Shows: layer order (lowest precedence first), on/off state, policy sources (`allowed_approval_policies`, `allowed_sandbox_modes`, `mcp_servers`, `rules`, `enforce_residency`, `experimental_network`).

### `/statusline` — Footer Items

Pick and reorder: model, model+reasoning, context stats, rate limits, git branch, token counters, session id, current directory/project root, Codex version.

**Result:** Footer updates immediately; persists to `tui.status_line` in `config.toml`.

### `/title` — Window Title

Pick and reorder: app name, project, spinner, status, thread, git branch, model, task progress.

**Result:** Title updates immediately; persists to `tui.terminal_title` in `config.toml`.

## Conversation Management

### `/copy` — Copy Latest Output

If turn is running, copies latest completed output (not in-progress).

### `/clear` — Reset Chat

Unlike `Ctrl+L` (clears view, keeps chat), `/clear` starts a new conversation.

### `/new` — New Conversation

Starts fresh conversation in same CLI session. Doesn't clear current terminal view first.

### `/resume` — Resume Saved Session

Opens saved-session picker. Reloads transcript; original history intact.

### `/fork` — Fork Conversation

Clones current conversation into new thread with fresh ID. Original transcript untouched.

### `/compact` — Summarize

After long exchange, summarize to free tokens. Confirm when offered.

### `/mention` — Attach File

```bash
/mention src/lib/api.ts  # Fuzzy match from popup
```

**Result:** File added to conversation.

### `/diff` — Git Diff

Shows: staged changes, unstaged changes, untracked files.

### `/ps` — Background Terminals

Shows each background terminal's command + up to 3 recent non-empty output lines.

> Only when `unified_exec` is in use.

### `/stop` — Stop Background Terminals

Confirm if prompted. `/clean` alias.

## Tools & Plugins

### `/mcp` — List MCP Tools

Shows: configured servers and their available tools.

### `/apps` — Browse Apps

Pick app → inserted as `$app-slug` in composer.

### `/plugins` — Browse Plugins

Marketplace tabs → inspect capabilities. `Space` to toggle enabled state.

### `/review` — Working Tree Review

Runs with current session model (override with `review_model` in `config.toml`).

## Setup & Utility

### `/experimental` — Feature Toggles

Enable features → restart if prompted.

### `/init` — Generate AGENTS.md

Creates scaffold in current directory. Edit to match repo conventions.

### `/feedback` — Send Feedback

Collects diagnostics; submits to maintainers.

### `/logout` — Sign Out

Clears local credentials.

### `/sandbox-add-read-dir` — Windows Sandbox Read Access

```bash
/sandbox-add-read-dir C:\absolute\directory\path
```

Confirms path exists and is absolute.

### `/agent` — Switch Agent Thread

Picker shows spawned subagent threads.

## Exit

### `/quit` or `/exit`

Exits immediately. Save/commit work first.

## Related

- [[013-cli-features|Codex CLI Features]]
- [[015-cli|Codex CLI Overview]]
- [[070-models|Models]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/cli/slash-commands.md)*