---
title: Arize Phoenix Prompt Management | liteLLM
url: https://docs.litellm.ai/docs/proxy/arize_phoenix_prompts
source: sitemap
fetched_at: 2026-01-21T19:51:14.398541454-03:00
rendered_js: false
word_count: 94
summary: This document provides instructions for integrating Arize Phoenix prompt management with the LiteLLM SDK and Proxy, covering setup, configuration, and variable templating.
tags:
    - arize-phoenix
    - litellm
    - prompt-management
    - python-sdk
    - llm-proxy
    - prompt-templates
category: guide
---

Use prompt versions from [Arize Phoenix](https://phoenix.arize.com/) with LiteLLM SDK and Proxy.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### SDK[​](#sdk "Direct link to SDK")

```
import litellm

response = litellm.completion(
    model="gpt-4o",
    prompt_id="UHJvbXB0VmVyc2lvbjox",
    prompt_integration="arize_phoenix",
    api_key="your-arize-phoenix-token",
    api_base="https://app.phoenix.arize.com/s/your-workspace",
    prompt_variables={"question":"What is AI?"},
)
```

### Proxy[​](#proxy "Direct link to Proxy")

**1. Add prompt to config**

```
prompts:
-prompt_id:"simple_prompt"
litellm_params:
prompt_id:"UHJvbXB0VmVyc2lvbjox"
prompt_integration:"arize_phoenix"
api_base: https://app.phoenix.arize.com/s/your-workspace
api_key: os.environ/PHOENIX_API_KEY
ignore_prompt_manager_model:true# optional: use model from config instead
ignore_prompt_manager_optional_params:true# optional: ignore temp, max_tokens from prompt
```

**2. Make request**

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-1234' \
  -d '{
    "model": "gpt-3.5-turbo",
    "prompt_id": "simple_prompt",
    "prompt_variables": {
      "question": "Explain quantum computing"
    }
  }'
```

## Configuration[​](#configuration "Direct link to Configuration")

### Get Arize Phoenix Credentials[​](#get-arize-phoenix-credentials "Direct link to Get Arize Phoenix Credentials")

1. **API Token**: Get from [Arize Phoenix Settings](https://app.phoenix.arize.com/)
2. **Workspace URL**: `https://app.phoenix.arize.com/s/{your-workspace}`
3. **Prompt ID**: Found in prompt version URL

**Set environment variable**:

```
export PHOENIX_API_KEY="your-token"
```

### SDK + PROXY Options[​](#sdk--proxy-options "Direct link to SDK + PROXY Options")

ParameterRequiredDescription`prompt_id`YesArize Phoenix prompt version ID`prompt_integration`YesSet to `"arize_phoenix"``api_base`YesWorkspace URL`api_key`YesAccess token`prompt_variables`NoVariables for template

### Proxy-only Options[​](#proxy-only-options "Direct link to Proxy-only Options")

ParameterDescription`ignore_prompt_manager_model`Use config model instead of prompt's model`ignore_prompt_manager_optional_params`Ignore temperature, max\_tokens from prompt

## Variable Templates[​](#variable-templates "Direct link to Variable Templates")

Arize Phoenix uses Mustache/Handlebars syntax:

```
# Template: "Hello {{name}}, question: {{question}}"
prompt_variables ={
"name":"Alice",
"question":"What is ML?"
}
# Result: "Hello Alice, question: What is ML?"
```

## Combine with Additional Messages[​](#combine-with-additional-messages "Direct link to Combine with Additional Messages")

```
response = litellm.completion(
    model="gpt-4o",
    prompt_id="UHJvbXB0VmVyc2lvbjox",
    prompt_integration="arize_phoenix",
    api_base="https://app.phoenix.arize.com/s/your-workspace",
    prompt_variables={"question":"Explain AI"},
    messages=[
{"role":"user","content":"Keep it under 50 words"}
]
)
```

## Error Handling[​](#error-handling "Direct link to Error Handling")

```
try:
    response = litellm.completion(
        model="gpt-4o",
        prompt_id="invalid-id",
        prompt_integration="arize_phoenix",
        api_base="https://app.phoenix.arize.com/s/workspace"
)
except Exception as e:
print(f"Error: {e}")
# 404: Prompt not found
# 401: Invalid credentials
# 403: Access denied
```

## Support[​](#support "Direct link to Support")

- [LiteLLM GitHub Issues](https://github.com/BerriAI/litellm/issues)
- [Arize Phoenix Docs](https://docs.arize.com/phoenix)