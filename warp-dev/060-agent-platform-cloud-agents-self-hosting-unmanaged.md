---
title: Unmanaged | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged
source: sitemap
fetched_at: 2026-04-29T15:04:44.96173908-03:00
rendered_js: false
word_count: 611
summary: This document explains the unmanaged architecture for Warp agents, providing instructions on how to manually orchestrate agent runs using the CLI within existing CI/CD pipelines, VMs, or Kubernetes environments.
tags:
    - agent-orchestration
    - cli-automation
    - unmanaged-architecture
    - ci-cd-integration
    - kubernetes-deployment
category: guide
optimized: true
optimized_at: 2026-04-29T15:04:44.96173908-03:00
---
With the **unmanaged architecture**, **you orchestrate agent runs** by invoking `oz agent run` directly from your existing CI pipelines, Kubernetes pods, VMs, or dev boxes. The agent runs on whatever host the command is executed from; Warp tracks the session but does not start or stop agents.

> [!info]
> Use unmanaged if you already have a system that schedules work (CI, internal orchestrators, cron, dev environments). If you'd rather have Oz trigger and route runs from Slack, Linear, schedules, or the API, use the [[209-agent-platform-cloud-agents-self-hosting#managed-architecture|managed architecture]] instead.

## When to use unmanaged

| Use case | Description |
|----------|-------------|
| **Kubernetes pods** | Run agents inside pods with access to your cluster's network and services |
| **Dev boxes and VMs** | Run agents in pre-provisioned development environments, especially useful for large monorepos with long setup times |
| **Existing orchestrators** | Drop `oz agent run` into any system that schedules work (Jenkins, Buildkite, internal job schedulers) |

Unmanaged works on any platform Warp supports (Linux, macOS, Windows) with no dependency on Docker or any other sandboxing platform.

## Unmanaged quickstart

*~5 minutes*

No Docker, no worker daemon, no environment required — just the Oz CLI on any host that can reach the internet.

### Prerequisites

- **The Oz CLI** installed on the machine where agents will run. See [Installing the CLI](https://docs.warp.dev/reference/cli#installing-the-cli)
- **A Warp API key** — For automation, create a team-scoped API key in the Warp app at **Settings** > **Cloud platform** > **Oz Cloud API Keys**. See [API Keys](https://docs.warp.dev/reference/cli/api-keys)

### 1. Authenticate

```bash
export WARP_API_KEY="your-api-key"
```

### 2. Run an agent

```bash
oz agent run
```

Invoke `oz agent run` in the directory where you want the agent to operate. The agent has access to whatever tools, network resources, and credentials the host provides.

**Expected outcome:** The agent starts immediately in the current working directory, and a tracked session appears in the [Oz dashboard](https://oz.warp.dev).

### 3. Control sharing

Use `--share` to control who can attach to the session and steer the agent:

| Flag | Access level |
|------|--------------|
| `--share` | Share with yourself (accessible on other devices or in a browser) |
| `--share team` or `--share team:view` | All team members read-only access |
| `--share team:edit` | All team members read/write access |
| `--share user@example.com` | Specific user read-only access |
| `--share user@example.com:edit` | Specific user read/write access |

The `--share` flag can be repeated to combine multiple sharing targets. If you authenticate with a team API key, agents are automatically team-scoped.

## Example: GitHub Actions

Warp maintains the [`warpdotdev/oz-agent-action`](https://github.com/warpdotdev/oz-agent-action) action for running agents in GitHub Actions:

```yaml
- uses: warpdotdev/oz-agent-action@v1
  with:
    api-key: ${{ secrets.WARP_API_KEY }}
    share: team:edit
```

See [[050-agent-platform-cloud-agents-integrations-github-actions|GitHub Actions integration]] for full details.

## Example: Kubernetes

Run an agent inside a Kubernetes pod with access to your cluster's services:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: oz-agent
spec:
  containers:
    - name: agent
      image: warpdotdev/warp-agent:latest
      env:
        - name: WARP_API_KEY
          valueFrom:
            secretKeyRef:
              name: warp-api-key
              key: WARP_API_KEY
      command: ["oz", "agent", "run"]
```

> [!warning]
> For production deployments, pin to a specific Docker image digest (e.g., `warpdotdev/warp-agent@sha256:...`) instead of `latest` to ensure reproducible builds.

> [!info]
> Whether Kubernetes pods provide sufficient sandboxing for agents depends on your cluster configuration and risk profile. Evaluate your pod security policies, network policies, and RBAC settings based on your organization's security requirements.

## Tracking and observability

Unmanaged agents are tracked on Warp's backend. Each run creates a persistent session that your team can:
- View full transcripts and artifacts in the [Oz dashboard](https://oz.warp.dev)
- Share sessions with teammates for collaboration
- Access via the Oz CLI and REST API

Unmanaged sessions benefit from the same shared configuration as other cloud agent runs — [MCP servers](https://docs.warp.dev/agent-platform/cloud-agents/mcp), [secrets](https://docs.warp.dev/agent-platform/cloud-agents/secrets), Warp Drive context, and saved prompts all apply.

## Related pages

- [[209-agent-platform-cloud-agents-self-hosting|Self-hosting overview]] — Compare managed and unmanaged, architecture decision guide
- [[045-agent-platform-cloud-agents-deployment-patterns|Deployment patterns]] — Pattern 1 (CLI-only) explains the unmanaged model conceptually

Last updated 21 hours ago