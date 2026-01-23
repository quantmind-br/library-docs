---
title: Aim Security | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/aim_security
source: sitemap
fetched_at: 2026-01-21T19:52:00.639549064-03:00
rendered_js: false
word_count: 317
summary: This document explains how to set up and integrate Aim Guard with LiteLLM to enforce security policies and guardrails for AI applications.
tags:
    - aim-security
    - litellm
    - guardrails
    - ai-security
    - pii-detection
    - llm-gateway
category: tutorial
---

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Create a new Aim Guard[​](#1-create-a-new-aim-guard "Direct link to 1. Create a new Aim Guard")

Go to [Aim Application](https://app.aim.security/inventory/custom-ai-apps) and create a new guard.

When prompted, select API option, and name your guard.

note

In case you want to host your guard on-premise, you can enable this option by [installing Aim Outpost](https://app.aim.security/settings/on-prem-deployment) prior to creating the guard.

### 2. Configure your Aim Guard policies[​](#2-configure-your-aim-guard-policies "Direct link to 2. Configure your Aim Guard policies")

In the newly created guard's page, you can find a reference to the prompt policy center of this guard.

You can decide which detections will be enabled, and set the threshold for each detection.

info

When using LiteLLM with virtual keys, key-specific policies can be set directly in Aim's guards page by specifying the virtual key alias when creating the guard.

Only the aliases of your virtual keys (and not the actual key secrets) will be sent to Aim.

### 3. Add Aim Guardrail on your LiteLLM config.yaml[​](#3-add-aim-guardrail-on-your-litellm-configyaml "Direct link to 3. Add Aim Guardrail on your LiteLLM config.yaml")

Define your guardrails under the `guardrails` section

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name: aim-protected-app
litellm_params:
guardrail: aim
mode:[pre_call, post_call]# "During_call" is also available
api_key: os.environ/AIM_API_KEY
api_base: os.environ/AIM_API_BASE # Optional, use only when using a self-hosted Aim Outpost
```

Under the `api_key`, insert the API key you were issued. The key can be found in the guard's page. You can also set `AIM_API_KEY` as an environment variable.

By default, the `api_base` is set to `https://api.aim.security`. If you are using a self-hosted Aim Outpost, you can set the `api_base` to your Outpost's URL.

### 4. Start LiteLLM Gateway[​](#4-start-litellm-gateway "Direct link to 4. Start LiteLLM Gateway")

```
litellm --config config.yaml
```

### 5. Make your first request[​](#5-make-your-first-request "Direct link to 5. Make your first request")

note

The following example depends on enabling *PII* detection in your guard. You can adjust the request content to match different guard's policies.

- Successfully blocked request
- Successfully permitted request

note

When using LiteLLM with virtual keys, an `Authorization` header with the virtual key is required.

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "hi my email is ishaan@berri.ai"}
    ],
    "guardrails": ["aim-protected-app"]
  }'
```

If configured correctly, since `ishaan@berri.ai` would be detected by the Aim Guard as PII, you'll receive a response similar to the following with a `400 Bad Request` status code:

```
{
"error":{
"message":"\"ishaan@berri.ai\" detected as email",
"type":"None",
"param":"None",
"code":"400"
}
}
```

## Advanced[​](#advanced "Direct link to Advanced")

Aim Guard provides user-specific Guardrail policies, enabling you to apply tailored policies to individual users. To utilize this feature, include the end-user's email in the request payload by setting the `x-aim-user-email` header of your request.

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-aim-user-email: ishaan@berri.ai" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "hi what is the weather"}
    ],
    "guardrails": ["aim-protected-app"]
  }'
```