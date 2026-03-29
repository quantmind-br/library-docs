---
title: CLI
url: https://docs.docker.com/ai/cagent/reference/cli/
source: llms
fetched_at: 2026-01-24T14:13:35.485679656-03:00
rendered_js: false
word_count: 735
summary: This document provides a comprehensive command-line reference for cagent, detailing the commands and flags required to build, run, manage, and deploy AI agents.
tags:
    - cli-reference
    - ai-agents
    - cagent
    - docker-ai
    - mcp-protocol
    - agent-deployment
category: reference
---

## CLI reference

Command-line interface for running, managing, and deploying AI agents.

For agent configuration file syntax, see the [Configuration file reference](https://docs.docker.com/ai/cagent/reference/config/). For toolset capabilities, see the [Toolsets reference](https://docs.docker.com/ai/cagent/reference/toolsets/).

Work with all commands:

FlagTypeDefaultDescription`-d`, `--debug`booleanfalseEnable debug logging`-o`, `--otel`booleanfalseEnable OpenTelemetry`--log-file`string-Debug log file path

Debug logs write to `~/.cagent/cagent.debug.log` by default. Override with `--log-file`.

Work with most commands. Supported commands link to this section.

FlagTypeDefaultDescription`--models-gateway`string-Models gateway address`--env-from-file`array-Load environment variables from file`--code-mode-tools`booleanfalseEnable JavaScript tool orchestration`--working-dir`string-Working directory for the session

Set `--models-gateway` via `CAGENT_MODELS_GATEWAY` environment variable.

### [a2a](#a2a)

Expose agent via the Agent2Agent (A2A) protocol. Allows other A2A-compatible systems to discover and interact with your agent. Auto-selects an available port if not specified.

> A2A support is currently experimental and needs further work. Tool calls are handled internally and not exposed as separate ADK events. Some ADK features are not yet integrated.

Arguments:

- `agent-file|registry-ref` - Path to YAML or OCI registry reference (required)

Flags:

FlagTypeDefaultDescription`-a`, `--agent`stringrootAgent name`--port`integer0Port (0 = random)

Supports [runtime flags](#runtime-flags).

Examples:

### [acp](#acp)

Start agent as ACP (Agent Client Protocol) server on stdio for editor integration. See [ACP integration](https://docs.docker.com/ai/cagent/integrations/acp/) for setup guides.

Arguments:

- `agent-file|registry-ref` - Path to YAML or OCI registry reference (required)

Supports [runtime flags](#runtime-flags).

### [alias add](#alias-add)

Create alias for agent.

Arguments:

- `name` - Alias name (required)
- `target` - Path to YAML or registry reference (required)

Examples:

Setting alias name to "default" lets you run `cagent run` without arguments.

### [alias list](#alias-list)

List all aliases.

### [alias remove](#alias-remove)

Remove alias.

Arguments:

- `name` - Alias name (required)

### [api](#api)

HTTP API server.

Arguments:

- `agent-file|agents-dir` - Path to YAML or directory with agents (required)

Flags:

FlagTypeDefaultDescription`-l`, `--listen`string:8080Listen address`-s`, `--session-db`stringsession.dbSession database path`--pull-interval`integer0Auto-pull OCI ref every N minutes

Supports [runtime flags](#runtime-flags).

Examples:

The `--pull-interval` flag works only with OCI references. Automatically pulls and reloads at the specified interval.

### [build](#build)

Build Docker image for agent.

Arguments:

- `agent-file|registry-ref` - Path to YAML or OCI registry reference (required)
- `image-name` - Docker image name (optional)

Flags:

FlagTypeDefaultDescription`--dry-run`booleanfalsePrint Dockerfile only`--push`booleanfalsePush image after build`--no-cache`booleanfalseBuild without cache`--pull`booleanfalsePull all referenced images

Example:

### [catalog list](#catalog-list)

List catalog agents.

Arguments:

- `org` - Organization name (optional, default: `agentcatalog`)

Queries Docker Hub for agent repositories.

### [debug config](#debug-config)

Show resolved agent configuration.

Arguments:

- `agent-file|registry-ref` - Path to YAML or OCI registry reference (required)

Supports [runtime flags](#runtime-flags).

Shows canonical configuration in YAML after all processing and defaults.

### [debug toolsets](#debug-toolsets)

List agent tools.

Arguments:

- `agent-file|registry-ref` - Path to YAML or OCI registry reference (required)

Supports [runtime flags](#runtime-flags).

Lists all tools for each agent in the configuration.

### [eval](#eval)

Run evaluation tests.

Arguments:

- `agent-file|registry-ref` - Path to YAML or OCI registry reference (required)
- `eval-dir` - Evaluation files directory (optional, default: `./evals`)

Supports [runtime flags](#runtime-flags).

### [exec](#exec)

Single message execution without TUI.

Arguments:

- `agent-file|registry-ref` - Path to YAML or OCI registry reference (required)
- `message` - Prompt, or `-` for stdin (optional)

Same flags as [run](#run).

Supports [runtime flags](#runtime-flags).

Examples:

### [feedback](#feedback)

Submit feedback.

Shows link to submit feedback.

### [mcp](#mcp)

MCP (Model Context Protocol) server on stdio. Exposes agents as tools to MCP clients. See [MCP integration](https://docs.docker.com/ai/cagent/integrations/mcp/) for setup guides.

Arguments:

- `agent-file|registry-ref` - Path to YAML or OCI registry reference (required)

Supports [runtime flags](#runtime-flags).

Examples:

### [new](#new)

Create agent configuration interactively.

Flags:

FlagTypeDefaultDescription`--model`string-Model as `provider/model``--max-iterations`integer0Maximum agentic loop iterations

Supports [runtime flags](#runtime-flags).

Opens interactive TUI to configure and generate agent YAML.

### [pull](#pull)

Pull agent from OCI registry.

Arguments:

- `registry-ref` - OCI registry reference (required)

Flags:

FlagTypeDefaultDescription`--force`booleanfalsePull even if already exists

Example:

Saves to local YAML file.

### [push](#push)

Push agent to OCI registry.

Arguments:

- `agent-file` - Path to local YAML (required)
- `registry-ref` - OCI reference like `docker.io/user/agent:latest` (required)

Example:

### [run](#run)

Interactive terminal UI for agent sessions.

Arguments:

- `agent-file|registry-ref` - Path to YAML or OCI registry reference (optional)
- `message` - Initial prompt, or `-` for stdin (optional)

Flags:

FlagTypeDefaultDescription`-a`, `--agent`stringrootAgent name`--yolo`booleanfalseAuto-approve all tool calls`--attach`string-Attach image file`--model`array-Override model (repeatable)`--dry-run`booleanfalseInitialize without executing`--remote`string-Remote runtime address

Supports [runtime flags](#runtime-flags).

Examples:

Running without arguments uses the default agent or a "default" alias if configured.

Shows interactive TUI in a terminal. Falls back to exec mode otherwise.

#### [Interactive commands](#interactive-commands)

TUI slash commands:

CommandDescription`/exit`Exit`/reset`Clear history`/eval`Save conversation for evaluation`/compact`Compact conversation`/yolo`Toggle auto-approval

### [version](#version)

Print version information.

Shows cagent version and commit hash.

VariableDescription`CAGENT_MODELS_GATEWAY`Models gateway address`TELEMETRY_ENABLED`Telemetry control (set `false`)`CAGENT_HIDE_TELEMETRY_BANNER`Hide telemetry banner (set `1`)`OTEL_EXPORTER_OTLP_ENDPOINT`OpenTelemetry endpoint

Override models specified in your configuration file using the `--model` flag.

Format: `[agent=]provider/model`

Without an agent name, the model applies to all agents. With an agent name, it applies only to that specific agent.

Apply to all agents:

Apply to specific agents only:

Providers: `openai`, `anthropic`, `google`, `dmr`

Omit provider for automatic selection based on model name.