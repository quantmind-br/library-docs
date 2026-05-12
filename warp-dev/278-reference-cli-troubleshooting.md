---
title: CLI Troubleshooting | Reference | Warp
url: https://docs.warp.dev/reference/cli/troubleshooting
source: sitemap
fetched_at: 2026-04-29T15:05:03.011748379-03:00
rendered_js: false
word_count: 758
summary: This document provides troubleshooting steps and management procedures for the Warp CLI, covering environment configurations, integration settings, GitHub access permissions, and Docker image compatibility.
tags:
    - cli-troubleshooting
    - environment-management
    - docker-configuration
    - github-integration
    - error-resolution
    - warp-agents
category: guide
optimized: true
optimized_at: 2026-04-29T19:05:00Z
---
# CLI Troubleshooting

Troubleshooting steps and management procedures for the Warp CLI.

## Getting help

The CLI includes built-in documentation for all commands:

```bash
oz help
oz <command> --help
```

## Common errors

**Command not found / CLI not installed correctly** — Verify your installation path and confirm the CLI version.

**Authentication issues**

- Interactive login: ensure you've completed the browser-based flow with `oz login`
- API keys: confirm the key is valid, not expired, and exported correctly

**Agent or MCP errors** — Ensure your agent profile and [[072-agent-platform-warp-agents-agent-context-mcp|MCP servers]] are configured properly, with correct permissions. See [[159-reference-cli-mcp-servers|MCP Servers]] and [[156-reference-cli-agent-profiles|Agent profiles]] for details.

## Environments

### How do I see what environment my integration is using?

List your integrations:

```bash
oz integration list
```

This shows each integration, its ID, and the environment it's linked to.

### How do I see what's inside that environment?

Once you know the environment ID:

```bash
oz environment get <environment_id>
```

This prints the full configuration, including:

| Field | Description |
|-------|-------------|
| Environment ID | Used in other commands |
| Name | Display name |
| Docker image | Image used for agent runs |
| Associated repos | Repos available to the agent |

### How do I add or remove repos and setup commands?

Use `oz environment update`. You can modify environments incrementally without recreating them.

**Add a repo:**

```bash
oz environment update --repo "owner/repo"
```

**Remove a repo:**

```bash
oz environment update --remove-repo "owner/repo"
```

**Add a setup command:**

```bash
oz environment update --setup-command "apt-get update && apt-get install -y <package>"
```

**Remove a setup command (must match exactly):**

```bash
oz environment update --remove-setup-command "<exact-command>"
```

> [!note]
> - Warp may prompt you to adjust GitHub app permissions when adding repos.
> - Setup commands run in the order they are defined.

### How do I delete an environment?

```bash
oz environment delete <environment_id>
```

Add `--force` to skip confirmation checks for environments used by integrations.

> [!warning]
> Only delete an environment once you've confirmed no active integrations are relying on it. If an integration points to a deleted environment, requests from Slack/Linear will fail until you create a new integration with a valid environment.

## Integrations

### How do I figure out what environment my integration is using?

```bash
oz integration list
```

This shows each integration, its ID, and the environment it’s attached to.

### I created a new environment, but don't see it when running `oz integration create`

Check:

1. Environment exists and is healthy: `oz environment list`
2. You're on the correct Warp team. Make sure your local CLI is logged into the same team where the environment was created.
3. If both look correct, recreate it and confirm there were no errors during creation.

## GitHub & repo access issues

This happens when:

- You add a repo that Warp doesn't have access to yet, or
- You personally haven't granted the Warp GitHub app permissions for that repo.

Follow the GitHub popup flow to install/adjust the Warp GitHub app.

### The agent can't open PRs or push changes to my repo

Check the following:

1. **Repo is part of your environment** — Make sure the repo is listed in: `oz environment get <id>`
2. **Warp GitHub app has access to that repo** — In GitHub's settings, confirm the Warp app is installed and that the repo is selected.
3. **You have write access** — The agent inherits your GitHub permissions. If you only have read access, Warp can't open PRs or push branches on your behalf.

## Docker image & environment failures

### I see errors like "pull access denied" or "repository does not exist"

Check:

1. The Docker image name and tag are correct.
2. The image is public on Docker Hub.
3. You can pull it locally: `docker pull <image_name>`

If local docker pull fails, fix the image visibility/name first, then recreate or update the environment with a working image.

### The agent can't find tools or runtimes inside the environment

This usually means the Docker image is missing required dependencies. Fix by either:

- Updating the Dockerfile used to build the image, then pushing a new version to Docker Hub and updating the environment with the new image
- Adding additional setup commands: `oz environment update --setup-command "apt-get update && apt-get install -y <package>"`

### I see "VM failed before the agent could run. This is likely an issue with your Docker image"

> [!warning]
> This typically means your Docker image uses musl libc instead of glibc. Alpine Linux and other musl-based images are not compatible with the agent runtime.

Fix:

- Switch to a glibc-based image such as Debian, Ubuntu, or the default (non-Alpine) variants of official Docker Hub images (e.g. `node`, `python`, `rust`).
- If you're using an Alpine variant like `node:20-alpine`, replace it with the default tag (e.g. `node:20`).

#cli-troubleshooting #environments #docker #github
