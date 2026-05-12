---
title: Self-hosting | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/self-hosting
source: sitemap
fetched_at: 2026-04-29T15:04:44.240372966-03:00
rendered_js: false
word_count: 779
summary: This document provides an overview of self-hosting options for Oz cloud agents, comparing managed and unmanaged architectures to help teams choose the appropriate deployment strategy for their infrastructure requirements.
tags:
    - self-hosting
    - cloud-agents
    - infrastructure-management
    - deployment-architecture
    - enterprise-security
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Self-hosting runs Oz cloud agent workloads on your own infrastructure instead of Warp-managed servers. You control the execution environment, compute resources, and network access. Repositories are cloned and stored only on your machines.

> [!info]
> **Enterprise feature**: Self-hosted Oz agents are available exclusively to teams on an Enterprise plan. [Contact sales](https://warp.dev/contact-sales) to enable.

## Managed vs unmanaged

Two architectures. Core distinction is **who orchestrates agent runs**—not who owns compute. Both keep code and execution on your infrastructure.

| Architecture | Description |
|--------------|-------------|
| **Managed** | Oz orchestrates runs. Run `oz-agent-worker` daemon on your infrastructure; it connects to Oz and executes tasks in Docker containers, Kubernetes Jobs, or directly on host. Similar to GitHub self-hosted runners. |
| **Unmanaged** | You orchestrate runs. Invoke `oz agent run` directly from CI pipeline, Kubernetes pod, VM, or dev box. Oz provides session tracking and observability but doesn't start/stop agents. |

Architectures are not mutually exclusive—some teams run managed workers for integration-triggered work and unmanaged agents in CI.

## How self-hosting works

Warp uses a split-plane architecture: **execution on your infrastructure**, **orchestration, session management, and LLM inference through Warp's backend** under [ZDR](https://docs.warp.dev/enterprise/security-and-compliance/security-overview#zero-data-retention-zdr) agreements.

With any self-hosted architecture:
- **Agent runs are tracked and steerable** – view status, transcripts in Oz dashboard, Warp app, or API/SDK
- **Connectivity to Warp's backend required** – agents need outbound access; no inbound ports
- **Resource limits controlled by your infrastructure** – concurrency limited by machines you provision

> [!info]
> Enterprise teams can use [BYOLLM](https://docs.warp.dev/enterprise/enterprise-features/bring-your-own-llm) for full LLM inference control (currently local agents; cloud agent support coming).

## Choosing an architecture

> [!warning]
> **OS support**: managed architecture is **Linux-only** today (macOS/Windows support coming). For macOS or Windows, use [unmanaged](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged).

| Question | Yes | No |
|----------|-----|-----|
| Do you need agents on Windows or macOS? | [Unmanaged](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged) | Continue |
| Do you want Oz to handle starting/stopping agents? | [Managed](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting#managed-architecture) | [Unmanaged](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged) |
| Can your environment run in Docker container or K8s pod? | Any | [Unmanaged](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged) or [Managed: Direct](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-direct) |
| Do you have your own orchestrator that starts agents? | [Unmanaged](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged) | - |

### Choosing a managed backend

Managed architecture supports three backends:

| Question | Answer | Backend |
|----------|--------|---------|
| Deploying into Kubernetes cluster? | Yes | [Kubernetes](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-kubernetes) (Helm chart) |
| Docker available on worker host? | Yes | [Docker](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-docker) (default) |
| Need container-level isolation? | No | Any backend works |
| Need Kubernetes-native scheduling/resource management? | Yes | [Kubernetes](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-kubernetes) |

## Managed architecture

Run `oz-agent-worker` daemon on your infrastructure. It connects to Oz's backend, waits for tasks, executes using:

- [**Docker backend**](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-docker) (default) – isolated Docker containers
- [**Direct backend**](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-direct) – direct on-host execution without container runtime
- [**Kubernetes backend**](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-kubernetes) – Kubernetes Jobs with Helm chart

Managed enables full orchestration by Oz—remotely start agents via Slack, Linear, [Oz web app](https://oz.warp.dev), API/SDK, `oz agent run-cloud`.

## Unmanaged architecture

Run `oz agent run` inside your own orchestrator or dev environment. Works on any platform Warp supports (Linux, macOS, Windows), no Docker dependency. Similar to Claude Code or Codex CLI integration.

## Routing runs to self-hosted workers

Applies to **all managed backends**. Route runs by specifying `--host` with your worker ID (must match `--worker-id` exactly).

> [!info]
> Unmanaged runs don't need routing—invoke `oz agent run` directly on the host. Routing only relevant for managed workers.

### From the CLI

```bash
oz agent run-cloud --host <WORKER_ID> [other flags]
```

Combine with `--environment`, `--model`, `--mcp`, `--skill`, `--computer-use`, `--attach`.

### From scheduled agents

```bash
oz schedule create --name <NAME> --trigger <CRON> --host <WORKER_ID> [other flags]
```

### From integrations

```bash
oz integration create --name <NAME> --type <TYPE> --host <WORKER_ID> [other flags]
```

### From API and SDKs

Include `worker_host` in config when creating run via [Oz API](https://docs.warp.dev/reference/api-and-sdk/agent).

### From web UI

Select self-hosted worker from host dropdown in [Oz web app](https://oz.warp.dev).

## Environments with self-hosted workers

Self-hosted workers fully support [environments](https://docs.warp.dev/agent-platform/cloud-agents/environments). Worker resolves Docker image, clones repos, runs setup commands, executes agent inside container or Kubernetes Job.

The same environment works for both Warp-hosted and self-hosted runs without modification.

> [!info]
> With Kubernetes backend, setting [`default_image`](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/reference#kubernetes-backend-config) on worker lets you skip creating a Warp environment when all tasks use the same base image.

> [!warning]
> Musl-based Docker images (Alpine Linux) are not supported. Use glibc-based images (Debian, Ubuntu, non-Alpine variants).

## Monitoring runs

Self-hosted runs have same observability as Warp-hosted runs:
- **Session sharing** – authorized teammates can attach to running tasks
- **APIs/SDKs** – query task history and build monitoring via [Oz API](https://docs.warp.dev/reference/api-and-sdk/agent)

## Related pages

- [Unmanaged](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged) – run `oz agent run` in CI, K8s, or dev environment
- [Managed: Docker](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-docker) – default managed setup
- [Managed: Kubernetes](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-kubernetes) – K8s backend with Helm chart
- [Troubleshooting](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/troubleshooting) – common issues
- [Deployment patterns](https://docs.warp.dev/agent-platform/cloud-agents/deployment-patterns) – deployment comparison
- [Environments](https://docs.warp.dev/agent-platform/cloud-agents/environments) – runtime context for agent tasks

Last updated 21 hours ago
