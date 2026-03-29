---
title: ForgeCode
url: https://forgecode.dev/docs/custom-providers/
source: sitemap
fetched_at: 2026-03-29T16:30:35.476822-03:00
rendered_js: false
word_count: 566
summary: This document provides instructions for configuring, managing, and switching between various AI service providers within the ForgeCode platform using command-line tools.
tags:
    - ai-integration
    - credential-management
    - provider-configuration
    - cli-tools
    - api-keys
    - model-selection
category: configuration
---

Configure ForgeCode to work with your preferred AI provider. This guide covers provider setup, credential management, and provider-specific features.

ForgeCode supports multiple AI providers, each with unique capabilities and pricing models:

### Provider Overview[​](#provider-overview "Direct link to Provider Overview")

- **OpenRouter**: Access to 300+ models from multiple providers
- **OpenAI**: Official OpenAI models (GPT-4, o3-mini, etc.)
- **Anthropic**: Claude models (Claude 3.7 Sonnet, etc.)
- **Google Vertex AI**: Google's enterprise AI platform with Claude and Gemini models
- **Groq**: Ultra-fast inference with optimized models like DeepSeek R1
- **Amazon Bedrock**: AWS managed AI service with multiple model providers
- **OpenAI-Compatible Providers**: Any provider following OpenAI API format

The recommended way to configure providers is using the interactive login command:

### Login to a Provider

Use the `forge provider login` command to configure your AI provider credentials:

This interactive command will:

1. Show you a list of available providers
2. Guide you through entering the required credentials
3. Securely store your credentials in ForgeCode's configuration

### Verify Configuration

Test your provider configuration by running ForgeCode:

ForgeCode will automatically use your configured provider.

ForgeCode provides commands to manage your provider credentials:

**Where to get API keys:**

- [ForgeCode Provider](https://app.forgecode.dev/app/) - Sign up for Antinomy account
- [OpenRouter](https://openrouter.ai/) - Aggregated access to multiple models
- [OpenAI](https://platform.openai.com/) - Official OpenAI platform
- [Anthropic](https://console.anthropic.com/) - Official Anthropic console
- [Google Vertex AI](https://cloud.google.com/vertex-ai) - Google Cloud AI platform
- [Groq](https://console.groq.com/) - Ultra-fast inference platform
- [Amazon Bedrock](https://aws.amazon.com/bedrock/) - AWS managed AI service

Once you have multiple providers configured, you can easily switch between them using the `/provider` command.

### Using the `/provider` Command[​](#using-the-provider-command "Direct link to using-the-provider-command")

This will display an interactive menu showing all your configured providers:

**Navigation:**

- Use **arrow keys** to navigate up/down
- **Type** to filter providers by name
- Press **Enter** to select
- Press **Escape** to cancel

### Model Selection[​](#model-selection "Direct link to Model Selection")

After switching providers, you'll be prompted to select a compatible model from the new provider's available models.

Multiple Providers

Configure multiple providers to easily switch based on your needs:

- **OpenRouter**: For model variety and cost comparison
- **OpenAI**: For latest GPT models and features
- **Anthropic**: For Claude's reasoning capabilities
- **Groq**: For ultra-fast inference

DEPRECATED

Using `.env` files for provider configuration is **deprecated** and will be removed in a future version. Please use `forge provider login` instead.

### Automatic Migration[​](#automatic-migration "Direct link to Automatic Migration")

For backward compatibility, ForgeCode still supports environment variables. **On first run**, if credentials are found in environment variables (`.env` files), ForgeCode will:

1. **Automatically migrate** your API keys to credentials
2. Display a notification about the migration
3. Continue working with your credentials

After migration, you should manage your providers using:

### Legacy Environment Configuration[​](#legacy-environment-configuration "Direct link to Legacy Environment Configuration")

**Legacy .env Setup (Not Recommended)**

If you still need to use environment variables temporarily, ForgeCode searches for `.env` files in this order:

1. **Current working directory** (`.env`)
2. **Parent directories** (recursively up to root)
3. **Home directory** (`~/.env`)

**Example legacy configuration:**

**Migration process:**

When you run ForgeCode for the first time after upgrading, it will:

- Detect credentials in your `.env` files
- Automatically migrate them to secure file-based storage
- Show a notification about the migration
- Continue working without interruption

**After migration:**

- Your credentials are now managed by ForgeCode
- Use `forge provider login` to add new providers
- Use `forge provider logout` to remove providers
- Your original `.env` files remain unchanged (for other tools)

When multiple providers are configured, ForgeCode uses this priority order:

1. **OpenRouter** - Second priority (multiple models)
2. **OpenAI** - Third priority (official OpenAI)
3. **Anthropic** - Lowest priority (official Anthropic)

You can override the default provider using the `/provider` command at any time.

* * *

**Provider configuration complete!** Use `forge provider login` to manage your AI provider credentials securely.