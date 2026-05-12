---
title: Environments | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/environments
source: sitemap
fetched_at: 2026-04-29T15:04:35.787771223-03:00
rendered_js: false
word_count: 889
summary: This document explains the role of environments in the Warp agent platform, defining them as the execution context—including Docker images, repositories, and setup commands—that ensures consistency across automated tasks.
tags:
    - cloud-agents
    - execution-context
    - docker-configuration
    - automation-workflows
    - reproducibility
    - infrastructure-setup
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Environments ensure your [cloud agents](https://docs.warp.dev/agent-platform/cloud-agents/overview) run with the same toolchain and setup every time, regardless of where triggered.

> [!info]
> Environments are often unnecessary for interactive local runs where you're already in a working checkout.

## Key features

- **Consistent behavior across triggers** – Slack, Linear, CLI all behave identically
- **One configuration, many uses** – define Docker image once, reuse across triggers/hosts
- **Full visibility into runs** – inspect image, repos, commands used

## About environments

An environment defines *how* an agent runs (not *what* it does). Required for Oz Platform automation, not for interactive local usage.

An environment typically includes:

| Component | Description |
|-----------|-------------|
| **Docker image (required)** | Toolchain and runtime. Self-hosted Kubernetes workers can use `default_image` to skip environments. |
| **Repository/workspace** | One or more repos to clone and operate on |
| **Setup commands** | Prepare workspace (dependency install, builds, bootstrapping) |

> [!info]
> Configure **environment variables** in Dockerfile using `ENV` directives or pass when running the container. Use [Agent Secrets](https://docs.warp.dev/agent-platform/cloud-agents/secrets) for credentials—configured separately, injected at runtime.

What an environment is not:

- **Host** – determines where execution happens (Warp-hosted vs self-hosted)
- **Agent Profile** – controls behavior (permissions, model, defaults)
- **Rules** – determines agent responses/decisions
- **MCP Servers** – connect agents to external tools via MCP
- **Per-run context** – trigger-specific data attaches to tasks, not environments

## How environments fit into the Oz Platform

1. **Trigger** fires → creates a task
2. **Task** uses an environment to define execution context
3. **Host** runs the environment (Warp-hosted or self-hosted)
4. **Agent execution** runs the workflow
5. **Outputs** produced (PRs, messages, reports, transcripts)
6. **Container destroyed** → clean, isolated environment for next run

> [!info]
> **Local agent** runs (`oz agent run`) don't require an environment. Environments are required for **automated platform** runs.

### Hosts and environments

| Host option | Description |
|-------------|-------------|
| **Warp-hosted (default)** | Warp provides infrastructure |
| **Self-hosted** | You provide infrastructure (runners in your cloud/network) |
| Local (coming soon) | Run on local machine for sandbox testing |

The same environment runs on different hosts with identical behavior.

## Runtime process

1. **Trigger received** – captures message content and linked context
2. **Execution environment created** – spins up isolated container from Docker image
3. **Repositories cloned** – GitHub repos cloned into container
4. **Setup commands run** – dependencies, builds, etc.
5. **Agent workflow runs** – executes task using context, tools, permissions
6. **Results posted** – updates to trigger source (Slack, Linear, etc.)
7. **Container destroyed** – each run starts from clean, isolated environment

## When to use environments

Use an environment when runs need predictable toolchain and repeatable setup:

- Integrations and schedules (Slack, Linear, GitHub Actions, etc.)
- CI and remote automation (different runners, varying base images)
- Team standardization (same image, repos, setup steps)
- Toolchain-specific workflows (specific language versions, linters, build tools)

**Skip an environment when:** interactive local runs where you're already in a working checkout.

### Decision checklist

Choose an environment if:

- Runs must be consistent across triggers/hosts
- Toolchain must be fixed (known image, deterministic setup)
- Workflow is shared across a team

## Where to configure environments

Use guided setup or CLI. Use guided for onboarding, CLI for full control.

**Before you begin:**
- One or more GitHub repositories for the agent to clone
- **GitHub authorization** configured (user-triggered: each user authorizes; automated: [team GitHub authorization](https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity#team-github-authorization))

> [!warning]
> Musl-based Docker images (Alpine Linux) are not supported. The agent runtime requires glibc. Use glibc-based images (Debian, Ubuntu, or non-Alpine variants).

### Create an environment with guided setup

Use [`/create-environment`](warp://action/create_environment) — Warp inspects repos and recommends configuration automatically.

Warp will:
- Detect repos and identify languages/frameworks/tools
- Find existing Dockerfile or recommend base image
- Suggest setup commands based on scripts/package managers
- Create environment via CLI and return an environment ID

### Create an environment with the CLI

```bash
oz environment create [flags]
```

| Flag | Description |
|------|-------------|
| `--name`, `-n` | Human-readable label |
| `--docker-image`, `-d` | Image name on Docker Hub |
| `--repo`, `-r` | Repo to clone (repeatable) |
| `--setup-command`, `-c` | Commands to run (repeatable) |
| `--description` | Optional description (max 240 chars) |

## Managing environments

**List environments:**
```bash
oz environment list
```

**View configuration:**
```bash
oz environment get <ENV_ID>
```

**Update environment:**
```bash
oz environment update <ENV_ID> [flags]
```

| Flag | Description |
|------|-------------|
| `--remove-description` | Clear the description |
| `--force` | Skip confirmation for environments used by integrations |

**Delete environment:**
```bash
oz environment delete <ENV_ID> [--force]
```

## Best practices

- **Keep setup repeatable** – idempotent commands that work on fresh containers
- **Pin versions** – use Docker images pinning language runtimes; use lockfiles for dependencies
- **Define clear workspace** – state which repos are cloned and where setup commands run
- **Make prerequisites explicit** – encode build steps, code generation, system packages as setup

> [!info]
> If setup commands depend on secrets, configure them through Warp's [secrets mechanism](https://docs.warp.dev/agent-platform/cloud-agents/secrets)—don't hardcode tokens.

## Common issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Setup assumes previous state | Relies on caches, existing directories | Write idempotent commands |
| Missing credentials/secrets | Private repos, registries require auth | Configure secrets |
| Repo access issues | GitHub lacks permissions | Verify GitHub authorization |
| "VM failed before agent could run" | Alpine/musl image incompatibility | Switch to glibc-based image |

Last updated 21 hours ago
