---
title: Architecture and deployment | Enterprise | Warp
url: https://docs.warp.dev/enterprise/enterprise-features/architecture-and-deployment
source: sitemap
fetched_at: 2026-04-29T15:06:07.621182294-03:00
rendered_js: false
word_count: 998
summary: This document outlines the system architecture of Warp's cloud agent infrastructure, detailing the differences between SaaS, self-hosted, and hybrid deployment models for managing agent execution, security, and data flow.
tags:
    - system-architecture
    - deployment-models
    - agent-orchestration
    - enterprise-security
    - cloud-infrastructure
    - data-privacy
    - saas
category: concept
optimized: true
optimized_at: 2026-04-29T15:04:00Z
---
Warp's architecture separates the **control plane** (orchestration, observability, and LLM inference) from the **execution plane** (where agents run, code is accessed, and commands execute). This separation gives enterprise teams flexibility to choose where sensitive workloads run while maintaining centralized management and visibility.

## System architecture overview

Warp's cloud agent infrastructure has four key components:

| Component | Description |
|-----------|-------------|
| **Trigger** | What starts an agent run: CI step, webhook, cron schedule, Slack mention, CLI command, or API/SDK call |
| **Orchestration** | What decides what to run and tracks it: Oz orchestrator or your own system |
| **Execution** | Where the agent actually runs: Warp-hosted environment, your infrastructure, or your existing CI/orchestrator |
| **Visibility** | How the team monitors and intervenes: Oz dashboard, session sharing, APIs/SDKs |

### High-level data flow

```
Warp terminal (client) ↔ Warp backend (control plane) ↔ LLM providers
```

- The Warp backend handles task orchestration, observability, and LLM inference routing.
- LLM providers operate under **Zero Data Retention (ZDR)** agreements. They do not store or train on your data.
- The **execution plane** is where source code is accessed, commands run, and build artifacts are produced—either on Warp's infrastructure or yours.

## Warp-hosted (SaaS)

Warp-hosted is the default deployment model. Oz agents run on Warp-managed infrastructure with no setup required.

### How it works

- Agents execute in **isolated Docker containers** on Warp-hosted infrastructure (GCP).
- The Oz orchestrator manages agent lifecycle: provisioning, execution, monitoring, and cleanup.
- Environments are ephemeral and destroyed after each run.

### Triggers

- **First-party integrations** — Slack, Linear, and other connected tools
- **Scheduled agents** — Cron-like automation for recurring work
- **CLI** — `oz agent run-cloud` for on-demand cloud execution
- **API/SDK** — Programmatic triggers from your own systems

### When to use

- You want the simplest path to scalable cloud agent execution.
- You need to run many tasks in parallel without building sandboxing infrastructure.
- Your security requirements are met by Warp's SOC 2 Type II certified infrastructure with ZDR.

## Self-hosted execution

> [!info]
> Self-hosted execution is available exclusively on Warp's **Enterprise** plan.

For organizations that need agent execution and source code to remain within their own network boundary, Warp supports self-hosted execution.

### Split architecture

Self-hosted deployments use a split architecture:

- **Execution plane (customer-hosted)** — Source code repositories, build artifacts, shell commands, and runtime secrets stay on your infrastructure. Note that during agent interactions, code context is included in LLM prompts and session transcripts that route through Warp's servers under ZDR agreements.
- **Control plane (Warp-hosted)** — Task orchestration, observability data, and LLM inference route through Warp's servers under Zero Data Retention (ZDR) agreements.

### Deployment modes

| Mode | Description | Best for |
|------|-------------|----------|
| **Unmanaged** | Use `oz agent run` to run agents in your existing orchestrator or CI environment. Supports Linux, macOS, and Windows with no Docker dependency. | Teams with existing CI/CD infrastructure or internal orchestrators. You control scheduling, scaling, and environment setup. Warp provides cloud connectivity, shared context, visibility, and session sharing. |
| **Managed** | Run the `oz-agent-worker` daemon to let the Oz platform orchestrate agents in isolated Docker containers on your infrastructure. | Teams wanting Oz orchestration and visibility without sending code to Warp's infrastructure. The worker process connects to Oz via WebSocket and receives tasks automatically. |

### Network requirements

Self-hosted agents require **outbound-only** network access. No inbound network access is required.

**Egress requirements:**

- Outbound access to Warp's backend services (for orchestration and observability)
- For managed mode: access to Docker Hub and GitHub (for container images and repository access)

### When to use

- Compliance or security requirements prevent using Warp-hosted compute.
- Source code and execution must stay within your network boundary.
- You want Oz orchestration and visibility without sending code to Warp's infrastructure.

## Hybrid deployments

Organizations can combine Warp-hosted and self-hosted execution to balance convenience with security requirements.

**How it works:**

- Route sensitive workloads (e.g., production code, regulated data) to self-hosted agents.
- Route less sensitive workloads (e.g., open-source tooling, internal utilities) to Warp-hosted agents.
- Both execution modes share the same Oz dashboard, session sharing, and API/SDK visibility.

### Example configurations

- **By sensitivity** — Production repositories run on self-hosted agents; staging and development run on Warp-hosted.
- **By team** — Security-sensitive teams (e.g., infrastructure, payments) use self-hosted; other teams use Warp-hosted.
- **By task type** — Scheduled maintenance tasks run on Warp-hosted; ad-hoc debugging runs self-hosted in dev environments.

## Data flow and boundaries

### What stays on customer infrastructure (self-hosted)

- **Source code** — Repository contents and version history
- **Build artifacts** — Compiled outputs and generated files
- **Shell commands** — Terminal commands and their output
- **Runtime secrets** — Environment variables and credentials
- **Execution logs** — Agent run logs and diagnostics

### What transits Warp's servers

- **Task orchestration** — Scheduling, routing, and lifecycle management
- **Observability data** — Run status, duration, and metadata
- **LLM inference** — Prompts and responses (which include code context from agent interactions) routed through Warp to contracted LLM providers under ZDR agreements
- **Session sharing data** — Session transcripts, which include code context from agent interactions, when session sharing is enabled for monitoring and collaboration

## Choosing a deployment model

| Model | Choose when... |
|-------|----------------|
| **Warp-hosted** | You want zero infrastructure management. Your security team is comfortable with SOC 2 Type II certified, ZDR-covered infrastructure. You need maximum parallelization and scalability. |
| **Self-hosted** | Compliance requirements mandate that code stays within your network. You need to integrate with existing CI/CD or infrastructure tooling. You want full control over the execution environment. |
| **Hybrid** | Different teams or repositories have different security requirements. You want the convenience of Warp-hosted for most work but need self-hosted for sensitive workloads. |

## Related resources

- [Security overview](https://docs.warp.dev/enterprise/security-and-compliance/security-overview) — Data handling, encryption, and compliance details
- [Bring Your Own LLM](https://docs.warp.dev/enterprise/enterprise-features/bring-your-own-llm) — Route inference through your own cloud infrastructure
- [Admin Panel](https://docs.warp.dev/enterprise/team-management/admin-panel) — Configure agent policies and security settings