---
title: DynamoAI Guardrails | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/dynamoai
source: sitemap
fetched_at: 2026-01-21T19:52:07.965972294-03:00
rendered_js: false
word_count: 290
summary: This document explains how to integrate and configure DynamoAI guardrails within LiteLLM for content moderation and policy enforcement. It covers configuration parameters, execution modes, environment variables, and monitoring for LLM inputs and outputs.
tags:
    - litellm
    - dynamoai
    - guardrails
    - content-moderation
    - llm-security
    - api-gateway
    - llm-observability
category: guide
---

LiteLLM supports DynamoAI guardrails for content moderation and policy enforcement on LLM inputs and outputs.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Define Guardrails on your LiteLLM config.yaml[​](#1-define-guardrails-on-your-litellm-configyaml "Direct link to 1. Define Guardrails on your LiteLLM config.yaml")

Define your guardrails under the `guardrails` section:

config.yaml

```
model_list:
-model_name: gpt-4
litellm_params:
model: openai/gpt-4
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"dynamoai-guard"
litellm_params:
guardrail: dynamoai
mode:"pre_call"
api_key: os.environ/DYNAMOAI_API_KEY
```

#### Supported values for `mode`[​](#supported-values-for-mode "Direct link to supported-values-for-mode")

- `pre_call` - Run **before** LLM call, on **input**
- `post_call` - Run **after** LLM call, on **output**
- `during_call` - Run **during** LLM call, on **input**. Same as `pre_call` but runs in parallel as LLM call

### 2. Set Environment Variables[​](#2-set-environment-variables "Direct link to 2. Set Environment Variables")

```
export DYNAMOAI_API_KEY="your-api-key"
# Optional: Set policy IDs via environment variable (comma-separated)
export DYNAMOAI_POLICY_IDS="policy-id-1,policy-id-2,policy-id-3"
```

### 3. Start LiteLLM Gateway[​](#3-start-litellm-gateway "Direct link to 3. Start LiteLLM Gateway")

```
litellm --config config.yaml --detailed_debug
```

### 4. Test Request[​](#4-test-request "Direct link to 4. Test Request")

[**Langchain, OpenAI SDK Usage Examples**](https://docs.litellm.ai/docs/proxy/proxy/user_keys#request-format)

- Successful Call
- Blocked Call

Successful Request

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ],
    "guardrails": ["dynamoai-guard"]
  }'
```

**Response: HTTP 200 Success**

Content passes all policy checks and is allowed through.

## Advanced Configuration[​](#advanced-configuration "Direct link to Advanced Configuration")

### Specify Policy IDs[​](#specify-policy-ids "Direct link to Specify Policy IDs")

Configure specific DynamoAI policies to apply:

config.yaml

```
guardrails:
-guardrail_name:"dynamoai-policies"
litellm_params:
guardrail: dynamoai
mode:"pre_call"
api_key: os.environ/DYNAMOAI_API_KEY
policy_ids:
-"policy-id-1"
-"policy-id-2"
-"policy-id-3"
```

### Custom API Base[​](#custom-api-base "Direct link to Custom API Base")

Specify a custom DynamoAI API endpoint:

config.yaml

```
guardrails:
-guardrail_name:"dynamoai-custom"
litellm_params:
guardrail: dynamoai
mode:"pre_call"
api_key: os.environ/DYNAMOAI_API_KEY
api_base:"https://custom.dynamo.ai"
```

### Model ID for Tracking[​](#model-id-for-tracking "Direct link to Model ID for Tracking")

Add a model ID for tracking and logging purposes:

config.yaml

```
guardrails:
-guardrail_name:"dynamoai-tracked"
litellm_params:
guardrail: dynamoai
mode:"pre_call"
api_key: os.environ/DYNAMOAI_API_KEY
model_id:"gpt-4-production"
```

### Input and Output Guardrails[​](#input-and-output-guardrails "Direct link to Input and Output Guardrails")

Configure separate guardrails for input and output:

config.yaml

```
guardrails:
# Input guardrail
-guardrail_name:"dynamoai-input"
litellm_params:
guardrail: dynamoai
mode:"pre_call"
api_key: os.environ/DYNAMOAI_API_KEY

# Output guardrail
-guardrail_name:"dynamoai-output"
litellm_params:
guardrail: dynamoai
mode:"post_call"
api_key: os.environ/DYNAMOAI_API_KEY
```

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

ParameterTypeDescriptionDefault`api_key`stringDynamoAI API key (required)`DYNAMOAI_API_KEY` env var`api_base`stringDynamoAI API base URL`https://api.dynamo.ai``policy_ids`arrayList of DynamoAI policy IDs to apply (optional)`DYNAMOAI_POLICY_IDS` env var (comma-separated)`model_id`stringModel ID for tracking/logging`DYNAMOAI_MODEL_ID` env var`mode`stringWhen to run: `pre_call`, `post_call`, or `during_call`Required

## Observability[​](#observability "Direct link to Observability")

DynamoAI guardrail logs include:

- **guardrail\_status**: `success`, `guardrail_intervened`, or `guardrail_failed_to_respond`
- **guardrail\_provider**: `dynamoai`
- **guardrail\_json\_response**: Full API response with policy details
- **duration**: Time taken for guardrail check
- **start\_time** and **end\_time**: Timestamps

These logs are available through your configured LiteLLM logging callbacks.

## Error Handling[​](#error-handling "Direct link to Error Handling")

The guardrail handles errors gracefully:

- **API Failures**: Logs error and raises exception with status `guardrail_failed_to_respond`
- **Policy Violations**: Raises `ValueError` with detailed violation information
- **Invalid Configuration**: Raises `ValueError` on initialization if API key is missing

## Current Limitations[​](#current-limitations "Direct link to Current Limitations")

- Only the `BLOCK` action is currently supported
- `WARN`, `REDACT`, and `SANITIZE` actions are treated as success (pass through)

## Support[​](#support "Direct link to Support")

For more information about DynamoAI:

- Website: [https://dynamo.ai](https://dynamo.ai)
- Documentation: Contact DynamoAI for API documentation