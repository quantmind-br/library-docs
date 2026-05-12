---
title: Access, billing, and identity | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity
source: sitemap
fetched_at: 2026-04-29T15:04:52.262970088-03:00
rendered_js: false
word_count: 781
summary: This document explains the differences between individual and team-based cloud agent access, covering billing requirements, integration features, identity mapping, and GitHub authentication configuration.
tags:
    - cloud-agents
    - team-collaboration
    - billing-and-credits
    - identity-mapping
    - github-integration
    - api-keys
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Cloud agents work for individual users and teams, with teams unlocking integrations, self-hosting, and shared configuration.

## Individual vs team access

| Capability | Individual users | Teams |
|---|---|---|
| Run cloud agents via CLI/API | ✓ | ✓ |
| Integrations (Slack, Linear) | ✗ | ✓ |
| Self-hosted agents | ✗ | ✓ (Enterprise only) |
| Team-level config (environments, secrets) | ✗ | ✓ |
| Required plan | Any | Build, Max, or Business with ≥20 credits |

## Individual access

- Run agents using `oz agent run-cloud` or the Oz API
- Credits drawn from normal Warp credits, Cloud Agent Credits, or Build plan credits
- Agents execute on Warp-hosted infrastructure
- Integrations, self-hosting, and team secrets require a team

## Team access

A [Warp team](https://docs.warp.dev/knowledge-and-collaboration/teams) enables:

- **Integrations** — Slack and Linear integrations shared by all team members
- **Shared configuration** — Team-level environments, secrets, and settings
- **Self-hosting** — Run agents on own infrastructure (Enterprise only)
- **Team visibility** — Shared observability into agent runs and history

### Requirements for integrations

- Team needs at least **20 credits** (any type) to run integrations and cloud agents
- Credit precedence for integration-triggered runs: Cloud Agent Credits → user base credits → team Reload Credits → user Reload Credits

## Identity mapping

Warp maps user identity across Slack, Linear, and GitHub:

| Platform | Method |
|---|---|
| Slack | Account-linking flow (recommended) |
| Linear | Email matching — Linear email must match Warp account |
| GitHub | Each teammate must authorize individually |

Agents always operate using the GitHub permissions of the triggering user.

## Team GitHub authorization

Team GitHub authorization uses the **Oz by Warp** GitHub App instead of personal tokens. Ideal for fully automated workflows (CI/CD, scheduled agents, SDK-triggered runs) where code changes should be attributed to the GitHub App rather than an individual.

### Setup

1. **Install the GitHub App.** A user with admin permissions on the GitHub organization installs [Oz by Warp](https://github.com/apps/oz-by-warp). Grant access to **all repositories** or **selected repositories**.
2. **Enable the GitHub org.** A Warp team admin opens **Settings** → **Admin Panel** → **Platform** and adds the GitHub organization under **Enabled GitHub Orgs**.
3. **Use a team API key.** Tasks initiated with a team API key use GitHub App tokens.

> [!note]
> Each GitHub App installation is scoped to a single GitHub organization or personal account. For multi-org workflows, use user-triggered runs with personal API keys.

### Environments and enabled orgs

An [environment](https://docs.warp.dev/agent-platform/cloud-agents/environments) defines the Docker image, repos, and setup commands — it does not carry its own GitHub permissions. The environment repo list and **Enabled GitHub Orgs** serve different purposes:

- **Environment repo list** — "This agent needs repos A, B, and C."
- **Enabled GitHub Orgs** — "This team can use the GitHub App to access repos in this org."

### Personal tokens vs GitHub App tokens

| Run type | Authentication | Attribution |
|---|---|---|
| User-triggered (personal API key, Slack, Linear, Warp app) | Personal token | Triggering user |
| Team API key with GitHub App authorization | GitHub App token | GitHub App (not individual) |

Both flows can coexist on the same team.

## Data and permissions

### Slack / Linear

When a run is triggered, Warp receives the content of the tagged thread or issue and surrounding context used to build the agent prompt. Only content required for the task is stored.

### GitHub

Control is defined by two layers:

1. **Warp GitHub App installation scope** — determines which repos Warp can read/write to
2. **Triggering user's permissions** — agents inherit the user's read/write privileges and cannot elevate permissions

Agents can only operate on repositories that are included in the environment configuration AND accessible to both the GitHub app and triggering user.

## Credit usage

### User-triggered runs

- Tied to the triggering user's identity
- Credits consumed in order: credit grants for cloud agents → user base credits → team Reload Credits → user Reload Credits

### Team API key runs

- Not tied to any individual user
- Only team Reload Credit pool is used
- Ideal for CI/CD pipelines and scheduled tasks
- For workflows requiring code changes, configure team GitHub authorization or use a personal API key

> [!info]
> For workflows triggering via Slack or Linear, credit precedence starts with credit grants allocated for cloud agent usage, even for integrations.

## Who configures triggers

All triggers and instructions are defined and controlled by your team's authorized users. Admins decide which triggers exist, when they fire, and what the agent should do. Credits used are billed to the team's Reload Credit balance.
