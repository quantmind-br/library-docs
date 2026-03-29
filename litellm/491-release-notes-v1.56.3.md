---
title: v1.56.3
url: https://docs.litellm.ai/release_notes/v1.56.3
source: sitemap
fetched_at: 2026-01-21T19:43:12.504949527-03:00
rendered_js: false
word_count: 139
summary: This document details recent updates and new features for LiteLLM, including guardrail tracing, API endpoints for guardrail listing, and support for new language models.
tags:
    - litellm
    - guardrails
    - api-updates
    - model-support
    - logging
    - key-management
category: other
---

`guardrails`, `logging`, `virtual key management`, `new models`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Features[​](#new-features "Direct link to New Features")

### ✨ Log Guardrail Traces[​](#-log-guardrail-traces "Direct link to ✨ Log Guardrail Traces")

Track guardrail failure rate and if a guardrail is going rogue and failing requests. [Start here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

#### Traced Guardrail Success[​](#traced-guardrail-success "Direct link to Traced Guardrail Success")

#### Traced Guardrail Failure[​](#traced-guardrail-failure "Direct link to Traced Guardrail Failure")

### `/guardrails/list`[​](#guardrailslist "Direct link to guardrailslist")

`/guardrails/list` allows clients to view available guardrails + supported guardrail params

```
curl -X GET 'http://0.0.0.0:4000/guardrails/list'
```

Expected response

```
{
"guardrails":[
{
"guardrail_name":"aporia-post-guard",
"guardrail_info":{
"params":[
{
"name":"toxicity_score",
"type":"float",
"description":"Score between 0-1 indicating content toxicity level"
},
{
"name":"pii_detection",
"type":"boolean"
}
]
}
}
]
}
```

### ✨ Guardrails with Mock LLM[​](#-guardrails-with-mock-llm "Direct link to ✨ Guardrails with Mock LLM")

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

### Assign Keys to Users[​](#assign-keys-to-users "Direct link to Assign Keys to Users")

You can now assign keys to users via Proxy UI

## New Models[​](#new-models "Direct link to New Models")

- `openrouter/openai/o1`
- `vertex_ai/mistral-large@2411`

## Fixes[​](#fixes "Direct link to Fixes")

- Fix `vertex_ai/` mistral model pricing: [https://github.com/BerriAI/litellm/pull/7345](https://github.com/BerriAI/litellm/pull/7345)
- Missing model\_group field in logs for aspeech call types [https://github.com/BerriAI/litellm/pull/7392](https://github.com/BerriAI/litellm/pull/7392)

<!--THE END-->

- [New Features](#new-features)
  
  - [✨ Log Guardrail Traces](#-log-guardrail-traces)
  - [`/guardrails/list`](#guardrailslist)
  - [✨ Guardrails with Mock LLM](#-guardrails-with-mock-llm)
  - [Assign Keys to Users](#assign-keys-to-users)
- [New Models](#new-models)
- [Fixes](#fixes)