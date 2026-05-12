---
title: Azure DevOps | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/integrations/azure-devops
source: sitemap
fetched_at: 2026-04-29T15:04:30.914248028-03:00
rendered_js: false
word_count: 406
summary: This document provides instructions on how to authenticate Oz cloud agents with Azure DevOps repositories using personal access tokens and managed secrets.
tags:
    - azure-devops
    - cloud-agents
    - repository-access
    - secret-management
    - integration-guide
    - workflow-automation
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Oz cloud agents work with any Git repository, including Azure DevOps. A native Azure DevOps integration is not yet available, but you can grant agents access using a personal access token and Warp-managed secrets.

> [!note]
> This approach works for both Azure DevOps Services (dev.azure.com) and Azure DevOps Server (self-hosted) instances.

## Prerequisites

- A repository hosted on Azure DevOps (cloud or self-hosted)

## Step 1: Generate a personal access token

1. Sign in to `dev.azure.com/{your-org}` (or `https://{server}/{collection}` for self-hosted)
2. Click the user settings icon (gear) > **Personal access tokens** > **+ New Token**
3. Enter a name (e.g. `warp-oz-agent`), set expiration, select organization
4. Under **Scopes**, select **Custom defined**, then **Code** > **Read**
5. Click **Create** and copy the token immediately

> [!note]
> **Code (Read)** is the minimum required scope to clone. For pushing commits or opening PRs, you need **Code (Read & Write)**.

## Step 2: Store the token as a Warp-managed secret

Warp injects managed secrets as environment variables at runtime and never exposes them in logs or configuration files. See [[208-agent-platform-cloud-agents-secrets|Secrets]] for full details.

```bash
oz secret create --name AZURE_DEVOPS_TOKEN --team
# When prompted, paste the token
```

> [!note]
> Use `--team` for shared tokens available to all teammates and automated triggers. Use `--personal` if each team member authenticates with their own token.

To update a secret:

```bash
oz secret update --name AZURE_DEVOPS_TOKEN --team
```

## Step 3: Create an environment with a clone setup command

Create an environment that clones the repository at the start of each agent run. Use a setup command instead of `--repo` (which is designed for GitHub).

```bash
oz environment create \
  --name 'azure-devops-env' \
  --setup-command 'git clone https://dev.azure.com/your-org/your-project/_git/your-repo.git . && npm ci' \
  --env AZURE_DEVOPS_TOKEN
```

> [!warning]
> Use single quotes around setup commands that reference secrets. Double quotes cause your shell to expand `$AZURE_DEVOPS_TOKEN` immediately rather than letting Warp inject it at runtime.

Replace:
- `your-org`, `your-project`, `your-repo` with your actual values
- For Azure DevOps Server, replace `dev.azure.com` with your server's hostname
- Add dependency install/build steps (e.g., `npm ci` or `pip install -r requirements.txt`)

> [!warning]
> Setup commands run on a fresh container for every agent run. Write them to be idempotent. See [[055-agent-platform-cloud-agents-environments|Environment design best practices]].

Note the environment ID returned.

## Step 4: Test your environment

Run a one-off agent to verify the environment works:

```bash
oz agent run-cloud --environment <ENV_ID> "Hello, can you list the files in this repository?"
```

## Next steps

Connect your environment to any Warp trigger:

- **[[053-agent-platform-cloud-agents-integrations-slack|Slack]]** — Tag **@Oz** in a message
- **[[052-agent-platform-cloud-agents-integrations-linear|Linear]]** — Tag **@Oz** on an issue
- **[[063-agent-platform-cloud-agents-triggers-scheduled-agents|Scheduled agents]]** — Run on recurring schedule

> [!info]
> Native support for opening Azure DevOps pull requests from agent-generated changes is planned. #azure-devops #cloud-agents