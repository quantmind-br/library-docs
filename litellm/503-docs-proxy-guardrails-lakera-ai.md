---
title: Lakera AI | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/lakera_ai
source: sitemap
fetched_at: 2026-01-21T19:52:18.321567098-03:00
rendered_js: false
word_count: 262
summary: This document provides instructions on configuring and implementing Lakera guardrails within LiteLLM to monitor or block LLM inputs and outputs for content safety.
tags:
    - litellm
    - lakera
    - guardrails
    - content-safety
    - configuration
    - llm-security
category: configuration
---

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Define Guardrails on your LiteLLM config.yaml[​](#1-define-guardrails-on-your-litellm-configyaml "Direct link to 1. Define Guardrails on your LiteLLM config.yaml")

Define your guardrails under the `guardrails` section

litellm config.yaml

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"lakera-guard"
litellm_params:
guardrail: lakera_v2  # supported values: "aporia", "bedrock", "lakera"
mode:"during_call"
api_key: os.environ/LAKERA_API_KEY
api_base: os.environ/LAKERA_API_BASE
-guardrail_name:"lakera-pre-guard"
litellm_params:
guardrail: lakera_v2  # supported values: "aporia", "bedrock", "lakera"
mode:"pre_call"
api_key: os.environ/LAKERA_API_KEY
api_base: os.environ/LAKERA_API_BASE
-guardrail_name:"lakera-monitor"
litellm_params:
guardrail: lakera_v2
mode:"pre_call"
on_flagged:"monitor"# Log violations but don't block
api_key: os.environ/LAKERA_API_KEY
api_base: os.environ/LAKERA_API_BASE

```

#### Supported values for `mode`[​](#supported-values-for-mode "Direct link to supported-values-for-mode")

- `pre_call` Run **before** LLM call, on **input**
- `post_call` Run **after** LLM call, on **input & output**
- `during_call` Run **during** LLM call, on **input** Same as `pre_call` but runs in parallel as LLM call. Response not returned until guardrail check completes

### 2. Start LiteLLM Gateway[​](#2-start-litellm-gateway "Direct link to 2. Start LiteLLM Gateway")

```
litellm --config config.yaml --detailed_debug
```

### 3. Test request[​](#3-test-request "Direct link to 3. Test request")

[**Langchain, OpenAI SDK Usage Examples**](https://docs.litellm.ai/docs/proxy/proxy/user_keys#request-format)

- Unsuccessful call
- Successful Call

Expect this to fail since since `ishaan@berri.ai` in the request is PII

Curl Request

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "hi my email is ishaan@berri.ai"}
    ],
    "guardrails": ["lakera-guard"]
  }'
```

Expected response on failure

```
{
 "error": {
   "message": {
     "error": "Violated content safety policy",
     "lakera_ai_response": {
       "model": "lakera-guard-1",
       "results": [
         {
           "categories": {
             "prompt_injection": true,
             "jailbreak": false
           },
           "category_scores": {
             "prompt_injection": 0.999,
             "jailbreak": 0.0
           },
           "flagged": true,
           "payload": {}
         }
       ],
       "dev_info": {
         "git_revision": "cb163444",
         "git_timestamp": "2024-08-19T16:00:28+02:00",
         "version": "1.3.53"
       }
     }
   },
   "type": "None",
   "param": "None",
   "code": "400"
 }
}

```

## Supported Params[​](#supported-params "Direct link to Supported Params")

```
guardrails:
-guardrail_name:"lakera-guard"
litellm_params:
guardrail: lakera_v2  # supported values: "aporia", "bedrock", "lakera"
mode:"during_call"
api_key: os.environ/LAKERA_API_KEY
api_base: os.environ/LAKERA_API_BASE
### OPTIONAL ### 
# project_id: Optional[str] = None,
# payload: Optional[bool] = True,
# breakdown: Optional[bool] = True,
# metadata: Optional[Dict] = None,
# dev_info: Optional[bool] = True,
# on_flagged: Optional[str] = "block",  # "block" or "monitor"
```

- `api_base`: (Optional\[str]) The base of the Lakera integration. Defaults to `https://api.lakera.ai`
- `api_key`: (str) The API Key for the Lakera integration.
- `project_id`: (Optional\[str]) ID of the relevant project
- `payload`: (Optional\[bool]) When true the response will return a payload object containing any PII, profanity or custom detector regex matches detected, along with their location within the contents.
- `breakdown`: (Optional\[bool]) When true the response will return a breakdown list of the detectors that were run, as defined in the policy, and whether each of them detected something or not.
- `metadata`: (Optional\[Dict]) Metadata tags can be attached to screening requests as an object that can contain any arbitrary key-value pairs.
- `dev_info`: (Optional\[bool]) When true the response will return an object with developer information about the build of Lakera Guard.
- `on_flagged`: (Optional\[str]) Action to take when content is flagged. Defaults to `"block"`.
  
  - `"block"`: Raises an HTTP 400 exception when violations are detected (default behavior)
  - `"monitor"`: Logs violations but allows the request to proceed. Useful for tuning security policies without blocking legitimate requests.