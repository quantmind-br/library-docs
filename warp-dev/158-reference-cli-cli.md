---
title: Oz CLI | Reference | Warp
url: https://docs.warp.dev/reference/cli/cli
source: sitemap
fetched_at: 2026-04-29T15:04:58.732235446-03:00
rendered_js: false
word_count: 659
summary: The Oz CLI is a command-line tool used to execute, manage, and automate Warp cloud agents locally or in remote environments.
tags:
    - cli-tool
    - warp-agents
    - automation
    - cloud-computing
    - command-line-interface
    - mcp
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
> [!info]
> `warp-cli` is deprecated and replaced by `oz`. Replace `warp-cli` with `oz` in all scripts and workflows.

## What is the Oz CLI?

The Oz CLI runs [Cloud Agents](https://docs.warp.dev/agent-platform/cloud-agents/overview) from terminals, scripts, or automated systems. It turns a **prompt + configuration** into an executable agent task running on Warp-hosted or [self-hosted](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting) infrastructure.

Capabilities:
- Run agents locally for development/debugging
- Run agents on remote machines
- Connect agents to MCP servers (GitHub, Linear, etc.)
- Configure integrations with Slack, Linear, and other trigger surfaces

## Install the CLI

### Bundled with Warp

The Oz CLI is included with the Warp desktop app. To make it globally available in your PATH:

1. In the search field, find and select **Install Oz CLI Command**

> [!info]
> Administrator permissions are required to install into `/usr/local/bin`.

### Standalone (Homebrew)

```bash
brew install warpdotdev/warp/warp
```

Preview version:
```bash
brew install warpdotdev/warp/warp --with-warp-preview
```

### Direct download

Download from the Warp releases page. These builds do not auto-update.

## Log in

Two authentication methods:

| Method | Best for |
|---|---|
| Interactive login | Local machines with browser access |
| API keys | CI pipelines, headless servers, VMs, containers |

**Interactive login:** `oz login` — prints a URL to open in a browser. On hosts already signed in to Warp, credentials are reused automatically.

**API key:** Set `WARP_API_KEY=wk-...` (see [API Keys](https://docs.warp.dev/reference/cli/api-keys)).

## Run agents

| Command | Use when |
|---|---|
| `oz agent run` | Developing locally, immediate feedback, file inspection, debugging |
| `oz agent run-cloud` | Remote/standardized environments, CI/CD, background processing |

### Local: `oz agent run`

```bash
oz agent run --prompt "<TASK>" [flags]
```

| Flag | Description |
|---|---|
| `--cwd`, `-C` | Run from a different directory |
| `--name`, `-n` | Label the run for grouping/traceability |
| `--share` | Share the session with teammates |
| `--skill <SPEC>` | Use a skill as the base prompt |
| `--mcp <SPEC>` | Start one or more MCP servers before execution |
| `--environment`, `-e` | Run in a specific cloud environment |
| `--file`, `-f` | Load run config from a YAML or JSON file |

### Remote: `oz agent run-cloud`

```bash
oz agent run-cloud --environment <ENV_ID> --prompt "<TASK>" [flags]
```

| Flag | Description |
|---|---|
| `--environment`, `-e` | Select the environment |
| `--no-environment` | Run without an environment (not recommended) |
| `--open` | Open the session in Warp once available |
| `--name`, `-n` | Label the run |
| `--mcp <SPEC>` | Start MCP servers |
| `--model <MODEL_ID>` | Override the default model |
| `--skill <SPEC>` | Use a skill from the environment's repo |
| `--host <WORKER_ID>` | Run on a specific self-hosted worker |
| `--attach <PATH>` | Attach a file to the agent query (max 5) |
| `--file`, `-f` | Load run config from a YAML or JSON file |

> [!info]
> `run-cloud` does **not** use `--cwd`, `--share`, or `--profile`.

### Naming runs

The `--name` flag groups related runs under a shared label for filtering and tracking. For skill-based runs, the name is auto-set to the skill name. Filter by name using the `name` query parameter on `GET /agent/runs` in the [Oz API](https://docs.warp.dev/reference/api-and-sdk).

**If cloud runs fail:** Verify the environment has the correct repo/context, the profile allows needed commands/MCP servers, and environment variables are set in the environment (not locally).

## Additional features

### Agent profiles

Apply a profile with `--profile` on `oz agent run`. See [Agent profiles](https://docs.warp.dev/reference/cli/agent-profiles).

### MCP servers

Connect agents to GitHub, Linear, Sentry, etc. Use `--mcp` with a UUID, inline JSON, or JSON file path. See [MCP Servers](https://docs.warp.dev/reference/cli/mcp-servers).

### Skills

Use `--skill` to run an agent from a skill stored in a repository. See [Skills](https://docs.warp.dev/reference/cli/skills).

### Collaboration

Share agent sessions with `--share`:

```bash
--share user@email.com       # read-only
--share user@email.com:edit  # read/write
--share team                 # all team members, read-only
--share team:edit            # all team members, read/write
```

### Warp Drive objects

Use `--saved-prompt` to reuse saved prompts, and reference notebooks, workflows, and rules inline in `--prompt`. See [Referencing Warp Drive objects](https://docs.warp.dev/reference/cli/warp-drive).

## Additional commands

```bash
oz agent list                      # list available skills from environments
oz agent list --repo <REPO>        # filter by repository
oz run list                        # list cloud agent runs
oz run get <RUN_ID>                # inspect a specific run
oz model list                      # list available models
oz environment image list          # list suggested base images for environments
```

## Troubleshooting

See [Troubleshooting](https://docs.warp.dev/reference/cli/troubleshooting) for CLI help commands and solutions to common errors (authentication, agent failures, environment problems, Docker issues).

#cli-tool #warp-agents #automation #cloud-computing #command-line-interface #mcp
