---
number: 13
category: guide
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/cli/features.md
word_count: 786
---
# Codex CLI Features

> **BLUF:** Full CLI reference covering interactive TUI, session management, remote connectivity, model selection, feature flags, subagents, image I/O, web search, `/review`, `codex cloud`, slash commands, and scripting.

## Interactive TUI

Launch with `codex` or `codex "initial prompt"`. In-session:

| Action | Key/Command |
|--------|-------------|
| Paste images/screenshot | Paste into composer |
| Image files via CLI | `codex -i screenshot.png "prompt"` |
| Multiple images | `codex --image img1.png,img2.jpg "prompt"` |
| Copy latest output | `/copy` or `Ctrl+O` |
| Clear screen | `Ctrl+L` (keeps conversation) |
| Clear + new chat | `/clear` |
| Queue follow-up | `Tab` while running (prompt, slash command, or `!` shell command) |
| Draft history | `Up`/`Down` arrows |
| Search history | `Ctrl+R` → Enter to accept, Esc to cancel |
| Exit | `Ctrl+C` or `/exit` |

### Syntax Highlighting & Themes

Use `/theme` to preview and save `.tmTheme` files from `$CODEX_HOME/themes`.

## Resuming Conversations

```bash
codex resume                    # Interactive picker
codex resume --all              # All sessions (not just cwd)
codex resume --last            # Most recent in cwd
codex resume <SESSION_ID>      # Specific session

# Non-interactive
codex exec resume --last "Fix the race conditions you found"
codex exec resume <ID> "Implement the plan"
```

Sessions preserve transcript, plan history, and approvals. Override cwd with `--cd` or add extra roots with `--add-dir`.

## Remote TUI

Run Codex app server on remote host, connect TUI from local machine.

**App server (remote host):**
```bash
# Basic
codex app-server --listen ws://127.0.0.1:4500

# Expose externally (with auth)
codex app-server \
  --listen ws://0.0.0.0:4500 \
  --ws-auth capability-token \
  --ws-token-file /path/to/token
```

**TUI client (local):**
```bash
codex --remote ws://127.0.0.1:4500
# or with auth
export CODEX_REMOTE_AUTH_TOKEN="<token>"
codex --remote wss://codex-devbox.example.com:4500 \
  --remote-auth-token-env CODEX_REMOTE_AUTH_TOKEN
```

### WebSocket Auth Modes

| Mode | Setup | When to Use |
|------|-------|-------------|
| **No auth** | None | `localhost`, SSH port-forwarded |
| **Capability token** | Shared file + env var | TLS behind proxy |
| **Signed bearer (JWT)** | HMAC secret, HS256, `exp` required | Production remote |

Token file creation:
```bash
TOKEN_FILE="$HOME/.codex/codex-app-server-token"
openssl rand -base64 32 > "$TOKEN_FILE"
chmod 600 "$TOKEN_FILE"
```

> ⚠️ Codex only sends auth tokens over `wss://` or `ws://` to `localhost`/`127.0.0.1`/`::1`. Put non-local listeners behind TLS.

## Models

```bash
codex -m gpt-5.5          # Specify model
/model gpt-5.4           # Switch mid-session
```

See [[070-models|Codex Models]] for recommendations.

## Feature Flags

```bash
codex features list
codex features enable unified_exec
codex features disable shell_snapshot
```

Changes persist to `~/.codex/config.toml` (or `--profile` if specified).

## Subagents

Codex spawns subagents only when explicitly requested. See [[043-concepts-subagents|Subagents]] for setup and [[042-concepts-customization|Customization]] for role configuration.

## Image Generation

- Trigger: natural language or `$imagegen` in prompt
- Built-in: `gpt-image-2` (counts toward Codex limits; ~3–5x faster than non-image turns)
- Larger batches: set `OPENAI_API_KEY` in env → use API (API pricing applies)

## Local Code Review

Type `/review` in CLI for review presets. Uses session model by default; override with `review_model` in `config.toml`.

| Mode | What It Reviews |
|------|-----------------|
| **Base branch** | Diff against merge base |
| **Uncommitted changes** | Staged + unstaged + untracked |
| **Commit** | Specific SHA |
| **Custom instructions** | Your own focus areas |

## Web Search

| Sandbox | Default | Flag |
|---------|---------|------|
| Standard | Cached (OpenAI index) | — |
| Full access (`--yolo`) | Live results | — |
| Any | Force live | `--search` or `web_search = "live"` |

Cached mode reduces prompt injection exposure from live content.

## Non-Interactive Exec

```bash
codex exec "fix the CI failure"
codex exec --full-auto --sandbox workspace-write "deploy to staging"
codex exec -c model=gpt-5.4 -c sandbox_mode=read-only "review PR"
```

Options: `--ephemeral`, `--json`, `--output-last-message`, `--output-schema`, `--skip-git-repo-check`.

## Cloud Tasks

```bash
codex cloud                      # Interactive picker
codex cloud exec --env ENV_ID "Summarize open bugs"
codex cloud exec --env ENV_ID --attempts 3 "Summarize open bugs"
```

See [[016-cloud|Codex Cloud]] for details.

## Slash Commands

`/` in composer → open slash popup. Queue commands while running: type + `Tab`.

| Command | Purpose |
|---------|---------|
| `/permissions` | Approval mode |
| `/agent` | Switch agent thread |
| `/apps` | Browse apps/connectors |
| `/plugins` | Browse plugins |
| `/clear` | New chat |
| `/compact` | Summarize conversation |
| `/copy` | Copy latest output |
| `/diff` | Git diff |
| `/experimental` | Toggle experimental features |
| `/feedback` | Send logs to maintainers |
| `/init` | Generate `AGENTS.md` |
| `/logout` | Sign out |
| `/mcp` | List MCP tools |
| `/mention` | Attach file |
| `/model` | Set model |
| `/fast` | Toggle Fast mode |
| `/plan` | Plan mode |
| `/personality` | Communication style |
| `/ps` | Background terminals |
| `/stop` | Stop background terminals |
| `/fork` | Fork conversation |
| `/resume` | Resume saved session |
| `/new` | New conversation |
| `/review` | Working tree review |
| `/status` | Session info |
| `/debug-config` | Config diagnostics |
| `/statusline` | Configure footer |
| `/title` | Configure window title |

See [[014-cli-slash-commands|Slash Commands]] for full reference.

## Prompt Editor

`Ctrl+G` → opens `$VISUAL`/`$EDITOR` for longer prompts.

## MCP

```bash
codex mcp list                  # List servers
codex mcp add <name> -- <cmd>   # Add stdio server
codex mcp add <name> --url <url> # Add HTTP server
codex mcp-server                # Run Codex as MCP server
```

See [[052-mcp|Model Context Protocol]] for details.

## Tips

- `@` in composer → fuzzy file search
- `!` prefix → run local shell command (output fed to Codex as user input)
- `Esc` twice while composer empty → edit previous user message (continue to walk back)
- `codex --cd <path>` → set working root without `cd`
- `--add-dir` → expose additional writable roots
- Source environment before launching (venv, daemons, env vars)

## Related

- [[015-cli|Codex CLI]]
- [[066-cli-reference|CLI Reference]]
- [[070-models|Models]]
- [[016-cloud|Codex Cloud]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/cli/features.md)*