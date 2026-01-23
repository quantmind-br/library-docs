---
title: Bedrock Guardrails | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/bedrock
source: sitemap
fetched_at: 2026-01-21T19:52:05.83042428-03:00
rendered_js: false
word_count: 427
summary: This document explains how to integrate and configure AWS Bedrock guardrails within LiteLLM to enforce content policies and PII masking. It covers setup procedures for different execution modes, handling blocked responses, and optimizing performance with experimental flags.
tags:
    - litellm
    - aws-bedrock
    - guardrails
    - pii-masking
    - llm-security
    - proxy-configuration
category: guide
---

LiteLLM supports Bedrock guardrails via the [Bedrock ApplyGuardrail API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ApplyGuardrail.html).

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Define Guardrails on your LiteLLM config.yaml[​](#1-define-guardrails-on-your-litellm-configyaml "Direct link to 1. Define Guardrails on your LiteLLM config.yaml")

Define your guardrails under the `guardrails` section

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"bedrock-pre-guard"
litellm_params:
guardrail: bedrock  # supported values: "aporia", "bedrock", "lakera"
mode:"during_call"
guardrailIdentifier: ff6ujrregl1q      # your guardrail ID on bedrock
guardrailVersion:"DRAFT"# your guardrail version on bedrock
aws_region_name: os.environ/AWS_REGION # region guardrail is defined
aws_role_name: os.environ/AWS_ROLE_ARN # your role with permissions to use the guardrail

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

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "hi my email is ishaan@berri.ai"}
    ],
    "guardrails": ["bedrock-pre-guard"]
  }'
```

Expected response on failure

```
{
  "error": {
    "message": {
      "error": "Violated guardrail policy",
      "bedrock_guardrail_response": {
        "action": "GUARDRAIL_INTERVENED",
        "assessments": [
          {
            "topicPolicy": {
              "topics": [
                {
                  "action": "BLOCKED",
                  "name": "Coffee",
                  "type": "DENY"
                }
              ]
            }
          }
        ],
        "blockedResponse": "Sorry, the model cannot answer this question. coffee guardrail applied ",
        "output": [
          {
            "text": "Sorry, the model cannot answer this question. coffee guardrail applied "
          }
        ],
        "outputs": [
          {
            "text": "Sorry, the model cannot answer this question. coffee guardrail applied "
          }
        ],
        "usage": {
          "contentPolicyUnits": 0,
          "contextualGroundingPolicyUnits": 0,
          "sensitiveInformationPolicyFreeUnits": 0,
          "sensitiveInformationPolicyUnits": 0,
          "topicPolicyUnits": 1,
          "wordPolicyUnits": 0
        }
      }
    },
    "type": "None",
    "param": "None",
    "code": "400"
  }
}

```

## PII Masking with Bedrock Guardrails[​](#pii-masking-with-bedrock-guardrails "Direct link to PII Masking with Bedrock Guardrails")

Bedrock guardrails support PII detection and masking capabilities. To enable this feature, you need to:

1. Set `mode` to `pre_call` to run the guardrail check before the LLM call
2. Enable masking by setting `mask_request_content` and/or `mask_response_content` to `true`

Here's how to configure it in your config.yaml:

litellm proxy config.yaml

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"bedrock-pre-guard"
litellm_params:
guardrail: bedrock
mode:"pre_call"# Important: must use pre_call mode for masking
guardrailIdentifier: wf0hkdb5x07f
guardrailVersion:"DRAFT"
aws_region_name: os.environ/AWS_REGION
aws_role_name: os.environ/AWS_ROLE_ARN
mask_request_content:true# Enable masking in user requests
mask_response_content:true# Enable masking in model responses
```

With this configuration, when the bedrock guardrail intervenes, litellm will read the masked output from the guardrail and send it to the model.

### Example Usage[​](#example-usage "Direct link to Example Usage")

When enabled, PII will be automatically masked in the text. For example, if a user sends:

```
My email is john.doe@example.com and my phone number is 555-123-4567
```

The text sent to the model might be masked as:

```
My email is [EMAIL] and my phone number is [PHONE_NUMBER]
```

This helps protect sensitive information while still allowing the model to understand the context of the request.

## Experimental: Only Send Latest User Message[​](#experimental-only-send-latest-user-message "Direct link to Experimental: Only Send Latest User Message")

When you're chaining long conversations through Bedrock guardrails, you can opt into a lighter, experimental behavior by setting `experimental_use_latest_role_message_only: true` in the guardrail's `litellm_params`. When enabled, LiteLLM only sends the most recent `user` message (or assistant output during post-call checks) to Bedrock, which:

- prevents unintended blocks on older system/dev messages
- keeps Bedrock payloads smaller, reducing latency and cost
- applies to proxy hooks (`pre_call`, `during_call`) and the `/guardrails/apply_guardrail` testing endpoint

litellm proxy config.yaml

```
guardrails:
-guardrail_name:"bedrock-pre-guard"
litellm_params:
guardrail: bedrock
mode:"pre_call"
guardrailIdentifier: wf0hkdb5x07f
guardrailVersion:"DRAFT"
aws_region_name: os.environ/AWS_REGION
experimental_use_latest_role_message_only:true# NEW
```

> ⚠️ This flag is currently experimental and defaults to `false` to preserve the legacy behavior (entire message history). We'll be listening to user feedback to decide if this becomes the default or rolls out more broadly.

## Disabling Exceptions on Bedrock BLOCK[​](#disabling-exceptions-on-bedrock-block "Direct link to Disabling Exceptions on Bedrock BLOCK")

By default, when Bedrock guardrails block content, LiteLLM raises an HTTP 400 exception. However, you can disable this behavior by setting `disable_exception_on_block: true`. This is particularly useful when integrating with **OpenWebUI**, where exceptions can interrupt the chat flow and break the user experience.

When exceptions are disabled, instead of receiving an error, you'll get a successful response containing the Bedrock guardrail's modified/blocked output.

### Configuration[​](#configuration "Direct link to Configuration")

Add `disable_exception_on_block: true` to your guardrail configuration:

litellm proxy config.yaml

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"bedrock-guardrail"
litellm_params:
guardrail: bedrock
mode:"post_call"
guardrailIdentifier: ff6ujrregl1q
guardrailVersion:"DRAFT"
aws_region_name: os.environ/AWS_REGION
aws_role_name: os.environ/AWS_ROLE_ARN
disable_exception_on_block:true# Prevents exceptions when content is blocked
```

### Behavior Comparison[​](#behavior-comparison "Direct link to Behavior Comparison")

- With Exceptions (Default)
- Without Exceptions

When `disable_exception_on_block: false` (default):

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "How do I make explosives?"}
    ],
    "guardrails": ["bedrock-guardrail"]
  }'
```

**Response: HTTP 400 Error**

```
{
"error":{
"message":{
"error":"Violated guardrail policy",
"bedrock_guardrail_response":{
"action":"GUARDRAIL_INTERVENED",
"blockedResponse":"I can't provide information on creating explosives.",
// ... additional details
}
},
"type":"None",
"param":"None",
"code":"400"
}
}
```