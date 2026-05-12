---
title: Cloud agent FAQs | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/faqs
source: sitemap
fetched_at: 2026-04-29T15:04:53.218224843-03:00
rendered_js: false
word_count: 1304
summary: This document provides a comprehensive overview of Warp's cloud agents, covering their architecture, execution environment, security, and configuration options.
tags:
    - cloud-agents
    - automation
    - orchestration
    - security
    - workflow-automation
    - agent-architecture
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Common questions about cloud agents: where they run, how they're configured, and how teams use them for engineering work.

## Architecture and execution

### Where do cloud agents run?

Agents run **locally** (inside your Warp session) or **in the cloud** inside an **environment** (see [Environments](https://docs.warp.dev/agent-platform/cloud-agents/environments)).

The platform is built around modular, observable execution:
- **Trigger** starts work (manual, cron, webhook, or integration like Slack/GitHub)
- **Agent** executes inside an **environment** (Warp-hosted cloud sandbox or self-hosted)
- Every step is recorded: **transcripts, tool calls, logs, outputs**

The same agent can be invoked consistently across entry points (terminal, web app, CLI, API/SDK, Slack/GitHub triggers).

### What exactly are cloud agents in Warp?

A **cloud agent** is a packaged automation unit:

- **Instructions** – reusable skill/prompt
- **Profile** – model selection + tools + permissions
- **Trigger** – manual, cron, webhook, or integration event
- **Environment** – repo access, dependencies, secrets, setup commands, runtime config
- **Host** – local (interactive) or cloud (run), optionally self-hosted

### Can we intervene mid-run?

Yes. For cloud agent runs, you can:
- Inspect **run state**, tool calls, logs
- **Steer** the agent while running
- Unblock with additional instructions or context
- Take over to finish if not satisfied

### Do cloud agents have access to Codebase Context?

Yes. [Codebase Context](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/codebase-context) is enabled for all Oz cloud agent runs if Codebase Context is enabled for your account. No additional configuration needed.

### Can I access a shell inside a cloud agent environment?

Yes. Cloud agent runs execute in a full Linux environment. You can install dependencies, run Docker, use headless tools like Playwright, subject to sandbox resource limits.

### Do cloud agents support self-hosted, on-prem, or offline mode?

The platform supports self-hosting the **agent sandbox** (execution environment) on your own infrastructure. The **control plane** (orchestration, tracking, auditability) remains Warp-managed.

Self-hosted execution is available on **Enterprise** plans. See [Self-Hosting](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting).

## Models

### Which models are supported?

Cloud agents are **multi-model by design**. Choose models based on cost, latency, and capability:
- Faster/cheaper models for triage and routine tasks
- Stronger models for complex changes (refactors, multi-file work)

### Can I choose which model cloud agents use?

Yes. Same set of models as Warp. Configurable per agent or environment.

### Can I authenticate with my own ChatGPT or Claude Pro/Max plan?

Actively working with providers to explore direct third-party authentication.

### Do you support local or private LLMs?

Enterprise plans will support managed integrations like AWS Bedrock and Google Vertex. Fully local LLM execution is difficult given current architecture, but private-model support via enterprise cloud providers is on the roadmap.

### Will cloud agents support Agent-to-Agent Protocols (A2A)?

Actively exploring. Focus is on durable orchestration primitives—runs, environments, observability, steering, coordination—that can support A2A and other standards.

## Security and billing

### Is cloud storage secure and encrypted?

Yes. All cloud agent data is encrypted at rest and in transit, protected by Warp account-level access controls. Cloud agent environments are sandboxed by default with scoped access to repos, secrets, and compute.

### Are cloud agents included in the Build plan?

Cloud agents are included in the Build plan. Usage is metered via credits based on agent runs and resource consumption.

### How do cloud agents handle API keys and secrets?

Secrets are managed via the cloud agents CLI, encrypted at rest, scoped to your Warp account, and injected at runtime. Never hard-coded into instructions or logs.

→ [Cloud Agent Secrets](https://docs.warp.dev/agent-platform/cloud-agents/secrets)

## Workflows

### How do agents handle branching, merge conflicts, and multi-agent coordination?

The platform is intentionally flexible. You decide how agents should branch, coordinate, and resolve conflicts. Cloud agents provide building blocks rather than enforcing fixed workflows.

### Why focus on orchestration primitives?

Durable infrastructure matters more than transient standards. The platform provides stable building blocks—agent runs, environments, auditability, steering, coordination—that orchestration frameworks can plug into.

### Can cloud agents integrate with external tools, APIs, or services?

Yes. Agents can install CLIs, call external APIs, use MCP servers, and access the internet directly. Flexibility is delegated to agents rather than constrained with fixed connectors.

### Can I export agent conversations and runs?

Yes. Conversations can be copied from the UI. The CLI and API provide programmatic access to full conversation text, logs, and outputs.

### How do cloud agents handle environment access compared to SSH?

Access is handled through Warp session sharing rather than SSH keys. Authentication is tied to Warp accounts and access controls. Configuration files can use encrypted .env workflows.

### Can cloud agents review PRs like a teammate?

Yes. Common patterns:
- Summarize changes and intent
- Flag risky diffs and edge cases
- Suggest tests and missing coverage
- Propose refactors for maintainability

Agent leaves structured review comments and optionally opens a follow-up PR.

### Can cloud agents write unit tests?

Yes, especially when:
- Repo has consistent test framework
- **Environment** is reproducible (dependencies and setup reliable)

### Can cloud agents do big refactors?

Scope into smaller, reviewable chunks. Agents are strongest when they can continuously validate progress (tests, lint, typecheck). Large refactors benefit from staged approach with checkpoints.

### Can cloud agents triage issues/tickets automatically?

Yes. Common workflow:
- Gather context on ticket creation (recent changes, logs/metrics, ownership)
- Propose labels/priority and likely causes
- Draft next steps or response
- Ask clarifying questions back to reporter

### Can cloud agents do dependency upgrades?

Yes. Scheduled dependency bumps are a classic use case:
- Open a PR
- Run tests
- Resolve simple conflicts
- Attach risk summary (optional)

Implemented as a scheduled **cloud agent** producing recurring **runs**.

### Can cloud agents keep docs up to date?

Yes. Agents can:
- Scan for drift (commands that no longer work, onboarding steps that changed)
- Run validations in docs/test environment
- Propose doc updates as PRs

## Self-hosting

### Where does my source code go with self-hosted agents?

With self-hosting, repositories are cloned and stored only on your infrastructure—Warp never hosts your codebase.

- **Execution plane (your infrastructure)**: repo clones, build artifacts, runtime secrets, container filesystem
- **Control plane (Warp-hosted)**: session transcripts, orchestration metadata, LLM inference under [ZDR](https://docs.warp.dev/enterprise/security-and-compliance/security-overview#zero-data-retention-zdr) agreements

Warp does not persistently store source code or use it for model training.

### Can I use `oz agent run` in CI or existing runners?

Yes. The [unmanaged architecture](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged) runs `oz agent run` in any environment—GitHub Actions, Jenkins, Buildkite, Kubernetes pods, custom orchestrators. The [`warpdotdev/oz-agent-action`](https://github.com/warpdotdev/oz-agent-action) GitHub Action uses this approach.

### Can self-hosted agents access services behind a VPN?

Yes. Since agents run on your infrastructure, they inherit your network access—self-hosted GitLab/Bitbucket, internal APIs, databases, any internal resources.

### Does self-hosting work with GitLab or other non-GitHub SCMs?

Yes. With [unmanaged architecture](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged), agents use whatever Git and SCM access is already available on the host. With [managed architecture](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting#managed-architecture), configure access via volume mounts, environment variables, setup commands, or Kubernetes Secrets. See [GitLab](https://docs.warp.dev/agent-platform/cloud-agents/integrations/gitlab) and [Bitbucket](https://docs.warp.dev/agent-platform/cloud-agents/integrations/bitbucket) setup guides.

### Do LLM requests still go through Warp with self-hosting?

Yes. LLM inference routes through Warp's backend under [ZDR](https://docs.warp.dev/enterprise/security-and-compliance/security-overview#zero-data-retention-zdr) agreements. Enterprise teams can use [BYOLLM](https://docs.warp.dev/enterprise/enterprise-features/bring-your-own-llm) to route inference through their own cloud provider accounts (currently for local agents; cloud agent support coming).

### What about large monorepos with long setup times?

[Unmanaged architecture](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged) is well-suited—agents run directly in your pre-provisioned environment. For managed architecture:
- Docker backend: use volume mounts (`-v`) to mount pre-existing repo checkout
- Kubernetes backend: configure persistent volume claims via `pod_template`

> [!info]
> The managed architecture supports three execution backends: **Docker** (default), **Kubernetes**, and **Direct**. See [Self-Hosting](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting#choosing-a-managed-backend).

### Do Kubernetes pods provide enough sandboxing?

Depends on your cluster configuration. Evaluate pod security policies, network policies, and RBAC settings.

## Current limitations

### Do cloud agents support image attachments?

Not currently. Image attachments (toolbar, clipboard, drag-and-drop) are only available in [local agent conversations](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents/terminal-and-agent-modes).

Provide visual context by describing image contents or referencing image file paths within the agent's [environment](https://docs.warp.dev/agent-platform/cloud-agents/environments).
