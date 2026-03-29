---
title: One post tagged with "virtual key management" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/virtual-key-management
source: sitemap
fetched_at: 2026-01-21T19:42:18.14384962-03:00
rendered_js: false
word_count: 42
summary: This document explains how to monitor guardrail performance, list available guardrails, and test guardrail configurations using mock responses within the LiteLLM proxy.
tags:
    - litellm
    - guardrails
    - api-monitoring
    - mock-responses
    - llm-proxy
    - request-validation
category: guide
---

Track guardrail failure rate and if a guardrail is going rogue and failing requests. [Start here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

`/guardrails/list` allows clients to view available guardrails + supported guardrail params

Send `mock_response` to test guardrails without making an LLM call. More info on `mock_response` [here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "hi my email is ishaan@berri.ai"}
    ],
    "mock_response": "This is a mock response",
    "guardrails": ["aporia-pre-guard", "aporia-post-guard"]
  }'
```