---
title: Gray Swan Cygnal Guardrail | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/grayswan
source: sitemap
fetched_at: 2026-01-21T19:52:10.839231147-03:00
rendered_js: false
word_count: 352
summary: This document explains how to integrate Gray Swan Cygnal as a safety guardrail within LiteLLM to monitor and manage LLM requests for policy violations and prompt injections.
tags:
    - litellm
    - gray-swan-cygnal
    - guardrails
    - llm-security
    - prompt-injection
    - safety-monitoring
category: guide
---

Use [Gray Swan Cygnal](https://docs.grayswan.ai/cygnal/monitor-requests) to continuously monitor conversations for policy violations, indirect prompt injection (IPI), jailbreak attempts, and other safety risks.

Cygnal returns a `violation` score between `0` and `1` (higher means more likely to violate policy), plus metadata such as violated rule indices, mutation detection, and IPI flags. LiteLLM can automatically block or monitor requests based on this signal.

* * *

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Obtain Credentials[​](#1-obtain-credentials "Direct link to 1. Obtain Credentials")

1. Create a Gray Swan account and generate a Cygnal API key.
2. Configure environment variables for the LiteLLM proxy host:

```
export GRAYSWAN_API_KEY="your-grayswan-key"
export GRAYSWAN_API_BASE="https://api.grayswan.ai"
```

### 2. Configure `config.yaml`[​](#2-configure-configyaml "Direct link to 2-configure-configyaml")

Add a guardrail entry that references the Gray Swan integration. Below is a balanced example that monitors both input and output but only blocks once the violation score reaches the configured threshold.

```
model_list:
-model_name: openai/gpt-4.1-mini
litellm_params:
model: openai/gpt-4.1-mini
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"cygnal-monitor"
litellm_params:
guardrail: grayswan
mode:[pre_call, post_call]# monitor both input and output
api_key: os.environ/GRAYSWAN_API_KEY
api_base: os.environ/GRAYSWAN_API_BASE  # optional
optional_params:
on_flagged_action: monitor             # or "block"
violation_threshold:0.5# score >= threshold is flagged
reasoning_mode: hybrid                 # off | hybrid | thinking
categories:
safety:"Detect jailbreaks and policy violations"
policy_id:"your-cygnal-policy-id"
default_on:true

general_settings:
master_key:"your-litellm-master-key"

litellm_settings:
set_verbose:true
```

### 3. Launch the Proxy[​](#3-launch-the-proxy "Direct link to 3. Launch the Proxy")

```
litellm --config config.yaml --port 4000
```

* * *

## Choosing Guardrail Modes[​](#choosing-guardrail-modes "Direct link to Choosing Guardrail Modes")

Gray Swan can run during `pre_call`, `during_call`, and `post_call` stages. Combine modes based on your latency and coverage requirements.

ModeWhen it RunsProtectsTypical Use Case`pre_call`Before LLM callUser input onlyBlock prompt injection before it reaches the model`during_call`Parallel to callUser input onlyLow-latency monitoring without blocking`post_call`After responseFull conversationScan output for policy violations, leaked secrets, or IPI

When using `during_call` with `on_flagged_action: block` or `on_flagged_action: passthrough`:

- **The LLM call runs in parallel** with the guardrail check using `asyncio.gather`
- **LLM tokens are still consumed** even if the guardrail detects a violation
- The guardrail exception prevents the response from reaching the user, but **does not cancel the running LLM task**
- This means you pay full LLM costs while returning an error/passthrough message to the user

**Recommendation:** For cost-sensitive applications, use `pre_call` and `post_call` instead of `during_call` for blocking or passthrough modes. Reserve `during_call` for `monitor` mode where you want low-latency logging without impacting the user experience.

- Monitor Only
- Block Input
- Full Coverage
- Passthrough Mode

```
guardrails:
-guardrail_name:"cygnal-monitor-only"
litellm_params:
guardrail: grayswan
mode:"during_call"
api_key: os.environ/GRAYSWAN_API_KEY
optional_params:
on_flagged_action: monitor
violation_threshold:0.6
default_on:true
```

Best for visibility without blocking. Alerts are logged via LiteLLM’s standard logging callbacks.

* * *

## Configuration Reference[​](#configuration-reference "Direct link to Configuration Reference")

ParameterTypeDescription`api_key`stringGray Swan Cygnal API key. Reads from `GRAYSWAN_API_KEY` if omitted.`mode`string or listGuardrail stages (`pre_call`, `during_call`, `post_call`).`optional_params.on_flagged_action`string`monitor` (log only), `block` (raise `HTTPException`), or `passthrough` (replace response content with violation message, no 400 error).`.optional_params.violation_threshold`number (0-1)Scores at or above this value are considered violations.`optional_params.reasoning_mode`string`off`, `hybrid`, or `thinking`. Enables Cygnal's reasoning capabilities.`optional_params.categories`objectMap of custom category names to descriptions.`optional_params.policy_id`stringGray Swan policy identifier.