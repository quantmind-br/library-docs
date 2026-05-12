---
title: Quick start | Enterprise | Warp
url: https://docs.warp.dev/enterprise/getting-started/quickstart
source: sitemap
fetched_at: 2026-04-29T15:05:59.721649881-03:00
rendered_js: false
word_count: 428
summary: This document provides a foundational walkthrough for setting up the Warp terminal, enabling SSO, and utilizing Oz agents for local and cloud-based code development.
tags:
    - warp-terminal
    - oz-agents
    - getting-started
    - cloud-automation
    - sso-authentication
    - codebase-indexing
category: tutorial
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
This quickstart walks through the essentials: logging in via SSO, setting up Warp, and running your first Oz agent. Complete in under 10 minutes.

When you use agents in Warp, you're using **Oz agents**. Oz is Warp's programmable agent for running and coordinating agents at scale, locally or in the cloud.

## Step 1: Log in via SSO

1. Click **Continue with SSO**.
2. Enter your work email or organization's domain.
3. Complete authentication with your identity provider.

If you have an existing Warp account, [link it to SSO first](https://app.warp.dev/link_sso).

## Step 2: Download and set up Warp

1. Install Warp:
   - **macOS**: Open `.dmg`, drag Warp to Applications
   - **Linux**: Install via `.deb`, `.rpm`, or install script
   - **Windows**: Run `.exe` installer
2. Launch Warp and log in with SSO.
3. Verify you see your team name in **Settings** > **Teams**.

## Step 3: Configure and run your first Oz agent

### Index your codebase

1. Navigate to a Git repository in Warp.
2. Warp automatically detects the repo and begins indexing.
3. Optionally run `/init` to manually trigger or re-index.
4. Once indexed, Oz agents understand your code structure, patterns, and conventions.

### Run your first Oz agent locally

Start an Oz conversation in the terminal. Try:

- "Explain how this codebase handles authentication"
- "What patterns does this repo use for error handling?"

Oz reads your codebase and responds with context-aware explanations.

### Try more prompts

| Task | Prompt |
|---|---|
| **Write code** | "Add input validation to the signup form" |
| **Debug** | "Why is this test failing?" (paste error output) |
| **Explore** | "What patterns does this repo use for error handling?" |
| **Plan** | Use `/plan` to have Oz create a structured task plan |

## Step 4: Run an Oz cloud agent

Oz cloud agents run in the cloud for background work, unlimited parallelization, and long-running tasks.

### Create an environment

Environments define the execution context for cloud agents (repo access, dependencies, secrets, compute).

**Option 1: Slash command in Warp**
Run `oz env create` in the terminal input. This launches an interactive flow for environment setup.

**Option 2: Oz web app**
Go to [app.warp.dev/environments](https://app.warp.dev/environments) and click **Create Environment**.

### Run a cloud agent

Once your environment is ready:
```bash
oz run --env <environment-id>
```

Monitor and steer Oz cloud agents from the Oz dashboard or directly in Warp.

## Next steps

- **Set up key features** — Follow the full [[010-enterprise-getting-started-getting-started-developers|Getting started for developers]] guide
- **Explore Oz cloud agents** — Learn about [[194-agent-platform-cloud-agents-overview|Oz cloud agents]] for background automation and parallel workflows