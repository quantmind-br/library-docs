---
title: Use Claude Code with Non-Anthropic Models | liteLLM
url: https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models
source: sitemap
fetched_at: 2026-01-21T19:55:09.811400895-03:00
rendered_js: false
word_count: 367
summary: This tutorial explains how to integrate Claude Code with non-Anthropic LLM providers using LiteLLM as a proxy to translate requests into the Anthropic Messages API format.
tags:
    - claude-code
    - litellm
    - api-proxy
    - llm-integration
    - openai
    - gemini
    - multi-model
category: tutorial
---

This tutorial shows how to use Claude Code with non-Anthropic models like OpenAI, Gemini, and other LLM providers through LiteLLM proxy.

info

LiteLLM automatically translates between different provider formats, allowing you to use any supported LLM provider with Claude Code while maintaining the Anthropic Messages API format.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) installed
- API keys for your chosen providers (OpenAI, Vertex AI, etc.)

## Installation[​](#installation "Direct link to Installation")

First, install LiteLLM with proxy support:

```
pip install 'litellm[proxy]'
```

## Configuration[​](#configuration "Direct link to Configuration")

### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

Create a configuration file with your preferred non-Anthropic models:

- OpenAI
- Google AI Studio
- Vertex AI
- Azure OpenAI

```
model_list:
# OpenAI GPT-4o
-model_name: gpt-4o
litellm_params:
model: openai/gpt-4o
api_key: os.environ/OPENAI_API_KEY

# OpenAI GPT-4o-mini
-model_name: gpt-4o-mini
litellm_params:
model: openai/gpt-4o-mini
api_key: os.environ/OPENAI_API_KEY
```

Set your environment variables:

```
export OPENAI_API_KEY="your-openai-api-key"
export LITELLM_MASTER_KEY="sk-1234567890"  # Generate a secure key
```

### 2. Start LiteLLM Proxy[​](#2-start-litellm-proxy "Direct link to 2. Start LiteLLM Proxy")

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 3. Verify Setup[​](#3-verify-setup "Direct link to 3. Verify Setup")

Test that your proxy is working correctly:

- OpenAI
- Google AI Studio
- Vertex AI
- Azure OpenAI

```
curl -X POST http://0.0.0.0:4000/v1/messages \
-H "Authorization: Bearer $LITELLM_MASTER_KEY" \
-H "Content-Type: application/json" \
-d '{
    "model": "gpt-4o",
    "max_tokens": 1000,
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
}'
```

### 4. Configure Claude Code[​](#4-configure-claude-code "Direct link to 4. Configure Claude Code")

Configure Claude Code to use your LiteLLM proxy:

```
export ANTHROPIC_BASE_URL="http://0.0.0.0:4000"
export ANTHROPIC_AUTH_TOKEN="$LITELLM_MASTER_KEY"
```

tip

The `LITELLM_MASTER_KEY` gives Claude Code access to all proxy models. You can also create virtual keys in the LiteLLM UI to limit access to specific models.

### 5. Use Claude Code with Non-Anthropic Models[​](#5-use-claude-code-with-non-anthropic-models "Direct link to 5. Use Claude Code with Non-Anthropic Models")

Start Claude Code and specify which model to use:

```
# Use OpenAI GPT-4o
claude --model gpt-4o

# Use OpenAI GPT-4o-mini for faster responses
claude --model gpt-4o-mini

# Use Google Gemini
claude --model gemini-3.0-flash-exp

# Use Vertex AI Gemini
claude --model vertex-gemini-3-flash-preview

# Use Vertex AI Anthropic Claude
claude --model anthropic-vertex

# Use Azure OpenAI
claude --model azure-gpt-4
```

## How It Works[​](#how-it-works "Direct link to How It Works")

LiteLLM acts as a unified interface that:

1. **Receives requests** from Claude Code in Anthropic Messages API format
2. **Translates** the request to the target provider's format (OpenAI, Gemini, etc.)
3. **Forwards** the request to the actual provider
4. **Translates** the response back to Anthropic Messages API format
5. **Returns** the response to Claude Code

This allows you to use Claude Code's interface with any LLM provider supported by LiteLLM.

## Advanced Features[​](#advanced-features "Direct link to Advanced Features")

### Load Balancing and Fallbacks[​](#load-balancing-and-fallbacks "Direct link to Load Balancing and Fallbacks")

Configure multiple deployments with automatic fallback:

```
model_list:
-model_name: gpt-4o  # virtual model name
litellm_params:
model: openai/gpt-4o
api_key: os.environ/OPENAI_API_KEY

-model_name: gpt-4o  # same virtual name
litellm_params:
model: azure/gpt-4o
api_key: os.environ/AZURE_API_KEY
api_base: os.environ/AZURE_API_BASE

router_settings:
routing_strategy: simple-shuffle  # Load balance between deployments
num_retries:2
timeout:30
```

### Usage Tracking and Budgets[​](#usage-tracking-and-budgets "Direct link to Usage Tracking and Budgets")

Track usage and set budgets through the LiteLLM UI:

```
litellm_settings:
master_key: os.environ/LITELLM_MASTER_KEY
database_url:"postgresql://..."# Enable database for tracking

general_settings:
store_model_in_db:true
```

Start the proxy with the UI:

```
litellm --config /path/to/config.yaml --detailed_debug
```

Access the UI at `http://0.0.0.0:4000/ui` to:

- View usage analytics
- Set budget limits per user/key
- Monitor costs across different providers
- Create virtual keys with specific permissions

## Supported Providers[​](#supported-providers "Direct link to Supported Providers")

LiteLLM supports 100+ providers. Here are some popular ones for use with Claude Code:

- **OpenAI**: GPT-4o, GPT-4o-mini, o1, o3-mini
- **Google**: Gemini 2.0 Flash, Gemini 1.5 Pro/Flash
- **Azure OpenAI**: All OpenAI models via Azure
- **AWS Bedrock**: Llama, Mistral, and other models
- **Vertex AI**: Gemini, Claude, and other models on Google Cloud
- **Groq**: Fast inference for Llama and Mixtral
- **Together AI**: Llama, Mixtral, and other open source models
- **Deepseek**: Deepseek-chat, Deepseek-coder

[View full list of supported providers →](https://docs.litellm.ai/docs/providers)