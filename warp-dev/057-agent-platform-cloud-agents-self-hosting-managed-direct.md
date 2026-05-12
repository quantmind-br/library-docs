---
title: 'Managed: Direct | Agents | Warp'
url: https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-direct
source: sitemap
fetched_at: 2026-04-29T15:04:47.956709484-03:00
rendered_js: false
word_count: 550
summary: This document explains how to configure and use the Direct backend for oz-agent-worker, which allows tasks to execute directly on a host filesystem without containerization.
tags:
    - oz-agent
    - direct-backend
    - self-hosting
    - worker-daemon
    - task-orchestration
    - workspace-management
category: guide
optimized: true
optimized_at: 2026-04-29T15:04:47.956709484-03:00
---
Run the `oz-agent-worker` daemon with the **Direct backend** — tasks execute directly on the worker host without Docker or Kubernetes. Oz still orchestrates runs end to end (Slack, Linear, schedules, API, `oz agent run-cloud`); the worker runs the agent in a per-task workspace on its own filesystem.

> [!warning]
> The Direct backend does **not** provide per-task container isolation. Each task runs in an isolated workspace directory but shares the host OS and kernel. Evaluate whether this fits your security requirements before production use.

## When to use the Direct backend

- Neither Docker nor Kubernetes is available on the worker host
- Tasks need direct access to host resources hard to expose through a container
- You want managed orchestration without container runtime overhead

## How it works

1. The worker creates a per-task workspace directory under `workspace_root`
2. If a `setup_command` is configured, it runs before the task with environment variables pointing to the workspace
3. The `oz` CLI runs the agent task inside the workspace directory
4. After the task completes, the optional `teardown_command` runs and the workspace is cleaned up

## Prerequisites

- **Enterprise plan with self-hosting enabled** — [Contact sales](https://warp.dev/contact-sales) if self-hosting is not yet enabled for your team
- **A worker host** with write access to `workspace_root` (defaults to `/var/lib/oz/workspaces`)
- **The Oz CLI** installed and available in `PATH` on the worker host (or specify `oz_path` in the config file). See [Installing the CLI](https://docs.warp.dev/reference/cli#installing-the-cli)
- **A team API key** — In the Warp app, go to **Settings** > **Cloud platform** > **Oz Cloud API Keys**. See [API Keys](https://docs.warp.dev/reference/cli/api-keys)

## Setup

### 1. Set your API key

```bash
export WARP_API_KEY="your-api-key"
```

### 2. Start the worker with the Direct backend

Pass `--backend direct`:

```bash
oz-agent-worker start \
  --worker-id "my-worker" \
  --backend direct \
  --api-key "$WARP_API_KEY"
```

Or with a [config file](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/reference#config-file):

```yaml
worker_id: "my-worker"
api_key: "${WARP_API_KEY}"
backend: direct
workspace_root: "/var/lib/oz/workspaces"
```

**Expected outcome:** The worker connects to Oz and begins listening for tasks. Each assigned task runs in a freshly-created subdirectory of `workspace_root`.

## Workspace model

Each task gets its own directory under `workspace_root` (default: `/var/lib/oz/workspaces`). Override with the `workspace_root` config option.

After task completion, the workspace is deleted unless `--no-cleanup` is set (keeps directory for debugging).

## Setup and teardown commands

The `setup_command` runs before each task and receives these environment variables:

| Variable | Description |
|----------|-------------|
| `OZ_WORKSPACE_ROOT` | The workspace directory for the task |
| `OZ_RUN_ID` | The unique task ID |
| `OZ_ENVIRONMENT_FILE` | Path to a file where the setup script can write additional `KEY=VALUE` environment variables to inject into the task |
| `OZ_WORKER_BACKEND` | Always set to `direct` |

The `teardown_command` runs after each task and receives `OZ_WORKSPACE_ROOT`, `OZ_RUN_ID`, and `OZ_WORKER_BACKEND`.

Use the setup command to clone repos, install dependencies, or write task-specific env vars into `OZ_ENVIRONMENT_FILE`. Use the teardown command for cleanup or reporting.

## Environment variables for Direct tasks

> [!info]
> The Direct backend starts tasks with a **minimal environment** (only `HOME`, `TMPDIR`, and `PATH` from the host) to avoid leaking sensitive worker credentials like `WARP_API_KEY` into tasks. Add variables explicitly via `environment` in the config file or `-e` flags on the worker CLI.

Config file example:

```yaml
worker_id: "my-worker"
api_key: "${WARP_API_KEY}"
backend: direct
workspace_root: "/var/lib/oz/workspaces"
environment:
  DATABASE_URL: "postgres://..."
  API_SECRET: "${API_SECRET}"
```

## Related pages

- [[209-agent-platform-cloud-agents-self-hosting#routing-runs-to-self-hosted-workers|Routing runs to self-hosted workers]] — Send tasks to your connected worker from CLI, schedules, integrations, API, and web UI
- [[209-agent-platform-cloud-agents-self-hosting-security-and-networking|Security and networking]] — Data boundaries and security considerations for the Direct backend

Last updated 21 hours ago