---
title: Diagnosing Errors - Provider vs Gateway | liteLLM
url: https://docs.litellm.ai/docs/proxy/error_diagnosis
source: sitemap
fetched_at: 2026-01-21T19:51:56.185612111-03:00
rendered_js: false
word_count: 204
summary: This guide explains how to identify whether an error message originates from an LLM provider or the LiteLLM AI Gateway by looking for specific exception prefixes.
tags:
    - litellm
    - error-handling
    - debugging
    - troubleshooting
    - exception-mapping
    - api-gateway
category: guide
---

Having trouble diagnosing if an error is from the **LLM Provider** (OpenAI, Anthropic, etc.) or from the **LiteLLM AI Gateway** itself? Here's how to tell.

## Quick Rule[​](#quick-rule "Direct link to Quick Rule")

**If the error contains `<Provider>Exception`, it's from the provider.**

Error ContainsError Source`AnthropicException`Anthropic`OpenAIException`OpenAI`AzureException`Azure`BedrockException`AWS Bedrock`VertexAIException`Google Vertex AINo provider nameLiteLLM AI Gateway

## Examples[​](#examples "Direct link to Examples")

### Provider Error (from AWS Bedrock)[​](#provider-error-from-aws-bedrock "Direct link to Provider Error (from AWS Bedrock)")

```
{
  "error": {
    "message": "litellm.BadRequestError: BedrockException - {\"message\":\"The model returned the following errors: messages.1.content.0.type: Expected `thinking` or `redacted_thinking`, but found `text`.\"}",
    "type": "invalid_request_error",
    "param": null,
    "code": "400"
  }
}
```

This error is from **AWS Bedrock** (notice `BedrockException`). The Bedrock API is rejecting the request due to invalid message format - this is not a LiteLLM issue.

### Provider Error (from OpenAI)[​](#provider-error-from-openai "Direct link to Provider Error (from OpenAI)")

```
{
  "error": {
    "message": "litellm.AuthenticationError: OpenAIException - Incorrect API key provided: <my-key>. You can find your API key at https://platform.openai.com/account/api-keys.",
    "type": "invalid_request_error",
    "param": null,
    "code": "invalid_api_key"
  }
}
```

This error is from **OpenAI** (notice `OpenAIException`). The OpenAI API key configured in LiteLLM is invalid.

### Provider Error (from Anthropic)[​](#provider-error-from-anthropic "Direct link to Provider Error (from Anthropic)")

```
{
  "error": {
    "message": "litellm.InternalServerError: AnthropicException - Overloaded. Handle with `litellm.InternalServerError`.",
    "type": "internal_server_error",
    "param": null,
    "code": "500"
  }
}
```

This error is from **Anthropic** (notice `AnthropicException`). The Anthropic API is overloaded - this is not a LiteLLM issue.

### Gateway Error (from LiteLLM)[​](#gateway-error-from-litellm "Direct link to Gateway Error (from LiteLLM)")

```
{
  "error": {
    "message": "Invalid API Key. Please check your LiteLLM API key.",
    "type": "auth_error",
    "param": null,
    "code": "401"
  }
}
```

This error is from the **LiteLLM AI Gateway** (no provider name). Your LiteLLM virtual key is invalid.

## What to do?[​](#what-to-do "Direct link to What to do?")

Error SourceActionProvider ErrorCheck the provider's status page, adjust rate limits, or retry laterGateway ErrorCheck your LiteLLM configuration, API keys, or [open an issue](https://github.com/BerriAI/litellm/issues)

## See Also[​](#see-also "Direct link to See Also")

- [Debugging](https://docs.litellm.ai/docs/proxy/debugging) - Enable debug logs to see detailed request/response info
- [Exception Mapping](https://docs.litellm.ai/docs/exception_mapping) - Full list of LiteLLM exception types