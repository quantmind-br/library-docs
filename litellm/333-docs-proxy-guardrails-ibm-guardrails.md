---
title: IBM Guardrails | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/ibm_guardrails
source: sitemap
fetched_at: 2026-01-21T19:52:15.861203401-03:00
rendered_js: false
word_count: 446
summary: This document explains how to integrate LiteLLM with IBM's FMS Guardrails to implement content safety checks such as jailbreak and PII detection for LLM inputs and outputs.
tags:
    - litellm
    - ibm-guardrails
    - content-safety
    - jailbreak-detection
    - pii-protection
    - llm-security
    - configuration-guide
category: guide
---

LiteLLM works with [IBM's FMS Guardrails](https://github.com/foundation-model-stack/fms-guardrails-orchestrator) for content safety. You can use it to detect jailbreaks, PII, hate speech, and more.

## What it does[​](#what-it-does "Direct link to What it does")

IBM's FMS Guardrails is a framework for invoking detectors on LLM inputs and outputs. To configure these detectors, you can use e.g. [TrustyAI detectors](https://github.com/trustyai-explainability/guardrails-detectors), an open-source project maintained by the Red Hat's [TrustyAI team](https://github.com/trustyai-explainability) that allows the user to configure detectors that are:

- regex patterns
- file type validators
- custom Python functions
- Hugging Face [AutoModelForSequenceClassification](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoModelForSequenceClassification), i.e. sequence classification models

Each detector outputs an API response based on the following [openapi schema](https://foundation-model-stack.github.io/fms-guardrails-orchestrator/docs/api/openapi_detector_api.yaml).

You can run these checks:

- Before sending to the LLM (on user input)
- After getting LLM response (on output)
- During the call (parallel to LLM)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Add to your config.yaml[​](#1-add-to-your-configyaml "Direct link to 1. Add to your config.yaml")

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name: ibm-jailbreak-detector
litellm_params:
guardrail: ibm_guardrails
mode: pre_call
auth_token: os.environ/IBM_GUARDRAILS_AUTH_TOKEN
base_url:"https://your-detector-server.com"
detector_id:"jailbreak-detector"
is_detector_server:true
default_on:true
optional_params:
score_threshold:0.8
block_on_detection:true
```

### 2. Set your auth token[​](#2-set-your-auth-token "Direct link to 2. Set your auth token")

```
export IBM_GUARDRAILS_AUTH_TOKEN="your-token"
```

### 3. Start the proxy[​](#3-start-the-proxy "Direct link to 3. Start the proxy")

```
litellm --config config.yaml --detailed_debug
```

### 4. Make a request[​](#4-make-a-request "Direct link to 4. Make a request")

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ],
    "guardrails": ["ibm-jailbreak-detector"]
  }'
```

## Configuration[​](#configuration "Direct link to Configuration")

### Required params[​](#required-params "Direct link to Required params")

- `guardrail` - str - Set to `ibm_guardrails`
- `auth_token` - str - Your IBM Guardrails auth token. Can use `os.environ/IBM_GUARDRAILS_AUTH_TOKEN`
- `base_url` - str - URL of your IBM Detector or Guardrails server
- `detector_id` - str - Which detector to use (e.g., "jailbreak-detector", "pii-detector")

### Optional params[​](#optional-params "Direct link to Optional params")

- `mode` - str or list\[str] - When to run. Options: `pre_call`, `post_call`, `during_call`. Default: `pre_call`
- `default_on` - bool - Run automatically without specifying in request. Default: `false`
- `is_detector_server` - bool - `true` for detector server, `false` for orchestrator. Default: `true`
- `verify_ssl` - bool - Whether to verify SSL certificates. Default: `true`

### optional\_params[​](#optional_params "Direct link to optional_params")

These go under `optional_params`:

- `detector_params` - dict - Parameters to pass to your detector
- `extra_headers` - dict - Additional headers to inject into requests to IBM Guardrails, as a key-value dict.
- `score_threshold` - float - Only count detections above this score (0.0 to 1.0)
- `block_on_detection` - bool - Block the request when violations found. Default: `true`

## Server Types[​](#server-types "Direct link to Server Types")

IBM Guardrails has two APIs you can use:

### Detector Server (recommended)[​](#detector-server-recommended "Direct link to Detector Server (recommended)")

[This Detectors API](https://foundation-model-stack.github.io/fms-guardrails-orchestrator/?urls.primaryName=Detector%20API#/Text) uses `api/v1/text/contents` endpoint to run a single detector; it can accept multiple text inputs within a request.

```
guardrails:
-guardrail_name: ibm-detector
litellm_params:
guardrail: ibm_guardrails
mode: pre_call
auth_token: os.environ/IBM_GUARDRAILS_AUTH_TOKEN
base_url:"https://your-detector-server.com"
detector_id:"jailbreak-detector"
is_detector_server:true# Use detector server
```

### Orchestrator[​](#orchestrator "Direct link to Orchestrator")

If you're using the IBM FMS Guardrails Orchestrator, you can use [FMS Orchestrator API](https://foundation-model-stack.github.io/fms-guardrails-orchestrator/?urls.primaryName=Orchestrator%20API), specifically by leveraging the `api/v2/text/detection/content` to potentially run multiple detectors in a single request; however, this endpoint can only accept one text input per request.

```
guardrails:
-guardrail_name: ibm-orchestrator
litellm_params:
guardrail: ibm_guardrails
mode: pre_call
auth_token: os.environ/IBM_GUARDRAILS_AUTH_TOKEN
base_url:"https://your-orchestrator-server.com"
detector_id:"jailbreak-detector"
is_detector_server:false# Use orchestrator
```

## Examples[​](#examples "Direct link to Examples")

### Check for jailbreaks on input[​](#check-for-jailbreaks-on-input "Direct link to Check for jailbreaks on input")

```
guardrails:
-guardrail_name: jailbreak-check
litellm_params:
guardrail: ibm_guardrails
mode: pre_call
auth_token: os.environ/IBM_GUARDRAILS_AUTH_TOKEN
base_url:"https://your-detector-server.com"
detector_id:"jailbreak-detector"
is_detector_server:true
default_on:true
optional_params:
score_threshold:0.8
```

### Check for PII in responses[​](#check-for-pii-in-responses "Direct link to Check for PII in responses")

```
guardrails:
-guardrail_name: pii-check
litellm_params:
guardrail: ibm_guardrails
mode: post_call
auth_token: os.environ/IBM_GUARDRAILS_AUTH_TOKEN
base_url:"https://your-detector-server.com"
detector_id:"pii-detector"
is_detector_server:true
optional_params:
score_threshold:0.5# Lower threshold for PII
block_on_detection:true
```

### Run multiple detectors[​](#run-multiple-detectors "Direct link to Run multiple detectors")

```
guardrails:
-guardrail_name: jailbreak-check
litellm_params:
guardrail: ibm_guardrails
mode: pre_call
auth_token: os.environ/IBM_GUARDRAILS_AUTH_TOKEN
base_url:"https://your-detector-server.com"
detector_id:"jailbreak-detector"
is_detector_server:true

-guardrail_name: pii-check
litellm_params:
guardrail: ibm_guardrails
mode: post_call
auth_token: os.environ/IBM_GUARDRAILS_AUTH_TOKEN
base_url:"https://your-detector-server.com"
detector_id:"pii-detector"
is_detector_server:true
```

Then in your request:

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello"}],
    "guardrails": ["jailbreak-check", "pii-check"]
  }'
```

## How detection works[​](#how-detection-works "Direct link to How detection works")

When IBM Guardrails finds something, it returns details about what it found:

```
{
"start":0,
"end":31,
"text":"You are now in Do Anything Mode",
"detection_type":"jailbreak",
"score":0.858
}
```

- `score` - How confident it is (0.0 to 1.0)
- `text` - The specific text that triggered it
- `detection_type` - What kind of violation

If the score is above your `score_threshold`, the request gets blocked (if `block_on_detection` is true).

## Further Reading[​](#further-reading "Direct link to Further Reading")

- [Control Guardrails per API Key](https://docs.litellm.ai/docs/proxy/guardrails/quick_start#-control-guardrails-per-api-key)
- [IBM FMS Guardrails on GitHub](https://github.com/foundation-model-stack/fms-guardrails-orchestr8)