---
title: SSO | Mistral Docs
url: https://docs.mistral.ai/admin/security-access/sso
source: sitemap
fetched_at: 2026-04-26T04:01:01.959188142-03:00
rendered_js: false
word_count: 599
summary: This document provides instructions for configuring Single Sign-On (SSO) using SAML 2.0 for enterprise accounts, including the prerequisite domain verification process.
tags:
    - sso
    - saml-2.0
    - identity-provider
    - enterprise-security
    - domain-verification
    - authentication-management
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# SSO (Single Sign-On)

> [!warning]
> Enterprise only. Contact [sales](https://mistral.ai/contact/) to upgrade.

SSO lets users authenticate with their existing corporate **identity provider (IdP)** using SAML 2.0. We support any compliant IdP (Okta, Microsoft Entra ID, Google Workspace).

## Benefits

- **Centralized authentication**: users sign in with familiar corporate credentials.
- **Automatic account creation**: user accounts provisioned on first sign-in through your IdP.
- **Simplified management**: manage access centrally from your IdP.

## Prerequisites

- **Enterprise** plan subscription
- **Domain verification** completed in the Admin Panel

## Domain Verification

1. Open [Admin Access](https://admin.mistral.ai) settings.
2. Click **Add domain** in Domain Ownership section.
3. Enter your domain (e.g., `yourcompany.com`) and click **Add domain**.
4. Click **Instructions** and copy the DNS TXT record.
5. In your DNS provider, add a new TXT record:
   - **Type**: `TXT`
   - **Host/Name**: `@` or your domain
   - **Value**: paste the verification code (e.g., `mistral-domain-verification=xxxxxx`)
6. Save and wait for DNS propagation (typically 10 minutes to 24 hours).

> [!warning]
> Keep the DNS TXT record active. Removing it breaks both Email Domain Authentication and SSO.

## Setting Up SSO

1. Open [Admin Access](https://admin.mistral.ai) settings.
2. Find **Single Sign-On (SAML SSO)** and click **Activate SSO**.
3. In your IdP admin console, create a new **SAML 2.0 application** for Mistral AI.
4. Copy **ACS URL** and **Entity ID** from Mistral modal to your IdP.
5. Map user attributes (case-sensitive):
   - User's first name: `firstName`
   - User's last name: `lastName`
6. Set **Name ID Format** to `EmailAddress`.
7. Obtain **SAML metadata XML** from your IdP.
8. Paste the XML into the Mistral configuration modal.
9. Click **Enable SSO**.

## User Login Flow

1. Go to Mistral AI login page.
2. Enter work email address.
3. Click **Sign in with SSO**, then select your organization.
4. Authenticate with corporate credentials on your IdP.
5. Redirected back to Mistral AI, logged in.

## Supported Identity Providers

- Microsoft Entra ID (formerly Azure Active Directory)
- Google Workspace / Google Identity Platform
- Okta

## Disabling SSO

> [!warning]
> Disabling SSO means users can no longer sign in through your IdP. They'll need to set a password or be re-invited. Automatic user provisioning stops.

Consider enabling [Email Domain Authentication](https://docs.mistral.ai/admin/security-access/email-domain-auth) as an alternative before disabling SSO.

## Notes

- OIDC isn't supported. We use SAML 2.0 only for enterprise SSO.
- SSO is available on Enterprise plans only.

## Troubleshooting

If SSO fails:
- Verify **ACS URL** and **Entity ID** match exactly between Mistral and your IdP.
- Confirm attribute mappings are case-sensitive (`firstName`, `lastName`).
- Check that **Name ID Format** is set to `EmailAddress`.
- Make sure the metadata XML is complete and correctly pasted.
- Contact [support](https://help.mistral.ai) if issues persist.

#sso #saml-2.0 #identity-provider #enterprise-security #domain-verification
