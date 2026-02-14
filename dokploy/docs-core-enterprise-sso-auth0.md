---
title: Auth0 | Dokploy
url: https://docs.dokploy.com/docs/core/enterprise/sso/auth0
source: crawler
fetched_at: 2026-02-14T14:18:27.655088-03:00
rendered_js: true
word_count: 335
summary: This guide provides step-by-step instructions for configuring Single Sign-On (SSO) between Auth0 and Dokploy using the SAML 2.0 protocol.
tags:
    - dokploy
    - auth0
    - saml
    - sso
    - authentication
    - identity-provider
category: tutorial
---

## [1. Create a SAML application in Auth0](#1-create-a-saml-application-in-auth0)

1. Log in to the [Auth0 Dashboard](https://manage.auth0.com/).
2. Go to **Applications** → **Applications** → **Create Application**.
3. Choose **Regular Web Application** and create it.
4. In the application, go to **Add Ons** → enable **SAML 2 Web App** and configure it, in the settings specify this callback URL: `https://your-dokploy-domain.com/api/auth/sso/saml2/callback/myorg-name-auth0-saml`.
5. Next & Save.

## [2. Configure Dokploy](#2-configure-dokploy-1)

1. In Dokploy, go to **Settings** (or **Organization** / **Security** in Enterprise).
2. Enable **SSO** and choose **SAML**.
3. Enter:
   
   - **Provider**: myorg-name-auth0-saml (unique name for this provider)
   - **Issuer URL**: the Auth0 SAML Entity ID / Issuer located in `Add Ons` tab called `SAML 2 Web App` called `Entity ID` (e.g. `urn:auth0:your-tenant:your-app`)
   - **SSO URL**: the Auth0 SAML Single Sign-On URL located in `Add Ons` tab called `SAML 2 Web App` called `Single Sign-On URL` (e.g. `https://dev-ladsadb.us.auth0.com/samlp/wgJe9bWmwhVnuAC7eNtyUsiou4b6wxuf`)
   - **Certificate**: download the certificate active (x509) from the `Add Ons` tab called `SAML 2 Web App` called `Identity Provider Certificate` and paste it in the `Certificate` field.
   - **Federation Metadata XML**: copy the Identity Provider Metadata XML from the certificate active and paste it in the `Metadata XML` field.
   - **Domain**: the domain users use to authenticate via Auth0 (e.g. your organization domain like `acme.com`), not the Dokploy instance URL
4. Save.

## [3. Configure Auth0 (SAML)](#3-configure-auth0-saml)

1. In your Auth0 SAML application, set the **Application Callback URL** (ACS URL) to your Dokploy SAML ACS URL, for example:
   
   - `https://your-dokploy-domain.com/api/auth/sso/saml2/callback/myorg-name-auth0-saml`
2. In the **SAML 2 Web App** add-on, open **Settings** and paste the following JSON in the **Settings** (Application Settings) field. Replace `https://your-dokploy-domain.com` with your Dokploy base URL and `myorg-name-auth0-saml` with the **exact same provider name** you entered in Dokploy in step 2 (the callback URL path must match), so Dokploy can read email, display name, and other attributes:

```
{
  "audience": "https://your-dokploy-domain.com/saml/metadata",
  "recipient": "https://your-dokploy-domain.com/api/auth/sso/saml2/callback/myorg-name-auth0-saml",
  "destination": "https://your-dokploy-domain.com/api/auth/sso/saml2/callback/myorg-name-auth0-saml",
  "signResponse": true,
  "signAssertion": true,
  "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
  "nameIdentifierProbes": [
    "email"
  ],
  "mappings": {
    "email": "email",
    "displayName": "name",
    "givenName": "given_name",
    "surname": "family_name"
  }
}
```

4. Save.

## [Troubleshooting (SAML)](#troubleshooting-saml)

- **ACS URL mismatch** — Ensure the callback/ACS URL in Auth0 matches exactly what Dokploy provides (including protocol and path).
- **Certificate** — Use the full x509 certificate from Auth0 (PEM format); ensure no extra spaces or line breaks.
- **Entity ID** — The Entity ID in Dokploy must match the Issuer/Entity ID configured in Auth0.