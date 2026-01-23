---
title: PII, PHI Masking - Presidio | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2
source: sitemap
fetched_at: 2026-01-21T19:52:30.031127748-03:00
rendered_js: false
word_count: 1128
summary: This document explains how to configure and deploy the Microsoft Presidio guardrail in LiteLLM to mask or block sensitive PII and PHI data in LLM requests and responses.
tags:
    - pii-masking
    - presidio
    - litellm
    - data-privacy
    - security-guardrails
    - phi-protection
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionUse this guardrail to mask PII (Personally Identifiable Information), PHI (Protected Health Information), and other sensitive data.Provider[Microsoft Presidio](https://github.com/microsoft/presidio/)Supported Entity TypesAll Presidio Entity TypesSupported Actions`MASK`, `BLOCK`Supported Modes`pre_call`, `during_call`, `post_call`, `logging_only`, `pre_mcp_call`Language SupportConfigurable via `presidio_language` parameter (supports multiple languages including English, Spanish, German, etc.)

## Deployment options[​](#deployment-options "Direct link to Deployment options")

For this guardrail you need a deployed Presidio Analyzer and Presido Anonymizer containers.

Deployment OptionDetailsDeploy Presidio Docker Containers- [Presidio Analyzer Docker Container](https://hub.docker.com/r/microsoft/presidio-analyzer)  
\- [Presidio Anonymizer Docker Container](https://hub.docker.com/r/microsoft/presidio-anonymizer)

## Quick Start[​](#quick-start "Direct link to Quick Start")

- LiteLLM UI
- Config.yaml

### 1. Create a PII, PHI Masking Guardrail[​](#1-create-a-pii-phi-masking-guardrail "Direct link to 1. Create a PII, PHI Masking Guardrail")

On the LiteLLM UI, navigate to Guardrails. Click "Add Guardrail". On this dropdown select "Presidio PII" and enter your presidio analyzer and anonymizer endpoints.

#### 1.2 Configure Entity Types[​](#12-configure-entity-types "Direct link to 1.2 Configure Entity Types")

Now select the entity types you want to mask. See the [supported actions here](#supported-actions)

#### 1.3 Set Default Language (Optional)[​](#13-set-default-language-optional "Direct link to 1.3 Set Default Language (Optional)")

You can also configure a default language for PII analysis using the `presidio_language` field in the UI. This sets the default language that will be used for all requests unless overridden by a per-request language setting.

**Supported language codes include:**

- `en` - English (default)
- `es` - Spanish
- `de` - German

If not specified, English (`en`) will be used as the default language.

### 3. Test it\![​](#3-test-it "Direct link to 3. Test it!")

#### 3.1 LiteLLM UI[​](#31-litellm-ui "Direct link to 3.1 LiteLLM UI")

On the litellm UI, navigate to the 'Test Keys' page, select the guardrail you created and send the following messaged filled with PII data.

PII Request

```
My credit card is 4111-1111-1111-1111 and my email is test@example.com.
```

#### 3.2 Test in code[​](#32-test-in-code "Direct link to 3.2 Test in code")

In order to apply a guardrail for a request send `guardrails=["presidio-pii"]` in the request body.

[**Langchain, OpenAI SDK Usage Examples**](https://docs.litellm.ai/docs/proxy/proxy/user_keys#request-format)

- Masked PII call
- No PII Call

Expect this to mask `Jane Doe` since it's PII

Masked PII Request

```
curl http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "Hello my name is Jane Doe"}
    ],
    "guardrails": ["presidio-pii"],
  }'
```

Expected response on failure

Response with Masked PII

```
{
 "id": "chatcmpl-A3qSC39K7imjGbZ8xCDacGJZBoTJQ",
 "choices": [
   {
     "finish_reason": "stop",
     "index": 0,
     "message": {
       "content": "Hello, <PERSON>! How can I assist you today?",
       "role": "assistant",
       "tool_calls": null,
       "function_call": null
     }
   }
 ],
 "created": 1725479980,
 "model": "gpt-3.5-turbo-2024-07-18",
 "object": "chat.completion",
 "system_fingerprint": "fp_5bd87c427a",
 "usage": {
   "completion_tokens": 13,
   "prompt_tokens": 14,
   "total_tokens": 27
 },
 "service_tier": null
}
```

## Tracing Guardrail requests[​](#tracing-guardrail-requests "Direct link to Tracing Guardrail requests")

Once your guardrail is live in production, you will also be able to trace your guardrail on LiteLLM Logs, Langfuse, Arize Phoenix, etc, all LiteLLM logging integrations.

### LiteLLM UI[​](#litellm-ui "Direct link to LiteLLM UI")

On the LiteLLM logs page you can see that the PII content was masked for this specific request. And you can see detailed tracing for the guardrail. This allows you to monitor entity types masked with their corresponding confidence score and the duration of the guardrail execution.

### Langfuse[​](#langfuse "Direct link to Langfuse")

When connecting Litellm to Langfuse, you can see the guardrail information on the Langfuse Trace.

## Entity Types, Detection Confidence Score Threshold, and Scope Configuration[​](#entity-types-detection-confidence-score-threshold-and-scope-configuration "Direct link to Entity Types, Detection Confidence Score Threshold, and Scope Configuration")

- **Entity Types**
  
  - You can configure specific entity types for PII detection and decide how to handle each entity type (mask or block).
- **Detection Confidence Score Threshold**
  
  - You can also provide an optional confidence score threshold at which detections will be passed to the anonymizer. Entities without an entry in `presidio_score_thresholds` keep all detections (no minimum score).
- **Scope**
  
  - Use the optional `presidio_filter_scope` to choose where checks run:
    
    - `input`: only user → model content is scanned
    - `output`: only model → user content is scanned
    - `both` (default): scan both directions
    
    **What about `output_parse_pii`?**  
    This flag only un-masks tokens back to the originals after the model call; it does not run Presidio detection on outputs. Use `presidio_filter_scope: output` (or `both`) when you want Presidio to actively scan and mask the model’s response before it reaches the user.
    
    **When to pick input vs output:**
    
    - `input`: Protect upstream providers; strip PII before it leaves your boundary.
    - `output`: Catch PII the model might generate or leak back to users.
    - `both`: End-to-end protection in both directions.

### Configure Entity Types, Detection Confidence Score Threshold, and Scope in `config.yaml`[​](#configure-entity-types-detection-confidence-score-threshold-and-scope-in-configyaml "Direct link to configure-entity-types-detection-confidence-score-threshold-and-scope-in-configyaml")

Define your guardrails with specific entity type configuration:

config.yaml with Entity Types

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"presidio-mask-guard"
litellm_params:
guardrail: presidio
mode:"pre_mcp_call"# Use this mode for MCP requests
presidio_filter_scope: both  # input | output | both, optional
presidio_score_thresholds:# Optional
ALL:0.7# Default confidence threshold applied to all entities
CREDIT_CARD:0.8# Override for credit cards
EMAIL_ADDRESS:0.6# Override for emails
pii_entities_config:
CREDIT_CARD:"MASK"# Will mask credit card numbers
EMAIL_ADDRESS:"MASK"# Will mask email addresses

-guardrail_name:"presidio-block-guard"
litellm_params:
guardrail: presidio
mode:"pre_call"# Use this mode for regular LLM requests
presidio_filter_scope: both  # input | output | both, optional
presidio_score_thresholds:# Optional
CREDIT_CARD:0.8# Only keep credit card detections scoring 0.8+
pii_entities_config:
CREDIT_CARD:"BLOCK"# Will block requests containing credit card numbers
```

#### Confidence threshold behavior:[​](#confidence-threshold-behavior "Direct link to Confidence threshold behavior:")

- No `presidio_score_thresholds`: keep all detections (no thresholds applied)
- `presidio_score_thresholds.ALL`: apply this confidence threshold to every detection
- `presidio_score_thresholds.<ENTITY>`: apply only to that entity
- If both `ALL` and an entity override exist, `ALL` applies globally and the entity override takes precedence for that entity

### Supported Entity Types[​](#supported-entity-types "Direct link to Supported Entity Types")

LiteLLM Supports all Presidio entity types. See the complete list of presidio entity types [here](https://microsoft.github.io/presidio/supported_entities/).

### Supported Actions[​](#supported-actions "Direct link to Supported Actions")

For each entity type, you can specify one of the following actions:

- `MASK`: Replace the entity with a placeholder (e.g., `<PERSON>`)
- `BLOCK`: Block the request entirely if this entity type is detected

### Test request with Entity Type Configuration[​](#test-request-with-entity-type-configuration "Direct link to Test request with Entity Type Configuration")

- Masking PII entities
- Blocking PII entities

When using the masking configuration, entities will be replaced with placeholders:

Masking PII Request

```
curl http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "My credit card is 4111-1111-1111-1111 and my email is test@example.com"}
    ],
    "guardrails": ["presidio-mask-guard"]
  }'
```

Example response with masked entities:

```
{
"id":"chatcmpl-123abc",
"choices":[
{
"message":{
"content":"I can see you provided a <CREDIT_CARD> and an <EMAIL_ADDRESS>. For security reasons, I recommend not sharing this sensitive information.",
"role":"assistant"
},
"index":0,
"finish_reason":"stop"
}
],
// ... other response fields
}
```

## Advanced[​](#advanced "Direct link to Advanced")

### Supported Modes[​](#supported-modes "Direct link to Supported Modes")

The Presidio guardrail supports the following modes:

- `pre_call`: Run **before** LLM call, on **input**
- `post_call`: Run **after** LLM call, on **input & output**
- `logging_only`: Run **after** LLM call, only apply PII Masking before logging to Langfuse, etc. Not on the actual llm api request / response
- `pre_mcp_call`: Run **before** MCP call, on **input**. Use this mode when you want to apply PII masking/blocking for MCP requests

### MCP Usage Example[​](#mcp-usage-example "Direct link to MCP Usage Example")

Here's how to use Presidio guardrails with MCP:

MCP Configuration Example

```
guardrails:
-guardrail_name:"presidio-mcp-guard"
litellm_params:
guardrail: presidio
mode:"pre_mcp_call"
presidio_filter_scope: both  # input | output | both
presidio_score_thresholds:
CREDIT_CARD:0.8# Only keep credit card detections scoring 0.8+
EMAIL_ADDRESS:0.6# Only keep email detections scoring 0.6+
pii_entities_config:
CREDIT_CARD:"MASK"# Will mask credit card numbers
EMAIL_ADDRESS:"BLOCK"# Will block email addresses
PHONE_NUMBER:"MASK"# Will mask phone numbers
MEDICAL_LICENSE:"BLOCK"# Will block medical license numbers
default_on:true
```

Test the MCP guardrail with a request:

Test MCP Guardrail

```
curl http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "My credit card is 4111-1111-1111-1111 and my medical license is ABC123"}
    ],
    "guardrails": ["presidio-mcp-guard"]
  }'
```

The request will be processed as follows:

1. Credit card number will be masked (e.g., replaced with `<CREDIT_CARD>`)
2. If a medical license is detected, the request will be blocked with a `BlockedPiiEntityError`

### Set `language` per request[​](#set-language-per-request "Direct link to set-language-per-request")

The Presidio API [supports passing the `language` param](https://microsoft.github.io/presidio/api-docs/api-docs.html#tag/Analyzer/paths/~1analyze/post). Here is how to set the `language` per request

- curl
- OpenAI Python SDK

Language Parameter - curl

```
curl http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "is this credit card number 9283833 correct?"}
    ],
    "guardrails": ["presidio-pre-guard"],
    "guardrail_config": {"language": "es"}
  }'
```

### Set default `language` in config.yaml[​](#set-default-language-in-configyaml "Direct link to set-default-language-in-configyaml")

You can configure a default language for PII analysis in your YAML configuration using the `presidio_language` parameter. This language will be used for all requests unless overridden by a per-request language setting.

Default Language Configuration

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"presidio-german"
litellm_params:
guardrail: presidio
mode:"pre_call"
presidio_language:"de"# Default to German for PII analysis
pii_entities_config:
CREDIT_CARD:"MASK"
EMAIL_ADDRESS:"MASK"
PERSON:"MASK"

-guardrail_name:"presidio-spanish"
litellm_params:
guardrail: presidio
mode:"pre_call"
presidio_language:"es"# Default to Spanish for PII analysis
pii_entities_config:
CREDIT_CARD:"MASK"
PHONE_NUMBER:"MASK"
```

#### Supported Language Codes[​](#supported-language-codes "Direct link to Supported Language Codes")

Presidio supports multiple languages for PII detection. Common language codes include:

- `en` - English (default)
- `es` - Spanish
- `de` - German

For a complete list of supported languages, refer to the [Presidio documentation](https://microsoft.github.io/presidio/analyzer/languages/).

#### Language Precedence[​](#language-precedence "Direct link to Language Precedence")

The language setting follows this precedence order:

1. **Per-request language** (via `guardrail_config.language`) - highest priority
2. **YAML config language** (via `presidio_language`) - medium priority
3. **Default language** (`en`) - lowest priority

**Example with mixed languages:**

Mixed Language Configuration

```
guardrails:
-guardrail_name:"presidio-multilingual"
litellm_params:
guardrail: presidio
mode:"pre_call"
presidio_language:"de"# Default to German
pii_entities_config:
CREDIT_CARD:"MASK"
PERSON:"MASK"
```

Override with per-request language

```
curl http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "Mi tarjeta de crédito es 4111-1111-1111-1111"}
    ],
    "guardrails": ["presidio-multilingual"],
    "guardrail_config": {"language": "es"}
  }'
```

In this example, the request will use Spanish (`es`) for PII detection even though the guardrail is configured with German (`de`) as the default language.

### Output parsing[​](#output-parsing "Direct link to Output parsing")

LLM responses can sometimes contain the masked tokens.

For presidio 'replace' operations, LiteLLM can check the LLM response and replace the masked token with the user-submitted values.

Define your guardrails under the `guardrails` section

Output Parsing Config

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"presidio-pre-guard"
litellm_params:
guardrail: presidio  # supported values: "aporia", "bedrock", "lakera", "presidio"
mode:"pre_call"
output_parse_pii:True
```

\*\*Expected Flow: \**

1. User Input: "hello world, my name is Jane Doe. My number is: 034453334"
2. LLM Input: "hello world, my name is \[PERSON]. My number is: \[PHONE\_NUMBER]"
3. LLM Response: "Hey \[PERSON], nice to meet you!"
4. User Response: "Hey Jane Doe, nice to meet you!"

### Ad Hoc Recognizers[​](#ad-hoc-recognizers "Direct link to Ad Hoc Recognizers")

Send ad-hoc recognizers to presidio `/analyze` by passing a json file to the proxy

[**Example** ad-hoc recognizer](https://github.com/BerriAI/litellm/blob/b69b7503db5aa039a49b7ca96ae5b34db0d25a3d/litellm/proxy/hooks/example_presidio_ad_hoc_recognizer.json)

Define your guardrails under the `guardrails` section

Ad Hoc Recognizers Config

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"presidio-pre-guard"
litellm_params:
guardrail: presidio  # supported values: "aporia", "bedrock", "lakera", "presidio"
mode:"pre_call"
presidio_ad_hoc_recognizers:"./hooks/example_presidio_ad_hoc_recognizer.json"
```

Set the following env vars

Ad Hoc Recognizers Environment Variables

```
export PRESIDIO_ANALYZER_API_BASE="http://localhost:5002"
export PRESIDIO_ANONYMIZER_API_BASE="http://localhost:5001"
```

You can see this working, when you run the proxy:

Run Proxy with Debug

```
litellm --config /path/to/config.yaml --debug
```

Make a chat completions request, example:

Custom PII Request

```
{
"model":"azure-gpt-3.5",
"messages":[{"role":"user","content":"John Smith AHV number is 756.3026.0705.92. Zip code: 1334023"}]
}
```

And search for any log starting with `Presidio PII Masking`, example:

PII Masking Log

```
Presidio PII Masking: Redacted pii message: <PERSON> AHV number is <AHV_NUMBER>. Zip code: <US_DRIVER_LICENSE>
```

### Logging Only[​](#logging-only "Direct link to Logging Only")

Only apply PII Masking before logging to Langfuse, etc.

Not on the actual llm api request / response.

note

This is currently only applied for

- `/chat/completion` requests
- on 'success' logging

<!--THE END-->

1. Define mode: `logging_only` on your LiteLLM config.yaml

Define your guardrails under the `guardrails` section

Logging Only Config

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"presidio-pre-guard"
litellm_params:
guardrail: presidio  # supported values: "aporia", "bedrock", "lakera", "presidio"
mode:"logging_only"
```

Set the following env vars

Logging Only Environment Variables

```
export PRESIDIO_ANALYZER_API_BASE="http://localhost:5002"
export PRESIDIO_ANONYMIZER_API_BASE="http://localhost:5001"
```

2. Start proxy

Start Proxy

```
litellm --config /path/to/config.yaml
```

3. Test it!

Test Logging Only

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-D '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "Hi, my name is Jane!"
    }
  ]
  }'
```

**Expected Logged Response**

Logged Response with Masked PII