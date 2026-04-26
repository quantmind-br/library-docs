---
title: Organizations and Workspaces | Mistral Docs
url: https://docs.mistral.ai/admin/security-access/organization
source: sitemap
fetched_at: 2026-04-26T04:00:59.824021789-03:00
rendered_js: false
word_count: 453
summary: This document explains the hierarchical structure of Mistral AI accounts, detailing the roles, management features, and configuration differences between Organizations and Workspaces.
tags:
    - account-management
    - workspace-configuration
    - organization-structure
    - user-roles
    - billing-management
    - api-security
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Organizations and Workspaces

Your Mistral AI account has two levels: **Organizations** (billing, user management, security) and **Workspaces** (isolated environments for projects, teams, or API usage).

## Organizations

An Organization is the top-level entity for your company or team. A default Organization is created automatically when you create an account.

### Organization Administration

- **Billing** for all Workspaces
- **Subscriptions** (Le Chat and Studio)
- **Members** and role assignments
- **Security** settings (SSO, domain authentication)
- **Privacy** and data handling preferences
- **Audit logs** (Enterprise)

Every Organization has a unique **Organization ID** for API calls or support requests.

## Workspaces

A Workspace is an isolated environment within your Organization. Each Workspace has its own API keys, member access list, and usage tracking.

### Use Cases

- **Separating environments**: keep development, staging, and production isolated
- **Scoping API keys**: keys created in a Workspace only access that Workspace's resources
- **Tracking costs**: monitor usage and spending per team or project
- **Sharing resources**: datasets and batch jobs shared among Workspace members

> [!note]
> You can create unlimited Workspaces regardless of plan. On Team and Enterprise plans, you can add multiple members to each Workspace. On other plans, Workspaces are single-user.

Workspace roles are **independent** from Organization roles. A user with Member role at Organization level can be an Admin within a specific Workspace.

## Creating Workspaces

Only Organization Admins can create Workspaces.

1. Open [Admin Workspaces](https://admin.mistral.ai).
2. Click **New workspace**.
3. Configure:
   - **Name** (required): clear label
   - **Description** (optional): context about purpose
   - **Members** (optional): add Organization members now or later
4. Click **Create**.

You can also create Workspaces from Studio by clicking your organization name and selecting **+ Add** in the Workspaces section.

## Managing Workspace Members

1. Open the Workspace settings.
2. Click the **Members** tab.
3. Click **Add Members** and select users from your Organization.
4. Assign a Workspace role (Admin or Member).

## Workspace Settings

Workspace Admins can customize:

- **Name** and **description**
- **Icon** (optional emoji)
- **Permissions**: control whether members can create API keys
- **Spending limits**: set a monthly cap

## Archiving a Workspace

> [!warning]
> Archiving a Workspace is permanent and can't be undone. All API keys in the Workspace stop working immediately.

#account-management #workspace-configuration #organization-structure #user-roles
