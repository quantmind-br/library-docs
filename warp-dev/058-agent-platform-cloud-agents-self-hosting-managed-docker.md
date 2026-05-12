---
title: 'Managed: Docker | Agents | Warp'
url: https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-docker
source: sitemap
fetched_at: 2026-04-29T15:04:46.810217827-03:00
rendered_js: false
word_count: 770
summary: This document provides instructions for setting up and configuring the oz-agent-worker using the Docker backend, including prerequisites, installation methods, and runtime configuration.
tags:
    - docker
    - agent-worker
    - self-hosting
    - infrastructure
    - configuration
    - task-orchestration
category: guide
optimized: true
optimized_at: 2026-04-29T15:04:46.810217827-03:00
---
Run the `oz-agent-worker` daemon with the **Docker backend** — the default managed path. Each agent task runs in an isolated Docker container spawned from the worker, with full orchestration by Oz (Slack, Linear, schedules, API, `oz agent run-cloud`).

## When to use the Docker backend

- You want the simplest managed setup with Docker available
- You want per-task isolation without running a Kubernetes cluster
- You're not already deploying workloads into Kubernetes

## Prerequisites

- **Enterprise plan with self-hosting enabled** — [Contact sales](https://warp.dev/contact-sales)
- **A machine to run the worker** — VM, server, or local machine running Linux (recommended for production). macOS and Windows with Docker Desktop work for testing
- **Docker installed** — Worker uses Docker to spawn task containers. The daemon must run Linux containers (Windows containers not supported)
- **A team API key** — In the Warp app, go to **Settings** > **Cloud platform** > **Oz Cloud API Keys**. See [API Keys](https://docs.warp.dev/reference/cli/api-keys)

> [!warning]
> Task containers require a **linux/amd64** or **linux/arm64** Docker daemon. The worker host itself can be any OS — Docker Desktop on macOS and Windows runs a Linux VM that satisfies this requirement.

### Install Docker

Follow the [official Docker installation guide](https://docs.docker.com/get-docker/) for your platform. Verify Docker is running:

```bash
docker info
```

**Expected outcome:** `docker info` prints daemon details without errors.

## Set your API key

```bash
export WARP_API_KEY="your-api-key"
```

## Install and run the worker

The `oz-agent-worker` is open source. See the [oz-agent-worker repository](https://github.com/warpdotdev/oz-agent-worker) for source code and contribution guidelines.

Three ways to install and run the worker with the Docker backend:

### Option 1: Docker (recommended)

Mount the host's Docker socket into the worker container:

```bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e WARP_API_KEY="$WARP_API_KEY" \
  warpdotdev/oz-agent-worker \
  --worker-id "my-worker" \
  --backend docker
```

**Expected outcome:** The worker connects to Oz and logs that it's listening for tasks.

### Option 2: Go install

```bash
go install github.com/warpdotdev/oz-agent-worker/cmd/oz-agent-worker@latest
oz-agent-worker start \
  --worker-id "my-worker" \
  --backend docker \
  --api-key "$WARP_API_KEY"
```

### Option 3: Build from source

```bash
git clone https://github.com/warpdotdev/oz-agent-worker.git
cd oz-agent-worker
go build -o oz-agent-worker ./cmd/oz-agent-worker
./oz-agent-worker start \
  --worker-id "my-worker" \
  --backend docker \
  --api-key "$WARP_API_KEY"
```

Once started, the worker connects to Oz, waits for tasks routed to its `--worker-id`, runs each task in an isolated Docker container, and reports status and results back. The worker automatically reconnects if the connection drops.

Run multiple workers with the same `--worker-id` for redundancy — Oz distributes tasks across connected workers.

## Docker backend configuration

Configure via CLI flags or a YAML [config file](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/reference#config-file). CLI flags take precedence.

**Common CLI flags:**

| Flag | Description | Default |
|------|-------------|---------|
| `--worker-id` | Worker identifier | - |
| `--backend` | Backend type | `docker` |
| `--api-key` | Warp API key | - |
| `-e`, `--env` | Environment variables to pass to task containers | - |
| `--workspace-root` | Directory for task workspaces | `/var/lib/oz/workspaces` |
| `--cleanup` | Clean up workspaces after tasks | `true` |
| `--no-cleanup` | Keep workspaces for debugging | `false` |

> [!warning]
> When running the worker via Docker, there are two levels of `-e` flags:
> - Docker's `-e` passes env vars to the **worker container** (e.g., `WARP_API_KEY`)
> - The worker's `-e` / `--env` flags pass env vars into the **task containers** the worker spawns
>
> ```bash
> # Docker -e: passes WARP_API_KEY to the worker container
> # Worker -e: passes MY_SECRET to task containers
> docker run \
>   -e WARP_API_KEY="$WARP_API_KEY" \
>   warpdotdev/oz-agent-worker \
>   --worker-id "my-worker" \
>   -e MY_SECRET=hunter2
> ```

**Equivalent config file** (`config.yaml`):

```yaml
worker_id: "my-worker"
api_key: "${WARP_API_KEY}"
backend: docker
workspace_root: "/var/lib/oz/workspaces"
environment:
  DATABASE_URL: "postgres://..."
  API_SECRET: "${API_SECRET}"
```

Pass it with `--config-file config.yaml`. See the [self-hosted worker reference](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/reference) for the full flag and config schema.

## Docker connectivity

The worker uses standard Docker client discovery:

1. `DOCKER_HOST` environment variable (e.g., `unix:///var/run/docker.sock`, `tcp://localhost:2375`)
2. **Default socket** (`/var/run/docker.sock` on Linux, `~/.docker/run/docker.sock` for rootless Docker)
3. **Docker context** via `DOCKER_CONTEXT` environment variable
4. **Config file** (`~/.docker/config.json`) for context settings

Additional environment variables:
- `DOCKER_API_VERSION` — Specify Docker API version
- `DOCKER_CERT_PATH` — Path to TLS certificates
- `DOCKER_TLS_VERIFY` — Enable TLS verification

> [!info]
> If the worker itself runs in Docker, mount any relevant config files (e.g., `~/.docker/config.json`) into the worker container for Docker context and credential discovery.

**Example: Connecting to a remote Docker daemon**

```bash
export DOCKER_HOST="tcp://remote-docker-host:2375"
docker run \
  -v ~/.docker/config.json:/root/.docker/config.json:ro \
  -e WARP_API_KEY="$WARP_API_KEY" \
  warpdotdev/oz-agent-worker \
  --worker-id "my-worker" \
  --backend docker
```

## Private Docker registries

The worker automatically uses credentials from your Docker config (`~/.docker/config.json`) when pulling task images. For [environments](https://docs.warp.dev/agent-platform/cloud-agents/environments) using images from a private registry, authenticate the worker's host first:

```bash
docker login ghcr.io  # or your private registry
```

When running the worker via Docker, mount the Docker config into the container:

```bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ~/.docker/config.json:/root/.docker/config.json:ro \
  -e WARP_API_KEY="$WARP_API_KEY" \
  warpdotdev/oz-agent-worker \
  --worker-id "my-worker" \
  --backend docker
```

> [!info]
> Sidecar images (the `oz` binary and dependencies) are pulled from public registries and do not require authentication.

## Routing runs to this worker

Once your Docker worker is connected, route tasks to it with `--host "<your-worker-id>"`. See [[209-agent-platform-cloud-agents-self-hosting#routing-runs-to-self-hosted-workers|Routing runs to self-hosted workers]] for CLI, scheduled, integration, API, and web UI examples.

## Related pages

- [[205-agent-platform-cloud-agents-environments|Environments]] — Define the Docker image, repos, and setup commands for tasks

Last updated 21 hours ago