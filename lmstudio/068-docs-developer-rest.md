---
title: LM Studio API
url: https://lmstudio.ai/docs/developer/rest
source: sitemap
fetched_at: 2026-04-07T21:30:11.63995991-03:00
rendered_js: false
word_count: 170
summary: This document details the REST API provided by LM Studio, highlighting the official v1 endpoints and its compatibility with OpenAI and Anthropic standards. It outlines key features like stateful chats and model management.
tags:
    - rest-api
    - local-inference
    - openai-compatibility
    - anthropic-compatibility
    - v1-api
    - model-management
category: reference
---

LM Studio offers a powerful REST API with first-class support for local inference and model management. In addition to our native API, we provide OpenAI-compatible endpoints ([learn more](https://lmstudio.ai/docs/developer/openai-compat)) and Anthropic-compatible endpoints ([learn more](https://lmstudio.ai/docs/developer/anthropic-compat)).

## What's new[](#whats-new "Link to 'What's new'")

Previously, there was a [v0 REST API](https://lmstudio.ai/docs/developer/rest/endpoints). With LM Studio 0.4.0, we have officially released our native v1 REST API at `/api/v1/*` endpoints and recommend using it.

The v1 REST API includes enhanced features such as:

- [MCP via API](https://lmstudio.ai/docs/developer/core/mcp)
- [Stateful chats](https://lmstudio.ai/docs/developer/rest/stateful-chats)
- [Authentication](https://lmstudio.ai/docs/developer/core/authentication) configuration with API tokens
- Model [download](https://lmstudio.ai/docs/developer/rest/download), [load](https://lmstudio.ai/docs/developer/rest/load) and [unload](https://lmstudio.ai/docs/developer/rest/unload) endpoints

## Supported endpoints[](#supported-endpoints "Link to 'Supported endpoints'")

The following endpoints are available in LM Studio's v1 REST API.

EndpointMethodDocs`/api/v1/chat`POST[Chat](https://lmstudio.ai/docs/developer/rest/chat)`/api/v1/models`GET[List Models](https://lmstudio.ai/docs/developer/rest/list)`/api/v1/models/load`POST[Load](https://lmstudio.ai/docs/developer/rest/load)`/api/v1/models/unload`POST[Unload](https://lmstudio.ai/docs/developer/rest/unload)`/api/v1/models/download`POST[Download](https://lmstudio.ai/docs/developer/rest/download)`/api/v1/models/download/status`GET[Download Status](https://lmstudio.ai/docs/developer/rest/download-status)

## Inference endpoint comparison[](#inference-endpoint-comparison "Link to 'Inference endpoint comparison'")

The table below compares the features of LM Studio's `/api/v1/chat` endpoint with OpenAI-compatible and Anthropic-compatible inference endpoints.

Feature[`/api/v1/chat`](https://lmstudio.ai/docs/developer/rest/chat)[`/v1/responses`](https://lmstudio.ai/docs/developer/openai-compat/responses)[`/v1/chat/completions`](https://lmstudio.ai/docs/developer/openai-compat/chat-completions)[`/v1/messages`](https://lmstudio.ai/docs/developer/anthropic-compat/messages)Streaming✅✅✅✅Stateful chat✅✅❌❌Remote MCPs✅✅❌❌MCPs you have in LM Studio✅✅❌❌Custom tools❌✅✅✅Include assistant messages in the request❌✅✅✅Model load streaming events✅❌❌❌Prompt processing streaming events✅❌❌❌Specify context length in the request✅❌❌❌

* * *

Please report bugs by opening an issue on [Github](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues).