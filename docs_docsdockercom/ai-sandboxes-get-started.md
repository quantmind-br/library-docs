---
title: Get started
url: https://docs.docker.com/ai/sandboxes/get-started/
source: llms
fetched_at: 2026-01-24T14:14:25.815215638-03:00
rendered_js: false
word_count: 290
summary: This guide provides instructions for setting up and running Claude Code within a Docker Sandbox environment, covering prerequisites and basic management commands.
tags:
    - docker-desktop
    - claude-code
    - sandboxing
    - containerization
    - cli-commands
category: guide
---

## Get started with Docker Sandboxes

Table of contents

* * *

Availability: Experimental

Requires: Docker Desktop [4.50](https://docs.docker.com/desktop/release-notes/#4500) or later

This guide will help you run Claude Code in a sandboxed environment for the first time.

## [Prerequisites](#prerequisites)

Before you begin, ensure you have:

- Docker Desktop 4.50 or later
- A Claude Code subscription

## [Run a sandboxed agent](#run-a-sandboxed-agent)

Follow these steps to run Claude Code in a sandboxed environment:

1. Navigate to Your Project
2. Start Claude in a sandbox
   
   ```
   $ docker sandbox run claude
   ```
3. Authenticate: on first run, Claude will prompt you to authenticate.
   
   Once you've authenticated, the credentials are stored in a persistent Docker volume and reused for future sessions.
4. Claude Code launches inside the container.

## [What just happened?](#what-just-happened)

When you ran `docker sandbox run claude`:

- Docker created a container from a template image
- Your current directory was mounted at the same path inside the container
- Your Git name and email were injected into the container
- Your API key was stored in a Docker volume (`docker-claude-sandbox-data`)
- Claude Code started with bypass permissions enabled

The container continues running in the background. Running `docker sandbox run claude` again in the same directory reuses the existing container, allowing the agent to maintain state (installed packages, temporary files) across sessions.

## [Basic commands](#basic-commands)

Here are a few essential commands to manage your sandboxes:

### [List your sandboxes](#list-your-sandboxes)

Shows all your sandboxes with their IDs, names, status, and creation time.

### [Remove a sandbox](#remove-a-sandbox)

```
$ docker sandbox rm <sandbox-id>
```

Deletes a sandbox when you're done with it. Get the sandbox ID from `docker sandbox ls`.

### [View sandbox details](#view-sandbox-details)

```
$ docker sandbox inspect <sandbox-id>
```

Shows detailed information about a specific sandbox in JSON format.

For a complete list of all commands and options, see the [CLI reference](https://docs.docker.com/reference/cli/docker/sandbox/).

## [Next Steps](#next-steps)

Now that you have Claude running in a sandboxed environment, learn more about:

- [Authentication strategies](https://docs.docker.com/ai/sandboxes/claude-code/#authentication)
- [Configuration options](https://docs.docker.com/ai/sandboxes/claude-code/#configuration)
- [Advanced configurations](https://docs.docker.com/ai/sandboxes/advanced-config/)
- [Troubleshooting guide](https://docs.docker.com/ai/sandboxes/troubleshooting/)