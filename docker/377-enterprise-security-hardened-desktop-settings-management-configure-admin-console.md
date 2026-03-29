---
title: Use the Admin Console
url: https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/
source: llms
fetched_at: 2026-01-24T14:26:41.672151321-03:00
rendered_js: false
word_count: 388
summary: This document explains how administrators can use the Docker Admin Console to create, manage, and enforce configuration policies for Docker Desktop across an organization.
tags:
    - docker-desktop
    - admin-console
    - settings-management
    - docker-business
    - security-policies
    - enterprise-configuration
category: configuration
---

## Configure Settings Management with the Admin Console

Subscription: Business

For: Administrators

Use the Docker Admin Console to create and manage settings policies for Docker Desktop across your organization. Settings policies let you standardize configurations, enforce security requirements, and maintain consistent Docker Desktop environments.

## [Prerequisites](#prerequisites)

Before you begin, make sure you have:

- [Docker Desktop 4.37.1 or later](https://docs.docker.com/desktop/release-notes/) installed
- [A verified domain](https://docs.docker.com/enterprise/security/single-sign-on/configure/#step-one-add-and-verify-your-domain)
- [Enforced sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) for your organization
- A Docker Business subscription

> Important
> 
> You must add users to your verified domain for settings to take effect.

## [Create a settings policy](#create-a-settings-policy)

To create a new settings policy:

1. Sign in to [Docker Home](https://app.docker.com/) and select your organization.
2. Select **Admin Console**, then **Desktop Settings Management**.
3. Select **Create a settings policy**.
4. Provide a name and optional description.
   
   > Tip
   > 
   > You can upload an existing `admin-settings.json` file to pre-fill the form. Admin Console policies override local `admin-settings.json` files.
5. Choose who the policy applies to:
   
   - All users
   - Specific users
     
     > Note
     > 
     > User-specific policies override global default policies. Test your policy with a small group before applying it organization-wide.
6. Configure each setting using a state:
   
   - **User-defined**: Users can change the setting.
   - **Always enabled**: Setting is on and locked.
   - **Enabled**: Setting is on but can be changed.
   - **Always disabled**: Setting is off and locked.
   - **Disabled**: Setting is off but can be changed.
     
     > Tip
     > 
     > For a complete list of configurable settings, supported platforms, and configuration methods, see the [Settings reference](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/settings-reference/).
7. Select **Create** to save your policy.

## [Apply the policy](#apply-the-policy)

Settings policies take effect after Docker Desktop restarts and users sign in.

For new installations:

1. Launch Docker Desktop.
2. Sign in with your Docker account.

For existing installations:

1. Quit Docker Desktop completely.
2. Relaunch Docker Desktop.

> Important
> 
> Users must fully quit and reopen Docker Desktop. Restarting from the Docker Desktop menu isn't sufficient.

Docker Desktop checks for policy updates when it launches and every 60 minutes while running.

## [Verify applied settings](#verify-applied-settings)

After you apply policies:

- Docker Desktop displays most settings as greyed out
- Some settings, particularly Enhanced Container Isolation configurations, may not appear in the GUI
- You can verify all applied settings by checking the [`settings-store.json` file](https://docs.docker.com/desktop/settings-and-maintenance/settings/) on your system

## [Manage existing policies](#manage-existing-policies)

From the **Desktop Settings Management** page in the Admin Console, use the **Actions** menu to:

- Edit or delete an existing settings policy
- Export a settings policy as an `admin-settings.json` file
- Promote a user-specific policy to be the new global default

## [Roll back policies](#roll-back-policies)

To roll back a settings policy:

- Complete rollback: Delete the entire policy.
- Partial rollback: Set specific settings to **User-defined**.

When you roll back settings, users regain control over those settings configurations.