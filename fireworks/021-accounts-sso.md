---
title: Custom SSO - Fireworks AI Docs
url: https://docs.fireworks.ai/accounts/sso
source: sitemap
fetched_at: 2026-04-27T20:19:25.101566918-03:00
rendered_js: false
word_count: 167
summary: This document outlines the methods and features available for authenticating with Fireworks using Single Sign-On (SSO), detailing support for Google, OpenID Connect (OIDC), and SAML 2.0 providers.
tags:
    - single-sign-on
    - sso
    - oidc
    - saml-2.0
    - jit-provisioning
    - authentication
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks uses SSO as the primary authentication mechanism. Default support includes Google SSO. Enterprise accounts can bring their own identity provider via OpenID Connect (OIDC) or SAML 2.0.

## OpenID Connect (OIDC) Provider

Configure OIDC using firectl.

## SAML 2.0 Provider

Configure SAML 2.0 using firectl.

## Just-In-Time (JIT) User Provisioning

JIT automatically creates user accounts on first SSO sign-in. Enable with the [`--enable-jit-user-provisioning`](https://docs.fireworks.ai/tools-sdks/firectl/commands/identity-provider-create) flag when creating your identity provider.

## Enforce SSO

When enforced, only users with approved tenant domains can access the account. Use the [`--enforce-sso`](https://docs.fireworks.ai/tools-sdks/firectl/commands/identity-provider-create) flag or toggle "Enforce SSO for all users" in the Fireworks console.

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| Invalid `samlResponse` or `relayState` from identity provider | SP-initiated login only is supported | Fireworks does not support IdP-initiated login. See [Understanding SAML](https://developer.okta.com/docs/concepts/saml/#understand-sp-initiated-sign-in-flow) |
| Required String parameter 'RelayState' is not present | SP-initiated login only is supported | Same as above |

> [!info]
> Fireworks currently only supports Service Provider (SP) initiated login flows.
