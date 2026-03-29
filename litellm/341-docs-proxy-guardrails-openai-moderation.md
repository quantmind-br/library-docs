---
title: OpenAI Moderation | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/openai_moderation
source: sitemap
fetched_at: 2026-01-21T19:52:25.404689788-03:00
rendered_js: false
word_count: 457
summary: This guide explains how to integrate and configure OpenAI's Moderation API as a guardrail in LiteLLM to filter harmful content from user inputs and model responses. It details various execution modes, streaming support, and best practices for implementing content safety policies.
tags:
    - litellm
    - openai-moderation
    - guardrails
    - content-safety
    - llm-security
    - streaming-support
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionUse OpenAI's built-in Moderation API to detect and block harmful content including hate speech, harassment, self-harm, sexual content, and violence.Provider[OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation)Supported Actions`BLOCK` (raises HTTP 400 exception when violations detected)Supported Modes`pre_call`, `during_call`, `post_call`Streaming Support✅ Full support for streaming responsesAPI RequirementsOpenAI API key

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Define Guardrails on your LiteLLM config.yaml[​](#1-define-guardrails-on-your-litellm-configyaml "Direct link to 1. Define Guardrails on your LiteLLM config.yaml")

Define your guardrails under the `guardrails` section:

- Config.yaml
- Environment Variables

config.yaml

```
model_list:
-model_name: gpt-4
litellm_params:
model: openai/gpt-4
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"openai-moderation-pre"
litellm_params:
guardrail: openai_moderation
mode:"pre_call"
api_key: os.environ/OPENAI_API_KEY  # Optional if already set globally
model:"omni-moderation-latest"# Optional, defaults to omni-moderation-latest
api_base:"https://api.openai.com/v1"# Optional, defaults to OpenAI API
```

#### Supported values for `mode`[​](#supported-values-for-mode "Direct link to supported-values-for-mode")

- `pre_call` Run **before** LLM call, on **user input**
- `during_call` Run **during** LLM call, on **user input**. Same as `pre_call` but runs in parallel as LLM call. Response not returned until guardrail check completes.
- `post_call` Run **after** LLM call, on **LLM response**

#### Supported OpenAI Moderation Models[​](#supported-openai-moderation-models "Direct link to Supported OpenAI Moderation Models")

- `omni-moderation-latest` (default) - Latest multimodal moderation model
- `text-moderation-latest` - Latest text-only moderation model

### 2. Start LiteLLM Gateway[​](#2-start-litellm-gateway "Direct link to 2. Start LiteLLM Gateway")

```
litellm --config config.yaml --detailed_debug
```

### 3. Test request[​](#3-test-request "Direct link to 3. Test request")

- Blocked Request
- Successful Call

Expect this to fail since the request contains harmful content:

```
curl -i http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "user", "content": "I hate all people and want to hurt them"}
    ],
    "guardrails": ["openai-moderation-pre"]
  }'
```

Expected response on failure:

```
{
"error":{
"message":{
"error":"Violated OpenAI moderation policy",
"moderation_result":{
"violated_categories":["hate","violence"],
"category_scores":{
"hate":0.95,
"violence":0.87,
"harassment":0.12,
"self-harm":0.01,
"sexual":0.02
}
}
},
"type":"None",
"param":"None",
"code":"400"
}
}
```

## Advanced Configuration[​](#advanced-configuration "Direct link to Advanced Configuration")

### Multiple Guardrails for Input and Output[​](#multiple-guardrails-for-input-and-output "Direct link to Multiple Guardrails for Input and Output")

You can configure separate guardrails for user input and LLM responses:

Multiple Guardrails Config

```
guardrails:
-guardrail_name:"openai-moderation-input"
litellm_params:
guardrail: openai_moderation
mode:"pre_call"
api_key: os.environ/OPENAI_API_KEY

-guardrail_name:"openai-moderation-output"
litellm_params:
guardrail: openai_moderation
mode:"post_call"
api_key: os.environ/OPENAI_API_KEY
```

### Custom API Configuration[​](#custom-api-configuration "Direct link to Custom API Configuration")

Configure custom OpenAI API endpoints or different models:

Custom API Config

```
guardrails:
-guardrail_name:"openai-moderation-custom"
litellm_params:
guardrail: openai_moderation
mode:"pre_call"
api_key: os.environ/OPENAI_API_KEY
api_base:"https://your-custom-openai-endpoint.com/v1"
model:"text-moderation-latest"
```

## Streaming Support[​](#streaming-support "Direct link to Streaming Support")

The OpenAI Moderation guardrail fully supports streaming responses. When used in `post_call` mode, it will:

1. Collect all streaming chunks
2. Assemble the complete response
3. Apply moderation to the full content
4. Block the entire stream if violations are detected
5. Return the original stream if content is safe

Streaming Config

```
guardrails:
-guardrail_name:"openai-moderation-streaming"
litellm_params:
guardrail: openai_moderation
mode:"post_call"# Works with streaming responses
api_key: os.environ/OPENAI_API_KEY
```

## Content Categories[​](#content-categories "Direct link to Content Categories")

The OpenAI Moderation API detects the following categories of harmful content:

CategoryDescription`hate`Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste`harassment`Content that harasses, bullies, or intimidates an individual`self-harm`Content that promotes, encourages, or depicts acts of self-harm`sexual`Content meant to arouse sexual excitement or promote sexual services`violence`Content that depicts death, violence, or physical injury

Each category is evaluated with both a boolean flag and a confidence score (0.0 to 1.0).

## Error Handling[​](#error-handling "Direct link to Error Handling")

When content violates OpenAI's moderation policy:

- **HTTP Status**: 400 Bad Request
- **Error Type**: `HTTPException`
- **Error Details**: Includes violated categories and confidence scores
- **Behavior**: Request is immediately blocked

## Best Practices[​](#best-practices "Direct link to Best Practices")

### 1. Use Pre-call for User Input[​](#1-use-pre-call-for-user-input "Direct link to 1. Use Pre-call for User Input")

```
guardrails:
-guardrail_name:"input-moderation"
litellm_params:
guardrail: openai_moderation
mode:"pre_call"# Block harmful user inputs early
```

### 2. Use Post-call for LLM Responses[​](#2-use-post-call-for-llm-responses "Direct link to 2. Use Post-call for LLM Responses")

```
guardrails:
-guardrail_name:"output-moderation"
litellm_params:
guardrail: openai_moderation  
mode:"post_call"# Ensure LLM responses are safe
```

### 3. Combine with Other Guardrails[​](#3-combine-with-other-guardrails "Direct link to 3. Combine with Other Guardrails")

```
guardrails:
-guardrail_name:"openai-moderation"
litellm_params:
guardrail: openai_moderation
mode:"pre_call"

-guardrail_name:"custom-pii-detection"
litellm_params:
guardrail: presidio
mode:"pre_call"
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Common Issues[​](#common-issues "Direct link to Common Issues")

1. **Invalid API Key**: Ensure your OpenAI API key is correctly set
   
   ```
   export OPENAI_API_KEY="sk-your-actual-key"
   ```
2. **Rate Limiting**: OpenAI Moderation API has rate limits. Monitor usage in high-volume scenarios.
3. **Network Issues**: Verify connectivity to OpenAI's API endpoints.

### Debug Mode[​](#debug-mode "Direct link to Debug Mode")

Enable detailed logging to troubleshoot issues:

```
litellm --config config.yaml --detailed_debug
```

Look for logs starting with `OpenAI Moderation:` to trace guardrail execution.

## API Costs[​](#api-costs "Direct link to API Costs")

The OpenAI Moderation API is **free to use** for content policy compliance. This makes it a cost-effective guardrail option compared to other commercial moderation services.

## Need Help?[​](#need-help "Direct link to Need Help?")

For additional support:

- Check the [OpenAI Moderation API documentation](https://platform.openai.com/docs/guides/moderation)
- Review [LiteLLM Guardrails documentation](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)
- Join our [Discord community](https://discord.gg/wuPM9dRgDw)