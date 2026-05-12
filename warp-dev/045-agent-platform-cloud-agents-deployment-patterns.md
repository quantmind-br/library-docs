---
title: Deployment patterns | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/deployment-patterns
source: sitemap
fetched_at: 2026-04-29T15:04:41.987560798-03:00
rendered_js: false
word_count: 720
summary: This document outlines the three primary architectures for deploying Oz cloud agents, ranging from CLI-based execution to managed cloud hosting and self-hosted environments.
tags:
    - cloud-agents
    - agent-orchestration
    - architecture-patterns
    - enterprise-security
    - automation-workflow
    - cli-integration
    - deployment-strategies
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Teams adopt cloud agents in repeatable patterns. This page outlines the most common architectures.

## Quick mental model

Oz cloud agent setups have four moving parts:

1. **Trigger** — something happens (CI step, webhook, cron, Slack mention)
2. **Orchestration** — decides what to run and tracks it (Oz, GitHub Actions, internal system)
3. **Execution** — where the agent runs (runner, Oz-hosted, self-hosted workers)
4. **Visibility** — how the team monitors and intervenes (Oz dashboard, session sharing, APIs)

---

## Pattern 1: CLI-only agents (bring your own orchestrator)

Use when you already have a system scheduling work and need a reliable, cloud-connected agent runner.

### What it looks like

| Component | Implementation |
|-----------|----------------|
| Trigger | GitHub Actions/CI, script, dev box action, internal orchestrator |
| Orchestration | Your existing system |
| Execution | Wherever that system runs |
| Warp adds | Cloud connectivity, shared context, visibility, session sharing, tracking |

### Why teams choose it

- Drop-in replacement for CLI/SDK-based agents (Claude Code, Codex CLI, Gemini CLI)
- Run agents anywhere without Warp desktop
- Team-level observability even when execution is "outside Warp"

### Common examples

- **CI PR helper:** run formatting checks, generate review comments, open PRs
- **Remote dev box agent:** run refactors or debugging tasks in pre-provisioned boxes
- **Internal orchestrator integration:** treat Warp as one agent option alongside other providers

### What you still get

- Access to shared Warp context (MCP config, Warp Drive context, rules/prompts)
- Agent Session Sharing to monitor/steer runs
- Read-only APIs for tracking and reporting
- Path to "handoff" workflows (continue or inspect runs in richer surfaces)

### Minimal setup checklist

- A Warp team
- A service account (recommended for automation)
- The Oz CLI installed on the runner/box
- Any needed credentials (via secrets + environment variables)

---

## Pattern 2: Oz-hosted agents + Oz orchestration (managed cloud execution)

Use when you want Oz to run agent workloads on Warp-managed infrastructure in reproducible Docker environments.

### Why teams choose it

- Simplest path to reproducible, scalable cloud execution
- Run many tasks in parallel without building your own sandboxing/scaling layer
- Consistent "production" setup with standardized environments and centralized configuration

### Common ways to trigger

- **First-party integrations** (Slack, Linear) that create tasks from external events
- **Scheduled agents** for recurring work (cron-like automation)
- **Custom triggers** via Warp's API/SDK
- **On-demand cloud jobs** using `oz agent run-cloud`

### Example: Daily dead-code cleanup

1. Define an Oz Environment with the repo + toolchain
2. Create a schedule with a fixed prompt for cleanup
3. Oz runs the agent on the cadence
4. Monitor runs in the Oz dashboard, review artifacts (PRs, plans)

### Example: Crash triage via Sentry webhook

1. Define an Oz Environment with the target repo
2. Register a Sentry webhook to your handler (server, cloud function, Zapier/n8n)
3. Handler extracts crash details, constructs a prompt, calls Oz orchestrator API/SDK
4. Warp spins up the run; monitor progress via UI/API

### Example: Fan-out parallel work (sharding)

Launch multiple cloud agents via `oz agent run-cloud`, each with:
- A shard of the repo (directory/module ownership)
- A shard of the prompt (one responsibility)

Aggregate results (PRs, notes, plans) in whatever system you prefer.

### Example: Same task across multiple models

Launch N runs with the same prompt but different profiles mapping to different models. Compare results and choose best output.

---

## Pattern 3: Self-hosted execution

Use when you need to control where agent execution happens while using Oz orchestration and visibility. Repositories are cloned and stored only on your infrastructure.

> [!warning]
> **Enterprise feature:** Self-hosted execution is available exclusively to Enterprise plan teams.

### Architectures

- **[[210-agent-platform-cloud-agents-self-hosting|Managed]]** — Oz orchestrates. You run the `oz-agent-worker` daemon; Oz routes runs to it. Tasks execute in Docker containers, Kubernetes Jobs, or directly on the host.
- **[[060-agent-platform-cloud-agents-self-hosting-unmanaged|Unmanaged]]** — You orchestrate. Invoke `oz agent run` from CI, Kubernetes, or dev environment. Warp provides session tracking and observability but does not start/stop agents.

### Why teams choose self-hosted

- Code and execution must stay within your network boundary
- Agents need to access services behind VPN or self-hosted SCMs (GitLab, Bitbucket)
- Environments (multi-service stacks, heavy resource requirements) don't fit in a single Docker container

For setup, decision guides, and quickstart, start with [[210-agent-platform-cloud-agents-self-hosting|Self-hosting]]. #cloud-agents #deployment-strategies