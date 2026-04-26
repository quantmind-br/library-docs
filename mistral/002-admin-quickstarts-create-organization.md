---
title: Create your organization | Mistral Docs
url: https://docs.mistral.ai/admin/quickstarts/create-organization
source: sitemap
fetched_at: 2026-04-26T04:00:53.191090591-03:00
rendered_js: false
word_count: 316
summary: This document provides a step-by-step guide for setting up and managing a Mistral organization, including billing configuration, workspace creation, and team member management.
tags:
    - mistral-ai
    - organization-setup
    - billing-configuration
    - workspace-management
    - team-onboarding
    - admin-console
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Set up a Mistral organization from a new account through [Admin](https://admin.mistral.ai).

- Activate billing so API keys work
- Create your first workspace
- Invite team members and assign roles

**Time to complete:** ~15 minutes

**Prerequisites:**
- A Mistral AI account. [Create account](https://console.mistral.ai)
- A credit card or cloud billing account (AWS or Azure Marketplace)
- The email address of at least one colleague to invite

## Start Setup

Log in to [Studio](https://console.mistral.ai). New accounts are prompted to name their organization and redirected to Admin automatically.

Already have an account without an organization? Open [Admin](https://admin.mistral.ai) and follow the setup prompt.

> [!warning]
> Team members can't generate working API keys until billing is active.

## Activate Billing

Open [Admin › Subscriptions › Billing](https://admin.mistral.ai/organization/billing), click **Add payment method**, and connect your card or cloud marketplace account. Optionally set a **Monthly spending limit** before saving.

Billing takes 2–3 minutes to take effect. If team members report inactive API keys right after, ask them to wait and retry.

## Create a Workspace

Your default workspace is created automatically — skip this step if one workspace is enough.

Open [Admin › Manage › Workspaces](https://admin.mistral.ai/organization/workspaces), click **Create workspace**, and give it a name (e.g., "Engineering" or "Production").

## Invite Team Members

Open [Admin › Administration › Members](https://admin.mistral.ai/organization/members), click **Invite member**, enter the email address, and assign a role.

The invited team member receives an email within a few minutes. Once they accept, their status changes from **Pending** to **Active**.

## Ongoing Management

As your team grows, control who can access what:

- **Configure SSO:** Enforce enterprise authentication with SAML-based SSO. Navigate to **Administration › Settings** in the Admin panel to configure your identity provider and define an **Allowed email domain** to block invites to personal or external addresses.
- **Monitor audit logs:** Open [Admin › Administration › Audit logs](https://admin.mistral.ai/audit-logs) to track critical events (API key creation, invites, billing changes).

#organization-setup #billing-configuration #workspace-management #team-onboarding
