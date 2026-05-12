---
title: Self-hosting quickstart | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/quickstart
source: sitemap
fetched_at: 2026-04-29T15:04:44.772677882-03:00
rendered_js: false
word_count: 561
summary: This document provides a step-by-step guide for deploying and configuring an Oz cloud agent using a managed Docker-based infrastructure.
tags:
    - cloud-agents
    - self-hosting
    - docker-containers
    - infrastructure-setup
    - managed-architecture
    - dev-ops
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Run your first Oz cloud agent on your own infrastructure in ~10 minutes using the managed architecture with the Docker backend — the default and fastest path to self-hosting.

> [!info]
> This quickstart sets up the [managed architecture](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting#managed-architecture), where Oz orchestrates the agent and your worker provides the compute. **Prefer a CLI-only path with no Docker requirement?** Jump to the [Unmanaged quickstart](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged#unmanaged-quickstart) to run `oz agent run` directly on any host.

## Prerequisites

- **Enterprise plan with self-hosting enabled** — [Contact sales](https://warp.dev/contact-sales) if self-hosting is not yet enabled for your team.
- **A Linux machine with Docker** — A VM, server, or local machine with the Docker daemon running Linux containers. Verify with `docker info`. Docker Desktop on macOS or Windows works for testing.
- **A team API key** — In the Warp app, go to **Settings** > **Cloud platform** > **Oz Cloud API Keys** to create a team-scoped API key. See [API Keys](https://docs.warp.dev/reference/cli/api-keys) for details.

## Run your first self-hosted agent

*~10 minutes*

### 1. Export your API key

Export the team API key so the worker container can authenticate to Oz automatically:

```bash
export OZ_API_KEY=<your-team-api-key>
```

### 2. Start the worker

Run the `oz-agent-worker` container, mounting the host's Docker socket so the worker can spawn task containers. Choose any `--worker-id` meaningful for your team — you'll use this value to route tasks to this worker.

```bash
docker run -d \
  --restart unless-stopped \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e OZ_API_KEY \
  warpdotdev/oz-agent-worker:latest \
  --worker-id <your-worker-id>
```

**Expected outcome:** The worker connects to Oz and begins listening for tasks. You should see log output confirming the connection (something like `Connected to Oz` / `Waiting for tasks`).

> [!warning]
> For production deployments, pin to a specific image digest (e.g., `warpdotdev/oz-agent-worker@sha256:...`) instead of the `latest` tag.

### 3. Route a run to your worker

In a separate terminal on any machine with the Oz CLI, route a cloud agent run to your worker by passing `--host` with the worker ID you chose:

```bash
oz agent run-cloud \
  --env-id <env-id> \
  --host <your-worker-id> \
  "Analyze the latest commits and summarize changes"
```

**Expected outcome:** Oz accepts the task, routes it to your worker, and the worker spawns a Docker container to execute the agent. You'll see the run appear in the [Oz dashboard](https://oz.warp.dev) with status moving from `QUEUED` → `INPROGRESS` → `SUCCEEDED`.

### 4. Verify the run

Open the [Oz dashboard](https://oz.warp.dev), find the new task, and confirm the session transcript shows the agent running against your worker. You can attach to the session at any time via [Agent Session Sharing](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/session-sharing) to monitor or steer it.

## Next steps

- [Unmanaged quickstart](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged#unmanaged-quickstart) — ~5-minute CLI-only path: run `oz agent run` in your CI, Kubernetes pod, or dev box with no worker daemon and no Docker requirement.
- [Managed: Docker](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-docker) — Full Docker backend setup, including private registries, volume mounts, and runtime configuration.
- [Environments](https://docs.warp.dev/agent-platform/cloud-agents/environments) — Define a repository, Docker image, and setup commands so agents have a reproducible workspace for every run.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Worker won't start** | Verify Docker is running (`docker info`) and that the daemon platform is `linux/amd64` or `linux/arm64`. Musl-based (Alpine) worker hosts are not supported. |
| **Worker won't connect** | Verify your API key has team scope. Ensure the machine has outbound internet access to `oz.warp.dev:443`. Increase log verbosity with `--log-level debug` to see connection details. |
| **Task stays queued** | Confirm the `--host` value you passed to `oz agent run-cloud` matches your `--worker-id` exactly (case-sensitive). Check that the worker's team matches the team creating the task. |

For more, see [Troubleshooting](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/troubleshooting).