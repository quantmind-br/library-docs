---
title: Advanced Configuration
url: https://developers.openai.com/codex/config-advanced.md
source: llms
fetched_at: 2026-04-30T10:15:26.676846954-03:00
rendered_js: false
word_count: 1366
summary: This document outlines advanced configuration options for the Codex system, including the use of profiles, CLI overrides, project-specific settings, hooks, and custom model providers.
tags:
    - configuration
    - cli-usage
    - project-settings
    - custom-providers
    - lifecycle-hooks
    - environment-variables
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Advanced Configuration

For quick start, see [[055-config-basic|Config basics]]. For background on customization, see [[042-concepts-customization|Customization]]. For keys, see [[067-config-reference|Configuration Reference]].

## Profiles

Save named sets of configuration values and switch between them from the CLI.

> [!warning]
> Experimental; may change or be removed in future releases. Not currently supported in the Codex IDE extension.

Define under `[profiles.<name>]` in `config.toml`, then run `codex --profile <name>`:

```toml
model = "gpt-5.4"
approval_policy = "on-request"
model_catalog_json = "/Users/me/.codex/model-catalogs/default.json"

[profiles.deep-review]
model = "gpt-5-pro"
model_reasoning_effort = "high"
approval_policy = "never"
model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"

[profiles.lightweight]
model = "gpt-4.1"
approval_policy = "untrusted"
```

Make a profile default with `profile = "deep-review"` at top level. Profile `model_catalog_json` overrides top-level value.

## One-off CLI overrides

| Method | Example |
|--------|---------|
| Dedicated flag | `codex --model gpt-5.4` |
| Generic `-c` / `--config` | `codex --config model='"gpt-5.4"'` |
| Nested key | `codex --config sandbox_workspace_write.network_access=true` |
| Array value | `codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'` |

`--config` values parsed as TOML. Quote values so your shell doesn't split on spaces. If value can't be parsed as TOML, Codex treats it as a string.

## Config and state locations

`CODEX_HOME` (default `~/.codex`):
- `config.toml` — local configuration
- `auth.json` — file-based credential storage (or OS keychain/keyring)
- `history.jsonl` — session transcripts (if persistence enabled)
- logs, caches, and other per-user state

For auth details: [[012-auth|Authentication]]. For full key list: [[067-config-reference|Configuration Reference]].

For shared defaults, rules, and skills: see [[009-enterprise-admin-setup|Team Config]].

To point built-in OpenAI provider at an LLM proxy, router, or data-residency project, set `openai_base_url` instead of defining a new provider:
```toml
openai_base_url = "https://us.api.openai.com/v1"
```

## Project config files (`.codex/config.toml`)

Codex reads project-scoped overrides from `.codex/config.toml` inside your repo. Walks from project root to current working directory, loading every `.codex/config.toml` found. Closest file to working directory wins on key conflicts.

Loads only when project is **trusted**. If untrusted, Codex ignores project `.codex/` layers (config, hooks, rules). User and system layers still load.

Relative paths inside project config resolved relative to the `.codex/` folder containing `config.toml`.

## Hooks (experimental)

Lifecycle hooks from `hooks.json` files or inline `[hooks]` tables next to active config layers.

Useful locations:
- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

Project-local hooks load only when project `.codex/` layer is trusted. User-level hooks remain independent of project trust.

Enable:
```toml
[features]
codex_hooks = true
```

Inline TOML example:
```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"
```

If a single layer contains both `hooks.json` and inline `[hooks]`, Codex loads both and warns. Prefer one representation per layer.

For events, input fields, output behavior, and limitations: see [[023-hooks|Hooks]].

## Agent roles (`[agents]` in `config.toml`)

See [[049-subagents|Subagents]] for subagent role configuration.

## Project root detection

Codex discovers project configuration (`.codex/` layers, `AGENTS.md`) by walking up from working directory until reaching a project root.

Default: directory containing `.git` is project root. Customize with `project_root_markers`:
```toml
project_root_markers = [".git", ".hg", ".sl"]
```

Set `project_root_markers = []` to skip parent search and treat current working directory as project root.

## Custom model providers

Defines how Codex connects to a model: base URL, wire API, authentication, optional HTTP headers.

Reserved built-in IDs (can't override): `openai`, `ollama`, `lmstudio`.

Example:
```toml
model = "gpt-5.4"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"
```

Add headers:
```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }
```

Command-backed authentication:
```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
wire_api = "responses"

[model_providers.proxy.auth]
command = "/usr/local/bin/fetch-codex-token"
args = ["--audience", "codex"]
timeout_ms = 5000
refresh_interval_ms = 300000
```

Auth command receives no `stdin`, must print token to `stdout`. Codex trims whitespace, treats empty token as error, refreshes proactively at `refresh_interval_ms`. Set `refresh_interval_ms = 0` to refresh only after authentication retry. Don't combine `[model_providers.<id>.auth]` with `env_key`, `experimental_bearer_token`, or `requires_openai_auth`.

## OSS mode (local providers)

Run against local provider (Ollama, LM Studio) with `--oss`. Without specifying provider, uses `oss_provider` default:
```toml
oss_provider = "ollama"  # or "lmstudio"
```

## Azure provider and per-provider tuning

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000
```

To change built-in OpenAI provider base URL, use `openai_base_url`; don't create `[model_providers.openai]`.

## ChatGPT data residency

Projects with [data residency](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt) can create a provider with the [correct prefix](https://platform.openai.com/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency):
```toml
model_provider = "openaidr"

[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1"  # Replace 'us' with domain prefix
```

## Model reasoning, verbosity, and limits

```toml
model_reasoning_summary = "none"          # Disable summaries
model_verbosity = "low"                   # Shorten responses
model_supports_reasoning_summaries = true # Force reasoning
model_context_window = 128000             # Context window size
```

`model_verbosity` applies only to Responses API providers; Chat Completions providers ignore it.

## Approval policies and sandbox modes

Pick approval strictness (when Codex pauses) and sandbox level (file/network access).

Operational details: [[041-agent-approvals-security#common-sandbox-and-approval-combinations|Common sandbox and approval combinations]], [[041-agent-approvals-security#protected-paths-in-writable-roots|Protected paths in writable roots]], [[041-agent-approvals-security#network-access|Network access]].

Granular approval policy:
```toml
approval_policy = { granular = {
  sandbox_approval = true,
  rules = true,
  mcp_elicitations = true,
  request_permissions = false,
  skill_approval = false
} }
```

Set `approvals_reviewer = "auto_review"` to route eligible interactive approval requests through automatic review. Changes reviewer, not sandbox boundary.

Local reviewer policy instructions under `[auto_review].policy`. Managed `guardian_policy_config` takes precedence.

```toml
approval_policy = "untrusted"   # on-request, never, or granular
approvals_reviewer = "user"     # or "auto_review"
sandbox_mode = "workspace-write"
allow_login_shell = false

[sandbox_workspace_write]
exclude_tmpdir_env_var = false
exclude_slash_tmp = false
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false

[auto_review]
policy = """
Use your organization's automatic review policy.
"""
```

In workspace-write mode, `.git/` and `.codex/` may stay read-only even when rest of workspace is writable. Commands like `git commit` may still require approval to run outside sandbox. To skip specific commands, use [[061-rules|rules]].

Disable sandboxing entirely (only if environment already isolates processes):
```toml
sandbox_mode = "danger-full-access"
```

## Shell environment policy

Controls which environment variables Codex passes to subprocesses. Start clean (`inherit = "none"`) or trimmed (`inherit = "core"`), then layer excludes, includes, and overrides.

```toml
[shell_environment_policy]
inherit = "none"
set = { PATH = "/usr/bin", MY_FLAG = "1" }
ignore_default_excludes = false
exclude = ["AWS_*", "AZURE_*"]
include_only = ["PATH", "HOME"]
```

Patterns are case-insensitive globs (`*`, `?`, `[A-Z]`). `ignore_default_excludes = false` keeps automatic KEY/SECRET/TOKEN filter before your includes/excludes run.

## MCP servers

See [[058-mcp|MCP documentation]] for configuration details.

## Observability and telemetry

Enable OpenTelemetry (OTel) log export to track Codex runs. Disabled by default; opt in via `[otel]`:

```toml
[otel]
environment = "staging"   # defaults to "dev"
exporter = "none"         # otlp-http or otlp-grpc to send events
log_user_prompt = false   # redact user prompts unless explicitly enabled
```

Exporters:
```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}
```
```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}
```

If `exporter = "none"`, Codex records events but sends nothing. Exporters batch asynchronously and flush on shutdown.

### Events emitted

Representative event types:
- `codex.conversation_starts` (model, reasoning settings, sandbox/approval policy)
- `codex.api_request` (attempt, status/success, duration, error details)
- `codex.sse_event` (stream event kind, success/failure, duration, token counts on `response.completed`)
- `codex.websocket_request` / `codex.websocket_event` (request duration, per-message kind/success/error)
- `codex.user_prompt` (length; content redacted unless explicitly enabled)
- `codex.tool_decision` (approved/denied, config vs user decision)
- `codex.tool_result` (duration, success, output snippet)

### OTel metrics

When enabled, Codex emits counters and duration histograms for API, stream, and tool activity. Each metric includes default tags: `auth_mode`, `originator`, `session_source`, `model`, `app.version`.

| Metric | Type | Fields | Description |
|--------|------|--------|-------------|
| `codex.api_request` | counter | `status`, `success` | API request count |
| `codex.api_request.duration_ms` | histogram | `status`, `success` | API request duration |
| `codex.sse_event` | counter | `kind`, `success` | SSE event count |
| `codex.sse_event.duration_ms` | histogram | `kind`, `success` | SSE event processing duration |
| `codex.websocket.request` | counter | `success` | WebSocket request count |
| `codex.websocket.request.duration_ms` | histogram | `success` | WebSocket request duration |
| `codex.websocket.event` | counter | `kind`, `success` | WebSocket message/event count |
| `codex.websocket.event.duration_ms` | histogram | `kind`, `success` | WebSocket message processing duration |
| `codex.tool.call` | counter | `tool`, `success` | Tool invocation count |
| `codex.tool.call.duration_ms` | histogram | `tool`, `success` | Tool execution duration |

For security and privacy guidance: [[041-agent-approvals-security#monitoring-and-telemetry|Security]].

### Metrics (anonymous usage data)

By default, Codex periodically sends anonymous usage and health data to OpenAI. No PII. Independent of OTel export.

Disable:
```toml
[analytics]
enabled = false
```

Full metrics catalog omitted for brevity; see [[067-config-reference|Configuration Reference]] for complete list.

### Feedback controls

Disable feedback collection:
```toml
[feedback]
enabled = false
```

When disabled, `/feedback` shows a disabled message and Codex rejects submissions.

### Reasoning events

Reduce noisy reasoning output (e.g., in CI logs):
```toml
hide_agent_reasoning = true
```

Surface raw reasoning content when emitted:
```toml
show_raw_agent_reasoning = true
```

Some models/providers (e.g., `gpt-oss`) don't emit raw reasoning; setting has no visible effect.

## Notifications

Trigger external program on supported events (currently `agent-turn-complete`):
```toml
notify = ["python3", "/path/to/notify.py"]
```

Script receives single JSON argument with fields:
- `type` (`agent-turn-complete`)
- `thread-id`, `turn-id`
- `cwd`
- `input-messages`
- `last-assistant-message`

Example `notify.py` (truncated):
```python
#!/usr/bin/env python3
import json, subprocess, sys

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

`notify` vs `tui.notifications`:
- `notify` — external program (webhooks, desktop notifiers, CI hooks)
- `tui.notifications` — built-in TUI, filterable by event type
- `tui.notification_method` — `auto`, `osc9`, or `bel`
- `tui.notification_condition` — `unfocused` or `always`

In `auto` mode, Codex prefers OSC 9 notifications (terminal escape sequence interpreted as desktop notification by some terminals), falling back to BEL (`\x07`) otherwise.

## History persistence

Default: saves local session transcripts under `CODEX_HOME` (e.g., `~/.codex/history.jsonl`).

Disable:
```toml
[history]
persistence = "none"
```

Cap file size:
```toml
[history]
max_bytes = 104857600  # 100 MiB
```

When exceeded, Codex drops oldest entries and compacts while keeping newest records.

## Clickable citations

Configure `file_opener` for file citation URI scheme:
```toml
file_opener = "vscode"  # cursor, windsurf, vscode-insiders, none
```

Example: `/home/user/project/main.py:42` → `vscode://file/...:42`

## Project instructions discovery

Codex reads `AGENTS.md` and related files, including limited project guidance in first turn.

| Knob | Purpose |
|------|---------|
| `project_doc_max_bytes` | How much to read from each `AGENTS.md` file |
| `project_doc_fallback_filenames` | Additional filenames to try when `AGENTS.md` is missing |

See [[020-guides-agents-md|Custom instructions with AGENTS.md]] for detailed walkthrough.

## TUI options

Running `codex` with no subcommand launches the interactive TUI. TUI-specific config under `[tui]`:

| Key | Description |
|-----|-------------|
| `tui.notifications` | Enable/disable or restrict to specific event types |
| `tui.notification_method` | `auto`, `osc9`, or `bel` |
| `tui.notification_condition` | `unfocused` or `always` |
| `tui.animations` | Enable/disable ASCII animations and shimmer effects |
| `tui.alternate_screen` | Control alternate screen usage (`never` keeps terminal scrollback) |
| `tui.show_tooltips` | Show/hide onboarding tooltips on welcome screen |

See [[067-config-reference|Configuration Reference]] for full key list.

#configuration #advanced #profiles #hooks #telemetry #codex