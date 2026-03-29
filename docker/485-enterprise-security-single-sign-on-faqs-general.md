---
title: General
url: https://docs.docker.com/enterprise/security/single-sign-on/faqs/general/
source: llms
fetched_at: 2026-01-24T14:27:07.794429143-03:00
rendered_js: false
word_count: 190
summary: This document provides answers to frequently asked questions about Docker Single Sign-On (SSO) implementation, including supported flows, account management, and configuration requirements.
tags:
    - docker-sso
    - authentication
    - identity-provider
    - saml
    - access-management
category: reference
---

## General SSO FAQs

Table of contents

* * *

## [What SSO flows does Docker support?](#what-sso-flows-does-docker-support)

Docker supports Service Provider Initiated (SP-initiated) SSO flow. Users must sign in to Docker Hub or Docker Desktop to initiate the SSO authentication process.

## [Does Docker SSO support multi-factor authentication?](#does-docker-sso-support-multi-factor-authentication)

When an organization uses SSO, multi-factor authentication is controlled at the identity provider level, not on the Docker platform.

## [Can I retain my Docker ID when using SSO?](#can-i-retain-my-docker-id-when-using-sso)

Users with personal Docker IDs retain ownership of their repositories, images, and assets. When SSO is enforced, existing accounts with company domain emails are connected to the organization. Users signing in without existing accounts automatically have new accounts and Docker IDs created.

## [Are there any firewall rules required for SSO configuration?](#are-there-any-firewall-rules-required-for-sso-configuration)

No specific firewall rules are required as long as `login.docker.com` is accessible. This domain is commonly accessible by default, but some organizations may need to allow it in their firewall settings if SSO setup encounters issues.

## [Does Docker use my IdP's default session timeout?](#does-docker-use-my-idps-default-session-timeout)

Yes, Docker supports your IdP's session timeout using a custom `dockerSessionMinutes` SAML attribute instead of the standard `SessionNotOnOrAfter` element. See [SSO attributes](https://docs.docker.com/enterprise/security/provisioning/#sso-attributes) for more information.