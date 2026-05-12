---
title: Integration Setup | Reference | Warp
url: https://docs.warp.dev/reference/cli/integration-setup
source: sitemap
fetched_at: 2026-04-29T15:05:02.619547434-03:00
rendered_js: false
word_count: 735
summary: This document provides instructions on how to configure environments and GitHub access to enable Warp agents to be triggered by external tools like Slack and Linear.
tags:
    - warp-agents
    - integration-setup
    - environment-configuration
    - github-authorization
    - automation-tools
    - cloud-agents
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Set up the environment and integrations required to trigger agents from external tools (Slack, Linear).

> [!info]
> Complete this setup **once per Warp team**. After an integration exists, anyone on the team can use it (each user authorizes GitHub with their own account to write back to repos).

> [!note]
> Cloud agents can run individually via CLI without a team. Integrations (Slack, Linear) require team membership.

## How it works

Three components connect external tools to agents:

| Component | Role |
|---|---|
| **Triggers** | Provide context — a Slack @Oz tag, Linear issue, or comment |
| **Integrations** | Connect the trigger surface (Slack, Linear) to Warp and handle result posting |
| **Environments** | Define how and where agents run — Docker image, repos, setup commands |

## Step 1: Create an environment

Environments define how and where Warp runs your code. Create **one environment per codebase** and reuse it across integrations.

**Requirements:**
- GitHub repository (or repositories)
- Publicly-accessible Docker image (e.g., `node`, `python`, `rust`)

### Option 1: Guided setup (recommended)

Run `/create-environment` [slash command](https://docs.warp.dev/agent-platform/warp-agents/slash-commands) with optional repo paths. The guided flow:

1. Detects repos and identifies languages/frameworks/tools
2. Finds or recommends a Dockerfile/base image
3. Suggests setup commands based on scripts and package managers
4. Creates the environment via CLI and returns an environment ID

### Option 2: CLI directly

```bash
oz environment create \
  --name "<LABEL>" \
  --docker-image "<IMAGE>" \
  --repo "<REPO_URL>" \
  --setup-command "<CMD>" \
  --description "<DESC>"
```

| Flag | Description |
|---|---|
| `--name`, `-n` | Human-readable label |
| `--docker-image`, `-d` | Docker Hub image name |
| `--repo`, `-r` | GitHub repo URL (repeatable) |
| `--setup-command`, `-c` | Commands to run on startup (repeatable) |
| `--description` | Optional description (max 240 chars) |

Inspect environments: `oz environment list`
Delete: `oz environment delete <ID>` (add `--force` for environments used by integrations)

## Step 2: Authorize GitHub

Agents need GitHub access to clone repos, create branches/commits, and open pull requests.

**Public repos:** Read-only without authorization. Write and PRs require the Warp GitHub App.

**Private repos:** The Warp GitHub App must have access and the triggering user must have write permissions.

When creating an environment or integration, Warp prompts you to install/update the Warp GitHub App and grant repo access.

### Team-level authorization (CI/CD)

For automated workflows using a [team API key](https://docs.warp.dev/reference/cli/api-keys), configure team GitHub authorization so agents authenticate via the Oz by Warp GitHub App instead of a personal token.

A Warp team admin enables this in **Settings** → **Admin Panel** → **Platform** (see [Team GitHub authorization](https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity#team-github-authorization)).

> [!info]
> Personal API keys authenticate as you — changes are attributed to your account. Team API keys with team GitHub authorization use the GitHub App token instead.

## Step 3: Set up an integration

With at least one environment, create an integration:

```bash
oz integration create \
  --environment <ENV_ID> \
  --type <slack|linear>
```

Omitting `--environment` shows a list to choose from. The CLI then links the integration, opens a browser to install the Oz app in Slack/Linear, and returns an integration ID.

**Additional flags:**
| Flag | Description |
|---|---|
| `--prompt <TEXT>` | Custom instructions for all runs |
| `--mcp <SPEC>` | Attach MCP servers (inline JSON, file path, or UUID) |
| `--model <MODEL_ID>` | Override the default model |
| `--host <WORKER_ID>` | Run on a specific self-hosted worker |
| `--file`, `-f` | Load config from a YAML or JSON file |

**Update an integration:** `oz integration update <ID>`

| Flag | Description |
|---|---|
| `--environment <ID>` | Change the environment |
| `--remove-environment` | Remove the environment |
| `--prompt <TEXT>` | Update custom instructions |
| `--mcp <SPEC>` | Add an MCP server |
| `--remove-mcp <NAME>` | Remove an MCP server |
| `--model <MODEL_ID>` | Update the default model |
| `--host <WORKER_ID>` | Update the execution host |

## Runtime execution flow

When an agent is triggered from Slack or Linear:

1. Warp captures the trigger message content and linked context
2. Warp spins up a fresh container from the Docker image
3. GitHub repos are cloned into the container
4. Setup commands are executed
5. The agent executes the task
6. Results are posted back to Slack or Linear
7. The container is destroyed (clean, isolated environment per run)

## Next steps

- Add or adjust setup commands
- Switch to a custom Docker image
- Include additional repositories
- Add custom prompts for consistent agent behavior
- Create separate environments for different workflows or teams

#warp-agents #integration-setup #environment-configuration #github-authorization #automation-tools #cloud-agents
