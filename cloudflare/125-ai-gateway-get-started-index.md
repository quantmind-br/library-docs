---
title: Getting started · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/get-started/index.md
source: llms
fetched_at: 2026-01-24T15:07:08.817188447-03:00
rendered_js: false
word_count: 429
summary: This guide provides instructions for setting up and configuring a Cloudflare AI Gateway through the dashboard or API, covering authentication and integration options.
tags:
    - cloudflare-ai-gateway
    - ai-integration
    - authentication
    - api-configuration
    - openai-compatibility
    - gateway-management
category: guide
---

In this guide, you will learn how to create and use your first AI Gateway.

* Dashboard

  [Go to **AI Gateway**](https://dash.cloudflare.com/?to=/:account/ai/ai-gateway)

  1. Log into the [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account.
  2. Go to **AI** > **AI Gateway**.
  3. Select **Create Gateway**.
  4. Enter your **Gateway name**. Note: Gateway name has a 64 character limit.
  5. Select **Create**.

* API

  To set up an AI Gateway using the API:

  1. [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the following permissions:

     * `AI Gateway - Read`
     * `AI Gateway - Edit`

  2. Get your [Account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).

  3. Using that API token and Account ID, send a [`POST` request](https://developers.cloudflare.com/api/resources/ai_gateway/methods/create/) to the Cloudflare API.

### Authenticated gateway 🔒

When you enable authentication on a gateway, each request is required to include a valid Cloudflare API token, adding an extra layer of security. We recommend using an authenticated gateway to prevent unauthorized access. [Learn more](https://developers.cloudflare.com/ai-gateway/configuration/authentication/).

## Provider Authentication

Authenticate with your upstream AI provider using one of the following options:

* **Unified Billing:** Use the AI Gateway billing to pay for and authenticate your inference requests. Refer to [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).
* **BYOK (Store Keys):** Store your own provider API Keys with Cloudflare, and AI Gateway will include them at runtime. Refer to [BYOK](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).
* **Request headers:** Include your provider API Key in the request headers as you normally would (for example, `Authorization: Bearer <OPENAI_API_KEY>`).

## Integration Options

### Unified API Endpoint

OpenAI Compatible Recommended

The easiest way to get started with AI Gateway is through our OpenAI-compatible `/chat/completions` endpoint. This allows you to use existing OpenAI SDKs and tools with minimal code changes while gaining access to multiple AI providers.

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_name}/compat/chat/completions`

**Key benefits:**

* Drop-in replacement for OpenAI API, works with existing OpenAI SDKs and other OpenAI compliant clients
* Switch between providers by changing the `model` parameter
* Dynamic Routing - Define complex routing scenarios requiring conditional logic, conduct A/B tests, set rate / budget limits, etc

#### Example:

Make a request to

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIGZpbGw9IiMwMDAwMDAiIHdpZHRoPSI2NHB4IiBoZWlnaHQ9IjY0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgcm9sZT0iaW1nIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjx0aXRsZT5PcGVuQUkgaWNvbjwvdGl0bGU+PHBhdGggZD0iTTIyLjI4MTkgOS44MjExYTUuOTg0NyA1Ljk4NDcgMCAwIDAtLjUxNTctNC45MTA4IDYuMDQ2MiA2LjA0NjIgMCAwIDAtNi41MDk4LTIuOUE2LjA2NTEgNi4wNjUxIDAgMCAwIDQuOTgwNyA0LjE4MThhNS45ODQ3IDUuOTg0NyAwIDAgMC0zLjk5NzcgMi45IDYuMDQ2MiA2LjA0NjIgMCAwIDAgLjc0MjcgNy4wOTY2IDUuOTggNS45OCAwIDAgMCAuNTExIDQuOTEwNyA2LjA1MSA2LjA1MSAwIDAgMCA2LjUxNDYgMi45MDAxQTUuOTg0NyA1Ljk4NDcgMCAwIDAgMTMuMjU5OSAyNGE2LjA1NTcgNi4wNTU3IDAgMCAwIDUuNzcxOC00LjIwNTggNS45ODk0IDUuOTg5NCAwIDAgMCAzLjk5NzctMi45MDAxIDYuMDU1NyA2LjA1NTcgMCAwIDAtLjc0NzUtNy4wNzI5em0tOS4wMjIgMTIuNjA4MWE0LjQ3NTUgNC40NzU1IDAgMCAxLTIuODc2NC0xLjA0MDhsLjE0MTktLjA4MDQgNC43NzgzLTIuNzU4MmEuNzk0OC43OTQ4IDAgMCAwIC4zOTI3LS42ODEzdi02LjczNjlsMi4wMiAxLjE2ODZhLjA3MS4wNzEgMCAwIDEgLjAzOC4wNTJ2NS41ODI2YTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0NSA0LjQ5NDR6bS05LjY2MDctNC4xMjU0YTQuNDcwOCA0LjQ3MDggMCAwIDEtLjUzNDYtMy4wMTM3bC4xNDIuMDg1MiA0Ljc4MyAyLjc1ODJhLjc3MTIuNzcxMiAwIDAgMCAuNzgwNiAwbDUuODQyOC0zLjM2ODV2Mi4zMzI0YS4wODA0LjA4MDQgMCAwIDEtLjAzMzIuMDYxNUw5Ljc0IDE5Ljk1MDJhNC40OTkyIDQuNDk5MiAwIDAgMS02LjE0MDgtMS42NDY0ek0yLjM0MDggNy44OTU2YTQuNDg1IDQuNDg1IDAgMCAxIDIuMzY1NS0xLjk3MjhWMTEuNmEuNzY2NC43NjY0IDAgMCAwIC4zODc5LjY3NjVsNS44MTQ0IDMuMzU0My0yLjAyMDEgMS4xNjg1YS4wNzU3LjA3NTcgMCAwIDEtLjA3MSAwbC00LjgzMDMtMi43ODY1QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQwOCA3Ljg3MnptMTYuNTk2MyAzLjg1NThMMTMuMTAzOCA4LjM2NCAxNS4xMTkyIDcuMmEuMDc1Ny4wNzU3IDAgMCAxIC4wNzEgMGw0LjgzMDMgMi43OTEzYTQuNDk0NCA0LjQ5NDQgMCAwIDEtLjY3NjUgOC4xMDQydi01LjY3NzJhLjc5Ljc5IDAgMCAwLS40MDctLjY2N3ptMi4wMTA3LTMuMDIzMWwtLjE0Mi0uMDg1Mi00Ljc3MzUtMi43ODE4YS43NzU5Ljc3NTkgMCAwIDAtLjc4NTQgMEw5LjQwOSA5LjIyOTdWNi44OTc0YS4wNjYyLjA2NjIgMCAwIDEgLjAyODQtLjA2MTVsNC44MzAzLTIuNzg2NmE0LjQ5OTIgNC40OTkyIDAgMCAxIDYuNjgwMiA0LjY2ek04LjMwNjUgMTIuODYzbC0yLjAyLTEuMTYzOGEuMDgwNC4wODA0IDAgMCAxLS4wMzgtLjA1NjdWNi4wNzQyYTQuNDk5MiA0LjQ5OTIgMCAwIDEgNy4zNzU3LTMuNDUzN2wtLjE0Mi4wODA1TDguNzA0IDUuNDU5YS43OTQ4Ljc5NDggMCAwIDAtLjM5MjcuNjgxM3ptMS4wOTc2LTIuMzY1NGwyLjYwMi0xLjQ5OTggMi42MDY5IDEuNDk5OHYyLjk5OTRsLTIuNTk3NCAxLjQ5OTctMi42MDY3LTEuNDk5N1oiLz48L3N2Zz4=) OpenAI

using

OpenAI JS SDK

with

Stored Key (BYOK)

Refer to [Unified API](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) to learn more about OpenAI compatibility.

### Provider-specific endpoints

For direct integration with specific AI providers, use dedicated endpoints that maintain the original provider's API schema while adding AI Gateway features.

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/{provider}
```

**Available providers:**

* [OpenAI](https://developers.cloudflare.com/ai-gateway/usage/providers/openai/) - GPT models and embeddings
* [Anthropic](https://developers.cloudflare.com/ai-gateway/usage/providers/anthropic/) - Claude models
* [Google AI Studio](https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/) - Gemini models
* [Workers AI](https://developers.cloudflare.com/ai-gateway/usage/providers/workersai/) - Cloudflare's inference platform
* [AWS Bedrock](https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/) - Amazon's managed AI service
* [Azure OpenAI](https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/) - Microsoft's OpenAI service
* [and more...](https://developers.cloudflare.com/ai-gateway/usage/providers/)

## Next steps

* Learn more about [caching](https://developers.cloudflare.com/ai-gateway/features/caching/) for faster requests and cost savings and [rate limiting](https://developers.cloudflare.com/ai-gateway/features/rate-limiting/) to control how your application scales.
* Explore how to specify model or provider [fallbacks, ratelimits, A/B tests](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/) for resiliency.
* Learn how to use low-cost, open source models on [Workers AI](https://developers.cloudflare.com/ai-gateway/usage/providers/workersai/) - our AI inference service.