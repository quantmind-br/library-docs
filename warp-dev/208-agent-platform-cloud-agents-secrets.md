---
title: Secrets | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/secrets
source: sitemap
fetched_at: 2026-04-29T15:04:40.145793273-03:00
rendered_js: false
word_count: 765
summary: This document explains how to securely manage and inject credentials into cloud agent runs using Warp-managed secrets, which are scoped to either teams or individuals. It covers the lifecycle of secrets, including creation, scoping, trigger availability, and security auditing.
tags:
    - secret-management
    - cloud-agents
    - security
    - credential-injection
    - cli-tools
    - environment-variables
    - access-control
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp-managed **agent secrets** securely store, scope, and inject credentials into cloud agent runs without exposing secret values to users or logs.

**Warp-managed secrets are useful when:**
- An cloud agent needs to call an API or CLI that does not support OAuth
- Using [MCP servers](https://docs.warp.dev/agent-platform/cloud-agents/mcp) that expect static tokens or keys
- Agent needs credentials for cloud CLIs, databases, monitoring systems, internal services
- You want centralized auditing and control over credentials

## Common use cases

- Run SQL queries against BigQuery or Metabase using read-only service account/API token
- Call cloud or infrastructure CLIs for predefined remediation steps (restart service, scale deployment, clear stuck job)
- List and review all API keys, service accounts, tokens that cloud agents can access to verify scopes and rotation policies

## How Warp-managed secrets work

Warp provides CLI commands for creating, updating, and listing secrets. Secret values are stored securely and **cannot be retrieved once created**.

At runtime, **Warp sets secrets as environment variables** for each cloud agent run, based on who triggered the agent and how.

> [!info]
> Secret values are available only to the agent process (and subprocesses) during execution. **Cannot be viewed or retrieved afterward.**

### Key properties

- **Scoped** to either a team or an individual user
- Values are **never readable after creation** (only metadata visible)
- **Automatically set** for cloud agent runs when in scope

## Secret scopes

### Team secrets

Shared across the entire team, available to all cloud agents running on behalf of the team.

| Characteristic | Description |
|----------------|-------------|
| **Injection** | Always injected regardless of trigger (CLI, Slack, Linear, scheduled) |
| **User context** | Available with or without specific user context |
| **Ideal for** | Shared infrastructure, service accounts, read-only API keys |

> [!info]
> Because team secrets may be used by fully automated or scheduled agents, create them **using bot or service accounts** rather than credentials tied to an individual.

**Examples:**
- Use a Metabase service account or read-only API token (not personal API key)
- Use cloud provider service accounts with minimal required permissions
- Use integration-specific tokens created for automation

This ensures credentials remain valid as team membership changes, permissions are tightly scoped, and rotation aligns with internal policies.

### Personal secrets

Belong to an **individual user**.

- Only available to cloud agents triggered by that user
- Not accessible to teammates or user-less triggers
- Useful for personal API keys or credentials tied to an individual account

## Managing agent secrets with the Oz CLI

Secrets are managed using the `oz secret` command family.

### Create a team secret interactively

```bash
oz secret create --team
```

### Create a personal secret from a file

```bash
oz secret create --personal --name <NAME> --value-from <FILE>
```

Useful for long values (JSON blobs, private keys).

### Adding descriptions

```bash
oz secret create --team --name <NAME> --description "<DESCRIPTION>"
```

Descriptions help with auditing and rotation tracking. Visible in listings but never expose secret values.

### Updating a secret

**Update value interactively:**
```bash
oz secret update --team --name <NAME>
```

**Update from file (recommended for rotation):**
```bash
oz secret update --team --name <NAME> --value-from <FILE>
```

**Update description:**
```bash
oz secret update --team --name <NAME> --description "<DESCRIPTION>"
```

### Deleting a secret

```bash
oz secret delete --team --name <NAME>
```

Add `--force` to skip confirmation. Use `--personal` instead of `--team` for personal secrets.

> [!warning]
> Deleting a secret is permanent. Any cloud agent runs depending on the deleted secret will no longer receive it as an environment variable.

### Listing secrets

```bash
oz secret list
```

Example output shows secrets by name, scope, and description. **Secret values are never displayed.**

## How secrets are made available

When a cloud agent starts, Warp determines which secrets are in scope and sets them as environment variables using the secret name as the variable name.

Example: secret named `GITHUB_TOKEN` becomes environment variable `GITHUB_TOKEN` in the agent's execution environment.

## Secret availability by trigger type

### User-initiated triggers

When triggered by a specific user (CLI, Slack mentions, Linear updates), the agent receives:
- All team-level secrets
- The triggering user's personal secrets

Does **not** receive personal secrets belonging to other team members.

### Unattended triggers

When triggered without user context (scheduled runs, API calls without user identity), the agent receives:
- Team-level secrets only

> [!warning]
> Personal secrets are never injected in unattended triggers.

## Auditing and security considerations

- Secret values cannot be read or exported after creation
- All secrets are explicitly scoped to a team or user
- Engineering and security leads can list all secrets available to them
- Rotation is handled by updating secrets in place
- Cloud agents only receive secrets that are in scope for the trigger

**Teams remain responsible for:**
- Choosing appropriate scopes for each secret
- Limiting permissions on external systems (e.g., read-only API keys)
- Rotating credentials according to internal policies
- Managing which agents and triggers exist within their environment
