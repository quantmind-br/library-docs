---
title: Authentication
url: https://lmstudio.ai/docs/python/getting-started/authentication
source: sitemap
fetched_at: 2026-04-07T21:30:58.797197158-03:00
rendered_js: false
word_count: 108
summary: This document explains how to secure access to the LM Studio API by implementing API Token authentication for use in production or shared environments.
tags:
    - api-token
    - lm-studio
    - authentication
    - environment-variable
    - secure-access
category: guide
---

##### Requires [LM Studio 0.4.0](https://lmstudio.ai/download) or newer.

LM Studio supports API Tokens for authentication, providing a secure and convenient way to access the LM Studio API.

By default, the LM Studio API runs **without enforcing authentication**. For production or shared environments, enable API Token authentication for secure access.

To enable API Token authentication, create tokens and control granular permissions, check [this guide](https://lmstudio.ai/docs/developer/core/authentication) for more details.

## Providing the API Token[](#providing-the-api-token "Link to 'Providing the API Token'")

The API Token can be provided in two ways:

- **Environment Variable (Recommended)**: Set the `LM_API_TOKEN` environment variable, and the SDK will automatically read it.
- **Function Argument**: Pass the token directly as the `api_token` parameter.