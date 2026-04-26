---
title: API keys | Mistral Docs
url: https://docs.mistral.ai/admin/security-access/api-keys
source: sitemap
fetched_at: 2026-04-26T04:00:56.786779373-03:00
rendered_js: false
word_count: 235
summary: This document provides instructions on how to generate, manage, and securely store API keys for authenticating requests to the Mistral platform.
tags:
    - api-keys
    - authentication
    - security-best-practices
    - workspace-management
    - api-credentials
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# API Keys

API keys authenticate your requests to the Mistral API. Each key is scoped to a specific Workspace and grants access to all API endpoints available on your plan.

## Creating an API Key

1. Go to [Studio API keys](https://console.mistral.ai/api-keys).
2. Click **Create new key**.
3. Optionally set a **name** and **expiration date**.
4. Click **Create new key**.
5. Copy the key immediately.

> [!warning]
> **The full key is shown only once.** After you close the dialog, you can't retrieve it. Store the key securely in a password manager or secrets vault.

## Using Your API Key

Pass the key in the `Authorization` header, or set it as an environment variable for the SDKs.

## Scope

API keys are **scoped to the Workspace** where they were created. Resources created with a key (datasets, batch jobs, etc.) are visible to all members of that Workspace.

To use different keys for different environments, create separate [Workspaces](https://docs.mistral.ai/admin/security-access/organization).

## Best Practices

- **Rotate keys** regularly. Create a new key, update your applications, then delete the old one.
- **Revoke compromised keys** immediately.
- **Set expiration dates** so keys automatically stop working after a given date.
- **Usage tracking**: all usage from keys in a Workspace is tracked together and billed to the Organization.

> [!info]
> API keys require activated payments. Set up billing at [Admin Subscriptions Billing](https://admin.mistral.ai/organization/billing). You can choose between the free Experiment tier (with conservative rate limits) and the pay-as-you-go Scale plan.

#api-keys #authentication #security-best-practices #workspace-management
