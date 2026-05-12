---
title: Teams | Enterprise | Warp
url: https://docs.warp.dev/enterprise/team-management/teams
source: sitemap
fetched_at: 2026-04-29T15:06:04.081113001-03:00
rendered_js: false
word_count: 448
summary: This document explains how to manage teams in Warp, covering creation, membership invitations, access control, role permissions, and administrative settings.
tags:
    - team-management
    - collaboration
    - user-roles
    - access-control
    - enterprise-configuration
    - warp-drive
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
A team is a group of Warp users sharing a Warp Drive workspace (Workflows, Notebooks, Prompts, Rules, Plans, Environment Variables). Teams enable centralized administration and policy enforcement via the [[189-enterprise-team-management-admin-panel|Admin Panel]].

> [!info]
> Each user can be admin or member of one team at a time.

## Creating a team

- **Warp Drive** side panel → **+ Create a team**
- **Settings** → **Teams** → follow the prompts

The creator becomes the **Team Owner**. Rename anytime via **Settings** → **Teams** → click team name → `Enter`.

> [!warning]
> On paid plans, new members add paid seats billed prorated for the remainder of the billing cycle.

## Inviting team members

**Settings** → **Teams** → copy invite link → share via secure channel.

## Restricting team invites by domain

Admins can restrict membership to specific email domains:

1. **Settings** → **Teams** → toggle **Restrict by domain**
2. Add allowed email domains to the allowlist

Users with non-matching domains authenticate via an emailed link to an allowed domain.

## Joining a team

Use the invite link. If domain restriction is enabled, verify access to an allowed-domain email address.

## Leaving and deleting teams

- **Members/Admins** — **Settings** → **Teams** → **Leave team**
- **Team Owners** — delete only after removing all other members first

## Team discoverability

When enabled, users sharing the same email domain can find and join the team without an invite link.

**Settings** → **Teams** → **Make team discoverable**

> [!info]
> Each new user who joins adds a prorated charge to the next billing cycle.

## Transferring team ownership

1. **Settings** → **Teams** → **Team Members**
2. Click the three-dot menu next to the target member
3. **Transfer ownership**

> [!info]
> If the new owner's email is not on a work domain, discoverability is automatically disabled as a safety measure.

## Team roles and permissions

| Role | Permissions |
|---|---|
| **Team Owner** | Full access to Admin Panel and all settings; can manage members, assign roles, configure policies, transfer ownership. One Owner per team. |
| **Team Admin** | Same as Owner except cannot transfer ownership. Enterprise plans support multiple admins. |
| **Member** | Standard access to Warp features and team resources within admin-set limits. |

> [!info]
> Recommend at least one Team Admin in addition to the Owner to prevent access issues.

### Multi-admin support (Enterprise)

1. **Settings** → **Teams** → **Team Members**
2. Find the user → three-dot menu → **Promote to Admin** or **Demote from Admin**
3. Confirm

> [!warning]
> Admins cannot demote or modify the Owner's role. Ownership transfer is the only path.

See [[189-enterprise-team-management-admin-panel|Admin Panel]] for configuration details.

#team-management #collaboration #user-roles #access-control #enterprise-configuration #warp-drive
