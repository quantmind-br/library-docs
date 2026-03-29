---
title: /responses/compact | liteLLM
url: https://docs.litellm.ai/docs/response_api_compact
source: sitemap
fetched_at: 2026-01-21T19:54:14.835769093-03:00
rendered_js: false
word_count: 7
summary: This document explains how to use the OpenAI /responses/compact endpoint to compress conversation history and optimize token usage.
tags:
    - openai-api
    - conversation-history
    - message-compaction
    - token-optimization
    - data-compression
category: api
---

Compress conversation history using OpenAI's `/responses/compact` endpoint.

```
{
"id":"resp_abc123",
"object":"response.compaction",
"created_at":1734366691,
"output":[
{
"type":"message",
"role":"assistant",
"content":[...]
},
{
"type":"compaction",
"encrypted_content":"..."
}
],
"usage":{
"input_tokens":100,
"output_tokens":50,
"total_tokens":150
}
}
```