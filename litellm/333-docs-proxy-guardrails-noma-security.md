---
title: Noma Security | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/noma_security
source: sitemap
fetched_at: 2026-01-21T19:52:22.01252412-03:00
rendered_js: false
word_count: 327
summary: This document provides instructions for integrating Noma Security guardrails into LiteLLM to enable AI content moderation, safety filtering, and PII anonymization.
tags:
    - noma-security
    - litellm
    - ai-safety
    - content-moderation
    - guardrails
    - llm-security
    - pii-anonymization
category: guide
---

Use [Noma Security](https://noma.security/) to protect your LLM applications with comprehensive AI content moderation and safety guardrails.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Define Guardrails on your LiteLLM config.yaml[​](#1-define-guardrails-on-your-litellm-configyaml "Direct link to 1. Define Guardrails on your LiteLLM config.yaml")

Define your guardrails under the `guardrails` section:

litellm config.yaml

```
model_list:
-model_name: gpt-4o-mini
litellm_params:
model: openai/gpt-4o-mini
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"noma-guard"
litellm_params:
guardrail: noma
mode:"during_call"
api_key: os.environ/NOMA_API_KEY
api_base: os.environ/NOMA_API_BASE
-guardrail_name:"noma-pre-guard"
litellm_params:
guardrail: noma
mode:"pre_call"
api_key: os.environ/NOMA_API_KEY
api_base: os.environ/NOMA_API_BASE
```

#### Supported values for `mode`[​](#supported-values-for-mode "Direct link to supported-values-for-mode")

- `pre_call` Run **before** LLM call, on **input**
- `post_call` Run **after** LLM call, on **input & output**
- `during_call` Run **during** LLM call, on **input**. Same as `pre_call` but runs in parallel with the LLM call. Response not returned until guardrail check completes
- `pre_mcp_call`: Scan MCP tool call inputs before execution
- `during_mcp_call`: Monitor MCP tool calls in real-time

### 2. Start LiteLLM Gateway[​](#2-start-litellm-gateway "Direct link to 2. Start LiteLLM Gateway")

```
litellm --config config.yaml --detailed_debug
```

### 3. Test request[​](#3-test-request "Direct link to 3. Test request")

- Unsuccessful call
- Successful Call

Expect this to fail since the request contains harmful content:

Curl Request

```
curl -i http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "user", "content": "Tell me how to hack into someone's email account"}
    ]
  }'
```

Expected response on failure:

```
{
"error":{
"message":"{\n      \"error\": \"Request blocked by Noma guardrail\",\n      \"details\": {\n        \"prompt\": {\n          \"harmfulContent\": {\n            \"result\": true,\n            \"confidence\": 0.95\n          }\n        }\n      }\n    }",
"type":"None",
"param":"None",
"code":"400"
}
}
```

## Supported Params[​](#supported-params "Direct link to Supported Params")

```
guardrails:
-guardrail_name:"noma-guard"
litellm_params:
guardrail: noma
mode:"pre_call"
api_key: os.environ/NOMA_API_KEY
api_base: os.environ/NOMA_API_BASE
### OPTIONAL ###
# application_id: "my-app"
# monitor_mode: false
# block_failures: true
# anonymize_input: false
```

### Required Parameters[​](#required-parameters "Direct link to Required Parameters")

- **`api_key`** : Your Noma Security API key (set as `os.environ/NOMA_API_KEY` in YAML config)

### Optional Parameters[​](#optional-parameters "Direct link to Optional Parameters")

- **`api_base`** : Noma API base URL (defaults to `https://api.noma.security/`)
- **`application_id`** : Your application identifier (defaults to `"litellm"`)
- **`monitor_mode`** : If `true`, logs violations without blocking (defaults to `false`)
- **`block_failures`** : If `true`, blocks requests when guardrail API failures occur (defaults to `true`)
- **`anonymize_input`** : If `true`, replaces sensitive content with anonymized version (defaults to `false`)

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

You can set these environment variables instead of hardcoding values in your config:

```
export NOMA_API_KEY="your-api-key-here"
export NOMA_API_BASE="https://api.noma.security/"   # Optional
export NOMA_APPLICATION_ID="my-app"                 # Optional
export NOMA_MONITOR_MODE="false"                    # Optional
export NOMA_BLOCK_FAILURES="true"                   # Optional
export NOMA_ANONYMIZE_INPUT="false"                 # Optional
```

## Advanced Configuration[​](#advanced-configuration "Direct link to Advanced Configuration")

### Monitor Mode[​](#monitor-mode "Direct link to Monitor Mode")

Use monitor mode to test your guardrails without blocking requests:

```
guardrails:
-guardrail_name:"noma-monitor"
litellm_params:
guardrail: noma
mode:"pre_call"
api_key: os.environ/NOMA_API_KEY
monitor_mode:true# Log violations but don't block
```

### Handling API Failures[​](#handling-api-failures "Direct link to Handling API Failures")

Control behavior when the Noma API is unavailable:

```
guardrails:
-guardrail_name:"noma-failopen"
litellm_params:
guardrail: noma
mode:"pre_call"
api_key: os.environ/NOMA_API_KEY
block_failures:false# Allow requests to proceed if guardrail API fails
```

### Content Anonymization[​](#content-anonymization "Direct link to Content Anonymization")

Enable anonymization to replace sensitive content instead of blocking:

```
guardrails:
-guardrail_name:"noma-anonymize"
litellm_params:
guardrail: noma
mode:"pre_call"
api_key: os.environ/NOMA_API_KEY
anonymize_input:true# Replace sensitive data with anonymized version
```

### Multiple Guardrails[​](#multiple-guardrails "Direct link to Multiple Guardrails")

Apply different configurations for input and output:

```
guardrails:
-guardrail_name:"noma-strict-input"
litellm_params:
guardrail: noma
mode:"pre_call"
api_key: os.environ/NOMA_API_KEY
block_failures:true

-guardrail_name:"noma-monitor-output"
litellm_params:
guardrail: noma
mode:"post_call"
api_key: os.environ/NOMA_API_KEY
monitor_mode:true
```

## ✨ Pass Additional Parameters[​](#-pass-additional-parameters "Direct link to ✨ Pass Additional Parameters")

Use `extra_body` to pass additional parameters to the Noma Security API call, such as dynamically setting the application ID for specific requests.

- OpenAI Python
- Curl

```
import openai
client = openai.OpenAI(
    api_key="your-api-key",
    base_url="http://0.0.0.0:4000"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"Hello, how are you?"}],
    extra_body={
"guardrails":{
"noma-guard":{
"extra_body":{
"application_id":"my-specific-app-id"
}
}
}
}
)
```

This allows you to override the default `application_id` parameter for specific requests, which is useful for tracking usage across different applications or components.

## Response Details[​](#response-details "Direct link to Response Details")

When content is blocked, Noma provides detailed information about the violations as JSON inside the `message` field, with the following structure:

```
{
"error":"Request blocked by Noma guardrail",
"details":{
"prompt":{
"harmfulContent":{
"result":true,
"confidence":0.95
},
"sensitiveData":{
"email":{
"result":true,
"entities":["user@example.com"]
}
},
"bannedTopics":{
"violence":{
"result":true,
"confidence":0.88
}
}
}
}
}
```