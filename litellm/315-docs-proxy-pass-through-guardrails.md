---
title: Guardrails on Pass-Through Endpoints | liteLLM
url: https://docs.litellm.ai/docs/proxy/pass_through_guardrails
source: sitemap
fetched_at: 2026-01-21T19:53:11.768480724-03:00
rendered_js: false
word_count: 432
summary: This document explains how to enable and configure security guardrails for LiteLLM pass-through endpoints using the UI or YAML configuration files. It covers field-level targeting with JSONPath, inheritance from organizational levels, and pre-call and post-call validation flows.
tags:
    - litellm
    - guardrails
    - pass-through-endpoints
    - api-security
    - jsonpath
    - content-moderation
    - endpoint-configuration
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionEnable guardrail execution on LiteLLM pass-through endpoints with opt-in activation and automatic inheritance from org/team/key levelsSupported GuardrailsAll LiteLLM guardrails (Bedrock, Aporia, Lakera, etc.)Default BehaviorGuardrails are **disabled** on pass-through endpoints unless explicitly enabled

## Quick Start[​](#quick-start "Direct link to Quick Start")

You can configure guardrails on pass-through endpoints either via the **UI** (recommended) or **config file**.

### Using the UI[​](#using-the-ui "Direct link to Using the UI")

#### 1. Navigate to Pass-Through Endpoints[​](#1-navigate-to-pass-through-endpoints "Direct link to 1. Navigate to Pass-Through Endpoints")

Go to **Models + Endpoints** → Click **+ Add Pass-Through Endpoint**

Scroll to the **Guardrails** section and select which guardrails to enforce.

Default Behavior

By default, you don't need to specify fields - LiteLLM will JSON dump the entire request/response payload and send it to the guardrail.

#### 2. Target Specific Fields (Optional)[​](#2-target-specific-fields-optional "Direct link to 2. Target Specific Fields (Optional)")

To check only specific fields instead of the entire payload:

1. Select your guardrails
2. In **Field Targeting (Optional)**, specify fields for each guardrail
3. Use the quick-add buttons (`+ query`, `+ documents[*]`) or type custom JSONPath expressions
4. **Request Fields (pre\_call)**: Fields to check before sending to target API
5. **Response Fields (post\_call)**: Fields to check in the response from target API

**Example**: In the screenshot above, we set `query` as a request field, so only the `query` field is sent to the guardrail instead of the entire request.

* * *

### Using Config File[​](#using-config-file "Direct link to Using Config File")

#### 1. Define guardrails and pass-through endpoint[​](#1-define-guardrails-and-pass-through-endpoint "Direct link to 1. Define guardrails and pass-through endpoint")

config.yaml

```
guardrails:
-guardrail_name:"pii-guard"
litellm_params:
guardrail: bedrock
mode: pre_call
guardrailIdentifier:"your-guardrail-id"
guardrailVersion:"1"

general_settings:
pass_through_endpoints:
-path:"/v1/rerank"
target:"https://api.cohere.com/v1/rerank"
headers:
Authorization:"bearer os.environ/COHERE_API_KEY"
guardrails:
        pii-guard:
```

#### 2. Start proxy[​](#2-start-proxy "Direct link to 2. Start proxy")

```
litellm --config config.yaml
```

#### 3. Test request[​](#3-test-request "Direct link to 3. Test request")

```
curl -X POST "http://localhost:4000/v1/rerank" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "rerank-english-v3.0",
    "query": "What is the capital of France?",
    "documents": ["Paris is the capital of France."]
  }'
```

* * *

## Opt-In Behavior[​](#opt-in-behavior "Direct link to Opt-In Behavior")

ConfigurationBehavior`guardrails` not setNo guardrails execute (default)`guardrails` setAll org/team/key + pass-through guardrails execute

When guardrails are enabled, the system collects and executes:

- Org-level guardrails
- Team-level guardrails
- Key-level guardrails
- Pass-through specific guardrails

* * *

## How It Works[​](#how-it-works "Direct link to How It Works")

The diagram below shows what happens when a client makes a request to `/special/rerank` - a pass-through endpoint configured with guardrails in your `config.yaml`.

When guardrails are configured on a pass-through endpoint:

1. **Pre-call guardrails** run on the request before forwarding to the target API
2. If `request_fields` is specified (e.g., `["query"]`), only those fields are sent to the guardrail. Otherwise, the entire request payload is evaluated.
3. The request is forwarded to the target API only if guardrails pass
4. **Post-call guardrails** run on the response from the target API
5. If `response_fields` is specified (e.g., `["results[*].text"]`), only those fields are evaluated. Otherwise, the entire response is checked.

info

If the `guardrails` block is omitted or empty in your pass-through endpoint config, the request skips the guardrail flow entirely and goes directly to the target API.

* * *

## Field-Level Targeting[​](#field-level-targeting "Direct link to Field-Level Targeting")

Target specific JSON fields instead of the entire request/response payload.

config.yaml

```
guardrails:
-guardrail_name:"pii-detection"
litellm_params:
guardrail: bedrock
mode: pre_call
guardrailIdentifier:"pii-guard-id"
guardrailVersion:"1"

-guardrail_name:"content-moderation"
litellm_params:
guardrail: bedrock
mode: post_call
guardrailIdentifier:"content-guard-id"
guardrailVersion:"1"

general_settings:
pass_through_endpoints:
-path:"/v1/rerank"
target:"https://api.cohere.com/v1/rerank"
headers:
Authorization:"bearer os.environ/COHERE_API_KEY"
guardrails:
pii-detection:
request_fields:["query","documents[*].text"]
content-moderation:
response_fields:["results[*].text"]
```

### Field Options[​](#field-options "Direct link to Field Options")

FieldDescription`request_fields`JSONPath expressions for input (pre\_call)`response_fields`JSONPath expressions for output (post\_call)Neither specifiedGuardrail runs on entire payload

### JSONPath Examples[​](#jsonpath-examples "Direct link to JSONPath Examples")

ExpressionMatches`query`Single field named `query``documents[*].text`All `text` fields in `documents` array`messages[*].content`All `content` fields in `messages` array

* * *

## Configuration Examples[​](#configuration-examples "Direct link to Configuration Examples")

### Single guardrail on entire payload[​](#single-guardrail-on-entire-payload "Direct link to Single guardrail on entire payload")

config.yaml

```
guardrails:
-guardrail_name:"pii-detection"
litellm_params:
guardrail: bedrock
mode: pre_call
guardrailIdentifier:"your-id"
guardrailVersion:"1"

general_settings:
pass_through_endpoints:
-path:"/v1/rerank"
target:"https://api.cohere.com/v1/rerank"
guardrails:
        pii-detection:
```

### Multiple guardrails with mixed settings[​](#multiple-guardrails-with-mixed-settings "Direct link to Multiple guardrails with mixed settings")

config.yaml

```
guardrails:
-guardrail_name:"pii-detection"
litellm_params:
guardrail: bedrock
mode: pre_call
guardrailIdentifier:"pii-id"
guardrailVersion:"1"

-guardrail_name:"content-moderation"
litellm_params:
guardrail: bedrock
mode: post_call
guardrailIdentifier:"content-id"
guardrailVersion:"1"

-guardrail_name:"prompt-injection"
litellm_params:
guardrail: lakera
mode: pre_call
api_key: os.environ/LAKERA_API_KEY

general_settings:
pass_through_endpoints:
-path:"/v1/rerank"
target:"https://api.cohere.com/v1/rerank"
guardrails:
pii-detection:
request_fields:["input","query"]
content-moderation:
prompt-injection:
request_fields:["messages[*].content"]
```