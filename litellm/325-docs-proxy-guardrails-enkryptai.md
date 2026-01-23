---
title: EnkryptAI Guardrails | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/enkryptai
source: sitemap
fetched_at: 2026-01-21T19:52:08.359062343-03:00
rendered_js: false
word_count: 338
summary: This document provides instructions for integrating EnkryptAI guardrails with LiteLLM to perform content moderation, PII detection, and safety checks on model inputs and outputs. It covers configuration options, execution modes, and advanced settings like monitor mode and custom policies.
tags:
    - litellm
    - enkryptai
    - content-moderation
    - llm-guardrails
    - ai-safety
    - pii-detection
    - prompt-injection
    - observability
category: guide
---

LiteLLM supports EnkryptAI guardrails for content moderation and safety checks on LLM inputs and outputs.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Define Guardrails on your LiteLLM config.yaml[​](#1-define-guardrails-on-your-litellm-configyaml "Direct link to 1. Define Guardrails on your LiteLLM config.yaml")

Define your guardrails under the `guardrails` section:

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"enkryptai-guard"
litellm_params:
guardrail: enkryptai
mode:"pre_call"
api_key: os.environ/ENKRYPTAI_API_KEY
detectors:
toxicity:
enabled:true
nsfw:
enabled:true
pii:
enabled:true
entities:["email","phone","secrets"]
injection_attack:
enabled:true
```

#### Supported values for `mode`[​](#supported-values-for-mode "Direct link to supported-values-for-mode")

- `pre_call` - Run **before** LLM call, on **input**
- `post_call` - Run **after** LLM call, on **output**
- `during_call` - Run **during** LLM call, on **input**. Same as `pre_call` but runs in parallel as LLM call

#### Available Detectors[​](#available-detectors "Direct link to Available Detectors")

EnkryptAI supports multiple content detection types:

- **toxicity** - Detect toxic language
- **nsfw** - Detect NSFW (Not Safe For Work) content
- **pii** - Detect personally identifiable information
  
  - Configure entities: `["pii", "email", "phone", "secrets", "ip_address", "url"]`
- **injection\_attack** - Detect prompt injection attempts
- **keyword\_detector** - Detect custom keywords/phrases
- **policy\_violation** - Detect policy violations
- **bias** - Detect biased content
- **sponge\_attack** - Detect sponge attacks

### 2. Set Environment Variables[​](#2-set-environment-variables "Direct link to 2. Set Environment Variables")

```
export ENKRYPTAI_API_KEY="your-api-key"
```

### 3. Start LiteLLM Gateway[​](#3-start-litellm-gateway "Direct link to 3. Start LiteLLM Gateway")

```
litellm --config config.yaml --detailed_debug
```

### 4. Test Request[​](#4-test-request "Direct link to 4. Test Request")

[**Langchain, OpenAI SDK Usage Examples**](https://docs.litellm.ai/docs/proxy/proxy/user_keys#request-format)

- Successful Call
- Unsuccessful Call

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "Hello, how can you help me today?"}
    ],
    "guardrails": ["enkryptai-guard"]
  }'
```

**Response: HTTP 200 Success**

Content passes all detector checks and is allowed through.

## Video Walkthrough[​](#video-walkthrough "Direct link to Video Walkthrough")

## Advanced Configuration[​](#advanced-configuration "Direct link to Advanced Configuration")

### Using Custom Policies[​](#using-custom-policies "Direct link to Using Custom Policies")

You can specify a custom EnkryptAI policy:

```
guardrails:
-guardrail_name:"enkryptai-custom"
litellm_params:
guardrail: enkryptai
mode:"pre_call"
api_key: os.environ/ENKRYPTAI_API_KEY
policy_name:"my-custom-policy"# Sent via x-enkrypt-policy header
detectors:
toxicity:
enabled:true
```

### Using Deployments[​](#using-deployments "Direct link to Using Deployments")

Specify an EnkryptAI deployment:

```
guardrails:
-guardrail_name:"enkryptai-deployment"
litellm_params:
guardrail: enkryptai
mode:"pre_call"
api_key: os.environ/ENKRYPTAI_API_KEY
deployment_name:"production"# Sent via X-Enkrypt-Deployment header
detectors:
toxicity:
enabled:true
```

### Monitor Mode (Logging Without Blocking)[​](#monitor-mode-logging-without-blocking "Direct link to Monitor Mode (Logging Without Blocking)")

Set `block_on_violation: false` to log violations without blocking requests:

```
guardrails:
-guardrail_name:"enkryptai-monitor"
litellm_params:
guardrail: enkryptai
mode:"pre_call"
api_key: os.environ/ENKRYPTAI_API_KEY
block_on_violation:false# Log violations but don't block
detectors:
toxicity:
enabled:true
nsfw:
enabled:true
```

In monitor mode, all violations are logged but requests are never blocked.

### Input and Output Guardrails[​](#input-and-output-guardrails "Direct link to Input and Output Guardrails")

Configure separate guardrails for input and output:

```
guardrails:
# Input guardrail
-guardrail_name:"enkryptai-input"
litellm_params:
guardrail: enkryptai
mode:"pre_call"
api_key: os.environ/ENKRYPTAI_API_KEY
detectors:
pii:
enabled:true
entities:["email","phone","ssn"]
injection_attack:
enabled:true

# Output guardrail
-guardrail_name:"enkryptai-output"
litellm_params:
guardrail: enkryptai
mode:"post_call"
api_key: os.environ/ENKRYPTAI_API_KEY
detectors:
toxicity:
enabled:true
nsfw:
enabled:true
```

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

ParameterTypeDescriptionDefault`api_key`stringEnkryptAI API key`ENKRYPTAI_API_KEY` env var`api_base`stringEnkryptAI API base URL`https://api.enkryptai.com``policy_name`stringCustom policy name (sent via `x-enkrypt-policy` header)None`deployment_name`stringDeployment name (sent via `X-Enkrypt-Deployment` header)None`detectors`objectDetector configuration`{}``block_on_violation`booleanBlock requests on violations`true``mode`stringWhen to run: `pre_call`, `post_call`, or `during_call`Required

## Observability[​](#observability "Direct link to Observability")

EnkryptAI guardrail logs include:

- **guardrail\_status**: `success`, `guardrail_intervened`, or `guardrail_failed_to_respond`
- **guardrail\_provider**: `enkryptai`
- **guardrail\_json\_response**: Full API response with detection details
- **duration**: Time taken for guardrail check
- **start\_time** and **end\_time**: Timestamps

These logs are available through your configured LiteLLM logging callbacks.

## Error Handling[​](#error-handling "Direct link to Error Handling")

The guardrail handles errors gracefully:

- **API Failures**: Logs error and raises exception
- **Rate Limits (429)**: Logs error and raises exception
- **Invalid Configuration**: Raises `ValueError` on initialization

Set `block_on_violation: false` to continue processing even when violations are detected (monitor mode).

## Support[​](#support "Direct link to Support")

For more information about EnkryptAI:

- Documentation: [https://docs.enkryptai.com](https://docs.enkryptai.com)
- Website: [https://enkryptai.com](https://enkryptai.com)