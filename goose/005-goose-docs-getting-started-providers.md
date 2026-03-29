---
title: Configure LLM Provider | goose
url: https://block.github.io/goose/docs/getting-started/providers
source: github_pages
fetched_at: 2026-01-22T22:13:25.762788519-03:00
rendered_js: true
word_count: 2426
summary: This document provides a comprehensive list of supported LLM providers and models for goose, detailing required environment variables and configuration parameters for each. It covers cloud-based APIs, local model runners, and pass-through CLI providers to help users select and integrate their preferred AI backend.
tags:
    - llm-providers
    - model-selection
    - api-configuration
    - cloud-ai
    - local-llm
    - environment-variables
    - integration-guide
category: reference
---

goose is compatible with a wide range of LLM providers, allowing you to choose and integrate your preferred model.

Model Selection

goose relies heavily on tool calling capabilities and currently works best with Claude 4 models.

[Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) can be a good guide for selecting models.

## Available Providers[​](#available-providers "Direct link to Available Providers")

ProviderDescriptionParameters[Amazon Bedrock](https://aws.amazon.com/bedrock/)Offers a variety of foundation models, including Claude, Jurassic-2, and others. **AWS environment variables must be set in advance, not configured through `goose configure`**`AWS_PROFILE`, or `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`[Amazon SageMaker TGI](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)Run Text Generation Inference models through Amazon SageMaker endpoints. **AWS credentials must be configured in advance.**`SAGEMAKER_ENDPOINT_NAME`, `AWS_REGION` (optional), `AWS_PROFILE` (optional)[Anthropic](https://www.anthropic.com/)Offers Claude, an advanced AI model for natural language tasks.`ANTHROPIC_API_KEY`, `ANTHROPIC_HOST` (optional)[Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)Access Azure-hosted OpenAI models, including GPT-4 and GPT-3.5. Supports both API key and Azure credential chain authentication.`AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_KEY` (optional)[Databricks](https://www.databricks.com/)Unified data analytics and AI platform for building and deploying models.`DATABRICKS_HOST`, `DATABRICKS_TOKEN`[Docker Model Runner](https://docs.docker.com/ai/model-runner/)Local models running in Docker Desktop or Docker CE with OpenAI-compatible API endpoints. **Because this provider runs locally, you must first [download a model](#local-llms).**`OPENAI_HOST`, `OPENAI_BASE_PATH`[Gemini](https://ai.google.dev/gemini-api/docs)Advanced LLMs by Google with multimodal capabilities (text, images).`GOOGLE_API_KEY`[GCP Vertex AI](https://cloud.google.com/vertex-ai)Google Cloud's Vertex AI platform, supporting Gemini and Claude models. **Credentials must be [configured in advance](https://cloud.google.com/vertex-ai/docs/authentication).**`GCP_PROJECT_ID`, `GCP_LOCATION` and optionally `GCP_MAX_RATE_LIMIT_RETRIES` (5), `GCP_MAX_OVERLOADED_RETRIES` (5), `GCP_INITIAL_RETRY_INTERVAL_MS` (5000), `GCP_BACKOFF_MULTIPLIER` (2.0), `GCP_MAX_RETRY_INTERVAL_MS` (320\_000).[GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/ai-models)Access to AI models from OpenAI, Anthropic, Google, and other providers through GitHub's Copilot infrastructure. **GitHub account with Copilot access required.**No manual key. Uses [device flow authentication](#github-copilot-authentication) for both CLI and Desktop.[Groq](https://groq.com/)High-performance inference hardware and tools for LLMs.`GROQ_API_KEY`[LiteLLM](https://docs.litellm.ai/docs/)LiteLLM proxy supporting multiple models with automatic prompt caching and unified API access.`LITELLM_HOST`, `LITELLM_BASE_PATH` (optional), `LITELLM_API_KEY` (optional), `LITELLM_CUSTOM_HEADERS` (optional), `LITELLM_TIMEOUT` (optional)[Mistral AI](https://mistral.ai/)Provides access to Mistral models including general-purpose models, specialized coding models (Codestral), and multimodal models (Pixtral).`MISTRAL_API_KEY`[Ollama](https://ollama.com/)Local model runner supporting Qwen, Llama, DeepSeek, and other open-source models. **Because this provider runs locally, you must first [download and run a model](#local-llms).**`OLLAMA_HOST`[Ramalama](https://ramalama.ai/)Local model using native [OCI](https://opencontainers.org/) container runtimes, [CNCF](https://www.cncf.io/) tools, and supporting models as OCI artifacts. Ramalama API an compatible alternative to Ollama and can be used with the goose Ollama provider. Supports Qwen, Llama, DeepSeek, and other open-source models. **Because this provider runs locally, you must first [download and run a model](#local-llms).**`OLLAMA_HOST`[OpenAI](https://platform.openai.com/api-keys)Provides gpt-4o, o1, and other advanced language models. Also supports OpenAI-compatible endpoints (e.g., self-hosted LLaMA, vLLM, KServe). **o1-mini and o1-preview are not supported because goose uses tool calling.**`OPENAI_API_KEY`, `OPENAI_HOST` (optional), `OPENAI_ORGANIZATION` (optional), `OPENAI_PROJECT` (optional), `OPENAI_CUSTOM_HEADERS` (optional)[OpenRouter](https://openrouter.ai/)API gateway for unified access to various models with features like rate-limiting management.`OPENROUTER_API_KEY`[Snowflake](https://docs.snowflake.com/user-guide/snowflake-cortex/aisql#choosing-a-model)Access the latest models using Snowflake Cortex services, including Claude models. **Requires a Snowflake account and programmatic access token (PAT)**.`SNOWFLAKE_HOST`, `SNOWFLAKE_TOKEN`[Tetrate Agent Router Service](https://router.tetrate.ai)Unified API gateway for AI models including Claude, Gemini, GPT, open-weight models, and others. Supports PKCE authentication flow for secure API key generation.`TETRATE_API_KEY`, `TETRATE_HOST` (optional)[Venice AI](https://venice.ai/home)Provides access to open source models like Llama, Mistral, and Qwen while prioritizing user privacy. **Requires an account and an [API key](https://docs.venice.ai/overview/guides/generating-api-key)**.`VENICE_API_KEY`, `VENICE_HOST` (optional), `VENICE_BASE_PATH` (optional), `VENICE_MODELS_PATH` (optional)[xAI](https://x.ai/)Access to xAI's Grok models including grok-3, grok-3-mini, and grok-3-fast with 131,072 token context window.`XAI_API_KEY`, `XAI_HOST` (optional)

Prompt Caching for Claude Models

goose automatically enables Anthropic's [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) when using Claude models via Anthropic, Databricks, OpenRouter, and LiteLLM providers. This adds `cache_control` markers to requests, which can reduce costs for longer conversations by caching frequently-used context. See the [provider implementations](https://github.com/block/goose/tree/main/crates/goose/src/providers) for technical details.

### CLI Providers[​](#cli-providers "Direct link to CLI Providers")

goose also supports special "pass-through" providers that work with existing CLI tools, allowing you to use your subscriptions instead of paying per token:

ProviderDescriptionRequirements[Claude Code](https://www.anthropic.com/claude-code) (`claude-code`)Uses Anthropic's Claude CLI tool with your Claude Code subscription. Provides access to Claude with 200K context limit.Claude CLI installed and authenticated, active Claude Code subscription[OpenAI Codex](https://developers.openai.com/codex/cli) (`codex`)Uses OpenAI's Codex CLI tool with your ChatGPT Plus/Pro subscription. Provides access to GPT-5 models with up to 400K context limit.Codex CLI installed and authenticated, active ChatGPT Plus/Pro subscription[Cursor Agent](https://docs.cursor.com/en/cli/overview) (`cursor-agent`)Uses Cursor's AI CLI tool with your Cursor subscription. Provides access to GPT-5, Claude 4, and other models through the cursor-agent command-line interface.cursor-agent CLI installed and authenticated[Gemini CLI](https://ai.google.dev/gemini-api/docs) (`gemini-cli`)Uses Google's Gemini CLI tool with your Google AI subscription. Provides access to Gemini with 1M context limit.Gemini CLI installed and authenticated

CLI Providers

CLI providers are cost-effective alternatives that use your existing subscriptions. They work differently from API providers as they execute CLI commands and integrate with the tools' native capabilities. See the [CLI Providers guide](https://block.github.io/goose/docs/guides/cli-providers) for detailed setup instructions.

## Configure Provider and Model[​](#configure-provider-and-model "Direct link to Configure Provider and Model")

To configure your chosen provider, see available options, or select a model, visit the `Models` tab in goose Desktop or run `goose configure` in the CLI.

- goose Desktop
- goose CLI

**First-time users:**

On the welcome screen the first time you open goose, you have three options:

- **Automatic setup with [Tetrate Agent Router](https://tetrate.io/products/tetrate-agent-router-service)**
- **Automatic Setup with [OpenRouter](https://openrouter.ai/)**
- **Other Providers**

<!--THE END-->

- Tetrate Agent Router
- OpenRouter
- Other Providers

We recommend starting with Tetrate Agent Router. Tetrate provides access to multiple AI models with built-in rate limiting and automatic failover.

Free Credits Offer

You'll receive $10 in free credits the first time you automatically authenticate with Tetrate through goose. This offer is available to both new and existing Tetrate users.

1. Choose `Automatic setup with Tetrate Agent Router`.
2. goose will open a browser window for you to authenticate with Tetrate, or create a new account if you don't have one already.
3. When you return to the goose desktop app, you're ready to begin your first session.

**To update your LLM provider and API key:**

1. Click the button in the top-left to open the sidebar
2. Click the `Settings` button on the sidebar
3. Click the `Models` tab
4. Click `Configure providers`
5. Click your provider in the list
6. Add your API key and other required configurations, then click `Submit`

**To change your current model:**

1. Click the button in the top-left to open the sidebar
2. Click the `Settings` button on the sidebar
3. Click the `Models` tab
4. Click `Switch models`
5. Choose from your configured providers in the dropdown, or select `Use other provider` to configure a new one
6. Select a model from the available options, or choose `Use custom model` to enter a specific model name
7. Click `Select model` to confirm your choice

Shortcut

For faster access, click your current model name at the bottom of the app and choose `Change Model`.

**To start over with provider and model configuration:**

1. Click the button in the top-left to open the sidebar
2. Click the `Settings` button on the sidebar
3. Click the `Models` tab
4. Click `Reset Provider and Model` to clear your current settings and return to the welcome screen

### Using Custom OpenAI Endpoints[​](#using-custom-openai-endpoints "Direct link to Using Custom OpenAI Endpoints")

The built-in OpenAI provider can connect to OpenAI's official API (`api.openai.com`) or any OpenAI-compatible endpoint, such as:

- Self-hosted LLMs (e.g., LLaMA, Mistral) using vLLM or KServe
- Private OpenAI-compatible API servers
- Enterprise deployments requiring data governance and security compliance
- OpenAI API proxies or gateways

Custom Provider Option

Need to connect to multiple OpenAI-compatible endpoints? [Configure custom providers](#configure-custom-provider) instead for easier switching and better organization, as well as custom naming and shareable configurations.

#### Configuration Parameters[​](#configuration-parameters "Direct link to Configuration Parameters")

ParameterRequiredDescription`OPENAI_API_KEY`YesAuthentication key for the API`OPENAI_HOST`NoCustom endpoint URL (defaults to api.openai.com)`OPENAI_ORGANIZATION`NoOrganization ID for usage tracking and governance`OPENAI_PROJECT`NoProject identifier for resource management`OPENAI_CUSTOM_HEADERS`NoAdditional headers to include in the request. Can be set via environment variable, configuration file, or CLI, in the format `HEADER_A=VALUE_A,HEADER_B=VALUE_B`.

#### Example Configurations[​](#example-configurations "Direct link to Example Configurations")

- vLLM Self-Hosted
- KServe Deployment
- Enterprise OpenAI
- Custom Headers

If you're running LLaMA or other models using vLLM with OpenAI compatibility:

```
OPENAI_HOST=https://your-vllm-endpoint.internal
OPENAI_API_KEY=your-internal-api-key
```

#### Setup Instructions[​](#setup-instructions "Direct link to Setup Instructions")

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click the `Settings` button on the sidebar
3. Click the `Models` tab
4. Click `Configure providers`
5. Click `OpenAI` in the provider list
6. Fill in your configuration details:
   
   - API Key (required)
   - Host URL (for custom endpoints)
   - Organization ID (for usage tracking)
   - Project (for resource management)
7. Click `Submit`

Enterprise Deployment

For enterprise deployments, you can pre-configure these values using environment variables or configuration files to ensure consistent governance across your organization.

Custom providers let you connect to services that aren't in the [available providers](#available-providers) list. They appear in goose's provider list and can be selected like any other provider.

**Benefits:**

- **Multiple endpoints**: Switch between different services (e.g., vLLM, corporate proxy, OpenAI)
- **Pre-configured models**: Store a list of preferred models
- **Shareable configuration**: JSON files can be shared across teams or checked into repos
- **Custom naming**: Show "Corporate API" instead of "OpenAI" in the UI
- **Separate credentials**: Assign each provider its own API key

Custom providers must use OpenAI, Anthropic, or Ollama compatible API formats. OpenAI-compatible providers can include custom headers for additional authentication, API keys, tokens, or tenant identifiers. Each custom provider maps to a JSON configuration file.

**To add a custom provider:**

- goose Desktop
- goose CLI
- Config File

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click the `Settings` button on the sidebar
3. Click the `Models` tab
4. Click `Configure providers`
5. Click `Add Custom Provider` at the bottom of the window
6. Fill in the provider details:
   
   - **Provider Type**:
     
     - `OpenAI Compatible` (most common)
     - `Anthropic Compatible`
     - `Ollama Compatible`
   - **Display Name**: A friendly name for the provider
   - **API URL**: The base URL of the API endpoint
   - **API Key**: The API key, which is accessed using a custom environment variable and stored in the keychain (or `secrets.yaml` if the keyring is disabled)
     
     - For `Ollama Compatible` providers, click `This is a local model (no auth required)`
   - **Available Models**: Comma-separated list of available model names
   - **Streaming Support**: Whether the API supports streaming responses (click to toggle)
7. Click `Create Provider`

Custom Headers

Currently, custom headers for OpenAI compatible providers can't be defined in goose Desktop. As a workaround, configure the provider using goose CLI or edit the provider configuration file directly.

**To update a custom provider:**

- goose Desktop
- goose CLI
- Config File

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click the `Settings` button on the sidebar
3. Click the `Models` tab
4. Click `Configure providers`
5. Click on your custom provider in the list
6. Update the fields you want to change  
   **Important:** Verify that `Provider Type` shows the correct value before saving. Otherwise, it may default to `OpenAI Compatible` regardless of the original setting.
7. Click `Update Provider`

Your changes are available in your next goose session.

**To remove a custom provider:**

- goose Desktop
- goose CLI
- Config File

Currently you cannot remove custom providers using goose Desktop.

## Using goose for Free[​](#using-goose-for-free "Direct link to Using goose for Free")

goose is a free and open source AI agent that you can start using right away, but not all supported [LLM Providers](https://block.github.io/goose/docs/getting-started/providers) provide a free tier.

Below, we outline a couple of free options and how to get started with them.

Limitations

These free options are a great way to get started with goose and explore its capabilities. However, you may need to upgrade your LLM for better performance.

### Groq[​](#groq "Direct link to Groq")

Groq provides free access to open source models with high-speed inference. To use Groq with goose, you need an API key from [Groq Console](https://console.groq.com/keys).

Groq offers several open source models that support tool calling:

- **moonshotai/kimi-k2-instruct** - Mixture-of-Experts model with 1 trillion parameters, optimized for agentic intelligence and tool use
- **qwen/qwen3-32b** - 32.8 billion parameter model with advanced reasoning and multilingual capabilities
- **gemma2-9b-it** - Google's Gemma 2 model with instruction tuning
- **llama-3.3-70b-versatile** - Meta's Llama 3.3 model for versatile applications

To set up Groq with goose, follow these steps:

- goose Desktop
- goose CLI

**To update your LLM provider and API key:**

1. Click the button in the top-left to open the sidebar.
2. Click the `Settings` button on the sidebar.
3. Click the `Models` tab.
4. Click `Configure Providers`
5. Choose `Groq` as provider from the list.
6. Click `Configure`, enter your API key, and click `Submit`.

### Google Gemini[​](#google-gemini "Direct link to Google Gemini")

Google Gemini provides a free tier. To start using the Gemini API with goose, you need an API Key from [Google AI studio](https://aistudio.google.com/app/apikey).

To set up Google Gemini with goose, follow these steps:

- goose Desktop
- goose CLI

**To update your LLM provider and API key:**

1. Click the button in the top-left to open the sidebar.
2. Click the `Settings` button on the sidebar.
3. Click the `Models` tab.
4. Click `Configure Providers`
5. Choose `Google Gemini` as provider from the list.
6. Click `Configure`, enter your API key, and click `Submit`.

### Local LLMs[​](#local-llms "Direct link to Local LLMs")

goose is a local AI agent, and by using a local LLM, you keep your data private, maintain full control over your environment, and can work entirely offline without relying on cloud access. However, please note that local LLMs require a bit more set up before you can use one of them with goose.

Limited Support for models without tool calling

goose extensively uses tool calling, so models without it can only do chat completion. If using models without tool calling, all goose [extensions must be disabled](https://block.github.io/goose/docs/getting-started/using-extensions#enablingdisabling-extensions).

Here are some local providers we support:

- Ollama
- Docker Model Runner

<!--THE END-->

- Ramalala
- DeepSeek-R1
- Other Models

<!--THE END-->

1. [Download Ollama](https://ollama.com/download).
2. In a terminal, run any [model supporting tool-calling](https://ollama.com/search?c=tools)

Example:

3. In a separate terminal window, configure with goose:

<!--THE END-->

4. Choose to `Configure Providers`

```
┌   goose-configure 
│
◆  What would you like to configure?
│  ● Configure Providers (Change provider or update credentials)
│  ○ Toggle Extensions 
│  ○ Add Extension 
└  
```

5. Choose `Ollama` as the model provider

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Configure Providers 
│
◆  Which model provider should we use?
│  ○ Anthropic 
│  ○ Databricks 
│  ○ Google Gemini 
│  ○ Groq 
│  ● Ollama (Local open source models)
│  ○ OpenAI 
│  ○ OpenRouter 
└  
```

6. Enter the host where your model is running

Endpoint

For Ollama, if you don't provide a host, we set it to `localhost:11434`. When constructing the URL, we prepend `http://` if the scheme is not `http` or `https`. If you're running Ollama on a different server, you'll have to set `OLLAMA_HOST=http://{host}:{port}`.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Configure Providers 
│
◇  Which model provider should we use?
│  Ollama 
│
◆  Provider Ollama requires OLLAMA_HOST, please enter a value
│  http://localhost:11434
└
```

7. Enter the model you have running

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Configure Providers 
│
◇  Which model provider should we use?
│  Ollama 
│
◇  Provider Ollama requires OLLAMA_HOST, please enter a value
│  http://localhost:11434
│
◇  Enter a model from that provider:
│  qwen2.5
│
◇  Welcome! You're all set to explore and utilize my capabilities. Let's get started on solving your problems together!
│
└  Configuration saved successfully
```

Context Length

If you notice that goose is having trouble using extensions or is ignoring [.goosehints](https://block.github.io/goose/docs/guides/context-engineering/using-goosehints), it is likely that the model's default context length of 4096 tokens is too low. Set the `OLLAMA_CONTEXT_LENGTH` environment variable to a [higher value](https://github.com/ollama/ollama/blob/main/docs/faq.mdx#how-can-i-specify-the-context-window-size).

## GitHub Copilot Authentication[​](#github-copilot-authentication "Direct link to GitHub Copilot Authentication")

GitHub Copilot uses a device flow for authentication, so no API keys are required:

1. Run [`goose configure`](#configure-provider-and-model) and select **GitHub Copilot**
2. An eight-character code will be automatically copied to your clipboard
3. A browser will open to GitHub's device activation page
4. Paste the code to authorize the application
5. When you return to goose, GitHub Copilot will be available as a provider in both CLI and Desktop.

## Azure OpenAI Credential Chain[​](#azure-openai-credential-chain "Direct link to Azure OpenAI Credential Chain")

goose supports two authentication methods for Azure OpenAI:

1. **API Key Authentication** - Uses the `AZURE_OPENAI_API_KEY` for direct authentication
2. **Azure Credential Chain** - Uses Azure CLI credentials automatically without requiring an API key

To use the Azure Credential Chain:

- Ensure you're logged in with `az login`
- Have appropriate Azure role assignments for the Azure OpenAI service
- Configure with `goose configure` and select Azure OpenAI, leaving the API key field empty

This method simplifies authentication and enhances security for enterprise environments.

## Multi-Model Configuration[​](#multi-model-configuration "Direct link to Multi-Model Configuration")

Beyond single-model setups, goose supports [multi-model configurations](https://block.github.io/goose/docs/guides/multi-model/) that can use different models and providers for specialized tasks:

- **Lead/Worker Model** - Automatic switching between a lead model for initial turns and a worker model for execution tasks
- **Planning Mode** - Manual planning phase using a dedicated model to create detailed project breakdowns before execution

* * *

If you have any questions or need help with a specific provider, feel free to reach out to us on [Discord](https://discord.gg/goose-oss) or on the [goose repo](https://github.com/block/goose).