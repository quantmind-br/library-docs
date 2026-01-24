---
title: Service API token · Cloudflare AI Search docs
url: https://developers.cloudflare.com/ai-search/configuration/service-api-token/index.md
source: llms
fetched_at: 2026-01-24T14:00:26.977908627-03:00
rendered_js: false
word_count: 502
summary: This document explains the purpose and lifecycle of service API tokens in Cloudflare AI Search, detailing how they differ from standard API tokens and how to manage them via the dashboard or API.
tags:
    - cloudflare-ai-search
    - api-tokens
    - service-tokens
    - authentication
    - access-management
    - cloud-security
category: concept
---

A service API token grants AI Search permission to access and configure resources in your Cloudflare account. This token is different from API tokens you use to interact with your AI Search instance.

Beta

Service API tokens are required during the AI Search beta. This requirement may change in future releases.

## What is a service API token

When you create an AI Search instance, it needs to interact with other Cloudflare services on your behalf, such as [R2](https://developers.cloudflare.com/r2/), [Vectorize](https://developers.cloudflare.com/vectorize/), and [Workers AI](https://developers.cloudflare.com/workers-ai/). The service API token authorizes AI Search to perform these operations. Without it, AI Search cannot index your data or respond to queries.

## Service API token vs. AI Search API token

AI Search uses two types of API tokens for different purposes:

| Token type | Purpose | Who uses it | When to create |
| - | - | - | - |
| Service API token | Grants AI Search permission to access R2, Vectorize, and Workers AI | AI Search (internal) | Once per account, during first instance creation |
| AI Search API token | Authenticates your requests to query or manage AI Search instances | You (external) | When calling the AI Search REST API |

The **service API token** is used internally by AI Search to perform background operations like indexing your content and generating responses. You create it once and AI Search uses it automatically.

The **AI Search API token** is a standard [Cloudflare API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) that you create with AI Search permissions. You use this token to authenticate REST API requests, such as creating instances, updating configuration, or querying your AI Search.

## How it works

When you create an AI Search instance via the [dashboard](https://developers.cloudflare.com/ai-search/get-started/dashboard/), the service API token is created automatically as part of the setup flow.

When you create an instance via the [API](https://developers.cloudflare.com/ai-search/get-started/api/), you must create and register the service API token manually before creating your instance.

Once registered, the service API token is stored securely and reused across all AI Search instances in your account. You do not need to create a new token for each instance.

## Token lifecycle

The service API token remains active for as long as you have AI Search instances that depend on it.

Warning

Do not delete your service API token. If you revoke or delete the token, your AI Search instances will lose access to the underlying resources and stop functioning.

If you need a new service API token, you can create one via the dashboard or the API.

### Dashboard

1. Go to an existing AI Search instance in the [Cloudflare dashboard](https://dash.cloudflare.com/?to=/:account/ai/ai-search).
2. Select **Settings**.
3. Under **General**, find **Service API Token** and select the edit icon.
4. Select **Create a new token**.
5. Select **Save**.

### API

Follow steps 1-4 in the [API guide](https://developers.cloudflare.com/ai-search/get-started/api/) to create and register a new token programmatically.

## View registered tokens

You can view the service API tokens registered with AI Search in your account using the [List tokens API](https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens/methods/list/). Replace `<API_TOKEN>` with an API token that has AI Search read permissions.

```bash
curl https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/tokens \
  -H "Authorization: Bearer <API_TOKEN>"
```