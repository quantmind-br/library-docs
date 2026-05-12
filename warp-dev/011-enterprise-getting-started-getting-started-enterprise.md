---
title: Getting started for admins | Enterprise | Warp
url: https://docs.warp.dev/enterprise/getting-started/getting-started-enterprise
source: sitemap
fetched_at: 2026-04-29T15:05:59.793276816-03:00
rendered_js: false
word_count: 854
summary: This document provides a comprehensive guide for administrators to set up and manage an organization's Warp Enterprise account, covering SSO configuration, user management, policy enforcement, and resource deployment.
tags:
    - enterprise-onboarding
    - sso-configuration
    - user-management
    - admin-panel
    - team-administration
    - warp-setup
category: guide
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
This guide walks IT or platform admins through initial Warp setup: configuring SSO, creating your team, inviting users, and setting Admin Panel policies.

## Prerequisites

- Active Warp Enterprise subscription
- Admin access to your identity provider (Okta, Microsoft Entra ID, Google Workspace, etc.)
- Identified team members who need admin privileges in Warp

## Step 1: Configure Single Sign-On (SSO)

Warp uses SSO to authenticate users and control access. Supported providers: Okta, Microsoft Entra ID, Google Workspace, OneLogin, and any SAML 2.0 or OIDC compatible provider via [WorkOS](https://workos.com).

SSO setup is coordinated with Warp's team—contact your account team or [enterprise support](https://warp.dev/contact-sales). See [[188-enterprise-security-and-compliance-sso|SSO documentation]] for full setup process.

> [!warning]
> Before rolling out to your team, test SSO login in an incognito window to confirm it works. See [[188-enterprise-security-and-compliance-sso#testing-sso|Testing SSO]].

## Step 2: Create and configure your team

### Creating your team

Enterprise plan application happens in one of two ways:
- **Warp provisions your team** — Warp creates the team and adds your admin
- **You create or bring your own team** — Apply the Enterprise plan during onboarding

> [!note]
> The Enterprise plan must be applied by Warp internally—this cannot be self-served. Contact your account manager.

### Team settings

Settings are configured in different places:

| Setting | Location |
|---|---|
| Team name | **Settings** > **Teams** in Warp app |
| Domain restrictions | **Settings** > **Teams** |
| Auto-join | **Settings** > **Teams** (domain set by Warp team during onboarding) |
| SSO | Configured through WorkOS (not Admin Panel) |

## Step 3: Invite and manage users

### Inviting users

**Option 1: Invite by email**
1. Navigate to **Settings** > **Teams**.
2. Enter email addresses (comma-separated) in **Invite by Email**.
3. Click **Invite**.

**Option 2: Share invite link**
1. Navigate to **Settings** > **Teams**.
2. Copy the team invite link.
3. Share via your preferred channel.

**Option 3: Domain auto-join**
1. Domain must be configured by Warp team during onboarding. Contact your account team.
2. Users signing in via SSO from your domain are automatically added.

### User roles and permissions

| Role | Permissions |
|---|---|
| **Team Owner** | Full access to Admin Panel, manage settings, invite users, assign roles, transfer ownership. One Owner only. |
| **Team Admin** | Same as Owner except cannot transfer ownership. |
| **Member** | Standard access to Warp features and team resources. |

### Managing admins

1. Navigate to **Settings** > **Teams** > **Team Members**.
2. Find the user, click **...** next to their name.
3. Select **Promote to admin** or **Demote admin**.

> [!tip]
> Teams can have multiple admins. We recommend at least one admin in addition to the Owner to prevent access issues if one is unavailable.

## Step 4: Configure the Admin Panel

The Admin Panel provides centralized control over Warp features, permissions, and usage.

**Access:**
- In Warp: **Settings** > **Billing and usage** > **Open Admin Panel**
- Direct: [app.warp.dev/admin](https://app.warp.dev/admin)

**Key sections:**

| Section | Description |
|---|---|
| **Billing** | Plan type and AI usage limits |
| **Teams** | Manage members, roles, invites |
| **AI** | General and AI autonomy settings |
| **Models** | Available models and AWS Bedrock config |
| **Code** | Codebase Context for your team |
| **Platform** | Oz cloud agent settings |
| **Privacy** | Data collection, cloud storage, secret redaction |
| **Sharing** | Direct link sharing and "anyone with link" permissions |

**Settings enforcement:**
- **Enforced settings** — Cannot be overridden by users (e.g., BYOLLM routing policies)
- **Respect User Setting** — Defers to individual user preferences

## Step 5: Set up team resources

### Enable Codebase Context

1. Navigate to **Admin Panel** > **Code**.
2. Toggle **Codebase Indexing** to **Enabled**.

Warp prompts team members to index repositories when they navigate to a Git-tracked directory.

### Create shared Warp Drive resources

Populate Warp Drive with shared resources:

- **Workflows** — Parameterized commands for common tasks
- **Notebooks** — Interactive runbooks for onboarding and procedures
- **Prompts** — Saved agent prompts for recurring tasks
- **Rules** — Coding standards agents should follow
- **Environment Variables** — Shared configuration for dev environments

See [[144-knowledge-and-collaboration-warp-drive|Warp Drive documentation]].

### Configure MCP integrations

1. Navigate to **Settings** > **Agents** > **MCP servers**.
2. Enable integrations (Linear, GitHub, Sentry available with one click).
3. Add custom MCP server configurations as needed.
4. Click the share icon on a server to make it available to your team.

See [[072-agent-platform-warp-agents-agent-context-mcp|MCP documentation]].

## Next steps

- **Agent Profiles** — Configure default [[035-agent-platform-warp-agents-capabilities-overview-agent-profiles-permissions|Agent Profiles]] for different types of work
- **BYOLLM** — Set up [[232-enterprise-enterprise-features-bring-your-own-llm|Bring Your Own LLM]] for data locality and cost control
- **Monitor usage** — Review usage analytics in Admin Panel
- **Self-hosting** — Run Oz agents on your own infrastructure. See [[210-agent-platform-cloud-agents-self-hosting|Self-Hosting]]

## Troubleshooting

### SSO login issues

See [[188-enterprise-security-and-compliance-sso#troubleshooting|SSO troubleshooting]] for common problems (login failures, account linking, provider portal errors).

### Team invite links not working

**Common causes:** Invite link expired or revoked, user's email domain doesn't match configured restrictions.

**Solution:**
1. Generate a new invite link.
2. Verify domain restrictions match user's email.