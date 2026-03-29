---
title: Why Pass-Through Endpoints? | liteLLM
url: https://docs.litellm.ai/docs/pass_through/intro
source: sitemap
fetched_at: 2026-01-21T19:46:53.212379997-03:00
rendered_js: false
word_count: 220
summary: This document explains how LiteLLM's passthrough endpoints function to forward provider-specific requests while providing unified authentication, cost tracking, and centralized logging.
tags:
    - litellm-proxy
    - passthrough-endpoints
    - api-forwarding
    - cost-tracking
    - unified-authentication
    - request-handling
category: guide
---

These endpoints are useful for 2 scenarios:

1. **Migrate existing projects** to litellm proxy. E.g: If you have users already in production with Anthropic's SDK, you just need to change the base url to get cost tracking/logging/budgets/etc.
2. **Use provider-specific endpoints** E.g: If you want to use [Vertex AI's token counting endpoint](https://docs.litellm.ai/docs/pass_through/vertex_ai#count-tokens-api)

## How is your request handled?[​](#how-is-your-request-handled "Direct link to How is your request handled?")

The request is passed through to the provider's endpoint. The response is then passed back to the client. **No translation is done.**

### Request Forwarding Process[​](#request-forwarding-process "Direct link to Request Forwarding Process")

1. **Request Reception**: LiteLLM receives your request at `/provider/endpoint`
2. **Authentication**: Your LiteLLM API key is validated and mapped to the provider's API key
3. **Request Transformation**: Request is reformatted for the target provider's API
4. **Forwarding**: Request is sent to the actual provider endpoint
5. **Response Handling**: Provider response is returned directly to you

### Authentication Flow[​](#authentication-flow "Direct link to Authentication Flow")

**Key Points:**

- Use your **LiteLLM API key** in requests, not the provider's key
- LiteLLM handles the provider authentication internally
- Same authentication works across all passthrough endpoints

### Error Handling[​](#error-handling "Direct link to Error Handling")

**Provider Errors**: Forwarded directly to you with original error codes and messages

**LiteLLM Errors**:

- `401`: Invalid LiteLLM API key
- `404`: Provider or endpoint not supported
- `500`: Internal routing/forwarding errors

### Benefits[​](#benefits "Direct link to Benefits")

- **Unified Authentication**: One API key for all providers
- **Centralized Logging**: All requests logged through LiteLLM
- **Cost Tracking**: Usage tracked across all endpoints
- **Access Control**: Same permissions apply to passthrough endpoints