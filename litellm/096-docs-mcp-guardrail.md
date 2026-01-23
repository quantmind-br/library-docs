---
title: MCP Guardrails | liteLLM
url: https://docs.litellm.ai/docs/mcp_guardrail
source: sitemap
fetched_at: 2026-01-21T19:45:43.869826869-03:00
rendered_js: false
word_count: 191
summary: This document explains how to configure and implement security guardrails for MCP tool calls in LiteLLM to validate inputs and protect sensitive information.
tags:
    - litellm
    - mcp-tools
    - guardrails
    - data-security
    - pii-masking
    - input-validation
    - model-context-protocol
category: guide
---

LiteLLM supports applying guardrails to MCP tool calls to ensure security and compliance. You can configure guardrails to run before or during MCP calls to validate inputs and block or mask sensitive information.

### Supported MCP Guardrail Modes[​](#supported-mcp-guardrail-modes "Direct link to Supported MCP Guardrail Modes")

MCP guardrails support the following modes:

- `pre_mcp_call`: Run **before** MCP call, on **input**. Use this mode when you want to apply validation/masking/blocking for MCP requests
- `during_mcp_call`: Run **during** MCP call execution. Use this mode for real-time monitoring and intervention

### Configuration Examples[​](#configuration-examples "Direct link to Configuration Examples")

Configure guardrails to run before MCP tool calls to validate and sanitize inputs:

config.yaml

```
guardrails:
-guardrail_name:"mcp-input-validation"
litellm_params:
guardrail: presidio  # or other supported guardrails
mode:"pre_mcp_call"# or during_mcp_call
pii_entities_config:
CREDIT_CARD:"BLOCK"# Will block requests containing credit card numbers
EMAIL_ADDRESS:"MASK"# Will mask email addresses
PHONE_NUMBER:"MASK"# Will mask phone numbers
default_on:true
```

### Usage Examples[​](#usage-examples "Direct link to Usage Examples")

#### Testing Pre-MCP Call Guardrails[​](#testing-pre-mcp-call-guardrails "Direct link to Testing Pre-MCP Call Guardrails")

Test your MCP guardrails with a request that includes sensitive information:

Test MCP Guardrail

```
curl http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "My credit card is 4111-1111-1111-1111 and my email is john@example.com"}
    ],
    "guardrails": ["mcp-input-validation"]
  }'
```

The request will be processed as follows:

1. Credit card number will be blocked (request rejected)
2. Email address will be masked (e.g., replaced with `<EMAIL_ADDRESS>`)

#### Using with MCP Tools[​](#using-with-mcp-tools "Direct link to Using with MCP Tools")

When using MCP tools, guardrails will be applied to the tool inputs:

Python Example with MCP Guardrails

```
import openai

client = openai.OpenAI(
    api_key="your-api-key",
    base_url="http://localhost:4000"
)

# This request will trigger MCP guardrails
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
{"role":"user","content":"Send an email to 555-123-4567 with my SSN 123-45-6789"}
],
    tools=[{"type":"mcp","server_label":"litellm","server_url":"litellm_proxy"}],
    guardrails=["mcp-input-validation"]
)
```

### Supported Guardrail Providers[​](#supported-guardrail-providers "Direct link to Supported Guardrail Providers")

MCP guardrails work with all LiteLLM-supported guardrail providers:

- **Presidio**: PII detection and masking
- **Bedrock**: AWS Bedrock guardrails
- **Lakera**: Content moderation
- **Aporia**: Custom guardrails
- **Noma**: Noma Security
- **Custom**: Your own guardrail implementations