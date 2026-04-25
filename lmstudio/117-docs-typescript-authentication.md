---
title: Authentication
url: https://lmstudio.ai/docs/typescript/authentication
source: sitemap
fetched_at: 2026-04-07T21:31:36.503243309-03:00
rendered_js: false
word_count: 117
summary: This document explains how to securely authenticate access to the LM Studio API using API Tokens, detailing the recommended method of setting an environment variable or passing it as a function argument.
tags:
    - lm-studio
    - api-token
    - authentication
    - sdk-setup
    - environment-variable
category: guide
---

##### Requires [LM Studio 0.4.0](https://lmstudio.ai/download) or newer.

LM Studio supports API Tokens for authentication, providing a secure and convenient way to access the LM Studio API.

By default, the LM Studio API runs **without enforcing authentication**. For production or shared environments, enable API Token authentication for secure access.

To enable API Token authentication, create tokens and control granular permissions, check [this guide](https://lmstudio.ai/docs/developer/core/authentication) for more details.

## Providing the API Token[](#providing-the-api-token "Link to 'Providing the API Token'")

There are two ways to provide the API Token when creating an instance of `LMStudioClient`:

- **Environment Variable (Recommended)**: Set the `LM_API_TOKEN` environment variable, and the SDK will automatically read it.
- **Function Argument**: Pass the token directly as the `apiToken` parameter in the constructor.