---
title: Anthropic Tool Search | liteLLM
url: https://docs.litellm.ai/docs/providers/anthropic_tool_search
source: sitemap
fetched_at: 2026-01-21T19:47:56.442280753-03:00
rendered_js: false
word_count: 588
summary: This document explains how to implement dynamic tool search with Claude models using LiteLLM to efficiently manage and load tools from large catalogs on-demand. It covers configuration for major cloud providers, search algorithm variants, and optimization strategies like deferred loading.
tags:
    - litellm
    - claude-ai
    - tool-search
    - function-calling
    - anthropic-api
    - context-optimization
category: guide
---

Tool search enables Claude to dynamically discover and load tools on-demand from large tool catalogs (10,000+ tools). Instead of loading all tool definitions into the context window upfront, Claude searches your tool catalog and loads only the tools it needs.

## Benefits[​](#benefits "Direct link to Benefits")

- **Context efficiency**: Avoid consuming massive portions of your context window with tool definitions
- **Better tool selection**: Claude's tool selection accuracy degrades with more than 30-50 tools. Tool search maintains accuracy even with thousands of tools
- **On-demand loading**: Tools are only loaded when Claude needs them

## Supported Models[​](#supported-models "Direct link to Supported Models")

Tool search is available on:

- Claude Opus 4.5
- Claude Sonnet 4.5

## Supported Platforms[​](#supported-platforms "Direct link to Supported Platforms")

- Anthropic API (direct)
- Azure Anthropic (Microsoft Foundry)
- Google Cloud Vertex AI
- Amazon Bedrock (invoke API only, not converse API)

LiteLLM supports both tool search variants:

### 1. Regex Tool Search (`tool_search_tool_regex_20251119`)[​](#1-regex-tool-search-tool_search_tool_regex_20251119 "Direct link to 1-regex-tool-search-tool_search_tool_regex_20251119")

Claude constructs regex patterns to search for tools.

### 2. BM25 Tool Search (`tool_search_tool_bm25_20251119`)[​](#2-bm25-tool-search-tool_search_tool_bm25_20251119 "Direct link to 2-bm25-tool-search-tool_search_tool_bm25_20251119")

Claude uses natural language queries to search for tools using the BM25 algorithm.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Basic Example with Regex Tool Search[​](#basic-example-with-regex-tool-search "Direct link to Basic Example with Regex Tool Search")

```
import litellm

response = litellm.completion(
    model="anthropic/claude-sonnet-4-5-20250929",
    messages=[
{"role":"user","content":"What is the weather in San Francisco?"}
],
    tools=[
# Tool search tool (regex variant)
{
"type":"tool_search_tool_regex_20251119",
"name":"tool_search_tool_regex"
},
# Deferred tool - will be loaded on-demand
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get the weather at a specific location",
"parameters":{
"type":"object",
"properties":{
"location":{"type":"string"},
"unit":{
"type":"string",
"enum":["celsius","fahrenheit"]
}
},
"required":["location"]
}
},
"defer_loading":True# Mark for deferred loading
},
# Another deferred tool
{
"type":"function",
"function":{
"name":"search_files",
"description":"Search through files in the workspace",
"parameters":{
"type":"object",
"properties":{
"query":{"type":"string"},
"file_types":{
"type":"array",
"items":{"type":"string"}
}
},
"required":["query"]
}
},
"defer_loading":True
}
]
)

print(response.choices[0].message.content)
```

### BM25 Tool Search Example[​](#bm25-tool-search-example "Direct link to BM25 Tool Search Example")

```
import litellm

response = litellm.completion(
    model="anthropic/claude-sonnet-4-5-20250929",
    messages=[
{"role":"user","content":"Search for Python files containing 'authentication'"}
],
    tools=[
# Tool search tool (BM25 variant)
{
"type":"tool_search_tool_bm25_20251119",
"name":"tool_search_tool_bm25"
},
# Deferred tools...
{
"type":"function",
"function":{
"name":"search_codebase",
"description":"Search through codebase files by content and filename",
"parameters":{
"type":"object",
"properties":{
"query":{"type":"string"},
"file_pattern":{"type":"string"}
},
"required":["query"]
}
},
"defer_loading":True
}
]
)
```

## Using with Azure Anthropic[​](#using-with-azure-anthropic "Direct link to Using with Azure Anthropic")

```
import litellm

response = litellm.completion(
    model="azure_anthropic/claude-sonnet-4-5",
    api_base="https://<your-resource>.services.ai.azure.com/anthropic",
    api_key="your-azure-api-key",
    messages=[
{"role":"user","content":"What's the weather like?"}
],
    tools=[
{
"type":"tool_search_tool_regex_20251119",
"name":"tool_search_tool_regex"
},
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get current weather",
"parameters":{
"type":"object",
"properties":{
"location":{"type":"string"}
},
"required":["location"]
}
},
"defer_loading":True
}
]
)
```

## Using with Vertex AI[​](#using-with-vertex-ai "Direct link to Using with Vertex AI")

```
import litellm

response = litellm.completion(
    model="vertex_ai/claude-sonnet-4-5",
    vertex_project="your-project-id",
    vertex_location="us-central1",
    messages=[
{"role":"user","content":"Search my documents"}
],
    tools=[
{
"type":"tool_search_tool_bm25_20251119",
"name":"tool_search_tool_bm25"
},
# Your deferred tools...
]
)
```

## Streaming Support[​](#streaming-support "Direct link to Streaming Support")

Tool search works with streaming:

```
import litellm

response = litellm.completion(
    model="anthropic/claude-sonnet-4-5-20250929",
    messages=[
{"role":"user","content":"Get the weather"}
],
    tools=[
{
"type":"tool_search_tool_regex_20251119",
"name":"tool_search_tool_regex"
},
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get weather information",
"parameters":{
"type":"object",
"properties":{
"location":{"type":"string"}
},
"required":["location"]
}
},
"defer_loading":True
}
],
    stream=True
)

for chunk in response:
if chunk.choices[0].delta.content:
print(chunk.choices[0].delta.content, end="")
```

## LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

Tool search works automatically through the LiteLLM proxy:

### Proxy Config[​](#proxy-config "Direct link to Proxy Config")

```
model_list:
-model_name: claude-sonnet
litellm_params:
model: anthropic/claude-sonnet-4-5-20250929
api_key: os.environ/ANTHROPIC_API_KEY
```

### Client Request[​](#client-request "Direct link to Client Request")

```
import openai

client = openai.OpenAI(
    api_key="your-litellm-proxy-key",
    base_url="http://0.0.0.0:4000"
)

response = client.chat.completions.create(
    model="claude-sonnet",
    messages=[
{"role":"user","content":"What's the weather?"}
],
    tools=[
{
"type":"tool_search_tool_regex_20251119",
"name":"tool_search_tool_regex"
},
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get weather information",
"parameters":{
"type":"object",
"properties":{
"location":{"type":"string"}
},
"required":["location"]
}
},
"defer_loading":True
}
]
)
```

## Important Notes[​](#important-notes "Direct link to Important Notes")

LiteLLM automatically detects tool search tools and adds the appropriate beta header based on your provider:

- **Anthropic API & Microsoft Foundry**: `advanced-tool-use-2025-11-20`
- **Google Cloud Vertex AI**: `tool-search-tool-2025-10-19`
- **Amazon Bedrock** (Invoke API, Opus 4.5 only): `tool-search-tool-2025-10-19`

You don't need to manually specify beta headers—LiteLLM handles this automatically.

### Deferred Loading[​](#deferred-loading "Direct link to Deferred Loading")

- Tools with `defer_loading: true` are only loaded when Claude discovers them via search
- At least one tool must be non-deferred (the tool search tool itself)
- Keep your 3-5 most frequently used tools as non-deferred for optimal performance

### Tool Descriptions[​](#tool-descriptions "Direct link to Tool Descriptions")

Write clear, descriptive tool names and descriptions that match how users describe tasks. The search algorithm uses:

- Tool names
- Tool descriptions
- Argument names
- Argument descriptions

### Usage Tracking[​](#usage-tracking "Direct link to Usage Tracking")

Tool search requests are tracked in the usage object:

```
response = litellm.completion(
    model="anthropic/claude-sonnet-4-5-20250929",
    messages=[{"role":"user","content":"Search for tools"}],
    tools=[...]
)

# Check tool search usage
if response.usage.server_tool_use:
print(f"Tool search requests: {response.usage.server_tool_use.tool_search_requests}")
```

## Error Handling[​](#error-handling "Direct link to Error Handling")

### All Tools Deferred[​](#all-tools-deferred "Direct link to All Tools Deferred")

```
# ❌ This will fail - at least one tool must be non-deferred
tools =[
{
"type":"function",
"function":{...},
"defer_loading":True
}
]

# ✅ Correct - tool search tool is non-deferred
tools =[
{
"type":"tool_search_tool_regex_20251119",
"name":"tool_search_tool_regex"
},
{
"type":"function",
"function":{...},
"defer_loading":True
}
]
```

### Missing Tool Definition[​](#missing-tool-definition "Direct link to Missing Tool Definition")

If Claude references a tool that isn't in your deferred tools list, you'll get an error. Make sure all tools that might be discovered are included in the tools parameter with `defer_loading: true`.

## Best Practices[​](#best-practices "Direct link to Best Practices")

1. **Keep frequently used tools non-deferred**: Your 3-5 most common tools should not have `defer_loading: true`
2. **Use semantic descriptions**: Tool descriptions should use natural language that matches user queries
3. **Choose the right variant**:
   
   - Use **regex** for exact pattern matching (faster)
   - Use **BM25** for natural language semantic search
4. **Monitor usage**: Track `tool_search_requests` in the usage object to understand search patterns
5. **Optimize tool catalog**: Remove unused tools and consolidate similar functionality

**Good use cases:**

- 10+ tools available in your system
- Tool definitions consuming &gt;10K tokens
- Experiencing tool selection accuracy issues
- Building systems with multiple tool categories
- Tool library growing over time

**When traditional tool calling is better:**

- Less than 10 tools total
- All tools are frequently used
- Very small tool definitions (&lt;100 tokens total)

## Limitations[​](#limitations "Direct link to Limitations")

- Not compatible with tool use examples
- Requires Claude Opus 4.5 or Sonnet 4.5
- On Bedrock, only available via invoke API (not converse API)
- On Bedrock, only supported for Claude Opus 4.5 (not Sonnet 4.5)
- BM25 variant (`tool_search_tool_bm25_20251119`) is not supported on Bedrock
- Maximum 10,000 tools in catalog
- Returns 3-5 most relevant tools per search

### Bedrock-Specific Notes[​](#bedrock-specific-notes "Direct link to Bedrock-Specific Notes")

When using Bedrock's Invoke API:

- The regex variant (`tool_search_tool_regex_20251119`) is automatically normalized to `tool_search_tool_regex`
- The BM25 variant (`tool_search_tool_bm25_20251119`) is automatically filtered out as it's not supported
- Tool search is only available for Claude Opus 4.5 models

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Anthropic Tool Search Documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/tool-search)
- [LiteLLM Tool Calling Guide](https://docs.litellm.ai/docs/completion/function_call)