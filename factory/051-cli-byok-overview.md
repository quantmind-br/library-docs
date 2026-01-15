---
title: Bring Your Own Key (BYOK) - Factory Documentation
url: https://docs.factory.ai/cli/byok/overview
source: sitemap
fetched_at: 2026-01-13T19:03:23.31098483-03:00
rendered_js: false
word_count: 614
summary: Explains how to configure and use custom AI models within the Factory CLI by modifying the settings JSON file to define providers, API keys, and parameters.
tags:
    - factory-cli
    - custom-models
    - byok
    - api-configuration
    - model-providers
category: configuration
---

Factory CLI supports custom model configurations through BYOK (Bring Your Own Key). Use your own OpenAI or Anthropic keys, connect to any open source model providers, or run models locally on your hardware. Once configured, switch between models using the `/model` command.

![Model selector showing custom models](https://mintcdn.com/factory/76eHQsYrywYjfJno/images/custom_models.png?fit=max&auto=format&n=76eHQsYrywYjfJno&q=85&s=5e8af07b3c42614e2c32c43e8a04d146) [Install the CLI with the 5-minute quickstart →](https://docs.factory.ai/cli/getting-started/quickstart)

* * *

## Configuration Reference

Add custom models to `~/.factory/settings.json` under the `customModels` array:

```
{
  "customModels": [
    {
      "model": "your-model-id",
      "displayName": "My Custom Model",
      "baseUrl": "https://api.provider.com/v1",
      "apiKey": "YOUR_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    }
  ]
}
```

### Supported Fields

FieldTypeRequiredDescription`model``string`✓Model identifier sent via API (e.g., `claude-sonnet-4-5-20250929`, `gpt-5-codex`, `qwen3:4b`)`displayName``string`Human-friendly name shown in model selector`baseUrl``string`✓API endpoint base URL`apiKey``string`✓Your API key for the provider. Can’t be empty.`provider``string`✓One of: `anthropic`, `openai`, or `generic-chat-completion-api``maxOutputTokens``number`Maximum output tokens for model responses`supportsImages``boolean`Whether the model supports image inputs`extraArgs``object`Additional provider-specific arguments to include in API requests`extraHeaders``object`Additional HTTP headers to send with requests

Pass provider-specific parameters like temperature or top\_p:

```
{
  "customModels": [
    {
      "model": "your-model",
      "displayName": "Custom Model",
      "baseUrl": "https://your-provider.com/v1",
      "apiKey": "YOUR_API_KEY",
      "provider": "generic-chat-completion-api",
      "extraArgs": {
        "temperature": 0.7,
        "top_p": 0.9
      }
    }
  ]
}
```

Add custom HTTP headers to API requests:

```
{
  "customModels": [
    {
      "model": "your-model",
      "displayName": "Custom Model",
      "baseUrl": "https://your-provider.com/v1",
      "apiKey": "YOUR_API_KEY",
      "provider": "generic-chat-completion-api",
      "extraHeaders": {
        "X-Custom-Header": "value",
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  ]
}
```

* * *

## Understanding Providers

Factory supports three provider types that determine API compatibility:

ProviderAPI FormatUse ForDocumentation`anthropic`Anthropic Messages API (v1/messages)Anthropic models on their official API or compatible proxies[Anthropic Messages API](https://docs.claude.com/en/api/messages)`openai`OpenAI Responses APIOpenAI models on their official API or compatible proxies. Required for the newest models like GPT-5 and GPT-5-Codex.[OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)`generic-chat-completion-api`OpenAI Chat Completions APIOpenRouter, Fireworks, Together AI, Ollama, vLLM, and most open-source providers[OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat)

* * *

## Prompt Caching

Factory CLI automatically uses prompt caching when available to reduce API costs:

- **Official providers (`anthropic`, `openai`)**: Factory attempts to use prompt caching via the official APIs. Caching behavior follows each provider’s implementation and requirements.
- **Generic providers (`generic-chat-completion-api`)**: Prompt caching support varies by provider and cannot be guaranteed. Some providers may support caching, while others may not.

### Verifying Prompt Caching

To check if prompt caching is working correctly with your custom model:

1. Run a conversation with your custom model
2. Use the `/cost` command in Droid CLI to view cost breakdowns
3. Look for cache hit rates and savings in the output

If you’re not seeing expected caching savings, consult your provider’s documentation about their prompt caching support and requirements.

* * *

## Quick Start

Choose a provider from the left navigation to see specific configuration examples:

- [**Baseten**](https://docs.factory.ai/cli/byok/baseten) - Deploy and serve custom models
- [**DeepInfra**](https://docs.factory.ai/cli/byok/deepinfra) - Cost-effective inference for open-source models
- [**Fireworks AI**](https://docs.factory.ai/cli/byok/fireworks) - High-performance inference for open-source models
- [**Google Gemini**](https://docs.factory.ai/cli/byok/google-gemini) - Access Google’s Gemini models
- [**Groq**](https://docs.factory.ai/cli/byok/groq) - Ultra-fast inference with Groq’s LPU™ Inference Engine
- [**Hugging Face**](https://docs.factory.ai/cli/byok/huggingface) - Connect to models on HF Inference API
- [**Ollama**](https://docs.factory.ai/cli/byok/ollama) - Run models locally or in the cloud
- [**OpenAI & Anthropic**](https://docs.factory.ai/cli/byok/openai-anthropic) - Use your own API keys for official models
- [**OpenRouter**](https://docs.factory.ai/cli/byok/openrouter) - Access multiple providers through a single interface

* * *

## Using Custom Models

Once configured, access your custom models in the CLI:

1. Use the `/model` command
2. Your custom models appear in a separate “Custom models” section below Factory-provided models
3. Select any model to start using it

Custom models display with the name you set in `displayName`, making it easy to identify different providers and configurations.

* * *

## Troubleshooting

### Model not appearing in selector

- Check JSON syntax in `~/.factory/settings.json` (or `config.json` if using legacy format)
- Settings changes are detected automatically via file watching
- Verify all required fields are present

### ”Invalid provider” error

- Provider must be exactly `anthropic`, `openai`, or `generic-chat-completion-api`
- Check for typos and ensure proper capitalization

### Authentication errors

- Verify your API key is valid and has available credits
- Check that the API key has proper permissions
- Confirm the base URL matches your provider’s documentation

### Local model won’t connect

- Ensure your local server is running (e.g., `ollama serve`)
- Verify the base URL is correct and includes `/v1/` suffix if required
- Check that the model is pulled/available locally

### Rate limiting or quota errors

- Check your provider’s rate limits and usage quotas
- Monitor your usage through your provider’s dashboard

* * *

## Billing

- You pay your provider directly with no Factory markup or usage fees
- Track costs and usage in your provider’s dashboard