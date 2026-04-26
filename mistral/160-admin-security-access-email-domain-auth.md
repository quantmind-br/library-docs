---
title: Email domain authentication | Mistral Docs
url: https://docs.mistral.ai/admin/security-access/email-domain-auth
source: sitemap
fetched_at: 2026-04-26T04:00:58.212971842-03:00
rendered_js: false
word_count: 202
summary: This document explains how to configure email domain authentication to automatically add new users from a verified domain to an organization.
tags:
    - email-authentication
    - domain-verification
    - user-management
    - organization-access
    - admin-settings
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Email Domain Authentication

> [!info]
> Available on **Team** plans and above.

Email domain authentication controls how new users join your Organization. When enabled, anyone signing up or logging in with an **email address matching your verified domain** is automatically added.

- Users with matching domain emails are **automatically added** to your Organization.
- Users still **create and manage their own credentials**. This feature controls Organization membership, not authentication.
- For SSO without separate credentials, use [SSO](https://docs.mistral.ai/admin/security-access/sso) instead (Enterprise plans).

## Setup

> [!warning]
> You need to **verify ownership of your domain** before enabling. Domain verification uses a DNS TXT record.

1. Open [Admin Access](https://admin.mistral.ai) settings.
2. In the **Authentication** section, click **Activate email domain authentication**.
3. Confirm by clicking **Enable email domain authentication**.

See [domain verification](https://docs.mistral.ai/admin/security-access/sso#domain-verification) for DNS TXT record setup.

## Disabling

You can disable email domain authentication at any time:

- New users with matching domain emails won't be auto-added.
- Existing members aren't affected.
- You'll need to manually invite new users unless [SSO](https://docs.mistral.ai/admin/security-access/sso) is configured.

> [!note]
> If you re-enable later, you'll need to go through the setup process again.

#email-authentication #domain-verification #user-management #organization-access
