---
title: v1.68.0-stable
url: https://docs.litellm.ai/release_notes/v1.68.0-stable
source: sitemap
fetched_at: 2026-01-21T19:43:37.170913026-03:00
rendered_js: false
word_count: 777
summary: This document provides the release notes for LiteLLM version 1.68.0-stable, detailing new features such as Bedrock Knowledge Base support and improved multi-instance rate limiting. It also covers updates to various model providers, API endpoints, and spend tracking functionality.
tags:
    - litellm-release
    - bedrock-knowledge-base
    - rate-limiting
    - llm-proxy
    - model-support
    - api-updates
    - vector-stores
    - spend-tracking
category: reference
---

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.68.0-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

LiteLLM v1.68.0-stable will be live soon. Here are the key highlights of this release:

- **Bedrock Knowledge Base**: You can now call query your Bedrock Knowledge Base with all LiteLLM models via `/chat/completion` or `/responses` API.
- **Rate Limits**: This release brings accurate rate limiting across multiple instances, reducing spillover to at most 10 additional requests in high traffic.
- **Meta Llama API**: Added support for Meta Llama API [Get Started](https://docs.litellm.ai/docs/providers/meta_llama)
- **LlamaFile**: Added support for LlamaFile [Get Started](https://docs.litellm.ai/docs/providers/llamafile)

## Bedrock Knowledge Base (Vector Store)[​](#bedrock-knowledge-base-vector-store "Direct link to Bedrock Knowledge Base (Vector Store)")

This release adds support for Bedrock vector stores (knowledge bases) in LiteLLM. With this update, you can:

- Use Bedrock vector stores in the OpenAI /chat/completions spec with all LiteLLM supported models.
- View all available vector stores through the LiteLLM UI or API.
- Configure vector stores to be always active for specific models.
- Track vector store usage in LiteLLM Logs.

For the next release we plan on allowing you to set key, user, team, org permissions for vector stores.

[Read more here](https://docs.litellm.ai/docs/completion/knowledgebase)

## Rate Limiting[​](#rate-limiting "Direct link to Rate Limiting")

This release brings accurate multi-instance rate limiting across keys/users/teams. Outlining key engineering changes below:

- **Change**: Instances now increment cache value instead of setting it. To avoid calling Redis on each request, this is synced every 0.01s.
- **Accuracy**: In testing, we saw a maximum spill over from expected of 10 requests, in high traffic (100 RPS, 3 instances), vs. current 189 request spillover
- **Performance**: Our load tests show this to reduce median response time by 100ms in high traffic

This is currently behind a feature flag, and we plan to have this be the default by next week. To enable this today, just add this environment variable:

```
export LITELLM_RATE_LIMIT_ACCURACY=true
```

[Read more here](https://docs.litellm.ai/docs/proxy/users#beta-multi-instance-rate-limiting)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **Gemini ([VertexAI](https://docs.litellm.ai/docs/providers/vertex#usage-with-litellm-proxy-server) + [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini))**
  
  - Handle more json schema - openapi schema conversion edge cases [PR](https://github.com/BerriAI/litellm/pull/10351)
  - Tool calls - return ‘finish\_reason=“tool\_calls”’ on gemini tool calling response [PR](https://github.com/BerriAI/litellm/pull/10485)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex#metallama-api)
  
  - Meta/llama-4 model support [PR](https://github.com/BerriAI/litellm/pull/10492)
  - Meta/llama3 - handle tool call result in content [PR](https://github.com/BerriAI/litellm/pull/10492)
  - Meta/* - return ‘finish\_reason=“tool\_calls”’ on tool calling response [PR](https://github.com/BerriAI/litellm/pull/10492)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock#litellm-proxy-usage)
  
  - [Image Generation](https://docs.litellm.ai/docs/providers/bedrock#image-generation) - Support new ‘stable-image-core’ models - [PR](https://github.com/BerriAI/litellm/pull/10351)
  - [Knowledge Bases](https://docs.litellm.ai/docs/completion/knowledgebase) - support using Bedrock knowledge bases with `/chat/completions` [PR](https://github.com/BerriAI/litellm/pull/10413)
  - [Anthropic](https://docs.litellm.ai/docs/providers/bedrock#litellm-proxy-usage) - add ‘supports\_pdf\_input’ for claude-3.7-bedrock models [PR](https://github.com/BerriAI/litellm/pull/9917), [Get Started](https://docs.litellm.ai/docs/completion/document_understanding#checking-if-a-model-supports-pdf-input)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Support OPENAI\_BASE\_URL in addition to OPENAI\_API\_BASE [PR](https://github.com/BerriAI/litellm/pull/10423)
  - Correctly re-raise 504 timeout errors [PR](https://github.com/BerriAI/litellm/pull/10462)
  - Native Gpt-4o-mini-tts support [PR](https://github.com/BerriAI/litellm/pull/10462)
- 🆕 [**Meta Llama API**](https://docs.litellm.ai/docs/providers/meta_llama) provider [PR](https://github.com/BerriAI/litellm/pull/10451)
- 🆕 [**LlamaFile**](https://docs.litellm.ai/docs/providers/llamafile) provider [PR](https://github.com/BerriAI/litellm/pull/10482)

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

- [**Response API**](https://docs.litellm.ai/docs/response_api)
  
  - Fix for handling multi turn sessions [PR](https://github.com/BerriAI/litellm/pull/10415)
- [**Embeddings**](https://docs.litellm.ai/docs/embedding/supported_embedding)
  
  - Caching fixes - [PR](https://github.com/BerriAI/litellm/pull/10424)
    
    - handle str -&gt; list cache
    - Return usage tokens for cache hit
    - Combine usage tokens on partial cache hits
- 🆕 [**Vector Stores**](https://docs.litellm.ai/docs/completion/knowledgebase)
  
  - Allow defining Vector Store Configs - [PR](https://github.com/BerriAI/litellm/pull/10448)
  - New StandardLoggingPayload field for requests made when a vector store is used - [PR](https://github.com/BerriAI/litellm/pull/10509)
  - Show Vector Store / KB Request on LiteLLM Logs Page - [PR](https://github.com/BerriAI/litellm/pull/10514)
  - Allow using vector store in OpenAI API spec with tools - [PR](https://github.com/BerriAI/litellm/pull/10516)
- [**MCP**](https://docs.litellm.ai/docs/mcp)
  
  - Ensure Non-Admin virtual keys can access /mcp routes - [PR](https://github.com/BerriAI/litellm/pull/10473)
    
    **Note:** Currently, all Virtual Keys are able to access the MCP endpoints. We are working on a feature to allow restricting MCP access by keys/teams/users/orgs. Follow [here](https://github.com/BerriAI/litellm/discussions/9891) for updates.
- **Moderations**
  
  - Add logging callback support for `/moderations` API - [PR](https://github.com/BerriAI/litellm/pull/10390)

## Spend Tracking / Budget Improvements[​](#spend-tracking--budget-improvements "Direct link to Spend Tracking / Budget Improvements")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - [computer-use-preview](https://docs.litellm.ai/docs/providers/openai/responses_api#computer-use) cost tracking / pricing [PR](https://github.com/BerriAI/litellm/pull/10422)
  - [gpt-4o-mini-tts](https://docs.litellm.ai/docs/providers/openai/text_to_speech) input cost tracking - [PR](https://github.com/BerriAI/litellm/pull/10462)
- [**Fireworks AI**](https://docs.litellm.ai/docs/providers/fireworks_ai) - pricing updates - new `0-4b` model pricing tier + llama4 model pricing
- [**Budgets**](https://docs.litellm.ai/docs/proxy/users#set-budgets)
  
  - [Budget resets](https://docs.litellm.ai/docs/proxy/users#reset-budgets) now happen as start of day/week/month - [PR](https://github.com/BerriAI/litellm/pull/10333)
  - Trigger [Soft Budget Alerts](https://docs.litellm.ai/docs/proxy/alerting#soft-budget-alerts-for-virtual-keys) When Key Crosses Threshold - [PR](https://github.com/BerriAI/litellm/pull/10491)
- [**Token Counting**](https://docs.litellm.ai/docs/completion/token_usage#3-token_counter)
  
  - Rewrite of token\_counter() function to handle to prevent undercounting tokens - [PR](https://github.com/BerriAI/litellm/pull/10409)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Virtual Keys**
  
  - Fix filtering on key alias - [PR](https://github.com/BerriAI/litellm/pull/10455)
  - Support global filtering on keys - [PR](https://github.com/BerriAI/litellm/pull/10455)
  - Pagination - fix clicking on next/back buttons on table - [PR](https://github.com/BerriAI/litellm/pull/10528)
- **Models**
  
  - Triton - Support adding model/provider on UI - [PR](https://github.com/BerriAI/litellm/pull/10456)
  - VertexAI - Fix adding vertex models with reusable credentials - [PR](https://github.com/BerriAI/litellm/pull/10528)
  - LLM Credentials - show existing credentials for easy editing - [PR](https://github.com/BerriAI/litellm/pull/10519)
- **Teams**
  
  - Allow reassigning team to other org - [PR](https://github.com/BerriAI/litellm/pull/10527)
- **Organizations**
  
  - Fix showing org budget on table - [PR](https://github.com/BerriAI/litellm/pull/10528)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- [**Langsmith**](https://docs.litellm.ai/docs/observability/langsmith_integration)
  
  - Respect [langsmith\_batch\_size](https://docs.litellm.ai/docs/observability/langsmith_integration#local-testing---control-batch-size) param - [PR](https://github.com/BerriAI/litellm/pull/10411)

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- [**Redis**](https://docs.litellm.ai/docs/proxy/caching)
  
  - Ensure all redis queues are periodically flushed, this fixes an issue where redis queue size was growing indefinitely when request tags were used - [PR](https://github.com/BerriAI/litellm/pull/10393)
- [**Rate Limits**](https://docs.litellm.ai/docs/proxy/users#set-rate-limit)
  
  - [Multi-instance rate limiting](https://docs.litellm.ai/docs/proxy/users#beta-multi-instance-rate-limiting) support across keys/teams/users/customers - [PR](https://github.com/BerriAI/litellm/pull/10458), [PR](https://github.com/BerriAI/litellm/pull/10497), [PR](https://github.com/BerriAI/litellm/pull/10500)
- [**Azure OpenAI OIDC**](https://docs.litellm.ai/docs/providers/azure#entra-id---use-azure_ad_token)
  
  - allow using litellm defined params for [OIDC Auth](https://docs.litellm.ai/docs/providers/azure#entra-id---use-azure_ad_token) - [PR](https://github.com/BerriAI/litellm/pull/10394)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Security**
  
  - Allow [blocking web crawlers](https://docs.litellm.ai/docs/proxy/enterprise#blocking-web-crawlers) - [PR](https://github.com/BerriAI/litellm/pull/10420)
- **Auth**
  
  - Support [`x-litellm-api-key` header param by default](https://docs.litellm.ai/docs/pass_through/vertex_ai#use-with-virtual-keys), this fixes an issue from the prior release where `x-litellm-api-key` was not being used on vertex ai passthrough requests - [PR](https://github.com/BerriAI/litellm/pull/10392)
  - Allow key at max budget to call non-llm api endpoints - [PR](https://github.com/BerriAI/litellm/pull/10392)
- 🆕 **[Python Client Library](https://docs.litellm.ai/docs/proxy/management_cli) for LiteLLM Proxy management endpoints**
  
  - Initial PR - [PR](https://github.com/BerriAI/litellm/pull/10445)
  - Support for doing HTTP requests - [PR](https://github.com/BerriAI/litellm/pull/10452)
- **Dependencies**
  
  - Don’t require uvloop for windows - [PR](https://github.com/BerriAI/litellm/pull/10483)