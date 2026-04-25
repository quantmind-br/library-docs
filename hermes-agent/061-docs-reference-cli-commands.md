---
title: CLI Commands Reference | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
source: crawler
fetched_at: 2026-04-24T17:00:01.552910193-03:00
rendered_js: false
word_count: 2998
summary: This document serves as a comprehensive reference guide detailing the terminal commands and available options for the Hermes agent CLI. It explains how various commands like 'chat' and 'setup' function, along with specific flags that control session behavior, providers, and configurations.
tags:
    - hermes-commands
    - cli-reference
    - agent-interface
    - terminal-options
    - provider-setup
    - command-guide
category: reference
---

This page covers the **terminal commands** you run from your shell.

For in-chat slash commands, see [Slash Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/slash-commands).

## Global entrypoint[​](#global-entrypoint "Direct link to Global entrypoint")

```bash
hermes [global-options]<command>[subcommand/options]
```

### Global options[​](#global-options "Direct link to Global options")

OptionDescription`--version`, `-V`Show version and exit.`--profile <name>`, `-p <name>`Select which Hermes profile to use for this invocation. Overrides the sticky default set by `hermes profile use`.`--resume <session>`, `-r <session>`Resume a previous session by ID or title.`--continue [name]`, `-c [name]`Resume the most recent session, or the most recent session matching a title.`--worktree`, `-w`Start in an isolated git worktree for parallel-agent workflows.`--yolo`Bypass dangerous-command approval prompts.`--pass-session-id`Include the session ID in the agent's system prompt.`--ignore-user-config`Ignore `~/.hermes/config.yaml` and fall back to built-in defaults. Credentials in `.env` are still loaded.`--ignore-rules`Skip auto-injection of `AGENTS.md`, `SOUL.md`, `.cursorrules`, memory, and preloaded skills.`--tui`Launch the [TUI](https://hermes-agent.nousresearch.com/docs/user-guide/tui) instead of the classic CLI. Equivalent to `HERMES_TUI=1`.`--dev`With `--tui`: run the TypeScript sources directly via `tsx` instead of the prebuilt bundle (for TUI contributors).

## Top-level commands[​](#top-level-commands "Direct link to Top-level commands")

CommandPurpose`hermes chat`Interactive or one-shot chat with the agent.`hermes model`Interactively choose the default provider and model.`hermes gateway`Run or manage the messaging gateway service.`hermes setup`Interactive setup wizard for all or part of the configuration.`hermes whatsapp`Configure and pair the WhatsApp bridge.`hermes auth`Manage credentials — add, list, remove, reset, set strategy. Handles OAuth flows for Codex/Nous/Anthropic.`hermes login` / `logout`**Deprecated** — use `hermes auth` instead.`hermes status`Show agent, auth, and platform status.`hermes cron`Inspect and tick the cron scheduler.`hermes webhook`Manage dynamic webhook subscriptions for event-driven activation.`hermes doctor`Diagnose config and dependency issues.`hermes dump`Copy-pasteable setup summary for support/debugging.`hermes debug`Debug tools — upload logs and system info for support.`hermes backup`Back up Hermes home directory to a zip file.`hermes import`Restore a Hermes backup from a zip file.`hermes logs`View, tail, and filter agent/gateway/error log files.`hermes config`Show, edit, migrate, and query configuration files.`hermes pairing`Approve or revoke messaging pairing codes.`hermes skills`Browse, install, publish, audit, and configure skills.`hermes honcho`Manage Honcho cross-session memory integration.`hermes memory`Configure external memory provider.`hermes acp`Run Hermes as an ACP server for editor integration.`hermes mcp`Manage MCP server configurations and run Hermes as an MCP server.`hermes plugins`Manage Hermes Agent plugins (install, enable, disable, remove).`hermes tools`Configure enabled tools per platform.`hermes sessions`Browse, export, prune, rename, and delete sessions.`hermes insights`Show token/cost/activity analytics.`hermes claw`OpenClaw migration helpers.`hermes dashboard`Launch the web dashboard for managing config, API keys, and sessions.`hermes profile`Manage profiles — multiple isolated Hermes instances.`hermes completion`Print shell completion scripts (bash/zsh).`hermes version`Show version information.`hermes update`Pull latest code and reinstall dependencies.`hermes uninstall`Remove Hermes from the system.

## `hermes chat`[​](#hermes-chat "Direct link to hermes-chat")

Common options:

OptionDescription`-q`, `--query "..."`One-shot, non-interactive prompt.`-m`, `--model <model>`Override the model for this run.`-t`, `--toolsets <csv>`Enable a comma-separated set of toolsets.`--provider <provider>`Force a provider: `auto`, `openrouter`, `nous`, `openai-codex`, `copilot-acp`, `copilot`, `anthropic`, `gemini`, `google-gemini-cli`, `huggingface`, `zai`, `kimi-coding`, `kimi-coding-cn`, `minimax`, `minimax-cn`, `kilocode`, `xiaomi`, `arcee`, `alibaba`, `deepseek`, `nvidia`, `ollama-cloud`, `xai` (alias `grok`), `qwen-oauth`, `bedrock`, `opencode-zen`, `opencode-go`, `ai-gateway`.`-s`, `--skills <name>`Preload one or more skills for the session (can be repeated or comma-separated).`-v`, `--verbose`Verbose output.`-Q`, `--quiet`Programmatic mode: suppress banner/spinner/tool previews.`--image <path>`Attach a local image to a single query.`--resume <session>` / `--continue [name]`Resume a session directly from `chat`.`--worktree`Create an isolated git worktree for this run.`--checkpoints`Enable filesystem checkpoints before destructive file changes.`--yolo`Skip approval prompts.`--pass-session-id`Pass the session ID into the system prompt.`--ignore-user-config`Ignore `~/.hermes/config.yaml` and use built-in defaults. Credentials in `.env` are still loaded. Useful for isolated CI runs, reproducible bug reports, and third-party integrations.`--ignore-rules`Skip auto-injection of `AGENTS.md`, `SOUL.md`, `.cursorrules`, persistent memory, and preloaded skills. Combine with `--ignore-user-config` for a fully isolated run.`--source <tag>`Session source tag for filtering (default: `cli`). Use `tool` for third-party integrations that should not appear in user session lists.`--max-turns <N>`Maximum tool-calling iterations per conversation turn (default: 90, or `agent.max_turns` in config).

Examples:

```bash
hermes
hermes chat -q"Summarize the latest PRs"
hermes chat --provider openrouter --model anthropic/claude-sonnet-4.6
hermes chat --toolsets web,terminal,skills
hermes chat --quiet-q"Return only JSON"
hermes chat --worktree-q"Review this repo and open a PR"
hermes chat --ignore-user-config --ignore-rules -q"Repro without my personal setup"
```

## `hermes model`[​](#hermes-model "Direct link to hermes-model")

Interactive provider + model selector. **This is the command for adding new providers, setting up API keys, and running OAuth flows.** Run it from your terminal — not from inside an active Hermes chat session.

Use this when you want to:

- **add a new provider** (OpenRouter, Anthropic, Copilot, DeepSeek, custom, etc.)
- log into OAuth-backed providers (Anthropic, Copilot, Codex, Nous Portal)
- enter or update API keys
- pick from provider-specific model lists
- configure a custom/self-hosted endpoint
- save the new default into config

hermes model vs /model — know the difference

**`hermes model`** (run from your terminal, outside any Hermes session) is the **full provider setup wizard**. It can add new providers, run OAuth flows, prompt for API keys, and configure endpoints.

**`/model`** (typed inside an active Hermes chat session) can only **switch between providers and models you've already set up**. It cannot add new providers, run OAuth, or prompt for API keys.

**If you need to add a new provider:** Exit your Hermes session first (`Ctrl+C` or `/quit`), then run `hermes model` from your terminal prompt.

### `/model` slash command (mid-session)[​](#model-slash-command-mid-session "Direct link to model-slash-command-mid-session")

Switch between already-configured models without leaving a session:

```text
/model                              # Show current model and available options
/model claude-sonnet-4              # Switch model (auto-detects provider)
/model zai:glm-5                    # Switch provider and model
/model custom:qwen-2.5              # Use model on your custom endpoint
/model custom                       # Auto-detect model from custom endpoint
/model custom:local:qwen-2.5        # Use a named custom provider
/model openrouter:anthropic/claude-sonnet-4  # Switch back to cloud
```

By default, `/model` changes apply **to the current session only**. Add `--global` to persist the change to `config.yaml`:

```text
/model claude-sonnet-4 --global     # Switch and save as new default
```

What if I only see OpenRouter models?

If you've only configured OpenRouter, `/model` will only show OpenRouter models. To add another provider (Anthropic, DeepSeek, Copilot, etc.), exit your session and run `hermes model` from the terminal.

Provider and base URL changes are persisted to `config.yaml` automatically. When switching away from a custom endpoint, the stale base URL is cleared to prevent it leaking into other providers.

## `hermes gateway`[​](#hermes-gateway "Direct link to hermes-gateway")

```bash
hermes gateway <subcommand>
```

Subcommands:

SubcommandDescription`run`Run the gateway in the foreground. Recommended for WSL, Docker, and Termux.`start`Start the installed systemd/launchd background service.`stop`Stop the service (or foreground process).`restart`Restart the service.`status`Show service status.`install`Install as a systemd (Linux) or launchd (macOS) background service.`uninstall`Remove the installed service.`setup`Interactive messaging-platform setup.

WSL users

Use `hermes gateway run` instead of `hermes gateway start` — WSL's systemd support is unreliable. Wrap it in tmux for persistence: `tmux new -s hermes 'hermes gateway run'`. See [WSL FAQ](https://hermes-agent.nousresearch.com/docs/reference/faq#wsl-gateway-keeps-disconnecting-or-hermes-gateway-start-fails) for details.

## `hermes setup`[​](#hermes-setup "Direct link to hermes-setup")

```bash
hermes setup [model|tts|terminal|gateway|tools|agent][--non-interactive][--reset]
```

Use the full wizard or jump into one section:

SectionDescription`model`Provider and model setup.`terminal`Terminal backend and sandbox setup.`gateway`Messaging platform setup.`tools`Enable/disable tools per platform.`agent`Agent behavior settings.

Options:

OptionDescription`--non-interactive`Use defaults / environment values without prompts.`--reset`Reset configuration to defaults before setup.

## `hermes whatsapp`[​](#hermes-whatsapp "Direct link to hermes-whatsapp")

Runs the WhatsApp pairing/setup flow, including mode selection and QR-code pairing.

## `hermes login` / `hermes logout` *(Deprecated)*[​](#hermes-login--hermes-logout-deprecated "Direct link to hermes-login--hermes-logout-deprecated")

caution

`hermes login` has been removed. Use `hermes auth` to manage OAuth credentials, `hermes model` to select a provider, or `hermes setup` for full interactive setup.

## `hermes auth`[​](#hermes-auth "Direct link to hermes-auth")

Manage credential pools for same-provider key rotation. See [Credential Pools](https://hermes-agent.nousresearch.com/docs/user-guide/features/credential-pools) for full documentation.

```bash
hermes auth                                              # Interactive wizard
hermes auth list                                         # Show all pools
hermes auth list openrouter                              # Show specific provider
hermes auth add openrouter --api-key sk-or-v1-xxx        # Add API key
hermes auth add anthropic --type oauth                   # Add OAuth credential
hermes auth remove openrouter 2# Remove by index
hermes auth reset openrouter                             # Clear cooldowns
```

Subcommands: `add`, `list`, `remove`, `reset`. When called with no subcommand, launches the interactive management wizard.

## `hermes status`[​](#hermes-status "Direct link to hermes-status")

```bash
hermes status [--all][--deep]
```

OptionDescription`--all`Show all details in a shareable redacted format.`--deep`Run deeper checks that may take longer.

## `hermes cron`[​](#hermes-cron "Direct link to hermes-cron")

```bash
hermes cron<list|create|edit|pause|resume|run|remove|status|tick>
```

SubcommandDescription`list`Show scheduled jobs.`create` / `add`Create a scheduled job from a prompt, optionally attaching one or more skills via repeated `--skill`.`edit`Update a job's schedule, prompt, name, delivery, repeat count, or attached skills. Supports `--clear-skills`, `--add-skill`, and `--remove-skill`.`pause`Pause a job without deleting it.`resume`Resume a paused job and compute its next future run.`run`Trigger a job on the next scheduler tick.`remove`Delete a scheduled job.`status`Check whether the cron scheduler is running.`tick`Run due jobs once and exit.

## `hermes webhook`[​](#hermes-webhook "Direct link to hermes-webhook")

```bash
hermes webhook <subscribe|list|remove|test>
```

Manage dynamic webhook subscriptions for event-driven agent activation. Requires the webhook platform to be enabled in config — if not configured, prints setup instructions.

SubcommandDescription`subscribe` / `add`Create a webhook route. Returns the URL and HMAC secret to configure on your service.`list` / `ls`Show all agent-created subscriptions.`remove` / `rm`Delete a dynamic subscription. Static routes from config.yaml are not affected.`test`Send a test POST to verify a subscription is working.

### `hermes webhook subscribe`[​](#hermes-webhook-subscribe "Direct link to hermes-webhook-subscribe")

```bash
hermes webhook subscribe <name>[options]
```

OptionDescription`--prompt`Prompt template with `{dot.notation}` payload references.`--events`Comma-separated event types to accept (e.g. `issues,pull_request`). Empty = all.`--description`Human-readable description.`--skills`Comma-separated skill names to load for the agent run.`--deliver`Delivery target: `log` (default), `telegram`, `discord`, `slack`, `github_comment`.`--deliver-chat-id`Target chat/channel ID for cross-platform delivery.`--secret`Custom HMAC secret. Auto-generated if omitted.

Subscriptions persist to `~/.hermes/webhook_subscriptions.json` and are hot-reloaded by the webhook adapter without a gateway restart.

## `hermes doctor`[​](#hermes-doctor "Direct link to hermes-doctor")

OptionDescription`--fix`Attempt automatic repairs where possible.

## `hermes dump`[​](#hermes-dump "Direct link to hermes-dump")

```bash
hermes dump [--show-keys]
```

Outputs a compact, plain-text summary of your entire Hermes setup. Designed to be copy-pasted into Discord, GitHub issues, or Telegram when asking for support — no ANSI colors, no special formatting, just data.

OptionDescription`--show-keys`Show redacted API key prefixes (first and last 4 characters) instead of just `set`/`not set`.

### What it includes[​](#what-it-includes "Direct link to What it includes")

SectionDetails**Header**Hermes version, release date, git commit hash**Environment**OS, Python version, OpenAI SDK version**Identity**Active profile name, HERMES\_HOME path**Model**Configured default model and provider**Terminal**Backend type (local, docker, ssh, etc.)**API keys**Presence check for all 22 provider/tool API keys**Features**Enabled toolsets, MCP server count, memory provider**Services**Gateway status, configured messaging platforms**Workload**Cron job counts, installed skill count**Config overrides**Any config values that differ from defaults

### Example output[​](#example-output "Direct link to Example output")

```text
--- hermes dump ---
version:          0.8.0 (2026.4.8) [af4abd2f]
os:               Linux 6.14.0-37-generic x86_64
python:           3.11.14
openai_sdk:       2.24.0
profile:          default
hermes_home:      ~/.hermes
model:            anthropic/claude-opus-4.6
provider:         openrouter
terminal:         local

api_keys:
  openrouter           set
  openai               not set
  anthropic            set
  nous                 not set
  firecrawl            set
  ...

features:
  toolsets:           all
  mcp_servers:        0
  memory_provider:    built-in
  gateway:            running (systemd)
  platforms:          telegram, discord
  cron_jobs:          3 active / 5 total
  skills:             42

config_overrides:
  agent.max_turns: 250
  compression.threshold: 0.85
  display.streaming: True
--- end dump ---
```

### When to use[​](#when-to-use "Direct link to When to use")

- Reporting a bug on GitHub — paste the dump into your issue
- Asking for help in Discord — share it in a code block
- Comparing your setup to someone else's
- Quick sanity check when something isn't working

tip

`hermes dump` is specifically designed for sharing. For interactive diagnostics, use `hermes doctor`. For a visual overview, use `hermes status`.

## `hermes debug`[​](#hermes-debug "Direct link to hermes-debug")

```bash
hermes debug share [options]
```

Upload a debug report (system info + recent logs) to a paste service and get a shareable URL. Useful for quick support requests — includes everything a helper needs to diagnose your issue.

OptionDescription`--lines <N>`Number of log lines to include per log file (default: 200).`--expire <days>`Paste expiry in days (default: 7).`--local`Print the report locally instead of uploading.

The report includes system info (OS, Python version, Hermes version), recent agent and gateway logs (512 KB limit per file), and redacted API key status. Keys are always redacted — no secrets are uploaded.

Paste services tried in order: paste.rs, dpaste.com.

### Examples[​](#examples "Direct link to Examples")

```bash
hermes debug share              # Upload debug report, print URL
hermes debug share --lines500# Include more log lines
hermes debug share --expire30# Keep paste for 30 days
hermes debug share --local# Print report to terminal (no upload)
```

## `hermes backup`[​](#hermes-backup "Direct link to hermes-backup")

Create a zip archive of your Hermes configuration, skills, sessions, and data. The backup excludes the hermes-agent codebase itself.

OptionDescription`-o`, `--output <path>`Output path for the zip file (default: `~/hermes-backup-<timestamp>.zip`).`-q`, `--quick`Quick snapshot: only critical state files (config.yaml, state.db, .env, auth, cron jobs). Much faster than a full backup.`-l`, `--label <name>`Label for the snapshot (only used with `--quick`).

The backup uses SQLite's `backup()` API for safe copying, so it works correctly even when Hermes is running (WAL-mode safe).

### Examples[​](#examples-1 "Direct link to Examples")

```bash
hermes backup                           # Full backup to ~/hermes-backup-*.zip
hermes backup -o /tmp/hermes.zip        # Full backup to specific path
hermes backup --quick# Quick state-only snapshot
hermes backup --quick--label"pre-upgrade"# Quick snapshot with label
```

## `hermes import`[​](#hermes-import "Direct link to hermes-import")

```bash
hermes import<zipfile>[options]
```

Restore a previously created Hermes backup into your Hermes home directory.

OptionDescription`-f`, `--force`Overwrite existing files without confirmation.

## `hermes logs`[​](#hermes-logs "Direct link to hermes-logs")

```bash
hermes logs [log_name][options]
```

View, tail, and filter Hermes log files. All logs are stored in `~/.hermes/logs/` (or `<profile>/logs/` for non-default profiles).

### Log files[​](#log-files "Direct link to Log files")

NameFileWhat it captures`agent` (default)`agent.log`All agent activity — API calls, tool dispatch, session lifecycle (INFO and above)`errors``errors.log`Warnings and errors only — a filtered subset of agent.log`gateway``gateway.log`Messaging gateway activity — platform connections, message dispatch, webhook events

### Options[​](#options "Direct link to Options")

OptionDescription`log_name`Which log to view: `agent` (default), `errors`, `gateway`, or `list` to show available files with sizes.`-n`, `--lines <N>`Number of lines to show (default: 50).`-f`, `--follow`Follow the log in real time, like `tail -f`. Press Ctrl+C to stop.`--level <LEVEL>`Minimum log level to show: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.`--session <ID>`Filter lines containing a session ID substring.`--since <TIME>`Show lines from a relative time ago: `30m`, `1h`, `2d`, etc. Supports `s` (seconds), `m` (minutes), `h` (hours), `d` (days).`--component <NAME>`Filter by component: `gateway`, `agent`, `tools`, `cli`, `cron`.

### Examples[​](#examples-2 "Direct link to Examples")

```bash
# View the last 50 lines of agent.log (default)
hermes logs

# Follow agent.log in real time
hermes logs -f

# View the last 100 lines of gateway.log
hermes logs gateway -n100

# Show only warnings and errors from the last hour
hermes logs --level WARNING --since 1h

# Filter by a specific session
hermes logs --session abc123

# Follow errors.log, starting from 30 minutes ago
hermes logs errors --since 30m -f

# List all log files with their sizes
hermes logs list
```

### Filtering[​](#filtering "Direct link to Filtering")

Filters can be combined. When multiple filters are active, a log line must pass **all** of them to be shown:

```bash
# WARNING+ lines from the last 2 hours containing session "tg-12345"
hermes logs --level WARNING --since 2h --session tg-12345
```

Lines without a parseable timestamp are included when `--since` is active (they may be continuation lines from a multi-line log entry). Lines without a detectable level are included when `--level` is active.

### Log rotation[​](#log-rotation "Direct link to Log rotation")

Hermes uses Python's `RotatingFileHandler`. Old logs are rotated automatically — look for `agent.log.1`, `agent.log.2`, etc. The `hermes logs list` subcommand shows all log files including rotated ones.

## `hermes config`[​](#hermes-config "Direct link to hermes-config")

```bash
hermes config <subcommand>
```

Subcommands:

SubcommandDescription`show`Show current config values.`edit`Open `config.yaml` in your editor.`set <key> <value>`Set a config value.`path`Print the config file path.`env-path`Print the `.env` file path.`check`Check for missing or stale config.`migrate`Add newly introduced options interactively.

## `hermes pairing`[​](#hermes-pairing "Direct link to hermes-pairing")

```bash
hermes pairing <list|approve|revoke|clear-pending>
```

SubcommandDescription`list`Show pending and approved users.`approve <platform> <code>`Approve a pairing code.`revoke <platform> <user-id>`Revoke a user's access.`clear-pending`Clear pending pairing codes.

## `hermes skills`[​](#hermes-skills "Direct link to hermes-skills")

```bash
hermes skills <subcommand>
```

Subcommands:

SubcommandDescription`browse`Paginated browser for skill registries.`search`Search skill registries.`install`Install a skill.`inspect`Preview a skill without installing it.`list`List installed skills.`check`Check installed hub skills for upstream updates.`update`Reinstall hub skills with upstream changes when available.`audit`Re-scan installed hub skills.`uninstall`Remove a hub-installed skill.`publish`Publish a skill to a registry.`snapshot`Export/import skill configurations.`tap`Manage custom skill sources.`config`Interactive enable/disable configuration for skills by platform.

Common examples:

```bash
hermes skills browse
hermes skills browse --source official
hermes skills search react --source skills-sh
hermes skills search https://mintlify.com/docs --source well-known
hermes skills inspect official/security/1password
hermes skills inspect skills-sh/vercel-labs/json-render/json-render-react
hermes skills install official/migration/openclaw-migration
hermes skills install skills-sh/anthropics/skills/pdf --force
hermes skills check
hermes skills update
hermes skills config
```

Notes:

- `--force` can override non-dangerous policy blocks for third-party/community skills.
- `--force` does not override a `dangerous` scan verdict.
- `--source skills-sh` searches the public `skills.sh` directory.
- `--source well-known` lets you point Hermes at a site exposing `/.well-known/skills/index.json`.

## `hermes honcho`[​](#hermes-honcho "Direct link to hermes-honcho")

```bash
hermes honcho [--target-profile NAME]<subcommand>
```

Manage Honcho cross-session memory integration. This command is provided by the Honcho memory provider plugin and is only available when `memory.provider` is set to `honcho` in your config.

The `--target-profile` flag lets you manage another profile's Honcho config without switching to it.

Subcommands:

SubcommandDescription`setup`Redirects to `hermes memory setup` (unified setup path).`status [--all]`Show current Honcho config and connection status. `--all` shows a cross-profile overview.`peers`Show peer identities across all profiles.`sessions`List known Honcho session mappings.`map [name]`Map the current directory to a Honcho session name. Omit `name` to list current mappings.`peer`Show or update peer names and dialectic reasoning level. Options: `--user NAME`, `--ai NAME`, `--reasoning LEVEL`.`mode [mode]`Show or set recall mode: `hybrid`, `context`, or `tools`. Omit to show current.`tokens`Show or set token budgets for context and dialectic. Options: `--context N`, `--dialectic N`.`identity [file] [--show]`Seed or show the AI peer identity representation.`enable`Enable Honcho for the active profile.`disable`Disable Honcho for the active profile.`sync`Sync Honcho config to all existing profiles (creates missing host blocks).`migrate`Step-by-step migration guide from openclaw-honcho to Hermes Honcho.

## `hermes memory`[​](#hermes-memory "Direct link to hermes-memory")

```bash
hermes memory <subcommand>
```

Set up and manage external memory provider plugins. Available providers: honcho, openviking, mem0, hindsight, holographic, retaindb, byterover, supermemory. Only one external provider can be active at a time. Built-in memory (MEMORY.md/USER.md) is always active.

Subcommands:

SubcommandDescription`setup`Interactive provider selection and configuration.`status`Show current memory provider config.`off`Disable external provider (built-in only).

## `hermes acp`[​](#hermes-acp "Direct link to hermes-acp")

Starts Hermes as an ACP (Agent Client Protocol) stdio server for editor integration.

Related entrypoints:

```bash
hermes-acp
python -m acp_adapter
```

Install support first:

See [ACP Editor Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp) and [ACP Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals).

## `hermes mcp`[​](#hermes-mcp "Direct link to hermes-mcp")

Manage MCP (Model Context Protocol) server configurations and run Hermes as an MCP server.

SubcommandDescription`serve [-v|--verbose]`Run Hermes as an MCP server — expose conversations to other agents.`add <name> [--url URL] [--command CMD] [--args ...] [--auth oauth|header]`Add an MCP server with automatic tool discovery.`remove <name>` (alias: `rm`)Remove an MCP server from config.`list` (alias: `ls`)List configured MCP servers.`test <name>`Test connection to an MCP server.`configure <name>` (alias: `config`)Toggle tool selection for a server.

See [MCP Config Reference](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference), [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes), and [MCP Server Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp#running-hermes-as-an-mcp-server).

## `hermes plugins`[​](#hermes-plugins "Direct link to hermes-plugins")

```bash
hermes plugins [subcommand]
```

Unified plugin management — general plugins, memory providers, and context engines in one place. Running `hermes plugins` with no subcommand opens a composite interactive screen with two sections:

- **General Plugins** — multi-select checkboxes to enable/disable installed plugins
- **Provider Plugins** — single-select configuration for Memory Provider and Context Engine. Press ENTER on a category to open a radio picker.

SubcommandDescription*(none)*Composite interactive UI — general plugin toggles + provider plugin configuration.`install <identifier> [--force]`Install a plugin from a Git URL or `owner/repo`.`update <name>`Pull latest changes for an installed plugin.`remove <name>` (aliases: `rm`, `uninstall`)Remove an installed plugin.`enable <name>`Enable a disabled plugin.`disable <name>`Disable a plugin without removing it.`list` (alias: `ls`)List installed plugins with enabled/disabled status.

Provider plugin selections are saved to `config.yaml`:

- `memory.provider` — active memory provider (empty = built-in only)
- `context.engine` — active context engine (`"compressor"` = built-in default)

General plugin disabled list is stored in `config.yaml` under `plugins.disabled`.

See [Plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins) and [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin).

OptionDescription`--summary`Print the current enabled-tools summary and exit.

Without `--summary`, this launches the interactive per-platform tool configuration UI.

## `hermes sessions`[​](#hermes-sessions "Direct link to hermes-sessions")

```bash
hermes sessions <subcommand>
```

Subcommands:

SubcommandDescription`list`List recent sessions.`browse`Interactive session picker with search and resume.`export <output> [--session-id ID]`Export sessions to JSONL.`delete <session-id>`Delete one session.`prune`Delete old sessions.`stats`Show session-store statistics.`rename <session-id> <title>`Set or change a session title.

## `hermes insights`[​](#hermes-insights "Direct link to hermes-insights")

```bash
hermes insights [--days N][--source platform]
```

OptionDescription`--days <n>`Analyze the last `n` days (default: 30).`--source <platform>`Filter by source such as `cli`, `telegram`, or `discord`.

## `hermes claw`[​](#hermes-claw "Direct link to hermes-claw")

```bash
hermes claw migrate [options]
```

Migrate your OpenClaw setup to Hermes. Reads from `~/.openclaw` (or a custom path) and writes to `~/.hermes`. Automatically detects legacy directory names (`~/.clawdbot`, `~/.moltbot`) and config filenames (`clawdbot.json`, `moltbot.json`).

OptionDescription`--dry-run`Preview what would be migrated without writing anything.`--preset <name>`Migration preset: `full` (default, includes secrets) or `user-data` (excludes API keys).`--overwrite`Overwrite existing Hermes files on conflicts (default: skip).`--migrate-secrets`Include API keys in migration (enabled by default with `--preset full`).`--source <path>`Custom OpenClaw directory (default: `~/.openclaw`).`--workspace-target <path>`Target directory for workspace instructions (AGENTS.md).`--skill-conflict <mode>`Handle skill name collisions: `skip` (default), `overwrite`, or `rename`.`--yes`Skip the confirmation prompt.

### What gets migrated[​](#what-gets-migrated "Direct link to What gets migrated")

The migration covers 30+ categories across persona, memory, skills, model providers, messaging platforms, agent behavior, session policies, MCP servers, TTS, and more. Items are either **directly imported** into Hermes equivalents or **archived** for manual review.

**Directly imported:** SOUL.md, MEMORY.md, USER.md, AGENTS.md, skills (4 source directories), default model, custom providers, MCP servers, messaging platform tokens and allowlists (Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost), agent defaults (reasoning effort, compression, human delay, timezone, sandbox), session reset policies, approval rules, TTS config, browser settings, tool settings, exec timeout, command allowlist, gateway config, and API keys from 3 sources.

**Archived for manual review:** Cron jobs, plugins, hooks/webhooks, memory backend (QMD), skills registry config, UI/identity, logging, multi-agent setup, channel bindings, IDENTITY.md, TOOLS.md, HEARTBEAT.md, BOOTSTRAP.md.

**API key resolution** checks three sources in priority order: config values → `~/.openclaw/.env` → `auth-profiles.json`. All token fields handle plain strings, env templates (`${VAR}`), and SecretRef objects.

For the complete config key mapping, SecretRef handling details, and post-migration checklist, see the [**full migration guide**](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw).

### Examples[​](#examples-3 "Direct link to Examples")

```bash
# Preview what would be migrated
hermes claw migrate --dry-run

# Full migration including API keys
hermes claw migrate --preset full

# Migrate user data only (no secrets), overwrite conflicts
hermes claw migrate --preset user-data --overwrite

# Migrate from a custom OpenClaw path
hermes claw migrate --source /home/user/old-openclaw
```

## `hermes dashboard`[​](#hermes-dashboard "Direct link to hermes-dashboard")

```bash
hermes dashboard [options]
```

Launch the web dashboard — a browser-based UI for managing configuration, API keys, and monitoring sessions. Requires `pip install hermes-agent[web]` (FastAPI + Uvicorn). See [Web Dashboard](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard) for full documentation.

OptionDefaultDescription`--port``9119`Port to run the web server on`--host``127.0.0.1`Bind address`--no-open`—Don't auto-open the browser

```bash
# Default — opens browser to http://127.0.0.1:9119
hermes dashboard

# Custom port, no browser
hermes dashboard --port8080 --no-open
```

## `hermes profile`[​](#hermes-profile "Direct link to hermes-profile")

```bash
hermes profile <subcommand>
```

Manage profiles — multiple isolated Hermes instances, each with its own config, sessions, skills, and home directory.

SubcommandDescription`list`List all profiles.`use <name>`Set a sticky default profile.`create <name> [--clone] [--clone-all] [--clone-from <source>] [--no-alias]`Create a new profile. `--clone` copies config, `.env`, and `SOUL.md` from the active profile. `--clone-all` copies all state. `--clone-from` specifies a source profile.`delete <name> [-y]`Delete a profile.`show <name>`Show profile details (home directory, config, etc.).`alias <name> [--remove] [--name NAME]`Manage wrapper scripts for quick profile access.`rename <old> <new>`Rename a profile.`export <name> [-o FILE]`Export a profile to a `.tar.gz` archive.`import <archive> [--name NAME]`Import a profile from a `.tar.gz` archive.

Examples:

```bash
hermes profile list
hermes profile create work --clone
hermes profile use work
hermes profile alias work --name h-work
hermes profile export work -o work-backup.tar.gz
hermes profile import work-backup.tar.gz --name restored
hermes -p work chat -q"Hello from work profile"
```

## `hermes completion`[​](#hermes-completion "Direct link to hermes-completion")

```bash
hermes completion [bash|zsh]
```

Print a shell completion script to stdout. Source the output in your shell profile for tab-completion of Hermes commands, subcommands, and profile names.

Examples:

```bash
# Bash
hermes completion bash>> ~/.bashrc

# Zsh
hermes completion zsh>> ~/.zshrc
```

## Maintenance commands[​](#maintenance-commands "Direct link to Maintenance commands")

CommandDescription`hermes version`Print version information.`hermes update`Pull latest changes and reinstall dependencies.`hermes uninstall [--full] [--yes]`Remove Hermes, optionally deleting all config/data.

## See also[​](#see-also "Direct link to See also")

- [Slash Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)
- [CLI Interface](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
- [Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions)
- [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Skins & Themes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins)