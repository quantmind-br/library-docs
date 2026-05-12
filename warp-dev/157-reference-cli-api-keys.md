---
title: API Keys | Reference | Warp
url: https://docs.warp.dev/reference/cli/api-keys
source: sitemap
fetched_at: 2026-04-29T15:04:58.632126027-03:00
rendered_js: false
word_count: 476
summary: This document explains how to create, manage, and use API keys for authenticating Oz CLI and cloud agents in automated environments.
tags:
    - api-keys
    - authentication
    - cloud-agents
    - security-best-practices
    - cli-configuration
    - automation
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
API keys let the Oz CLI and cloud agents authenticate without human interaction. Use for CI pipelines, headless servers, VMs, Codespaces, and containers.

## Create an API key

1. Click your profile photo → **Settings**
2. **Cloud platform** → **Oz Cloud API Keys**
3. Click **+ Create API Key**
4. Name the key and choose an expiration: 1 day, 30 days, 90 days, or never
5. Select the key type:
   - `Personal` — tied to your individual Warp account
   - `Team` — tied to your team, not any individual user

> [!info]
> When agents need to write to GitHub:
> - **Personal API key** → agent runs with your GitHub permissions, changes attributed to your account
> - **Team API key + team GitHub authorization** → agent authenticates with the Oz by Warp GitHub App, changes not attributed to any individual

> [!info]
> Team keys without GitHub App authorization are suitable for automated workflows that don't require writing to GitHub (analysis, monitoring, triage).

6. Click **Create key**
7. Copy the raw API key immediately — **it cannot be retrieved after closing the dialog**

## Personal vs team API keys

| Aspect | Personal | Team |
|---|---|---|
| **Identity** | Authenticated as you | Not tied to any individual |
| **Billing** | Uses your base credits first, then team Add-on Credits | Uses only team Add-on Credits |
| **GitHub write access** | With your permissions | Requires team GitHub authorization configured |

Team keys suit CI/CD pipelines and scheduled tasks where no specific user context is needed.

## Authenticate with API keys

**Environment variable (recommended):**
```bash
export WARP_API_KEY="wk-..."
```

**Command flag:**
```bash
oz agent run-cloud --api-key "wk-..." --prompt "..."
```

> [!info]
> API keys start with the prefix `wk-`. Missing this prefix may indicate an invalid or legacy key.

## Manage API keys

The **Oz Cloud API Keys** section in Settings lists all active keys with:

- **Name** — assigned at creation
- **Key** — masked suffix (`wk-**xxxx`) for identification
- **Scope** — Personal or Team
- **Created** / **Last used** — timestamps
- **Expires at** — date or "Never"

### Delete a key

1. Go to **Settings** → **Cloud platform** → **Oz Cloud API Keys**
2. Find the key and click the delete icon

Deleted keys are immediately invalidated and cannot be recovered.

## Best practices

- **Use environment variables** — avoid passing keys in commands where they may be logged
- **Set appropriate expiration** — shorter for dev/test, longer for stable production workflows
- **Use team keys for automation** — cleaner billing attribution, no dependency on individual accounts
- **Configure team GitHub authorization** — when agents need to write to GitHub (see [Team GitHub authorization](https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity#team-github-authorization))
- **Rotate periodically** — create new keys and retire old ones on a regular schedule
- **Store securely** — use secret managers (1Password CLI, HashiCorp Vault, or cloud provider secret services)

#api-keys #authentication #cloud-agents #security-best-practices #cli-configuration #automation
