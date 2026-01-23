---
title: /guardrails/apply_guardrail | liteLLM
url: https://docs.litellm.ai/docs/apply_guardrail
source: sitemap
fetched_at: 2026-01-21T19:44:03.094804563-03:00
rendered_js: false
word_count: 239
summary: This document explains how to use the LiteLLM apply_guardrail endpoint to directly invoke safety and moderation guardrails such as Presidio and Bedrock. It provides configuration instructions, request and response schemas, and details on supported guardrail types.
tags:
    - litellm
    - api-endpoint
    - guardrails
    - pii-masking
    - content-moderation
    - bedrock
    - presidio
    - ai-safety
category: api
---

Use this endpoint to directly call a guardrail configured on your LiteLLM instance. This is useful when you have services that need to directly call a guardrail.

## Supported Guardrail Types[​](#supported-guardrail-types "Direct link to Supported Guardrail Types")

This endpoint supports various guardrail types including:

- **Presidio** - PII detection and masking
- **Bedrock** - AWS Bedrock guardrails for content moderation
- **Lakera** - AI safety guardrails
- **Custom guardrails** - User-defined guardrails

## Configuration[​](#configuration "Direct link to Configuration")

### Bedrock Guardrail Configuration[​](#bedrock-guardrail-configuration "Direct link to Bedrock Guardrail Configuration")

To use Bedrock guardrails with the apply\_guardrail endpoint, configure your guardrail in your LiteLLM config.yaml:

```
guardrails:
-guardrail_name:"bedrock-content-guard"
litellm_params:
guardrail: bedrock
mode:"pre_call"
guardrailIdentifier:"your-guardrail-id"# Your actual Bedrock guardrail ID
guardrailVersion:"DRAFT"# or your version number
aws_region_name:"us-east-1"# Your AWS region
aws_role_name:"your-role-arn"# Your AWS role with Bedrock permissions
default_on:true
```

**Required AWS Setup:**

1. Create a Bedrock guardrail in AWS Console
2. Get the guardrail ID and version
3. Ensure your AWS credentials have Bedrock permissions
4. Configure the guardrail in your LiteLLM config

## Usage[​](#usage "Direct link to Usage")

* * *

- Presidio PII Guardrail
- Bedrock Guardrail

In this example `mask_pii` is a Presidio guardrail configured on LiteLLM.

Example calling the endpoint

```
curl -X POST 'http://localhost:4000/guardrails/apply_guardrail' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer your-api-key' \
-d '{
    "guardrail_name": "mask_pii",
    "text": "My name is John Doe and my email is john@example.com",
    "language": "en",
    "entities": ["NAME", "EMAIL"]
}'
```

## Request Format[​](#request-format "Direct link to Request Format")

* * *

The request body should follow the ApplyGuardrailRequest format.

#### Example Request Body[​](#example-request-body "Direct link to Example Request Body")

```
{
"guardrail_name":"mask_pii",
"text":"My name is John Doe and my email is john@example.com",
"language":"en",
"entities":["NAME","EMAIL"]
}
```

#### Required Fields[​](#required-fields "Direct link to Required Fields")

- **guardrail\_name** (string):  
  The identifier for the guardrail to apply (e.g., "mask\_pii").
- **text** (string):  
  The input text to process through the guardrail.

#### Optional Fields[​](#optional-fields "Direct link to Optional Fields")

- **language** (string):  
  The language of the input text (e.g., "en" for English).
- **entities** (array of strings):  
  Specific entities to process or filter (e.g., \["NAME", "EMAIL"]).

## Response Format[​](#response-format "Direct link to Response Format")

* * *

The response will contain the processed text after applying the guardrail.

#### Example Response[​](#example-response "Direct link to Example Response")

- Presidio Response
- Bedrock Response

```
{
"response_text":"My name is [REDACTED] and my email is [REDACTED]"
}
```

#### Response Fields[​](#response-fields "Direct link to Response Fields")

- **response\_text** (string):  
  The text after applying the guardrail.

#### Error Responses[​](#error-responses "Direct link to Error Responses")

If a guardrail blocks content (e.g., Bedrock guardrail), the endpoint will return an error:

```
{
"detail":"Content blocked by Bedrock guardrail: Content violates policy"
}
```