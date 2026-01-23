---
title: Pillar Security | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/pillar_security
source: sitemap
fetched_at: 2026-01-21T19:52:31.330888368-03:00
rendered_js: false
word_count: 605
summary: This document explains how to integrate Pillar Security with LiteLLM Proxy to implement AI security guardrails for prompt injection, jailbreak detection, and sensitive data masking.
tags:
    - litellm
    - pillar-security
    - ai-security
    - guardrails
    - prompt-injection
    - data-protection
category: tutorial
---

Pillar Security integrates with [LiteLLM Proxy](https://docs.litellm.ai) via the [Generic Guardrail API](https://docs.litellm.ai/docs/adding_provider/generic_guardrail_api), providing comprehensive AI security scanning for your LLM applications.

- **Prompt Injection Protection**: Prevent malicious prompt manipulation
- **Jailbreak Detection**: Detect attempts to bypass AI safety measures
- **PII + PCI Detection**: Automatically detect sensitive personal and payment card information
- **Secret Detection**: Identify API keys, tokens, and credentials
- **Content Moderation**: Filter harmful or inappropriate content
- **Toxic Language**: Filter offensive or harmful language

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Set Environment Variables[​](#1-set-environment-variables "Direct link to 1. Set Environment Variables")

```
export PILLAR_API_KEY=your-pillar-api-key
export OPENAI_API_KEY=your-openai-api-key
```

### 2. Configure LiteLLM[​](#2-configure-litellm "Direct link to 2. Configure LiteLLM")

Create or update your `config.yaml`:

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name: pillar-security
litellm_params:
guardrail: generic_guardrail_api
mode:[pre_call, post_call]
api_base: https://api.pillar.security/api/v1/integrations/litellm
api_key: os.environ/PILLAR_API_KEY
default_on:true
additional_provider_specific_params:
plr_mask:true
plr_evidence:true
plr_scanners:true
```

Important

- The `api_base` must be exactly `https://api.pillar.security/api/v1/integrations/litellm` — this is the only endpoint that supports the Generic Guardrail API integration.
- The value `guardrail: generic_guardrail_api` must not be changed. This is the LiteLLM built-in guardrail type. However, you can customize the `guardrail_name` to any value you prefer.

### 3. Start LiteLLM Proxy[​](#3-start-litellm-proxy "Direct link to 3. Start LiteLLM Proxy")

```
litellm --config config.yaml --port 4000
```

### 4. Test the Integration[​](#4-test-the-integration "Direct link to 4. Test the Integration")

```
curl -X POST "http://localhost:4000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-master-key" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello, how are you?"}]
  }'
```

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you begin, ensure you have:

1. **Pillar Security Account**: Sign up at [Pillar Dashboard](https://app.pillar.security)
2. **API Credentials**: Get your API key from the dashboard
3. **LiteLLM Proxy**: Install and configure LiteLLM proxy

## Guardrail Modes[​](#guardrail-modes "Direct link to Guardrail Modes")

Pillar Security supports three execution modes for comprehensive protection:

ModeWhen It RunsWhat It ProtectsUse Case**`pre_call`**Before LLM callUser input onlyBlock malicious prompts, prevent prompt injection**`during_call`**Parallel with LLM callUser input onlyInput monitoring with lower latency**`post_call`**After LLM responseFull conversation contextOutput filtering, PII/PCI detection in responses

### Why Dual Mode is Recommended[​](#why-dual-mode-is-recommended "Direct link to Why Dual Mode is Recommended")

Recommended

Use `[pre_call, post_call]` for complete protection of both inputs and outputs.

- **Complete Protection**: Guards both incoming prompts and outgoing responses
- **Prompt Injection Defense**: Blocks malicious input before reaching the LLM
- **Response Monitoring**: Detects PII, secrets, or inappropriate content in outputs
- **Full Context Analysis**: Pillar sees the complete conversation for better detection

## Configuration Reference[​](#configuration-reference "Direct link to Configuration Reference")

### Core Parameters[​](#core-parameters "Direct link to Core Parameters")

ParameterDescription`guardrail`Must be `generic_guardrail_api` (do not change this value)`api_base`Must be `https://api.pillar.security/api/v1/integrations/litellm` (do not change this value)`api_key`Pillar API key (sent as `x-api-key` header)`mode`When to run: `pre_call`, `post_call`, `during_call`, or array like `[pre_call, post_call]``default_on`Enable guardrail for all requests by default

### Pillar-Specific Parameters[​](#pillar-specific-parameters "Direct link to Pillar-Specific Parameters")

These parameters are passed via `additional_provider_specific_params`:

ParameterTypeDescription`plr_mask`boolEnable automatic masking of sensitive data (PII, PCI, secrets) before sending to LLM`plr_evidence`boolInclude detection evidence in response`plr_scanners`boolInclude scanner details in response`plr_persist`boolPersist session data to Pillar dashboard

tip

**Enable `plr_mask: true`** to automatically sanitize sensitive data (PII, secrets, payment card info) before it reaches the LLM. Masked content is replaced with placeholders while original data is preserved in Pillar's audit logs.

## Configuration Examples[​](#configuration-examples "Direct link to Configuration Examples")

- Recommended (Dual Mode)
- Monitor Mode
- Input-Only Protection
- Low Latency Parallel

**Best for:**

- **Complete Protection**: Guards both incoming prompts and outgoing responses
- **Maximum Visibility**: Full scanner and evidence details for debugging
- **Production Use**: Persistent sessions for dashboard monitoring

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name: pillar-security
litellm_params:
guardrail: generic_guardrail_api
mode:[pre_call, post_call]
api_base: https://api.pillar.security/api/v1/integrations/litellm
api_key: os.environ/PILLAR_API_KEY
default_on:true
additional_provider_specific_params:
plr_mask:true
plr_evidence:true
plr_scanners:true
plr_persist:true

general_settings:
master_key:"your-secure-master-key-here"

litellm_settings:
set_verbose:true
```

## Response Detail Levels[​](#response-detail-levels "Direct link to Response Detail Levels")

Control what detection data is included in responses using `plr_scanners` and `plr_evidence`:

### Minimal Response[​](#minimal-response "Direct link to Minimal Response")

When both `plr_scanners` and `plr_evidence` are `false`:

```
{
"session_id":"abc-123",
"flagged":true
}
```

Use when you only care about whether Pillar detected a threat.

### Scanner Breakdown[​](#scanner-breakdown "Direct link to Scanner Breakdown")

When `plr_scanners: true`:

```
{
"session_id":"abc-123",
"flagged":true,
"scanners":{
"jailbreak":true,
"prompt_injection":false,
"pii":false,
"secret":false,
"toxic_language":false
}
}
```

Use when you need to know which categories triggered.

### Full Context[​](#full-context "Direct link to Full Context")

When both `plr_scanners: true` and `plr_evidence: true`:

```
{
"session_id":"abc-123",
"flagged":true,
"scanners":{
"jailbreak":true
},
"evidence":[
{
"category":"jailbreak",
"type":"prompt_injection",
"evidence":"Ignore previous instructions",
"metadata":{"start_idx":0,"end_idx":28}
}
]
}
```

Ideal for debugging, audit logs, or compliance exports.

tip

**Always set `plr_scanners: true` and `plr_evidence: true`** to see what Pillar detected. This is essential for troubleshooting and understanding security threats.

## Session Tracking[​](#session-tracking "Direct link to Session Tracking")

Pillar supports comprehensive session tracking using LiteLLM's metadata system:

```
curl -X POST "http://localhost:4000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-key" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello!"}],
    "user": "user-123",
    "metadata": {
      "pillar_session_id": "conversation-456"
    }
  }'
```

This provides clear, explicit conversation tracking that works seamlessly with LiteLLM's session management.

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

Set your Pillar API key as an environment variable:

```
export PILLAR_API_KEY=your-pillar-api-key
```

## Examples[​](#examples "Direct link to Examples")

- Safe Request
- Prompt Injection
- Secret Detection

**Safe request**

```
curl -X POST "http://localhost:4000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-master-key-here" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello! Can you tell me a joke?"}],
    "max_tokens": 100
  }'
```

**Expected response (Allowed):**

```
{
"id":"chatcmpl-BvQhm0VZpiDSEbrssSzO7GLHgHCkW",
"object":"chat.completion",
"created":1753027050,
"model":"gpt-4o",
"choices":[
{
"index":0,
"finish_reason":"stop",
"message":{
"role":"assistant",
"content":"Sure! Here's a joke for you:\n\nWhy don't scientists trust atoms?\nBecause they make up everything!"
}
}
]
}
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

- **Monitor your applications**: Use the [Pillar Dashboard](https://app.pillar.security) to view security events and analytics
- **Customize detection**: Configure specific scanners and thresholds for your use case
- **Scale your deployment**: Use LiteLLM's load balancing features with Pillar protection

## Support[​](#support "Direct link to Support")

Need help with your LiteLLM integration? Contact us at [support@pillar.security](mailto:support@pillar.security)

### Resources[​](#resources "Direct link to Resources")

- [Pillar Dashboard](https://app.pillar.security)
- [LiteLLM Documentation](https://docs.litellm.ai)
- [Pillar API Reference](https://docs.pillar.security/docs/api/introduction)