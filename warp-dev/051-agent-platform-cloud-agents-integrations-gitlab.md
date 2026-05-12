---
title: GitLab | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/integrations/gitlab
source: sitemap
fetched_at: 2026-04-29T15:04:32.468057514-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-29T00:00:00Z
word_count: 633
summary: This document provides instructions on how to integrate GitLab repositories with Oz cloud agents by using personal access tokens and secure environment configurations.
tags:
    - gitlab
    - cloud-agents
    - authentication
    - repository-management
    - secrets-management
    - setup-guide
category: guide
---
Oz cloud agents work with any Git repository, including those hosted on GitLab. Unlike GitHub, GitLab does not have a native Warp integration, but you can grant agents access to your GitLab repositories using a personal access token and Warp-managed secrets.

> [!info]
> This approach works for both GitLab.com and self-hosted GitLab instances.

Once configured, your environment works with any Oz trigger—[[053-agent-platform-cloud-agents-integrations-slack|Slack]], [[052-agent-platform-cloud-agents-integrations-linear|Linear]], schedules, or the CLI.

## Prerequisites

- A repository hosted on GitLab (cloud or self-hosted)

## Step 1: Generate a personal access token

1. Sign in to GitLab.
2. Click your avatar in the top-right corner, then click **Edit profile**.
3. In the left sidebar, click **Access**, then click **Personal access tokens**.
4. Click **Add new token**.
5. Enter a descriptive name for the token (e.g. `warp-oz-agent`), and choose an expiration date that matches your team's rotation policy.
6. Under **Select scopes**, select **read_repository**.
7. Click **Generate token**.
8. Copy the token value immediately. GitLab will not show it again.

> [!info]
> **read_repository** is the minimum required scope to clone a repository. If a future workflow requires the agent to push commits or open merge requests, you will also need **write_repository**.

## Step 2: Store the token as a Warp-managed secret

Warp injects managed secrets as environment variables at runtime and never exposes them in logs or configuration files. See [[208-agent-platform-cloud-agents-secrets|Secrets]] for full details on scoping and managing secrets.

1. Run the following command:

<!--THE END-->

1. When prompted, paste the token.

The value is stored and encrypted, and cannot be retrieved after creation.

> [!info]
> Use `--team` to create a shared token available to all teammates and automated triggers (schedules, Slack, Linear). Use `--personal` if each team member should authenticate with their own GitLab token. Personal secrets work with all triggers and take precedence over a team secret of the same name when both exist.

If you need to update a secret value, run:

## Step 3: Create an environment with a clone setup command

Create an environment that uses your token to clone the repository at the start of each agent run. Because the `--repo` flag in `oz environment create` is designed for GitHub repositories, you clone your GitLab repo via a setup command instead.

1. Run the following command:

> [!warning]
> Use single quotes around setup commands that reference secrets. Double quotes cause your shell to expand `$GITLAB_TOKEN` immediately (to nothing), rather than letting Warp inject the secret at runtime inside the container.

1. Replace the following placeholders:
   - `gitlab.com/your-group/your-repo.git` with your actual repository URL
   - For a self-hosted GitLab instance, replace `gitlab.com` with your server's hostname.
   - The second `--setup-command` with any dependency install or build steps your project requires (e.g. `npm ci` or `pip install -r requirements.txt`).

> [!warning]
> Setup commands run on a fresh container for every agent run. Write them to be idempotent — commands that assume existing state (such as a partially cloned repo or a pre-built cache) can fail unpredictably. See [[205-agent-platform-cloud-agents-environments|Environment design and best practices]] for guidance.

1. Note the environment ID returned. You will need it in the next step.

## Step 4: Test your environment

Before connecting to integrations, verify the environment works by running a one-off agent.

1. Run the following command, replacing `<ENV_ID>` with the environment ID from Step 3:

## Next steps

With your environment configured, you can connect it to any Warp trigger:

- **Slack** — Tag **@Oz** in a message to start an agent run against your GitLab repo. See [[053-agent-platform-cloud-agents-integrations-slack|Slack]].
- **Linear** — Tag **@Oz** on an issue to kick off a workflow. See [[052-agent-platform-cloud-agents-integrations-linear|Linear]].
- **Scheduled agents** — Run agents on a recurring schedule. See [[063-agent-platform-cloud-agents-triggers-scheduled-agents|Scheduled Agents]].

> [!info]
> Native support for opening GitLab merge requests from agent-generated changes is planned as a future enhancement.