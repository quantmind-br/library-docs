---
title: Config basics
url: https://developers.openai.com/codex/config-basic.md
source: llms
fetched_at: 2026-04-30T10:15:27.636440122-03:00
rendered_js: false
word_count: 535
summary: This document explains how to configure Codex using TOML files, detailing the file locations, configuration precedence hierarchy, and common settings available for customization.
tags:
    - codex
    - configuration
    - toml
    - setup
    - settings
    - project-config
    - cli-tools
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Config basics

Codex reads configuration from multiple locations. Personal defaults live in `~/.codex/config.toml`; project overrides use `.codex/config.toml` files. Project `.codex/` layers load only when you trust the project.

## Configuration file

User-level: `~/.codex/config.toml`. Project-scoped: `.codex/config.toml` in your repo.

To open from IDE extension: gear icon > **Codex Settings > Open config.toml**.

CLI and IDE extension share the same configuration layers. Use them to:
- Set default model and provider
- Configure [[041-agent-approvals-security#sandbox-and-approvals|approval policies and sandbox settings]]
- Configure [[058-mcp|MCP servers]]

## Configuration precedence

Highest precedence first:

1. CLI flags and `--config` overrides
2. [[054-config-advanced#profiles|Profile]] values (`--profile <name>`)
3. Project config files: `.codex/config.toml`, ordered from project root down to current working directory (closest wins; trusted projects only)
4. User config: `~/.codex/config.toml`
5. System config (if present): `/etc/codex/config.toml` on Unix
6. Built-in defaults

Set shared defaults at the top level; keep profiles focused on differing values.

If project is untrusted, Codex skips project-scoped `.codex/` layers (config, hooks, rules). User and system config still load.

For one-off `-c`/`--config` overrides (including TOML quoting rules), see [[054-config-advanced#one-off-overrides-from-the-cli|Advanced Config]].

On managed machines, organization may enforce constraints via `requirements.toml` (e.g., disallowing `approval_policy = "never"` or `sandbox_mode = "danger-full-access"`). See [[018-enterprise-managed-configuration|Managed configuration]] and [[018-enterprise-managed-configuration#admin-enforced-requirements-requirementstoml|Admin-enforced requirements]].

## Common options

### Default model

```toml
model = "gpt-5.5"
```

### Approval prompts

```toml
approval_policy = "on-request"
```

Options: `untrusted`, `on-request`, `never`. See [[041-agent-approvals-security#run-without-approval-prompts|Run without approval prompts]] and [[041-agent-approvals-security#common-sandbox-and-approval-combinations|Common sandbox and approval combinations]].

### Sandbox level

```toml
sandbox_mode = "workspace-write"
```

See [[041-agent-approvals-security#sandbox-and-approvals|Sandbox and approvals]], [[041-agent-approvals-security#protected-paths-in-writable-roots|Protected paths in writable roots]], and [[041-agent-approvals-security#network-access|Network access]].

### Windows sandbox mode

```toml
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup unavailable
```

### Web search mode

```toml
web_search = "cached"  # default; pre-indexed results
# web_search = "live"  # fetch most recent data (same as --search)
# web_search = "disabled"
```

Cached mode serves results from OpenAI-maintained index, reducing prompt injection exposure. Still treat results as untrusted. Defaults to `live` when using full access sandbox settings.

### Reasoning effort

```toml
model_reasoning_effort = "high"
```

### Communication style

```toml
personality = "friendly"  # or "pragmatic" or "none"
```

Override per session with `/personality` or app-server APIs.

### Command environment

```toml
[shell_environment_policy]
include_only = ["PATH", "HOME"]
```

### Log directory

```toml
log_dir = "/absolute/path/to/codex-logs"
```

Or CLI one-off: `codex -c log_dir=./.codex-log`

## Feature flags

Toggle optional/experimental capabilities under `[features]` in `config.toml`:

```toml
[features]
shell_snapshot = true
```

| Key | Default | Maturity | Description |
|-----|---------|----------|-------------|
| `apps` | false | Experimental | ChatGPT Apps/connectors support |
| `codex_hooks` | true | Stable | Lifecycle hooks from `hooks.json` or inline `[hooks]`. See [[023-hooks|Hooks]] |
| `fast_mode` | true | Stable | Fast mode selection and `service_tier = "fast"` |
| `memories` | false | Stable | [[059-memories|Memories]] |
| `multi_agent` | true | Stable | Subagent collaboration tools |
| `personality` | true | Stable | Personality selection controls |
| `shell_snapshot` | true | Stable | Snapshot shell environment to speed up repeated commands |
| `shell_tool` | true | Stable | Default `shell` tool |
| `unified_exec` | true (except Windows) | Stable | Unified PTY-backed exec tool |
| `undo` | false | Stable | Undo via per-turn git ghost snapshots |
| `web_search` | true | Deprecated | Legacy toggle; prefer top-level `web_search` |
| `web_search_cached` | false | Deprecated | Maps to `web_search = "cached"` when unset |
| `web_search_request` | false | Deprecated | Maps to `web_search = "live"` when unset |

See [[063-feature-maturity|Feature Maturity]] for label meanings.

Omit feature keys to keep defaults.

### Enabling features

- In `config.toml`: `feature_name = true` under `[features]`
- CLI: `codex --enable feature_name`
- Multiple: `codex --enable feature_a --enable feature_b`
- Disable: set key to `false` in `config.toml`

#configuration #codex #toml #settings