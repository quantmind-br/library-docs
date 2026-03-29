---
title: Claude Code Quickstart | liteLLM
url: https://docs.litellm.ai/docs/tutorials/claude_responses_api
source: sitemap
fetched_at: 2026-01-21T19:55:10.023499558-03:00
rendered_js: false
word_count: 234
summary: This guide explains how to integrate Claude Code with LiteLLM proxy to access and manage Claude models across multiple providers including Anthropic, AWS Bedrock, and Google Vertex AI.
tags:
    - litellm
    - claude-code
    - proxy-server
    - model-routing
    - anthropic-claude
    - aws-bedrock
    - vertex-ai
category: tutorial
---

This tutorial shows how to call Claude models through LiteLLM proxy from Claude Code.

### Video Walkthrough[​](#video-walkthrough "Direct link to Video Walkthrough")

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) installed
- API keys for your chosen providers

## Installation[​](#installation "Direct link to Installation")

First, install LiteLLM with proxy support:

```
pip install 'litellm[proxy]'
```

### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

Create a secure configuration using environment variables:

```
model_list:
# Claude models
-model_name: claude-3-5-sonnet-20241022
litellm_params:
model: anthropic/claude-3-5-sonnet-20241022
api_key: os.environ/ANTHROPIC_API_KEY

-model_name: claude-3-5-haiku-20241022
litellm_params:
model: anthropic/claude-3-5-haiku-20241022
api_key: os.environ/ANTHROPIC_API_KEY


litellm_settings:
master_key: os.environ/LITELLM_MASTER_KEY
```

Set your environment variables:

```
export ANTHROPIC_API_KEY="your-anthropic-api-key"
export LITELLM_MASTER_KEY="sk-1234567890"  # Generate a secure key
```

### 2. Start proxy[​](#2-start-proxy "Direct link to 2. Start proxy")

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 3. Verify Setup[​](#3-verify-setup "Direct link to 3. Verify Setup")

Test that your proxy is working correctly:

```
curl -X POST http://0.0.0.0:4000/v1/messages \
-H "Authorization: Bearer $LITELLM_MASTER_KEY" \
-H "Content-Type: application/json" \
-d '{
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1000,
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
}'
```

### 4. Configure Claude Code[​](#4-configure-claude-code "Direct link to 4. Configure Claude Code")

#### Method 1: Unified Endpoint (Recommended)[​](#method-1-unified-endpoint-recommended "Direct link to Method 1: Unified Endpoint (Recommended)")

Configure Claude Code to use LiteLLM's unified endpoint:

Either a virtual key / master key can be used here

```
export ANTHROPIC_BASE_URL="http://0.0.0.0:4000"
export ANTHROPIC_AUTH_TOKEN="$LITELLM_MASTER_KEY"
```

tip

LITELLM\_MASTER\_KEY gives claude access to all proxy models, whereas a virtual key would be limited to the models set in UI

#### Method 2: Provider-specific Pass-through Endpoint[​](#method-2-provider-specific-pass-through-endpoint "Direct link to Method 2: Provider-specific Pass-through Endpoint")

Alternatively, use the Anthropic pass-through endpoint:

```
export ANTHROPIC_BASE_URL="http://0.0.0.0:4000/anthropic"
export ANTHROPIC_AUTH_TOKEN="$LITELLM_MASTER_KEY"
```

### 5. Use Claude Code[​](#5-use-claude-code "Direct link to 5. Use Claude Code")

Start Claude Code and it will automatically use your configured models:

```
# Claude Code will use the models configured in your LiteLLM proxy
claude

# Or specify a model if you have multiple configured
claude --model claude-3-5-sonnet-20241022
claude --model claude-3-5-haiku-20241022
```

Example conversation:

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

Common issues and solutions:

**Claude Code not connecting:**

- Verify your proxy is running: `curl http://0.0.0.0:4000/health`
- Check that `ANTHROPIC_BASE_URL` is set correctly
- Ensure your `ANTHROPIC_AUTH_TOKEN` matches your LiteLLM master key

**Authentication errors:**

- Verify your environment variables are set: `echo $LITELLM_MASTER_KEY`
- Check that your API keys are valid and have sufficient credits
- Ensure the `ANTHROPIC_AUTH_TOKEN` matches your LiteLLM master key

**Model not found:**

- Ensure the model name in Claude Code matches exactly with your `config.yaml`
- Check LiteLLM logs for detailed error messages

## Using Bedrock/Vertex AI/Azure Foundry Models[​](#using-bedrockvertex-aiazure-foundry-models "Direct link to Using Bedrock/Vertex AI/Azure Foundry Models")

Expand your configuration to support multiple providers and models:

- Multi-Provider Setup

```
model_list:
# Anthropic models
-model_name: claude-3-5-sonnet-20241022
litellm_params:
model: anthropic/claude-3-5-sonnet-20241022
api_key: os.environ/ANTHROPIC_API_KEY

-model_name: claude-3-5-haiku-20241022
litellm_params:
model: anthropic/claude-3-5-haiku-20241022
api_key: os.environ/ANTHROPIC_API_KEY

# AWS Bedrock
-model_name: claude-bedrock
litellm_params:
model: bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
aws_region_name: us-east-1

# Azure Foundry
-model_name: claude-4-azure
litellm_params:
model: azure_ai/claude-opus-4-1
api_key: os.environ/AZURE_AI_API_KEY
api_base: os.environ/AZURE_AI_API_BASE # https://my-resource.services.ai.azure.com/anthropic

# Google Vertex AI
-model_name: anthropic-vertex
litellm_params:
model: vertex_ai/claude-haiku-4-5@20251001
vertex_ai_project:"my-test-project"
vertex_ai_location:"us-east-1"
vertex_credentials: os.environ/VERTEX_FILE_PATH_ENV_VAR # os.environ["VERTEX_FILE_PATH_ENV_VAR"] = "/path/to/service_account.json" 


litellm_settings:
master_key: os.environ/LITELLM_MASTER_KEY
```

Switch between models seamlessly:

```
# Use Claude for complex reasoning
claude --model claude-3-5-sonnet-20241022

# Use Haiku for fast responses
claude --model claude-3-5-haiku-20241022

# Use Bedrock deployment
claude --model claude-bedrock

# Use Azure Foundry deployment
claude --model claude-4-azure

# Use Vertex AI deployment
claude --model anthropic-vertex
```