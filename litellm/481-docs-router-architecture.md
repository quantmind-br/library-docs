---
title: Router Architecture (Fallbacks / Retries) | liteLLM
url: https://docs.litellm.ai/docs/router_architecture
source: sitemap
fetched_at: 2026-01-21T19:54:16.140961426-03:00
rendered_js: false
word_count: 183
summary: This document describes the high-level architecture and internal request flow of the LiteLLM Router, detailing how requests are processed through fallback and retry mechanisms.
tags:
    - litellm
    - router-architecture
    - request-flow
    - error-handling
    - load-balancing
    - llm-infrastructure
category: concept
---

## High Level architecture[​](#high-level-architecture "Direct link to High Level architecture")

### Request Flow[​](#request-flow "Direct link to Request Flow")

1. **User Sends Request**: The process begins when a user sends a request to the LiteLLM Router endpoint. All unified endpoints (`.completion`, `.embeddings`, etc) are supported by LiteLLM Router.
2. **function\_with\_fallbacks**: The initial request is sent to the `function_with_fallbacks` function. This function wraps the initial request in a try-except block, to handle any exceptions - doing fallbacks if needed. This request is then sent to the `function_with_retries` function.
3. **function\_with\_retries**: The `function_with_retries` function wraps the request in a try-except block and passes the initial request to a base litellm unified function (`litellm.completion`, `litellm.embeddings`, etc) to handle LLM API calling. `function_with_retries` handles any exceptions - doing retries on the model group if needed (i.e. if the request fails, it will retry on an available model within the model group).
4. **litellm.completion**: The `litellm.completion` function is a base function that handles the LLM API calling. It is used by `function_with_retries` to make the actual request to the LLM API.

## Legend[​](#legend "Direct link to Legend")

**model\_group**: A group of LLM API deployments that share the same `model_name`, are part of the same `model_group`, and can be load balanced across.