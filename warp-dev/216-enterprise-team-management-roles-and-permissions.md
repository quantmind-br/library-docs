---
title: Roles and permissions | Enterprise | Warp
url: https://docs.warp.dev/enterprise/team-management/roles-and-permissions
source: sitemap
fetched_at: 2026-04-29T15:06:07.112462909-03:00
rendered_js: false
word_count: 543
summary: This document outlines the role-based access control system in Warp, detailing the permissions and responsibilities assigned to owners, admins, and members. It also explains how administrators manage team settings, enforce security policies, and control resource sharing within an organization.
tags:
    - role-based-access
    - user-permissions
    - team-management
    - security-policy
    - access-control
    - admin-settings
category: concept
optimized: true
optimized_at: 2026-04-29T15:04:00Z
---
Warp uses a role-based access model to control what team members can do within your organization. Admins manage team settings and enforce policies, while members use Warp's features within the boundaries admins define.

## User roles

| Role | Access level |
|------|--------------|
| **Team Owner** | Full access to the Admin Panel: manage team settings, invite users, assign roles, and transfer ownership. Only one Owner per team. |
| **Team Admin** | Same permissions as the Owner, except cannot transfer ownership of the team. |
| **Member** | Standard access to Warp features and team resources. Can use agents, access shared Warp Drive resources, and configure personal settings within admin-defined limits. |

## Managing admins

Teams can have multiple admins. We recommend at least one admin in addition to the Team Owner to prevent access issues if one is unavailable.

### Promoting or demoting admins

1. Navigate to **Settings** > **Teams** > **Team Members**.
2. Find the user you want to modify.
3. Click the three-dot menu icon next to their name.
4. Select **Promote to Admin** or **Demote from Admin**.
5. Confirm the change when prompted.

> [!warning]
> Team Admins cannot demote or modify the Team Owner role.

## Permission details

### What admins can do

- **Team management** — View members, invite users, remove users, and assign roles
- **Authentication** — Configure SSO and login requirements
- **Agent policies** — Set autonomy levels, command allowlists/denylists, and directory access controls
- **Security settings** — Configure secret redaction, telemetry controls, and data handling policies
- **Feature controls** — Enable or disable Codebase Context, BYOLLM, sharing, and other features
- **Billing** — Monitor credit usage, set spending limits, and manage subscriptions

### What members can do

- **Use agents** — Run Oz agents locally and in the cloud within the policies admins define
- **Access team resources** — Use shared Workflows, Notebooks, Prompts, Rules, and Environment Variables in Warp Drive
- **Configure personal settings** — Adjust settings where admins have selected "Respect User Setting"
- **Share sessions** — Collaborate via session sharing (if enabled by admins)
- **Index codebases** — Trigger Codebase Context indexing for repositories (if enabled by admins)

### Settings enforcement

Admin-configured settings follow a three-tier model:

| Tier | Behavior | Use case |
|------|----------|----------|
| **Organization enforced** | Applies to all members. Users cannot override. | Security-critical policies (e.g., secret redaction, command denylists) |
| **Respect user setting** | Admins set a default, individual users can customize. | Preferences that don't impact security |
| **Tier restricted** | Locked based on billing plan. Cannot change until plan is upgraded. | Plan-gated features |

See the [Admin Panel](https://docs.warp.dev/enterprise/team-management/admin-panel) documentation for details on configuring each setting.

## Resource sharing controls

Admins control how team members collaborate and share Warp Drive resources:

- **Direct link sharing** — Allow team members to share Notebooks, Workflows, Prompts, and other objects via direct links
- **Team-only links** — Restrict links so only team members can access them
- **Public link sharing** — Enable or disable access for anyone with the link (even non-team members)

> [!warning]
> For organizations with sensitive internal processes, disable public link sharing to prevent accidental exposure.

## Related resources

- [Admin Panel](https://docs.warp.dev/enterprise/team-management/admin-panel) — Configure team settings and enforce policies