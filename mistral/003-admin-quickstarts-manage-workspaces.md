---
title: Manage workspaces and API keys | Mistral Docs
url: https://docs.mistral.ai/admin/quickstarts/manage-workspaces
source: sitemap
fetched_at: 2026-04-26T04:00:53.426821486-03:00
rendered_js: false
word_count: 350
summary: This document provides instructions for managing Mistral workspaces to isolate API keys, monitor usage metrics, and implement spending controls for organizational teams.
tags:
    - workspace-management
    - api-security
    - billing-controls
    - access-management
    - mistral-admin
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Organize your Mistral account with workspaces, API keys, and spending controls.

- **Workspaces** isolate API keys and usage metrics by team or environment
- **API keys** are scoped to a workspace for tracking and access control
- **Spending limits** prevent unexpected costs per workspace

**Time to complete:** ~10 minutes

**Prerequisites:**
- Admin role in your Mistral organization
- Billing activated (API keys are inactive until a payment method is on file)

## Create Workspaces

Workspaces isolate API keys, usage metrics, and billing. Use them to separate development from production, or to track usage by team.

1. Open [Admin › Manage › Workspaces](https://admin.mistral.ai/organization/workspaces).
2. Click **Create workspace**.
3. Enter a name (e.g., `Production` or `ML Research`).
4. Optionally add an icon and description.
5. Click **Create**.

> [!tip]
> Create at least two workspaces (development and production) so test traffic doesn't consume production quotas.

## Add Workspace Members

Control who has access to each workspace independently.

1. Open the workspace you just created.
2. Click **Add members**.
3. Select team members from your organization.
4. Assign their workspace role.
5. Click **Confirm**.

## Generate API Keys

Each workspace has its own API keys. Usage is tracked and billed per workspace.

1. Open [Studio › API keys](https://console.mistral.ai/api-keys).
2. Select the target workspace from the workspace dropdown.
3. Click **Create new key**.
4. Name the key descriptively (e.g., `prod-backend` or `staging-chatbot`).
5. Copy the key immediately — it's shown only once.

> [!warning]
> Never commit API keys to source control. Use environment variables or a secrets manager.

## Set Spending Limits

Prevent unexpected costs by setting monthly spending limits per workspace.

1. Open [Admin › Subscriptions › Billing](https://admin.mistral.ai/organization/billing).
2. Under the workspace, click **Set limit**.
3. Enter a monthly budget in USD (e.g., `$500`).
4. When the workspace hits the limit, API requests return `429 Too Many Requests` until the next billing cycle.

Monitor real-time usage from the billing dashboard to spot trends before hitting limits.

## Verification Checklist

Your workspace setup is complete if:

- The workspace appears in the workspace dropdown in [Studio](https://console.mistral.ai)
- Team members added to the workspace can see it in their console
- API keys generated for the workspace return successful responses
- Usage appears under the correct workspace in the billing dashboard

#workspace-management #api-security #billing-controls #access-management
