---
title: Keycloak | Dokploy
url: https://docs.dokploy.com/docs/core/enterprise/sso/keycloak
source: crawler
fetched_at: 2026-02-14T14:13:02.495658-03:00
rendered_js: true
word_count: 278
summary: This document provides step-by-step instructions for configuring Single Sign-On (SSO) using Keycloak as an OpenID Connect provider for Dokploy. It details the setup process for both platforms, including client credentials, redirect URIs, and troubleshooting tips for common authentication issues.
tags:
    - sso
    - keycloak
    - openid-connect
    - authentication
    - identity-management
    - dokploy
category: configuration
---

Configure SSO with Keycloak

1. Log in to your Keycloak Admin Console.
2. Select your realm (or create one).
3. Go to **Clients** → **Create client**.
4. Set **Client ID** (e.g. `my-client-id`) and **Client type** to **OpenID Connect**.
5. Set **Root URL** to your Dokploy base URL, e.g. `https://your-dokploy-domain.com`.
6. Save.
7. Open the client, set **Access type** to **confidential**, then open the **Credentials** tab and note the **Secret**.
8. From **Realm settings** → **OpenID Endpoint Configuration**, note the **Issuer** (e.g. `https://keycloak.example.com/realms/your-realm`).

<!--THE END-->

1. In Dokploy, go to **Settings** (or **Organization** / **Security** in Enterprise).
2. Enable **SSO** and choose **OpenID Connect**.
3. Enter:
   
   - **Provider**: my-client-id (Unique)
   - **Issuer URL**: your Keycloak realm URL (e.g. `https://keycloak.example.com/realms/your-realm`)
   - **Domain**: the domain users use to authenticate via Keycloak (e.g. your organization domain like `acme.com`), not the Dokploy instance URL
   - **Client ID**: my-client-id
   - **Client Secret**: the secret from the Keycloak client Credentials tab
   - **Scopes**: openid email profile
4. Save.

<!--THE END-->

1. In your Keycloak client, go to **Settings**.
2. Set **Valid redirect URIs** to your Dokploy callback URL, for example:
   
   - `https://your-dokploy-domain.com/api/auth/callback/my-client-id`
3. Set **Valid post logout redirect URIs** to:
   
   - `https://your-dokploy-domain.com`
4. Set **Allowed Origins** to:
   
   - `https://your-dokploy-domain.com`
5. Save changes.

<!--THE END-->

- **Redirect URI mismatch** — Ensure the callback URL in Dokploy matches exactly what is configured in Keycloak (including protocol and path). Use the same **Provider** value in the path (e.g. `.../api/auth/callback/myorg-name-keycloak`).
- **Invalid client** — Double-check Client ID and Client Secret, and that the client is enabled and set to confidential access.
- **Scopes** — Ensure the client is configured to request `openid` and, if required, `email` and `profile`.
- **Attribute mapping** — If user email or name is missing, map Keycloak attributes (e.g. email, preferred\_username) in Dokploy if your setup supports it.

For help with your setup, [contact us](https://dokploy.com/contact).