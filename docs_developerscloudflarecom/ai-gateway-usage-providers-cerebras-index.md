---
title: Cerebras · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/index.md
source: llms
fetched_at: 2026-01-24T14:03:05.677959173-03:00
rendered_js: false
word_count: 76
summary: This guide explains how to route inference requests to Cerebras AI models through the Cloudflare AI Gateway using standard or OpenAI-compatible endpoints.
tags:
    - cloudflare-ai-gateway
    - cerebras
    - ai-inference
    - api-integration
    - openai-compatibility
category: configuration
---

[Cerebras](https://inference-docs.cerebras.ai/) offers developers a low-latency solution for AI model inference.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cerebras
```

## Prerequisites

When making requests to Cerebras, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active Cerebras API token.
* The name of the Cerebras model you want to use.

## Examples

### cURL

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cerebras/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer CEREBRAS_TOKEN' \
 --data '{
    "model": "llama3.1-8b",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

## OpenAI-Compatible Endpoint

You can also use the [OpenAI-compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) (`/ai-gateway/usage/chat-completion/`) to access Cerebras models using the OpenAI API schema. To do so, send your requests to:

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions
```

Specify:

```json
{
"model": "cerebras/{model}"
}
```