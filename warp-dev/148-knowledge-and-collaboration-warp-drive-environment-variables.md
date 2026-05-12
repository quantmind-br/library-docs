---
title: Environment variables | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/environment-variables
source: sitemap
fetched_at: 2026-04-29T15:03:36.103922042-03:00
rendered_js: false
word_count: 489
summary: This document explains how to create, manage, and use static and dynamic environment variables within the Warp terminal to securely handle configuration and secret retrieval.
tags:
    - warp-terminal
    - environment-variables
    - secret-management
    - terminal-configuration
    - dynamic-secrets
    - workflow-automation
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## What Are Environment Variables in Warp?

Environment variables in Warp are similar to .env files, but with additional capabilities:

- Load into terminal sessions with a click.
- Use in parameterized workflows.
- Dynamically reference secrets from external managers.

## Create and Edit Environment Variables

Create via:
- [Command Palette](https://docs.warp.dev/terminal/command-palette) — create team or personal environment variables.

This opens the environment variables editor where you name and describe variables.

## Static Variables

Static variables are similar to .env files. Enter raw string values — each has a name and a corresponding value.

Click to load into your terminal session. Warp stores them securely in Warp Drive.

> [!warning]
> Static variables should not replace a secret manager. Use dynamic variables for sensitive information.

## Dynamic Variables

> [!info]
> Warp never stores secrets used in dynamic variables. Warp only stores the command used to retrieve secrets at runtime.

Dynamic variables reference secrets stored outside Warp in external secret managers (e.g., 1Password, LastPass). Use custom commands to integrate any system with a public API or CLI (AWS, Hashicorp Vault, etc.).

### Create a Dynamic Variable

1. Open the environment variable editor.
2. Click the key icon → select an integrated password manager or "Command" for custom integration.

### Integrated Password Managers

Ensure the CLI is installed for your tool of choice and enabled per the tool's instructions. Then click the key icon and select your manager from the dropdown.

> [!info]
> Selecting a secret name never stores the actual secret. Warp generates a command that dynamically pulls the secret at runtime.

### Custom Secret Command

Write a custom command referencing your secret manager's documentation.

> [!info]
> Your command should return the exact string to load. Ensure you select the exact field — many CLIs add extra formatting by default.

Example using [Hashicorp Vault CLI](https://developer.hashicorp.com/vault/docs/commands) to retrieve a staging server password:

```bash
vault kv get -field=password secret/staging
```

Warp stores the command but never the secrets. Secrets are loaded at runtime.

## Load Environment Variables into a Session

Three ways to invoke and load environment variables:

### 1. Click to Load into Current Session

1. Click the environment variable from Warp Drive or the Command Palette.
2. Review the confirmation block.
3. Press `Enter` to load.

Variables persist for the remainder of the session.

### 2. Click to Load into a Subshell

Open [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive), locate the environment variable, and use the overflow menu → **Load in subshell**.

Loading into a subshell isolates variables. When you exit, Warp clears them — unless already present in the parent session.

### 3. Select to Load with a Workflow

When running a workflow, select from existing environment variables to dynamically inject them into a parameterized workflow.

Example: a workflow that creates a new team uses `$SERVER_URL`. Select the appropriate environment variable to run the same workflow across environments (production, staging) with the right values.

## Import and Export

See [[144-knowledge-and-collaboration-warp-drive#import-and-export|Warp Drive Import and Export]].

#environment-variables #warp-terminal #secret-management #dynamic-secrets
