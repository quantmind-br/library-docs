---
title: Linear | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/integrations/linear
source: sitemap
fetched_at: 2026-04-29T15:04:28.409910063-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-29T00:00:00Z
word_count: 823
summary: This document explains how to set up and use the Warp Linear integration to delegate development tasks to cloud-based agents directly from Linear issues.
tags:
    - linear-integration
    - warp-agents
    - development-automation
    - workflow-automation
    - github-integration
    - cloud-agents
category: guide
---
The Linear integration lets your team delegate development work directly to agents from inside Linear. When you tag @Oz on an issue or comment, an agent spins up in the cloud, clones the repos defined in your environment, and begins working through the task.

Agents keep you updated inside Linear, generate pull requests using your GitHub account, and provide a link to join a live remote session so you can watch or steer the workflow in real time.

## Using Oz inside Linear

Tagging @Oz on an issue or in a Linear comment starts an agent run. Oz clones the repositories defined in your environment, sets up your development environment using your Docker image and setup commands, and begins working through the task with full context from your codebase and the Linear issue.

Agents post updates as they progress, including a task list, elapsed time, and checkpoints, so you can follow along without leaving Linear. They also share a link to an interactive remote session using Warp's [[064-agent-platform-cloud-agents-viewing-cloud-agent-runs|cloud agent session sharing]]. Opening this link lets you view the live terminal output for the running agent in Warp or in the browser. From there, you can interrupt or guide the agent with additional instructions when needed.

Once the agent finishes, it will create a pull request on your behalf using your GitHub permissions and post a summary of its work and the PR link back into Linear.

You can start an agent in two ways:
- **Tag @Oz in a comment** and describe what you want done.
- **Assign the issue to Oz** as if it were a teammate.

### Joining the remote session

Selecting **Open in Warp** (or the web option) opens the active session where you'll see:

- The agent's full execution log
- The plan pane with the task list
- An input box to add clarifying instructions
- A real-time view identical to a local Warp task

Any instructions you give will interrupt the agent, feed the new context, and resume work.

When the task is complete:
- Warp commits the changes using your GitHub identity
- A pull request is created through the GitHub CLI
- The PR includes a clean title and description based on the Linear issue and the agent's work
- A summary and link to the PR appear in the Linear issue

Because PRs are created as *you*, this makes code review, auditing, and team collaboration straightforward.

* * *

## Requirements

- **Team membership** — The Linear integration requires you to be part of a [Warp team](https://docs.warp.dev/knowledge-and-collaboration/teams). Teams can be created on any plan, including Free.
- **Plan and credits** — Your team must be on a plan that supports integrations (Build, Max, or Business) and have at least 20 credits available (any type of Warp credits work). See [[062-agent-platform-cloud-agents-team-access-billing-and-identity|Access, Billing, and Identity]] for details.
- **Infrastructure** — By default, agents run on Warp-hosted infrastructure. Enterprise teams can [[210-agent-platform-cloud-agents-self-hosting|self-host agents]] on their own infrastructure.
- **Identity** — You must be logged into Warp with the same email as your Linear workspace.
- **GitHub authorization** — You must authorize the Warp GitHub app the first time you trigger an agent.
  - The repositories involved must be included in your environment and accessible to the Warp GitHub app.
  - You must have write access to the repo if you want Warp to create PRs on your behalf.

## How to configure the integration

Setup involves two steps powered by the [Oz CLI](https://docs.warp.dev/reference/cli). For more instructions, see [[054-agent-platform-cloud-agents-integrations|Integrations Overview]].

### 1. Create an environment

An environment defines everything the agent needs to run your code:

- A **Docker image** (public on Docker Hub)
- A set of **GitHub repos** the agent should clone
- Optional **setup commands** that run before the agent starts

You can create an environment via:
- The CLI
- The guided flow using `/create-environment` ([[043-agent-platform-warp-agents-capabilities-overview-slash-commands|Slash Commands]])

For full instructions, see our [[054-agent-platform-cloud-agents-integrations|Environment Setup]] docs.

### 2. Create the Linear integration

Once your environment exists, create the integration.

Alternatively, you can use the CLI:

The CLI will open a browser window prompting you to install the Oz app into your Linear workspace. After installation, the integration becomes available to all members of your Warp team.

## Uninstallation instructions

To remove the Oz integration from Linear:

1. Only a Linear team admin can manage app permissions.
2. In Linear, go to **Settings**.
3. Navigate to Agents under the Features section.
4. Select Oz from the list of installed agents.
5. Click **Revoke access** to remove the integration for your workspace.

After revoking access, Warp will no longer be able to read issues, receive triggers, or create updates in Linear. If you reinstall later, you'll need to authorize Warp again during setup.

## Troubleshooting

If something isn't working as expected—missing repos, PR failures, Linear not detecting Oz, or environment issues—see our [[054-agent-platform-cloud-agents-integrations#troubleshooting|Integrations Troubleshooting]] page for detailed guidance on GitHub permissions, environment configuration, and common setup problems.