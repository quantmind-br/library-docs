---
title: Life of a Request | liteLLM
url: https://docs.litellm.ai/docs/proxy/architecture
source: sitemap
fetched_at: 2026-01-21T19:51:13.829660994-03:00
rendered_js: false
word_count: 268
summary: This document outlines the high-level architecture and request flow of the LiteLLM Proxy Server, detailing the sequence of authentication, rate limiting, routing, and asynchronous post-request processing.
tags:
    - litellm
    - proxy-server
    - architecture
    - request-flow
    - rate-limiting
    - llm-routing
    - authentication
category: concept
---

## High Level architecture[​](#high-level-architecture "Direct link to High Level architecture")

### Request Flow[​](#request-flow "Direct link to Request Flow")

1. **User Sends Request**: The process begins when a user sends a request to the LiteLLM Proxy Server (Gateway).
2. [**Virtual Keys**](https://docs.litellm.ai/docs/virtual_keys): At this stage the `Bearer` token in the request is checked to ensure it is valid and under it's budget. [Here is the list of checks that run for each request](https://github.com/BerriAI/litellm/blob/ba41a72f92a9abf1d659a87ec880e8e319f87481/litellm/proxy/auth/auth_checks.py#L43)
   
   - 2.1 Check if the Virtual Key exists in Redis Cache or In Memory Cache
   - 2.2 **If not in Cache**, Lookup Virtual Key in DB
3. **Rate Limiting**: The [MaxParallelRequestsHandler](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/hooks/parallel_request_limiter.py) checks the **rate limit (rpm/tpm)** for the the following components:
   
   - Global Server Rate Limit
   - Virtual Key Rate Limit
   - User Rate Limit
   - Team Limit
4. **LiteLLM `proxy_server.py`** : Contains the `/chat/completions` and `/embeddings` endpoints. Requests to these endpoints are sent through the LiteLLM Router
5. [**LiteLLM Router**](https://docs.litellm.ai/docs/routing): The LiteLLM Router handles Load balancing, Fallbacks, Retries for LLM API deployments.
6. [**litellm.completion() / litellm.embedding()**:](https://docs.litellm.ai/docs/index#litellm-python-sdk) The litellm Python SDK is used to call the LLM in the OpenAI API format (Translation and parameter mapping)
7. **Post-Request Processing**: After the response is sent back to the client, the following **asynchronous** tasks are performed:
   
   - [Logging to Lunary, MLflow, LangFuse or other logging destinations](https://docs.litellm.ai/docs/proxy/logging)
   - The [MaxParallelRequestsHandler](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/hooks/parallel_request_limiter.py) updates the rpm/tpm usage for the
     
     - Global Server Rate Limit
     - Virtual Key Rate Limit
     - User Rate Limit
     - Team Limit
   - The `_ProxyDBLogger` updates spend / usage in the LiteLLM database. [Here is everything tracked in the DB per request](https://github.com/BerriAI/litellm/blob/ba41a72f92a9abf1d659a87ec880e8e319f87481/schema.prisma#L172)

## Frequently Asked Questions[​](#frequently-asked-questions "Direct link to Frequently Asked Questions")

1. Is a db transaction tied to the lifecycle of request?
   
   - No, a db transaction is not tied to the lifecycle of a request.
   - The check if a virtual key is valid relies on a DB read if it's not in cache.
   - All other DB transactions are async in background tasks