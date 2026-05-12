---
number: 66
category: reference
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/cli/reference.md
word_count: 1620
---
# CLI Reference

> **BLUF:** Complete reference for the `codex` CLI. Commands organized by maturity (stable vs experimental). Global flags apply to most subcommands. Configuration precedence: CLI flags > env vars > `~/.codex/config.toml`.

## Global Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `PROMPT` | string | — | Optional initial instruction |
| `--image, -i` | path(s) | — | Attach image(s) to initial prompt |
| `--model, -m` | string | — | Override configured model |
| `--oss` | boolean | false | Use local OSS provider (requires Ollama) |
| `--profile, -p` | string | — | Load profile from `~/.codex/config.toml` |
| `--sandbox, -s` | enum | — | Sandbox policy: `read-only`, `workspace-write`, `danger-full-access` |
| `--ask-for-approval, -a` | enum | — | Approval mode: `untrusted`, `on-request`, `never` |
| `--full-auto` | boolean | false | Shortcut: `--ask-for-approval on-request --sandbox workspace-write` |
| `--dangerously-bypass-approvals-and-sandbox, --yolo` | boolean | false | No approvals or sandbox (isolated environments only) |
| `--cd, -C` | path | — | Set working directory |
| `--search` | boolean | false | Enable live web search (default: cached) |
| `--add-dir` | path | — | Grant additional write directories |
| `--no-alt-screen` | boolean | false | Disable TUI alternate screen |
| `--remote` | ws://… | — | Connect TUI to remote app-server |
| `--remote-auth-token-env` | ENV_VAR | — | Bearer token env var for `--remote` |
| `--enable` | feature | — | Force-enable feature flag |
| `--disable` | feature | — | Force-disable feature flag |
| `--config, -c` | key=value | — | Override config values |

## Command Overview

| Command | Maturity | Description |
|---------|----------|-------------|
| `codex` | stable | Launch interactive TUI |
| `codex app-server` | experimental | Launch local app server |
| `codex app` | stable | Launch Codex Desktop (macOS/Windows) |
| `codex apply` | stable | Apply latest Codex Cloud diff locally |
| `codex cloud` | experimental | Browse/execute cloud tasks |
| `codex completion` | stable | Generate shell completions |
| `codex exec` | stable | Non-interactive execution |
| `codex execpolicy` | experimental | Evaluate execpolicy rules |
| `codex features` | stable | Manage feature flags |
| `codex fork` | stable | Fork session to new thread |
| `codex login` | stable | Authenticate |
| `codex logout` | stable | Remove credentials |
| `codex mcp` | experimental | Manage MCP servers |
| `codex mcp-server` | experimental | Run Codex as MCP server |
| `codex plugin marketplace` | experimental | Manage plugin marketplaces |
| `codex resume` | stable | Continue previous session |
| `codex sandbox` | experimental | Run commands in sandbox |

## `codex` (Interactive)

Launch TUI. Supports all global flags. Web search defaults to cached; use `--search` for live. `--full-auto` reduces approval friction. `--remote` connects to app-server WebSocket.

## `codex app-server`

Launch local app server for development/debugging.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--listen` | URL | `stdio://` | Transport: `stdio://` or `ws://IP:PORT` |
| `--ws-auth` | enum | — | Auth mode: `capability-token` or `signed-bearer-token` |
| `--ws-token-file` | path | — | Capability token file |
| `--ws-shared-secret-file` | path | — | HMAC secret for JWT validation |
| `--ws-issuer` | string | — | Expected JWT `iss` claim |
| `--ws-audience` | string | — | Expected JWT `aud` claim |
| `--ws-max-clock-skew-seconds` | number | 30 | Clock skew allowance |

## `codex app`

Launch Codex Desktop. Opens workspace path on macOS; prints path on Windows.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `PATH` | path | `.` | Workspace path |
| `--download-url` | URL | — | Override installer URL |

## `codex apply`

Apply most recent Codex Cloud task diff to local working tree.

| Flag | Type | Description |
|------|------|-------------|
| `TASK_ID` | string | Cloud task identifier |

## `codex cloud`

Interact with cloud tasks. Default: interactive picker.

**`codex cloud exec`:**

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `QUERY` | string | — | Task prompt |
| `--env` | ENV_ID | — | Target environment (required) |
| `--attempts` | 1-4 | 1 | Best-of-N attempts |

**`codex cloud list`:**

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--env` | ENV_ID | — | Filter by environment |
| `--limit` | 1-20 | 20 | Max tasks returned |
| `--cursor` | string | — | Pagination cursor |
| `--json` | boolean | false | JSON output |

## `codex completion`

Generate shell completion scripts.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `SHELL` | enum | `bash` | `bash`, `zsh`, `fish`, `power-shell`, `elvish` |

## `codex exec`

Non-interactive execution. Alias: `codex e`.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `PROMPT` | string/`-` | — | Initial instruction; `-` reads stdin |
| `--image, -i` | path(s) | — | Attach images |
| `--model, -m` | string | — | Override model |
| `--oss` | boolean | false | Use OSS provider |
| `--sandbox, -s` | enum | — | Sandbox policy |
| `--profile, -p` | string | — | Config profile |
| `--full-auto` | boolean | false | Low-friction preset |
| `--yolo` | boolean | false | Bypass approvals/sandbox |
| `--cd, -C` | path | — | Workspace root |
| `--skip-git-repo-check` | boolean | false | Allow running outside Git repo |
| `--ephemeral` | boolean | false | Don't persist session files |
| `--output-schema` | path | — | JSON Schema for final response |
| `--color` | enum | `auto` | `always`, `never`, `auto` |
| `--json` | boolean | false | JSONL events output |
| `--output-last-message, -o` | path | — | Write final message to file |
| `-c, --config` | key=value | — | Inline config overrides |

**`codex exec resume`:**

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `SESSION_ID` | uuid | — | Session to resume |
| `--last` | boolean | false | Most recent session (cwd-scoped) |
| `--all` | boolean | false | Include sessions outside cwd |
| `--image, -i` | path(s) | — | Images for follow-up |
| `PROMPT` | string/`-` | — | Follow-up instruction |

## `codex execpolicy`

Evaluate execpolicy rule files. Preview status.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--rules, -r` | path(s) | — | Rule file(s) to evaluate |
| `--pretty` | boolean | false | Pretty-print JSON |
| `COMMAND...` | var-args | — | Command to check |

## `codex features`

Manage feature flags in `config.toml`.

| Subcommand | Description |
|------------|-------------|
| `list` | Show known flags, maturity, effective state |
| `enable <feature>` | Persistently enable flag |
| `disable <feature>` | Persistently disable flag |

## `codex fork`

Fork session into new thread.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `SESSION_ID` | uuid | — | Session to fork |
| `--last` | boolean | false | Fork most recent session |
| `--all` | boolean | false | Include sessions outside cwd |

## `codex login`

Authenticate.

| Flag | Type | Description |
|------|------|-------------|
| `--with-api-key` | boolean | Read API key from stdin |
| `--device-auth` | boolean | Use OAuth device code flow |
| `status` | subcommand | Print auth mode; exits 0 if logged in |

## `codex logout`

Remove all stored credentials. No flags.

## `codex mcp`

Manage MCP servers.

| Subcommand | Description |
|------------|-------------|
| `list [--json]` | List configured servers |
| `get <name> [--json]` | Show server config |
| `add <name> -- <cmd...>` or `--url <url>` | Register server |
| `remove <name>` | Delete server config |
| `login <name> --scopes ...` | OAuth login for HTTP server |
| `logout <name>` | Remove OAuth credentials |

**`mcp add` flags:**

| Flag | Type | Description |
|------|------|-------------|
| `COMMAND...` | stdio | Executable + args (after `--`) |
| `--env KEY=VALUE` | repeatable | Env vars for stdio server |
| `--url` | URL | Streamable HTTP server |
| `--bearer-token-env-var` | ENV_VAR | Bearer token env var |

## `codex plugin marketplace`

Manage plugin marketplaces.

| Subcommand | Description |
|------------|-------------|
| `add <source> [--ref REF] [--sparse PATH]` | Install from GitHub/Git/local |
| `upgrade [name]` | Refresh Git marketplace(s) |
| `remove <name>` | Remove marketplace |

## `codex resume`

Continue interactive session.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `SESSION_ID` | uuid | — | Session to resume |
| `--last` | boolean | false | Most recent session (cwd-scoped) |
| `--all` | boolean | false | Include sessions outside cwd |

## `codex sandbox`

Run commands in Codex's sandbox.

**macOS seatbelt:**

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--full-auto` | boolean | false | Grant workspace + `/tmp` write |
| `--config, -c` | key=value | — | Config overrides |
| `COMMAND...` | var-args | — | Command after `--` |

**Linux Landlock:**

Same flags as macOS. Uses Landlock + seccomp.

## Safety Tips

| Combination | Risk |
|-------------|------|
| `--full-auto` + `--yolo` | **Dangerous** — only in isolated VMs |
| `--add-dir` | Prefer over `--sandbox danger-full-access` |
| `--json` + `--output-last-message` | Ideal for CI pipelines |

## Related

- [[015-cli|Codex CLI Overview]]
- [[067-config-reference|Configuration Reference]]
- [[016-cloud|Codex Cloud]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/cli/reference.md)*
