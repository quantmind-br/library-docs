---
title: Claude Code - WebSearch Across All Providers | liteLLM
url: https://docs.litellm.ai/docs/tutorials/claude_code_websearch
source: sitemap
fetched_at: 2026-01-21T19:55:05.196146451-03:00
rendered_js: false
word_count: 277
summary: This document explains how to configure LiteLLM to enable web search capabilities for Claude Code when using non-Anthropic providers like AWS Bedrock and Azure. It provides instructions for intercepting search requests and routing them through various search tool providers.
tags:
    - litellm
    - claude-code
    - web-search
    - proxy-configuration
    - search-interception
    - aws-bedrock
    - azure-openai
category: configuration
---

Enable Claude Code's web search tool to work with any provider (Bedrock, Azure, Vertex, etc.). LiteLLM automatically intercepts web search requests and executes them server-side.

## Proxy Configuration[​](#proxy-configuration "Direct link to Proxy Configuration")

Add WebSearch interception to your `litellm_config.yaml`:

litellm\_config.yaml

```
model_list:
-model_name: bedrock-sonnet
litellm_params:
model: bedrock/us.anthropic.claude-sonnet-4-5-20250929-v1:0
aws_region_name: us-east-1

# Enable WebSearch interception for providers
litellm_settings:
callbacks:
-websearch_interception:
enabled_providers:
- bedrock
- azure
- vertex_ai
search_tool_name: perplexity-search  # Optional: specific search tool

# Configure search provider
search_tools:
-search_tool_name: perplexity-search
litellm_params:
search_provider: perplexity
api_key: os.environ/PERPLEXITY_API_KEY
```

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Configure LiteLLM Proxy[​](#1-configure-litellm-proxy "Direct link to 1. Configure LiteLLM Proxy")

Create `config.yaml`:

config.yaml

```
model_list:
-model_name: bedrock-sonnet
litellm_params:
model: bedrock/us.anthropic.claude-sonnet-4-5-20250929-v1:0
aws_region_name: us-east-1

litellm_settings:
callbacks:
-websearch_interception:
enabled_providers:[bedrock]

search_tools:
-search_tool_name: perplexity-search
litellm_params:
search_provider: perplexity
api_key: os.environ/PERPLEXITY_API_KEY
```

### 2. Start Proxy[​](#2-start-proxy "Direct link to 2. Start Proxy")

Start LiteLLM Proxy

```
export PERPLEXITY_API_KEY=your-key
litellm --config config.yaml
```

### 3. Use with Claude Code[​](#3-use-with-claude-code "Direct link to 3. Use with Claude Code")

Configure Claude Code

```
export ANTHROPIC_BASE_URL=http://localhost:4000
export ANTHROPIC_API_KEY=sk-1234
claude
```

Now use web search in Claude Code - it works with any provider!

## How It Works[​](#how-it-works "Direct link to How It Works")

When Claude Code sends a web search request, LiteLLM:

1. Intercepts the native `web_search` tool
2. Converts it to LiteLLM's standard format
3. Executes the search via Perplexity/Tavily
4. Returns the final answer to Claude Code

**Result**: One API call from Claude Code → Complete answer with search results

## Supported Providers[​](#supported-providers "Direct link to Supported Providers")

ProviderNative Web SearchWith LiteLLM**Anthropic**✅ Yes✅ Yes**Bedrock**❌ No✅ Yes**Azure**❌ No✅ Yes**Vertex AI**❌ No✅ Yes**Other Providers**❌ No✅ Yes

## Search Providers[​](#search-providers "Direct link to Search Providers")

Configure which search provider to use. LiteLLM supports multiple search providers:

Provider`search_provider` ValueEnvironment Variable**Perplexity AI**`perplexity``PERPLEXITYAI_API_KEY`**Tavily**`tavily``TAVILY_API_KEY`**Exa AI**`exa_ai``EXA_API_KEY`**Parallel AI**`parallel_ai``PARALLEL_AI_API_KEY`**Google PSE**`google_pse``GOOGLE_PSE_API_KEY`, `GOOGLE_PSE_ENGINE_ID`**DataForSEO**`dataforseo``DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`**Firecrawl**`firecrawl``FIRECRAWL_API_KEY`**SearXNG**`searxng``SEARXNG_API_BASE` (required)**Linkup**`linkup``LINKUP_API_KEY`

See [all supported search providers](https://docs.litellm.ai/docs/search/) for detailed setup instructions and provider-specific parameters.

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

### WebSearch Interception Parameters[​](#websearch-interception-parameters "Direct link to WebSearch Interception Parameters")

ParameterTypeRequiredDescriptionExample`enabled_providers`List\[String]YesList of providers to enable web search interception for`[bedrock, azure, vertex_ai]``search_tool_name`StringNoSpecific search tool from `search_tools` config. If not set, uses first available search tool.`perplexity-search`

### Supported Provider Values[​](#supported-provider-values "Direct link to Supported Provider Values")

Use these values in `enabled_providers`:

ProviderValueDescriptionAWS Bedrock`bedrock`Amazon Bedrock Claude modelsAzure OpenAI`azure`Azure-hosted modelsGoogle Vertex AI`vertex_ai`Google Cloud Vertex AIAny OtherProvider nameAny LiteLLM-supported provider

### Complete Configuration Example[​](#complete-configuration-example "Direct link to Complete Configuration Example")

Complete config.yaml

```
model_list:
-model_name: bedrock-sonnet
litellm_params:
model: bedrock/us.anthropic.claude-sonnet-4-5-20250929-v1:0
aws_region_name: us-east-1

-model_name: azure-gpt4
litellm_params:
model: azure/gpt-4
api_base: https://my-azure.openai.azure.com
api_key: os.environ/AZURE_API_KEY

litellm_settings:
callbacks:
-websearch_interception:
enabled_providers:
- bedrock        # Enable for AWS Bedrock
- azure          # Enable for Azure OpenAI
- vertex_ai      # Enable for Google Vertex
search_tool_name: perplexity-search  # Optional: use specific search tool

# Configure search tools
search_tools:
-search_tool_name: perplexity-search
litellm_params:
search_provider: perplexity
api_key: os.environ/PERPLEXITY_API_KEY

-search_tool_name: tavily-search
litellm_params:
search_provider: tavily
api_key: os.environ/TAVILY_API_KEY
```

**How search tool selection works:**

- If `search_tool_name` is specified → Uses that specific search tool
- If `search_tool_name` is not specified → Uses first search tool in `search_tools` list
- In example above: Without `search_tool_name`, would use `perplexity-search` (first in list)

<!--THE END-->

- [Claude Code Quickstart](https://docs.litellm.ai/docs/tutorials/claude_responses_api)
- [Claude Code Cost Tracking](https://docs.litellm.ai/docs/tutorials/claude_code_customer_tracking)
- [Using Non-Anthropic Models](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models)