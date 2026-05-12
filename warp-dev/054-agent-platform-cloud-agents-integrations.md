---
title: Integrations | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/integrations
source: sitemap
fetched_at: 2026-04-29T15:04:24.909712529-03:00
rendered_js: false
word_count: 264
summary: This document provides a guide for setting up and configuring Warp agents to automate workflows within Slack and Linear by creating remote environments.
tags:
    - warp-agents
    - workflow-automation
    - slack-integration
    - linear-integration
    - dev-environments
    - remote-execution
    - oz-cli
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp integrations trigger agents from the terminal, [Slack](https://docs.warp.dev/agent-platform/cloud-agents/integrations/slack), or [Linear](https://docs.warp.dev/agent-platform/cloud-agents/integrations/linear). Agents can:

- Read conversation or issue context
- Run code inside your codebase in a remote environment
- Open pull requests and perform multi-step workflows on your behalf

All powered by the [Oz CLI](https://docs.warp.dev/reference/cli).

## Quickstart

### 1. Run /create-environment

Run the slash command from any repo, or point it at multiple repos:

```
/create-environment
/create-environment --repo https://github.com/org/repo --repo /path/to/local
```

> [!info]
> See [[043-agent-platform-warp-agents-capabilities-overview-slash-commands]] for more on slash commands.

The guided flow:
- Detects repos to work with
- Identifies languages, frameworks, and tools
- Suggests a Docker image (your own, an official base like `node`/`python`, or one of Warp's [prebuilt dev images](https://github.com/warpdotdev/oz-dev-environments))
- Recommends setup commands
- Creates the environment and returns an environment ID

Warp prompts you to install the Warp GitHub app so the agent can read/write to your repos. Install once; teammates authorize on first run.

> [!info]
> Using **Azure DevOps, GitLab, or Bitbucket?** Native integrations aren't available yet. Store a personal access token as a Warp-managed secret and clone via a setup command. See [Azure DevOps](https://docs.warp.dev/agent-platform/cloud-agents/integrations/azure-devops), [GitLab](https://docs.warp.dev/agent-platform/cloud-agents/integrations/gitlab), or [Bitbucket](https://docs.warp.dev/agent-platform/cloud-agents/integrations/bitbucket).

### 2. Create an integration

**Via slash command:**

```
/create-integration slack
/create-integration linear
```

**Via CLI:**

```bash
oz integrations create slack
oz integrations create linear
```

The CLI opens an authorization page to install Oz into your workspace or team.

### 3. Start using agents

**In Slack** — Tag **@Oz** in a message, thread, or DM.

**In Linear** — Tag @Oz on an issue.

Warp reads the thread/issue, spins up your environment, runs the workflow in the cloud, and posts progress + PRs back into the conversation.

> [!tip]
> See [Integration setup](https://docs.warp.dev/reference/cli/integration-setup) for detailed configuration.

#warp-agents #workflow-automation #slack-integration #linear-integration
