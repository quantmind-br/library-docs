---
title: Bring Your Own Key (BYOK)
url: https://docs.factory.ai/cli/byok/overview.md
source: llms
fetched_at: 2026-03-03T01:12:44.843716-03:00
rendered_js: false
word_count: 1016
summary: This document explains how to configure custom language models and private API keys in the Factory CLI using the Bring Your Own Key (BYOK) system.
tags:
    - factory-cli
    - byok
    - custom-models
    - api-configuration
    - llm-integration
    - local-models
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Bring Your Own Key (BYOK)

> Connect your own API keys, use open source models, or run local models

Factory CLI supports custom model configurations through BYOK (Bring Your Own Key). Use your own OpenAI or Anthropic keys, connect to any open source model providers, or run models locally on your hardware. Once configured, switch between models using the `/model` command.

<Note>
  Your API keys remain local and are not uploaded to Factory servers. Custom models are only available in the CLI and won't appear in Factory's web or mobile platforms.
</Note>

<img src="https://mintcdn.com/factory/76eHQsYrywYjfJno/images/custom_models.png?fit=max&auto=format&n=76eHQsYrywYjfJno&q=85&s=5e8af07b3c42614e2c32c43e8a04d146" alt="Model selector showing custom models" data-og-width="1376" width="1376" data-og-height="1166" height="1166" data-path="images/custom_models.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/76eHQsYrywYjfJno/images/custom_models.png?w=280&fit=max&auto=format&n=76eHQsYrywYjfJno&q=85&s=0a88e202f668a0055f577ad8af4e2c44 280w, https://mintcdn.com/factory/76eHQsYrywYjfJno/images/custom_models.png?w=560&fit=max&auto=format&n=76eHQsYrywYjfJno&q=85&s=b84709a21e42815a025af7923560d8e2 560w, https://mintcdn.com/factory/76eHQsYrywYjfJno/images/custom_models.png?w=840&fit=max&auto=format&n=76eHQsYrywYjfJno&q=85&s=a1ac1f0c71c0fd9e9e0ecbea359e8147 840w, https://mintcdn.com/factory/76eHQsYrywYjfJno/images/custom_models.png?w=1100&fit=max&auto=format&n=76eHQsYrywYjfJno&q=85&s=4ce271b2c579cdee03bb8ff175363689 1100w, https://mintcdn.com/factory/76eHQsYrywYjfJno/images/custom_models.png?w=1650&fit=max&auto=format&n=76eHQsYrywYjfJno&q=85&s=8addfdbeb4484a1ed22ac4d04fc9799e 1650w, https://mintcdn.com/factory/76eHQsYrywYjfJno/images/custom_models.png?w=2500&fit=max&auto=format&n=76eHQsYrywYjfJno&q=85&s=51f4623e0f5f1cde003f8a7f39b5e1c4 2500w" />

[Install the CLI with the 5-minute quickstart →](/cli/getting-started/quickstart)

***

## Configuration Reference

Add custom models to `~/.factory/settings.json` under the `customModels` array:

```json  theme={null}
{
  "customModels": [
    {
      "model": "your-model-id",
      "displayName": "My Custom Model",
      "baseUrl": "https://api.provider.com/v1",
      "apiKey": "${PROVIDER_API_KEY}",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    }
  ]
}
```

<Tip>
  In `settings.json` (and `settings.local.json`), `apiKey` supports environment variable references using `${VAR_NAME}` syntax. For example, `"apiKey": "${PROVIDER_API_KEY}"` reads from the environment variable named `PROVIDER_API_KEY` (for example: `export PROVIDER_API_KEY=your_key_here`).
</Tip>

<Note>
  **Legacy support**: Custom models in `~/.factory/config.json` using snake\_case field names (`custom_models`, `base_url`, etc.) are still supported for backwards compatibility. Both files are loaded and merged, with `settings.json` taking priority. Env var expansion for `apiKey` applies to `settings.json`/`settings.local.json` and not to legacy `config.json`.
</Note>

### Supported Fields

| Field             | Type      | Required | Description                                                                                                                                                                                    |
| ----------------- | --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`           | `string`  | ✓        | Model identifier sent via API (e.g., `claude-sonnet-4-5-20250929`, `gpt-5-codex`, `qwen3:4b`)                                                                                                  |
| `displayName`     | `string`  |          | Human-friendly name shown in model selector                                                                                                                                                    |
| `baseUrl`         | `string`  | ✓        | API endpoint base URL                                                                                                                                                                          |
| `apiKey`          | `string`  | ✓        | Your API key for the provider. Can't be empty. Supports `${VAR_NAME}` in `settings.json`/`settings.local.json` (e.g., `${PROVIDER_API_KEY}` uses the `PROVIDER_API_KEY` environment variable). |
| `provider`        | `string`  | ✓        | One of: `anthropic`, `openai`, or `generic-chat-completion-api`                                                                                                                                |
| `maxOutputTokens` | `number`  |          | Maximum output tokens for model responses                                                                                                                                                      |
| `supportsImages`  | `boolean` |          | Whether the model supports image inputs                                                                                                                                                        |
| `extraArgs`       | `object`  |          | Additional provider-specific arguments to include in API requests                                                                                                                              |
| `extraHeaders`    | `object`  |          | Additional HTTP headers to send with requests                                                                                                                                                  |

### Using extraArgs

Pass provider-specific parameters like temperature or top\_p:

```json  theme={null}
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

### Using extraHeaders

Add custom HTTP headers to API requests:

```json  theme={null}
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

***

## Understanding Providers

Factory supports three provider types that determine API compatibility:

| Provider                      | API Format                           | Use For                                                                                                               | Documentation                                                                      |
| ----------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `anthropic`                   | Anthropic Messages API (v1/messages) | Anthropic models on their official API or compatible proxies                                                          | [Anthropic Messages API](https://docs.claude.com/en/api/messages)                  |
| `openai`                      | OpenAI Responses API                 | OpenAI models on their official API or compatible proxies. Required for the newest models like GPT-5 and GPT-5-Codex. | [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)   |
| `generic-chat-completion-api` | OpenAI Chat Completions API          | OpenRouter, Fireworks, Together AI, Ollama, vLLM, and most open-source providers                                      | [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat) |

<Warning>
  Factory is actively verifying Droid's performance on popular models, but we cannot guarantee that all custom models will work out of the box. Only Anthropic and OpenAI models accessed via their official APIs are fully tested and benchmarked.
</Warning>

<Note>
  **Model Size Consideration**: Models below 30 billion parameters have shown significantly lower performance on agentic coding tasks. While these smaller models can be useful for experimentation and learning, they are generally not recommended for production coding work or complex software engineering tasks.
</Note>

***

## Prompt Caching

Factory CLI automatically uses prompt caching when available to reduce API costs:

* **Official providers (`anthropic`, `openai`)**: Factory attempts to use prompt caching via the official APIs. Caching behavior follows each provider's implementation and requirements.
* **Generic providers (`generic-chat-completion-api`)**: Prompt caching support varies by provider and cannot be guaranteed. Some providers may support caching, while others may not.

### Verifying Prompt Caching

To check if prompt caching is working correctly with your custom model:

1. Run a conversation with your custom model
2. Use the `/cost` command in Droid CLI to view cost breakdowns
3. Look for cache hit rates and savings in the output

If you're not seeing expected caching savings, consult your provider's documentation about their prompt caching support and requirements.

***

## Quick Start

Choose a provider from the left navigation to see specific configuration examples:

* **[Baseten](/cli/byok/baseten)** - Deploy and serve custom models
* **[DeepInfra](/cli/byok/deepinfra)** - Cost-effective inference for open-source models
* **[Fireworks AI](/cli/byok/fireworks)** - High-performance inference for open-source models
* **[Google Gemini](/cli/byok/google-gemini)** - Access Google's Gemini models
* **[Groq](/cli/byok/groq)** - Ultra-fast inference with Groq's LPU™ Inference Engine
* **[Hugging Face](/cli/byok/huggingface)** - Connect to models on HF Inference API
* **[Ollama](/cli/byok/ollama)** - Run models locally or in the cloud
* **[OpenAI & Anthropic](/cli/byok/openai-anthropic)** - Use your own API keys for official models
* **[OpenRouter](/cli/byok/openrouter)** - Access multiple providers through a single interface

***

## Using Custom Models

Once configured, access your custom models in the CLI:

1. Use the `/model` command
2. Your custom models appear in a separate "Custom models" section below Factory-provided models
3. Select any model to start using it

Custom models display with the name you set in `displayName`, making it easy to identify different providers and configurations.

***

## Troubleshooting

### Model not appearing in selector

* Check JSON syntax in `~/.factory/settings.json` (or `config.json` if using legacy format)
* Settings changes are detected automatically via file watching
* Verify all required fields are present

### "Invalid provider" error

* Provider must be exactly `anthropic`, `openai`, or `generic-chat-completion-api`
* Check for typos and ensure proper capitalization

### Authentication errors

* Verify your API key is valid and has available credits
* Check that the API key has proper permissions
* Confirm the base URL matches your provider's documentation

### Local model won't connect

* Ensure your local server is running (e.g., `ollama serve`)
* Verify the base URL is correct and includes `/v1/` suffix if required
* Check that the model is pulled/available locally

### Rate limiting or quota errors

* Check your provider's rate limits and usage quotas
* Monitor your usage through your provider's dashboard

***

## Billing

* You pay your provider directly with no Factory markup or usage fees
* Track costs and usage in your provider's dashboard