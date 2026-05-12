---
title: Team management | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/teams
source: sitemap
fetched_at: 2026-04-29T15:03:36.761617921-03:00
rendered_js: false
word_count: 335
summary: This document explains how to manage teams in Warp, including creating teams, inviting members, setting domain restrictions, and configuring administrative roles and permissions.
tags:
    - team-management
    - collaboration
    - user-administration
    - warp-drive
    - billing-management
    - access-control
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## What is a Team?

A team is a group of Warp users who can collaborate on the command line together, sharing a dedicated workspace in Warp Drive.

> [!info]
> Each Warp user can only be an admin or member of one team at a time.

See [pricing](https://www.warp.dev/pricing) and [Pricing FAQ](https://docs.warp.dev/support-and-community/plans-and-billing/pricing-faqs).

## Create a Team

Create via:
- Warp Drive → **+ Create a team**
- **Settings** → **Teams**

Give the team a meaningful name (organization, company, or project name). Rename by going to **Settings** → **Teams**, clicking the team name, and pressing `ENTER`.

> [!info]
> The team creator becomes the admin and the only person who can delete the team.

## Invite Team Members

Under **Settings** → **Teams**, copy the invite link and share it securely (e.g., Slack or email).

> [!warning]
> On a paid plan, upgrading automatically includes all team members in billing. Adding new members after upgrading adds paid seats.

See [billing FAQ](https://docs.warp.dev/support-and-community/plans-and-billing/pricing-faqs#what-counts-as-a-team-member-and-how-does-billing-work-for-members) for billing details.

## Restrict Team Invites by Domain

Toggle on **Restrict by domain** to set an allowlist. Members with non-matching email domains must authenticate via an emailed link sent to a matching domain.

## Join a Team

Use the invite link to sign up/log in and join. If domain restriction is enabled, authenticate with a matching domain.

## Leave or Delete a Team

- **Members** — go to **Settings** → **Teams** to leave at any time.
- **Admins** — delete the team only after removing all members.

## Team Discoverability

Team admins can make teams discoverable to colleagues from the same email domain: **Settings** → **Teams** → **Make team discoverable**.

> [!info]
> Any user who joins while discoverability is enabled adds a prorated charge to the team's next bill.

## Transfer Admin Role

Go to **Settings** → **Teams** → **Transfer admin**, then select the target member.

## Team Roles and Permissions

> [!warning]
> If a Team admin deletes their Warp account, the deletion flow requires assigning a team member as the new admin.
