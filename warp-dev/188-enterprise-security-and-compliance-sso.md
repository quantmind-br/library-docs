---
title: Single Sign-On (SSO) | Enterprise | Warp
url: https://docs.warp.dev/enterprise/security-and-compliance/sso
source: sitemap
fetched_at: 2026-04-29T15:06:03.897357454-03:00
rendered_js: false
word_count: 483
summary: This document provides instructions for configuring and managing Single Sign-On (SSO) for Warp teams using supported identity providers and WorkOS.
tags:
    - sso
    - identity-provider
    - user-authentication
    - security-compliance
    - team-management
    - scim-provisioning
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
SSO authenticates users and controls access to your Warp team. Configure via WorkOS in coordination with Warp.

## Supported identity providers

- **Okta**
- **Microsoft Entra ID**
- **Google Workspace**
- **OneLogin**
- **Any SAML 2.0 or OpenID Connect (OIDC) compatible provider**

## SSO enforcement and session management

| Feature | Behavior |
|---|---|
| SSO enforcement | Admins can require SSO for all team members, blocking other login methods |
| MFA | Enforced through your identity provider (Okta, Entra ID, Google Workspace, etc.) |
| Session management | Configurable via your identity provider |

## Setting up SSO

SSO is configured through [WorkOS](https://workos.com):

1. Warp creates an organization in WorkOS and sets your team domain.
2. Your IT admin receives an email invite from WorkOS.
3. Follow the WorkOS wizard to connect your identity provider (SAML attributes or OAuth scopes, SSO URL, certificate).

> [!note]
> After enabling SSO, existing users who signed up via email or OAuth must link their accounts before using SSO.

## Testing SSO

1. Open an incognito/private browser window.
2. Click **Continue with SSO**.
3. Enter your organization's domain.
4. Verify redirect to your identity provider and successful login.

> [!warning]
> Warp cannot be launched directly from your SSO provider's app portal (e.g., Okta dashboard). Users must go to [app.warp.dev/login](https://app.warp.dev/login) and select **Continue with SSO**.

## SCIM provisioning

Warp supports user lifecycle management via Just-In-Time (JIT) provisioning + SSO + domain capture:

- **User provisioning** — Add users in your identity provider; they are automatically added to your Warp team on first SSO login.
- **Domain auto-join** — Users signing in from your configured domain auto-join your team.
- **User deprovisioning** — Removing a user from the Warp app in your identity provider blocks future SSO logins (existing sessions not immediately revoked).

> [!info]
> Warp does not currently support SCIM group sync. Users appear after their first SSO login, not at the time they're assigned in the identity provider.

## Linking existing accounts

Users with pre-SSO accounts must link before logging in with SSO:

1. Log in to Warp with the original method (email, Google, or GitHub).
2. Complete the linking process.
3. Log out and log back in with **Continue with SSO**.

## Domain auto-join

Users from your organization automatically join your Warp team after SSO authentication.

> [!info]
> Domain configuration is set up by the Warp team during onboarding. Contact your Warp account team to configure or update your team domain.

## Troubleshooting

### Users can't log in with SSO

**Common causes:** SSO misconfigured in identity provider; user launching Warp directly from SSO portal.

**Solution:** Verify SSO configuration in your identity provider. Log in through [app.warp.dev/login](https://app.warp.dev/login).

### Warp won't open from SSO provider portal

**Problem:** Clicking Warp in Okta/Microsoft Entra ID portal shows an error.

**Solution:** Log in through [app.warp.dev/login](https://app.warp.dev/login) and select **Continue with SSO**.

#sso #identity-provider #user-authentication #security-compliance #team-management #scim-provisioning
