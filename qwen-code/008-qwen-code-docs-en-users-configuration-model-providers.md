---
title: Model Providers
url: https://qwenlm.github.io/qwen-code-docs/en/users/configuration/model-providers
source: github_pages
fetched_at: 2026-04-09T09:04:14.440759179-03:00
rendered_js: true
word_count: 1803
summary: This document explains how to configure multiple AI model providers within Qwen Code using the `settings.json` file's `modelProviders` setting. It details structure requirements for various authentication types (OpenAI, Anthropic, Gemini) and provides guidelines on connecting local self-hosted models.
tags:
    - qwen-code
    - model-providers
    - ai-configuration
    - api-setup
    - settings-json
    - llm-integration
category: guide
---

Qwen Code allows you to configure multiple model providers through the `modelProviders` setting in your `settings.json`. This enables you to switch between different AI models and providers using the `/model` command.

## Overview[](#overview)

Use `modelProviders` to declare curated model lists per auth type that the `/model` picker can switch between. Keys must be valid auth types (`openai`, `anthropic`, `gemini`, etc.). Each entry requires an `id` and **must include `envKey`** , with optional `name`, `description`, `baseUrl`, and `generationConfig`. Credentials are never persisted in settings; the runtime reads them from `process.env[envKey]`. Qwen OAuth models remain hard-coded and cannot be overridden.

**Note**

Only the `/model` command exposes non-default auth types. Anthropic, Gemini, etc., must be defined via `modelProviders`. The `/auth` command lists Qwen OAuth, Alibaba Cloud Coding Plan, and API Key as the built-in authentication options.

**Warning**

**Duplicate model IDs within the same authType:** Defining multiple models with the same `id` under a single `authType` (e.g., two entries with `"id": "gpt-4o"` in `openai`) is currently not supported. If duplicates exist, **the first occurrence wins** and subsequent duplicates are skipped with a warning. Note that the `id` field is used both as the configuration identifier and as the actual model name sent to the API, so using unique IDs (e.g., `gpt-4o-creative`, `gpt-4o-balanced`) is not a viable workaround. This is a known limitation that we plan to address in a future release.

## Configuration Examples by Auth Type[](#configuration-examples-by-auth-type)

Below are comprehensive configuration examples for different authentication types, showing the available parameters and their combinations.

### Supported Auth Types[](#supported-auth-types)

The `modelProviders` object keys must be valid `authType` values. Currently supported auth types are:

Auth TypeDescription`openai`OpenAI-compatible APIs (OpenAI, Azure OpenAI, local inference servers like vLLM/Ollama)`anthropic`Anthropic Claude API`gemini`Google Gemini API`qwen-oauth`Qwen OAuth (hard-coded, cannot be overridden in `modelProviders`)

> \[!warning] If an invalid auth type key is used (e.g., a typo like `"openai-custom"`), the configuration will be **silently skipped** and the models will not appear in the `/model` picker. Always use one of the supported auth type values listed above.

### SDKs Used for API Requests[](#sdks-used-for-api-requests)

Qwen Code uses the following official SDKs to send requests to each provider:

Auth TypeSDK Package`openai`[`openai`](https://www.npmjs.com/package/openai) - Official OpenAI Node.js SDK`anthropic`[`@anthropic-ai/sdk`](https://www.npmjs.com/package/@anthropic-ai/sdk) - Official Anthropic SDK`gemini`[`@google/genai`](https://www.npmjs.com/package/@google/genai) - Official Google GenAI SDK`qwen-oauth`[`openai`](https://www.npmjs.com/package/openai) with custom provider (DashScope-compatible)

This means the `baseUrl` you configure should be compatible with the corresponding SDK’s expected API format. For example, when using `openai` auth type, the endpoint must accept OpenAI API format requests.

### OpenAI-compatible providers (`openai`)[](#openai-compatible-providers-openai)

This auth type supports not only OpenAI’s official API but also any OpenAI-compatible endpoint, including aggregated model providers like OpenRouter.

```
{
  "modelProviders": {
    "openai": [
      {
        "id": "gpt-4o",
        "name": "GPT-4o",
        "envKey": "OPENAI_API_KEY",
        "baseUrl": "https://api.openai.com/v1",
        "generationConfig": {
          "timeout": 60000,
          "maxRetries": 3,
          "enableCacheControl": true,
          "contextWindowSize": 128000,
          "modalities": {
            "image": true
          },
          "customHeaders": {
            "X-Client-Request-ID": "req-123"
          },
          "extra_body": {
            "enable_thinking": true,
            "service_tier": "priority"
          },
          "samplingParams": {
            "temperature": 0.2,
            "top_p": 0.8,
            "max_tokens": 4096,
            "presence_penalty": 0.1,
            "frequency_penalty": 0.1
          }
        }
      },
      {
        "id": "gpt-4o-mini",
        "name": "GPT-4o Mini",
        "envKey": "OPENAI_API_KEY",
        "baseUrl": "https://api.openai.com/v1",
        "generationConfig": {
          "timeout": 30000,
          "samplingParams": {
            "temperature": 0.5,
            "max_tokens": 2048
          }
        }
      },
      {
        "id": "openai/gpt-4o",
        "name": "GPT-4o (via OpenRouter)",
        "envKey": "OPENROUTER_API_KEY",
        "baseUrl": "https://openrouter.ai/api/v1",
        "generationConfig": {
          "timeout": 120000,
          "maxRetries": 3,
          "samplingParams": {
            "temperature": 0.7
          }
        }
      }
    ]
  }
}
```

### Anthropic (`anthropic`)[](#anthropic-anthropic)

```
{
  "modelProviders": {
    "anthropic": [
      {
        "id": "claude-3-5-sonnet",
        "name": "Claude 3.5 Sonnet",
        "envKey": "ANTHROPIC_API_KEY",
        "baseUrl": "https://api.anthropic.com/v1",
        "generationConfig": {
          "timeout": 120000,
          "maxRetries": 3,
          "contextWindowSize": 200000,
          "samplingParams": {
            "temperature": 0.7,
            "max_tokens": 8192,
            "top_p": 0.9
          }
        }
      },
      {
        "id": "claude-3-opus",
        "name": "Claude 3 Opus",
        "envKey": "ANTHROPIC_API_KEY",
        "baseUrl": "https://api.anthropic.com/v1",
        "generationConfig": {
          "timeout": 180000,
          "samplingParams": {
            "temperature": 0.3,
            "max_tokens": 4096
          }
        }
      }
    ]
  }
}
```

### Google Gemini (`gemini`)[](#google-gemini-gemini)

```
{
  "modelProviders": {
    "gemini": [
      {
        "id": "gemini-2.0-flash",
        "name": "Gemini 2.0 Flash",
        "envKey": "GEMINI_API_KEY",
        "baseUrl": "https://generativelanguage.googleapis.com",
        "capabilities": {
          "vision": true
        },
        "generationConfig": {
          "timeout": 60000,
          "maxRetries": 2,
          "contextWindowSize": 1000000,
          "schemaCompliance": "auto",
          "samplingParams": {
            "temperature": 0.4,
            "top_p": 0.95,
            "max_tokens": 8192,
            "top_k": 40
          }
        }
      }
    ]
  }
}
```

### Local Self-Hosted Models (via OpenAI-compatible API)[](#local-self-hosted-models-via-openai-compatible-api)

Most local inference servers (vLLM, Ollama, LM Studio, etc.) provide an OpenAI-compatible API endpoint. Configure them using the `openai` auth type with a local `baseUrl`:

```
{
  "modelProviders": {
    "openai": [
      {
        "id": "qwen2.5-7b",
        "name": "Qwen2.5 7B (Ollama)",
        "envKey": "OLLAMA_API_KEY",
        "baseUrl": "http://localhost:11434/v1",
        "generationConfig": {
          "timeout": 300000,
          "maxRetries": 1,
          "contextWindowSize": 32768,
          "samplingParams": {
            "temperature": 0.7,
            "top_p": 0.9,
            "max_tokens": 4096
          }
        }
      },
      {
        "id": "llama-3.1-8b",
        "name": "Llama 3.1 8B (vLLM)",
        "envKey": "VLLM_API_KEY",
        "baseUrl": "http://localhost:8000/v1",
        "generationConfig": {
          "timeout": 120000,
          "maxRetries": 2,
          "contextWindowSize": 128000,
          "samplingParams": {
            "temperature": 0.6,
            "max_tokens": 8192
          }
        }
      },
      {
        "id": "local-model",
        "name": "Local Model (LM Studio)",
        "envKey": "LMSTUDIO_API_KEY",
        "baseUrl": "http://localhost:1234/v1",
        "generationConfig": {
          "timeout": 60000,
          "samplingParams": {
            "temperature": 0.5
          }
        }
      }
    ]
  }
}
```

For local servers that don’t require authentication, you can use any placeholder value for the API key:

```
# For Ollama (no auth required)
export OLLAMA_API_KEY="ollama"

# For vLLM (if no auth is configured)
export VLLM_API_KEY="not-needed"
```

**Note**

The `extra_body` parameter is **only supported for OpenAI-compatible providers** (`openai`, `qwen-oauth`). It is ignored for Anthropic, and Gemini providers.

## Alibaba Cloud Coding Plan[](#alibaba-cloud-coding-plan)

Alibaba Cloud Coding Plan provides a pre-configured set of Qwen models optimized for coding tasks. This feature is available for users with Alibaba Cloud Coding Plan API access and offers a simplified setup experience with automatic model configuration updates.

### Overview[](#overview-1)

When you authenticate with an Alibaba Cloud Coding Plan API key using the `/auth` command, Qwen Code automatically configures the following models:

Model IDNameDescription`qwen3.5-plus`qwen3.5-plusAdvanced model with thinking enabled`qwen3-coder-plus`qwen3-coder-plusOptimized for coding tasks`qwen3-max-2026-01-23`qwen3-max-2026-01-23Latest max model with thinking enabled

### Setup[](#setup)

1. Obtain an Alibaba Cloud Coding Plan API key:
   
   - **China**: [https://bailian.console.aliyun.com/?tab=model#/efm/coding\_plan](https://bailian.console.aliyun.com/?tab=model#/efm/coding_plan)
   - **International**: [https://modelstudio.console.alibabacloud.com/?tab=dashboard#/efm/coding\_plan](https://modelstudio.console.alibabacloud.com/?tab=dashboard#/efm/coding_plan)
2. Run the `/auth` command in Qwen Code
3. Select **Alibaba Cloud Coding Plan**
4. Select your region
5. Enter your API key when prompted

The models will be automatically configured and added to your `/model` picker.

### Regions[](#regions)

Alibaba Cloud Coding Plan supports two regions:

RegionEndpointDescriptionChina`https://coding.dashscope.aliyuncs.com/v1`Mainland China endpointGlobal/International`https://coding-intl.dashscope.aliyuncs.com/v1`International endpoint

The region is selected during authentication and stored in `settings.json` under `codingPlan.region`. To switch regions, re-run the `/auth` command and select a different region.

### API Key Storage[](#api-key-storage)

When you configure Coding Plan through the `/auth` command, the API key is stored using the reserved environment variable name `BAILIAN_CODING_PLAN_API_KEY`. By default, it is stored in the `env` field of your `settings.json` file.

**Warning**

**Security Recommendation**: For better security, it is recommended to move the API key from `settings.json` to a separate `.env` file and load it as an environment variable. For example:

```
# ~/.qwen/.env
BAILIAN_CODING_PLAN_API_KEY=your-api-key-here
```

Then ensure this file is added to your `.gitignore` if you’re using project-level settings.

### Automatic Updates[](#automatic-updates)

Coding Plan model configurations are versioned. When Qwen Code detects a newer version of the model template, you will be prompted to update. Accepting the update will:

- Replace the existing Coding Plan model configurations with the latest versions
- Preserve any custom model configurations you’ve added manually
- Automatically switch to the first model in the updated configuration

The update process ensures you always have access to the latest model configurations and features without manual intervention.

### Manual Configuration (Advanced)[](#manual-configuration-advanced)

If you prefer to manually configure Coding Plan models, you can add them to your `settings.json` like any OpenAI-compatible provider:

```
{
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3-coder-plus",
        "name": "qwen3-coder-plus",
        "description": "Qwen3-Coder via Alibaba Cloud Coding Plan",
        "envKey": "YOUR_CUSTOM_ENV_KEY",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1"
      }
    ]
  }
}
```

**Note**

When using manual configuration:

- You can use any environment variable name for `envKey`
- You do not need to configure `codingPlan.*`
- **Automatic updates will not apply** to manually configured Coding Plan models

**Warning**

If you also use automatic Coding Plan configuration, automatic updates may overwrite your manual configurations if they use the same `envKey` and `baseUrl` as the automatic configuration. To avoid this, ensure your manual configuration uses a different `envKey` if possible.

## Resolution Layers and Atomicity[](#resolution-layers-and-atomicity)

The effective auth/model/credential values are chosen per field using the following precedence (first present wins). You can combine `--auth-type` with `--model` to point directly at a provider entry; these CLI flags run before other layers.

Layer (highest → lowest)authTypemodelapiKeybaseUrlapiKeyEnvKeyproxyProgrammatic overrides`/auth``/auth` input`/auth` input`/auth` input——Model provider selection—`modelProvider.id``env[modelProvider.envKey]``modelProvider.baseUrl``modelProvider.envKey`—CLI arguments`--auth-type``--model``--openaiApiKey` (or provider-specific equivalents)`--openaiBaseUrl` (or provider-specific equivalents)——Environment variables—Provider-specific mapping (e.g. `OPENAI_MODEL`)Provider-specific mapping (e.g. `OPENAI_API_KEY`)Provider-specific mapping (e.g. `OPENAI_BASE_URL`)——Settings (`settings.json`)`security.auth.selectedType``model.name``security.auth.apiKey``security.auth.baseUrl`——Default / computedFalls back to `AuthType.QWEN_OAUTH`Built-in default (OpenAI ⇒ `qwen3-coder-plus`)———`Config.getProxy()` if configured

\*When present, CLI auth flags override settings. Otherwise, `security.auth.selectedType` or the implicit default determine the auth type. Qwen OAuth and OpenAI are the only auth types surfaced without extra configuration.

**Warning**

**Deprecation of `security.auth.apiKey` and `security.auth.baseUrl`:** Directly configuring API credentials via `security.auth.apiKey` and `security.auth.baseUrl` in `settings.json` is deprecated. These settings were used in historical versions for credentials entered through the UI, but the credential input flow was removed in version 0.10.1. These fields will be fully removed in a future release. **It is strongly recommended to migrate to `modelProviders`** for all model and credential configurations. Use `envKey` in `modelProviders` to reference environment variables for secure credential management instead of hardcoding credentials in settings files.

## Generation Config Layering: The Impermeable Provider Layer[](#generation-config-layering-the-impermeable-provider-layer)

The configuration resolution follows a strict layering model with one crucial rule: **the modelProvider layer is impermeable**.

### How it works[](#how-it-works)

1. **When a modelProvider model IS selected** (e.g., via `/model` command choosing a provider-configured model):
   
   - The entire `generationConfig` from the provider is applied **atomically**
   - **The provider layer is completely impermeable** — lower layers (CLI, env, settings) do not participate in generationConfig resolution at all
   - All fields defined in `modelProviders[].generationConfig` use the provider’s values
   - All fields **not defined** by the provider are set to `undefined` (not inherited from settings)
   - This ensures provider configurations act as a complete, self-contained “sealed package”
2. **When NO modelProvider model is selected** (e.g., using `--model` with a raw model ID, or using CLI/env/settings directly):
   
   - The resolution falls through to lower layers
   - Fields are populated from CLI → env → settings → defaults
   - This creates a **Runtime Model** (see next section)

### Per-field precedence for `generationConfig`[](#per-field-precedence-for-generationconfig)

PrioritySourceBehavior1Programmatic overridesRuntime `/model`, `/auth` changes2`modelProviders[authType][].generationConfig`**Impermeable layer** - completely replaces all generationConfig fields; lower layers do not participate3`settings.model.generationConfig`Only used for **Runtime Models** (when no provider model is selected)4Content-generator defaultsProvider-specific defaults (e.g., OpenAI vs Gemini) - only for Runtime Models

### Atomic field treatment[](#atomic-field-treatment)

The following fields are treated as atomic objects - provider values completely replace the entire object, no merging occurs:

- `samplingParams` - Temperature, top\_p, max\_tokens, etc.
- `customHeaders` - Custom HTTP headers
- `extra_body` - Extra request body parameters

### Example[](#example)

```
// User settings (~/.qwen/settings.json)
{
  "model": {
    "generationConfig": {
      "timeout": 30000,
      "samplingParams": { "temperature": 0.5, "max_tokens": 1000 }
    }
  }
}

// modelProviders configuration
{
  "modelProviders": {
    "openai": [{
      "id": "gpt-4o",
      "envKey": "OPENAI_API_KEY",
      "generationConfig": {
        "timeout": 60000,
        "samplingParams": { "temperature": 0.2 }
      }
    }]
  }
}
```

When `gpt-4o` is selected from modelProviders:

- `timeout` = 60000 (from provider, overrides settings)
- `samplingParams.temperature` = 0.2 (from provider, completely replaces settings object)
- `samplingParams.max_tokens` = **undefined** (not defined in provider, and provider layer does not inherit from settings — fields are explicitly set to undefined if not provided)

When using a raw model via `--model gpt-4` (not from modelProviders, creates a Runtime Model):

- `timeout` = 30000 (from settings)
- `samplingParams.temperature` = 0.5 (from settings)
- `samplingParams.max_tokens` = 1000 (from settings)

The merge strategy for `modelProviders` itself is REPLACE: the entire `modelProviders` from project settings will override the corresponding section in user settings, rather than merging the two.

## Provider Models vs Runtime Models[](#provider-models-vs-runtime-models)

Qwen Code distinguishes between two types of model configurations:

### Provider Model[](#provider-model)

- Defined in `modelProviders` configuration
- Has a complete, atomic configuration package
- When selected, its configuration is applied as an impermeable layer
- Appears in `/model` command list with full metadata (name, description, capabilities)
- Recommended for multi-model workflows and team consistency

### Runtime Model[](#runtime-model)

- Created dynamically when using raw model IDs via CLI (`--model`), environment variables, or settings
- Not defined in `modelProviders`
- Configuration is built by “projecting” through resolution layers (CLI → env → settings → defaults)
- Automatically captured as a **RuntimeModelSnapshot** when a complete configuration is detected
- Allows reuse without re-entering credentials

### RuntimeModelSnapshot lifecycle[](#runtimemodelsnapshot-lifecycle)

When you configure a model without using `modelProviders`, Qwen Code automatically creates a RuntimeModelSnapshot to preserve your configuration:

```
# This creates a RuntimeModelSnapshot with ID: $runtime|openai|my-custom-model
qwen --auth-type openai --model my-custom-model --openaiApiKey $KEY --openaiBaseUrl https://api.example.com/v1
```

The snapshot:

- Captures model ID, API key, base URL, and generation config
- Persists across sessions (stored in memory during runtime)
- Appears in the `/model` command list as a runtime option
- Can be switched to using `/model $runtime|openai|my-custom-model`

### Key differences[](#key-differences)

AspectProvider ModelRuntime ModelConfiguration source`modelProviders` in settingsCLI, env, settings layersConfiguration atomicityComplete, impermeable packageLayered, each field resolved independentlyReusabilityAlways available in `/model` listCaptured as snapshot, appears if completeTeam sharingYes (via committed settings)No (user-local)Credential storageReference via `envKey` onlyMay capture actual key in snapshot

### When to use each[](#when-to-use-each)

- **Use Provider Models** when: You have standard models shared across a team, need consistent configurations, or want to prevent accidental overrides
- **Use Runtime Models** when: Quickly testing a new model, using temporary credentials, or working with ad-hoc endpoints

## Selection Persistence and Recommendations[](#selection-persistence-and-recommendations)

**Important**

Define `modelProviders` in the user-scope `~/.qwen/settings.json` whenever possible and avoid persisting credential overrides in any scope. Keeping the provider catalog in user settings prevents merge/override conflicts between project and user scopes and ensures `/auth` and `/model` updates always write back to a consistent scope.

- `/model` and `/auth` persist `model.name` (where applicable) and `security.auth.selectedType` to the closest writable scope that already defines `modelProviders`; otherwise they fall back to the user scope. This keeps workspace/user files in sync with the active provider catalog.
- Without `modelProviders`, the resolver mixes CLI/env/settings layers, creating Runtime Models. This is fine for single-provider setups but cumbersome when frequently switching. Define provider catalogs whenever multi-model workflows are common so that switches stay atomic, source-attributed, and debuggable.