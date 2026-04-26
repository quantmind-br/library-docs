---
title: Configure SSO and domain verification | Mistral Docs
url: https://docs.mistral.ai/getting-started/quickstarts/admin/configure-sso
source: sitemap
fetched_at: 2026-04-26T04:07:00.705709479-03:00
rendered_js: false
word_count: 503
summary: This document provides instructions for administrators to verify their corporate domain and configure SAML SSO to integrate identity providers with their Mistral organization.
tags:
    - domain-verification
    - saml-sso
    - identity-provider
    - corporate-access
    - admin-configuration
    - user-onboarding
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Verify your company domain and connect your corporate identity provider to your Mistral organization.

- Add a DNS TXT record to prove domain ownership
- Enable email-domain authentication for automatic team onboarding
- Configure SAML SSO with your IdP (Okta, Azure AD, Ping Identity, or similar)

Team members sign in with corporate credentials instead of separate Mistral passwords.

**Time to complete:** ~20 minutes

**Prerequisites:**
- Enterprise plan (SAML SSO requires Enterprise; domain verification works on Team+)
- Admin role in your Mistral organization
- Access to your company's DNS records
- Access to your identity provider admin console

## Domain Verification

Domain verification proves you own your company's email domain, enabling email-domain authentication and SSO.

1. Navigate to **Administration › Settings** in the [Admin panel](https://admin.mistral.ai).
2. Under **Domain verification**, click **Add domain**.
3. Enter your domain (e.g., `acme.com`).
4. Copy the generated DNS TXT record value.
5. Add the TXT record to your domain's DNS configuration.
6. Click **Verify**. DNS propagation can take up to 48 hours but typically finishes within 15 minutes.

> [!tip]
> Confirm the TXT record is live before clicking Verify: `dig TXT _mistral-verification.acme.com`

## Email-Domain Authentication

Once your domain is verified, automatically add anyone with a matching email address to your organization.

1. Navigate to **Administration › Settings** in the [Admin panel](https://admin.mistral.ai).
2. Under **Email domain authentication**, toggle it **on**.
3. Select the default role for auto-joined users: **Member** (recommended).

> [!warning]
> Only enable this if you want all employees with your domain email to have automatic access.

## SAML SSO

SAML SSO lets team members sign in through your corporate identity provider.

1. Navigate to **Administration › Settings** in the [Admin panel](https://admin.mistral.ai).
2. Under **SAML SSO**, click **Configure**.
3. Two values are provided for your IdP — paste these in your IdP's SAML application.
4. In your IdP (Okta, Azure AD, etc.), create a new SAML application and paste the ACS URL and Entity ID.
5. Configure attribute mapping in your IdP.
6. Copy the **IdP metadata URL** (or download the metadata XML) from your IdP.
7. Paste the metadata URL in the settings page and click **Save**.

## Test SSO

1. Open a private/incognito browser window.
2. Open [Le Chat](https://chat.mistral.ai) or [Studio](https://console.mistral.ai).
3. Click **Sign in with SSO** and enter your company email.
4. Your IdP login page opens.
5. After authenticating, you land in your Mistral dashboard with your organization selected.

> [!warning]
> If login fails: verify the ACS URL and Entity ID match exactly between Mistral and your IdP. Check that the Name ID format is set to **email**.

## Verification Checklist

Your SSO is configured correctly if:

- The domain shows **Verified** in Organization Settings
- Team members can sign in via your IdP without a separate Mistral password
- New users who sign in via SSO are automatically added to your organization
- User names (first and last) appear correctly from the IdP attribute mapping

#domain-verification #saml-sso #identity-provider
