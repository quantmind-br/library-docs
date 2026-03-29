---
title: Guardrails AI | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/guardrails_ai
source: sitemap
fetched_at: 2026-01-21T19:52:13.438736841-03:00
rendered_js: false
word_count: 81
summary: This document provides instructions on integrating Guardrails AI with LiteLLM to implement output validation and manage security checks through configuration and API keys.
tags:
    - guardrails-ai
    - litellm
    - llm-security
    - proxy-server
    - api-gateway
    - configuration
category: tutorial
---

Use Guardrails AI ([guardrailsai.com](https://www.guardrailsai.com/)) to add checks to LLM output.

## Pre-requisites[​](#pre-requisites "Direct link to Pre-requisites")

- Setup Guardrails AI Server. [quick start](https://www.guardrailsai.com/docs/getting_started/guardrails_server)

## Usage[​](#usage "Direct link to Usage")

1. Setup config.yaml

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"guardrails_ai-guard"
litellm_params:
guardrail: guardrails_ai
guard_name:"detect-secrets-guard"# 👈 Guardrail AI guard name
mode:"pre_call"
guardrails_ai_api_input_format:"llmOutput"# 👈 This is the only option that currently works (and it is a default), use it for both pre_call and post_call hooks
api_base: os.environ/GUARDRAILS_AI_API_BASE   # 👈 Guardrails AI API Base. Defaults to "http://0.0.0.0:8000"
```

2. Start LiteLLM Gateway

```
litellm --config config.yaml --detailed_debug
```

3. Test request

[**Langchain, OpenAI SDK Usage Examples**](https://docs.litellm.ai/docs/proxy/proxy/user_keys#request-format)

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "hi my email is ishaan@berri.ai"}
    ],
    "guardrails": ["guardrails_ai-guard"]
  }'
```

## ✨ Control Guardrails per Project (API Key)[​](#-control-guardrails-per-project-api-key "Direct link to ✨ Control Guardrails per Project (API Key)")

Use this to control what guardrails run per project. In this tutorial we only want the following guardrails to run for 1 project (API Key)

- `guardrails`: \["aporia-pre-guard", "aporia-post-guard"]

**Step 1** Create Key with guardrail settings

- /key/generate
- /key/update

```
curl -X POST 'http://0.0.0.0:4000/key/generate' \
    -H 'Authorization: Bearer sk-1234' \
    -H 'Content-Type: application/json' \
    -d '{
            "guardrails": ["guardrails_ai-guard"]
        }
    }'
```

**Step 2** Test it with new key

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
    --header 'Authorization: Bearer sk-jNm1Zar7XfNdZXp49Z1kSQ' \
    --header 'Content-Type: application/json' \
    --data '{
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": "my email is ishaan@berri.ai"
        }
    ]
}'
```