---
title: Bitbucket | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/integrations/bitbucket
source: sitemap
fetched_at: 2026-04-29T15:04:31.423432619-03:00
rendered_js: false
word_count: 501
summary: This document provides instructions for configuring Oz cloud agents to access and clone private Bitbucket repositories using secure access tokens and managed environment variables.
tags:
    - bitbucket
    - cloud-agents
    - access-tokens
    - repository-cloning
    - devops-automation
    - warp-agent
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Oz cloud agents work with any Git repository, including Bitbucket. Unlike GitHub, Bitbucket does not have a native Warp integration, but you can grant agents access using an access token and Warp-managed secrets.

Bitbucket Cloud and Bitbucket Data Center/Server use different token types:

| Platform | Token Type |
|----------|------------|
| Bitbucket Cloud | **API tokens** (via Atlassian Account) |
| Bitbucket Data Center/Server | **HTTP access tokens** (via Bitbucket profile) |

## Prerequisites

- A repository hosted on Bitbucket (Cloud or Data Center/Server)

---

## Bitbucket Cloud

### Step 1: Generate an API token

> [!note]
> Bitbucket Cloud API tokens are managed through your Atlassian Account at atlassian.com.

1. Click your avatar in Bitbucket > **Account settings**
2. On the Atlassian Account page, click **Security** tab
3. Click **Create and manage API tokens** > **Create API token with scopes**
4. Enter a name (e.g. `warp-oz-agent`) and choose expiration
5. Click **Next**, select **Bitbucket** as the app
6. Search for `repository` and select **read:repository:bitbucket** (View your repositories)
7. Click **Next** > **Create token**
8. Copy the token immediately — it is only shown once

> [!note]
> **read:repository:bitbucket** is the minimum required scope to clone. For pushing commits or opening PRs, you need **write:repository:bitbucket**.

### Step 2: Store the token as a Warp-managed secret

```bash
oz secret create --name BITBUCKET_API_TOKEN --team
# When prompted, paste the token
```

> [!note]
> Use `--team` for shared tokens. Use `--personal` if each team member authenticates with their own token.

To update:

```bash
oz secret update --name BITBUCKET_API_TOKEN --team
```

### Step 3: Create an environment with a clone setup command

```bash
oz environment create \
  --name 'bitbucket-env' \
  --setup-command 'git clone https://x-token-auth:$BITBUCKET_API_TOKEN@bitbucket.org/your-workspace/your-repo.git . && npm ci' \
  --env BITBUCKET_API_TOKEN
```

> [!warning]
> Use single quotes around setup commands referencing secrets. Double quotes cause your shell to expand `$BITBUCKET_API_TOKEN` immediately.

Replace:
- `your-workspace/your-repo.git` with your actual repository URL
- Add dependency install/build steps

> [!warning]
> Setup commands run on a fresh container for every agent run. Write them to be idempotent. See [[055-agent-platform-cloud-agents-environments|Environment design best practices]].

Note the environment ID returned.

---

## Bitbucket Data Center / Server

### Step 1: Generate an HTTP access token

1. Click your profile avatar > **Manage account**
2. In the left sidebar, click **HTTP access tokens** > **Create token**
3. Enter a name and choose expiration if required by your administrator
4. Under **Permissions**, choose **Read** for **Repository** permission
5. Click **Create token** and copy immediately

> [!note]
> **Repository read** is the minimum required to clone. For pushing commits, you need **Repository write**.

### Step 2: Store the token as a Warp-managed secret

```bash
oz secret create --name BITBUCKET_TOKEN --team
# When prompted, paste the token
```

### Step 3: Create an environment with a clone setup command

```bash
oz environment create \
  --name 'bitbucket-data-center-env' \
  --setup-command 'git clone https://x-token-auth:$BITBUCKET_TOKEN@your-server.com/scm/your-project/your-repo.git . && npm ci' \
  --env BITBUCKET_TOKEN
```

> [!warning]
> Use single quotes around setup commands referencing secrets. The `/scm/` path segment is standard for Bitbucket Data Center/Server.

Replace `your-server.com/scm/your-project/your-repo.git` with your actual repository URL.

Note the environment ID returned.

---

## Step 4: Test your environment

```bash
oz agent run-cloud --environment <ENV_ID> "Hello, can you list the files in this repository?"
```

## Next steps

Connect your environment to any Warp trigger:

- **[[053-agent-platform-cloud-agents-integrations-slack|Slack]]** — Tag **@Oz** in a message
- **[[052-agent-platform-cloud-agents-integrations-linear|Linear]]** — Tag **@Oz** on an issue
- **[[063-agent-platform-cloud-agents-triggers-scheduled-agents|Scheduled agents]]** — Run on recurring schedule

> [!info]
> Native support for opening Bitbucket pull requests from agent-generated changes is planned. #bitbucket #cloud-agents