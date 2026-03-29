---
title: Qwen Code CLI | liteLLM
url: https://docs.litellm.ai/docs/tutorials/litellm_qwen_code_cli
source: sitemap
fetched_at: 2026-01-21T19:55:35.170576198-03:00
rendered_js: false
word_count: 452
summary: This tutorial provides instructions for integrating the Qwen Code CLI with LiteLLM Proxy to manage model access, routing, and costs through a unified interface.
tags:
    - qwen-code
    - litellm
    - proxy-integration
    - cli
    - model-routing
    - load-balancing
category: tutorial
---

This tutorial shows you how to integrate the Qwen Code CLI with LiteLLM Proxy, allowing you to route requests through LiteLLM's unified interface.

info

This integration is supported from LiteLLM v1.73.3-nightly and above.

## Benefits of using qwen-code with LiteLLM[​](#benefits-of-using-qwen-code-with-litellm "Direct link to Benefits of using qwen-code with LiteLLM")

When you use qwen-code with LiteLLM you get the following benefits:

**Developer Benefits:**

- Universal Model Access: Use any LiteLLM supported model (Anthropic, OpenAI, Vertex AI, Bedrock, etc.) through the qwen-code interface.
- Higher Rate Limits & Reliability: Load balance across multiple models and providers to avoid hitting individual provider limits, with fallbacks to ensure you get responses even if one provider fails.

**Proxy Admin Benefits:**

- Centralized Management: Control access to all models through a single LiteLLM proxy instance without giving your developers API Keys to each provider.
- Budget Controls: Set spending limits and track costs across all qwen-code usage.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you begin, ensure you have:

- Node.js and npm installed on your system
- A running LiteLLM Proxy instance
- A valid LiteLLM Proxy API key
- Git installed for cloning the repository

## Quick Start Guide[​](#quick-start-guide "Direct link to Quick Start Guide")

### Step 1: Install Qwen Code CLI[​](#step-1-install-qwen-code-cli "Direct link to Step 1: Install Qwen Code CLI")

Clone the Qwen Code CLI repository and navigate to the project directory:

```
npm install -g @qwen-code/qwen-code
```

### Step 2: Configure Qwen Code CLI for LiteLLM Proxy[​](#step-2-configure-qwen-code-cli-for-litellm-proxy "Direct link to Step 2: Configure Qwen Code CLI for LiteLLM Proxy")

Configure the Qwen Code CLI to point to your LiteLLM Proxy instance by setting the required environment variables:

```
export OPENAI_BASE_URL="http://localhost:4000"
export OPENAI_API_KEY=sk-1234567890
export OPENAI_MODEL="your-configured-model"
```

**Note:** Replace the values with your actual LiteLLM Proxy configuration:

- `OPENAI_BASE_URL`: The URL where your LiteLLM Proxy is running
- `OPENAI_API_KEY`: Your LiteLLM Proxy API key
- `OPENAI_MODEL`: The model you want to use (configured in your LiteLLM proxy)

### Step 3: Build and Start Qwen Code CLI[​](#step-3-build-and-start-qwen-code-cli "Direct link to Step 3: Build and Start Qwen Code CLI")

Build the project and start the CLI:

### Step 4: Test the Integration[​](#step-4-test-the-integration "Direct link to Step 4: Test the Integration")

Once the CLI is running, you can send test requests. These requests will be automatically routed through LiteLLM Proxy to the configured Qwen model.

The CLI will now use LiteLLM Proxy as the backend, giving you access to LiteLLM's features like:

- Request/response logging
- Rate limiting
- Cost tracking
- Model routing and fallbacks

## Advanced[​](#advanced "Direct link to Advanced")

### Use Anthropic, OpenAI, Bedrock, etc. models on qwen-code[​](#use-anthropic-openai-bedrock-etc-models-on-qwen-code "Direct link to Use Anthropic, OpenAI, Bedrock, etc. models on qwen-code")

In order to use non-qwen models on qwen-code, you need to set a `model_group_alias` in the LiteLLM Proxy config. This tells LiteLLM that requests with model = `qwen-code` should be routed to your desired model from any provider.

- Anthropic
- OpenAI
- Bedrock
- Multi-Provider Load Balancing

Route `qwen-code` requests to Claude Sonnet:

proxy\_config.yaml

```
model_list:
-model_name: claude-sonnet-4-20250514
litellm_params:
model: anthropic/claude-3-5-sonnet-20241022
api_key: os.environ/ANTHROPIC_API_KEY

router_settings:
model_group_alias:{"qwen-code":"claude-sonnet-4-20250514"}
```

With this configuration, when you use `qwen-code` in the CLI, LiteLLM will automatically route your requests to the configured provider(s) with load balancing and fallbacks.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

If you encounter issues:

1. **Connection errors**: Verify that your LiteLLM Proxy is running and accessible at the configured `OPENAI_BASE_URL`
2. **Authentication errors**: Ensure your `OPENAI_API_KEY` is valid and has the necessary permissions
3. **Build failures**: Make sure all dependencies are installed with `npm install`