---
title: Release Notes | liteLLM
url: https://docs.litellm.ai/release_notes
source: sitemap
fetched_at: 2026-01-21T19:41:13.959266166-03:00
rendered_js: false
word_count: 57449
summary: This document outlines the release notes and technical updates for LiteLLM version 1.81.0, focusing on performance optimizations, new model support, and administrative auditing features.
tags:
    - litellm-updates
    - claude-code
    - performance-optimization
    - image-handling
    - api-gateway
    - model-support
    - audit-logs
category: reference
---

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.81.0.rc.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Claude Code** - Support for using web search across Bedrock, Vertex AI, and all LiteLLM providers
- **Major Change** - [50MB limit on image URL downloads](#major-change---chatcompletions-image-url-download-size-limit) to improve reliability
- **Performance** - [25% CPU Usage Reduction](#performance---25-cpu-usage-reduction) by removing premature model.dump() calls from the hot path
- **Deleted Keys Audit Table on UI** - [View deleted keys and teams for audit purposes](https://docs.litellm.ai/docs/proxy/deleted_keys_teams.md) with spend and budget information at the time of deletion

* * *

## Claude Code - Web Search Across All Providers[​](#claude-code---web-search-across-all-providers "Direct link to Claude Code - Web Search Across All Providers")

This release brings web search support to Claude Code across all LiteLLM providers (Bedrock, Azure, Vertex AI, and more), enabling AI coding assistants to search the web for real-time information.

This means you can now use Claude Code's web search tool with any provider, not just Anthropic's native API. LiteLLM automatically intercepts web search requests and executes them server-side using your configured search provider (Perplexity, Tavily, Exa AI, and more).

Proxy Admins can configure web search interception in their LiteLLM proxy config to enable this capability for their teams using Claude Code with Bedrock, Azure, or any other supported provider.

[**Learn more →**](https://docs.litellm.ai/docs/tutorials/claude_code_websearch.md)

* * *

## Major Change - /chat/completions Image URL Download Size Limit[​](#major-change---chatcompletions-image-url-download-size-limit "Direct link to Major Change - /chat/completions Image URL Download Size Limit")

To improve reliability and prevent memory issues, LiteLLM now includes a configurable **50MB limit** on image URL downloads by default. Previously, there was no limit on image downloads, which could occasionally cause memory issues with very large images.

### How It Works[​](#how-it-works "Direct link to How It Works")

Requests with image URLs exceeding 50MB will receive a helpful error message:

```
curl -X POST 'https://your-litellm-proxy.com/chat/completions' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-1234' \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://example.com/very-large-image.jpg"
            }
          }
        ]
      }
    ]
  }'
```

**Error Response:**

```
{
"error":{
"message":"Error: Image size (75.50MB) exceeds maximum allowed size (50.0MB). url=https://example.com/very-large-image.jpg",
"type":"ImageFetchError"
}
}
```

### Configuring the Limit[​](#configuring-the-limit "Direct link to Configuring the Limit")

The default 50MB limit works well for most use cases, but you can easily adjust it if needed:

**Increase the limit (e.g., to 100MB):**

```
export MAX_IMAGE_URL_DOWNLOAD_SIZE_MB=100
```

**Disable image URL downloads (for security):**

```
export MAX_IMAGE_URL_DOWNLOAD_SIZE_MB=0
```

**Docker Configuration:**

```
docker run \
  -e MAX_IMAGE_URL_DOWNLOAD_SIZE_MB=100 \
  -p 4000:4000 \
  docker.litellm.ai/berriai/litellm:v1.81.0
```

**Proxy Config (config.yaml):**

```
general_settings:
master_key: sk-1234

# Set via environment variable
environment_variables:
MAX_IMAGE_URL_DOWNLOAD_SIZE_MB:"100"
```

### Why Add This?[​](#why-add-this "Direct link to Why Add This?")

This feature improves reliability by:

- Preventing memory issues from very large images
- Aligning with OpenAI's 50MB payload limit
- Validating image sizes early (when Content-Length header is available)

* * *

## Performance - 25% CPU Usage Reduction[​](#performance---25-cpu-usage-reduction "Direct link to Performance - 25% CPU Usage Reduction")

LiteLLM now reduces CPU usage by removing premature `model.dump()` calls from the hot path in request processing. Previously, Pydantic model serialization was performed earlier and more frequently than necessary, causing unnecessary CPU overhead on every request. By deferring serialization until it is actually needed, LiteLLM reduces CPU usage and improves request throughput under high load.

* * *

## Deleted Keys Audit Table on UI[​](#deleted-keys-audit-table-on-ui "Direct link to Deleted Keys Audit Table on UI")

LiteLLM now provides a comprehensive audit table for deleted API keys and teams directly in the UI. This feature allows you to easily track the spend of deleted keys, view their associated team information, and maintain accurate financial records for auditing and compliance purposes. The table displays key details including key aliases, team associations, and spend information captured at the time of deletion. For more information on how to use this feature, see the [Deleted Keys & Teams documentation](https://docs.litellm.ai/docs/proxy/deleted_keys_teams.md).

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelFeaturesOpenAI`gpt-5.2-codex`Code generationAzure`azure/gpt-5.2-codex`Code generationCerebras`cerebras/zai-glm-4.7`Reasoning, function callingReplicateAll chat modelsFull support for all Replicate chat models

#### Features[​](#features "Direct link to Features")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Add missing anthropic tool results in response - [PR #18945](https://github.com/BerriAI/litellm/pull/18945)
  - Preserve web\_fetch\_tool\_result in multi-turn conversations - [PR #18142](https://github.com/BerriAI/litellm/pull/18142)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add presence\_penalty support for Google AI Studio - [PR #18154](https://github.com/BerriAI/litellm/pull/18154)
  - Forward extra\_headers in generateContent adapter - [PR #18935](https://github.com/BerriAI/litellm/pull/18935)
  - Add medium value support for detail param - [PR #19187](https://github.com/BerriAI/litellm/pull/19187)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Improve passthrough endpoint URL parsing and construction - [PR #17526](https://github.com/BerriAI/litellm/pull/17526)
  - Add type object to tool schemas missing type field - [PR #19103](https://github.com/BerriAI/litellm/pull/19103)
  - Keep type field in Gemini schema when properties is empty - [PR #18979](https://github.com/BerriAI/litellm/pull/18979)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add OpenAI-compatible service\_tier parameter translation - [PR #18091](https://github.com/BerriAI/litellm/pull/18091)
  - Add user auth in standard logging object for Bedrock passthrough - [PR #19140](https://github.com/BerriAI/litellm/pull/19140)
  - Strip throughput tier suffixes from model names - [PR #19147](https://github.com/BerriAI/litellm/pull/19147)
- [**OCI**](https://docs.litellm.ai/docs/providers/oci)
  
  - Handle OpenAI-style image\_url object in multimodal messages - [PR #18272](https://github.com/BerriAI/litellm/pull/18272)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Set finish\_reason to tool\_calls and remove broken capability check - [PR #18924](https://github.com/BerriAI/litellm/pull/18924)
- [**Watsonx**](https://docs.litellm.ai/docs/providers/watsonx/index)
  
  - Allow passing scope ID for Watsonx inferencing - [PR #18959](https://github.com/BerriAI/litellm/pull/18959)
- [**Replicate**](https://docs.litellm.ai/docs/providers/replicate)
  
  - Add all chat Replicate models support - [PR #18954](https://github.com/BerriAI/litellm/pull/18954)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Add OpenRouter support for image/generation endpoints - [PR #19059](https://github.com/BerriAI/litellm/pull/19059)
- [**Volcengine**](https://docs.litellm.ai/docs/providers/volcano)
  
  - Add max\_tokens settings for Volcengine models (deepseek-v3-2, glm-4-7, kimi-k2-thinking) - [PR #19076](https://github.com/BerriAI/litellm/pull/19076)
- **Azure Model Router**
  
  - New Model - Azure Model Router on LiteLLM AI Gateway - [PR #19054](https://github.com/BerriAI/litellm/pull/19054)
- **GPT-5 Models**
  
  - Correct context window sizes for GPT-5 model variants - [PR #18928](https://github.com/BerriAI/litellm/pull/18928)
  - Correct max\_input\_tokens for GPT-5 models - [PR #19056](https://github.com/BerriAI/litellm/pull/19056)
- **Text Completion**
  
  - Support token IDs (list of integers) as prompt - [PR #18011](https://github.com/BerriAI/litellm/pull/18011)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Prevent dropping thinking when any message has thinking\_blocks - [PR #18929](https://github.com/BerriAI/litellm/pull/18929)
  - Fix anthropic token counter with thinking - [PR #19067](https://github.com/BerriAI/litellm/pull/19067)
  - Add better error handling for Anthropic - [PR #18955](https://github.com/BerriAI/litellm/pull/18955)
  - Fix Anthropic during call error - [PR #19060](https://github.com/BerriAI/litellm/pull/19060)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix missing `completion_tokens_details` in Gemini 3 Flash when reasoning\_effort is not used - [PR #18898](https://github.com/BerriAI/litellm/pull/18898)
  - Fix Gemini Image Generation imageConfig parameters - [PR #18948](https://github.com/BerriAI/litellm/pull/18948)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Fix Vertex AI 400 Error with CachedContent model mismatch - [PR #19193](https://github.com/BerriAI/litellm/pull/19193)
  - Fix Vertex AI doesn't support structured output - [PR #19201](https://github.com/BerriAI/litellm/pull/19201)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fix Claude Code (`/messages`) Bedrock Invoke usage and request signing - [PR #19111](https://github.com/BerriAI/litellm/pull/19111)
  - Fix model ID encoding for Bedrock passthrough - [PR #18944](https://github.com/BerriAI/litellm/pull/18944)
  - Respect max\_completion\_tokens in thinking feature - [PR #18946](https://github.com/BerriAI/litellm/pull/18946)
  - Fix header forwarding in Bedrock passthrough - [PR #19007](https://github.com/BerriAI/litellm/pull/19007)
  - Fix Bedrock stability model usage issues - [PR #19199](https://github.com/BerriAI/litellm/pull/19199)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/messages (Claude Code)**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Add support for Tool Search on `/messages` API across Azure, Bedrock, and Anthropic API - [PR #19165](https://github.com/BerriAI/litellm/pull/19165)
  - Track end-users with Claude Code (`/messages`) for better analytics and monitoring - [PR #19171](https://github.com/BerriAI/litellm/pull/19171)
  - Add web search support using LiteLLM `/search` endpoint with Claude Code (`/messages`) - [PR #19263](https://github.com/BerriAI/litellm/pull/19263), [PR #19294](https://github.com/BerriAI/litellm/pull/19294)
- [**/messages (Claude Code) - Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add support for Prompt Caching with Bedrock Converse on `/messages` - [PR #19123](https://github.com/BerriAI/litellm/pull/19123)
  - Ensure budget tokens are passed to Bedrock Converse API correctly on `/messages` - [PR #19107](https://github.com/BerriAI/litellm/pull/19107)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Add support for caching for responses API - [PR #19068](https://github.com/BerriAI/litellm/pull/19068)
  - Add retry policy support to responses API - [PR #19074](https://github.com/BerriAI/litellm/pull/19074)
- **Realtime API**
  
  - Use non-streaming method for endpoint v1/a2a/message/send - [PR #19025](https://github.com/BerriAI/litellm/pull/19025)
- **Batch API**
  
  - Fix batch deletion and retrieve - [PR #18340](https://github.com/BerriAI/litellm/pull/18340)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Fix responses content can't be none - [PR #19064](https://github.com/BerriAI/litellm/pull/19064)
  - Fix model name from query param in realtime request - [PR #19135](https://github.com/BerriAI/litellm/pull/19135)
  - Fix video status/content credential injection for wildcard models - [PR #18854](https://github.com/BerriAI/litellm/pull/18854)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

**Virtual Keys**

- View deleted keys for audit purposes - [PR #18228](https://github.com/BerriAI/litellm/pull/18228), [PR #19268](https://github.com/BerriAI/litellm/pull/19268)
- Add status query parameter for keys list - [PR #19260](https://github.com/BerriAI/litellm/pull/19260)
- Refetch keys after key creation - [PR #18994](https://github.com/BerriAI/litellm/pull/18994)
- Refresh keys list on delete - [PR #19262](https://github.com/BerriAI/litellm/pull/19262)
- Simplify key generate permission error - [PR #18997](https://github.com/BerriAI/litellm/pull/18997)
- Add search to key edit team dropdown - [PR #19119](https://github.com/BerriAI/litellm/pull/19119)

**Teams & Organizations**

- View deleted teams for audit purposes - [PR #18228](https://github.com/BerriAI/litellm/pull/18228), [PR #19268](https://github.com/BerriAI/litellm/pull/19268)
- Add filters to organization table - [PR #18916](https://github.com/BerriAI/litellm/pull/18916)
- Add query parameters to `/organization/list` - [PR #18910](https://github.com/BerriAI/litellm/pull/18910)
- Add status query parameter for teams list - [PR #19260](https://github.com/BerriAI/litellm/pull/19260)
- Show internal users their spend only - [PR #19227](https://github.com/BerriAI/litellm/pull/19227)
- Allow preventing team admins from deleting members from teams - [PR #19128](https://github.com/BerriAI/litellm/pull/19128)
- Refactor team member icon buttons - [PR #19192](https://github.com/BerriAI/litellm/pull/19192)

**Models + Endpoints**

- Display health information in public model hub - [PR #19256](https://github.com/BerriAI/litellm/pull/19256), [PR #19258](https://github.com/BerriAI/litellm/pull/19258)
- Quality of life improvements for Anthropic models - [PR #19058](https://github.com/BerriAI/litellm/pull/19058)
- Create reusable model select component - [PR #19164](https://github.com/BerriAI/litellm/pull/19164)
- Edit settings model dropdown - [PR #19186](https://github.com/BerriAI/litellm/pull/19186)
- Fix model hub client side exception - [PR #19045](https://github.com/BerriAI/litellm/pull/19045)

**Usage & Analytics**

- Allow top virtual keys and models to show more entries - [PR #19050](https://github.com/BerriAI/litellm/pull/19050)
- Fix Y axis on model activity chart - [PR #19055](https://github.com/BerriAI/litellm/pull/19055)
- Add Team ID and Team Name in export report - [PR #19047](https://github.com/BerriAI/litellm/pull/19047)
- Add user metrics for Prometheus - [PR #18785](https://github.com/BerriAI/litellm/pull/18785)

**SSO & Auth**

- Allow setting custom MSFT Base URLs - [PR #18977](https://github.com/BerriAI/litellm/pull/18977)
- Allow overriding env var attribute names - [PR #18998](https://github.com/BerriAI/litellm/pull/18998)
- Fix SCIM GET /Users error and enforce SCIM 2.0 compliance - [PR #17420](https://github.com/BerriAI/litellm/pull/17420)
- Feature flag for SCIM compliance fix - [PR #18878](https://github.com/BerriAI/litellm/pull/18878)

**General UI**

- Add allowClear to dropdown components for better UX - [PR #18778](https://github.com/BerriAI/litellm/pull/18778)
- Add community engagement buttons - [PR #19114](https://github.com/BerriAI/litellm/pull/19114)
- UI Feedback Form - why LiteLLM - [PR #18999](https://github.com/BerriAI/litellm/pull/18999)
- Refactor user and team table filters to reusable component - [PR #19010](https://github.com/BerriAI/litellm/pull/19010)
- Adjusting new badges - [PR #19278](https://github.com/BerriAI/litellm/pull/19278)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- Container API routes return 401 for non-admin users - routes missing from openai\_routes - [PR #19115](https://github.com/BerriAI/litellm/pull/19115)
- Allow routing to regional endpoints for Containers API - [PR #19118](https://github.com/BerriAI/litellm/pull/19118)
- Fix Azure Storage circular reference error - [PR #19120](https://github.com/BerriAI/litellm/pull/19120)
- Fix prompt deletion fails with Prisma FieldNotFoundError - [PR #18966](https://github.com/BerriAI/litellm/pull/18966)

* * *

## AI Integrations[​](#ai-integrations "Direct link to AI Integrations")

### Logging[​](#logging "Direct link to Logging")

- [**OpenTelemetry**](https://docs.litellm.ai/docs/proxy/logging#opentelemetry)
  
  - Update semantic conventions to 1.38 (gen\_ai attributes) - [PR #18793](https://github.com/BerriAI/litellm/pull/18793)
- [**LangSmith**](https://docs.litellm.ai/docs/proxy/logging#langsmith)
  
  - Hoist thread grouping metadata (session\_id, thread) - [PR #18982](https://github.com/BerriAI/litellm/pull/18982)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Include Langfuse logger in JSON logging when Langfuse callback is used - [PR #19162](https://github.com/BerriAI/litellm/pull/19162)
- [**Logfire**](https://docs.litellm.ai/docs/observability/logfire)
  
  - Add ability to customize Logfire base URL through env var - [PR #19148](https://github.com/BerriAI/litellm/pull/19148)
- **General Logging**
  
  - Enable JSON logging via configuration and add regression test - [PR #19037](https://github.com/BerriAI/litellm/pull/19037)
  - Fix header forwarding for embeddings endpoint - [PR #18960](https://github.com/BerriAI/litellm/pull/18960)
  - Preserve llm\_provider-* headers in error responses - [PR #19020](https://github.com/BerriAI/litellm/pull/19020)
  - Fix turn\_off\_message\_logging not redacting request messages in proxy\_server\_request field - [PR #18897](https://github.com/BerriAI/litellm/pull/18897)

### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**Grayswan**](https://docs.litellm.ai/docs/proxy/guardrails/grayswan)
  
  - Implement fail-open option (default: True) - [PR #18266](https://github.com/BerriAI/litellm/pull/18266)
- [**Pangea**](https://docs.litellm.ai/docs/proxy/guardrails/pangea)
  
  - Respect `default_on` during initialization - [PR #18912](https://github.com/BerriAI/litellm/pull/18912)
- [**Panw Prisma AIRS**](https://docs.litellm.ai/docs/proxy/guardrails/panw_prisma_airs)
  
  - Add custom violation message support - [PR #19272](https://github.com/BerriAI/litellm/pull/19272)
- **General Guardrails**
  
  - Fix SerializationIterator error and pass tools to guardrail - [PR #18932](https://github.com/BerriAI/litellm/pull/18932)
  - Properly handle custom guardrails parameters - [PR #18978](https://github.com/BerriAI/litellm/pull/18978)
  - Use clean error messages for blocked requests - [PR #19023](https://github.com/BerriAI/litellm/pull/19023)
  - Guardrail moderation support with responses API - [PR #18957](https://github.com/BerriAI/litellm/pull/18957)
  - Fix model-level guardrails not taking effect - [PR #18895](https://github.com/BerriAI/litellm/pull/18895)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Cost Calculation Fixes**
  
  - Include IMAGE token count in cost calculation for Gemini models - [PR #18876](https://github.com/BerriAI/litellm/pull/18876)
  - Fix negative text\_tokens when using cache with images - [PR #18768](https://github.com/BerriAI/litellm/pull/18768)
  - Fix image tokens spend logging for `/images/generations` - [PR #19009](https://github.com/BerriAI/litellm/pull/19009)
  - Fix incorrect `prompt_tokens_details` in Gemini Image Generation - [PR #19070](https://github.com/BerriAI/litellm/pull/19070)
  - Fix case-insensitive model cost map lookup - [PR #18208](https://github.com/BerriAI/litellm/pull/18208)
- **Pricing Updates**
  
  - Correct pricing for `openrouter/openai/gpt-oss-20b` - [PR #18899](https://github.com/BerriAI/litellm/pull/18899)
  - Add pricing for `azure_ai/claude-opus-4-5` - [PR #19003](https://github.com/BerriAI/litellm/pull/19003)
  - Update Novita models prices - [PR #19005](https://github.com/BerriAI/litellm/pull/19005)
  - Fix Azure Grok prices - [PR #19102](https://github.com/BerriAI/litellm/pull/19102)
  - Fix GCP GLM-4.7 pricing - [PR #19172](https://github.com/BerriAI/litellm/pull/19172)
  - Sync DeepSeek chat/reasoner to V3.2 pricing - [PR #18884](https://github.com/BerriAI/litellm/pull/18884)
  - Correct cache\_read pricing for gemini-2.5-pro models - [PR #18157](https://github.com/BerriAI/litellm/pull/18157)
- **Budget & Rate Limiting**
  
  - Correct budget limit validation operator (&gt;=) for team members - [PR #19207](https://github.com/BerriAI/litellm/pull/19207)
  - Fix TPM 25% limiting by ensuring priority queue logic - [PR #19092](https://github.com/BerriAI/litellm/pull/19092)
  - Cleanup spend logs cron verification, fix, and docs - [PR #19085](https://github.com/BerriAI/litellm/pull/19085)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- Prevent duplicate MCP reload scheduler registration - [PR #18934](https://github.com/BerriAI/litellm/pull/18934)
- Forward MCP extra headers case-insensitively - [PR #18940](https://github.com/BerriAI/litellm/pull/18940)
- Fix MCP REST auth checks - [PR #19051](https://github.com/BerriAI/litellm/pull/19051)
- Fix generating two telemetry events in responses - [PR #18938](https://github.com/BerriAI/litellm/pull/18938)
- Fix MCP chat completions - [PR #19129](https://github.com/BerriAI/litellm/pull/19129)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Performance Improvements**
  
  - Remove bottleneck causing high CPU usage & overhead under heavy load - [PR #19049](https://github.com/BerriAI/litellm/pull/19049)
  - Add CI enforcement for O(1) operations in `_get_model_cost_key` to prevent performance regressions - [PR #19052](https://github.com/BerriAI/litellm/pull/19052)
  - Fix Azure embeddings JSON parsing to prevent connection leaks and ensure proper router cooldown - [PR #19167](https://github.com/BerriAI/litellm/pull/19167)
  - Do not fallback to token counter if `disable_token_counter` is enabled - [PR #19041](https://github.com/BerriAI/litellm/pull/19041)
- **Reliability**
  
  - Add fallback endpoints support - [PR #19185](https://github.com/BerriAI/litellm/pull/19185)
  - Fix stream\_timeout parameter functionality - [PR #19191](https://github.com/BerriAI/litellm/pull/19191)
  - Fix model matching priority in configuration - [PR #19012](https://github.com/BerriAI/litellm/pull/19012)
  - Fix num\_retries in litellm\_params as per config - [PR #18975](https://github.com/BerriAI/litellm/pull/18975)
  - Handle exceptions without response parameter - [PR #18919](https://github.com/BerriAI/litellm/pull/18919)
- **Infrastructure**
  
  - Add Custom CA certificates to boto3 clients - [PR #18942](https://github.com/BerriAI/litellm/pull/18942)
  - Update boto3 to 1.40.15 and aioboto3 to 15.5.0 - [PR #19090](https://github.com/BerriAI/litellm/pull/19090)
  - Make keepalive\_timeout parameter work for Gunicorn - [PR #19087](https://github.com/BerriAI/litellm/pull/19087)
- **Helm Chart**
  
  - Fix mount config.yaml as single file in Helm chart - [PR #19146](https://github.com/BerriAI/litellm/pull/19146)
  - Sync Helm chart versioning with production standards and Docker versions - [PR #18868](https://github.com/BerriAI/litellm/pull/18868)

* * *

## Database Changes[​](#database-changes "Direct link to Database Changes")

### Schema Updates[​](#schema-updates "Direct link to Schema Updates")

TableChange TypeDescriptionPR`LiteLLM_ProxyModelTable`New ColumnsAdded `created_at` and `updated_at` timestamp fields[PR #18937](https://github.com/BerriAI/litellm/pull/18937)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- Add LiteLLM architecture md doc - [PR #19057](https://github.com/BerriAI/litellm/pull/19057), [PR #19252](https://github.com/BerriAI/litellm/pull/19252)
- Add troubleshooting guide - [PR #19096](https://github.com/BerriAI/litellm/pull/19096), [PR #19097](https://github.com/BerriAI/litellm/pull/19097), [PR #19099](https://github.com/BerriAI/litellm/pull/19099)
- Add structured issue reporting guides for CPU and memory issues - [PR #19117](https://github.com/BerriAI/litellm/pull/19117)
- Add Redis requirement warning for high-traffic deployments - [PR #18892](https://github.com/BerriAI/litellm/pull/18892)
- Update load balancing and routing with enable\_pre\_call\_checks - [PR #18888](https://github.com/BerriAI/litellm/pull/18888)
- Updated pass\_through with guided param - [PR #18886](https://github.com/BerriAI/litellm/pull/18886)
- Update message content types link and add content types table - [PR #18209](https://github.com/BerriAI/litellm/pull/18209)
- Add Redis initialization with kwargs - [PR #19183](https://github.com/BerriAI/litellm/pull/19183)
- Improve documentation for routing LLM calls via SAP Gen AI Hub - [PR #19166](https://github.com/BerriAI/litellm/pull/19166)
- Deleted Keys and Teams docs - [PR #19291](https://github.com/BerriAI/litellm/pull/19291)
- Claude Code end user tracking guide - [PR #19176](https://github.com/BerriAI/litellm/pull/19176)
- Add MCP troubleshooting guide - [PR #19122](https://github.com/BerriAI/litellm/pull/19122)
- Add auth message UI documentation - [PR #19063](https://github.com/BerriAI/litellm/pull/19063)
- Add guide for mounting custom callbacks in Helm/K8s - [PR #19136](https://github.com/BerriAI/litellm/pull/19136)

* * *

## Bug Fixes[​](#bug-fixes-1 "Direct link to Bug Fixes")

- Fix Swagger UI path execute error with server\_root\_path in OpenAPI schema - [PR #18947](https://github.com/BerriAI/litellm/pull/18947)
- Normalize OpenAI SDK BaseModel choices/messages to avoid Pydantic serializer warnings - [PR #18972](https://github.com/BerriAI/litellm/pull/18972)
- Add contextual gap checks and word-form digits - [PR #18301](https://github.com/BerriAI/litellm/pull/18301)
- Clean up orphaned files from repository root - [PR #19150](https://github.com/BerriAI/litellm/pull/19150)
- Include proxy/prisma\_migration.py in non-root - [PR #18971](https://github.com/BerriAI/litellm/pull/18971)
- Update prisma\_migration.py - [PR #19083](https://github.com/BerriAI/litellm/pull/19083)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @yogeshwaran10 made their first contribution in [PR #18898](https://github.com/BerriAI/litellm/pull/18898)
- @theonlypal made their first contribution in [PR #18937](https://github.com/BerriAI/litellm/pull/18937)
- @jonmagic made their first contribution in [PR #18935](https://github.com/BerriAI/litellm/pull/18935)
- @houdataali made their first contribution in [PR #19025](https://github.com/BerriAI/litellm/pull/19025)
- @hummat made their first contribution in [PR #18972](https://github.com/BerriAI/litellm/pull/18972)
- @berkeyalciin made their first contribution in [PR #18966](https://github.com/BerriAI/litellm/pull/18966)
- @MateuszOssGit made their first contribution in [PR #18959](https://github.com/BerriAI/litellm/pull/18959)
- @xfan001 made their first contribution in [PR #18947](https://github.com/BerriAI/litellm/pull/18947)
- @nulone made their first contribution in [PR #18884](https://github.com/BerriAI/litellm/pull/18884)
- @debnil-mercor made their first contribution in [PR #18919](https://github.com/BerriAI/litellm/pull/18919)
- @hakhundov made their first contribution in [PR #17420](https://github.com/BerriAI/litellm/pull/17420)
- @rohanwinsor made their first contribution in [PR #19078](https://github.com/BerriAI/litellm/pull/19078)
- @pgolm made their first contribution in [PR #19020](https://github.com/BerriAI/litellm/pull/19020)
- @vikigenius made their first contribution in [PR #19148](https://github.com/BerriAI/litellm/pull/19148)
- @burnerburnerburnerman made their first contribution in [PR #19090](https://github.com/BerriAI/litellm/pull/19090)
- @yfge made their first contribution in [PR #19076](https://github.com/BerriAI/litellm/pull/19076)
- @danielnyari-seon made their first contribution in [PR #19083](https://github.com/BerriAI/litellm/pull/19083)
- @guilherme-segantini made their first contribution in [PR #19166](https://github.com/BerriAI/litellm/pull/19166)
- @jgreek made their first contribution in [PR #19147](https://github.com/BerriAI/litellm/pull/19147)
- @anand-kamble made their first contribution in [PR #19193](https://github.com/BerriAI/litellm/pull/19193)
- @neubig made their first contribution in [PR #19162](https://github.com/BerriAI/litellm/pull/19162)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.80.15.rc.1...v1.81.0.rc.1)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.80.15-stable.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Manus API Support** - [New provider support for Manus API on /responses and GET /responses endpoints](https://docs.litellm.ai/docs/providers/manus)
- **MiniMax Provider** - [Full support for MiniMax chat completions, TTS, and Anthropic native endpoint](https://docs.litellm.ai/docs/providers/minimax)
- **AWS Polly TTS** - [New TTS provider using AWS Polly API](https://docs.litellm.ai/docs/providers/aws_polly)
- **SSO Role Mapping** - Configure role mappings for SSO providers directly in the UI
- **Cost Estimator** - New UI tool for estimating costs across multiple models and requests
- **MCP Global Mode** - [Configure MCP servers globally with visibility controls](https://docs.litellm.ai/docs/mcp)
- **Interactions API Bridge** - [Use all LiteLLM providers with the Interactions API](https://docs.litellm.ai/docs/interactions)
- **RAG Query Endpoint** - [New RAG Search/Query endpoint for retrieval-augmented generation](https://docs.litellm.ai/docs/search/index)
- **UI Usage - Endpoint Activity** - [Users can now see Endpoint Activity Metrics in the UI](https://docs.litellm.ai/docs/proxy/endpoint_activity.md)
- **50% Overhead Reduction** - LiteLLM now sends 2.5× more requests to LLM providers

* * *

## Performance - 50% Overhead Reduction[​](#performance---50-overhead-reduction "Direct link to Performance - 50% Overhead Reduction")

LiteLLM now sends 2.5× more requests to LLM providers by replacing sequential if/elif chains with O(1) dictionary lookups for provider configuration resolution (92.7% faster). This optimization has a high impact because it runs inside the client decorator, which is invoked on every HTTP request made to the proxy server.

### Before[​](#before "Direct link to Before")

> **Note:** Worse-looking provider metrics are a good sign here—they indicate requests spend less time inside LiteLLM.

```
============================================================
Fake LLM Provider Stats (When called by LiteLLM)
============================================================
Total Time:            0.56s
Requests/Second:       10746.68

Latency Statistics (seconds):
   Mean:               0.2039s
   Median (p50):       0.2310s
   Min:                0.0323s
   Max:                0.3928s
   Std Dev:            0.1166s
   p95:                0.3574s
   p99:                0.3748s

Status Codes:
   200: 6000
```

### After[​](#after "Direct link to After")

```
============================================================
Fake LLM Provider Stats (When called by LiteLLM)
============================================================
Total Time:            1.42s
Requests/Second:       4224.49

Latency Statistics (seconds):
   Mean:               0.5300s
   Median (p50):       0.5871s
   Min:                0.0885s
   Max:                1.0482s
   Std Dev:            0.3065s
   p95:                0.9750s
   p99:                1.0444s

Status Codes:
   200: 6000
```

> The benchmarks run LiteLLM locally with a lightweight LLM provider to eliminate network latency, isolating internal overhead and bottlenecks so we can focus on reducing pure LiteLLM overhead on a single instance.

* * *

### UI Usage - Endpoint Activity[​](#ui-usage---endpoint-activity "Direct link to UI Usage - Endpoint Activity")

Users can now see Endpoint Activity Metrics in the UI.

* * *

## New Providers and Endpoints[​](#new-providers-and-endpoints "Direct link to New Providers and Endpoints")

### New Providers (11 new providers)[​](#new-providers-11-new-providers "Direct link to New Providers (11 new providers)")

ProviderSupported LiteLLM EndpointsDescription[Manus](https://docs.litellm.ai/docs/providers/manus)`/responses`Manus API for agentic workflows[Manus](https://docs.litellm.ai/docs/providers/manus)`GET /responses`Manus API for retrieving responses[Manus](https://docs.litellm.ai/docs/providers/manus)`/files`Manus API for file management[MiniMax](https://docs.litellm.ai/docs/providers/minimax)`/chat/completions`MiniMax chat completions[MiniMax](https://docs.litellm.ai/docs/providers/minimax)`/audio/speech`MiniMax text-to-speech[AWS Polly](https://docs.litellm.ai/docs/providers/aws_polly)`/audio/speech`AWS Polly text-to-speech API[GigaChat](https://docs.litellm.ai/docs/providers/gigachat)`/chat/completions`GigaChat provider for Russian language AI[LlamaGate](https://docs.litellm.ai/docs/providers/llamagate)`/chat/completions`LlamaGate chat completions[LlamaGate](https://docs.litellm.ai/docs/providers/llamagate)`/embeddings`LlamaGate embeddings[Abliteration AI](https://docs.litellm.ai/docs/providers/abliteration)`/chat/completions`Abliteration.ai provider support[Bedrock](https://docs.litellm.ai/docs/providers/bedrock)`/v1/messages/count_tokens`Bedrock as new provider for token counting

### New LLM API Endpoints (3 new endpoints)[​](#new-llm-api-endpoints-3-new-endpoints "Direct link to New LLM API Endpoints (3 new endpoints)")

EndpointMethodDescriptionDocumentation`/responses/compact`POSTCompact responses API endpoint[Docs](https://docs.litellm.ai/docs/response_api)`/rag/query`POSTRAG Search/Query endpoint[Docs](https://docs.litellm.ai/docs/search/index)`/containers/{id}/files`POSTUpload files to containers[Docs](https://docs.litellm.ai/docs/container_files)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support (100+ new models)[​](#new-model-support-100-new-models "Direct link to New Model Support (100+ new models)")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesAzure`azure/gpt-5.2`400K$1.75$14.00Reasoning, vision, cachingAzure`azure/gpt-5.2-chat`128K$1.75$14.00Reasoning, visionAzure`azure/gpt-5.2-pro`400K$21.00$168.00Reasoning, vision, web searchAzure`azure/gpt-image-1.5`-Token-basedToken-basedImage generation/editingAzure AI`azure_ai/gpt-oss-120b`131K$0.15$0.60Function callingAzure AI`azure_ai/flux.2-pro`--$0.04/imageImage generationAzure AI`azure_ai/deepseek-v3.2`164K$0.58$1.68Reasoning, function callingBedrock`amazon.nova-2-multimodal-embeddings-v1:0`8K$0.135-Multimodal embeddingsBedrock`writer.palmyra-x4-v1:0`128K$2.50$10.00Function calling, PDFBedrock`writer.palmyra-x5-v1:0`1M$0.60$6.00Function calling, PDFBedrock`moonshot.kimi-k2-v1:0`---Kimi K2 modelCerebras`cerebras/zai-glm-4.6`128K$2.25$2.75Reasoning, function callingGigaChat`gigachat/GigaChat-2-Lite`---Chat completionsGigaChat`gigachat/GigaChat-2-Max`---Chat completionsGigaChat`gigachat/GigaChat-2-Pro`---Chat completionsGemini`gemini/veo-3.1-generate-001`---Video generationGemini`gemini/veo-3.1-fast-generate-001`---Video generationGitHub Copilot25+ modelsVarious--Chat completionsLlamaGate15+ modelsVarious--Chat, vision, embeddingsMiniMax`minimax/abab7-chat-preview`---Chat completionsNovita80+ modelsVariousVariousVariousChat, vision, embeddingsOpenRouter`openrouter/google/gemini-3-flash-preview`---Chat completionsTogether AIMultiple modelsVariousVariousVariousResponse schema supportVertex AI`vertex_ai/zai-glm-4.7`---GLM 4.7 support

#### Features[​](#features "Direct link to Features")

- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add image tokens in chat completion - [PR #18327](https://github.com/BerriAI/litellm/pull/18327)
  - Add usage object in image generation - [PR #18328](https://github.com/BerriAI/litellm/pull/18328)
  - Add thought signature support via tool call id - [PR #18374](https://github.com/BerriAI/litellm/pull/18374)
  - Add thought signature for non tool call requests - [PR #18581](https://github.com/BerriAI/litellm/pull/18581)
  - Preserve system instructions - [PR #18585](https://github.com/BerriAI/litellm/pull/18585)
  - Fix Gemini 3 images in tool response - [PR #18190](https://github.com/BerriAI/litellm/pull/18190)
  - Support snake\_case for google\_search tool parameters - [PR #18451](https://github.com/BerriAI/litellm/pull/18451)
  - Google GenAI adapter inline data support - [PR #18477](https://github.com/BerriAI/litellm/pull/18477)
  - Add deprecation\_date for discontinued Google models - [PR #18550](https://github.com/BerriAI/litellm/pull/18550)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add centralized get\_vertex\_base\_url() helper for global location support - [PR #18410](https://github.com/BerriAI/litellm/pull/18410)
  - Convert image URLs to base64 for Vertex AI Anthropic - [PR #18497](https://github.com/BerriAI/litellm/pull/18497)
  - Separate Tool objects for each tool type per API spec - [PR #18514](https://github.com/BerriAI/litellm/pull/18514)
  - Add thought\_signatures to VertexGeminiConfig - [PR #18853](https://github.com/BerriAI/litellm/pull/18853)
  - Add support for Vertex AI API keys - [PR #18806](https://github.com/BerriAI/litellm/pull/18806)
  - Add zai glm-4.7 model support - [PR #18782](https://github.com/BerriAI/litellm/pull/18782)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure/azure)
  
  - Add Azure gpt-image-1.5 pricing to cost map - [PR #18347](https://github.com/BerriAI/litellm/pull/18347)
  - Add azure/gpt-5.2-chat model - [PR #18361](https://github.com/BerriAI/litellm/pull/18361)
  - Add support for image generation via Azure AD token - [PR #18413](https://github.com/BerriAI/litellm/pull/18413)
  - Add logprobs support for Azure OpenAI GPT-5.2 model - [PR #18856](https://github.com/BerriAI/litellm/pull/18856)
  - Add Azure BFL Flux 2 models for image generation and editing - [PR #18764](https://github.com/BerriAI/litellm/pull/18764), [PR #18766](https://github.com/BerriAI/litellm/pull/18766)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add Bedrock Kimi K2 model support - [PR #18797](https://github.com/BerriAI/litellm/pull/18797)
  - Add support for model id in bedrock passthrough - [PR #18800](https://github.com/BerriAI/litellm/pull/18800)
  - Fix Nova model detection for Bedrock provider - [PR #18250](https://github.com/BerriAI/litellm/pull/18250)
  - Ensure toolUse.input is always a dict when converting from OpenAI format - [PR #18414](https://github.com/BerriAI/litellm/pull/18414)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks)
  
  - Add enhanced authentication, security features, and custom user-agent support - [PR #18349](https://github.com/BerriAI/litellm/pull/18349)
- [**MiniMax**](https://docs.litellm.ai/docs/providers/minimax)
  
  - Add MiniMax chat completion support - [PR #18380](https://github.com/BerriAI/litellm/pull/18380)
  - Add Anthropic native endpoint support for MiniMax - [PR #18377](https://github.com/BerriAI/litellm/pull/18377)
  - Add support for MiniMax TTS - [PR #18334](https://github.com/BerriAI/litellm/pull/18334)
  - Add MiniMax provider support to UI dashboard - [PR #18496](https://github.com/BerriAI/litellm/pull/18496)
- [**Together AI**](https://docs.litellm.ai/docs/providers/togetherai)
  
  - Add supports\_response\_schema to all supported Together AI models - [PR #18368](https://github.com/BerriAI/litellm/pull/18368)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Add OpenRouter embeddings API support - [PR #18391](https://github.com/BerriAI/litellm/pull/18391)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Pass server\_tool\_use and tool\_search\_tool\_result blocks - [PR #18770](https://github.com/BerriAI/litellm/pull/18770)
  - Add Anthropic cache control option to image tool call results - [PR #18674](https://github.com/BerriAI/litellm/pull/18674)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Add dimensions for ollama embedding - [PR #18536](https://github.com/BerriAI/litellm/pull/18536)
  - Extract pure base64 data from data URLs for Ollama - [PR #18465](https://github.com/BerriAI/litellm/pull/18465)
- [**Watsonx**](https://docs.litellm.ai/docs/providers/watsonx/index)
  
  - Add Watsonx fields support - [PR #18569](https://github.com/BerriAI/litellm/pull/18569)
  - Fix Watsonx Audio Transcription - filter model field - [PR #18810](https://github.com/BerriAI/litellm/pull/18810)
- [**SAP**](https://docs.litellm.ai/docs/providers/sap)
  
  - Add SAP creds for list in proxy UI - [PR #18375](https://github.com/BerriAI/litellm/pull/18375)
  - Pass through extra params from allowed\_openai\_params - [PR #18432](https://github.com/BerriAI/litellm/pull/18432)
  - Add client header for SAP AI Core Tracking - [PR #18714](https://github.com/BerriAI/litellm/pull/18714)
- [**Fireworks AI**](https://docs.litellm.ai/docs/providers/fireworks_ai)
  
  - Correct deepseek-v3p2 pricing - [PR #18483](https://github.com/BerriAI/litellm/pull/18483)
- [**ZAI**](https://docs.litellm.ai/docs/providers/zai)
  
  - Add GLM-4.7 model with reasoning support - [PR #18476](https://github.com/BerriAI/litellm/pull/18476)
- [**Codestral**](https://docs.litellm.ai/docs/providers/codestral)
  
  - Correctly route codestral chat and FIM endpoints - [PR #18467](https://github.com/BerriAI/litellm/pull/18467)
- [**Azure AI**](https://docs.litellm.ai/docs/providers/azure_ai)
  
  - Fix authentication errors at messages API via azure\_ai - [PR #18500](https://github.com/BerriAI/litellm/pull/18500)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**AWS Polly**](https://docs.litellm.ai/docs/providers/aws_polly) - Add AWS Polly API for TTS - [PR #18326](https://github.com/BerriAI/litellm/pull/18326)
- [**GigaChat**](https://docs.litellm.ai/docs/providers/gigachat) - Add GigaChat provider support - [PR #18564](https://github.com/BerriAI/litellm/pull/18564)
- [**LlamaGate**](https://docs.litellm.ai/docs/providers/llamagate) - Add LlamaGate as a new provider - [PR #18673](https://github.com/BerriAI/litellm/pull/18673)
- [**Abliteration AI**](https://docs.litellm.ai/docs/providers/abliteration) - Add abliteration.ai provider - [PR #18678](https://github.com/BerriAI/litellm/pull/18678)
- [**Manus**](https://docs.litellm.ai/docs/providers/manus) - Add Manus API support on /responses, GET /responses - [PR #18804](https://github.com/BerriAI/litellm/pull/18804)
- **5 AI Providers via openai\_like** - Add 5 AI providers using openai\_like - [PR #18362](https://github.com/BerriAI/litellm/pull/18362)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Properly catch context window exceeded errors - [PR #18283](https://github.com/BerriAI/litellm/pull/18283)
  - Remove prompt caching headers as support has been removed - [PR #18579](https://github.com/BerriAI/litellm/pull/18579)
  - Fix generate content request with audio file id - [PR #18745](https://github.com/BerriAI/litellm/pull/18745)
  - Fix google\_genai streaming adapter provider handling - [PR #18845](https://github.com/BerriAI/litellm/pull/18845)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Remove deprecated Groq models and update model registry - [PR #18062](https://github.com/BerriAI/litellm/pull/18062)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Handle unsupported region for Vertex AI count tokens endpoint - [PR #18665](https://github.com/BerriAI/litellm/pull/18665)
- **General**
  
  - Fix request body for image embedding request - [PR #18336](https://github.com/BerriAI/litellm/pull/18336)
  - Fix lost tool\_calls when streaming has both text and tool\_calls - [PR #18316](https://github.com/BerriAI/litellm/pull/18316)
  - Add all resolution for gpt-image-1.5 - [PR #18586](https://github.com/BerriAI/litellm/pull/18586)
  - Fix gpt-image-1 cost calculation using token-based pricing - [PR #17906](https://github.com/BerriAI/litellm/pull/17906)
  - Fix response\_format leaking into extra\_body - [PR #18859](https://github.com/BerriAI/litellm/pull/18859)
  - Align max\_tokens with max\_output\_tokens for consistency - [PR #18820](https://github.com/BerriAI/litellm/pull/18820)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Add new compact endpoint (v1/responses/compact) - [PR #18697](https://github.com/BerriAI/litellm/pull/18697)
  - Support more streaming callback hooks - [PR #18513](https://github.com/BerriAI/litellm/pull/18513)
  - Add mapping for reasoning effort to summary param - [PR #18635](https://github.com/BerriAI/litellm/pull/18635)
  - Add output\_text property to ResponsesAPIResponse - [PR #18491](https://github.com/BerriAI/litellm/pull/18491)
  - Add annotations to completions responses API bridge - [PR #18754](https://github.com/BerriAI/litellm/pull/18754)
- [**Interactions API**](https://docs.litellm.ai/docs/interactions)
  
  - Allow using all LiteLLM providers (interactions -&gt; responses API bridge) - [PR #18373](https://github.com/BerriAI/litellm/pull/18373)
- [**RAG Search API**](https://docs.litellm.ai/docs/search/index)
  
  - Add RAG Search/Query endpoint - [PR #18376](https://github.com/BerriAI/litellm/pull/18376)
- [**CountTokens API**](https://docs.litellm.ai/docs/anthropic_count_tokens)
  
  - Add Bedrock as a new provider for `/v1/messages/count_tokens` - [PR #18858](https://github.com/BerriAI/litellm/pull/18858)
- [**Generate Content**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add generate content in LLM route - [PR #18405](https://github.com/BerriAI/litellm/pull/18405)
- **General**
  
  - Enable async\_post\_call\_failure\_hook to transform error responses - [PR #18348](https://github.com/BerriAI/litellm/pull/18348)
  - Calculate total\_tokens manually if missing and can be calculated - [PR #18445](https://github.com/BerriAI/litellm/pull/18445)
  - Add custom llm provider to get\_llm\_provider when sent via UI - [PR #18638](https://github.com/BerriAI/litellm/pull/18638)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Handle empty error objects in response conversion - [PR #18493](https://github.com/BerriAI/litellm/pull/18493)
  - Preserve client error status codes in streaming mode - [PR #18698](https://github.com/BerriAI/litellm/pull/18698)
  - Return json error response instead of SSE format for initial streaming errors - [PR #18757](https://github.com/BerriAI/litellm/pull/18757)
  - Fix auth header for custom api base in generateContent request - [PR #18637](https://github.com/BerriAI/litellm/pull/18637)
  - Tool content should be string for Deepinfra - [PR #18739](https://github.com/BerriAI/litellm/pull/18739)
  - Fix incomplete usage in response object passed - [PR #18799](https://github.com/BerriAI/litellm/pull/18799)
  - Unify model names to provider-defined names - [PR #18573](https://github.com/BerriAI/litellm/pull/18573)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **SSO Configuration**
  
  - Add SSO Role Mapping feature - [PR #18090](https://github.com/BerriAI/litellm/pull/18090)
  - Add SSO Settings Page - [PR #18600](https://github.com/BerriAI/litellm/pull/18600)
  - Allow adding role mappings for SSO - [PR #18593](https://github.com/BerriAI/litellm/pull/18593)
  - SSO Settings Page Add Role Mappings - [PR #18677](https://github.com/BerriAI/litellm/pull/18677)
  - SSO Settings Loading State + Deprecate Previous SSO Flow - [PR #18617](https://github.com/BerriAI/litellm/pull/18617)
- **Virtual Keys**
  
  - Allow deleting key expiry - [PR #18278](https://github.com/BerriAI/litellm/pull/18278)
  - Add optional query param "expand" to /key/list - [PR #18502](https://github.com/BerriAI/litellm/pull/18502)
  - Key Table Loading Skeleton - [PR #18527](https://github.com/BerriAI/litellm/pull/18527)
  - Allow column resizing on Keys Table - [PR #18424](https://github.com/BerriAI/litellm/pull/18424)
  - Virtual Keys Table Loading State Between Pages - [PR #18619](https://github.com/BerriAI/litellm/pull/18619)
  - Key and Team Router Setting - [PR #18790](https://github.com/BerriAI/litellm/pull/18790)
  - Allow router\_settings on Keys and Teams - [PR #18675](https://github.com/BerriAI/litellm/pull/18675)
  - Use timedelta to calculate key expiry on generate - [PR #18666](https://github.com/BerriAI/litellm/pull/18666)
- **Models + Endpoints**
  
  - Add Model Clearer Flow For Team Admins - [PR #18532](https://github.com/BerriAI/litellm/pull/18532)
  - Model Page Loading State - [PR #18574](https://github.com/BerriAI/litellm/pull/18574)
  - Model Page Model Provider Select Performance - [PR #18425](https://github.com/BerriAI/litellm/pull/18425)
  - Model Page Sorting Sorts Entire Set - [PR #18420](https://github.com/BerriAI/litellm/pull/18420)
  - Refactor Model Hub Page - [PR #18568](https://github.com/BerriAI/litellm/pull/18568)
  - Add request provider form on UI - [PR #18704](https://github.com/BerriAI/litellm/pull/18704)
- **Organizations & Teams**
  
  - Allow Organization Admins to See Organization Tab - [PR #18400](https://github.com/BerriAI/litellm/pull/18400)
  - Resolve Organization Alias on Team Table - [PR #18401](https://github.com/BerriAI/litellm/pull/18401)
  - Resolve Team Alias in Organization Info View - [PR #18404](https://github.com/BerriAI/litellm/pull/18404)
  - Allow Organization Admins to View Their Organization Info - [PR #18417](https://github.com/BerriAI/litellm/pull/18417)
  - Allow editing team\_member\_budget\_duration in /team/update - [PR #18735](https://github.com/BerriAI/litellm/pull/18735)
  - Reusable Duration Select + Team Update Member Budget Duration - [PR #18736](https://github.com/BerriAI/litellm/pull/18736)
- **Usage & Spend**
  
  - Add Error Code Filtering on Spend Logs - [PR #18359](https://github.com/BerriAI/litellm/pull/18359)
  - Add Error Code Filtering on UI - [PR #18366](https://github.com/BerriAI/litellm/pull/18366)
  - Usage Page User Max Budget fix - [PR #18555](https://github.com/BerriAI/litellm/pull/18555)
  - Add endpoint to Daily Activity Tables - [PR #18729](https://github.com/BerriAI/litellm/pull/18729)
  - Endpoint Activity in Usage - [PR #18798](https://github.com/BerriAI/litellm/pull/18798)
- **Cost Estimator**
  
  - Add Cost Estimator for AI Gateway - [PR #18643](https://github.com/BerriAI/litellm/pull/18643)
  - Add view for estimating costs across requests - [PR #18645](https://github.com/BerriAI/litellm/pull/18645)
  - Allow selecting many models for cost estimator - [PR #18653](https://github.com/BerriAI/litellm/pull/18653)
- **CloudZero**
  
  - Improve Create and Delete Path for CloudZero - [PR #18263](https://github.com/BerriAI/litellm/pull/18263)
  - Add CloudZero UI Docs - [PR #18350](https://github.com/BerriAI/litellm/pull/18350)
- **Playground**
  
  - Add MCP test support to completions on Playground - [PR #18440](https://github.com/BerriAI/litellm/pull/18440)
  - Add selectable MCP servers to the playground - [PR #18578](https://github.com/BerriAI/litellm/pull/18578)
  - Add custom proxy base URL support to Playground - [PR #18661](https://github.com/BerriAI/litellm/pull/18661)
- **General UI**
  
  - UI styling improvements and fixes - [PR #18310](https://github.com/BerriAI/litellm/pull/18310)
  - Add reusable "New" badge component for feature highlights - [PR #18537](https://github.com/BerriAI/litellm/pull/18537)
  - Hide New Badges - [PR #18547](https://github.com/BerriAI/litellm/pull/18547)
  - Change Budget page to Have Tabs - [PR #18576](https://github.com/BerriAI/litellm/pull/18576)
  - Clicking on Logo Directs to Correct URL - [PR #18575](https://github.com/BerriAI/litellm/pull/18575)
  - Add UI support for configuring meta URLs - [PR #18580](https://github.com/BerriAI/litellm/pull/18580)
  - Expire Previous UI Session Tokens on Login - [PR #18557](https://github.com/BerriAI/litellm/pull/18557)
  - Add license endpoint - [PR #18311](https://github.com/BerriAI/litellm/pull/18311)
  - Router Fields Endpoint + React Query for Router Fields - [PR #18880](https://github.com/BerriAI/litellm/pull/18880)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **UI Fixes**
  
  - Fix Key Creation MCP Settings Submit Form Unintentionally - [PR #18355](https://github.com/BerriAI/litellm/pull/18355)
  - Fix UI Disappears in Development Environments - [PR #18399](https://github.com/BerriAI/litellm/pull/18399)
  - Fix Disable Admin UI Flag - [PR #18397](https://github.com/BerriAI/litellm/pull/18397)
  - Remove Model Analytics From Model Page - [PR #18552](https://github.com/BerriAI/litellm/pull/18552)
  - Useful Links Remove Modal on Adding Links - [PR #18602](https://github.com/BerriAI/litellm/pull/18602)
  - SSO Edit Modal Clear Role Mapping Values on Provider Change - [PR #18680](https://github.com/BerriAI/litellm/pull/18680)
  - UI Login Case Sensitivity fix - [PR #18877](https://github.com/BerriAI/litellm/pull/18877)
- **API Fixes**
  
  - Fix User Invite & Key Generation Email Notification Logic - [PR #18524](https://github.com/BerriAI/litellm/pull/18524)
  - Normalize Proxy Config Callback - [PR #18775](https://github.com/BerriAI/litellm/pull/18775)
  - Return empty data array instead of 500 when no models configured - [PR #18556](https://github.com/BerriAI/litellm/pull/18556)
  - Enforce org level max budget - [PR #18813](https://github.com/BerriAI/litellm/pull/18813)

* * *

## AI Integrations[​](#ai-integrations "Direct link to AI Integrations")

### New Integrations (4 new integrations)[​](#new-integrations-4-new-integrations "Direct link to New Integrations (4 new integrations)")

IntegrationTypeDescription[Focus](https://docs.litellm.ai/docs/observability/focus)LoggingFocus export support for observability - [PR #18802](https://github.com/BerriAI/litellm/pull/18802)[SigNoz](https://docs.litellm.ai/docs/observability/signoz)LoggingSigNoz integration for observability - [PR #18726](https://github.com/BerriAI/litellm/pull/18726)[Qualifire](https://docs.litellm.ai/docs/proxy/guardrails/qualifire)GuardrailsQualifire guardrails and eval webhook - [PR #18594](https://github.com/BerriAI/litellm/pull/18594)[Levo AI](https://docs.litellm.ai/docs/observability/levo_integration)GuardrailsLevo AI integration for security - [PR #18529](https://github.com/BerriAI/litellm/pull/18529)

### Logging[​](#logging "Direct link to Logging")

- [**DataDog**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Fix span kind fallback when parent\_id missing - [PR #18418](https://github.com/BerriAI/litellm/pull/18418)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Map Gemini cached\_tokens to Langfuse cache\_read\_input\_tokens - [PR #18614](https://github.com/BerriAI/litellm/pull/18614)
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/logging#prometheus)
  
  - Align prometheus metric names with DEFINED\_PROMETHEUS\_METRICS - [PR #18463](https://github.com/BerriAI/litellm/pull/18463)
  - Add Prometheus metrics for request queue time and guardrails - [PR #17973](https://github.com/BerriAI/litellm/pull/17973)
  - Add caching metrics for cache hits, misses, and tokens - [PR #18755](https://github.com/BerriAI/litellm/pull/18755)
  - Skip metrics for invalid API key requests - [PR #18788](https://github.com/BerriAI/litellm/pull/18788)
- [**Braintrust**](https://docs.litellm.ai/docs/proxy/logging#braintrust)
  
  - Pass span\_attributes in async logging and skip tags on non-root spans - [PR #18409](https://github.com/BerriAI/litellm/pull/18409)
- [**CloudZero**](https://docs.litellm.ai/docs/proxy/logging#cloudzero)
  
  - Add user email to CloudZero - [PR #18584](https://github.com/BerriAI/litellm/pull/18584)
- [**OpenTelemetry**](https://docs.litellm.ai/docs/proxy/logging#opentelemetry)
  
  - Use already configured opentelemetry providers - [PR #18279](https://github.com/BerriAI/litellm/pull/18279)
  - Prevent LiteLLM from closing external OTEL spans - [PR #18553](https://github.com/BerriAI/litellm/pull/18553)
  - Allow configuring arize project name for OpenTelemetry service name - [PR #18738](https://github.com/BerriAI/litellm/pull/18738)
- [**LangSmith**](https://docs.litellm.ai/docs/proxy/logging#langsmith)
  
  - Add support for LangSmith organization-scoped API keys with tenant ID - [PR #18623](https://github.com/BerriAI/litellm/pull/18623)
- [**Generic API Logger**](https://docs.litellm.ai/docs/proxy/logging#generic-api-logger)
  
  - Add log\_format option to GenericAPILogger - [PR #18587](https://github.com/BerriAI/litellm/pull/18587)

### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**Content Filter**](https://docs.litellm.ai/docs/proxy/guardrails/litellm_content_filter)
  
  - Add content filter logs page - [PR #18335](https://github.com/BerriAI/litellm/pull/18335)
  - Log actual event type for guardrails - [PR #18489](https://github.com/BerriAI/litellm/pull/18489)
- [**Qualifire**](https://docs.litellm.ai/docs/proxy/guardrails/qualifire)
  
  - Add Qualifire eval webhook - [PR #18836](https://github.com/BerriAI/litellm/pull/18836)
- [**Lasso Security**](https://docs.litellm.ai/docs/proxy/guardrails/lasso_security)
  
  - Add Lasso guardrail API docs - [PR #18652](https://github.com/BerriAI/litellm/pull/18652)
- [**Noma Security**](https://docs.litellm.ai/docs/proxy/guardrails/noma_security)
  
  - Add MCP guardrail support for Noma - [PR #18668](https://github.com/BerriAI/litellm/pull/18668)
- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/bedrock)
  
  - Remove redundant Bedrock guardrail block handling - [PR #18634](https://github.com/BerriAI/litellm/pull/18634)
- **General**
  
  - Generic guardrail API update - [PR #18647](https://github.com/BerriAI/litellm/pull/18647)
  - Prevent proxy startup failures from case-sensitive tool permission guardrail validation - [PR #18662](https://github.com/BerriAI/litellm/pull/18662)
  - Extend case normalization to ALL guardrail types - [PR #18664](https://github.com/BerriAI/litellm/pull/18664)
  - Fix MCP handling in unified guardrail - [PR #18630](https://github.com/BerriAI/litellm/pull/18630)
  - Fix embeddings calltype for guardrail precallhook - [PR #18740](https://github.com/BerriAI/litellm/pull/18740)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Platform Fee / Margins** - Add support for Platform Fee / Margins - [PR #18427](https://github.com/BerriAI/litellm/pull/18427)
- **Negative Budget Validation** - Add validation for negative budget - [PR #18583](https://github.com/BerriAI/litellm/pull/18583)
- **Cost Calculation Fixes**
  
  - Correct cost calculation when reasoning\_tokens are without text\_tokens - [PR #18607](https://github.com/BerriAI/litellm/pull/18607)
  - Fix background cost tracking tests - [PR #18588](https://github.com/BerriAI/litellm/pull/18588)
- **Tag Routing** - Support toggling tag matching between ANY and ALL - [PR #18776](https://github.com/BerriAI/litellm/pull/18776)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **MCP Global Mode** - Add MCP global mode - [PR #18639](https://github.com/BerriAI/litellm/pull/18639)
- **MCP Server Visibility** - Add configurable MCP server visibility - [PR #18681](https://github.com/BerriAI/litellm/pull/18681)
- **MCP Registry** - Add MCP registry - [PR #18850](https://github.com/BerriAI/litellm/pull/18850)
- **MCP Stdio Header** - Support MCP stdio header env overrides - [PR #18324](https://github.com/BerriAI/litellm/pull/18324)
- **Parallel Tool Fetching** - Parallelize tool fetching from multiple MCP servers - [PR #18627](https://github.com/BerriAI/litellm/pull/18627)
- **Optimize MCP Server Listing** - Separate health checks for optimized listing - [PR #18530](https://github.com/BerriAI/litellm/pull/18530)
- **Auth Improvements**
  
  - Require auth for MCP connection test endpoint - [PR #18290](https://github.com/BerriAI/litellm/pull/18290)
  - Fix MCP gateway OAuth2 auth issues and ClosedResourceError - [PR #18281](https://github.com/BerriAI/litellm/pull/18281)
- **Bug Fixes**
  
  - Fix MCP server health status reporting - [PR #18443](https://github.com/BerriAI/litellm/pull/18443)
  - Fix OpenAPI to MCP tool conversion - [PR #18597](https://github.com/BerriAI/litellm/pull/18597)
  - Remove exec() usage and handle invalid OpenAPI parameter names for security - [PR #18480](https://github.com/BerriAI/litellm/pull/18480)
  - Fix MCP error when using multiple servers simultaneously - [PR #18855](https://github.com/BerriAI/litellm/pull/18855)
- **Migrate MCP Fetching Logic to React Query** - [PR #18352](https://github.com/BerriAI/litellm/pull/18352)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **92.7% Faster Provider Config Lookup** - LiteLLM now stresses LLM providers 2.5x more - [PR #18867](https://github.com/BerriAI/litellm/pull/18867)
- **Lazy Loading Improvements**
  
  - Consolidate lazy import handlers with registry pattern - [PR #18389](https://github.com/BerriAI/litellm/pull/18389)
  - Complete lazy loading migration for all 180+ LLM config classes - [PR #18392](https://github.com/BerriAI/litellm/pull/18392)
  - Lazy load additional components (types, callbacks, utilities) - [PR #18396](https://github.com/BerriAI/litellm/pull/18396)
  - Add lazy loading for get\_llm\_provider - [PR #18591](https://github.com/BerriAI/litellm/pull/18591)
  - Lazy-load heavy audio library and loggers - [PR #18592](https://github.com/BerriAI/litellm/pull/18592)
  - Lazy load 9 heavy imports in litellm/utils.py - [PR #18595](https://github.com/BerriAI/litellm/pull/18595)
  - Lazy load heavy imports to improve import time and memory usage - [PR #18610](https://github.com/BerriAI/litellm/pull/18610)
  - Implement lazy loading for provider configs, model info classes, streaming handlers - [PR #18611](https://github.com/BerriAI/litellm/pull/18611)
  - Lazy load 15 additional imports - [PR #18613](https://github.com/BerriAI/litellm/pull/18613)
  - Lazy load 15+ unused imports - [PR #18616](https://github.com/BerriAI/litellm/pull/18616)
  - Lazy load DatadogLLMObsInitParams - [PR #18658](https://github.com/BerriAI/litellm/pull/18658)
  - Migrate utils.py lazy imports to registry pattern - [PR #18657](https://github.com/BerriAI/litellm/pull/18657)
  - Lazy load get\_llm\_provider and remove\_index\_from\_tool\_calls - [PR #18608](https://github.com/BerriAI/litellm/pull/18608)
- **Router Improvements**
  
  - Validate routing\_strategy at startup to fail fast with helpful error - [PR #18624](https://github.com/BerriAI/litellm/pull/18624)
  - Correct num\_retries tracking in retry logic - [PR #18712](https://github.com/BerriAI/litellm/pull/18712)
  - Improve error messages and validation for wildcard routing with multiple credentials - [PR #18629](https://github.com/BerriAI/litellm/pull/18629)
- **Memory Improvements**
  
  - Add memory pattern detection test and fix bad memory patterns - [PR #18589](https://github.com/BerriAI/litellm/pull/18589)
  - Add unbounded data structure detection to memory test - [PR #18590](https://github.com/BerriAI/litellm/pull/18590)
  - Add memory leak detection tests with CI integration - [PR #18881](https://github.com/BerriAI/litellm/pull/18881)
- **Database**
  
  - Add idx on LOWER(user\_email) for faster duplicate email checks - [PR #18828](https://github.com/BerriAI/litellm/pull/18828)
  - Proactive RDS IAM token refresh to prevent 15-min connection failed - [PR #18795](https://github.com/BerriAI/litellm/pull/18795)
  - Clarify database\_connection\_pool\_limit applies per worker - [PR #18780](https://github.com/BerriAI/litellm/pull/18780)
  - Make base\_connection\_pool\_limit default value the same - [PR #18721](https://github.com/BerriAI/litellm/pull/18721)
- **Docker**
  
  - Add libsndfile to database Docker image for audio processing - [PR #18612](https://github.com/BerriAI/litellm/pull/18612)
  - Add line\_profiler support for performance analysis and fix Windows CRLF issues - [PR #18773](https://github.com/BerriAI/litellm/pull/18773)
- **Helm**
  
  - Add lifecycle support to Helm charts - [PR #18517](https://github.com/BerriAI/litellm/pull/18517)
- **Authentication**
  
  - Add Kubernetes ServiceAccount JWT authentication support - [PR #18055](https://github.com/BerriAI/litellm/pull/18055)
  - Use async anthropic client to prevent event loop blocking - [PR #18435](https://github.com/BerriAI/litellm/pull/18435)
- **Logging Worker**
  
  - Handle event loop changes in multiprocessing - [PR #18423](https://github.com/BerriAI/litellm/pull/18423)
- **Security**
  
  - Prevent expired key plaintext leak in error response - [PR #18860](https://github.com/BerriAI/litellm/pull/18860)
  - Mask extra header secrets in model info - [PR #18822](https://github.com/BerriAI/litellm/pull/18822)
  - Prevent duplicate User-Agent tags in request\_tags - [PR #18723](https://github.com/BerriAI/litellm/pull/18723)
  - Properly use litellm api keys - [PR #18832](https://github.com/BerriAI/litellm/pull/18832)
- **Misc**
  
  - Remove double imports in main.py - [PR #18406](https://github.com/BerriAI/litellm/pull/18406)
  - Add LITELLM\_DISABLE\_LAZY\_LOADING env var to fix VCR cassette creation issue - [PR #18725](https://github.com/BerriAI/litellm/pull/18725)
  - Add xiaomi\_mimo to LlmProviders enum to fix router support - [PR #18819](https://github.com/BerriAI/litellm/pull/18819)
  - Allow installation with current grpcio on old Python - [PR #18473](https://github.com/BerriAI/litellm/pull/18473)
  - Add Custom CA certificates to boto3 clients - [PR #18852](https://github.com/BerriAI/litellm/pull/18852)
  - Fix bedrock\_cache, metadata and max\_model\_budget - [PR #18872](https://github.com/BerriAI/litellm/pull/18872)
  - Fix LiteLLM SDK embedding headers missing field - [PR #18844](https://github.com/BerriAI/litellm/pull/18844)
  - Put automatic reasoning summary inclusion behind feat flag - [PR #18688](https://github.com/BerriAI/litellm/pull/18688)
  - turn\_off\_message\_logging Does Not Redact Request Messages in proxy\_server\_request Field - [PR #18897](https://github.com/BerriAI/litellm/pull/18897)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Update MiniMax docs to be in proper format - [PR #18403](https://github.com/BerriAI/litellm/pull/18403)
  - Add docs for 5 AI providers - [PR #18388](https://github.com/BerriAI/litellm/pull/18388)
  - Fix gpt-5-mini reasoning\_effort supported values - [PR #18346](https://github.com/BerriAI/litellm/pull/18346)
  - Fix PDF documentation inconsistency in Anthropic page - [PR #18816](https://github.com/BerriAI/litellm/pull/18816)
  - Update OpenRouter docs to include embedding support - [PR #18874](https://github.com/BerriAI/litellm/pull/18874)
  - Add LITELLM\_REASONING\_AUTO\_SUMMARY in doc - [PR #18705](https://github.com/BerriAI/litellm/pull/18705)
- **MCP Documentation**
  
  - Agentcore MCP server docs - [PR #18603](https://github.com/BerriAI/litellm/pull/18603)
  - Mention MCP prompt/resources types in overview - [PR #18669](https://github.com/BerriAI/litellm/pull/18669)
  - Add Focus docs - [PR #18837](https://github.com/BerriAI/litellm/pull/18837)
- **Guardrails Documentation**
  
  - Qualifire docs hotfix - [PR #18724](https://github.com/BerriAI/litellm/pull/18724)
- **Infrastructure Documentation**
  
  - IAM Roles Anywhere docs - [PR #18559](https://github.com/BerriAI/litellm/pull/18559)
  - Fix formatting in proxy configs documentation - [PR #18498](https://github.com/BerriAI/litellm/pull/18498)
  - Fix GCS cache docs missing for proxy mode - [PR #13328](https://github.com/BerriAI/litellm/pull/13328)
  - Fix how to execute cloudzero sql - [PR #18841](https://github.com/BerriAI/litellm/pull/18841)
- **General**
  
  - LiteLLM adopters section - [PR #18605](https://github.com/BerriAI/litellm/pull/18605)
  - Remove redundant comments about setting litellm.callbacks - [PR #18711](https://github.com/BerriAI/litellm/pull/18711)
  - Update header to be markdown bold by removing space - [PR #18846](https://github.com/BerriAI/litellm/pull/18846)
  - Manus docs - new provider - [PR #18817](https://github.com/BerriAI/litellm/pull/18817)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @prasadkona made their first contribution in [PR #18349](https://github.com/BerriAI/litellm/pull/18349)
- @lucasrothman made their first contribution in [PR #18283](https://github.com/BerriAI/litellm/pull/18283)
- @aggeentik made their first contribution in [PR #18317](https://github.com/BerriAI/litellm/pull/18317)
- @mihidumh made their first contribution in [PR #18361](https://github.com/BerriAI/litellm/pull/18361)
- @Prazeina made their first contribution in [PR #18498](https://github.com/BerriAI/litellm/pull/18498)
- @systec-dk made their first contribution in [PR #18500](https://github.com/BerriAI/litellm/pull/18500)
- @xuan07t2 made their first contribution in [PR #18514](https://github.com/BerriAI/litellm/pull/18514)
- @RensDimmendaal made their first contribution in [PR #18190](https://github.com/BerriAI/litellm/pull/18190)
- @yurekami made their first contribution in [PR #18483](https://github.com/BerriAI/litellm/pull/18483)
- @agertz7 made their first contribution in [PR #18556](https://github.com/BerriAI/litellm/pull/18556)
- @yudelevi made their first contribution in [PR #18550](https://github.com/BerriAI/litellm/pull/18550)
- @smallp made their first contribution in [PR #18536](https://github.com/BerriAI/litellm/pull/18536)
- @kevinpauer made their first contribution in [PR #18569](https://github.com/BerriAI/litellm/pull/18569)
- @cansakiroglu made their first contribution in [PR #18517](https://github.com/BerriAI/litellm/pull/18517)
- @dee-walia20 made their first contribution in [PR #18432](https://github.com/BerriAI/litellm/pull/18432)
- @luxinfeng made their first contribution in [PR #18477](https://github.com/BerriAI/litellm/pull/18477)
- @cantalupo555 made their first contribution in [PR #18476](https://github.com/BerriAI/litellm/pull/18476)
- @andersk made their first contribution in [PR #18473](https://github.com/BerriAI/litellm/pull/18473)
- @majiayu000 made their first contribution in [PR #18467](https://github.com/BerriAI/litellm/pull/18467)
- @amangupta-20 made their first contribution in [PR #18529](https://github.com/BerriAI/litellm/pull/18529)
- @hamzaq453 made their first contribution in [PR #18480](https://github.com/BerriAI/litellm/pull/18480)
- @ktsaou made their first contribution in [PR #18627](https://github.com/BerriAI/litellm/pull/18627)
- @FlibbertyGibbitz made their first contribution in [PR #18624](https://github.com/BerriAI/litellm/pull/18624)
- @drorIvry made their first contribution in [PR #18594](https://github.com/BerriAI/litellm/pull/18594)
- @urainshah made their first contribution in [PR #18524](https://github.com/BerriAI/litellm/pull/18524)
- @mangabits made their first contribution in [PR #18279](https://github.com/BerriAI/litellm/pull/18279)
- @0717376 made their first contribution in [PR #18564](https://github.com/BerriAI/litellm/pull/18564)
- @nmgarza5 made their first contribution in [PR #17330](https://github.com/BerriAI/litellm/pull/17330)
- @wileykestner made their first contribution in [PR #18445](https://github.com/BerriAI/litellm/pull/18445)
- @minijeong-log made their first contribution in [PR #14440](https://github.com/BerriAI/litellm/pull/14440)
- @Isaac4real made their first contribution in [PR #18710](https://github.com/BerriAI/litellm/pull/18710)
- @marukaz made their first contribution in [PR #18711](https://github.com/BerriAI/litellm/pull/18711)
- @rohitravirane made their first contribution in [PR #18712](https://github.com/BerriAI/litellm/pull/18712)
- @lizzzcai made their first contribution in [PR #18714](https://github.com/BerriAI/litellm/pull/18714)
- @hkd987 made their first contribution in [PR #18673](https://github.com/BerriAI/litellm/pull/18673)
- @Mr-Pepe made their first contribution in [PR #18674](https://github.com/BerriAI/litellm/pull/18674)
- @gkarthi-signoz made their first contribution in [PR #18726](https://github.com/BerriAI/litellm/pull/18726)
- @Tianduo16 made their first contribution in [PR #18723](https://github.com/BerriAI/litellm/pull/18723)
- @wilsonjr made their first contribution in [PR #18721](https://github.com/BerriAI/litellm/pull/18721)
- @abliteration-ai made their first contribution in [PR #18678](https://github.com/BerriAI/litellm/pull/18678)
- @danialkhan02 made their first contribution in [PR #18770](https://github.com/BerriAI/litellm/pull/18770)
- @ihower made their first contribution in [PR #18409](https://github.com/BerriAI/litellm/pull/18409)
- @elkkhan made their first contribution in [PR #18391](https://github.com/BerriAI/litellm/pull/18391)
- @runixer made their first contribution in [PR #18435](https://github.com/BerriAI/litellm/pull/18435)
- @choby-shun made their first contribution in [PR #18776](https://github.com/BerriAI/litellm/pull/18776)
- @jutaz made their first contribution in [PR #18853](https://github.com/BerriAI/litellm/pull/18853)
- @sjmatta made their first contribution in [PR #18250](https://github.com/BerriAI/litellm/pull/18250)
- @andres-ortizl made their first contribution in [PR #18856](https://github.com/BerriAI/litellm/pull/18856)
- @gauthiermartin made their first contribution in [PR #18844](https://github.com/BerriAI/litellm/pull/18844)
- @mel2oo made their first contribution in [PR #18845](https://github.com/BerriAI/litellm/pull/18845)
- @DominikHallab made their first contribution in [PR #18846](https://github.com/BerriAI/litellm/pull/18846)
- @ji-chuan-che made their first contribution in [PR #18540](https://github.com/BerriAI/litellm/pull/18540)
- @raghav-stripe made their first contribution in [PR #18858](https://github.com/BerriAI/litellm/pull/18858)
- @akraines made their first contribution in [PR #18629](https://github.com/BerriAI/litellm/pull/18629)
- @otaviofbrito made their first contribution in [PR #18665](https://github.com/BerriAI/litellm/pull/18665)
- @chetanchoudhary-sumo made their first contribution in [PR #18587](https://github.com/BerriAI/litellm/pull/18587)
- @pascalwhoop made their first contribution in [PR #13328](https://github.com/BerriAI/litellm/pull/13328)
- @orgersh92 made their first contribution in [PR #18652](https://github.com/BerriAI/litellm/pull/18652)
- @DevajMody made their first contribution in [PR #18497](https://github.com/BerriAI/litellm/pull/18497)
- @matt-greathouse made their first contribution in [PR #18247](https://github.com/BerriAI/litellm/pull/18247)
- @emerzon made their first contribution in [PR #18290](https://github.com/BerriAI/litellm/pull/18290)
- @Eric84626 made their first contribution in [PR #18281](https://github.com/BerriAI/litellm/pull/18281)
- @LukasdeBoer made their first contribution in [PR #18055](https://github.com/BerriAI/litellm/pull/18055)
- @LingXuanYin made their first contribution in [PR #18513](https://github.com/BerriAI/litellm/pull/18513)
- @krisxia0506 made their first contribution in [PR #18698](https://github.com/BerriAI/litellm/pull/18698)
- @LouisShark made their first contribution in [PR #18414](https://github.com/BerriAI/litellm/pull/18414)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.80.11.rc.1...v1.80.15-stable.1)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.80.11-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Gemini 3 Flash Preview** - [Day 0 support for Google's Gemini 3 Flash Preview with reasoning capabilities](https://docs.litellm.ai/docs/providers/gemini)
- **Stability AI Image Generation** - [New provider for Stability AI image generation and editing](https://docs.litellm.ai/docs/providers/stability)
- **LiteLLM Content Filter** - [Built-in guardrails for harmful content, bias, and PII detection with image support](https://docs.litellm.ai/docs/proxy/guardrails/litellm_content_filter)
- **New Provider: Venice.ai** - Support for Venice.ai API via providers.json
- **Unified Skills API** - [Skills API works across Anthropic, Vertex, Azure, and Bedrock](https://docs.litellm.ai/docs/skills)
- **Azure Sentinel Logging** - [New logging integration for Azure Sentinel](https://docs.litellm.ai/docs/observability/azure_sentinel)
- **Guardrails Load Balancing** - [Load balance between multiple guardrail providers](https://docs.litellm.ai/docs/proxy/guardrails)
- **Email Budget Alerts** - [Send email notifications when budgets are reached](https://docs.litellm.ai/docs/proxy/email)
- **Cloudzero Integration on UI** - Setup your Cloudzero Integration Directly on the UI

* * *

### Cloudzero Integration on UI[​](#cloudzero-integration-on-ui "Direct link to Cloudzero Integration on UI")

Users can now configure their Cloudzero Integration directly on the UI.

* * *

### Performance: 50% Reduction in Memory Usage and Import Latency for the LiteLLM SDK[​](#performance-50-reduction-in-memory-usage-and-import-latency-for-the-litellm-sdk "Direct link to Performance: 50% Reduction in Memory Usage and Import Latency for the LiteLLM SDK")

We've completely restructured `litellm.__init__.py` to defer heavy imports until they're actually needed, implementing lazy loading for **109 components**.

This refactoring includes **41 provider config classes**, **40 utility functions**, cache implementations (Redis, DualCache, InMemoryCache), HTTP handlers, logging, types, and other heavy dependencies. Heavy libraries like tiktoken and boto3 are now loaded on-demand rather than eagerly at import time.

This makes LiteLLM especially beneficial for serverless functions, Lambda deployments, and containerized environments where cold start times and memory footprint matter.

* * *

## New Providers and Endpoints[​](#new-providers-and-endpoints "Direct link to New Providers and Endpoints")

### New Providers (5 new providers)[​](#new-providers-5-new-providers "Direct link to New Providers (5 new providers)")

ProviderSupported LiteLLM EndpointsDescription[Stability AI](https://docs.litellm.ai/docs/providers/stability)`/images/generations`, `/images/edits`Stable Diffusion 3, SD3.5, image editing and generationVenice.ai`/chat/completions`, `/messages`, `/responses`Venice.ai API integration via providers.json[Pydantic AI Agents](https://docs.litellm.ai/docs/providers/pydantic_ai_agent)`/a2a`Pydantic AI agents for A2A protocol workflows[VertexAI Agent Engine](https://docs.litellm.ai/docs/providers/vertex_ai_agent_engine)`/a2a`Google Vertex AI Agent Engine for agentic workflows[LinkUp Search](https://docs.litellm.ai/docs/search/linkup)`/search`LinkUp web search API integration

### New LLM API Endpoints (2 new endpoints)[​](#new-llm-api-endpoints-2-new-endpoints "Direct link to New LLM API Endpoints (2 new endpoints)")

EndpointMethodDescriptionDocumentation`/interactions`POSTGoogle Interactions API for conversational AI[Docs](https://docs.litellm.ai/docs/interactions)`/search`POSTRAG Search API with rerankers[Docs](https://docs.litellm.ai/docs/search/index)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support (55+ new models)[​](#new-model-support-55-new-models "Direct link to New Model Support (55+ new models)")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesGemini`gemini/gemini-3-flash-preview`1M$0.50$3.00Reasoning, vision, audio, video, PDFVertex AI`vertex_ai/gemini-3-flash-preview`1M$0.50$3.00Reasoning, vision, audio, video, PDFAzure AI`azure_ai/deepseek-v3.2`164K$0.58$1.68Reasoning, function calling, cachingAzure AI`azure_ai/cohere-rerank-v4.0-pro`32K$0.0025/query-RerankAzure AI`azure_ai/cohere-rerank-v4.0-fast`32K$0.002/query-RerankOpenRouter`openrouter/openai/gpt-5.2`400K$1.75$14.00Reasoning, vision, cachingOpenRouter`openrouter/openai/gpt-5.2-pro`400K$21.00$168.00Reasoning, visionOpenRouter`openrouter/mistralai/devstral-2512`262K$0.15$0.60Function callingOpenRouter`openrouter/mistralai/ministral-3b-2512`131K$0.10$0.10Function calling, visionOpenRouter`openrouter/mistralai/ministral-8b-2512`262K$0.15$0.15Function calling, visionOpenRouter`openrouter/mistralai/ministral-14b-2512`262K$0.20$0.20Function calling, visionOpenRouter`openrouter/mistralai/mistral-large-2512`262K$0.50$1.50Function calling, visionOpenAI`gpt-4o-transcribe-diarize`16K$6.00/audio-Audio transcription with diarizationOpenAI`gpt-image-1.5-2025-12-16`-VariousVariousImage generationStability`stability/sd3-large`--$0.065/imageImage generationStability`stability/sd3.5-large`--$0.065/imageImage generationStability`stability/stable-image-ultra`--$0.08/imageImage generationStability`stability/inpaint`--$0.005/imageImage editingStability`stability/outpaint`--$0.004/imageImage editingBedrock`stability.stable-conservative-upscale-v1:0`--$0.40/imageImage upscalingBedrock`stability.stable-creative-upscale-v1:0`--$0.60/imageImage upscalingVertex AI`vertex_ai/deepseek-ai/deepseek-ocr-maas`-$0.30$1.20OCRLinkUp`linkup/search`-$5.87/1K queries-Web searchLinkUp`linkup/search-deep`-$58.67/1K queries-Deep web searchGitHub Copilot20+ modelsVarious--Chat completions

#### Features[​](#features "Direct link to Features")

- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add Gemini 3 Flash Preview day 0 support with reasoning - [PR #18135](https://github.com/BerriAI/litellm/pull/18135)
  - Support extra\_headers in batch embeddings - [PR #18004](https://github.com/BerriAI/litellm/pull/18004)
  - Propagate token usage when generating images - [PR #17987](https://github.com/BerriAI/litellm/pull/17987)
  - Use JSON instead of form-data for image edit requests - [PR #18012](https://github.com/BerriAI/litellm/pull/18012)
  - Fix web search requests count - [PR #17921](https://github.com/BerriAI/litellm/pull/17921)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Use dynamic max\_tokens based on model - [PR #17900](https://github.com/BerriAI/litellm/pull/17900)
  - Fix claude-3-7-sonnet max\_tokens to 64K default - [PR #17979](https://github.com/BerriAI/litellm/pull/17979)
  - Add OpenAI-compatible API with modify\_params=True - [PR #17106](https://github.com/BerriAI/litellm/pull/17106)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add Gemini 3 Flash Preview support - [PR #18164](https://github.com/BerriAI/litellm/pull/18164)
  - Add reasoning support for gemini-3-flash-preview - [PR #18175](https://github.com/BerriAI/litellm/pull/18175)
  - Fix image edit credential source - [PR #18121](https://github.com/BerriAI/litellm/pull/18121)
  - Pass credentials to PredictionServiceClient for custom endpoints - [PR #17757](https://github.com/BerriAI/litellm/pull/17757)
  - Fix multimodal embeddings for text + base64 image combinations - [PR #18172](https://github.com/BerriAI/litellm/pull/18172)
  - Add OCR support for DeepSeek model - [PR #17971](https://github.com/BerriAI/litellm/pull/17971)
- [**Azure AI**](https://docs.litellm.ai/docs/providers/azure_ai)
  
  - Add Azure Cohere 4 reranking models - [PR #17961](https://github.com/BerriAI/litellm/pull/17961)
  - Add Azure DeepSeek V3.2 versions - [PR #18019](https://github.com/BerriAI/litellm/pull/18019)
  - Return AzureAnthropicConfig for Claude models in get\_provider\_chat\_config - [PR #18086](https://github.com/BerriAI/litellm/pull/18086)
- [**Fireworks AI**](https://docs.litellm.ai/docs/providers/fireworks_ai)
  
  - Add reasoning param support for Fireworks AI models - [PR #17967](https://github.com/BerriAI/litellm/pull/17967)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add Qwen 2 and Qwen 3 to get\_bedrock\_model\_id - [PR #18100](https://github.com/BerriAI/litellm/pull/18100)
  - Remove ttl field when routing to bedrock - [PR #18049](https://github.com/BerriAI/litellm/pull/18049)
  - Add Bedrock Stability image edit models - [PR #18254](https://github.com/BerriAI/litellm/pull/18254)
- [**Perplexity**](https://docs.litellm.ai/docs/providers/perplexity)
  
  - Use API-provided cost instead of manual calculation - [PR #17887](https://github.com/BerriAI/litellm/pull/17887)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Add diarize model for audio transcription - [PR #18117](https://github.com/BerriAI/litellm/pull/18117)
  - Add gpt-image-1.5-2025-12-16 in model cost map - [PR #18107](https://github.com/BerriAI/litellm/pull/18107)
  - Fix cost calculation of gpt-image-1 model - [PR #17966](https://github.com/BerriAI/litellm/pull/17966)
- [**GitHub Copilot**](https://docs.litellm.ai/docs/providers/github_copilot)
  
  - Add github\_copilot model info - [PR #17858](https://github.com/BerriAI/litellm/pull/17858)
- [**Custom LLM**](https://docs.litellm.ai/docs/providers/custom_llm_server)
  
  - Add image\_edit and aimage\_edit support - [PR #17999](https://github.com/BerriAI/litellm/pull/17999)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix pricing for Gemini 3 Flash on Vertex AI - [PR #18202](https://github.com/BerriAI/litellm/pull/18202)
  - Add output\_cost\_per\_image\_token for gemini-2.5-flash-image models - [PR #18156](https://github.com/BerriAI/litellm/pull/18156)
  - Fix properties should be non-empty for OBJECT type - [PR #18237](https://github.com/BerriAI/litellm/pull/18237)
- [**Qwen**](https://docs.litellm.ai/docs/providers/fireworks_ai)
  
  - Add qwen3-embedding-8b input per token price - [PR #18018](https://github.com/BerriAI/litellm/pull/18018)
- **General**
  
  - Fix image URL handling - [PR #18139](https://github.com/BerriAI/litellm/pull/18139)
  - Support Signed URLs with Query Parameters in Image Processing - [PR #17976](https://github.com/BerriAI/litellm/pull/17976)
  - Add none to encoding\_format instead of omitting it - [PR #18042](https://github.com/BerriAI/litellm/pull/18042)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Add provider specific tools support - [PR #17980](https://github.com/BerriAI/litellm/pull/17980)
  - Add custom headers support - [PR #18036](https://github.com/BerriAI/litellm/pull/18036)
  - Fix tool calls transformation in completion bridge - [PR #18226](https://github.com/BerriAI/litellm/pull/18226)
  - Use list format with input\_text for tool results - [PR #18257](https://github.com/BerriAI/litellm/pull/18257)
  - Add cost tracking in background mode - [PR #18236](https://github.com/BerriAI/litellm/pull/18236)
  - Fix Claude code responses API bridge errors - [PR #18194](https://github.com/BerriAI/litellm/pull/18194)
- [**Chat Completions API**](https://docs.litellm.ai/docs/completion/input)
  
  - Add support for agent skills - [PR #18031](https://github.com/BerriAI/litellm/pull/18031)
- [**Skills API**](https://docs.litellm.ai/docs/skills)
  
  - Unified Skills API works across Anthropic, Vertex, Azure, Bedrock - [PR #18232](https://github.com/BerriAI/litellm/pull/18232)
- [**Search API**](https://docs.litellm.ai/docs/search/index)
  
  - Add new RAG Search API with rerankers - [PR #18217](https://github.com/BerriAI/litellm/pull/18217)
- [**Interactions API**](https://docs.litellm.ai/docs/interactions)
  
  - Add Google Interactions API on SDK and AI Gateway - [PR #18079](https://github.com/BerriAI/litellm/pull/18079), [PR #18081](https://github.com/BerriAI/litellm/pull/18081)
- [**Image Edit API**](https://docs.litellm.ai/docs/image_edits)
  
  - Add drop\_params support and fix Vertex AI config - [PR #18077](https://github.com/BerriAI/litellm/pull/18077)
- **General**
  
  - Skip adding beta headers for Vertex AI as it is not supported - [PR #18037](https://github.com/BerriAI/litellm/pull/18037)
  - Fix managed files endpoint - [PR #18046](https://github.com/BerriAI/litellm/pull/18046)
  - Allow base\_model for non-Azure providers in proxy - [PR #18038](https://github.com/BerriAI/litellm/pull/18038)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Fix basemodel import in guardrail translation - [PR #17977](https://github.com/BerriAI/litellm/pull/17977)
  - Fix No module named 'fastapi' error - [PR #18239](https://github.com/BerriAI/litellm/pull/18239)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Virtual Keys**
  
  - Add master key rotation for credentials table - [PR #17952](https://github.com/BerriAI/litellm/pull/17952)
  - Fix tag management to preserve encrypted fields in litellm\_params - [PR #17484](https://github.com/BerriAI/litellm/pull/17484)
  - Fix key delete and regenerate permissions - [PR #18214](https://github.com/BerriAI/litellm/pull/18214)
- **Models + Endpoints**
  
  - Add Models Conditional Rendering in UI - [PR #18071](https://github.com/BerriAI/litellm/pull/18071)
  - Add Health Check Model for Wildcard Model in UI - [PR #18269](https://github.com/BerriAI/litellm/pull/18269)
  - Auto Resolve Vector Store Embedding Model Config - [PR #18167](https://github.com/BerriAI/litellm/pull/18167)
- **Vector Stores**
  
  - Add Milvus Vector Store UI support - [PR #18030](https://github.com/BerriAI/litellm/pull/18030)
  - Persist Vector Store Settings in Team Update - [PR #18274](https://github.com/BerriAI/litellm/pull/18274)
- **Logs & Spend**
  
  - Add LiteLLM Overhead to Logs - [PR #18033](https://github.com/BerriAI/litellm/pull/18033)
  - Show LiteLLM Overhead in Logs UI - [PR #18034](https://github.com/BerriAI/litellm/pull/18034)
  - Resolve Team ID to Team Alias in Usage Page - [PR #18275](https://github.com/BerriAI/litellm/pull/18275)
  - Fix Usage Page Top Key View Button Visibility - [PR #18203](https://github.com/BerriAI/litellm/pull/18203)
- **SSO & Health**
  
  - Add SSO Readiness Health Check - [PR #18078](https://github.com/BerriAI/litellm/pull/18078)
  - Fix /health/test\_connection to resolve env variables like /chat/completions - [PR #17752](https://github.com/BerriAI/litellm/pull/17752)
- **CloudZero**
  
  - Add CloudZero Cost Tracking UI - [PR #18163](https://github.com/BerriAI/litellm/pull/18163)
  - Add Delete CloudZero Settings Route and UI - [PR #18168](https://github.com/BerriAI/litellm/pull/18168), [PR #18170](https://github.com/BerriAI/litellm/pull/18170)
- **General**
  
  - Update UI path handling for non-root Docker - [PR #17989](https://github.com/BerriAI/litellm/pull/17989)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **UI Fixes**
  
  - Fix Login Page Failed To Parse JSON Error - [PR #18159](https://github.com/BerriAI/litellm/pull/18159)
  - Fix new user route user\_id collision handling - [PR #17559](https://github.com/BerriAI/litellm/pull/17559)
  - Fix Callback Environment Variables Casing - [PR #17912](https://github.com/BerriAI/litellm/pull/17912)

* * *

## AI Integrations[​](#ai-integrations "Direct link to AI Integrations")

### Logging[​](#logging "Direct link to Logging")

- [**Azure Sentinel**](https://docs.litellm.ai/docs/observability/azure_sentinel)
  
  - Add new Azure Sentinel Logger integration - [PR #18146](https://github.com/BerriAI/litellm/pull/18146)
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/logging#prometheus)
  
  - Add extraction of top level metadata for custom labels - [PR #18087](https://github.com/BerriAI/litellm/pull/18087)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Fix not working log\_failure\_event - [PR #18234](https://github.com/BerriAI/litellm/pull/18234)
- [**Arize Phoenix**](https://docs.litellm.ai/docs/observability/phoenix_integration)
  
  - Fix nested spans - [PR #18102](https://github.com/BerriAI/litellm/pull/18102)
- **General**
  
  - Change extra\_headers to additional\_headers - [PR #17950](https://github.com/BerriAI/litellm/pull/17950)

### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**LiteLLM Content Filter**](https://docs.litellm.ai/docs/proxy/guardrails/litellm_content_filter)
  
  - Add built-in guardrails for harmful content, bias, etc. - [PR #18029](https://github.com/BerriAI/litellm/pull/18029)
  - Add support for running content filters on images - [PR #18044](https://github.com/BerriAI/litellm/pull/18044)
  - Add support for Brazil PII field - [PR #18076](https://github.com/BerriAI/litellm/pull/18076)
  - Add configurable guardrail options for content filtering - [PR #18007](https://github.com/BerriAI/litellm/pull/18007)
- [**Guardrails API**](https://docs.litellm.ai/docs/adding_provider/generic_guardrail_api)
  
  - Support LLM tool call response checks on `/chat/completions`, `/v1/responses`, `/v1/messages` - [PR #17619](https://github.com/BerriAI/litellm/pull/17619)
  - Add guardrails load balancing - [PR #18181](https://github.com/BerriAI/litellm/pull/18181)
  - Fix guardrails for passthrough endpoint - [PR #18109](https://github.com/BerriAI/litellm/pull/18109)
  - Add headers to metadata for guardrails on pass-through endpoints - [PR #17992](https://github.com/BerriAI/litellm/pull/17992)
  - Various fixes for guardrail on OpenRouter models - [PR #18085](https://github.com/BerriAI/litellm/pull/18085)
- [**Lakera**](https://docs.litellm.ai/docs/proxy/guardrails/lakera_ai)
  
  - Add monitor mode for Lakera - [PR #18084](https://github.com/BerriAI/litellm/pull/18084)
- [**Pillar Security**](https://docs.litellm.ai/docs/proxy/guardrails/pillar_security)
  
  - Add masking support and MCP call support - [PR #17959](https://github.com/BerriAI/litellm/pull/17959)
- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/bedrock)
  
  - Add support for Bedrock image guardrails - [PR #18115](https://github.com/BerriAI/litellm/pull/18115)
  - Guardrails block action takes precedence over masking - [PR #17968](https://github.com/BerriAI/litellm/pull/17968)

### Secret Managers[​](#secret-managers "Direct link to Secret Managers")

- [**HashiCorp Vault**](https://docs.litellm.ai/docs/secret_managers/hashicorp_vault)
  
  - Add documentation for configurable Vault mount - [PR #18082](https://github.com/BerriAI/litellm/pull/18082)
  - Add per-team Vault configuration - [PR #18150](https://github.com/BerriAI/litellm/pull/18150)
- **UI**
  
  - Add secret manager settings controls to team management UI - [PR #18149](https://github.com/BerriAI/litellm/pull/18149)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Email Budget Alerts** - Send email notifications when budgets are reached - [PR #17995](https://github.com/BerriAI/litellm/pull/17995)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **Auth Header Propagation** - Add MCP auth header propagation - [PR #17963](https://github.com/BerriAI/litellm/pull/17963)
- **Fix deepcopy error** - Fix MCP tool call deepcopy error when processing requests - [PR #18010](https://github.com/BerriAI/litellm/pull/18010)
- **Fix list tool** - Fix MCP list\_tools not working without database connection - [PR #18161](https://github.com/BerriAI/litellm/pull/18161)

* * *

## Agent Gateway (A2A)[​](#agent-gateway-a2a "Direct link to Agent Gateway (A2A)")

- **New Provider: Agent Gateway** - Add pydantic ai agents support - [PR #18013](https://github.com/BerriAI/litellm/pull/18013)
- **VertexAI Agent Engine** - Add Vertex AI Agent Engine provider - [PR #18014](https://github.com/BerriAI/litellm/pull/18014)
- **Fix model extraction** - Fix get\_model\_from\_request() to extract model ID from Vertex AI passthrough URLs - [PR #18097](https://github.com/BerriAI/litellm/pull/18097)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Lazy Imports** - Use per-attribute lazy imports and extract shared constants - [PR #17994](https://github.com/BerriAI/litellm/pull/17994)
- **Lazy Load HTTP Handlers** - Lazy load http handlers - [PR #17997](https://github.com/BerriAI/litellm/pull/17997)
- **Lazy Load Caches** - Lazy load caches - [PR #18001](https://github.com/BerriAI/litellm/pull/18001)
- **Lazy Load Types** - Lazy load bedrock types, .types.utils, GuardrailItem - [PR #18053](https://github.com/BerriAI/litellm/pull/18053), [PR #18054](https://github.com/BerriAI/litellm/pull/18054), [PR #18072](https://github.com/BerriAI/litellm/pull/18072)
- **Lazy Load Configs** - Lazy load 41 configuration classes - [PR #18267](https://github.com/BerriAI/litellm/pull/18267)
- **Lazy Load Client Decorators** - Lazy load heavy client decorator imports - [PR #18064](https://github.com/BerriAI/litellm/pull/18064)
- **Prisma Build Time** - Download Prisma binaries at build time instead of runtime for security restricted environments - [PR #17695](https://github.com/BerriAI/litellm/pull/17695)
- **Docker Alpine** - Add libsndfile to Alpine image for ARM64 audio processing - [PR #18092](https://github.com/BerriAI/litellm/pull/18092)
- **Security** - Prevent LiteLLM API key leakage on /health endpoint failures - [PR #18133](https://github.com/BerriAI/litellm/pull/18133)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **SAP Docs** - Update SAP documentation - [PR #17974](https://github.com/BerriAI/litellm/pull/17974)
- **Pydantic AI Agents** - Add docs on using pydantic ai agents with LiteLLM A2A gateway - [PR #18026](https://github.com/BerriAI/litellm/pull/18026)
- **Vertex AI Agent Engine** - Add Vertex AI Agent Engine documentation - [PR #18027](https://github.com/BerriAI/litellm/pull/18027)
- **Router Order** - Add router order parameter documentation - [PR #18045](https://github.com/BerriAI/litellm/pull/18045)
- **Secret Manager Settings** - Improve secret manager settings documentation - [PR #18235](https://github.com/BerriAI/litellm/pull/18235)
- **Gemini 3 Flash** - Add version requirement in Gemini 3 Flash blog - [PR #18227](https://github.com/BerriAI/litellm/pull/18227)
- **README** - Expand Responses API section and update endpoints - [PR #17354](https://github.com/BerriAI/litellm/pull/17354)
- **Amazon Nova** - Add Amazon Nova to sidebar and supported models - [PR #18220](https://github.com/BerriAI/litellm/pull/18220)
- **Benchmarks** - Add infrastructure recommendations to benchmarks documentation - [PR #18264](https://github.com/BerriAI/litellm/pull/18264)
- **Broken Links** - Fix broken link corrections - [PR #18104](https://github.com/BerriAI/litellm/pull/18104)
- **README Fixes** - Various README improvements - [PR #18206](https://github.com/BerriAI/litellm/pull/18206)

* * *

## Infrastructure / CI/CD[​](#infrastructure--cicd "Direct link to Infrastructure / CI/CD")

- **PR Templates** - Add LiteLLM team PR template and CI/CD rules - [PR #17983](https://github.com/BerriAI/litellm/pull/17983), [PR #17985](https://github.com/BerriAI/litellm/pull/17985)
- **Issue Labeling** - Improve issue labeling with component dropdown and more provider keywords - [PR #17957](https://github.com/BerriAI/litellm/pull/17957)
- **PR Template Cleanup** - Remove redundant fields from PR template - [PR #17956](https://github.com/BerriAI/litellm/pull/17956)
- **Dependencies** - Bump altcha-lib from 1.3.0 to 1.4.1 - [PR #18017](https://github.com/BerriAI/litellm/pull/18017)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @dongbin-lunark made their first contribution in [PR #17757](https://github.com/BerriAI/litellm/pull/17757)
- @qdrddr made their first contribution in [PR #18004](https://github.com/BerriAI/litellm/pull/18004)
- @donicrosby made their first contribution in [PR #17962](https://github.com/BerriAI/litellm/pull/17962)
- @NicolaivdSmagt made their first contribution in [PR #17992](https://github.com/BerriAI/litellm/pull/17992)
- @Reapor-Yurnero made their first contribution in [PR #18085](https://github.com/BerriAI/litellm/pull/18085)
- @jk-f5 made their first contribution in [PR #18086](https://github.com/BerriAI/litellm/pull/18086)
- @castrapel made their first contribution in [PR #18077](https://github.com/BerriAI/litellm/pull/18077)
- @dtikhonov made their first contribution in [PR #17484](https://github.com/BerriAI/litellm/pull/17484)
- @opleonnn made their first contribution in [PR #18175](https://github.com/BerriAI/litellm/pull/18175)
- @eurogig made their first contribution in [PR #18084](https://github.com/BerriAI/litellm/pull/18084)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.80.10-nightly...v1.80.11)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.80.10.rc.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Agent (A2A) Gateway with Cost Tracking** - [Track agent costs per query, per token pricing, and view agent usage in the dashboard](https://docs.litellm.ai/docs/a2a_cost_tracking)
- **2 New Agent Providers** - [LangGraph Agents](https://docs.litellm.ai/docs/providers/langgraph) and [Azure AI Foundry Agents](https://docs.litellm.ai/docs/providers/azure_ai_agents) for agentic workflows
- **New Provider: SAP Gen AI Hub** - [Full support for SAP Generative AI Hub with chat completions](https://docs.litellm.ai/docs/providers/sap)
- **New Bedrock Writer Models** - Add Palmyra-X4 and Palmyra-X5 models on Bedrock
- **OpenAI GPT-5.2 Models** - Full support for GPT-5.2, GPT-5.2-pro, and Azure GPT-5.2 models with reasoning support
- **227 New Fireworks AI Models** - Comprehensive model coverage for Fireworks AI platform
- **MCP Support on /chat/completions** - [Use MCP servers directly via chat completions endpoint](https://docs.litellm.ai/docs/mcp)
- **Performance Improvements** - Reduced memory leaks by 50%

* * *

### Agent Gateway - 4 New Agent Providers[​](#agent-gateway---4-new-agent-providers "Direct link to Agent Gateway - 4 New Agent Providers")

This release adds support for agents from the following providers:

- **LangGraph Agents** - Deploy and manage LangGraph-based agents
- **Azure AI Foundry Agents** - Enterprise agent deployments on Azure
- **Bedrock AgentCore** - AWS Bedrock agent integration
- **A2A Agents** - Agent-to-Agent protocol support

AI Gateway admins can now add agents from any of these providers, and developers can invoke them through a unified interface using the A2A protocol.

For all agent requests running through the AI Gateway, LiteLLM automatically tracks request/response logs, cost, and token usage.

### Agent (A2A) Usage UI[​](#agent-a2a-usage-ui "Direct link to Agent (A2A) Usage UI")

Users can now filter usage statistics by agents, providing the same granular filtering capabilities available for teams, organizations, and customers.

**Details:**

- Filter usage analytics, spend logs, and activity metrics by agent ID
- View breakdowns on a per-agent basis
- Consistent filtering experience across all usage and analytics views

* * *

## New Providers and Endpoints[​](#new-providers-and-endpoints "Direct link to New Providers and Endpoints")

### New Providers (5 new providers)[​](#new-providers-5-new-providers "Direct link to New Providers (5 new providers)")

ProviderSupported LiteLLM EndpointsDescription[SAP Gen AI Hub](https://docs.litellm.ai/docs/providers/sap)`/chat/completions`, `/messages`, `/responses`SAP Generative AI Hub integration for enterprise AI[LangGraph](https://docs.litellm.ai/docs/providers/langgraph)`/chat/completions`, `/messages`, `/responses`, `/a2a`LangGraph agents for agentic workflows[Azure AI Foundry Agents](https://docs.litellm.ai/docs/providers/azure_ai_agents)`/chat/completions`, `/messages`, `/responses`, `/a2a`Azure AI Foundry Agents for enterprise agent deployments[Voyage AI Rerank](https://docs.litellm.ai/docs/providers/voyage)`/rerank`Voyage AI rerank models support[Fireworks AI Rerank](https://docs.litellm.ai/docs/providers/fireworks_ai)`/rerank`Fireworks AI rerank endpoint support

### New LLM API Endpoints (4 new endpoints)[​](#new-llm-api-endpoints-4-new-endpoints "Direct link to New LLM API Endpoints (4 new endpoints)")

EndpointMethodDescriptionDocumentation`/containers/{id}/files`GETList files in a container[Docs](https://docs.litellm.ai/docs/container_files)`/containers/{id}/files/{file_id}`GETRetrieve container file metadata[Docs](https://docs.litellm.ai/docs/container_files)`/containers/{id}/files/{file_id}`DELETEDelete a file from a container[Docs](https://docs.litellm.ai/docs/container_files)`/containers/{id}/files/{file_id}/content`GETRetrieve container file content[Docs](https://docs.litellm.ai/docs/container_files)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support (270+ new models)[​](#new-model-support-270-new-models "Direct link to New Model Support (270+ new models)")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesOpenAI`gpt-5.2`400K$1.75$14.00Reasoning, vision, PDF, cachingOpenAI`gpt-5.2-pro`400K$21.00$168.00Reasoning, web search, visionAzure`azure/gpt-5.2`400K$1.75$14.00Reasoning, vision, PDF, cachingAzure`azure/gpt-5.2-pro`400K$21.00$168.00Reasoning, web searchBedrock`us.writer.palmyra-x4-v1:0`128K$2.50$10.00Function calling, PDF inputBedrock`us.writer.palmyra-x5-v1:0`1M$0.60$6.00Function calling, PDF inputBedrock`eu.anthropic.claude-opus-4-5-20251101-v1:0`200K$5.00$25.00Reasoning, computer use, visionBedrock`google.gemma-3-12b-it`128K$0.10$0.30Audio inputBedrock`moonshot.kimi-k2-thinking`128K$0.60$2.50ReasoningBedrock`nvidia.nemotron-nano-12b-v2`128K$0.20$0.60VisionBedrock`qwen.qwen3-next-80b-a3b`128K$0.15$1.20Function callingVertex AI`vertex_ai/deepseek-ai/deepseek-v3.2-maas`164K$0.56$1.68Reasoning, cachingMistral`mistral/codestral-2508`256K$0.30$0.90Function callingMistral`mistral/devstral-2512`256K$0.40$2.00Function callingMistral`mistral/labs-devstral-small-2512`256K$0.10$0.30Function callingCerebras`cerebras/zai-glm-4.6`128K--Chat completionsNVIDIA NIM`nvidia_nim/ranking/nvidia/llama-3.2-nv-rerankqa-1b-v2`-FreeFreeRerankVoyage`voyage/rerank-2.5`32K$0.05/1K tokens-RerankFireworks AI227 new modelsVariousVariousVariousFull model catalog

#### Features[​](#features "Direct link to Features")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Add support for OpenAI GPT-5.2 models with reasoning\_effort='xhigh' - [PR #17836](https://github.com/BerriAI/litellm/pull/17836), [PR #17875](https://github.com/BerriAI/litellm/pull/17875)
  - Include 'user' param for responses API models - [PR #17648](https://github.com/BerriAI/litellm/pull/17648)
  - Use optimized async http client for text completions - [PR #17831](https://github.com/BerriAI/litellm/pull/17831)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Add Azure GPT-5.2 models support - [PR #17866](https://github.com/BerriAI/litellm/pull/17866)
- [**Azure AI**](https://docs.litellm.ai/docs/providers/azure_ai)
  
  - Fix Azure AI Anthropic api-key header and passthrough cost calculation - [PR #17656](https://github.com/BerriAI/litellm/pull/17656)
  - Remove unsupported params from Azure AI Anthropic requests - [PR #17822](https://github.com/BerriAI/litellm/pull/17822)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Prevent duplicate tool\_result blocks with same tool - [PR #17632](https://github.com/BerriAI/litellm/pull/17632)
  - Handle partial JSON chunks in streaming responses - [PR #17493](https://github.com/BerriAI/litellm/pull/17493)
  - Preserve server\_tool\_use and web\_search\_tool\_result in multi-turn conversations - [PR #17746](https://github.com/BerriAI/litellm/pull/17746)
  - Capture web\_search\_tool\_result in streaming for multi-turn conversations - [PR #17798](https://github.com/BerriAI/litellm/pull/17798)
  - Add retrieve batches and retrieve file content support - [PR #17700](https://github.com/BerriAI/litellm/pull/17700)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add new Bedrock OSS models to model list - [PR #17638](https://github.com/BerriAI/litellm/pull/17638)
  - Add Bedrock Writer models (Palmyra-X4, Palmyra-X5) - [PR #17685](https://github.com/BerriAI/litellm/pull/17685)
  - Add EU Claude Opus 4.5 model - [PR #17897](https://github.com/BerriAI/litellm/pull/17897)
  - Add serviceTier support for Converse API - [PR #17810](https://github.com/BerriAI/litellm/pull/17810)
  - Fix header forwarding with custom API for Bedrock embeddings - [PR #17872](https://github.com/BerriAI/litellm/pull/17872)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add support for computer use for Gemini - [PR #17756](https://github.com/BerriAI/litellm/pull/17756)
  - Handle context window errors - [PR #17751](https://github.com/BerriAI/litellm/pull/17751)
  - Add speechConfig to GenerationConfig for Gemini TTS - [PR #17851](https://github.com/BerriAI/litellm/pull/17851)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add DeepSeek-V3.2 model support - [PR #17770](https://github.com/BerriAI/litellm/pull/17770)
  - Preserve systemInstructions for generate content request - [PR #17803](https://github.com/BerriAI/litellm/pull/17803)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Add Codestral 2508, Devstral 2512 models - [PR #17801](https://github.com/BerriAI/litellm/pull/17801)
- [**Cerebras**](https://docs.litellm.ai/docs/providers/cerebras)
  
  - Add zai-glm-4.6 model support - [PR #17683](https://github.com/BerriAI/litellm/pull/17683)
  - Fix context window errors not recognized - [PR #17587](https://github.com/BerriAI/litellm/pull/17587)
- [**DeepSeek**](https://docs.litellm.ai/docs/providers/deepseek)
  
  - Add native support for thinking and reasoning\_effort params - [PR #17712](https://github.com/BerriAI/litellm/pull/17712)
- [**NVIDIA NIM Rerank**](https://docs.litellm.ai/docs/providers/nvidia_nim_rerank)
  
  - Add llama-3.2-nv-rerankqa-1b-v2 rerank model - [PR #17670](https://github.com/BerriAI/litellm/pull/17670)
- [**Fireworks AI**](https://docs.litellm.ai/docs/providers/fireworks_ai)
  
  - Add 227 new Fireworks AI models - [PR #17692](https://github.com/BerriAI/litellm/pull/17692)
- [**Dashscope**](https://docs.litellm.ai/docs/providers/dashscope)
  
  - Fix default base\_url error - [PR #17584](https://github.com/BerriAI/litellm/pull/17584)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Fix missing content in Anthropic to OpenAI conversion - [PR #17693](https://github.com/BerriAI/litellm/pull/17693)
  - Avoid error when we have just the tool\_calls in input - [PR #17753](https://github.com/BerriAI/litellm/pull/17753)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Fix error about encoding video id for Azure - [PR #17708](https://github.com/BerriAI/litellm/pull/17708)
- [**Azure AI**](https://docs.litellm.ai/docs/providers/azure_ai)
  
  - Fix LLM provider for azure\_ai in model map - [PR #17805](https://github.com/BerriAI/litellm/pull/17805)
- [**Watsonx**](https://docs.litellm.ai/docs/providers/watsonx)
  
  - Fix Watsonx Audio Transcription to only send supported params to API - [PR #17840](https://github.com/BerriAI/litellm/pull/17840)
- [**Router**](https://docs.litellm.ai/docs/routing)
  
  - Handle tools=None in completion requests - [PR #17684](https://github.com/BerriAI/litellm/pull/17684)
  - Add minimum request threshold for error rate cooldown - [PR #17464](https://github.com/BerriAI/litellm/pull/17464)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Add usage details in responses usage object - [PR #17641](https://github.com/BerriAI/litellm/pull/17641)
  - Fix error for response API polling - [PR #17654](https://github.com/BerriAI/litellm/pull/17654)
  - Fix streaming tool\_calls being dropped when text + tool\_calls - [PR #17652](https://github.com/BerriAI/litellm/pull/17652)
  - Transform image content in tool results for Responses API - [PR #17799](https://github.com/BerriAI/litellm/pull/17799)
  - Fix responses api not applying tpm rate limits on api keys - [PR #17707](https://github.com/BerriAI/litellm/pull/17707)
- [**Containers API**](https://docs.litellm.ai/docs/containers)
  
  - Allow using LIST, Create Containers using custom-llm-provider - [PR #17740](https://github.com/BerriAI/litellm/pull/17740)
  - Add new container API file management + UI Interface - [PR #17745](https://github.com/BerriAI/litellm/pull/17745)
- [**Rerank API**](https://docs.litellm.ai/docs/rerank)
  
  - Add support for forwarding client headers in /rerank endpoint - [PR #17873](https://github.com/BerriAI/litellm/pull/17873)
- [**Files API**](https://docs.litellm.ai/docs/files_endpoints)
  
  - Add support for expires\_after param in Files endpoint - [PR #17860](https://github.com/BerriAI/litellm/pull/17860)
- [**Video API**](https://docs.litellm.ai/docs/videos)
  
  - Use litellm params for all videos APIs - [PR #17732](https://github.com/BerriAI/litellm/pull/17732)
  - Respect videos content db creds - [PR #17771](https://github.com/BerriAI/litellm/pull/17771)
- [**Embeddings API**](https://docs.litellm.ai/docs/proxy/embedding)
  
  - Fix handling token array input decoding for embeddings - [PR #17468](https://github.com/BerriAI/litellm/pull/17468)
- [**Chat Completions API**](https://docs.litellm.ai/docs/completion/input)
  
  - Add v0 target storage support - store files in Azure AI storage and use with chat completions API - [PR #17758](https://github.com/BerriAI/litellm/pull/17758)
- [**generateContent API**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Support model names with slashes on Gemini generateContent endpoints - [PR #17743](https://github.com/BerriAI/litellm/pull/17743)
- **General**
  
  - Use audio content for caching - [PR #17651](https://github.com/BerriAI/litellm/pull/17651)
  - Return 403 exception when calling GET responses API - [PR #17629](https://github.com/BerriAI/litellm/pull/17629)
  - Add nested field removal support to additional\_drop\_params - [PR #17711](https://github.com/BerriAI/litellm/pull/17711)
  - Async post\_call\_streaming\_iterator\_hook now properly iterates async generators - [PR #17626](https://github.com/BerriAI/litellm/pull/17626)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Fix handle string content in is\_cached\_message - [PR #17853](https://github.com/BerriAI/litellm/pull/17853)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **UI Settings**
  
  - Add Get and Update Backend Routes for UI Settings - [PR #17689](https://github.com/BerriAI/litellm/pull/17689)
  - UI Settings page implementation - [PR #17697](https://github.com/BerriAI/litellm/pull/17697)
  - Ensure Model Page honors UI Settings - [PR #17804](https://github.com/BerriAI/litellm/pull/17804)
  - Add All Proxy Models to Default User Settings - [PR #17902](https://github.com/BerriAI/litellm/pull/17902)
- **Agent & Usage UI**
  
  - Daily Agent Usage Backend - [PR #17781](https://github.com/BerriAI/litellm/pull/17781)
  - Agent Usage UI - [PR #17797](https://github.com/BerriAI/litellm/pull/17797)
  - Add agent cost tracking on UI - [PR #17899](https://github.com/BerriAI/litellm/pull/17899)
  - New Badge for Agent Usage - [PR #17883](https://github.com/BerriAI/litellm/pull/17883)
  - Usage Entity labels for filtering - [PR #17896](https://github.com/BerriAI/litellm/pull/17896)
  - Agent Usage Page minor fixes - [PR #17901](https://github.com/BerriAI/litellm/pull/17901)
  - Usage Page View Select component - [PR #17854](https://github.com/BerriAI/litellm/pull/17854)
  - Usage Page Components refactor - [PR #17848](https://github.com/BerriAI/litellm/pull/17848)
- **Logs & Spend**
  
  - Enhanced spend analytics in logs view - [PR #17623](https://github.com/BerriAI/litellm/pull/17623)
  - Add user info delete modal for user management - [PR #17625](https://github.com/BerriAI/litellm/pull/17625)
  - Show request and response details in logs view - [PR #17928](https://github.com/BerriAI/litellm/pull/17928)
- **Virtual Keys**
  
  - Fix x-litellm-key-spend header update - [PR #17864](https://github.com/BerriAI/litellm/pull/17864)
- **Models & Endpoints**
  
  - Model Hub Useful Links Rearrange - [PR #17859](https://github.com/BerriAI/litellm/pull/17859)
  - Create Team Model Dropdown honors Organization's Models - [PR #17834](https://github.com/BerriAI/litellm/pull/17834)
- **SSO & Auth**
  
  - Allow upserting user role when SSO provider role changes - [PR #17754](https://github.com/BerriAI/litellm/pull/17754)
  - Allow fetching role from generic SSO provider (Keycloak) - [PR #17787](https://github.com/BerriAI/litellm/pull/17787)
  - JWT Auth - allow selecting team\_id from request header - [PR #17884](https://github.com/BerriAI/litellm/pull/17884)
  - Remove SSO Config Values from Config Table on SSO Update - [PR #17668](https://github.com/BerriAI/litellm/pull/17668)
- **Teams**
  
  - Attach team to org table - [PR #17832](https://github.com/BerriAI/litellm/pull/17832)
  - Expose the team alias when authenticating - [PR #17725](https://github.com/BerriAI/litellm/pull/17725)
- **MCP Server Management**
  
  - Add extra\_headers and allowed\_tools to UpdateMCPServerRequest - [PR #17940](https://github.com/BerriAI/litellm/pull/17940)
- **Notifications**
  
  - Show progress and pause on hover for Notifications - [PR #17942](https://github.com/BerriAI/litellm/pull/17942)
- **General**
  
  - Allow Root Path to Redirect when Docs not on Root Path - [PR #16843](https://github.com/BerriAI/litellm/pull/16843)
  - Show UI version number on top left near logo - [PR #17891](https://github.com/BerriAI/litellm/pull/17891)
  - Re-organize left navigation with correct categories and agents on root - [PR #17890](https://github.com/BerriAI/litellm/pull/17890)
  - UI Playground - allow custom model names in model selector dropdown - [PR #17892](https://github.com/BerriAI/litellm/pull/17892)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **UI Fixes**
  
  - Fix links + old login page deprecation message - [PR #17624](https://github.com/BerriAI/litellm/pull/17624)
  - Filtering for Chat UI Endpoint Selector - [PR #17567](https://github.com/BerriAI/litellm/pull/17567)
  - Race Condition Handling in SCIM v2 - [PR #17513](https://github.com/BerriAI/litellm/pull/17513)
  - Make /litellm\_model\_cost\_map public - [PR #16795](https://github.com/BerriAI/litellm/pull/16795)
  - Custom Callback on UI - [PR #17522](https://github.com/BerriAI/litellm/pull/17522)
  - Add User Writable Directory to Non Root Docker for Logo - [PR #17180](https://github.com/BerriAI/litellm/pull/17180)
  - Swap URL Input and Display Name inputs - [PR #17682](https://github.com/BerriAI/litellm/pull/17682)
  - Change deprecation banner to only show on /sso/key/generate - [PR #17681](https://github.com/BerriAI/litellm/pull/17681)
  - Change credential encryption to only affect db credentials - [PR #17741](https://github.com/BerriAI/litellm/pull/17741)
- **Auth & Routes**
  
  - Return 403 instead of 503 for unauthorized routes - [PR #17723](https://github.com/BerriAI/litellm/pull/17723)
  - AI Gateway Auth - allow using wildcard patterns for public routes - [PR #17686](https://github.com/BerriAI/litellm/pull/17686)

* * *

## AI Integrations[​](#ai-integrations "Direct link to AI Integrations")

### New Integrations (4 new integrations)[​](#new-integrations-4-new-integrations "Direct link to New Integrations (4 new integrations)")

IntegrationTypeDescription[SumoLogic](https://docs.litellm.ai/docs/proxy/logging#sumologic)LoggingNative webhook integration for SumoLogic - [PR #17630](https://github.com/BerriAI/litellm/pull/17630)[Arize Phoenix](https://docs.litellm.ai/docs/proxy/arize_phoenix_prompts)Prompt ManagementArize Phoenix OSS prompt management integration - [PR #17750](https://github.com/BerriAI/litellm/pull/17750)[Sendgrid](https://docs.litellm.ai/docs/proxy/email)EmailSendgrid email notifications integration - [PR #17775](https://github.com/BerriAI/litellm/pull/17775)[Onyx](https://docs.litellm.ai/docs/proxy/guardrails/onyx_security)GuardrailsOnyx guardrail hooks integration - [PR #16591](https://github.com/BerriAI/litellm/pull/16591)

### Logging[​](#logging "Direct link to Logging")

- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Propagate Langfuse trace\_id - [PR #17669](https://github.com/BerriAI/litellm/pull/17669)
  - Prefer standard trace id for Langfuse logging - [PR #17791](https://github.com/BerriAI/litellm/pull/17791)
  - Move query params to create\_pass\_through\_route call in Langfuse passthrough - [PR #17660](https://github.com/BerriAI/litellm/pull/17660)
  - Add support for custom masking function - [PR #17826](https://github.com/BerriAI/litellm/pull/17826)
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/logging#prometheus)
  
  - Add 'exception\_status' to prometheus logger - [PR #17847](https://github.com/BerriAI/litellm/pull/17847)
- [**OpenTelemetry**](https://docs.litellm.ai/docs/proxy/logging#otel)
  
  - Add latency metrics (TTFT, TPOT, Total Generation Time) to OTEL payload - [PR #17888](https://github.com/BerriAI/litellm/pull/17888)
- **General**
  
  - Add polling via cache feature for async logging - [PR #16862](https://github.com/BerriAI/litellm/pull/16862)

### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**HiddenLayer**](https://docs.litellm.ai/docs/proxy/guardrails/hiddenlayer)
  
  - Add HiddenLayer Guardrail Hooks - [PR #17728](https://github.com/BerriAI/litellm/pull/17728)
- [**Pillar Security**](https://docs.litellm.ai/docs/proxy/guardrails/pillar_security)
  
  - Add opt-in evidence results for Pillar Security guardrail during monitoring - [PR #17812](https://github.com/BerriAI/litellm/pull/17812)
- [**PANW Prisma AIRS**](https://docs.litellm.ai/docs/proxy/guardrails/panw_prisma_airs)
  
  - Add configurable fail-open, timeout, and app\_user tracking - [PR #17785](https://github.com/BerriAI/litellm/pull/17785)
- [**Presidio**](https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2)
  
  - Add support for configurable confidence score thresholds and scope in Presidio PII masking - [PR #17817](https://github.com/BerriAI/litellm/pull/17817)
- [**LiteLLM Content Filter**](https://docs.litellm.ai/docs/proxy/guardrails/litellm_content_filter)
  
  - Mask all regex pattern matches, not just first - [PR #17727](https://github.com/BerriAI/litellm/pull/17727)
- [**Regex Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/secret_detection)
  
  - Add enhanced regex pattern matching for guardrails - [PR #17915](https://github.com/BerriAI/litellm/pull/17915)
- [**Gray Swan Guardrail**](https://docs.litellm.ai/docs/proxy/guardrails/grayswan)
  
  - Add passthrough mode for model response - [PR #17102](https://github.com/BerriAI/litellm/pull/17102)

### Prompt Management[​](#prompt-management "Direct link to Prompt Management")

- **General**
  
  - New API for integrating prompt management providers - [PR #17829](https://github.com/BerriAI/litellm/pull/17829)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Service Tier Pricing** - Extract service\_tier from response/usage for OpenAI flex pricing - [PR #17748](https://github.com/BerriAI/litellm/pull/17748)
- **Agent Cost Tracking** - Track agent\_id in SpendLogs - [PR #17795](https://github.com/BerriAI/litellm/pull/17795)
- **Tag Activity** - Deduplicate /tag/daily/activity metadata - [PR #16764](https://github.com/BerriAI/litellm/pull/16764)
- **Rate Limiting** - Dynamic Rate Limiter - allow specifying ttl for in memory cache - [PR #17679](https://github.com/BerriAI/litellm/pull/17679)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **Chat Completions Integration** - Add support for using MCPs on /chat/completions - [PR #17747](https://github.com/BerriAI/litellm/pull/17747)
- **UI Session Permissions** - Fix UI session MCP permissions across real teams - [PR #17620](https://github.com/BerriAI/litellm/pull/17620)
- **OAuth Callback** - Fix MCP OAuth callback routing and URL handling - [PR #17789](https://github.com/BerriAI/litellm/pull/17789)
- **Tool Name Prefix** - Fix MCP tool name prefix - [PR #17908](https://github.com/BerriAI/litellm/pull/17908)

* * *

## Agent Gateway (A2A)[​](#agent-gateway-a2a "Direct link to Agent Gateway (A2A)")

- **Cost Per Query** - Add cost per query for agent invocations - [PR #17774](https://github.com/BerriAI/litellm/pull/17774)
- **Token Counting** - Add token counting non streaming + streaming - [PR #17779](https://github.com/BerriAI/litellm/pull/17779)
- **Cost Per Token** - Add cost per token pricing for A2A - [PR #17780](https://github.com/BerriAI/litellm/pull/17780)
- **LangGraph Provider** - Add LangGraph provider for Agent Gateway - [PR #17783](https://github.com/BerriAI/litellm/pull/17783)
- **Bedrock & LangGraph Agents** - Allow using Bedrock AgentCore, LangGraph agents with A2A Gateway - [PR #17786](https://github.com/BerriAI/litellm/pull/17786)
- **Agent Management** - Allow adding LangGraph, Bedrock Agent Core agents - [PR #17802](https://github.com/BerriAI/litellm/pull/17802)
- **Azure Foundry Agents** - Add Azure AI Foundry Agents support - [PR #17845](https://github.com/BerriAI/litellm/pull/17845)
- **Azure Foundry UI** - Allow adding Azure Foundry Agents on UI - [PR #17909](https://github.com/BerriAI/litellm/pull/17909)
- **Azure Foundry Fixes** - Ensure Azure Foundry agents work correctly - [PR #17943](https://github.com/BerriAI/litellm/pull/17943)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Memory Leak Fix** - Cut memory leak in half - [PR #17784](https://github.com/BerriAI/litellm/pull/17784)
- **Spend Logs Memory** - Reduce memory accumulation of spend\_logs - [PR #17742](https://github.com/BerriAI/litellm/pull/17742)
- **Router Optimization** - Replace time.perf\_counter() with time.time() - [PR #17881](https://github.com/BerriAI/litellm/pull/17881)
- **Filter Internal Params** - Filter internal params in fallback code - [PR #17941](https://github.com/BerriAI/litellm/pull/17941)
- **Gunicorn Suggestion** - Suggest Gunicorn instead of uvicorn when using max\_requests\_before\_restart - [PR #17788](https://github.com/BerriAI/litellm/pull/17788)
- **Pydantic Warnings** - Mitigate PydanticDeprecatedSince20 warnings - [PR #17657](https://github.com/BerriAI/litellm/pull/17657)
- **Python 3.14 Support** - Add Python 3.14 support via grpcio version constraints - [PR #17666](https://github.com/BerriAI/litellm/pull/17666)
- **OpenAI Package** - Bump openai package to 2.9.0 - [PR #17818](https://github.com/BerriAI/litellm/pull/17818)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Contributing** - Update clone instructions to recommend forking first - [PR #17637](https://github.com/BerriAI/litellm/pull/17637)
- **Getting Started** - Improve Getting Started page and SDK documentation structure - [PR #17614](https://github.com/BerriAI/litellm/pull/17614)
- **JSON Mode** - Make it clearer how to get Pydantic model output - [PR #17671](https://github.com/BerriAI/litellm/pull/17671)
- **drop\_params** - Update litellm docs for drop\_params - [PR #17658](https://github.com/BerriAI/litellm/pull/17658)
- **Environment Variables** - Document missing environment variables and fix incorrect types - [PR #17649](https://github.com/BerriAI/litellm/pull/17649)
- **SumoLogic** - Add SumoLogic integration documentation - [PR #17647](https://github.com/BerriAI/litellm/pull/17647)
- **SAP Gen AI** - Add SAP Gen AI provider documentation - [PR #17667](https://github.com/BerriAI/litellm/pull/17667)
- **Authentication** - Add Note for Authentication - [PR #17733](https://github.com/BerriAI/litellm/pull/17733)
- **Known Issues** - Adding known issues to 1.80.5-stable docs - [PR #17738](https://github.com/BerriAI/litellm/pull/17738)
- **Supported Endpoints** - Fix Supported Endpoints page - [PR #17710](https://github.com/BerriAI/litellm/pull/17710)
- **Token Count** - Document token count endpoint - [PR #17772](https://github.com/BerriAI/litellm/pull/17772)
- **Overview** - Made litellm proxy and SDK difference cleaner in overview with a table - [PR #17790](https://github.com/BerriAI/litellm/pull/17790)
- **Containers API** - Add docs for containers files API + code interpreter on LiteLLM - [PR #17749](https://github.com/BerriAI/litellm/pull/17749)
- **Target Storage** - Add documentation for target storage - [PR #17882](https://github.com/BerriAI/litellm/pull/17882)
- **Agent Usage** - Agent Usage documentation - [PR #17931](https://github.com/BerriAI/litellm/pull/17931), [PR #17932](https://github.com/BerriAI/litellm/pull/17932), [PR #17934](https://github.com/BerriAI/litellm/pull/17934)
- **Cursor Integration** - Cursor Integration documentation - [PR #17855](https://github.com/BerriAI/litellm/pull/17855), [PR #17939](https://github.com/BerriAI/litellm/pull/17939)
- **A2A Cost Tracking** - A2A cost tracking docs - [PR #17913](https://github.com/BerriAI/litellm/pull/17913)
- **Azure Search** - Update azure search docs - [PR #17726](https://github.com/BerriAI/litellm/pull/17726)
- **Milvus Client** - Fix milvus client docs - [PR #17736](https://github.com/BerriAI/litellm/pull/17736)
- **Streaming Logging** - Remove streaming logging doc - [PR #17739](https://github.com/BerriAI/litellm/pull/17739)
- **Integration Docs** - Update integration docs location - [PR #17644](https://github.com/BerriAI/litellm/pull/17644)
- **Links** - Updated docs links for mistral and anthropic - [PR #17852](https://github.com/BerriAI/litellm/pull/17852)
- **Community** - Add community doc link - [PR #17734](https://github.com/BerriAI/litellm/pull/17734)
- **Pricing** - Update pricing for global.anthropic.claude-haiku-4-5-20251001-v1:0 - [PR #17703](https://github.com/BerriAI/litellm/pull/17703)
- **gpt-image-1-mini** - Correct model type for gpt-image-1-mini - [PR #17635](https://github.com/BerriAI/litellm/pull/17635)

* * *

## Infrastructure / Deployment[​](#infrastructure--deployment "Direct link to Infrastructure / Deployment")

- **Docker** - Use python instead of wget for healthcheck in docker-compose.yml - [PR #17646](https://github.com/BerriAI/litellm/pull/17646)
- **Helm Chart** - Add extraResources support for Helm chart deployments - [PR #17627](https://github.com/BerriAI/litellm/pull/17627)
- **Helm Versioning** - Add semver prerelease suffix to helm chart versions - [PR #17678](https://github.com/BerriAI/litellm/pull/17678)
- **Database Schema** - Add storage\_backend and storage\_url columns to schema.prisma for target storage feature - [PR #17936](https://github.com/BerriAI/litellm/pull/17936)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @xianzongxie-stripe made their first contribution in [PR #16862](https://github.com/BerriAI/litellm/pull/16862)
- @krisxia0506 made their first contribution in [PR #17637](https://github.com/BerriAI/litellm/pull/17637)
- @chetanchoudhary-sumo made their first contribution in [PR #17630](https://github.com/BerriAI/litellm/pull/17630)
- @kevinmarx made their first contribution in [PR #17632](https://github.com/BerriAI/litellm/pull/17632)
- @expruc made their first contribution in [PR #17627](https://github.com/BerriAI/litellm/pull/17627)
- @rcII made their first contribution in [PR #17626](https://github.com/BerriAI/litellm/pull/17626)
- @tamirkiviti13 made their first contribution in [PR #16591](https://github.com/BerriAI/litellm/pull/16591)
- @Eric84626 made their first contribution in [PR #17629](https://github.com/BerriAI/litellm/pull/17629)
- @vasilisazayka made their first contribution in [PR #16053](https://github.com/BerriAI/litellm/pull/16053)
- @juliettech13 made their first contribution in [PR #17663](https://github.com/BerriAI/litellm/pull/17663)
- @jason-nance made their first contribution in [PR #17660](https://github.com/BerriAI/litellm/pull/17660)
- @yisding made their first contribution in [PR #17671](https://github.com/BerriAI/litellm/pull/17671)
- @emilsvennesson made their first contribution in [PR #17656](https://github.com/BerriAI/litellm/pull/17656)
- @kumekay made their first contribution in [PR #17646](https://github.com/BerriAI/litellm/pull/17646)
- @chenzhaofei01 made their first contribution in [PR #17584](https://github.com/BerriAI/litellm/pull/17584)
- @shivamrawat1 made their first contribution in [PR #17733](https://github.com/BerriAI/litellm/pull/17733)
- @ephrimstanley made their first contribution in [PR #17723](https://github.com/BerriAI/litellm/pull/17723)
- @hwittenborn made their first contribution in [PR #17743](https://github.com/BerriAI/litellm/pull/17743)
- @peterkc made their first contribution in [PR #17727](https://github.com/BerriAI/litellm/pull/17727)
- @saisurya237 made their first contribution in [PR #17725](https://github.com/BerriAI/litellm/pull/17725)
- @Ashton-Sidhu made their first contribution in [PR #17728](https://github.com/BerriAI/litellm/pull/17728)
- @CyrusTC made their first contribution in [PR #17810](https://github.com/BerriAI/litellm/pull/17810)
- @jichmi made their first contribution in [PR #17703](https://github.com/BerriAI/litellm/pull/17703)
- @ryan-crabbe made their first contribution in [PR #17852](https://github.com/BerriAI/litellm/pull/17852)
- @nlineback made their first contribution in [PR #17851](https://github.com/BerriAI/litellm/pull/17851)
- @butnarurazvan made their first contribution in [PR #17468](https://github.com/BerriAI/litellm/pull/17468)
- @yoshi-p27 made their first contribution in [PR #17915](https://github.com/BerriAI/litellm/pull/17915)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.80.8.rc.1...v1.80.10)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.80.8-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Agent Gateway (A2A)** - [Invoke agents through the AI Gateway with request/response logging and access controls](https://docs.litellm.ai/docs/a2a)
- **Guardrails API v2** - [Generic Guardrail API with streaming support, structured messages, and tool call checks](https://docs.litellm.ai/docs/adding_provider/generic_guardrail_api)
- **Customer (End User) Usage UI** - [Track and visualize end-user spend directly in the dashboard](https://docs.litellm.ai/docs/proxy/customer_usage)
- **vLLM Batch + Files API** - [Support for batch and files API with vLLM deployments](https://docs.litellm.ai/docs/batches)
- **Dynamic Rate Limiting on Teams** - [Enable dynamic rate limits and priority reservation on team-level](https://docs.litellm.ai/docs/proxy/team_budgets)
- **Google Cloud Chirp3 HD** - [New text-to-speech provider with Chirp3 HD voices](https://docs.litellm.ai/docs/text_to_speech)

* * *

### Agent Gateway (A2A)[​](#agent-gateway-a2a "Direct link to Agent Gateway (A2A)")

This release introduces **A2A Agent Gateway** for LiteLLM, allowing you to invoke and manage A2A agents with the same controls you have for LLM APIs.

As a **LiteLLM Gateway Admin**, you can now do the following:

- **Request/Response Logging** - Every agent invocation is logged to the Logs page with full request and response tracking.
- **Access Control** - Control which Team/Key can access which agents.

As a developer, you can continue using the A2A SDK, all you need to do is point you `A2AClient` to the LiteLLM proxy URL and your API key.

**Works with the A2A SDK:**

```
from a2a.client import A2AClient

client = A2AClient(
    base_url="http://localhost:4000",# Your LiteLLM proxy
    api_key="sk-1234"# LiteLLM API key
)

response = client.send_message(
    agent_id="my-agent",
    message="What's the status of my order?"
)
```

Get started with Agent Gateway here: [Agent Gateway Documentation](https://docs.litellm.ai/docs/a2a)

* * *

### Customer (End User) Usage UI[​](#customer-end-user-usage-ui "Direct link to Customer (End User) Usage UI")

Users can now filter usage statistics by customers, providing the same granular filtering capabilities available for teams and organizations.

**Details:**

- Filter usage analytics, spend logs, and activity metrics by customer ID
- View customer-level breakdowns alongside existing team and user-level filters
- Consistent filtering experience across all usage and analytics views

* * *

## New Providers and Endpoints[​](#new-providers-and-endpoints "Direct link to New Providers and Endpoints")

### New Providers (5 new providers)[​](#new-providers-5-new-providers "Direct link to New Providers (5 new providers)")

ProviderSupported LiteLLM EndpointsDescription[**Z.AI (Zhipu AI)**](https://docs.litellm.ai/docs/providers/zai)`/v1/chat/completions`, `/v1/responses`, `/v1/messages`Built-in support for Zhipu AI GLM models[**RAGFlow**](https://docs.litellm.ai/docs/providers/ragflow)`/v1/chat/completions`, `/v1/responses`, `/v1/messages`, `/v1/vector_stores`RAG-based chat completions with vector store support[**PublicAI**](https://docs.litellm.ai/docs/providers/publicai)`/v1/chat/completions`, `/v1/responses`, `/v1/messages`OpenAI-compatible provider via JSON config[**Google Cloud Chirp3 HD**](https://docs.litellm.ai/docs/text_to_speech)`/v1/audio/speech`, `/v1/audio/speech/stream`Text-to-speech with Google Cloud Chirp3 HD voices

### New LLM API Endpoints (2 new endpoints)[​](#new-llm-api-endpoints-2-new-endpoints "Direct link to New LLM API Endpoints (2 new endpoints)")

EndpointMethodDescriptionDocumentation`/v1/agents/invoke`POSTInvoke A2A agents through the AI Gateway[Agent Gateway](https://docs.litellm.ai/docs/a2a)`/cursor/chat/completions`POSTCursor BYOK endpoint - accepts Responses API input, returns Chat Completions output[Cursor Integration](https://docs.litellm.ai/docs/tutorials/cursor_integration)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support (33 new models)[​](#new-model-support-33-new-models "Direct link to New Model Support (33 new models)")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesOpenAI`gpt-5.1-codex-max`400K$1.25$10.00Reasoning, vision, PDF input, responses APIAzure`azure/gpt-5.1-codex-max`400K$1.25$10.00Reasoning, vision, PDF input, responses APIAnthropic`claude-opus-4-5`200K$5.00$25.00Computer use, reasoning, visionBedrock`global.anthropic.claude-opus-4-5-20251101-v1:0`200K$5.00$25.00Computer use, reasoning, visionBedrock`amazon.nova-2-lite-v1:0`1M$0.30$2.50Reasoning, vision, video, PDF inputBedrock`amazon.titan-image-generator-v2:0`--$0.008/imageImage generationFireworks`fireworks_ai/deepseek-v3p2`164K$1.20$1.20Function calling, response schemaFireworks`fireworks_ai/kimi-k2-instruct-0905`262K$0.60$2.50Function calling, response schemaDeepSeek`deepseek/deepseek-v3.2`164K$0.28$0.40Reasoning, function callingMistral`mistral/mistral-large-3`256K$0.50$1.50Function calling, visionAzure AI`azure_ai/mistral-large-3`256K$0.50$1.50Function calling, visionMoonshot`moonshot/kimi-k2-0905-preview`262K$0.60$2.50Function calling, web searchMoonshot`moonshot/kimi-k2-turbo-preview`262K$1.15$8.00Function calling, web searchMoonshot`moonshot/kimi-k2-thinking-turbo`262K$1.15$8.00Function calling, web searchOpenRouter`openrouter/deepseek/deepseek-v3.2`164K$0.28$0.40Reasoning, function callingDatabricks`databricks/databricks-claude-haiku-4-5`200K$1.00$5.00Reasoning, function callingDatabricks`databricks/databricks-claude-opus-4`200K$15.00$75.00Reasoning, function callingDatabricks`databricks/databricks-claude-opus-4-1`200K$15.00$75.00Reasoning, function callingDatabricks`databricks/databricks-claude-opus-4-5`200K$5.00$25.00Reasoning, function callingDatabricks`databricks/databricks-claude-sonnet-4`200K$3.00$15.00Reasoning, function callingDatabricks`databricks/databricks-claude-sonnet-4-1`200K$3.00$15.00Reasoning, function callingDatabricks`databricks/databricks-gemini-2-5-flash`1M$0.30$2.50Function callingDatabricks`databricks/databricks-gemini-2-5-pro`1M$1.25$10.00Function callingDatabricks`databricks/databricks-gpt-5`400K$1.25$10.00Function callingDatabricks`databricks/databricks-gpt-5-1`400K$1.25$10.00Function callingDatabricks`databricks/databricks-gpt-5-mini`400K$0.25$2.00Function callingDatabricks`databricks/databricks-gpt-5-nano`400K$0.05$0.40Function callingVertex AI`vertex_ai/chirp`-$30.00/1M chars-Text-to-speech (Chirp3 HD)Z.AI`zai/glm-4.6`200K$0.60$2.20Function callingZ.AI`zai/glm-4.5`128K$0.60$2.20Function callingZ.AI`zai/glm-4.5v`128K$0.60$1.80Function calling, visionZ.AI`zai/glm-4.5-flash`128KFreeFreeFunction callingVertex AI`vertex_ai/bge-large-en-v1.5`---BGE Embeddings

#### Features[​](#features "Direct link to Features")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Add `gpt-5.1-codex-max` model pricing and configuration - [PR #17541](https://github.com/BerriAI/litellm/pull/17541)
  - Add xhigh reasoning effort for gpt-5.1-codex-max - [PR #17585](https://github.com/BerriAI/litellm/pull/17585)
  - Add clear error message for empty LLM endpoint responses - [PR #17445](https://github.com/BerriAI/litellm/pull/17445)
- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure/azure)
  
  - Allow reasoning\_effort='none' for Azure gpt-5.1 models - [PR #17311](https://github.com/BerriAI/litellm/pull/17311)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Add `claude-opus-4-5` alias to pricing data - [PR #17313](https://github.com/BerriAI/litellm/pull/17313)
  - Parse `<budget:thinking>` blocks for opus 4.5 - [PR #17534](https://github.com/BerriAI/litellm/pull/17534)
  - Update new Anthropic features as reviewed - [PR #17142](https://github.com/BerriAI/litellm/pull/17142)
  - Skip empty text blocks in Anthropic system messages - [PR #17442](https://github.com/BerriAI/litellm/pull/17442)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add Nova embedding support - [PR #17253](https://github.com/BerriAI/litellm/pull/17253)
  - Add support for Bedrock Qwen 2 imported model - [PR #17461](https://github.com/BerriAI/litellm/pull/17461)
  - Bedrock OpenAI model support - [PR #17368](https://github.com/BerriAI/litellm/pull/17368)
  - Add support for file content download for Bedrock batches - [PR #17470](https://github.com/BerriAI/litellm/pull/17470)
  - Make streaming chunk size configurable in Bedrock API - [PR #17357](https://github.com/BerriAI/litellm/pull/17357)
  - Add experimental latest-user filtering for Bedrock - [PR #17282](https://github.com/BerriAI/litellm/pull/17282)
  - Handle Cohere v4 embed response dictionary format - [PR #17220](https://github.com/BerriAI/litellm/pull/17220)
  - Remove not compatible beta header from Bedrock - [PR #17301](https://github.com/BerriAI/litellm/pull/17301)
  - Add model price and details for Global Opus 4.5 Bedrock endpoint - [PR #17380](https://github.com/BerriAI/litellm/pull/17380)
- [**Gemini (Google AI Studio + Vertex AI)**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add better handling in image generation for Gemini models - [PR #17292](https://github.com/BerriAI/litellm/pull/17292)
  - Fix reasoning\_content showing duplicate content in streaming responses - [PR #17266](https://github.com/BerriAI/litellm/pull/17266)
  - Handle partial JSON chunks after first valid chunk - [PR #17496](https://github.com/BerriAI/litellm/pull/17496)
  - Fix Gemini 3 last chunk thinking block - [PR #17403](https://github.com/BerriAI/litellm/pull/17403)
  - Fix Gemini image\_tokens treated as text tokens in cost calculation - [PR #17554](https://github.com/BerriAI/litellm/pull/17554)
  - Make sure that media resolution is only for Gemini 3 model - [PR #17137](https://github.com/BerriAI/litellm/pull/17137)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add Google Cloud Chirp3 HD support on /speech - [PR #17391](https://github.com/BerriAI/litellm/pull/17391)
  - Add BGE Embeddings support - [PR #17362](https://github.com/BerriAI/litellm/pull/17362)
  - Handle global location for Vertex AI image generation endpoint - [PR #17255](https://github.com/BerriAI/litellm/pull/17255)
  - Add Google Private API Endpoint to Vertex AI fields - [PR #17382](https://github.com/BerriAI/litellm/pull/17382)
- [**Z.AI (Zhipu AI)**](https://docs.litellm.ai/docs/providers/zai)
  
  - Add Z.AI as built-in provider - [PR #17307](https://github.com/BerriAI/litellm/pull/17307)
- [**GitHub Copilot**](https://docs.litellm.ai/docs/providers/github_copilot)
  
  - Add Embedding API support - [PR #17278](https://github.com/BerriAI/litellm/pull/17278)
  - Preserve encrypted\_content in reasoning items for multi-turn conversations - [PR #17130](https://github.com/BerriAI/litellm/pull/17130)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks)
  
  - Update Databricks model pricing and add new models - [PR #17277](https://github.com/BerriAI/litellm/pull/17277)
- [**OVHcloud**](https://docs.litellm.ai/docs/providers/ovhcloud)
  
  - Add support of audio transcription for OVHcloud - [PR #17305](https://github.com/BerriAI/litellm/pull/17305)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Add Mistral Large 3 model support - [PR #17547](https://github.com/BerriAI/litellm/pull/17547)
- [**Moonshot**](https://docs.litellm.ai/docs/providers/moonshot)
  
  - Fix missing Moonshot turbo models and fix incorrect pricing - [PR #17432](https://github.com/BerriAI/litellm/pull/17432)
- [**Together AI**](https://docs.litellm.ai/docs/providers/togetherai)
  
  - Add context window exception mapping for Together AI - [PR #17284](https://github.com/BerriAI/litellm/pull/17284)
- [**WatsonX**](https://docs.litellm.ai/docs/providers/watsonx/index)
  
  - Allow passing zen\_api\_key dynamically - [PR #16655](https://github.com/BerriAI/litellm/pull/16655)
  - Fix Watsonx Audio Transcription API - [PR #17326](https://github.com/BerriAI/litellm/pull/17326)
  - Fix audio transcriptions, don't force content type in request headers - [PR #17546](https://github.com/BerriAI/litellm/pull/17546)
- [**Fireworks AI**](https://docs.litellm.ai/docs/providers/fireworks_ai)
  
  - Add new model `fireworks_ai/kimi-k2-instruct-0905` - [PR #17328](https://github.com/BerriAI/litellm/pull/17328)
  - Add `fireworks/deepseek-v3p2` - [PR #17395](https://github.com/BerriAI/litellm/pull/17395)
- [**DeepSeek**](https://docs.litellm.ai/docs/providers/deepseek)
  
  - Support Deepseek 3.2 with Reasoning - [PR #17384](https://github.com/BerriAI/litellm/pull/17384)
- [**Nova Lite 2**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add Nova Lite 2 reasoning support with reasoningConfig - [PR #17371](https://github.com/BerriAI/litellm/pull/17371)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Fix auth not working with ollama.com - [PR #17191](https://github.com/BerriAI/litellm/pull/17191)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Fix supports\_response\_schema before using json\_tool\_call workaround - [PR #17438](https://github.com/BerriAI/litellm/pull/17438)
- [**vLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Fix empty response + vLLM streaming - [PR #17516](https://github.com/BerriAI/litellm/pull/17516)
- [**Azure AI**](https://docs.litellm.ai/docs/providers/azure_ai)
  
  - Migrate Anthropic provider to Azure AI - [PR #17202](https://github.com/BerriAI/litellm/pull/17202)
  - Fix GA path for Azure OpenAI realtime models - [PR #17260](https://github.com/BerriAI/litellm/pull/17260)
- [**Bedrock TwelveLabs**](https://docs.litellm.ai/docs/providers/bedrock#twelvelabs-pegasus---video-understanding)
  
  - Add support for TwelveLabs Pegasus video understanding - [PR #17193](https://github.com/BerriAI/litellm/pull/17193)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fix extra\_headers in messages API bedrock invoke - [PR #17271](https://github.com/BerriAI/litellm/pull/17271)
  - Fix Bedrock models in model map - [PR #17419](https://github.com/BerriAI/litellm/pull/17419)
  - Make Bedrock converse messages respect modify\_params as expected - [PR #17427](https://github.com/BerriAI/litellm/pull/17427)
  - Fix Anthropic beta headers for Bedrock imported Qwen models - [PR #17467](https://github.com/BerriAI/litellm/pull/17467)
  - Preserve usage from JSON response for OpenAI provider in Bedrock - [PR #17589](https://github.com/BerriAI/litellm/pull/17589)
- [**SambaNova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Fix acompletion throws error with SambaNova models - [PR #17217](https://github.com/BerriAI/litellm/pull/17217)
- **General**
  
  - Fix AttributeError when metadata is null in request body - [PR #17306](https://github.com/BerriAI/litellm/pull/17306)
  - Fix 500 error for malformed request - [PR #17291](https://github.com/BerriAI/litellm/pull/17291)
  - Respect custom LLM provider in header - [PR #17290](https://github.com/BerriAI/litellm/pull/17290)
  - Replace deprecated .dict() with .model\_dump() in streaming\_handler - [PR #17359](https://github.com/BerriAI/litellm/pull/17359)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Add cost tracking for responses API - [PR #17258](https://github.com/BerriAI/litellm/pull/17258)
  - Map output\_tokens\_details of responses API to completion\_tokens\_details - [PR #17458](https://github.com/BerriAI/litellm/pull/17458)
  - Add image generation support for Responses API - [PR #16586](https://github.com/BerriAI/litellm/pull/16586)
- [**Batch API**](https://docs.litellm.ai/docs/batches)
  
  - Add vLLM batch+files API support - [PR #15823](https://github.com/BerriAI/litellm/pull/15823)
  - Fix optional parameter default value - [PR #17434](https://github.com/BerriAI/litellm/pull/17434)
  - Add status parameter as optional for FileObject - [PR #17431](https://github.com/BerriAI/litellm/pull/17431)
- [**Video Generation API**](https://docs.litellm.ai/docs/videos)
  
  - Add passthrough cost tracking for Veo - [PR #17296](https://github.com/BerriAI/litellm/pull/17296)
- [**OCR API**](https://docs.litellm.ai/docs/ocr)
  
  - Add missing OCR and aOCR to CallTypes enum - [PR #17435](https://github.com/BerriAI/litellm/pull/17435)
- **General**
  
  - Support routing to only websearch supported deployments - [PR #17500](https://github.com/BerriAI/litellm/pull/17500)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Fix streaming error validation - [PR #17242](https://github.com/BerriAI/litellm/pull/17242)
  - Add length validation for empty tool\_calls in delta - [PR #17523](https://github.com/BerriAI/litellm/pull/17523)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **New Login Page**
  
  - New Login Page UI - [PR #17443](https://github.com/BerriAI/litellm/pull/17443)
  - Refactor /login route - [PR #17379](https://github.com/BerriAI/litellm/pull/17379)
  - Add auto\_redirect\_to\_sso to UI Config - [PR #17399](https://github.com/BerriAI/litellm/pull/17399)
  - Add Auto Redirect to SSO to New Login Page - [PR #17451](https://github.com/BerriAI/litellm/pull/17451)
- **Customer (End User) Usage**
  
  - Customer (end user) Usage feature - [PR #17498](https://github.com/BerriAI/litellm/pull/17498)
  - Customer Usage UI - [PR #17506](https://github.com/BerriAI/litellm/pull/17506)
  - Add Info Banner for Customer Usage - [PR #17598](https://github.com/BerriAI/litellm/pull/17598)
- **Virtual Keys**
  
  - Standardize API Key vs Virtual Key in UI - [PR #17325](https://github.com/BerriAI/litellm/pull/17325)
  - Add User Alias Column to Internal User Table - [PR #17321](https://github.com/BerriAI/litellm/pull/17321)
  - Delete Credential Enhancements - [PR #17317](https://github.com/BerriAI/litellm/pull/17317)
- **Models + Endpoints**
  
  - Show all credential values on Edit Credential Modal - [PR #17397](https://github.com/BerriAI/litellm/pull/17397)
  - Change Edit Team Models Shown to Match Create Team - [PR #17394](https://github.com/BerriAI/litellm/pull/17394)
  - Support Images in Compare UI - [PR #17562](https://github.com/BerriAI/litellm/pull/17562)
- **Callbacks**
  
  - Show all callbacks on UI - [PR #16335](https://github.com/BerriAI/litellm/pull/16335)
  - Credentials to use React Query - [PR #17465](https://github.com/BerriAI/litellm/pull/17465)
- **Management Routes**
  
  - Allow admin viewer to access global tag usage - [PR #17501](https://github.com/BerriAI/litellm/pull/17501)
  - Allow wildcard routes for nonproxy admin (SCIM) - [PR #17178](https://github.com/BerriAI/litellm/pull/17178)
  - Return 404 when a user is not found on /user/info - [PR #16850](https://github.com/BerriAI/litellm/pull/16850)
- **OCI Configuration**
  
  - Enable Oracle Cloud Infrastructure configuration via UI - [PR #17159](https://github.com/BerriAI/litellm/pull/17159)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **UI Fixes**
  
  - Fix Request and Response Panel JSONViewer - [PR #17233](https://github.com/BerriAI/litellm/pull/17233)
  - Adding Button Loading States to Edit Settings - [PR #17236](https://github.com/BerriAI/litellm/pull/17236)
  - Fix Various Text, button state, and test changes - [PR #17237](https://github.com/BerriAI/litellm/pull/17237)
  - Fix Fallbacks Immediately Deleting before API resolves - [PR #17238](https://github.com/BerriAI/litellm/pull/17238)
  - Remove Feature Flags - [PR #17240](https://github.com/BerriAI/litellm/pull/17240)
  - Fix metadata tags and model name display in UI for Azure passthrough - [PR #17258](https://github.com/BerriAI/litellm/pull/17258)
  - Change labeling around Vertex Fields - [PR #17383](https://github.com/BerriAI/litellm/pull/17383)
  - Remove second scrollbar when sidebar is expanded + tooltip z index - [PR #17436](https://github.com/BerriAI/litellm/pull/17436)
  - Fix Select in Edit Membership Modal - [PR #17524](https://github.com/BerriAI/litellm/pull/17524)
  - Change useAuthorized Hook to redirect to new Login Page - [PR #17553](https://github.com/BerriAI/litellm/pull/17553)
- **SSO**
  
  - Fix the generic SSO provider - [PR #17227](https://github.com/BerriAI/litellm/pull/17227)
  - Clear SSO integration for all users - [PR #17287](https://github.com/BerriAI/litellm/pull/17287)
  - Fix SSO users not added to Entra synced team - [PR #17331](https://github.com/BerriAI/litellm/pull/17331)
- **Auth / JWT**
  
  - JWT Auth - Allow using regular OIDC flow with user info endpoints - [PR #17324](https://github.com/BerriAI/litellm/pull/17324)
  - Fix litellm user auth not passing issue - [PR #17342](https://github.com/BerriAI/litellm/pull/17342)
  - Add other routes in JWT auth - [PR #17345](https://github.com/BerriAI/litellm/pull/17345)
  - Fix new org team validate against org - [PR #17333](https://github.com/BerriAI/litellm/pull/17333)
  - Fix litellm\_enterprise ensure imported routes exist - [PR #17337](https://github.com/BerriAI/litellm/pull/17337)
  - Use organization.members instead of deprecated organization field - [PR #17557](https://github.com/BerriAI/litellm/pull/17557)
- **Organizations/Teams**
  
  - Fix organization max budget not enforced - [PR #17334](https://github.com/BerriAI/litellm/pull/17334)
  - Fix budget update to allow null max\_budget - [PR #17545](https://github.com/BerriAI/litellm/pull/17545)

* * *

## AI Integrations (2 new integrations)[​](#ai-integrations-2-new-integrations "Direct link to AI Integrations (2 new integrations)")

### Logging (1 new integration)[​](#logging-1-new-integration "Direct link to Logging (1 new integration)")

#### New Integration[​](#new-integration "Direct link to New Integration")

- [**Weave**](https://docs.litellm.ai/docs/proxy/logging)
  
  - Basic Weave OTEL integration - [PR #17439](https://github.com/BerriAI/litellm/pull/17439)

#### Improvements & Fixes[​](#improvements--fixes "Direct link to Improvements & Fixes")

- [**DataDog**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Fix Datadog callback regression when ddtrace is installed - [PR #17393](https://github.com/BerriAI/litellm/pull/17393)
- [**Arize Phoenix**](https://docs.litellm.ai/docs/observability/arize_integration)
  
  - Fix clean arize-phoenix traces - [PR #16611](https://github.com/BerriAI/litellm/pull/16611)
- [**MLflow**](https://docs.litellm.ai/docs/proxy/logging#mlflow)
  
  - Fix MLflow streaming spans for Anthropic passthrough - [PR #17288](https://github.com/BerriAI/litellm/pull/17288)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Fix Langfuse logger test mock setup - [PR #17591](https://github.com/BerriAI/litellm/pull/17591)
- **General**
  
  - Improve PII anonymization handling in logging callbacks - [PR #17207](https://github.com/BerriAI/litellm/pull/17207)

### Guardrails (1 new integration)[​](#guardrails-1-new-integration "Direct link to Guardrails (1 new integration)")

#### New Integration[​](#new-integration-1 "Direct link to New Integration")

- [**Generic Guardrail API**](https://docs.litellm.ai/docs/adding_provider/generic_guardrail_api)
  
  - Generic Guardrail API - allows guardrail providers to add INSTANT support for LiteLLM w/out PR to repo - [PR #17175](https://github.com/BerriAI/litellm/pull/17175)
  - Guardrails API V2 - user api key metadata, session id, specify input type (request/response), image support - [PR #17338](https://github.com/BerriAI/litellm/pull/17338)
  - Guardrails API - add streaming support - [PR #17400](https://github.com/BerriAI/litellm/pull/17400)
  - Guardrails API - support tool call checks on OpenAI `/chat/completions`, OpenAI `/responses`, Anthropic `/v1/messages` - [PR #17459](https://github.com/BerriAI/litellm/pull/17459)
  - Guardrails API - new `structured_messages` param - [PR #17518](https://github.com/BerriAI/litellm/pull/17518)
  - Correctly map a v1/messages call to the anthropic unified guardrail - [PR #17424](https://github.com/BerriAI/litellm/pull/17424)
  - Support during\_call event type for unified guardrails - [PR #17514](https://github.com/BerriAI/litellm/pull/17514)

#### Improvements & Fixes[​](#improvements--fixes-1 "Direct link to Improvements & Fixes")

- [**Noma Guardrail**](https://docs.litellm.ai/docs/proxy/guardrails/noma_security)
  
  - Refactor Noma guardrail to use shared Responses transformation and include system instructions - [PR #17315](https://github.com/BerriAI/litellm/pull/17315)
- [**Presidio**](https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2)
  
  - Handle empty content and error dict responses in guardrails - [PR #17489](https://github.com/BerriAI/litellm/pull/17489)
  - Fix Presidio guardrail test TypeError and license base64 decoding error - [PR #17538](https://github.com/BerriAI/litellm/pull/17538)
- [**Tool Permissions**](https://docs.litellm.ai/docs/proxy/guardrails/tool_permission)
  
  - Add regex-based tool\_name/tool\_type matching for tool-permission - [PR #17164](https://github.com/BerriAI/litellm/pull/17164)
  - Add images for tool permission guardrail documentation - [PR #17322](https://github.com/BerriAI/litellm/pull/17322)
- [**AIM Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/aim_security)
  
  - Fix AIM guardrail tests - [PR #17499](https://github.com/BerriAI/litellm/pull/17499)
- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/bedrock)
  
  - Fix Bedrock Guardrail indent and import - [PR #17378](https://github.com/BerriAI/litellm/pull/17378)
- **General Guardrails**
  
  - Mask all matching keywords in content filter - [PR #17521](https://github.com/BerriAI/litellm/pull/17521)
  - Ensure guardrail metadata is preserved in request\_data - [PR #17593](https://github.com/BerriAI/litellm/pull/17593)
  - Fix apply\_guardrail method and improve test isolation - [PR #17555](https://github.com/BerriAI/litellm/pull/17555)

### Secret Managers[​](#secret-managers "Direct link to Secret Managers")

- [**CyberArk**](https://docs.litellm.ai/docs/secret_managers/cyberark)
  
  - Allow setting SSL verify to false - [PR #17433](https://github.com/BerriAI/litellm/pull/17433)
- **General**
  
  - Make email and secret manager operations independent in key management hooks - [PR #17551](https://github.com/BerriAI/litellm/pull/17551)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Rate Limiting**
  
  - Parallel Request Limiter with /messages - [PR #17426](https://github.com/BerriAI/litellm/pull/17426)
  - Allow using dynamic rate limit/priority reservation on teams - [PR #17061](https://github.com/BerriAI/litellm/pull/17061)
  - Dynamic Rate Limiter - Fix token count increases/decreases by 1 instead of actual count + Redis TTL - [PR #17558](https://github.com/BerriAI/litellm/pull/17558)
- **Spend Logs**
  
  - Deprecate `spend/logs` & add `spend/logs/v2` - [PR #17167](https://github.com/BerriAI/litellm/pull/17167)
  - Optimize SpendLogs queries to use timestamp filtering for index usage - [PR #17504](https://github.com/BerriAI/litellm/pull/17504)
- **Enforce User Param**
  
  - Enforce support of enforce\_user\_param to OpenAI post endpoints - [PR #17407](https://github.com/BerriAI/litellm/pull/17407)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **MCP Configuration**
  
  - Remove URL format validation for MCP server endpoints - [PR #17270](https://github.com/BerriAI/litellm/pull/17270)
  - Add stack trace to MCP error message - [PR #17269](https://github.com/BerriAI/litellm/pull/17269)
- **MCP Tool Results**
  
  - Preserve tool metadata in CallToolResult - [PR #17561](https://github.com/BerriAI/litellm/pull/17561)

* * *

## Agent Gateway (A2A)[​](#agent-gateway-a2a-1 "Direct link to Agent Gateway (A2A)")

- **Agent Invocation**
  
  - Allow invoking agents through AI Gateway - [PR #17440](https://github.com/BerriAI/litellm/pull/17440)
  - Allow tracking request/response in "Logs" Page - [PR #17449](https://github.com/BerriAI/litellm/pull/17449)
- **Agent Access Control**
  
  - Enforce Allowed agents by key, team + add agent access groups on backend - [PR #17502](https://github.com/BerriAI/litellm/pull/17502)
- **Agent Gateway UI**
  
  - Allow testing agents on UI - [PR #17455](https://github.com/BerriAI/litellm/pull/17455)
  - Set allowed agents by key, team - [PR #17511](https://github.com/BerriAI/litellm/pull/17511)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Audio/Speech Performance**
  
  - Fix `/audio/speech` performance by using `shared_sessions` - [PR #16739](https://github.com/BerriAI/litellm/pull/16739)
- **Memory Optimization**
  
  - Prevent memory leak in aiohttp connection pooling - [PR #17388](https://github.com/BerriAI/litellm/pull/17388)
  - Lazy-load utils to reduce memory + import time - [PR #17171](https://github.com/BerriAI/litellm/pull/17171)
- **Database**
  
  - Update default database connection number - [PR #17353](https://github.com/BerriAI/litellm/pull/17353)
  - Update default proxy\_batch\_write\_at number - [PR #17355](https://github.com/BerriAI/litellm/pull/17355)
  - Add background health checks to db - [PR #17528](https://github.com/BerriAI/litellm/pull/17528)
- **Proxy Caching**
  
  - Fix proxy caching between requests in aiohttp transport - [PR #17122](https://github.com/BerriAI/litellm/pull/17122)
- **Session Management**
  
  - Fix session consistency, move Lasso API version away from source code - [PR #17316](https://github.com/BerriAI/litellm/pull/17316)
  - Conditionally pass enable\_cleanup\_closed to aiohttp TCPConnector - [PR #17367](https://github.com/BerriAI/litellm/pull/17367)
- **Vector Store**
  
  - Fix vector store configuration synchronization failure - [PR #17525](https://github.com/BerriAI/litellm/pull/17525)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Add Azure AI Foundry documentation for Claude models - [PR #17104](https://github.com/BerriAI/litellm/pull/17104)
  - Document responses and embedding API for GitHub Copilot - [PR #17456](https://github.com/BerriAI/litellm/pull/17456)
  - Add gpt-5.1-codex-max to OpenAI provider documentation - [PR #17602](https://github.com/BerriAI/litellm/pull/17602)
  - Update Instructions For Phoenix Integration - [PR #17373](https://github.com/BerriAI/litellm/pull/17373)
- **Guides**
  
  - Add guide on how to debug gateway error vs provider error - [PR #17387](https://github.com/BerriAI/litellm/pull/17387)
  - Agent Gateway documentation - [PR #17454](https://github.com/BerriAI/litellm/pull/17454)
  - A2A Permission management documentation - [PR #17515](https://github.com/BerriAI/litellm/pull/17515)
  - Update docs to link agent hub - [PR #17462](https://github.com/BerriAI/litellm/pull/17462)
- **Projects**
  
  - Add Google ADK and Harbor to projects - [PR #17352](https://github.com/BerriAI/litellm/pull/17352)
  - Add Microsoft Agent Lightning to projects - [PR #17422](https://github.com/BerriAI/litellm/pull/17422)
- **Cleanup**
  
  - Cleanup: Remove orphan docs pages and Docusaurus template files - [PR #17356](https://github.com/BerriAI/litellm/pull/17356)
  - Remove `source .env` from docs - [PR #17466](https://github.com/BerriAI/litellm/pull/17466)

* * *

## Infrastructure / CI/CD[​](#infrastructure--cicd "Direct link to Infrastructure / CI/CD")

- **Helm Chart**
  
  - Add ingress-only labels - [PR #17348](https://github.com/BerriAI/litellm/pull/17348)
- **Docker**
  
  - Add retry logic to apk package installation in Dockerfile.non\_root - [PR #17596](https://github.com/BerriAI/litellm/pull/17596)
  - Chainguard fixes - [PR #17406](https://github.com/BerriAI/litellm/pull/17406)
- **OpenAPI Schema**
  
  - Refactor add\_schema\_to\_components to move definitions to components/schemas - [PR #17389](https://github.com/BerriAI/litellm/pull/17389)
- **Security**
  
  - Fix security vulnerability: update mdast-util-to-hast to 13.2.1 - [PR #17601](https://github.com/BerriAI/litellm/pull/17601)
  - Bump jws from 3.2.2 to 3.2.3 - [PR #17494](https://github.com/BerriAI/litellm/pull/17494)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @weichiet made their first contribution in [PR #17242](https://github.com/BerriAI/litellm/pull/17242)
- @AndyForest made their first contribution in [PR #17220](https://github.com/BerriAI/litellm/pull/17220)
- @omkar806 made their first contribution in [PR #17217](https://github.com/BerriAI/litellm/pull/17217)
- @v0rtex20k made their first contribution in [PR #17178](https://github.com/BerriAI/litellm/pull/17178)
- @hxomer made their first contribution in [PR #17207](https://github.com/BerriAI/litellm/pull/17207)
- @orgersh92 made their first contribution in [PR #17316](https://github.com/BerriAI/litellm/pull/17316)
- @dannykopping made their first contribution in [PR #17313](https://github.com/BerriAI/litellm/pull/17313)
- @rioiart made their first contribution in [PR #17333](https://github.com/BerriAI/litellm/pull/17333)
- @codgician made their first contribution in [PR #17278](https://github.com/BerriAI/litellm/pull/17278)
- @epistoteles made their first contribution in [PR #17277](https://github.com/BerriAI/litellm/pull/17277)
- @kothamah made their first contribution in [PR #17368](https://github.com/BerriAI/litellm/pull/17368)
- @flozonn made their first contribution in [PR #17371](https://github.com/BerriAI/litellm/pull/17371)
- @richardmcsong made their first contribution in [PR #17389](https://github.com/BerriAI/litellm/pull/17389)
- @matt-greathouse made their first contribution in [PR #17384](https://github.com/BerriAI/litellm/pull/17384)
- @mossbanay made their first contribution in [PR #17380](https://github.com/BerriAI/litellm/pull/17380)
- @mhielpos-asapp made their first contribution in [PR #17376](https://github.com/BerriAI/litellm/pull/17376)
- @Joilence made their first contribution in [PR #17367](https://github.com/BerriAI/litellm/pull/17367)
- @deepaktammali made their first contribution in [PR #17357](https://github.com/BerriAI/litellm/pull/17357)
- @axiomofjoy made their first contribution in [PR #16611](https://github.com/BerriAI/litellm/pull/16611)
- @DevajMody made their first contribution in [PR #17445](https://github.com/BerriAI/litellm/pull/17445)
- @andrewtruong made their first contribution in [PR #17439](https://github.com/BerriAI/litellm/pull/17439)
- @AnasAbdelR made their first contribution in [PR #17490](https://github.com/BerriAI/litellm/pull/17490)
- @dominicfeliton made their first contribution in [PR #17516](https://github.com/BerriAI/litellm/pull/17516)
- @kristianmitk made their first contribution in [PR #17504](https://github.com/BerriAI/litellm/pull/17504)
- @rgshr made their first contribution in [PR #17130](https://github.com/BerriAI/litellm/pull/17130)
- @dominicfallows made their first contribution in [PR #17489](https://github.com/BerriAI/litellm/pull/17489)
- @irfansofyana made their first contribution in [PR #17467](https://github.com/BerriAI/litellm/pull/17467)
- @GusBricker made their first contribution in [PR #17191](https://github.com/BerriAI/litellm/pull/17191)
- @OlivverX made their first contribution in [PR #17255](https://github.com/BerriAI/litellm/pull/17255)
- @withsmilo made their first contribution in [PR #17585](https://github.com/BerriAI/litellm/pull/17585)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.80.7-nightly...v1.80.8)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.80.5-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Gemini 3** - [Day-0 support for Gemini 3 models with thought signatures](https://docs.litellm.ai/blog/gemini_3)
- **Prompt Management** - [Full prompt versioning support with UI for editing, testing, and version history](https://docs.litellm.ai/docs/proxy/litellm_prompt_management)
- **MCP Hub** - [Publish and discover MCP servers within your organization](https://docs.litellm.ai/docs/proxy/ai_hub#mcp-servers)
- **Model Compare UI** - [Side-by-side model comparison interface for testing](https://docs.litellm.ai/docs/proxy/model_compare_ui)
- **Batch API Spend Tracking** - [Granular spend tracking with custom metadata for batch and file creation requests](https://docs.litellm.ai/docs/proxy/cost_tracking#-custom-spend-log-metadata)
- **AWS IAM Secret Manager** - [IAM role authentication support for AWS Secret Manager](https://docs.litellm.ai/docs/secret_managers/aws_secret_manager#iam-role-assumption)
- **Logging Callback Controls** - [Admin-level controls to prevent callers from disabling logging callbacks in compliance environments](https://docs.litellm.ai/docs/proxy/dynamic_logging#disabling-dynamic-callback-management-enterprise)
- **Proxy CLI JWT Authentication** - [Enable developers to authenticate to LiteLLM AI Gateway using the Proxy CLI](https://docs.litellm.ai/docs/proxy/cli_sso)
- **Batch API Routing** - [Route batch operations to different provider accounts using model-specific credentials from your config.yaml](https://docs.litellm.ai/docs/batches#multi-account--model-based-routing)

* * *

### Prompt Management[​](#prompt-management "Direct link to Prompt Management")

This release introduces **LiteLLM Prompt Studio** - a comprehensive prompt management solution built directly into the LiteLLM UI. Create, test, and version your prompts without leaving your browser.

You can now do the following on LiteLLM Prompt Studio:

- **Create & Test Prompts**: Build prompts with developer messages (system instructions) and test them in real-time with an interactive chat interface
- **Dynamic Variables**: Use `{{variable_name}}` syntax to create reusable prompt templates with automatic variable detection
- **Version Control**: Automatic versioning for every prompt update with complete version history tracking and rollback capabilities
- **Prompt Studio**: Edit prompts in a dedicated studio environment with live testing and preview

**API Integration:**

Use your prompts in any application with simple API calls:

```
response = client.chat.completions.create(
    model="gpt-4",
    extra_body={
"prompt_id":"your-prompt-id",
"prompt_version":2,# Optional: specify version
"prompt_variables":{"name":"value"}# Optional: pass variables
}
)
```

Get started here: [LiteLLM Prompt Management Documentation](https://docs.litellm.ai/docs/proxy/litellm_prompt_management)

* * *

### Performance – `/realtime` 182× Lower p99 Latency[​](#performance--realtime-182-lower-p99-latency "Direct link to performance--realtime-182-lower-p99-latency")

This update reduces `/realtime` latency by removing redundant encodings on the hot path, reusing shared SSL contexts, and caching formatting strings that were being regenerated twice per request despite rarely changing.

#### Results[​](#results "Direct link to Results")

MetricBeforeAfterImprovementMedian latency2,200 ms**59 ms****−97% (~37× faster)**p95 latency8,500 ms**67 ms****−99% (~127× faster)**p99 latency18,000 ms**99 ms****−99% (~182× faster)**Average latency3,214 ms**63 ms****−98% (~51× faster)**RPS165**1,207****+631% (~7.3× increase)**

#### Test Setup[​](#test-setup "Direct link to Test Setup")

CategorySpecification**Load Testing**Locust: 1,000 concurrent users, 500 ramp-up**System**4 vCPUs, 8 GB RAM, 4 workers, 4 instances**Database**PostgreSQL (Redis unused)**Configuration**[config.yaml](https://gist.github.com/AlexsanderHamir/420fb44c31c00b4f17a99588637f01ec)**Load Script**[no\_cache\_hits.py](https://gist.github.com/AlexsanderHamir/73b83ada21d9b84d4fe09665cf1745f5)

* * *

### Model Compare UI[​](#model-compare-ui "Direct link to Model Compare UI")

New interactive playground UI enables side-by-side comparison of multiple LLM models, making it easy to evaluate and compare model responses.

**Features:**

- Compare responses from multiple models in real-time
- Side-by-side view with synchronized scrolling
- Support for all LiteLLM-supported models
- Cost tracking per model
- Response time comparison
- Pre-configured prompts for quick and easy testing

**Details:**

- **Parameterization**: Configure API keys, endpoints, models, and model parameters, as well as interaction types (chat completions, embeddings, etc.)
- **Model Comparison**: Compare up to 3 different models simultaneously with side-by-side response views
- **Comparison Metrics**: View detailed comparison information including:
  
  - Time To First Token
  - Input / Output / Reasoning Tokens
  - Total Latency
  - Cost (if enabled in config)
- **Safety Filters**: Configure and test guardrails (safety filters) directly in the playground interface

[Get Started with Model Compare](https://docs.litellm.ai/docs/proxy/model_compare_ui)

## New Providers and Endpoints[​](#new-providers-and-endpoints "Direct link to New Providers and Endpoints")

### New Providers[​](#new-providers "Direct link to New Providers")

ProviderSupported EndpointsDescription[**Docker Model Runner**](https://docs.litellm.ai/docs/providers/docker_model_runner)`/v1/chat/completions`Run LLM models in Docker containers

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesAzure`azure/gpt-5.1`272K$1.38$11.00Reasoning, vision, PDF input, responses APIAzure`azure/gpt-5.1-2025-11-13`272K$1.38$11.00Reasoning, vision, PDF input, responses APIAzure`azure/gpt-5.1-codex`272K$1.38$11.00Responses API, reasoning, visionAzure`azure/gpt-5.1-codex-2025-11-13`272K$1.38$11.00Responses API, reasoning, visionAzure`azure/gpt-5.1-codex-mini`272K$0.275$2.20Responses API, reasoning, visionAzure`azure/gpt-5.1-codex-mini-2025-11-13`272K$0.275$2.20Responses API, reasoning, visionAzure EU`azure/eu/gpt-5-2025-08-07`272K$1.375$11.00Reasoning, vision, PDF inputAzure EU`azure/eu/gpt-5-mini-2025-08-07`272K$0.275$2.20Reasoning, vision, PDF inputAzure EU`azure/eu/gpt-5-nano-2025-08-07`272K$0.055$0.44Reasoning, vision, PDF inputAzure EU`azure/eu/gpt-5.1`272K$1.38$11.00Reasoning, vision, PDF input, responses APIAzure EU`azure/eu/gpt-5.1-codex`272K$1.38$11.00Responses API, reasoning, visionAzure EU`azure/eu/gpt-5.1-codex-mini`272K$0.275$2.20Responses API, reasoning, visionGemini`gemini-3-pro-preview`2M$1.25$5.00Reasoning, vision, function callingGemini`gemini-3-pro-image`2M$1.25$5.00Image generation, reasoningOpenRouter`openrouter/deepseek/deepseek-v3p1-terminus`164K$0.20$0.40Function calling, reasoningOpenRouter`openrouter/moonshot/kimi-k2-instruct`262K$0.60$2.50Function calling, web searchOpenRouter`openrouter/gemini/gemini-3-pro-preview`2M$1.25$5.00Reasoning, vision, function callingXAI`xai/grok-4.1-fast`2M$0.20$0.50Reasoning, function callingTogether AI`together_ai/z-ai/glm-4.6`203K$0.40$1.75Function calling, reasoningCerebras`cerebras/gpt-oss-120b`131K$0.60$0.60Function callingBedrock`anthropic.claude-sonnet-4-5-20250929-v1:0`200K$3.00$15.00Computer use, reasoning, vision

#### Features[​](#features "Direct link to Features")

- [**Gemini (Google AI Studio + Vertex AI)**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add Day 0 gemini-3-pro-preview support - [PR #16719](https://github.com/BerriAI/litellm/pull/16719)
  - Add support for Gemini 3 Pro Image model - [PR #16938](https://github.com/BerriAI/litellm/pull/16938)
  - Add reasoning\_content to streaming responses with tools enabled - [PR #16854](https://github.com/BerriAI/litellm/pull/16854)
  - Add includeThoughts=True for Gemini 3 reasoning\_effort - [PR #16838](https://github.com/BerriAI/litellm/pull/16838)
  - Support thought signatures for Gemini 3 in responses API - [PR #16872](https://github.com/BerriAI/litellm/pull/16872)
  - Correct wrong system message handling for gemma - [PR #16767](https://github.com/BerriAI/litellm/pull/16767)
  - Gemini 3 Pro Image: capture image\_tokens and support cost\_per\_output\_image - [PR #16912](https://github.com/BerriAI/litellm/pull/16912)
  - Fix missing costs for gemini-2.5-flash-image - [PR #16882](https://github.com/BerriAI/litellm/pull/16882)
  - Gemini 3 thought signatures in tool call id - [PR #16895](https://github.com/BerriAI/litellm/pull/16895)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Add azure gpt-5.1 models - [PR #16817](https://github.com/BerriAI/litellm/pull/16817)
  - Add Azure models 2025 11 to cost maps - [PR #16762](https://github.com/BerriAI/litellm/pull/16762)
  - Update Azure Pricing - [PR #16371](https://github.com/BerriAI/litellm/pull/16371)
  - Add SSML Support for Azure Text-to-Speech (AVA) - [PR #16747](https://github.com/BerriAI/litellm/pull/16747)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Support GPT-5.1 reasoning.effort='none' in proxy - [PR #16745](https://github.com/BerriAI/litellm/pull/16745)
  - Add gpt-5.1-codex and gpt-5.1-codex-mini models to documentation - [PR #16735](https://github.com/BerriAI/litellm/pull/16735)
  - Inherit BaseVideoConfig to enable async content response for OpenAI video - [PR #16708](https://github.com/BerriAI/litellm/pull/16708)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Add support for `strict` parameter in Anthropic tool schemas - [PR #16725](https://github.com/BerriAI/litellm/pull/16725)
  - Add image as url support to anthropic - [PR #16868](https://github.com/BerriAI/litellm/pull/16868)
  - Add thought signature support to v1/messages api - [PR #16812](https://github.com/BerriAI/litellm/pull/16812)
  - Anthropic - support Structured Outputs `output_format` for Claude 4.5 sonnet and Opus 4.1 - [PR #16949](https://github.com/BerriAI/litellm/pull/16949)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Haiku 4.5 correct Bedrock configs - [PR #16732](https://github.com/BerriAI/litellm/pull/16732)
  - Ensure consistent chunk IDs in Bedrock streaming responses - [PR #16596](https://github.com/BerriAI/litellm/pull/16596)
  - Add Claude 4.5 to US Gov Cloud - [PR #16957](https://github.com/BerriAI/litellm/pull/16957)
  - Fix images being dropped from tool results for bedrock - [PR #16492](https://github.com/BerriAI/litellm/pull/16492)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add Vertex AI Image Edit Support - [PR #16828](https://github.com/BerriAI/litellm/pull/16828)
  - Update veo 3 pricing and add prod models - [PR #16781](https://github.com/BerriAI/litellm/pull/16781)
  - Fix Video download for veo3 - [PR #16875](https://github.com/BerriAI/litellm/pull/16875)
- [**Snowflake**](https://docs.litellm.ai/docs/providers/snowflake)
  
  - Snowflake provider support: added embeddings, PAT, account\_id - [PR #15727](https://github.com/BerriAI/litellm/pull/15727)
- [**OCI**](https://docs.litellm.ai/docs/providers/oci)
  
  - Add oci\_endpoint\_id Parameter for OCI Dedicated Endpoints - [PR #16723](https://github.com/BerriAI/litellm/pull/16723)
- [**XAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - Add support for Grok 4.1 Fast models - [PR #16936](https://github.com/BerriAI/litellm/pull/16936)
- [**Together AI**](https://docs.litellm.ai/docs/providers/togetherai)
  
  - Add GLM 4.6 from together.ai - [PR #16942](https://github.com/BerriAI/litellm/pull/16942)
- [**Cerebras**](https://docs.litellm.ai/docs/providers/cerebras)
  
  - Fix Cerebras GPT-OSS-120B model name - [PR #16939](https://github.com/BerriAI/litellm/pull/16939)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Fix for 16863 - openai conversion from responses to completions - [PR #16864](https://github.com/BerriAI/litellm/pull/16864)
  - Revert "Make all gpt-5 and reasoning models to responses by default" - [PR #16849](https://github.com/BerriAI/litellm/pull/16849)
- **General**
  
  - Get custom\_llm\_provider from query param - [PR #16731](https://github.com/BerriAI/litellm/pull/16731)
  - Fix optional param mapping - [PR #16852](https://github.com/BerriAI/litellm/pull/16852)
  - Add None check for litellm\_params - [PR #16754](https://github.com/BerriAI/litellm/pull/16754)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Add Responses API support for gpt-5.1-codex model - [PR #16845](https://github.com/BerriAI/litellm/pull/16845)
  - Add managed files support for responses API - [PR #16733](https://github.com/BerriAI/litellm/pull/16733)
  - Add extra\_body support for response supported api params from chat completion - [PR #16765](https://github.com/BerriAI/litellm/pull/16765)
- [**Batch API**](https://docs.litellm.ai/docs/batches)
  
  - Support /delete for files + support /cancel for batches - [PR #16387](https://github.com/BerriAI/litellm/pull/16387)
  - Add config based routing support for batches and files - [PR #16872](https://github.com/BerriAI/litellm/pull/16872)
  - Populate spend\_logs\_metadata in batch and files endpoints - [PR #16921](https://github.com/BerriAI/litellm/pull/16921)
- [**Search APIs**](https://docs.litellm.ai/docs/search)
  
  - Search APIs - error in firecrawl-search "Invalid request body" - [PR #16943](https://github.com/BerriAI/litellm/pull/16943)
- [**Vector Stores**](https://docs.litellm.ai/docs/vector_stores)
  
  - Fix vector store create issue - [PR #16804](https://github.com/BerriAI/litellm/pull/16804)
  - Team vector-store permissions now respected for key access - [PR #16639](https://github.com/BerriAI/litellm/pull/16639)
- [**Audio Transcription**](https://docs.litellm.ai/docs/audio_transcription)
  
  - Fix audio transcription cost tracking - [PR #16478](https://github.com/BerriAI/litellm/pull/16478)
  - Add missing shared\_sessions to audio/transcriptions - [PR #16858](https://github.com/BerriAI/litellm/pull/16858)
- [**Video Generation API**](https://docs.litellm.ai/docs/video_generation)
  
  - Fix videos tagging - [PR #16770](https://github.com/BerriAI/litellm/pull/16770)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Responses API cost tracking with custom deployment names - [PR #16778](https://github.com/BerriAI/litellm/pull/16778)
  - Trim logged response strings in spend-logs - [PR #16654](https://github.com/BerriAI/litellm/pull/16654)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Proxy CLI Auth**
  
  - Allow using JWTs for signing in with Proxy CLI - [PR #16756](https://github.com/BerriAI/litellm/pull/16756)
- **Virtual Keys**
  
  - Fix Key Model Alias Not Working - [PR #16896](https://github.com/BerriAI/litellm/pull/16896)
- **Models + Endpoints**
  
  - Add additional model settings to chat models in test key - [PR #16793](https://github.com/BerriAI/litellm/pull/16793)
  - Deactivate delete button on model table for config models - [PR #16787](https://github.com/BerriAI/litellm/pull/16787)
  - Change Public Model Hub to use proxyBaseUrl - [PR #16892](https://github.com/BerriAI/litellm/pull/16892)
  - Add JSON Viewer to request/response panel - [PR #16687](https://github.com/BerriAI/litellm/pull/16687)
  - Standarize icon images - [PR #16837](https://github.com/BerriAI/litellm/pull/16837)
- **Teams**
  
  - Teams table empty state - [PR #16738](https://github.com/BerriAI/litellm/pull/16738)
- **Fallbacks**
  
  - Fallbacks icon button tooltips and delete with friction - [PR #16737](https://github.com/BerriAI/litellm/pull/16737)
- **MCP Servers**
  
  - Delete user and MCP Server Modal, MCP Table Tooltips - [PR #16751](https://github.com/BerriAI/litellm/pull/16751)
- **Callbacks**
  
  - Expose backend endpoint for callbacks settings - [PR #16698](https://github.com/BerriAI/litellm/pull/16698)
  - Edit add callbacks route to use data from backend - [PR #16699](https://github.com/BerriAI/litellm/pull/16699)
- **Usage & Analytics**
  
  - Allow partial matches for user ID in User Table - [PR #16952](https://github.com/BerriAI/litellm/pull/16952)
- **General UI**
  
  - Allow setting base\_url in API reference docs - [PR #16674](https://github.com/BerriAI/litellm/pull/16674)
  - Change /public fields to honor server root path - [PR #16930](https://github.com/BerriAI/litellm/pull/16930)
  - Correct ui build - [PR #16702](https://github.com/BerriAI/litellm/pull/16702)
  - Enable automatic dark/light mode based on system preference - [PR #16748](https://github.com/BerriAI/litellm/pull/16748)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **UI Fixes**
  
  - Fix flaky tests due to antd Notification Manager - [PR #16740](https://github.com/BerriAI/litellm/pull/16740)
  - Fix UI MCP Tool Test Regression - [PR #16695](https://github.com/BerriAI/litellm/pull/16695)
  - Fix edit logging settings not appearing - [PR #16798](https://github.com/BerriAI/litellm/pull/16798)
  - Add css to truncate long request ids in request viewer - [PR #16665](https://github.com/BerriAI/litellm/pull/16665)
  - Remove azure/ prefix in Placeholder for Azure in Add Model - [PR #16597](https://github.com/BerriAI/litellm/pull/16597)
  - Remove UI Session Token from user/info return - [PR #16851](https://github.com/BerriAI/litellm/pull/16851)
  - Remove console logs and errors from model tab - [PR #16455](https://github.com/BerriAI/litellm/pull/16455)
  - Change Bulk Invite User Roles to Match Backend - [PR #16906](https://github.com/BerriAI/litellm/pull/16906)
  - Mock Tremor's Tooltip to Fix Flaky UI Tests - [PR #16786](https://github.com/BerriAI/litellm/pull/16786)
  - Fix e2e ui playwright test - [PR #16799](https://github.com/BerriAI/litellm/pull/16799)
  - Fix Tests in CI/CD - [PR #16972](https://github.com/BerriAI/litellm/pull/16972)
- **SSO**
  
  - Ensure `role` from SSO provider is used when a user is inserted onto LiteLLM - [PR #16794](https://github.com/BerriAI/litellm/pull/16794)
  - Docs - SSO - Manage User Roles via Azure App Roles - [PR #16796](https://github.com/BerriAI/litellm/pull/16796)
- **Auth**
  
  - Ensure Team Tags works when using JWT Auth - [PR #16797](https://github.com/BerriAI/litellm/pull/16797)
  - Fix key never expires - [PR #16692](https://github.com/BerriAI/litellm/pull/16692)
- **Swagger UI**
  
  - Fixes Swagger UI resolver errors for chat completion endpoints caused by Pydantic v2 `$defs` not being properly exposed in the OpenAPI schema - [PR #16784](https://github.com/BerriAI/litellm/pull/16784)

* * *

## AI Integrations[​](#ai-integrations "Direct link to AI Integrations")

### Logging[​](#logging "Direct link to Logging")

- [**Arize Phoenix**](https://docs.litellm.ai/docs/observability/arize_phoenix)
  
  - Fix arize phoenix logging - [PR #16301](https://github.com/BerriAI/litellm/pull/16301)
  - Arize Phoenix - root span logging - [PR #16949](https://github.com/BerriAI/litellm/pull/16949)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Filter secret fields form Langfuse - [PR #16842](https://github.com/BerriAI/litellm/pull/16842)
- **General**
  
  - Exclude litellm\_credential\_name from Sensitive Data Masker (Updated) - [PR #16958](https://github.com/BerriAI/litellm/pull/16958)
  - Allow admins to disable, dynamic callback controls - [PR #16750](https://github.com/BerriAI/litellm/pull/16750)

### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**IBM Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Fix IBM Guardrails optional params, add extra\_headers field - [PR #16771](https://github.com/BerriAI/litellm/pull/16771)
- [**Noma Guardrail**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Use LiteLLM key alias as fallback Noma applicationId in NomaGuardrail - [PR #16832](https://github.com/BerriAI/litellm/pull/16832)
  - Allow custom violation message for tool-permission guardrail - [PR #16916](https://github.com/BerriAI/litellm/pull/16916)
- [**Grayswan Guardrail**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Grayswan guardrail passthrough on flagged - [PR #16891](https://github.com/BerriAI/litellm/pull/16891)
- **General Guardrails**
  
  - Fix prompt injection not working - [PR #16701](https://github.com/BerriAI/litellm/pull/16701)

### Prompt Management[​](#prompt-management-1 "Direct link to Prompt Management")

- [**Prompt Management**](https://docs.litellm.ai/docs/proxy/prompt_management)
  
  - Allow specifying just prompt\_id in a request to a model - [PR #16834](https://github.com/BerriAI/litellm/pull/16834)
  - Add support for versioning prompts - [PR #16836](https://github.com/BerriAI/litellm/pull/16836)
  - Allow storing prompt version in DB - [PR #16848](https://github.com/BerriAI/litellm/pull/16848)
  - Add UI for editing the prompts - [PR #16853](https://github.com/BerriAI/litellm/pull/16853)
  - Allow testing prompts with Chat UI - [PR #16898](https://github.com/BerriAI/litellm/pull/16898)
  - Allow viewing version history - [PR #16901](https://github.com/BerriAI/litellm/pull/16901)
  - Allow specifying prompt version in code - [PR #16929](https://github.com/BerriAI/litellm/pull/16929)
  - UI, allow seeing model, prompt id for Prompt - [PR #16932](https://github.com/BerriAI/litellm/pull/16932)
  - Show "get code" section for prompt management + minor polish of showing version history - [PR #16941](https://github.com/BerriAI/litellm/pull/16941)

### Secret Managers[​](#secret-managers "Direct link to Secret Managers")

- [**AWS Secrets Manager**](https://docs.litellm.ai/docs/secret_managers)
  
  - Adds IAM role assumption support for AWS Secret Manager - [PR #16887](https://github.com/BerriAI/litellm/pull/16887)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **MCP Hub** - Publish/discover MCP Servers within a company - [PR #16857](https://github.com/BerriAI/litellm/pull/16857)
- **MCP Resources** - MCP resources support - [PR #16800](https://github.com/BerriAI/litellm/pull/16800)
- **MCP OAuth** - Docs - mcp oauth flow details - [PR #16742](https://github.com/BerriAI/litellm/pull/16742)
- **MCP Lifecycle** - Drop MCPClient.connect and use run\_with\_session lifecycle - [PR #16696](https://github.com/BerriAI/litellm/pull/16696)
- **MCP Server IDs** - Add mcp server ids - [PR #16904](https://github.com/BerriAI/litellm/pull/16904)
- **MCP URL Format** - Fix mcp url format - [PR #16940](https://github.com/BerriAI/litellm/pull/16940)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Realtime Endpoint Performance** - Fix bottlenecks degrading realtime endpoint performance - [PR #16670](https://github.com/BerriAI/litellm/pull/16670)
- **SSL Context Caching** - Cache SSL contexts to prevent excessive memory allocation - [PR #16955](https://github.com/BerriAI/litellm/pull/16955)
- **Cache Optimization** - Fix cache cooldown key generation - [PR #16954](https://github.com/BerriAI/litellm/pull/16954)
- **Router Cache** - Fix routing for requests with same cacheable prefix but different user messages - [PR #16951](https://github.com/BerriAI/litellm/pull/16951)
- **Redis Event Loop** - Fix redis event loop closed at first call - [PR #16913](https://github.com/BerriAI/litellm/pull/16913)
- **Dependency Management** - Upgrade pydantic to version 2.11.0 - [PR #16909](https://github.com/BerriAI/litellm/pull/16909)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Add missing details to benchmark comparison - [PR #16690](https://github.com/BerriAI/litellm/pull/16690)
  - Fix anthropic pass-through endpoint - [PR #16883](https://github.com/BerriAI/litellm/pull/16883)
  - Cleanup repo and improve AI docs - [PR #16775](https://github.com/BerriAI/litellm/pull/16775)
- **API Documentation**
  
  - Add docs related to openai metadata - [PR #16872](https://github.com/BerriAI/litellm/pull/16872)
  - Update docs with all supported endpoints and cost tracking - [PR #16872](https://github.com/BerriAI/litellm/pull/16872)
- **General Documentation**
  
  - Add mini-swe-agent to Projects built on LiteLLM - [PR #16971](https://github.com/BerriAI/litellm/pull/16971)

* * *

## Infrastructure / CI/CD[​](#infrastructure--cicd "Direct link to Infrastructure / CI/CD")

- **UI Testing**
  
  - Break e2e\_ui\_testing into build, unit, and e2e steps - [PR #16783](https://github.com/BerriAI/litellm/pull/16783)
  - Building UI for Testing - [PR #16968](https://github.com/BerriAI/litellm/pull/16968)
  - CI/CD Fixes - [PR #16937](https://github.com/BerriAI/litellm/pull/16937)
- **Dependency Management**
  
  - Bump js-yaml from 3.14.1 to 3.14.2 in /tests/proxy\_admin\_ui\_tests/ui\_unit\_tests - [PR #16755](https://github.com/BerriAI/litellm/pull/16755)
  - Bump js-yaml from 3.14.1 to 3.14.2 - [PR #16802](https://github.com/BerriAI/litellm/pull/16802)
- **Migration**
  
  - Migration job labels - [PR #16831](https://github.com/BerriAI/litellm/pull/16831)
- **Config**
  
  - This yaml actually works - [PR #16757](https://github.com/BerriAI/litellm/pull/16757)
- **Release Notes**
  
  - Add perf improvements on embeddings to release notes - [PR #16697](https://github.com/BerriAI/litellm/pull/16697)
  - Docs - v1.80.0 - [PR #16694](https://github.com/BerriAI/litellm/pull/16694)
- **Investigation**
  
  - Investigate issue root cause - [PR #16859](https://github.com/BerriAI/litellm/pull/16859)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @mattmorgis made their first contribution in [PR #16371](https://github.com/BerriAI/litellm/pull/16371)
- @mmandic-coatue made their first contribution in [PR #16732](https://github.com/BerriAI/litellm/pull/16732)
- @Bradley-Butcher made their first contribution in [PR #16725](https://github.com/BerriAI/litellm/pull/16725)
- @BenjaminLevy made their first contribution in [PR #16757](https://github.com/BerriAI/litellm/pull/16757)
- @CatBraaain made their first contribution in [PR #16767](https://github.com/BerriAI/litellm/pull/16767)
- @tushar8408 made their first contribution in [PR #16831](https://github.com/BerriAI/litellm/pull/16831)
- @nbsp1221 made their first contribution in [PR #16845](https://github.com/BerriAI/litellm/pull/16845)
- @idola9 made their first contribution in [PR #16832](https://github.com/BerriAI/litellm/pull/16832)
- @nkukard made their first contribution in [PR #16864](https://github.com/BerriAI/litellm/pull/16864)
- @alhuang10 made their first contribution in [PR #16852](https://github.com/BerriAI/litellm/pull/16852)
- @sebslight made their first contribution in [PR #16838](https://github.com/BerriAI/litellm/pull/16838)
- @TsurumaruTsuyoshi made their first contribution in [PR #16905](https://github.com/BerriAI/litellm/pull/16905)
- @cyberjunk made their first contribution in [PR #16492](https://github.com/BerriAI/litellm/pull/16492)
- @colinlin-stripe made their first contribution in [PR #16895](https://github.com/BerriAI/litellm/pull/16895)
- @sureshdsk made their first contribution in [PR #16883](https://github.com/BerriAI/litellm/pull/16883)
- @eiliyaabedini made their first contribution in [PR #16875](https://github.com/BerriAI/litellm/pull/16875)
- @justin-tahara made their first contribution in [PR #16957](https://github.com/BerriAI/litellm/pull/16957)
- @wangsoft made their first contribution in [PR #16913](https://github.com/BerriAI/litellm/pull/16913)
- @dsduenas made their first contribution in [PR #16891](https://github.com/BerriAI/litellm/pull/16891)

* * *

## Known Issues[​](#known-issues "Direct link to Known Issues")

- `/audit` and `/user/available_users` routes return 404. Fixed in [PR #17337](https://github.com/BerriAI/litellm/pull/17337)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.80.0-nightly...v1.80.5.rc.2)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.80.0-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **🆕 Agent Hub Support** - Register and make agents public for your organization
- **RunwayML Provider** - Complete video generation, image generation, and text-to-speech support
- **GPT-5.1 Family Support** - Day-0 support for OpenAI's latest GPT-5.1 and GPT-5.1-Codex models
- **Prometheus OSS** - Prometheus metrics now available in open-source version
- **Vector Store Files API** - Complete OpenAI-compatible Vector Store Files API with full CRUD operations
- **Embeddings Performance** - O(1) lookup optimization for router embeddings with shared sessions

* * *

### Agent Hub[​](#agent-hub "Direct link to Agent Hub")

This release adds support for registering and making agents public for your organization. This is great for **Proxy Admins** who want a central place to make agents built in their organization, discoverable to their users.

Here's the flow:

1. Add agent to litellm.
2. Make it public.
3. Allow anyone to discover it on the public AI Hub page.

[**Get Started with Agent Hub**](https://docs.litellm.ai/docs/proxy/ai_hub)

### Performance – `/embeddings` 13× Lower p95 Latency[​](#performance--embeddings-13-lower-p95-latency "Direct link to performance--embeddings-13-lower-p95-latency")

This update significantly improves `/embeddings` latency by routing it through the same optimized pipeline as `/chat/completions`, benefiting from all previously applied networking optimizations.

### Results[​](#results "Direct link to Results")

MetricBeforeAfterImprovementp95 latency5,700 ms**430 ms**−92% (~13× faster)\*\*p99 latency7,200 ms**780 ms**−89%Average latency844 ms**262 ms**−69%Median latency290 ms**230 ms**−21%RPS1,216.7**1,219.7****+0.25%**

### Test Setup[​](#test-setup "Direct link to Test Setup")

CategorySpecification**Load Testing**Locust: 1,000 concurrent users, 500 ramp-up**System**4 vCPUs, 8 GB RAM, 4 workers, 4 instances**Database**PostgreSQL (Redis unused)**Configuration**[config.yaml](https://gist.github.com/AlexsanderHamir/550791675fd752befcac6a9e44024652)**Load Script**[no\_cache\_hits.py](https://gist.github.com/AlexsanderHamir/99d673bf74cdd81fd39f59fa9048f2e8)

* * *

### 🆕 RunwayML[​](#-runwayml "Direct link to 🆕 RunwayML")

Complete integration for RunwayML's Gen-4 family of models, supporting video generation, image generation, and text-to-speech.

**Supported Endpoints:**

- `/v1/videos` - Video generation (Gen-4 Turbo, Gen-4 Aleph, Gen-3A Turbo)
- `/v1/images/generations` - Image generation (Gen-4 Image, Gen-4 Image Turbo)
- `/v1/audio/speech` - Text-to-speech (ElevenLabs Multilingual v2)

**Quick Start:**

Generate Video with RunwayML

```
curl --location 'http://localhost:4000/v1/videos' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-1234' \
--data '{
    "model": "runwayml/gen4_turbo",
    "prompt": "A high quality demo video of litellm ai gateway",
    "input_reference": "https://example.com/image.jpg",
    "seconds": 5,
    "size": "1280x720"
}'
```

[Get Started with RunwayML](https://docs.litellm.ai/docs/providers/runwayml/videos)

* * *

### Prometheus Metrics - Open Source[​](#prometheus-metrics---open-source "Direct link to Prometheus Metrics - Open Source")

Prometheus metrics are now available in the open-source version of LiteLLM, providing comprehensive observability for your AI Gateway without requiring an enterprise license.

**Quick Start:**

```
litellm_settings:
success_callback:["prometheus"]
failure_callback:["prometheus"]
```

[Get Started with Prometheus](https://docs.litellm.ai/docs/proxy/logging#prometheus)

* * *

### Vector Store Files API[​](#vector-store-files-api "Direct link to Vector Store Files API")

Complete OpenAI-compatible Vector Store Files API now stable, enabling full file lifecycle management within vector stores.

**Supported Endpoints:**

- `POST /v1/vector_stores/{vector_store_id}/files` - Create vector store file
- `GET /v1/vector_stores/{vector_store_id}/files` - List vector store files
- `GET /v1/vector_stores/{vector_store_id}/files/{file_id}` - Retrieve vector store file
- `GET /v1/vector_stores/{vector_store_id}/files/{file_id}/content` - Retrieve file content
- `DELETE /v1/vector_stores/{vector_store_id}/files/{file_id}` - Delete vector store file
- `DELETE /v1/vector_stores/{vector_store_id}` - Delete vector store

**Quick Start:**

Create Vector Store File

```
curl --location 'http://localhost:4000/v1/vector_stores/vs_123/files' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-1234' \
--data '{
    "file_id": "file_abc"
}'
```

[Get Started with Vector Stores](https://docs.litellm.ai/docs/vector_store_files)

* * *

## New Providers and Endpoints[​](#new-providers-and-endpoints "Direct link to New Providers and Endpoints")

### New Providers[​](#new-providers "Direct link to New Providers")

ProviderSupported EndpointsDescription[**RunwayML**](https://docs.litellm.ai/docs/providers/runwayml/videos)`/v1/videos`, `/v1/images/generations`, `/v1/audio/speech`Gen-4 video generation, image generation, and text-to-speech

### New LLM API Endpoints[​](#new-llm-api-endpoints "Direct link to New LLM API Endpoints")

EndpointMethodDescriptionDocumentation`/v1/vector_stores/{vector_store_id}/files`POSTCreate vector store file[Docs](https://docs.litellm.ai/docs/vector_store_files)`/v1/vector_stores/{vector_store_id}/files`GETList vector store files[Docs](https://docs.litellm.ai/docs/vector_store_files)`/v1/vector_stores/{vector_store_id}/files/{file_id}`GETRetrieve vector store file[Docs](https://docs.litellm.ai/docs/vector_store_files)`/v1/vector_stores/{vector_store_id}/files/{file_id}/content`GETRetrieve file content[Docs](https://docs.litellm.ai/docs/vector_store_files)`/v1/vector_stores/{vector_store_id}/files/{file_id}`DELETEDelete vector store file[Docs](https://docs.litellm.ai/docs/vector_store_files)`/v1/vector_stores/{vector_store_id}`DELETEDelete vector store[Docs](https://docs.litellm.ai/docs/vector_store_files)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesOpenAI`gpt-5.1`272K$1.25$10.00Reasoning, vision, PDF input, responses APIOpenAI`gpt-5.1-2025-11-13`272K$1.25$10.00Reasoning, vision, PDF input, responses APIOpenAI`gpt-5.1-chat-latest`128K$1.25$10.00Reasoning, vision, PDF inputOpenAI`gpt-5.1-codex`272K$1.25$10.00Responses API, reasoning, visionOpenAI`gpt-5.1-codex-mini`272K$0.25$2.00Responses API, reasoning, visionMoonshot`moonshot/kimi-k2-thinking`262K$0.60$2.50Function calling, web search, reasoningMistral`mistral/magistral-medium-2509`40K$2.00$5.00Reasoning, function callingVertex AI`vertex_ai/moonshotai/kimi-k2-thinking-maas`256K$0.60$2.50Function calling, web searchOpenRouter`openrouter/deepseek/deepseek-v3.2-exp`164K$0.20$0.40Function calling, prompt cachingOpenRouter`openrouter/minimax/minimax-m2`205K$0.26$1.02Function calling, reasoningOpenRouter`openrouter/z-ai/glm-4.6`203K$0.40$1.75Function calling, reasoningOpenRouter`openrouter/z-ai/glm-4.6:exacto`203K$0.45$1.90Function calling, reasoningVoyage`voyage/voyage-3.5`32K$0.06-EmbeddingsVoyage`voyage/voyage-3.5-lite`32K$0.02-Embeddings

#### Video Generation Models[​](#video-generation-models "Direct link to Video Generation Models")

ProviderModelCost Per SecondResolutionsFeaturesRunwayML`runwayml/gen4_turbo`$0.051280x720, 720x1280Text + image to videoRunwayML`runwayml/gen4_aleph`$0.151280x720, 720x1280Text + image to videoRunwayML`runwayml/gen3a_turbo`$0.051280x720, 720x1280Text + image to video

#### Image Generation Models[​](#image-generation-models "Direct link to Image Generation Models")

ProviderModelCost Per ImageResolutionsFeaturesRunwayML`runwayml/gen4_image`$0.051280x720, 1920x1080Text + image to imageRunwayML`runwayml/gen4_image_turbo`$0.021280x720, 1920x1080Text + image to imageFal.ai`fal_ai/fal-ai/flux-pro/v1.1`$0.04/image-Image generationFal.ai`fal_ai/fal-ai/flux/schnell`$0.003/image-Fast image generationFal.ai`fal_ai/fal-ai/bytedance/seedream/v3/text-to-image`$0.03/image-Image generationFal.ai`fal_ai/fal-ai/bytedance/dreamina/v3.1/text-to-image`$0.03/image-Image generationFal.ai`fal_ai/fal-ai/ideogram/v3`$0.06/image-Image generationFal.ai`fal_ai/fal-ai/imagen4/preview/fast`$0.02/image-Fast image generationFal.ai`fal_ai/fal-ai/imagen4/preview/ultra`$0.06/image-High-quality image generation

#### Audio Models[​](#audio-models "Direct link to Audio Models")

ProviderModelCostFeaturesRunwayML`runwayml/eleven_multilingual_v2`$0.0003/charText-to-speech

#### Features[​](#features "Direct link to Features")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Add GPT-5.1 family support with reasoning capabilities - [PR #16598](https://github.com/BerriAI/litellm/pull/16598)
  - Add support for `reasoning_effort='none'` for GPT-5.1 - [PR #16658](https://github.com/BerriAI/litellm/pull/16658)
  - Add `verbosity` parameter support for GPT-5 family models - [PR #16660](https://github.com/BerriAI/litellm/pull/16660)
  - Fix forward OpenAI organization for image generation - [PR #16607](https://github.com/BerriAI/litellm/pull/16607)
- [**Gemini (Google AI Studio + Vertex AI)**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add support for `reasoning_effort='none'` for Gemini models - [PR #16548](https://github.com/BerriAI/litellm/pull/16548)
  - Add all Gemini image models support in image generation - [PR #16526](https://github.com/BerriAI/litellm/pull/16526)
  - Add Gemini image edit support - [PR #16430](https://github.com/BerriAI/litellm/pull/16430)
  - Fix preserve non-ASCII characters in function call arguments - [PR #16550](https://github.com/BerriAI/litellm/pull/16550)
  - Fix Gemini conversation format issue with MCP auto-execution - [PR #16592](https://github.com/BerriAI/litellm/pull/16592)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add support for filtering knowledge base queries - [PR #16543](https://github.com/BerriAI/litellm/pull/16543)
  - Ensure correct `aws_region` is used when provided dynamically for embeddings - [PR #16547](https://github.com/BerriAI/litellm/pull/16547)
  - Add support for custom KMS encryption keys in Bedrock Batch operations - [PR #16662](https://github.com/BerriAI/litellm/pull/16662)
  - Add bearer token authentication support for AgentCore - [PR #16556](https://github.com/BerriAI/litellm/pull/16556)
  - Fix AgentCore SSE stream iterator to async for proper streaming support - [PR #16293](https://github.com/BerriAI/litellm/pull/16293)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Add context management param support - [PR #16528](https://github.com/BerriAI/litellm/pull/16528)
  - Fix preserve `$defs` for Anthropic tools input schema - [PR #16648](https://github.com/BerriAI/litellm/pull/16648)
  - Fix support Anthropic tool\_use and tool\_result in token counter - [PR #16351](https://github.com/BerriAI/litellm/pull/16351)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex_ai)
  
  - Add Vertex Kimi-K2-Thinking support - [PR #16671](https://github.com/BerriAI/litellm/pull/16671)
  - Add `vertex_credentials` support to `litellm.rerank()` - [PR #16479](https://github.com/BerriAI/litellm/pull/16479)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Fix Magistral streaming to emit reasoning chunks - [PR #16434](https://github.com/BerriAI/litellm/pull/16434)
- [**Moonshot (Kimi)**](https://docs.litellm.ai/docs/providers/moonshot)
  
  - Add Kimi K2 thinking model support - [PR #16445](https://github.com/BerriAI/litellm/pull/16445)
- [**SambaNova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Fix SambaNova API rejecting requests when message content is passed as a list format - [PR #16612](https://github.com/BerriAI/litellm/pull/16612)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Fix use vllm passthrough config for hosted vllm provider instead of raising error - [PR #16537](https://github.com/BerriAI/litellm/pull/16537)
  - Add headers to VLLM Passthrough requests with success event logging - [PR #16532](https://github.com/BerriAI/litellm/pull/16532)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Fix improve Azure auth parameter handling for None values - [PR #14436](https://github.com/BerriAI/litellm/pull/14436)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Fix parse failed chunks for Groq - [PR #16595](https://github.com/BerriAI/litellm/pull/16595)
- [**Voyage**](https://docs.litellm.ai/docs/providers/voyage)
  
  - Add Voyage 3.5 and 3.5-lite embeddings pricing and doc update - [PR #16641](https://github.com/BerriAI/litellm/pull/16641)
- [**Fal.ai**](https://docs.litellm.ai/docs/image_generation)
  
  - Add fal-ai/flux/schnell support - [PR #16580](https://github.com/BerriAI/litellm/pull/16580)
  - Add all Imagen4 variants of fal ai in model map - [PR #16579](https://github.com/BerriAI/litellm/pull/16579)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- **General**
  
  - Fix sanitize null token usage in OpenAI-compatible responses - [PR #16493](https://github.com/BerriAI/litellm/pull/16493)
  - Fix apply provided timeout value to ClientTimeout.total - [PR #16395](https://github.com/BerriAI/litellm/pull/16395)
  - Fix raising wrong 429 error on wrong exception - [PR #16482](https://github.com/BerriAI/litellm/pull/16482)
  - Add new models, delete repeat models, update pricing - [PR #16491](https://github.com/BerriAI/litellm/pull/16491)
  - Update model logging format for custom LLM provider - [PR #16485](https://github.com/BerriAI/litellm/pull/16485)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### New Endpoints[​](#new-endpoints "Direct link to New Endpoints")

- [**GET /providers**](https://docs.litellm.ai/docs/proxy/management_endpoints)
  
  - Add GET list of providers endpoint - [PR #16432](https://github.com/BerriAI/litellm/pull/16432)

#### Features[​](#features-1 "Direct link to Features")

- [**Video Generation API**](https://docs.litellm.ai/docs/video_generation)
  
  - Allow internal users to access video generation routes - [PR #16472](https://github.com/BerriAI/litellm/pull/16472)
- [**Vector Stores API**](https://docs.litellm.ai/docs/vector_stores)
  
  - Vector store files stable release with complete CRUD operations - [PR #16643](https://github.com/BerriAI/litellm/pull/16643)
    
    - `POST /v1/vector_stores/{vector_store_id}/files` - Create vector store file
    - `GET /v1/vector_stores/{vector_store_id}/files` - List vector store files
    - `GET /v1/vector_stores/{vector_store_id}/files/{file_id}` - Retrieve vector store file
    - `GET /v1/vector_stores/{vector_store_id}/files/{file_id}/content` - Retrieve file content
    - `DELETE /v1/vector_stores/{vector_store_id}/files/{file_id}` - Delete vector store file
    - `DELETE /v1/vector_stores/{vector_store_id}` - Delete vector store
  - Ensure users can access `search_results` for both stream + non-stream response - [PR #16459](https://github.com/BerriAI/litellm/pull/16459)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Video Generation API**](https://docs.litellm.ai/docs/video_generation)
  
  - Fix use GET for `/v1/videos/{video_id}/content` - [PR #16672](https://github.com/BerriAI/litellm/pull/16672)
- **General**
  
  - Fix remove generic exception handling - [PR #16599](https://github.com/BerriAI/litellm/pull/16599)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Proxy CLI Auth**
  
  - Fix remove strict master\_key check in add\_deployment - [PR #16453](https://github.com/BerriAI/litellm/pull/16453)
- **Virtual Keys**
  
  - UI - Add Tags To Edit Key Flow - [PR #16500](https://github.com/BerriAI/litellm/pull/16500)
  - UI - Test Key Page show models based on selected endpoint - [PR #16452](https://github.com/BerriAI/litellm/pull/16452)
  - UI - Expose user\_alias in view and update path - [PR #16669](https://github.com/BerriAI/litellm/pull/16669)
- **Models + Endpoints**
  
  - UI - Add LiteLLM Params to Edit Model - [PR #16496](https://github.com/BerriAI/litellm/pull/16496)
  - UI - Add Model use backend data - [PR #16664](https://github.com/BerriAI/litellm/pull/16664)
  - UI - Remove Description Field from LLM Credentials - [PR #16608](https://github.com/BerriAI/litellm/pull/16608)
  - UI - Add RunwayML on Admin UI supported models/providers - [PR #16606](https://github.com/BerriAI/litellm/pull/16606)
  - Infra - Migrate Add Model Fields to Backend - [PR #16620](https://github.com/BerriAI/litellm/pull/16620)
  - Add API Endpoint for creating model access group - [PR #16663](https://github.com/BerriAI/litellm/pull/16663)
- **Teams**
  
  - UI - Invite User Searchable Team Select - [PR #16454](https://github.com/BerriAI/litellm/pull/16454)
  - Fix use user budget instead of key budget when creating new team - [PR #16074](https://github.com/BerriAI/litellm/pull/16074)
- **Budgets**
  
  - UI - Move Budgets out of Experimental - [PR #16544](https://github.com/BerriAI/litellm/pull/16544)
- **Guardrails**
  
  - UI - Config Guardrails should not be deletable from table - [PR #16540](https://github.com/BerriAI/litellm/pull/16540)
  - Fix remove enterprise restriction from guardrails list endpoint - [PR #15333](https://github.com/BerriAI/litellm/pull/15333)
- **Callbacks**
  
  - UI - New Callbacks table - [PR #16512](https://github.com/BerriAI/litellm/pull/16512)
  - Fix delete callbacks failing - [PR #16473](https://github.com/BerriAI/litellm/pull/16473)
- **Usage & Analytics**
  
  - UI - Improve Usage Indicator - [PR #16504](https://github.com/BerriAI/litellm/pull/16504)
  - UI - Model Info Page Health Check - [PR #16416](https://github.com/BerriAI/litellm/pull/16416)
  - Infra - Show Deprecation Warning for Model Analytics Tab - [PR #16417](https://github.com/BerriAI/litellm/pull/16417)
  - Fix Litellm tags usage add request\_id - [PR #16111](https://github.com/BerriAI/litellm/pull/16111)
- **Health Check**
  
  - Add Langfuse OTEL and SQS to Health Check - [PR #16514](https://github.com/BerriAI/litellm/pull/16514)
- **General UI**
  
  - UI - Normalize table action columns appearance - [PR #16657](https://github.com/BerriAI/litellm/pull/16657)
  - UI - Button Styles and Sizing in Settings Pages - [PR #16600](https://github.com/BerriAI/litellm/pull/16600)
  - UI - SSO Modal Cosmetic Changes - [PR #16554](https://github.com/BerriAI/litellm/pull/16554)
  - Fix UI logos loading with SERVER\_ROOT\_PATH - [PR #16618](https://github.com/BerriAI/litellm/pull/16618)
  - Fix remove misleading 'Custom' option mention from OpenAI endpoint tooltips - [PR #16622](https://github.com/BerriAI/litellm/pull/16622)
- **SSO**
  
  - Ensure `role` from SSO provider is used when a user is inserted onto LiteLLM - [PR #16794](https://github.com/BerriAI/litellm/pull/16794)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **Management Endpoints**
  
  - Fix inconsistent error responses in customer management endpoints - [PR #16450](https://github.com/BerriAI/litellm/pull/16450)
  - Fix correct date range filtering in /spend/logs endpoint - [PR #16443](https://github.com/BerriAI/litellm/pull/16443)
  - Fix /spend/logs/ui Access Control - [PR #16446](https://github.com/BerriAI/litellm/pull/16446)
  - Add pagination for /spend/logs/session/ui endpoint - [PR #16603](https://github.com/BerriAI/litellm/pull/16603)
  - Fix LiteLLM Usage shows key\_hash - [PR #16471](https://github.com/BerriAI/litellm/pull/16471)
  - Fix app\_roles missing from jwt payload - [PR #16448](https://github.com/BerriAI/litellm/pull/16448)

* * *

## Logging / Guardrail / Prompt Management Integrations[​](#logging--guardrail--prompt-management-integrations "Direct link to Logging / Guardrail / Prompt Management Integrations")

#### New Integration[​](#new-integration "Direct link to New Integration")

- **🆕 [Zscaler AI Guard](https://docs.litellm.ai/docs/proxy/guardrails/zscaler_ai_guard)**
  
  - Add Zscaler AI Guard hook for security policy enforcement - [PR #15691](https://github.com/BerriAI/litellm/pull/15691)

#### Logging[​](#logging "Direct link to Logging")

- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Fix handle null usage values to prevent validation errors - [PR #16396](https://github.com/BerriAI/litellm/pull/16396)
- [**CloudZero**](https://docs.litellm.ai/docs/proxy/logging)
  
  - Fix updated spend would not be sent to CloudZero - [PR #16201](https://github.com/BerriAI/litellm/pull/16201)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**IBM Detector**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Ensure detector-id is passed as header to IBM detector server - [PR #16649](https://github.com/BerriAI/litellm/pull/16649)

#### Prompt Management[​](#prompt-management "Direct link to Prompt Management")

- [**Custom Prompt Management**](https://docs.litellm.ai/docs/proxy/prompt_management)
  
  - Add SDK focused examples for custom prompt management - [PR #16441](https://github.com/BerriAI/litellm/pull/16441)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **End User Budgets**
  
  - Allow pointing max\_end\_user budget to an id, so the default ID applies to all end users - [PR #16456](https://github.com/BerriAI/litellm/pull/16456)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **Configuration**
  
  - Add dynamic OAuth2 metadata discovery for MCP servers - [PR #16676](https://github.com/BerriAI/litellm/pull/16676)
  - Fix allow tool call even when server name prefix is missing - [PR #16425](https://github.com/BerriAI/litellm/pull/16425)
  - Fix exclude unauthorized MCP servers from allowed server list - [PR #16551](https://github.com/BerriAI/litellm/pull/16551)
  - Fix unable to delete MCP server from permission settings - [PR #16407](https://github.com/BerriAI/litellm/pull/16407)
  - Fix avoid crashing when MCP server record lacks credentials - [PR #16601](https://github.com/BerriAI/litellm/pull/16601)

* * *

## Agents[​](#agents "Direct link to Agents")

- [**Agent Registration (A2A Spec)**](https://docs.litellm.ai/docs/agents)
  
  - Support agent registration + discovery following Agent-to-Agent specification - [PR #16615](https://github.com/BerriAI/litellm/pull/16615)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Embeddings Performance**
  
  - Use router's O(1) lookup and shared sessions for embeddings - [PR #16344](https://github.com/BerriAI/litellm/pull/16344)
- **Router Reliability**
  
  - Support default fallbacks for unknown models - [PR #16419](https://github.com/BerriAI/litellm/pull/16419)
- **Callback Management**
  
  - Add atexit handlers to flush callbacks for async completions - [PR #16487](https://github.com/BerriAI/litellm/pull/16487)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Configuration Management**
  
  - Fix update model\_cost\_map\_url to use environment variable - [PR #16429](https://github.com/BerriAI/litellm/pull/16429)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Fix streaming example in README - [PR #16461](https://github.com/BerriAI/litellm/pull/16461)
  - Update broken Slack invite links to support page - [PR #16546](https://github.com/BerriAI/litellm/pull/16546)
  - Fix code block indentation for fallbacks page - [PR #16542](https://github.com/BerriAI/litellm/pull/16542)
  - Documentation code example corrections - [PR #16502](https://github.com/BerriAI/litellm/pull/16502)
  - Document `reasoning_effort` summary field options - [PR #16549](https://github.com/BerriAI/litellm/pull/16549)
- **API Documentation**
  
  - Add docs on APIs for model access management - [PR #16673](https://github.com/BerriAI/litellm/pull/16673)
  - Add docs for showing how to auto reload new pricing data - [PR #16675](https://github.com/BerriAI/litellm/pull/16675)
  - LiteLLM Quick start - show how model resolution works - [PR #16602](https://github.com/BerriAI/litellm/pull/16602)
  - Add docs for tracking callback failure - [PR #16474](https://github.com/BerriAI/litellm/pull/16474)
- **General Documentation**
  
  - Fix container api link in release page - [PR #16440](https://github.com/BerriAI/litellm/pull/16440)
  - Add softgen to projects that are using litellm - [PR #16423](https://github.com/BerriAI/litellm/pull/16423)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @artplan1 made their first contribution in [PR #16423](https://github.com/BerriAI/litellm/pull/16423)
- @JehandadK made their first contribution in [PR #16472](https://github.com/BerriAI/litellm/pull/16472)
- @vmiscenko made their first contribution in [PR #16453](https://github.com/BerriAI/litellm/pull/16453)
- @mcowger made their first contribution in [PR #16429](https://github.com/BerriAI/litellm/pull/16429)
- @yellowsubmarine372 made their first contribution in [PR #16395](https://github.com/BerriAI/litellm/pull/16395)
- @Hebruwu made their first contribution in [PR #16201](https://github.com/BerriAI/litellm/pull/16201)
- @jwang-gif made their first contribution in [PR #15691](https://github.com/BerriAI/litellm/pull/15691)
- @AnthonyMonaco made their first contribution in [PR #16502](https://github.com/BerriAI/litellm/pull/16502)
- @andrewm4894 made their first contribution in [PR #16487](https://github.com/BerriAI/litellm/pull/16487)
- @f14-bertolotti made their first contribution in [PR #16485](https://github.com/BerriAI/litellm/pull/16485)
- @busla made their first contribution in [PR #16293](https://github.com/BerriAI/litellm/pull/16293)
- @MightyGoldenOctopus made their first contribution in [PR #16537](https://github.com/BerriAI/litellm/pull/16537)
- @ultmaster made their first contribution in [PR #14436](https://github.com/BerriAI/litellm/pull/14436)
- @bchrobot made their first contribution in [PR #16542](https://github.com/BerriAI/litellm/pull/16542)
- @sep-grindr made their first contribution in [PR #16622](https://github.com/BerriAI/litellm/pull/16622)
- @pnookala-godaddy made their first contribution in [PR #16607](https://github.com/BerriAI/litellm/pull/16607)
- @dtunikov made their first contribution in [PR #16592](https://github.com/BerriAI/litellm/pull/16592)
- @lukapecnik made their first contribution in [PR #16648](https://github.com/BerriAI/litellm/pull/16648)
- @jyeros made their first contribution in [PR #16618](https://github.com/BerriAI/litellm/pull/16618)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.79.3.rc.1...v1.80.0.rc.1)

* * *

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.79.3-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **LiteLLM Custom Guardrail** - Built-in guardrail with UI configuration support
- **Performance Improvements** - `/responses` API 19× Lower Median Latency
- **Veo3 Video Generation (Vertex AI + Google AI Studio)** - Use OpenAI Video API to generate videos with Vertex AI and Google AI Studio Veo3 models

* * *

### Built-in Guardrails on AI Gateway[​](#built-in-guardrails-on-ai-gateway "Direct link to Built-in Guardrails on AI Gateway")

This release introduces built-in guardrails for LiteLLM AI Gateway, allowing you to enforce protections without depending on an external guardrail API.

- **Blocking Keywords** - Block known sensitive keywords like "litellm", "python", etc.
- **Pattern Detection** - Block known sensitive patterns like emails, Social Security Numbers, API keys, etc.
- **Custom Regex Patterns** - Define custom regex patterns for your specific use case.

Get started with the built-in guardrails on AI Gateway [here](https://docs.litellm.ai/docs/proxy/guardrails/litellm_content_filter).

* * *

### Performance – `/responses` 19× Lower Median Latency[​](#performance--responses-19-lower-median-latency "Direct link to performance--responses-19-lower-median-latency")

This update significantly improves `/responses` latency by integrating our internal network management for connection handling, eliminating per-request setup overhead.

#### Results[​](#results "Direct link to Results")

MetricBeforeAfterImprovementMedian latency3,600 ms**190 ms****−95% (~19× faster)**p95 latency4,300 ms**280 ms**−93%p99 latency4,600 ms**590 ms**−87%Average latency3,571 ms**208 ms**−94%RPS231**1,059**+358%

#### Test Setup[​](#test-setup "Direct link to Test Setup")

CategorySpecification**Load Testing**Locust: 1,000 concurrent users, 500 ramp-up**System**4 vCPUs, 8 GB RAM, 4 workers, 4 instances**Database**PostgreSQL (Redis unused)**Configuration**[config.yaml](https://gist.github.com/AlexsanderHamir/550791675fd752befcac6a9e44024652)**Load Script**[no\_cache\_hits.py](https://gist.github.com/AlexsanderHamir/99d673bf74cdd81fd39f59fa9048f2e8)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesAzure`azure/gpt-5-pro`272K$15.00$120.00Responses API, reasoning, vision, PDF inputAzure`azure/gpt-image-1-mini`---Image generation - per pixel pricingAzure`azure/container`---Container API - $0.03/sessionOpenAI`openai/container`---Container API - $0.03/sessionCohere`cohere/embed-v4.0`128K$0.12-Embeddings with image input supportGemini`gemini/gemini-live-2.5-flash-preview-native-audio-09-2025`1M$0.30$2.00Native audio, vision, web searchVertex AI`vertex_ai/minimaxai/minimax-m2-maas`196K$0.30$1.20Function calling, tool choiceNVIDIA`nvidia/nemotron-nano-9b-v2`---Chat completions

#### OCR Models[​](#ocr-models "Direct link to OCR Models")

ProviderModelCost Per PageFeaturesAzure AI`azure_ai/doc-intelligence/prebuilt-read`$0.0015Document readingAzure AI`azure_ai/doc-intelligence/prebuilt-layout`$0.01Layout analysisAzure AI`azure_ai/doc-intelligence/prebuilt-document`$0.01Document processingVertex AI`vertex_ai/mistral-ocr-2505`$0.0005OCR processing

#### Search Models[​](#search-models "Direct link to Search Models")

ProviderModelPricingFeaturesFirecrawl`firecrawl/search`Tiered: $0.00166-$0.0166/query10-100 results per querySearXNG`searxng/search`FreeOpen-source metasearch

#### Features[​](#features "Direct link to Features")

- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Add Azure GPT-5-Pro Responses API support with reasoning capabilities - [PR #16235](https://github.com/BerriAI/litellm/pull/16235)
  - Add gpt-image-1-mini pricing for Azure with quality tiers (low/medium/high) - [PR #16182](https://github.com/BerriAI/litellm/pull/16182)
  - Add support for returning Azure Content Policy error information when exceptions from Azure OpenAI occur - [PR #16231](https://github.com/BerriAI/litellm/pull/16231)
  - Fix Azure GPT-5 incorrectly routed to O-series config (temperature parameter unsupported) - [PR #16246](https://github.com/BerriAI/litellm/pull/16246)
  - Fix Azure doesn't accept extra body param - [PR #16116](https://github.com/BerriAI/litellm/pull/16116)
  - Fix Azure DALL-E-3 health check content policy violation by using safe default prompt - [PR #16329](https://github.com/BerriAI/litellm/pull/16329)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fix empty assistant message handling in AWS Bedrock Converse API to prevent 400 Bad Request errors - [PR #15850](https://github.com/BerriAI/litellm/pull/15850)
  - Fix: Filter AWS authentication params from Bedrock InvokeModel request body - [PR #16315](https://github.com/BerriAI/litellm/pull/16315)
  - Fix Bedrock proxy adding name to file content, breaks when cache\_control in use - [PR #16275](https://github.com/BerriAI/litellm/pull/16275)
  - Fix global.anthropic.claude-haiku-4-5-20251001-v1:0 supports\_reasoning flag and update pricing - [PR #16263](https://github.com/BerriAI/litellm/pull/16263)
- [**Gemini (Google AI Studio + Vertex AI)**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add gemini live audio model cost in model map - [PR #16183](https://github.com/BerriAI/litellm/pull/16183)
  - Fix translation problem with Gemini parallel tool calls - [PR #16194](https://github.com/BerriAI/litellm/pull/16194)
  - Fix: Send Gemini API key via x-goog-api-key header with custom api\_base - [PR #16085](https://github.com/BerriAI/litellm/pull/16085)
  - Fix image\_config.aspect\_ratio not working for gemini-2.5-flash-image - [PR #15999](https://github.com/BerriAI/litellm/pull/15999)
  - Fix Gemini minimal reasoning env overrides disabling thoughts - [PR #16347](https://github.com/BerriAI/litellm/pull/16347)
  - Fix cache\_read\_input\_token\_cost for gemini-2.5-flash - [PR #16354](https://github.com/BerriAI/litellm/pull/16354)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Fix Anthropic token counting for VertexAI - [PR #16171](https://github.com/BerriAI/litellm/pull/16171)
  - Fix anthropic-adapter: properly translate Anthropic image format to OpenAI - [PR #16202](https://github.com/BerriAI/litellm/pull/16202)
  - Enable automated prompt caching message format for Claude on Databricks - [PR #16200](https://github.com/BerriAI/litellm/pull/16200)
  - Add support for Anthropic Memory Tool - [PR #16115](https://github.com/BerriAI/litellm/pull/16115)
  - Propagate cache creation/read token costs for model info to fix Anthropic long context cost calculations - [PR #16376](https://github.com/BerriAI/litellm/pull/16376)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex_ai)
  
  - Add Vertex MiniMAX m2 model support - [PR #16373](https://github.com/BerriAI/litellm/pull/16373)
  - Correctly map 429 Resource Exhausted to RateLimitError - [PR #16363](https://github.com/BerriAI/litellm/pull/16363)
  - Add `vertex_credentials` support to `litellm.rerank()` for Vertex AI - [PR #16266](https://github.com/BerriAI/litellm/pull/16266)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks)
  
  - Fix databricks streaming - [PR #16368](https://github.com/BerriAI/litellm/pull/16368)
- [**Deepgram**](https://docs.litellm.ai/docs/providers/deepgram)
  
  - Return the diarized transcript when it's required in the request - [PR #16133](https://github.com/BerriAI/litellm/pull/16133)
- [**Fireworks**](https://docs.litellm.ai/docs/providers/fireworks_ai)
  
  - Update Fireworks audio endpoints to new `api.fireworks.ai` domains - [PR #16346](https://github.com/BerriAI/litellm/pull/16346)
- [**Cohere**](https://docs.litellm.ai/docs/providers/cohere)
  
  - Add cohere embed-v4.0 model support - [PR #16358](https://github.com/BerriAI/litellm/pull/16358)
- [**Watsonx**](https://docs.litellm.ai/docs/providers/watsonx)
  
  - Support `reasoning_effort` for watsonx chat models - [PR #16261](https://github.com/BerriAI/litellm/pull/16261)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Remove automatic summary from reasoning\_effort transformation - [PR #16210](https://github.com/BerriAI/litellm/pull/16210)
- [**XAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - Remove Grok 4 Models Reasoning Effort Parameter - [PR #16265](https://github.com/BerriAI/litellm/pull/16265)
- [**Hosted VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Fix HostedVLLMRerankConfig will not be used - [PR #16352](https://github.com/BerriAI/litellm/pull/16352)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**Bedrock Agentcore**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add Bedrock Agentcore as a provider on LiteLLM Python SDK and LiteLLM AI Gateway - [PR #16252](https://github.com/BerriAI/litellm/pull/16252)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**OCR API**](https://docs.litellm.ai/docs/ocr)
  
  - Add VertexAI OCR provider support + cost tracking - [PR #16216](https://github.com/BerriAI/litellm/pull/16216)
  - Add Azure AI Doc Intelligence OCR support - [PR #16219](https://github.com/BerriAI/litellm/pull/16219)
- [**Search API**](https://docs.litellm.ai/docs/search)
  
  - Add firecrawl search API support with tiered pricing - [PR #16257](https://github.com/BerriAI/litellm/pull/16257)
  - Add searxng search API provider - [PR #16259](https://github.com/BerriAI/litellm/pull/16259)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Support responses API streaming in langfuse otel - [PR #16153](https://github.com/BerriAI/litellm/pull/16153)
  - Pass extra\_body parameters to provider in Responses API requests - [PR #16320](https://github.com/BerriAI/litellm/pull/16320)
- [**Container API**](https://docs.litellm.ai/docs/container_api)
  
  - Add E2E Container API Support - [PR #16136](https://github.com/BerriAI/litellm/pull/16136)
  - Update container documentation to be similar to others - [PR #16327](https://github.com/BerriAI/litellm/pull/16327)
- [**Video Generation API**](https://docs.litellm.ai/docs/video_generation)
  
  - Add Vertex and Gemini Videos API with Cost Tracking + UI support - [PR #16323](https://github.com/BerriAI/litellm/pull/16323)
  - Add `custom_llm_provider` support for video endpoints (non-generation) - [PR #16121](https://github.com/BerriAI/litellm/pull/16121)
- [**Audio API**](https://docs.litellm.ai/docs/audio)
  
  - Add gpt-4o-transcribe cost tracking - [PR #16412](https://github.com/BerriAI/litellm/pull/16412)
- [**Vector Stores**](https://docs.litellm.ai/docs/vector_stores)
  
  - Milvus - search vector store support + support multi-part form data on passthrough - [PR #16035](https://github.com/BerriAI/litellm/pull/16035)
  - Azure AI Vector Stores - support "virtual" indexes + create vector store on passthrough API - [PR #16160](https://github.com/BerriAI/litellm/pull/16160)
  - Milvus - Passthrough API support - adds create + read vector store support via passthrough API's - [PR #16170](https://github.com/BerriAI/litellm/pull/16170)
- [**Embeddings API**](https://docs.litellm.ai/docs/embedding/supported_embedding)
  
  - Use valid CallTypes enum value in embeddings endpoint - [PR #16328](https://github.com/BerriAI/litellm/pull/16328)
- [**Rerank API**](https://docs.litellm.ai/docs/rerank)
  
  - Generalize tiered pricing in generic cost calculator - [PR #16150](https://github.com/BerriAI/litellm/pull/16150)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Fix index field not populated in streaming mode with n&gt;1 and tool calls - [PR #15962](https://github.com/BerriAI/litellm/pull/15962)
  - Pass aws\_region\_name in litellm\_params - [PR #16321](https://github.com/BerriAI/litellm/pull/16321)
  - Add `retry-after` header support for errors `502`, `503`, `504` - [PR #16288](https://github.com/BerriAI/litellm/pull/16288)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Virtual Keys**
  
  - UI - Delete Team Member with friction - [PR #16167](https://github.com/BerriAI/litellm/pull/16167)
  - UI - Litellm test key audio support - [PR #16251](https://github.com/BerriAI/litellm/pull/16251)
  - UI - Test Key Page Revert Model To Single Select - [PR #16390](https://github.com/BerriAI/litellm/pull/16390)
- **Models + Endpoints**
  
  - UI - Add Model Existing Credentials Improvement - [PR #16166](https://github.com/BerriAI/litellm/pull/16166)
  - UI - Add Azure AD Token field and Azure API Key optional - [PR #16331](https://github.com/BerriAI/litellm/pull/16331)
  - UI - Fixed Label for vLLM in Model Create Flow - [PR #16285](https://github.com/BerriAI/litellm/pull/16285)
  - UI - Include Model Access Group Models on Team Models Table - [PR #16298](https://github.com/BerriAI/litellm/pull/16298)
  - Fix /model\_group/info Returning Entire Model List for SSO Users - [PR #16296](https://github.com/BerriAI/litellm/pull/16296)
  - Litellm non root docker Model Hub Table fix - [PR #16282](https://github.com/BerriAI/litellm/pull/16282)
- **Guardrails**
  
  - UI - Fix regression where Guardrail Entity Could not be selected and entity was not displayed - [PR #16165](https://github.com/BerriAI/litellm/pull/16165)
  - UI - Guardrail Info Page Show PII Config - [PR #16164](https://github.com/BerriAI/litellm/pull/16164)
  - Change guardrail\_information to list type - [PR #16127](https://github.com/BerriAI/litellm/pull/16127)
  - UI - LiteLLM Guardrail - ensure you can see UI Friendly name for PII Patterns - [PR #16382](https://github.com/BerriAI/litellm/pull/16382)
  - UI - Guardrails - LiteLLM Content Filter, Allow Viewing/Editing Content Filter Settings - [PR #16383](https://github.com/BerriAI/litellm/pull/16383)
  - UI - Guardrails - allow updating guardrails through UI. Ensure litellm\_params actually get updated in memory - [PR #16384](https://github.com/BerriAI/litellm/pull/16384)
- **SSO Settings**
  
  - Support dot notation on ui sso - [PR #16135](https://github.com/BerriAI/litellm/pull/16135)
  - UI - Prevent trailing slash in sso proxy base url input - [PR #16244](https://github.com/BerriAI/litellm/pull/16244)
  - UI - SSO Proxy Base URL input validation and remove normalizing / - [PR #16332](https://github.com/BerriAI/litellm/pull/16332)
  - UI - Surface SSO Create errors on create flow - [PR #16369](https://github.com/BerriAI/litellm/pull/16369)
- **Usage & Analytics**
  
  - UI - Tag Usage Top Model Table View and Label Fix - [PR #16249](https://github.com/BerriAI/litellm/pull/16249)
  - UI - Litellm usage date picker - [PR #16264](https://github.com/BerriAI/litellm/pull/16264)
- **Cache Settings**
  
  - UI - Cache Settings Redis Add Semantic Cache Settings - [PR #16398](https://github.com/BerriAI/litellm/pull/16398)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **General**
  
  - UI - Remove encoding\_format in request for embedding models - [PR #16367](https://github.com/BerriAI/litellm/pull/16367)
  - UI - Revert Changes for Test Key Multiple Model Select - [PR #16372](https://github.com/BerriAI/litellm/pull/16372)
  - UI - Various Small Issues - [PR #16406](https://github.com/BerriAI/litellm/pull/16406)

* * *

## AI Integrations[​](#ai-integrations "Direct link to AI Integrations")

### Logging[​](#logging "Direct link to Logging")

- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Fix langfuse input tokens logic for cached tokens - [PR #16203](https://github.com/BerriAI/litellm/pull/16203)
- [**Opik**](https://docs.litellm.ai/docs/proxy/logging#opik)
  
  - Fix the bug with not incorrect attachment to existing trace & refactor - [PR #15529](https://github.com/BerriAI/litellm/pull/15529)
- [**S3**](https://docs.litellm.ai/docs/proxy/logging#s3)
  
  - S3 logger, add support for ssl\_verify when using minio logger - [PR #16211](https://github.com/BerriAI/litellm/pull/16211)
  - Strip base64 in s3 - [PR #16157](https://github.com/BerriAI/litellm/pull/16157)
  - Add allowing Key based prefix to s3 path - [PR #16237](https://github.com/BerriAI/litellm/pull/16237)
  - Add Prometheus metric to track callback logging failures in S3 - [PR #16209](https://github.com/BerriAI/litellm/pull/16209)
- [**OpenTelemetry**](https://docs.litellm.ai/docs/proxy/logging#opentelemetry)
  
  - OTEL - Log Cost Breakdown on OTEL Logger - [PR #16334](https://github.com/BerriAI/litellm/pull/16334)
- [**DataDog**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Add DD Agent Host support for `datadog` callback - [PR #16379](https://github.com/BerriAI/litellm/pull/16379)

### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**Noma**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Revert Noma Apply Guardrail implementation - [PR #16214](https://github.com/BerriAI/litellm/pull/16214)
  - Litellm noma guardrail support images - [PR #16199](https://github.com/BerriAI/litellm/pull/16199)
- [**PANW Prisma AIRS**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - PANW prisma airs guardrail deduplication and enhanced session tracking - [PR #16273](https://github.com/BerriAI/litellm/pull/16273)
- [**LiteLLM Custom Guardrail**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Add LiteLLM Gateway built in guardrail - [PR #16338](https://github.com/BerriAI/litellm/pull/16338)
  - UI - Allow configuring LiteLLM Custom Guardrail - [PR #16339](https://github.com/BerriAI/litellm/pull/16339)
  - Bug Fix: Content Filter Guard - [PR #16414](https://github.com/BerriAI/litellm/pull/16414)

### Secret Managers[​](#secret-managers "Direct link to Secret Managers")

- [**CyberArk**](https://docs.litellm.ai/docs/secret_managers)
  
  - Add CyberArk Secrets Manager Integration - [PR #16278](https://github.com/BerriAI/litellm/pull/16278)
  - Cyber Ark - Add Key Rotations support - [PR #16289](https://github.com/BerriAI/litellm/pull/16289)
- [**HashiCorp Vault**](https://docs.litellm.ai/docs/secret_managers)
  
  - Add configurable mount name and path prefix for HashiCorp Vault - [PR #16253](https://github.com/BerriAI/litellm/pull/16253)
  - Secret Manager - Hashicorp, add auth via approle - [PR #16374](https://github.com/BerriAI/litellm/pull/16374)
- [**AWS Secrets Manager**](https://docs.litellm.ai/docs/secret_managers)
  
  - Add tags and descriptions support to aws secrets manager - [PR #16224](https://github.com/BerriAI/litellm/pull/16224)
- [**Custom Secret Manager**](https://docs.litellm.ai/docs/secret_managers)
  
  - Add Custom Secret Manager - Allow users to define and write a custom secret manager - [PR #16297](https://github.com/BerriAI/litellm/pull/16297)
- **General**
  
  - Email Notifications - Ensure Users get Key Rotated Email - [PR #16292](https://github.com/BerriAI/litellm/pull/16292)
  - Fix verify ssl on sts boto3 - [PR #16313](https://github.com/BerriAI/litellm/pull/16313)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Cost Tracking**
  
  - Fix OpenAI Responses API streaming tests usage field names and cost calculation - [PR #16236](https://github.com/BerriAI/litellm/pull/16236)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **Configuration**
  
  - Configure static mcp header - [PR #16179](https://github.com/BerriAI/litellm/pull/16179)
  - Persist mcp credentials in db - [PR #16308](https://github.com/BerriAI/litellm/pull/16308)

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Memory Leak Fixes**
  
  - Resolve memory accumulation caused by Pydantic 2.11+ deprecation warnings - [PR #16110](https://github.com/BerriAI/litellm/pull/16110)
- **Session Management**
  
  - Add shared\_session support to responses API - [PR #16260](https://github.com/BerriAI/litellm/pull/16260)
- **Error Handling**
  
  - Gracefully handle connection closed errors during streaming - [PR #16294](https://github.com/BerriAI/litellm/pull/16294)
  - Handle None values in daily spend sort key - [PR #16245](https://github.com/BerriAI/litellm/pull/16245)
- **Configuration**
  
  - Remove minimum validation for cache control injection index - [PR #16149](https://github.com/BerriAI/litellm/pull/16149)
  - Improve clearing logic - only remove unvisited endpoints - [PR #16400](https://github.com/BerriAI/litellm/pull/16400)
- **Redis**
  
  - Handle float redis\_version from AWS ElastiCache Valkey - [PR #16207](https://github.com/BerriAI/litellm/pull/16207)
- **Hooks**
  
  - Add parallel execution handling in during\_call\_hook - [PR #16279](https://github.com/BerriAI/litellm/pull/16279)
- **Infrastructure**
  
  - Install runtime node for prisma - [PR #16410](https://github.com/BerriAI/litellm/pull/16410)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Docs - v1.79.1 - [PR #16163](https://github.com/BerriAI/litellm/pull/16163)
  - Fix broken link on model\_management.md - [PR #16217](https://github.com/BerriAI/litellm/pull/16217)
  - Fix image generation response format - use 'images' array instead of 'image' object - [PR #16378](https://github.com/BerriAI/litellm/pull/16378)
- **General Documentation**
  
  - Add minimum resource requirement for production - [PR #16146](https://github.com/BerriAI/litellm/pull/16146)
  - Add benchmark comparison with other AI gateways - [PR #16248](https://github.com/BerriAI/litellm/pull/16248)
  - LiteLLM content filter guard documentation - [PR #16413](https://github.com/BerriAI/litellm/pull/16413)
  - Fix typo of the word orginal - [PR #16255](https://github.com/BerriAI/litellm/pull/16255)
- **Security**
  
  - Remove tornado test files (including test.key), fixes Python 3.13 security issues - [PR #16342](https://github.com/BerriAI/litellm/pull/16342)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @steve-gore-snapdocs made their first contribution in [PR #16149](https://github.com/BerriAI/litellm/pull/16149)
- @timbmg made their first contribution in [PR #16120](https://github.com/BerriAI/litellm/pull/16120)
- @Nivg made their first contribution in [PR #16202](https://github.com/BerriAI/litellm/pull/16202)
- @pablobgar made their first contribution in [PR #16194](https://github.com/BerriAI/litellm/pull/16194)
- @AlanPonnachan made their first contribution in [PR #16150](https://github.com/BerriAI/litellm/pull/16150)
- @Chesars made their first contribution in [PR #16236](https://github.com/BerriAI/litellm/pull/16236)
- @bowenliang123 made their first contribution in [PR #16255](https://github.com/BerriAI/litellm/pull/16255)
- @dean-zavad made their first contribution in [PR #16199](https://github.com/BerriAI/litellm/pull/16199)
- @alexkuzmik made their first contribution in [PR #15529](https://github.com/BerriAI/litellm/pull/15529)
- @Granine made their first contribution in [PR #16281](https://github.com/BerriAI/litellm/pull/16281)
- @Oodapow made their first contribution in [PR #16279](https://github.com/BerriAI/litellm/pull/16279)
- @jgoodyear made their first contribution in [PR #16275](https://github.com/BerriAI/litellm/pull/16275)
- @Qanpi made their first contribution in [PR #16321](https://github.com/BerriAI/litellm/pull/16321)
- @ShimonMimoun made their first contribution in [PR #16313](https://github.com/BerriAI/litellm/pull/16313)
- @andriykislitsyn made their first contribution in [PR #16288](https://github.com/BerriAI/litellm/pull/16288)
- @reckless-huang made their first contribution in [PR #16263](https://github.com/BerriAI/litellm/pull/16263)
- @chenmoneygithub made their first contribution in [PR #16368](https://github.com/BerriAI/litellm/pull/16368)
- @stembe-digitalex made their first contribution in [PR #16354](https://github.com/BerriAI/litellm/pull/16354)
- @jfcherng made their first contribution in [PR #16352](https://github.com/BerriAI/litellm/pull/16352)
- @xingyaoww made their first contribution in [PR #16246](https://github.com/BerriAI/litellm/pull/16246)
- @emerzon made their first contribution in [PR #16373](https://github.com/BerriAI/litellm/pull/16373)
- @wwwillchen made their first contribution in [PR #16376](https://github.com/BerriAI/litellm/pull/16376)
- @fabriciojoc made their first contribution in [PR #16203](https://github.com/BerriAI/litellm/pull/16203)
- @jroberts2600 made their first contribution in [PR #16273](https://github.com/BerriAI/litellm/pull/16273)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.79.1-nightly...v1.79.2.rc.1)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.79.1-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Container API Support** - End-to-end OpenAI Container API support with proxy integration, logging, and cost tracking
- **FAL AI Image Generation** - Native support for FAL AI image generation models with cost tracking
- **UI Enhancements** - Guardrail Playground, Cache Settings, Tag Routing, SSO Settings
- **Batch API Rate Limiting** - Input-based rate limits support for Batch API requests
- **Vector Store Expansion** - Milvus vector store support and Azure AI virtual indexes
- **Memory Leak Fixes** - Resolved issues accounting for 90% of memory leaks on Python SDK & AI Gateway

* * *

## Dependency Upgrades[​](#dependency-upgrades "Direct link to Dependency Upgrades")

- **Dependencies**
  
  - Build(deps): bump starlette from 0.47.2 to 0.49.1 - [PR #16027](https://github.com/BerriAI/litellm/pull/16027)
  - Build(deps): bump fastapi from 0.116.1 to 0.120.1 - [PR #16054](https://github.com/BerriAI/litellm/pull/16054)
  - Build(deps): bump hono from 4.9.7 to 4.10.3 in /litellm-js/spend-logs - [PR #15915](https://github.com/BerriAI/litellm/pull/15915)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesMistral`mistral/codestral-embed`8K$0.15-EmbeddingsMistral`mistral/codestral-embed-2505`8K$0.15-EmbeddingsGemini`gemini/gemini-embedding-001`2K$0.15-EmbeddingsFAL AI`fal_ai/fal-ai/flux-pro/v1.1-ultra`---Image generation - $0.0398/imageFAL AI`fal_ai/fal-ai/imagen4/preview`---Image generation - $0.0398/imageFAL AI`fal_ai/fal-ai/recraft/v3/text-to-image`---Image generation - $0.0398/imageFAL AI`fal_ai/fal-ai/stable-diffusion-v35-medium`---Image generation - $0.0398/imageFAL AI`fal_ai/bria/text-to-image/3.2`---Image generation - $0.0398/imageOpenAI`openai/sora-2-pro`---Video generation - $0.30/video/second

#### Features[​](#features "Direct link to Features")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Extended Claude 3-7 Sonnet deprecation date from 2026-02-01 to 2026-02-19 - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
  - Extended Claude Opus 4-0 deprecation date from 2025-03-01 to 2026-05-01 - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
  - Removed Claude Haiku 3-5 deprecation date (previously 2025-03-01) - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
  - Added Claude Opus 4-1, Claude Opus 4-0 20250513, Claude Sonnet 4 20250514 deprecation dates - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
  - Added web search support for Claude Opus 4-1 - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fix empty assistant message handling in AWS Bedrock Converse API to prevent 400 Bad Request errors - [PR #15850](https://github.com/BerriAI/litellm/pull/15850)
  - Allow using ARNs when generating images via Bedrock - [PR #15789](https://github.com/BerriAI/litellm/pull/15789)
  - Add per model group header forwarding for Bedrock Invoke API - [PR #16042](https://github.com/BerriAI/litellm/pull/16042)
  - Preserve Bedrock inference profile IDs in health checks - [PR #15947](https://github.com/BerriAI/litellm/pull/15947)
  - Added fallback logic for detecting file content-type when S3 returns generic type - When using Bedrock with S3-hosted files, if the S3 object's Content-Type is not correctly set (e.g., binary/octet-stream instead of image/png), Bedrock can now handle it correctly - [PR #15635](https://github.com/BerriAI/litellm/pull/15635)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Add deprecation dates for Azure OpenAI models (gpt-4o-2024-08-06, gpt-4o-2024-11-20, gpt-4.1 series, o3-2025-04-16, text-embedding-3-small) - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
  - Fix Azure OpenAI ContextWindowExceededError mapping from Azure errors - [PR #15981](https://github.com/BerriAI/litellm/pull/15981)
  - Add handling for `v1` under Azure API versions - [PR #15984](https://github.com/BerriAI/litellm/pull/15984)
  - Fix azure doesn't accept extra body param - [PR #16116](https://github.com/BerriAI/litellm/pull/16116)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Add deprecation dates for gpt-3.5-turbo-1106, gpt-4-0125-preview, gpt-4-1106-preview, o1-mini-2024-09-12 - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
  - Add extended Sora-2 modality support (text + image inputs) - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
  - Updated OpenAI Sora-2-Pro pricing to $0.30/video/second - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Add Claude Haiku 4.5 pricing for OpenRouter - [PR #15909](https://github.com/BerriAI/litellm/pull/15909)
  - Add base\_url config with environment variables documentation - [PR #15946](https://github.com/BerriAI/litellm/pull/15946)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Add codestral-embed-2505 embedding model - [PR #16071](https://github.com/BerriAI/litellm/pull/16071)
- [**Gemini (Google AI Studio + Vertex AI)**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix gemini request mutation for tool use - [PR #16002](https://github.com/BerriAI/litellm/pull/16002)
  - Add gemini-embedding-001 pricing entry for Google GenAI API - [PR #16078](https://github.com/BerriAI/litellm/pull/16078)
  - Changes to fix frequency\_penalty and presence\_penalty issue for gemini-2.5-pro model - [PR #16041](https://github.com/BerriAI/litellm/pull/16041)
- [**DeepInfra**](https://docs.litellm.ai/docs/providers/deepinfra)
  
  - Add vision support for Qwen/Qwen3-chat-32b model - [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
- [**Vercel AI Gateway**](https://docs.litellm.ai/docs/providers/vercel_ai_gateway)
  
  - Fix vercel\_ai\_gateway entry for glm-4.6 (moved from vercel\_ai\_gateway/glm-4.6 to vercel\_ai\_gateway/zai/glm-4.6) - [PR #16084](https://github.com/BerriAI/litellm/pull/16084)
- [**Fireworks**](https://docs.litellm.ai/docs/providers/fireworks_ai)
  
  - Don't add "accounts/fireworks/models" prefix for Fireworks Provider - [PR #15938](https://github.com/BerriAI/litellm/pull/15938)
- [**Cohere**](https://docs.litellm.ai/docs/providers/cohere)
  
  - Add OpenAI-compatible annotations support for Cohere v2 citations - [PR #16038](https://github.com/BerriAI/litellm/pull/16038)
- [**Deepgram**](https://docs.litellm.ai/docs/providers/deepgram)
  
  - Handle Deepgram detected language when available - [PR #16093](https://github.com/BerriAI/litellm/pull/16093)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Xai**](https://docs.litellm.ai/docs/providers/xai)
  
  - Add Xai websearch cost tracking - [PR #16001](https://github.com/BerriAI/litellm/pull/16001)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**FAL AI**](https://docs.litellm.ai/docs/image_generation)
  
  - Add FAL AI Image Generation support - [PR #16067](https://github.com/BerriAI/litellm/pull/16067)
- [**OCI (Oracle Cloud Infrastructure)**](https://docs.litellm.ai/docs/providers/oci)
  
  - Add OCI Signer Authentication support - [PR #16064](https://github.com/BerriAI/litellm/pull/16064)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Container API**](https://docs.litellm.ai/docs/containers)
  
  - Add end-to-end OpenAI Container API support to LiteLLM SDK - [PR #16136](https://github.com/BerriAI/litellm/pull/16136)
  - Add proxy support for container APIs - [PR #16049](https://github.com/BerriAI/litellm/pull/16049)
  - Add logging support for Container API - [PR #16049](https://github.com/BerriAI/litellm/pull/16049)
  - Add cost tracking support for containers with documentation - [PR #16117](https://github.com/BerriAI/litellm/pull/16117)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Respect `LiteLLM-Disable-Message-Redaction` header for Responses API - [PR #15966](https://github.com/BerriAI/litellm/pull/15966)
  - Add /openai routes for responses API (Azure OpenAI SDK Compatibility) - [PR #15988](https://github.com/BerriAI/litellm/pull/15988)
  - Redact reasoning summaries in ResponsesAPI output when message logging is disabled - [PR #15965](https://github.com/BerriAI/litellm/pull/15965)
  - Support text.format parameter in Responses API for providers without native ResponsesAPIConfig - [PR #16023](https://github.com/BerriAI/litellm/pull/16023)
  - Add LLM provider response headers to Responses API - [PR #16091](https://github.com/BerriAI/litellm/pull/16091)
- [**Video Generation API**](https://docs.litellm.ai/docs/video_generation)
  
  - Add `custom_llm_provider` support for video endpoints (non-generation) - [PR #16121](https://github.com/BerriAI/litellm/pull/16121)
  - Fix documentation for videos - [PR #15937](https://github.com/BerriAI/litellm/pull/15937)
  - Add OpenAI client usage documentation for videos and fix navigation visibility - [PR #15996](https://github.com/BerriAI/litellm/pull/15996)
- [**Moderations API**](https://docs.litellm.ai/docs/moderations)
  
  - Moderations endpoint now respects `api_base` configuration parameter - [PR #16087](https://github.com/BerriAI/litellm/pull/16087)
- [**Vector Stores**](https://docs.litellm.ai/docs/vector_stores)
  
  - Milvus - search vector store support - [PR #16035](https://github.com/BerriAI/litellm/pull/16035)
  - Azure AI Vector Stores - support "virtual" indexes + create vector store on passthrough API - [PR #16160](https://github.com/BerriAI/litellm/pull/16160)
- [**Passthrough Endpoints**](https://docs.litellm.ai/docs/pass_through/vertex_ai)
  
  - Support multi-part form data on passthrough - [PR #16035](https://github.com/BerriAI/litellm/pull/16035)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Virtual Keys**
  
  - Validation for Proxy Base URL in SSO Settings - [PR #16082](https://github.com/BerriAI/litellm/pull/16082)
  - Test Key UI Embeddings support - [PR #16065](https://github.com/BerriAI/litellm/pull/16065)
  - Add Key Type Select in Key Settings - [PR #16034](https://github.com/BerriAI/litellm/pull/16034)
  - Key Already Exist Error Notification - [PR #15993](https://github.com/BerriAI/litellm/pull/15993)
- **Models + Endpoints**
  
  - Changed API Base from Select to Input in New LLM Credentials - [PR #15987](https://github.com/BerriAI/litellm/pull/15987)
  - Remove limit from admin UI numerical input - [PR #15991](https://github.com/BerriAI/litellm/pull/15991)
  - Config Models should not be editable - [PR #16020](https://github.com/BerriAI/litellm/pull/16020)
  - Add tags in model creation - [PR #16138](https://github.com/BerriAI/litellm/pull/16138)
  - Add Tags to update model - [PR #16140](https://github.com/BerriAI/litellm/pull/16140)
- **Guardrails**
  
  - Add Apply Guardrail Testing Playground - [PR #16030](https://github.com/BerriAI/litellm/pull/16030)
  - Config Guardrails should not be editable and guardrail info fix - [PR #16142](https://github.com/BerriAI/litellm/pull/16142)
- **Cache Settings**
  
  - Allow setting cache settings on UI - [PR #16143](https://github.com/BerriAI/litellm/pull/16143)
- **Routing**
  
  - Allow setting all routing strategies, tag filtering on UI - [PR #16139](https://github.com/BerriAI/litellm/pull/16139)
- **Admin Settings**
  
  - Add license metadata to health/readiness endpoint - [PR #15997](https://github.com/BerriAI/litellm/pull/15997)
  - Litellm Backend SSO Changes - [PR #16029](https://github.com/BerriAI/litellm/pull/16029)

* * *

## Logging / Guardrail / Prompt Management Integrations[​](#logging--guardrail--prompt-management-integrations "Direct link to Logging / Guardrail / Prompt Management Integrations")

#### Features[​](#features-3 "Direct link to Features")

- [**OpenTelemetry**](https://docs.litellm.ai/docs/proxy/logging#opentelemetry)
  
  - Enable OpenTelemetry context propagation by external tracers - [PR #15940](https://github.com/BerriAI/litellm/pull/15940)
  - Ensure error information is logged on OTEL - [PR #15978](https://github.com/BerriAI/litellm/pull/15978)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Fix duplicate trace in langfuse\_otel - [PR #15931](https://github.com/BerriAI/litellm/pull/15931)
  - Support tool usage messages with Langfuse OTEL integration - [PR #15932](https://github.com/BerriAI/litellm/pull/15932)
- [**DataDog**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Ensure key's metadata + guardrail is logged on DD - [PR #15980](https://github.com/BerriAI/litellm/pull/15980)
- [**Opik**](https://docs.litellm.ai/docs/proxy/logging#opik)
  
  - Enhance requester metadata retrieval from API key auth - [PR #15897](https://github.com/BerriAI/litellm/pull/15897)
  - User auth key metadata Documentation - [PR #16004](https://github.com/BerriAI/litellm/pull/16004)
- [**SQS**](https://docs.litellm.ai/docs/proxy/logging#sqs)
  
  - Add Base64 handling for SQS Logger - [PR #16028](https://github.com/BerriAI/litellm/pull/16028)
- **General**
  
  - Fix: User API key and team id and user id missing from custom callback is not misfiring - [PR #15982](https://github.com/BerriAI/litellm/pull/15982)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**IBM Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Update IBM Guardrails to correctly use SSL Verify argument - [PR #15975](https://github.com/BerriAI/litellm/pull/15975)
  - Add additional detail to ibm\_guardrails.md documentation - [PR #15971](https://github.com/BerriAI/litellm/pull/15971)
- [**Model Armor**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Support during\_call for model armor guardrails - [PR #15970](https://github.com/BerriAI/litellm/pull/15970)
- [**Lasso Security**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Upgrade to Lasso API v3 and fix ULID generation - [PR #15941](https://github.com/BerriAI/litellm/pull/15941)
- [**PANW Prisma AIRS**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Add per-request profile overrides to PANW Prisma AIRS - [PR #16069](https://github.com/BerriAI/litellm/pull/16069)
- [**Grayswan**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Improve Grayswan guardrail documentation - [PR #15875](https://github.com/BerriAI/litellm/pull/15875)
- [**Pillar AI**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Graceful degradation for pillar service when using litellm - [PR #15857](https://github.com/BerriAI/litellm/pull/15857)
- **General**
  
  - Ensure Key Guardrails are applied - [PR #16025](https://github.com/BerriAI/litellm/pull/16025)

#### Prompt Management[​](#prompt-management "Direct link to Prompt Management")

- [**GitLab**](https://docs.litellm.ai/docs/prompt_management)
  
  - Add GitlabPromptCache and enable subfolder access - [PR #15712](https://github.com/BerriAI/litellm/pull/15712)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Cost Tracking**
  
  - Fix spend tracking for OCR/aOCR requests (log `pages_processed` + recognize `OCRResponse`) - [PR #16070](https://github.com/BerriAI/litellm/pull/16070)
- **Rate Limiting**
  
  - Add support for Batch API Rate limiting - PR1 adds support for input based rate limits - [PR #16075](https://github.com/BerriAI/litellm/pull/16075)
  - Handle multiple rate limit types per descriptor and prevent IndexError - [PR #16039](https://github.com/BerriAI/litellm/pull/16039)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **OAuth**
  
  - Add support for dynamic client registration - [PR #15921](https://github.com/BerriAI/litellm/pull/15921)
  - Respect X-Forwarded- headers in OAuth endpoints - [PR #16036](https://github.com/BerriAI/litellm/pull/16036)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Memory Leak Fixes**
  
  - Fix: prevent httpx DeprecationWarning memory leak in AsyncHTTPHandler - [PR #16024](https://github.com/BerriAI/litellm/pull/16024)
  - Fix: resolve memory accumulation caused by Pydantic 2.11+ deprecation warnings - [PR #16110](https://github.com/BerriAI/litellm/pull/16110)
  - Fix(apscheduler): prevent memory leaks from jitter and frequent job intervals - [PR #15846](https://github.com/BerriAI/litellm/pull/15846)
- **Configuration**
  
  - Remove minimum validation for cache control injection index - [PR #16149](https://github.com/BerriAI/litellm/pull/16149)
  - Fix prompt\_caching.md: wrong prompt\_tokens definition - [PR #16044](https://github.com/BerriAI/litellm/pull/16044)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Use custom-llm-provider header in examples - [PR #16055](https://github.com/BerriAI/litellm/pull/16055)
  - Litellm docs readme fixes - [PR #16107](https://github.com/BerriAI/litellm/pull/16107)
  - Readme fixes add supported providers - [PR #16109](https://github.com/BerriAI/litellm/pull/16109)
- **Model References**
  
  - Add supports vision field to qwen-vl models in model\_prices\_and\_context\_window.json - [PR #16106](https://github.com/BerriAI/litellm/pull/16106)
- **General Documentation**
  
  - 1-79-0 docs - [PR #15936](https://github.com/BerriAI/litellm/pull/15936)
  - Add minimum resource requirement for production - [PR #16146](https://github.com/BerriAI/litellm/pull/16146)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @RobGeada made their first contribution in [PR #15975](https://github.com/BerriAI/litellm/pull/15975)
- @shanto12 made their first contribution in [PR #15946](https://github.com/BerriAI/litellm/pull/15946)
- @dima-hx430 made their first contribution in [PR #15976](https://github.com/BerriAI/litellm/pull/15976)
- @m-misiura made their first contribution in [PR #15971](https://github.com/BerriAI/litellm/pull/15971)
- @ylgibby made their first contribution in [PR #15947](https://github.com/BerriAI/litellm/pull/15947)
- @Somtom made their first contribution in [PR #15909](https://github.com/BerriAI/litellm/pull/15909)
- @rodolfo-nobrega made their first contribution in [PR #16023](https://github.com/BerriAI/litellm/pull/16023)
- @bernata made their first contribution in [PR #15997](https://github.com/BerriAI/litellm/pull/15997)
- @AlbertDeFusco made their first contribution in [PR #15881](https://github.com/BerriAI/litellm/pull/15881)
- @komarovd95 made their first contribution in [PR #15789](https://github.com/BerriAI/litellm/pull/15789)
- @langpingxue made their first contribution in [PR #15635](https://github.com/BerriAI/litellm/pull/15635)
- @OrionCodeDev made their first contribution in [PR #16070](https://github.com/BerriAI/litellm/pull/16070)
- @sbinnee made their first contribution in [PR #16078](https://github.com/BerriAI/litellm/pull/16078)
- @JetoPistola made their first contribution in [PR #16106](https://github.com/BerriAI/litellm/pull/16106)
- @gvioss made their first contribution in [PR #16093](https://github.com/BerriAI/litellm/pull/16093)
- @pale-aura made their first contribution in [PR #16084](https://github.com/BerriAI/litellm/pull/16084)
- @tanvithakur94 made their first contribution in [PR #16041](https://github.com/BerriAI/litellm/pull/16041)
- @li-boxuan made their first contribution in [PR #16044](https://github.com/BerriAI/litellm/pull/16044)
- @1stprinciple made their first contribution in [PR #15938](https://github.com/BerriAI/litellm/pull/15938)
- @raghav-stripe made their first contribution in [PR #16137](https://github.com/BerriAI/litellm/pull/16137)
- @steve-gore-snapdocs made their first contribution in [PR #16149](https://github.com/BerriAI/litellm/pull/16149)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.79.0-stable...v1.80.0-stable)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.79.0-stable
```

* * *

## Major Changes[​](#major-changes "Direct link to Major Changes")

- **Cohere models will now be routed to Cohere v2 API by default** - [PR #15722](https://github.com/BerriAI/litellm/pull/15722)

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Search APIs** - Native `/v1/search` endpoint with support for Perplexity, Tavily, Parallel AI, Exa AI, DataforSEO, and Google PSE with cost tracking
- **Vector Stores** - Vertex AI Search API integration as vector store through LiteLLM with passthrough endpoint support
- **Guardrails Expansion** - Apply guardrails across Responses API, Image Gen, Text completions, Audio transcriptions, Audio Speech, Rerank, and Anthropic Messages API via unified `apply_guardrails` function
- **New Guardrail Providers** - Gray Swan, Dynamo AI, IBM Guardrails, Lasso Security v3, and Bedrock Guardrail apply\_guardrail endpoint support
- **Video Generation API** - Native support for OpenAI Sora-2 and Azure Sora-2 (Pro, Pro-High-Res) with cost tracking and logging support
- **Azure AI Speech (TTS)** - Native Azure AI Speech integration with cost tracking for standard and HD voices

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesBedrock`anthropic.claude-3-7-sonnet-20240620-v1:0`200K$3.60$18.00Chat, reasoning, vision, function calling, prompt caching, computer useBedrock GovCloud`us-gov-west-1/anthropic.claude-3-7-sonnet-20250219-v1:0`200K$3.60$18.00Chat, reasoning, vision, function calling, prompt caching, computer useVertex AI`mistral-medium-3`128K$0.40$2.00Chat, function calling, tool choiceVertex AI`codestral-2`128K$0.30$0.90Chat, function calling, tool choiceBedrock`amazon.titan-image-generator-v1`---Image generation - $0.008/image, $0.01/premium imageBedrock`amazon.titan-image-generator-v2`---Image generation - $0.008/image, $0.01/premium imageOpenAI`sora-2`---Video generation - $0.10/video/secondAzure`sora-2`---Video generation - $0.10/video/secondAzure`sora-2-pro`---Video generation - $0.30/video/secondAzure`sora-2-pro-high-res`---Video generation - $0.50/video/second

#### Features[​](#features "Direct link to Features")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Fix cache\_control incorrectly applied to all content items instead of last item only - [PR #15699](https://github.com/BerriAI/litellm/pull/15699)
  - Forward anthropic-beta headers to Bedrock, VertexAI - [PR #15700](https://github.com/BerriAI/litellm/pull/15700)
  - Change max\_tokens value to match max\_output\_tokens for claude sonnet - [PR #15715](https://github.com/BerriAI/litellm/pull/15715)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add AWS us-gov-west-1 Claude 3.7 Sonnet costs - [PR #15775](https://github.com/BerriAI/litellm/pull/15775)
  - Fix the date for sonnet 3.7 in govcloud - [PR #15800](https://github.com/BerriAI/litellm/pull/15800)
  - Use proper bedrock model name in health check - [PR #15808](https://github.com/BerriAI/litellm/pull/15808)
  - Support for embeddings\_by\_type Response Format in Bedrock Cohere Embed v1 - [PR #15707](https://github.com/BerriAI/litellm/pull/15707)
  - Add titan image generations with cost tracking - [PR #15916](https://github.com/BerriAI/litellm/pull/15916)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add imageConfig parameter for gemini-2.5-flash-image - [PR #15530](https://github.com/BerriAI/litellm/pull/15530)
  - Replace deprecated gemini-1.5-pro-preview-0514 - [PR #15852](https://github.com/BerriAI/litellm/pull/15852)
  - Update vertex ai gemini costs - [PR #15911](https://github.com/BerriAI/litellm/pull/15911)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Set 'think' to False when reasoning effort is minimal/none/disable - [PR #15763](https://github.com/BerriAI/litellm/pull/15763)
  - Handle parsing ollama chunk error - [PR #15717](https://github.com/BerriAI/litellm/pull/15717)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add mistral medium 3 and Codestral 2 on vertex - [PR #15887](https://github.com/BerriAI/litellm/pull/15887)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks)
  
  - Allow prompt caching to be used for Anthropic Claude on Databricks - [PR #15801](https://github.com/BerriAI/litellm/pull/15801)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Add Azure AVA TTS integration - [PR #15749](https://github.com/BerriAI/litellm/pull/15749)
  - Add Azure AVA (Speech AI) Cost Tracking - [PR #15754](https://github.com/BerriAI/litellm/pull/15754)
  - Azure AI Speech - Ensure `voice` is mapped from request body to SSML body, allow sending `role` and `style` - [PR #15810](https://github.com/BerriAI/litellm/pull/15810)
  - Add Azure support for video generation functionality (Sora-2) - [PR #15901](https://github.com/BerriAI/litellm/pull/15901)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - OpenAI videos refactoring - [PR #15900](https://github.com/BerriAI/litellm/pull/15900)
- **General**
  
  - Read from custom-llm-provider header - [PR #15528](https://github.com/BerriAI/litellm/pull/15528)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Add gpt 4.1 pricing for response endpoint - [PR #15593](https://github.com/BerriAI/litellm/pull/15593)
  - Fix Incorrect status value in responses api with gemini - [PR #15753](https://github.com/BerriAI/litellm/pull/15753)
  - Simplify reasoning item handling for gpt-5-codex - [PR #15815](https://github.com/BerriAI/litellm/pull/15815)
  - ErrorEvent ValidationError when OpenAI Responses API returns nested error structure - [PR #15804](https://github.com/BerriAI/litellm/pull/15804)
  - Fix reasoning item ID auto-generation causing encrypted content verification errors - [PR #15782](https://github.com/BerriAI/litellm/pull/15782)
  - Support tags in metadata - [PR #15867](https://github.com/BerriAI/litellm/pull/15867)
  - Security: prevent User A from retrieving User B's response, if response.id is leaked - [PR #15757](https://github.com/BerriAI/litellm/pull/15757)
- [**Batch API**](https://docs.litellm.ai/docs/batch_api)
  
  - Add pre and post call for list batches - [PR #15673](https://github.com/BerriAI/litellm/pull/15673)
  - Add function responsible to call precall - [PR #15636](https://github.com/BerriAI/litellm/pull/15636)
  - Fix "User default\_user\_id does not have access to the object" when object not in db - [PR #15873](https://github.com/BerriAI/litellm/pull/15873)
- [**OCR API**](https://docs.litellm.ai/docs/ocr)
  
  - Add Azure AI - OCR to docs - [PR #15768](https://github.com/BerriAI/litellm/pull/15768)
  - Add mode + Health check support for OCR models - [PR #15767](https://github.com/BerriAI/litellm/pull/15767)
- [**Search API**](https://docs.litellm.ai/docs/search_api)
  
  - Add def search() APIs for Web Search - Perplexity API - [PR #15769](https://github.com/BerriAI/litellm/pull/15769)
  - Add Tavily Search API - [PR #15770](https://github.com/BerriAI/litellm/pull/15770)
  - Add Parallel AI - Search API - [PR #15772](https://github.com/BerriAI/litellm/pull/15772)
  - Add EXA AI Search API to LiteLLM - [PR #15774](https://github.com/BerriAI/litellm/pull/15774)
  - Add /search endpoint on LiteLLM Gateway - [PR #15780](https://github.com/BerriAI/litellm/pull/15780)
  - Add DataforSEO Search API - [PR #15817](https://github.com/BerriAI/litellm/pull/15817)
  - Add Google PSE Search Provider - [PR #15816](https://github.com/BerriAI/litellm/pull/15816)
  - Add cost tracking for Search API requests - Google PSE, Tavily, Parallel AI, Exa AI - [PR #15821](https://github.com/BerriAI/litellm/pull/15821)
  - Backend: Allow storing configured Search APIs in DB - [PR #15862](https://github.com/BerriAI/litellm/pull/15862)
  - Exa Search API - ensure request params are sent to Exa AI - [PR #15855](https://github.com/BerriAI/litellm/pull/15855)
- [**Vector Stores**](https://docs.litellm.ai/docs/vector_stores)
  
  - Support Vertex AI Search API as vector store through LiteLLM - [PR #15781](https://github.com/BerriAI/litellm/pull/15781)
  - Azure AI - Search Vector Stores - [PR #15873](https://github.com/BerriAI/litellm/pull/15873)
  - VertexAI Search Vector Store - Passthrough endpoint support + Vector store search Cost tracking support - [PR #15824](https://github.com/BerriAI/litellm/pull/15824)
  - Don't raise error if managed object is not found - [PR #15873](https://github.com/BerriAI/litellm/pull/15873)
  - Show config.yaml vector stores on UI - [PR #15873](https://github.com/BerriAI/litellm/pull/15873)
  - Cost tracking for search spend - [PR #15859](https://github.com/BerriAI/litellm/pull/15859)
- [**Images API**](https://docs.litellm.ai/docs/image_generation)
  
  - Pass user-defined headers and extra\_headers to image-edit calls - [PR #15811](https://github.com/BerriAI/litellm/pull/15811)
- [**Video Generation API**](https://docs.litellm.ai/docs/video_generation)
  
  - Add Azure support for video generation functionality (Sora-2, Sora-2-Pro, Sora-2-Pro-High-Res) - [PR #15901](https://github.com/BerriAI/litellm/pull/15901)
  - OpenAI video generation refactoring (Sora-2) - [PR #15900](https://github.com/BerriAI/litellm/pull/15900)
- [**Bedrock /invoke**](https://docs.litellm.ai/docs/bedrock_invoke)
  
  - Fix: Hooks broken on /bedrock passthrough due to missing metadata - [PR #15849](https://github.com/BerriAI/litellm/pull/15849)
- [**Realtime API**](https://docs.litellm.ai/docs/realtime_api)
  
  - Fix: OpenAI Realtime API integration fails due to websockets.exceptions.PayloadTooBig error - [PR #15751](https://github.com/BerriAI/litellm/pull/15751)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Passthrough**
  
  - Set auth on passthrough endpoints, on the UI - [PR #15778](https://github.com/BerriAI/litellm/pull/15778)
  - Fix pass-through endpoint budget enforcement bug - [PR #15805](https://github.com/BerriAI/litellm/pull/15805)
- **Organizations**
  
  - Allow org admins to create teams on UI - [PR #15924](https://github.com/BerriAI/litellm/pull/15924)
- **Search Tools**
  
  - UI - Search Tools, allow adding search tools on UI + testing search - [PR #15871](https://github.com/BerriAI/litellm/pull/15871)
  - UI - Add logos for search providers - [PR #15872](https://github.com/BerriAI/litellm/pull/15872)
- **General**
  
  - Fix routing for custom server root path - [PR #15701](https://github.com/BerriAI/litellm/pull/15701)

* * *

## Logging / Guardrail / Prompt Management Integrations[​](#logging--guardrail--prompt-management-integrations "Direct link to Logging / Guardrail / Prompt Management Integrations")

#### Features[​](#features-3 "Direct link to Features")

- [**OpenTelemetry**](https://docs.litellm.ai/docs/proxy/logging#opentelemetry)
  
  - Fix OpenTelemetry Logging functionality - [PR #15645](https://github.com/BerriAI/litellm/pull/15645)
  - Fix issue where headers were not being split correctly - [PR #15916](https://github.com/BerriAI/litellm/pull/15916)
- [**Sentry**](https://docs.litellm.ai/docs/proxy/logging#sentry)
  
  - Add SENTRY\_ENVIRONMENT configuration for Sentry integration - [PR #15760](https://github.com/BerriAI/litellm/pull/15760)
- [**Helicone**](https://docs.litellm.ai/docs/proxy/logging#helicone)
  
  - Fix JSON serialization error in Helicone logging by removing OpenTelemetry span from metadata - [PR #15728](https://github.com/BerriAI/litellm/pull/15728)
- [**MLFlow**](https://docs.litellm.ai/docs/proxy/logging#mlflow)
  
  - Fix MLFlow tags - split request\_tags into (key, val) if request\_tag has colon - [PR #15914](https://github.com/BerriAI/litellm/pull/15914)
- **General**
  
  - Rename configured\_cold\_storage\_logger to cold\_storage\_custom\_logger - [PR #15798](https://github.com/BerriAI/litellm/pull/15798)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**Gray Swan**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Add GraySwan Guardrails support - [PR #15756](https://github.com/BerriAI/litellm/pull/15756)
  - Rename GraySwan to Gray Swan - [PR #15771](https://github.com/BerriAI/litellm/pull/15771)
- [**Dynamo AI**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - New Guardrail - Dynamo AI Guardrail - [PR #15920](https://github.com/BerriAI/litellm/pull/15920)
- [**IBM Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - IBM Guardrails integration - [PR #15924](https://github.com/BerriAI/litellm/pull/15924)
- [**Lasso Security**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Add v3 API Support - [PR #12452](https://github.com/BerriAI/litellm/pull/12452)
  - Fixed lasso import config, redis cluster hash tags for test keys - [PR #15917](https://github.com/BerriAI/litellm/pull/15917)
- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Implement Bedrock Guardrail apply\_guardrail endpoint support - [PR #15892](https://github.com/BerriAI/litellm/pull/15892)
- **General**
  
  - Guardrails - Responses API, Image Gen, Text completions, Audio transcriptions, Audio Speech, Rerank, Anthropic Messages API support via the unified `apply_guardrails` function - [PR #15706](https://github.com/BerriAI/litellm/pull/15706)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Rate Limiting**
  
  - Support absolute RPM/TPM in priority\_reservation - [PR #15813](https://github.com/BerriAI/litellm/pull/15813)
  - Org level tpm/rpm limits + Team tpm/rpm validation when assigned to org - [PR #15549](https://github.com/BerriAI/litellm/pull/15549)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **OAuth**
  
  - Auth Header Fix for MCP Tool Call - [PR #15736](https://github.com/BerriAI/litellm/pull/15736)
  - Add response\_type + PKCE parameters to OAuth authorization endpoint - [PR #15720](https://github.com/BerriAI/litellm/pull/15720)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Database**
  
  - Minimize the occurrence of deadlocks - [PR #15281](https://github.com/BerriAI/litellm/pull/15281)
- **Redis**
  
  - Apply max\_connections configuration to Redis async client - [PR #15797](https://github.com/BerriAI/litellm/pull/15797)
- **Caching**
  
  - Add documentation for `enable_caching_on_provider_specific_optional_params` setting - [PR #15885](https://github.com/BerriAI/litellm/pull/15885)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Update worker recommendation - [PR #15702](https://github.com/BerriAI/litellm/pull/15702)
  - Fix the wrong request body in json mode doc - [PR #15729](https://github.com/BerriAI/litellm/pull/15729)
  - Add details in docs - [PR #15721](https://github.com/BerriAI/litellm/pull/15721)
  - Add responses api on openai docs - [PR #15866](https://github.com/BerriAI/litellm/pull/15866)
  - Add OpenAI responses api - [PR #15868](https://github.com/BerriAI/litellm/pull/15868)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @tlecomte made their first contribution in [PR #15528](https://github.com/BerriAI/litellm/pull/15528)
- @tomhaynes made their first contribution in [PR #15645](https://github.com/BerriAI/litellm/pull/15645)
- @talalryz made their first contribution in [PR #15720](https://github.com/BerriAI/litellm/pull/15720)
- @1vinodsingh1 made their first contribution in [PR #15736](https://github.com/BerriAI/litellm/pull/15736)
- @nuernber made their first contribution in [PR #15775](https://github.com/BerriAI/litellm/pull/15775)
- @Thomas-Mildner made their first contribution in [PR #15760](https://github.com/BerriAI/litellm/pull/15760)
- @javiergarciapleo made their first contribution in [PR #15721](https://github.com/BerriAI/litellm/pull/15721)
- @lshgdut made their first contribution in [PR #15717](https://github.com/BerriAI/litellm/pull/15717)
- @kk-wangjifeng made their first contribution in [PR #15530](https://github.com/BerriAI/litellm/pull/15530)
- @anthonyivn2 made their first contribution in [PR #15801](https://github.com/BerriAI/litellm/pull/15801)
- @romanglo made their first contribution in [PR #15707](https://github.com/BerriAI/litellm/pull/15707)
- @mythral made their first contribution in [PR #15859](https://github.com/BerriAI/litellm/pull/15859)
- @mubashirosmani made their first contribution in [PR #15866](https://github.com/BerriAI/litellm/pull/15866)
- @CAFxX made their first contribution in [PR #15281](https://github.com/BerriAI/litellm/pull/15281)
- @reflection made their first contribution in [PR #15914](https://github.com/BerriAI/litellm/pull/15914)
- @shadielfares made their first contribution in [PR #15917](https://github.com/BerriAI/litellm/pull/15917)

* * *

## PR Count Summary[​](#pr-count-summary "Direct link to PR Count Summary")

### 10/26/2025[​](#10262025 "Direct link to 10/26/2025")

- New Models / Updated Models: 20
- LLM API Endpoints: 29
- Management Endpoints / UI: 5
- Logging / Guardrail / Prompt Management Integrations: 10
- Spend Tracking, Budgets and Rate Limiting: 2
- MCP Gateway: 2
- Performance / Loadbalancing / Reliability improvements: 3
- Documentation Updates: 5

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.78.5-stable...v1.79.0-stable)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.78.5-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Native OCR Endpoints** - Native `/v1/ocr` endpoint support with cost tracking for Mistral OCR and Azure AI OCR
- **Global Vendor Discounts** - Specify global vendor discount percentages for accurate cost tracking and reporting
- **Team Spending Reports** - Team admins can now export detailed spending reports for their teams
- **Claude Haiku 4.5** - Day 0 support for Claude Haiku 4.5 across Bedrock, Vertex AI, and OpenRouter with 200K context window
- **GPT-5-Codex** - Support for GPT-5-Codex via Responses API on OpenAI and Azure
- **Performance Improvements** - Major router optimizations: O(1) model lookups, 10-100x faster shallow copy, 30-40% faster timing calls, and O(n) to O(1) hash generation

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesAnthropic`claude-haiku-4-5`200K$1.00$5.00Chat, reasoning, vision, function calling, prompt caching, computer useAnthropic`claude-haiku-4-5-20251001`200K$1.00$5.00Chat, reasoning, vision, function calling, prompt caching, computer useBedrock`anthropic.claude-haiku-4-5-20251001-v1:0`200K$1.00$5.00Chat, reasoning, vision, function calling, prompt cachingBedrock`global.anthropic.claude-haiku-4-5-20251001-v1:0`200K$1.00$5.00Chat, reasoning, vision, function calling, prompt cachingBedrock`jp.anthropic.claude-haiku-4-5-20251001-v1:0`200K$1.10$5.50Chat, reasoning, vision, function calling, prompt caching (JP Cross-Region)Bedrock`us.anthropic.claude-haiku-4-5-20251001-v1:0`200K$1.10$5.50Chat, reasoning, vision, function calling, prompt caching (US region)Bedrock`eu.anthropic.claude-haiku-4-5-20251001-v1:0`200K$1.10$5.50Chat, reasoning, vision, function calling, prompt caching (EU region)Bedrock`apac.anthropic.claude-haiku-4-5-20251001-v1:0`200K$1.10$5.50Chat, reasoning, vision, function calling, prompt caching (APAC region)Bedrock`au.anthropic.claude-haiku-4-5-20251001-v1:0`200K$1.10$5.50Chat, reasoning, vision, function calling, prompt caching (AU region)Vertex AI`vertex_ai/claude-haiku-4-5@20251001`200K$1.00$5.00Chat, reasoning, vision, function calling, prompt cachingOpenAI`gpt-5`272K$1.25$10.00Chat, responses API, reasoning, vision, function calling, prompt cachingOpenAI`gpt-5-codex`272K$1.25$10.00Responses API modeAzure`azure/gpt-5-codex`272K$1.25$10.00Responses API modeGemini`gemini-2.5-flash-image`32K$0.30$2.50Image generation (GA - Nano Banana) - $0.039/imageZhipuAI`glm-4.6`---Chat completions

#### Features[​](#features "Direct link to Features")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - GPT-5 return reasoning content via /chat/completions + GPT-5-Codex working on Claude Code - [PR #15441](https://github.com/BerriAI/litellm/pull/15441)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Reduce claude-4-sonnet max\_output\_tokens to 64k - [PR #15409](https://github.com/BerriAI/litellm/pull/15409)
  - Added claude-haiku-4.5 - [PR #15579](https://github.com/BerriAI/litellm/pull/15579)
  - Add support for thinking blocks and redacted thinking blocks in Anthropic v1/messages API - [PR #15501](https://github.com/BerriAI/litellm/pull/15501)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add anthropic.claude-haiku-4-5-20251001-v1:0 on Bedrock, VertexAI - [PR #15581](https://github.com/BerriAI/litellm/pull/15581)
  - Add Claude Haiku 4.5 support for Bedrock global and US regions - [PR #15650](https://github.com/BerriAI/litellm/pull/15650)
  - Add Claude Haiku 4.5 support for Bedrock Other regions - [PR #15653](https://github.com/BerriAI/litellm/pull/15653)
  - Add JP Cross-Region Inference jp.anthropic.claude-haiku-4-5-20251001 - [PR #15598](https://github.com/BerriAI/litellm/pull/15598)
  - Fix: bedrock-pricing-geo-inregion-cross-region / add Global Cross-Region Inference - [PR #15685](https://github.com/BerriAI/litellm/pull/15685)
  - Fix: Support us-gov prefix for AWS GovCloud Bedrock models - [PR #15626](https://github.com/BerriAI/litellm/pull/15626)
  - Fix GPT-OSS in Bedrock now supports streaming. Revert fake streaming - [PR #15668](https://github.com/BerriAI/litellm/pull/15668)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Feat(pricing): Add Gemini 2.5 Flash Image (Nano Banana) in GA - [PR #15557](https://github.com/BerriAI/litellm/pull/15557)
  - Fix: Gemini 2.5 Flash Image should not have supports\_web\_search=true - [PR #15642](https://github.com/BerriAI/litellm/pull/15642)
  - Remove penalty params as supported params for gemini preview model - [PR #15503](https://github.com/BerriAI/litellm/pull/15503)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Fix(ollama/chat): correctly map reasoning\_effort to think in requests - [PR #15465](https://github.com/BerriAI/litellm/pull/15465)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Add anthropic/claude-sonnet-4.5 to OpenRouter cost map - [PR #15472](https://github.com/BerriAI/litellm/pull/15472)
  - Prompt caching for anthropic models with OpenRouter - [PR #15535](https://github.com/BerriAI/litellm/pull/15535)
  - Get completion cost directly from OpenRouter - [PR #15448](https://github.com/BerriAI/litellm/pull/15448)
  - Fix OpenRouter Claude Opus 4 model naming - [PR #15495](https://github.com/BerriAI/litellm/pull/15495)
- [**CometAPI**](https://docs.litellm.ai/docs/providers/comet)
  
  - Fix(cometapi): improve CometAPI provider support (embeddings, image generation, docs) - [PR #15591](https://github.com/BerriAI/litellm/pull/15591)
- [**Lemonade**](https://docs.litellm.ai/docs/providers/lemonade)
  
  - Adding new models to the lemonade provider - [PR #15554](https://github.com/BerriAI/litellm/pull/15554)
- [**Watson X**](https://docs.litellm.ai/docs/providers/watsonx)
  
  - Fix (pricing): Fix pricing for watsonx model family for various models - [PR #15670](https://github.com/BerriAI/litellm/pull/15670)
- [**Vercel AI Gateway**](https://docs.litellm.ai/docs/providers/vercel_ai_gateway)
  
  - Add glm-4.6 model to pricing configuration - [PR #15679](https://github.com/BerriAI/litellm/pull/15679)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add Vertex AI Discovery Engine Rerank Support - [PR #15532](https://github.com/BerriAI/litellm/pull/15532)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Fix: Pricing for Claude Sonnet 4.5 in US regions is 10x too high - [PR #15374](https://github.com/BerriAI/litellm/pull/15374)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Change gpt-5-codex support in model\_price json - [PR #15540](https://github.com/BerriAI/litellm/pull/15540)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fix filtering headers for signature calcs - [PR #15590](https://github.com/BerriAI/litellm/pull/15590)
- **General**
  
  - Add native reasoning and streaming support flag for gpt-5-codex - [PR #15569](https://github.com/BerriAI/litellm/pull/15569)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Responses API - enable calling anthropic/gemini models in Responses API streaming in openai ruby sdk + DB - sanity check pending migrations before startup - [PR #15432](https://github.com/BerriAI/litellm/pull/15432)
  - Add support for responses mode in health check - [PR #15658](https://github.com/BerriAI/litellm/pull/15658)
- [**OCR API**](https://docs.litellm.ai/docs/ocr)
  
  - Feat: Add native litellm.ocr() functions - [PR #15567](https://github.com/BerriAI/litellm/pull/15567)
  - Feat: Add /ocr route on LiteLLM AI Gateway - Adds support for native Mistral OCR calling - [PR #15571](https://github.com/BerriAI/litellm/pull/15571)
  - Feat: Add Azure AI Mistral OCR Integration - [PR #15572](https://github.com/BerriAI/litellm/pull/15572)
  - Feat: Native /ocr endpoint support - [PR #15573](https://github.com/BerriAI/litellm/pull/15573)
  - Feat: Add Cost Tracking for /ocr endpoints - [PR #15678](https://github.com/BerriAI/litellm/pull/15678)
- [**/generateContent**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix: GEMINI - CLI - add google\_routes to llm\_api\_routes - [PR #15500](https://github.com/BerriAI/litellm/pull/15500)
  - Fix Pydantic validation error for citationMetadata.citationSources in Google GenAI responses - [PR #15592](https://github.com/BerriAI/litellm/pull/15592)
- [**Images API**](https://docs.litellm.ai/docs/image_generation)
  
  - Fix: Dall-e-2 for Image Edits API - [PR #15604](https://github.com/BerriAI/litellm/pull/15604)
- [**Bedrock Passthrough**](https://docs.litellm.ai/docs/pass_through/bedrock)
  
  - Feat: Allow calling /invoke, /converse routes through AI Gateway + models on config.yaml - [PR #15618](https://github.com/BerriAI/litellm/pull/15618)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Fix: Convert object to a correct type - [PR #15634](https://github.com/BerriAI/litellm/pull/15634)
  - Bug Fix: Tags as metadata dicts were raising exceptions - [PR #15625](https://github.com/BerriAI/litellm/pull/15625)
  - Add type hint to function\_to\_dict and fix typo - [PR #15580](https://github.com/BerriAI/litellm/pull/15580)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Virtual Keys**
  
  - Docs: Key Rotations - [PR #15455](https://github.com/BerriAI/litellm/pull/15455)
  - Fix: UI - Key Max Budget Removal Error Fix - [PR #15672](https://github.com/BerriAI/litellm/pull/15672)
  - litellm\_Key Settings Max Budget Removal Error Fix - [PR #15669](https://github.com/BerriAI/litellm/pull/15669)
- **Teams**
  
  - Feat: Allow Team Admins to export a report of the team spending - [PR #15542](https://github.com/BerriAI/litellm/pull/15542)
- **Passthrough**
  
  - Feat: Passthrough - allow admin to give access to specific passthrough endpoints - [PR #15401](https://github.com/BerriAI/litellm/pull/15401)
- **SCIM v2**
  
  - Feat(scim\_v2.py): if group.id doesn't exist, use external id + Passthrough - ensure updates and deletions persist across instances - [PR #15276](https://github.com/BerriAI/litellm/pull/15276)
- **SSO**
  
  - Feat: UI SSO - Add PKCE for OKTA SSO - [PR #15608](https://github.com/BerriAI/litellm/pull/15608)
  - Fix: Separate OAuth M2M authentication from UI SSO + Handle Introspection endpoint for Oauth2 - [PR #15667](https://github.com/BerriAI/litellm/pull/15667)
  - Fix/entraid app roles jwt claim clean - [PR #15583](https://github.com/BerriAI/litellm/pull/15583)

* * *

## Logging / Guardrail / Prompt Management Integrations[​](#logging--guardrail--prompt-management-integrations "Direct link to Logging / Guardrail / Prompt Management Integrations")

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- **General**
  
  - Fix apply\_guardrail endpoint returning raw string instead of ApplyGuardrailResponse - [PR #15436](https://github.com/BerriAI/litellm/pull/15436)
  - Fix: Ensure guardrail memory sync after database updates - [PR #15633](https://github.com/BerriAI/litellm/pull/15633)
  - Feat: add guardrail for image generation - [PR #15619](https://github.com/BerriAI/litellm/pull/15619)
  - Feat: Add Guardrails for /v1/messages and /v1/responses API - [PR #15686](https://github.com/BerriAI/litellm/pull/15686)
- [**Pillar Security**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Feature: update pillar security integration to support no persistence mode in litellm proxy - [PR #15599](https://github.com/BerriAI/litellm/pull/15599)

#### Prompt Management[​](#prompt-management "Direct link to Prompt Management")

- **General**
  
  - Small fix code snippet custom\_prompt\_management.md - [PR #15544](https://github.com/BerriAI/litellm/pull/15544)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Cost Tracking**
  
  - Feat: Cost Tracking - specify a global vendor discount for costs - [PR #15546](https://github.com/BerriAI/litellm/pull/15546)
  - Feat: UI - Allow setting Provider Discounts on UI - [PR #15550](https://github.com/BerriAI/litellm/pull/15550)
- **Budgets**
  
  - Fix: improve budget clarity - [PR #15682](https://github.com/BerriAI/litellm/pull/15682)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Router Optimizations**
  
  - Perf(router): use shallow copy instead of deepcopy for model aliases - 10-100x faster than deepcopy on nested dict structures - [PR #15576](https://github.com/BerriAI/litellm/pull/15576)
  - Perf(router): optimize string concatenation in hash generation - Improves time complexity from O(n²) to O(n) - [PR #15575](https://github.com/BerriAI/litellm/pull/15575)
  - Perf(router): optimize model lookups with O(1) data structures - Replace O(n) scans with index map lookups - [PR #15578](https://github.com/BerriAI/litellm/pull/15578)
  - Perf(router): optimize model lookups with O(1) index maps - Use model\_id\_to\_deployment\_index\_map and model\_name\_to\_deployment\_indices for instant lookups - [PR #15574](https://github.com/BerriAI/litellm/pull/15574)
  - Perf(router): optimize timing functions in completion hot path - Use time.perf\_counter() for duration measurements and time.monotonic() for timeout calculations, providing 30-40% faster timing calls - [PR #15617](https://github.com/BerriAI/litellm/pull/15617)
- **SSL/TLS Performance**
  
  - Feat(ssl): add configurable ECDH curve for TLS performance - Configure via ssl\_ecdh\_curve setting to disable PQC on OpenSSL 3.x for better performance - [PR #15617](https://github.com/BerriAI/litellm/pull/15617)
- **Token Counter**
  
  - Fix(token-counter): extract model\_info from deployment for custom\_tokenizer - [PR #15680](https://github.com/BerriAI/litellm/pull/15680)
- **Performance Metrics**
  
  - Add: perf summary - [PR #15458](https://github.com/BerriAI/litellm/pull/15458)
- **CI/CD**
  
  - Fix: CI/CD - Missing env key & Linter type error - [PR #15606](https://github.com/BerriAI/litellm/pull/15606)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Litellm docs 10 11 2025 - [PR #15457](https://github.com/BerriAI/litellm/pull/15457)
  - Docs: add ecs deployment guide - [PR #15468](https://github.com/BerriAI/litellm/pull/15468)
  - Docs: Update benchmark results - [PR #15461](https://github.com/BerriAI/litellm/pull/15461)
  - Fix: add missing context to benchmark docs - [PR #15688](https://github.com/BerriAI/litellm/pull/15688)
- **General**
  
  - Fixed a few typos - [PR #15267](https://github.com/BerriAI/litellm/pull/15267)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @jlan-nl made their first contribution in [PR #15374](https://github.com/BerriAI/litellm/pull/15374)
- @ImadSaddik made their first contribution in [PR #15267](https://github.com/BerriAI/litellm/pull/15267)
- @huangyafei made their first contribution in [PR #15472](https://github.com/BerriAI/litellm/pull/15472)
- @mubashir1osmani made their first contribution in [PR #15468](https://github.com/BerriAI/litellm/pull/15468)
- @kowyo made their first contribution in [PR #15465](https://github.com/BerriAI/litellm/pull/15465)
- @dhruvyad made their first contribution in [PR #15448](https://github.com/BerriAI/litellm/pull/15448)
- @davizucon made their first contribution in [PR #15544](https://github.com/BerriAI/litellm/pull/15544)
- @FelipeRodriguesGare made their first contribution in [PR #15540](https://github.com/BerriAI/litellm/pull/15540)
- @ndrsfel made their first contribution in [PR #15557](https://github.com/BerriAI/litellm/pull/15557)
- @shinharaguchi made their first contribution in [PR #15598](https://github.com/BerriAI/litellm/pull/15598)
- @TensorNull made their first contribution in [PR #15591](https://github.com/BerriAI/litellm/pull/15591)
- @TeddyAmkie made their first contribution in [PR #15583](https://github.com/BerriAI/litellm/pull/15583)
- @aniketmaurya made their first contribution in [PR #15580](https://github.com/BerriAI/litellm/pull/15580)
- @eddierichter-amd made their first contribution in [PR #15554](https://github.com/BerriAI/litellm/pull/15554)
- @konekohana made their first contribution in [PR #15535](https://github.com/BerriAI/litellm/pull/15535)
- @Classic298 made their first contribution in [PR #15495](https://github.com/BerriAI/litellm/pull/15495)
- @afogel made their first contribution in [PR #15599](https://github.com/BerriAI/litellm/pull/15599)
- @orolega made their first contribution in [PR #15633](https://github.com/BerriAI/litellm/pull/15633)
- @LucasSugi made their first contribution in [PR #15634](https://github.com/BerriAI/litellm/pull/15634)
- @uc4w6c made their first contribution in [PR #15619](https://github.com/BerriAI/litellm/pull/15619)
- @Sameerlite made their first contribution in [PR #15658](https://github.com/BerriAI/litellm/pull/15658)
- @yuneng-jiang made their first contribution in [PR #15672](https://github.com/BerriAI/litellm/pull/15672)
- @Nikro made their first contribution in [PR #15680](https://github.com/BerriAI/litellm/pull/15680)

* * *

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

[**View complete changelog on GitHub**](https://github.com/BerriAI/litellm/compare/v1.78.0-stable...v1.78.4-stable)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.78.0-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **MCP Gateway - Control Tool Access by Team, Key** - Control MCP tool access by team/key.
- **Performance Improvements** - 70% Lower p99 Latency
- **GPT-5 Pro & GPT-Image-1-Mini** - Day 0 support for OpenAI's GPT-5 Pro (400K context) and gpt-image-1-mini image generation
- **EnkryptAI Guardrails** - New guardrail integration for content moderation
- **Tag-Based Budgets** - Support for setting budgets based on request tags

* * *

### MCP Gateway - Control Tool Access by Team, Key[​](#mcp-gateway---control-tool-access-by-team-key "Direct link to MCP Gateway - Control Tool Access by Team, Key")

Proxy admins can now control MCP tool access by team or key. This makes it easy to grant different teams selective access to tools from the same MCP server.

For example, you can now give your Engineering team access to `list_repositories`, `create_issue`, and `search_code` tools, while Sales only gets `search_code` and `close_issue` tools.

This makes it easier for Proxy Admins to govern MCP Tool Access.

[Get Started](https://docs.litellm.ai/docs/mcp_control#set-allowed-tools-for-a-key-team-or-organization)

* * *

## Performance - 70% Lower p99 Latency[​](#performance---70-lower-p99-latency "Direct link to Performance - 70% Lower p99 Latency")

This release cuts p99 latency by 70% on LiteLLM AI Gateway, making it even better for low-latency use cases.

These gains come from two key enhancements:

**Reliable Sessions**

Added support for shared sessions with aiohttp. The shared\_session parameter is now consistently used across all calls, enabling connection pooling.

**Faster Routing**

A new `model_name_to_deployment_indices` hash map replaces O(n) list scans in `_get_all_deployments()` with O(1) hash lookups, boosting routing performance and scalability.

As a result, performance improved across all latency percentiles:

- **Median latency:** 110 ms → **100 ms** (−9.1%)
- **p95 latency:** 440 ms → **150 ms** (−65.9%)
- **p99 latency:** 810 ms → **240 ms** (−70.4%)
- **Average latency:** 310 ms → **111.73 ms** (−64.0%)

### **Test Setup**[​](#test-setup "Direct link to test-setup")

**Locust**

- **Concurrent users:** 1,000
- **Ramp-up:** 500

**System Specs**

- **Database was used**
- **CPU:** 4 vCPUs
- **Memory:** 8 GB RAM
- **LiteLLM Workers:** 4
- **Instances**: 4

**Configuration (config.yaml)**

View the complete configuration: [gist.github.com/AlexsanderHamir/config.yaml](https://gist.github.com/AlexsanderHamir/53f7d554a5d2afcf2c4edb5b6be68ff4)

**Load Script (no\_cache\_hits.py)**

View the complete load testing script: [gist.github.com/AlexsanderHamir/no\_cache\_hits.py](https://gist.github.com/AlexsanderHamir/42c33d7a4dc7a57f56a78b560dee3a42)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesOpenAI`gpt-5-pro`400K$15.00$120.00Responses API, reasoning, vision, function calling, prompt caching, web searchOpenAI`gpt-5-pro-2025-10-06`400K$15.00$120.00Responses API, reasoning, vision, function calling, prompt caching, web searchOpenAI`gpt-image-1-mini`-$2.00/img-Image generation and editingOpenAI`gpt-realtime-mini`128K$0.60$2.40Realtime audio, function callingAzure AI`azure_ai/Phi-4-mini-reasoning`131K$0.08$0.32Function callingAzure AI`azure_ai/Phi-4-reasoning`32K$0.125$0.50Function calling, reasoningAzure AI`azure_ai/MAI-DS-R1`128K$1.35$5.40Reasoning, function callingBedrock`au.anthropic.claude-sonnet-4-5-20250929-v1:0`200K$3.30$16.50Chat, reasoning, vision, function calling, prompt cachingBedrock`global.anthropic.claude-sonnet-4-5-20250929-v1:0`200K$3.00$15.00Chat, reasoning, vision, function calling, prompt cachingBedrock`global.anthropic.claude-sonnet-4-20250514-v1:0`1M$3.00$15.00Chat, reasoning, vision, function calling, prompt cachingBedrock`cohere.embed-v4:0`128K$0.12-Embeddings, image input supportOCI`oci/cohere.command-latest`128K$1.56$1.56Function callingOCI`oci/cohere.command-a-03-2025`256K$1.56$1.56Function callingOCI`oci/cohere.command-plus-latest`128K$1.56$1.56Function callingTogether AI`together_ai/moonshotai/Kimi-K2-Instruct-0905`262K$1.00$3.00Function callingTogether AI`together_ai/Qwen/Qwen3-Next-80B-A3B-Instruct`262K$0.15$1.50Function callingTogether AI`together_ai/Qwen/Qwen3-Next-80B-A3B-Thinking`262K$0.15$1.50Function callingVertex AIMedGemma modelsVariesVariesVariesMedical-focused Gemma models on custom endpointsWatson X27 new foundation modelsVariesVariesVariesGranite, Llama, Mistral families

#### Features[​](#features "Direct link to Features")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Add GPT-5 Pro model configuration and documentation - [PR #15258](https://github.com/BerriAI/litellm/pull/15258)
  - Add stop parameter to non-supported params for GPT-5 - [PR #15244](https://github.com/BerriAI/litellm/pull/15244)
  - Day 0 Support, Add gpt-image-1-mini - [PR #15259](https://github.com/BerriAI/litellm/pull/15259)
  - Add gpt-realtime-mini support - [PR #15283](https://github.com/BerriAI/litellm/pull/15283)
  - Add gpt-5-pro-2025-10-06 to model costs - [PR #15344](https://github.com/BerriAI/litellm/pull/15344)
  - Minimal fix: gpt5 models should not go on cooldown when called with temperature!=1 - [PR #15330](https://github.com/BerriAI/litellm/pull/15330)
- [**Snowflake Cortex**](https://docs.litellm.ai/docs/providers/snowflake)
  
  - Add function calling support for Snowflake Cortex REST API - [PR #15221](https://github.com/BerriAI/litellm/pull/15221)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix header forwarding for Gemini/Vertex AI providers in proxy mode - [PR #15231](https://github.com/BerriAI/litellm/pull/15231)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Removed stop param from unsupported azure models - [PR #15229](https://github.com/BerriAI/litellm/pull/15229)
  - Fix(azure/responses): remove invalid status param from azure call - [PR #15253](https://github.com/BerriAI/litellm/pull/15253)
  - Add new Azure AI models with pricing details - [PR #15387](https://github.com/BerriAI/litellm/pull/15387)
  - AzureAD Default credentials - select credential type based on environment - [PR #14470](https://github.com/BerriAI/litellm/pull/14470)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add Global Cross-Region Inference - [PR #15210](https://github.com/BerriAI/litellm/pull/15210)
  - Add Cohere Embed v4 support for AWS Bedrock - [PR #15298](https://github.com/BerriAI/litellm/pull/15298)
  - Fix(bedrock): include cacheWriteInputTokens in prompt\_tokens calculation - [PR #15292](https://github.com/BerriAI/litellm/pull/15292)
  - Add Bedrock AU Cross-Region Inference for Claude Sonnet 4.5 - [PR #15402](https://github.com/BerriAI/litellm/pull/15402)
  - Converse → /v1/messages streaming doesn't handle parallel tool calls with Claude models - [PR #15315](https://github.com/BerriAI/litellm/pull/15315)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Implement Context Caching for Vertex AI provider - [PR #15226](https://github.com/BerriAI/litellm/pull/15226)
  - Support for Vertex AI Gemma Models on Custom Endpoints - [PR #15397](https://github.com/BerriAI/litellm/pull/15397)
  - VertexAI - gemma model family support (custom endpoints) - [PR #15419](https://github.com/BerriAI/litellm/pull/15419)
  - VertexAI Gemma model family streaming support + Added MedGemma - [PR #15427](https://github.com/BerriAI/litellm/pull/15427)
- [**OCI**](https://docs.litellm.ai/docs/providers/oci)
  
  - Add OCI Cohere support with tool calling and streaming capabilities - [PR #15365](https://github.com/BerriAI/litellm/pull/15365)
- [**Watson X**](https://docs.litellm.ai/docs/providers/watsonx)
  
  - Add Watson X foundation model definitions to model\_prices\_and\_context\_window.json - [PR #15219](https://github.com/BerriAI/litellm/pull/15219)
  - Watsonx - Apply correct prompt templates for openai/gpt-oss model family - [PR #15341](https://github.com/BerriAI/litellm/pull/15341)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Fix - (openrouter): move cache\_control to content blocks for claude/gemini - [PR #15345](https://github.com/BerriAI/litellm/pull/15345)
  - Fix - OpenRouter cache\_control to only apply to last content block - [PR #15395](https://github.com/BerriAI/litellm/pull/15395)
- [**Together AI**](https://docs.litellm.ai/docs/providers/togetherai)
  
  - Add new together models - [PR #15383](https://github.com/BerriAI/litellm/pull/15383)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- **General**
  
  - Bug fix: gpt-5-chat-latest has incorrect max\_input\_tokens value - [PR #15116](https://github.com/BerriAI/litellm/pull/15116)
  - Fix reasoning response ID - [PR #15265](https://github.com/BerriAI/litellm/pull/15265)
  - Fix issue with parsing assistant messages - [PR #15320](https://github.com/BerriAI/litellm/pull/15320)
  - Fix litellm\_param based costing - [PR #15336](https://github.com/BerriAI/litellm/pull/15336)
  - Fix lint errors - [PR #15406](https://github.com/BerriAI/litellm/pull/15406)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Added streaming support for response api streaming image generation - [PR #15269](https://github.com/BerriAI/litellm/pull/15269)
  - Add native Responses API support for litellm\_proxy provider - [PR #15347](https://github.com/BerriAI/litellm/pull/15347)
  - Temporarily relax ResponsesAPIResponse parsing to support custom backends (e.g., vLLM) - [PR #15362](https://github.com/BerriAI/litellm/pull/15362)
- [**Files API**](https://docs.litellm.ai/docs/files_api)
  
  - Feat(files): add @client decorator to file operations - [PR #15339](https://github.com/BerriAI/litellm/pull/15339)
- [**/generateContent**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix gemini cli by actually streaming the response - [PR #15264](https://github.com/BerriAI/litellm/pull/15264)
- [**Azure Passthrough**](https://docs.litellm.ai/docs/pass_through/azure)
  
  - Azure - passthrough support with router models - [PR #15240](https://github.com/BerriAI/litellm/pull/15240)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Fix x-litellm-cache-key header not being returned on cache hit - [PR #15348](https://github.com/BerriAI/litellm/pull/15348)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Proxy CLI Auth**
  
  - Proxy CLI - dont store existing key in the URL, store it in the state param - [PR #15290](https://github.com/BerriAI/litellm/pull/15290)
- **Models + Endpoints**
  
  - Make PATCH `/model/{model_id}/update` handle `team_id` consistently with POST `/model/new` - [PR #15297](https://github.com/BerriAI/litellm/pull/15297)
  - Feature: adds Infinity as a provider in the UI - [PR #15285](https://github.com/BerriAI/litellm/pull/15285)
  - Fix: model + endpoints page crash when config file contains router\_settings.model\_group\_alias - [PR #15308](https://github.com/BerriAI/litellm/pull/15308)
  - Models & Endpoints Initial Refactor - [PR #15435](https://github.com/BerriAI/litellm/pull/15435)
  - Litellm UI API Reference page updates - [PR #15438](https://github.com/BerriAI/litellm/pull/15438)
- **Teams**
  
  - Teams page: new column "Your Role" on the teams table - [PR #15384](https://github.com/BerriAI/litellm/pull/15384)
  - LiteLLM Dashboard Teams UI refactor - [PR #15418](https://github.com/BerriAI/litellm/pull/15418)
- **UI Infrastructure**
  
  - Added prettier to autoformat frontend - [PR #15215](https://github.com/BerriAI/litellm/pull/15215)
  - Adds turbopack to the npm run dev command in UI to build faster during development - [PR #15250](https://github.com/BerriAI/litellm/pull/15250)
  - (perf) fix: Replaces bloated key list calls with lean key aliases endpoint - [PR #15252](https://github.com/BerriAI/litellm/pull/15252)
  - Potentially fixes a UI spasm issue with an expired cookie - [PR #15309](https://github.com/BerriAI/litellm/pull/15309)
  - LiteLLM UI Refactor Infrastructure - [PR #15236](https://github.com/BerriAI/litellm/pull/15236)
  - Enforces removal of unused imports from UI - [PR #15416](https://github.com/BerriAI/litellm/pull/15416)
  - Fix: usage page &gt;&gt; Model Activity &gt;&gt; spend per day graph: y-axis clipping on large spend values - [PR #15389](https://github.com/BerriAI/litellm/pull/15389)
  - Updates guardrail provider logos - [PR #15421](https://github.com/BerriAI/litellm/pull/15421)
- **Admin Settings**
  
  - Fix: Router settings do not update despite success message - [PR #15249](https://github.com/BerriAI/litellm/pull/15249)
  - Fix: Prevents DB from accidentally overriding config file values if they are empty in DB - [PR #15340](https://github.com/BerriAI/litellm/pull/15340)
- **SSO**
  
  - SSO - support EntraID app roles - [PR #15351](https://github.com/BerriAI/litellm/pull/15351)

* * *

## Logging / Guardrail / Prompt Management Integrations[​](#logging--guardrail--prompt-management-integrations "Direct link to Logging / Guardrail / Prompt Management Integrations")

#### Features[​](#features-3 "Direct link to Features")

- [**PostHog**](https://docs.litellm.ai/docs/observability/posthog)
  
  - Feat: posthog per request api key - [PR #15379](https://github.com/BerriAI/litellm/pull/15379)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**EnkryptAI**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Add EnkryptAI Guardrails on LiteLLM - [PR #15390](https://github.com/BerriAI/litellm/pull/15390)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Tag Management**
  
  - Tag Management - Add support for setting tag based budgets - [PR #15433](https://github.com/BerriAI/litellm/pull/15433)
- **Dynamic Rate Limiter v3**
  
  - QA/Fixes - Dynamic Rate Limiter v3 - final QA - [PR #15311](https://github.com/BerriAI/litellm/pull/15311)
  - Fix dynamic Rate limiter v3 - inserting litellm\_model\_saturation - [PR #15394](https://github.com/BerriAI/litellm/pull/15394)
- **Shared Health Check**
  
  - Implement Shared Health Check State Across Pods - [PR #15380](https://github.com/BerriAI/litellm/pull/15380)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **Tool Control**
  
  - MCP Gateway - UI - Select allowed tools for Key, Teams - [PR #15241](https://github.com/BerriAI/litellm/pull/15241)
  - MCP Gateway - Backend - Allow storing allowed tools by team/key - [PR #15243](https://github.com/BerriAI/litellm/pull/15243)
  - MCP Gateway - Fine-grained Database Object Storage Control - [PR #15255](https://github.com/BerriAI/litellm/pull/15255)
  - MCP Gateway - Litellm mcp fixes team control - [PR #15304](https://github.com/BerriAI/litellm/pull/15304)
  - MCP Gateway - QA/Fixes - Ensure Team/Key level enforcement works for MCPs - [PR #15305](https://github.com/BerriAI/litellm/pull/15305)
  - Feature: Include server\_name in /v1/mcp/server/health endpoint response - [PR #15431](https://github.com/BerriAI/litellm/pull/15431)
- **OpenAPI Integration**
  
  - MCP - support converting OpenAPI specs to MCP servers - [PR #15343](https://github.com/BerriAI/litellm/pull/15343)
  - MCP - specify allowed params per tool - [PR #15346](https://github.com/BerriAI/litellm/pull/15346)
- **Configuration**
  
  - MCP - support setting CA\_BUNDLE\_PATH - [PR #15253](https://github.com/BerriAI/litellm/pull/15253)
  - Fix: Ensure MCP client stays open during tool call - [PR #15391](https://github.com/BerriAI/litellm/pull/15391)
  - Remove hardcoded "public" schema in migration.sql - [PR #15363](https://github.com/BerriAI/litellm/pull/15363)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Router Optimizations**
  
  - Fix - Router: add model\_name index for O(1) deployment lookups - [PR #15113](https://github.com/BerriAI/litellm/pull/15113)
  - Refactor Utils: extract inner function from client - [PR #15234](https://github.com/BerriAI/litellm/pull/15234)
  - Fix Networking: remove limitations - [PR #15302](https://github.com/BerriAI/litellm/pull/15302)
- **Session Management**
  
  - Fix - Sessions not being shared - [PR #15388](https://github.com/BerriAI/litellm/pull/15388)
  - Fix: remove panic from hot path - [PR #15396](https://github.com/BerriAI/litellm/pull/15396)
  - Fix - shared session parsing and usage issue - [PR #15440](https://github.com/BerriAI/litellm/pull/15440)
  - Fix: handle closed aiohttp sessions - [PR #15442](https://github.com/BerriAI/litellm/pull/15442)
  - Fix: prevent session leaks when recreating aiohttp sessions - [PR #15443](https://github.com/BerriAI/litellm/pull/15443)
- **SSL/TLS Performance**
  
  - Perf: optimize SSL/TLS handshake performance with prioritized cipher - [PR #15398](https://github.com/BerriAI/litellm/pull/15398)
- **Dependencies**
  
  - Upgrades tenacity version to 8.5.0 - [PR #15303](https://github.com/BerriAI/litellm/pull/15303)
- **Data Masking**
  
  - Fix - SensitiveDataMasker converts lists to string - [PR #15420](https://github.com/BerriAI/litellm/pull/15420)

* * *

## General AI Gateway Improvements[​](#general-ai-gateway-improvements "Direct link to General AI Gateway Improvements")

#### Security[​](#security "Direct link to Security")

- **General**
  
  - Fix: redact AWS credentials when redact\_user\_api\_key\_info enabled - [PR #15321](https://github.com/BerriAI/litellm/pull/15321)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Update doc: perf update - [PR #15211](https://github.com/BerriAI/litellm/pull/15211)
  - Add W&B Inference documentation - [PR #15278](https://github.com/BerriAI/litellm/pull/15278)
- **Deployment**
  
  - Deletion of docker-compose buggy comment that cause `config.yaml` based startup fail - [PR #15425](https://github.com/BerriAI/litellm/pull/15425)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @Gal-bloch made their first contribution in [PR #15219](https://github.com/BerriAI/litellm/pull/15219)
- @lcfyi made their first contribution in [PR #15315](https://github.com/BerriAI/litellm/pull/15315)
- @ashengstd made their first contribution in [PR #15362](https://github.com/BerriAI/litellm/pull/15362)
- @vkolehmainen made their first contribution in [PR #15363](https://github.com/BerriAI/litellm/pull/15363)
- @jlan-nl made their first contribution in [PR #15330](https://github.com/BerriAI/litellm/pull/15330)
- @BCook98 made their first contribution in [PR #15402](https://github.com/BerriAI/litellm/pull/15402)
- @PabloGmz96 made their first contribution in [PR #15425](https://github.com/BerriAI/litellm/pull/15425)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.77.7.rc.1...v1.78.0.rc.1)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.77.7.rc.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Dynamic Rate Limiter v3** - Automatically maximizes throughput when capacity is available (&lt; 80% saturation) by allowing lower-priority requests to use unused capacity, then switches to fair priority-based allocation under high load (≥ 80%) to prevent blocking
- **Major Performance Improvements** - 2.9x lower median latency at 1,000 concurrent users.
- **Claude Sonnet 4.5** - Support for Anthropic's new Claude Sonnet 4.5 model family with 200K+ context and tiered pricing
- **MCP Gateway Enhancements** - Fine-grained tool control, server permissions, and forwardable headers
- **AMD Lemonade & Nvidia NIM** - New provider support for AMD Lemonade and Nvidia NIM Rerank
- **GitLab Prompt Management** - GitLab-based prompt management integration

### Performance - 2.9x Lower Median Latency[​](#performance---29x-lower-median-latency "Direct link to Performance - 2.9x Lower Median Latency")

This update removes LiteLLM router inefficiencies, reducing complexity from O(M×N) to O(1). Previously, it built a new array and ran repeated checks like data\["model"] in llm\_router.get\_model\_ids(). Now, a direct ID-to-deployment map eliminates redundant allocations and scans.

As a result, performance improved across all latency percentiles:

- **Median latency:** 320 ms → **110 ms** (−65.6%)
- **p95 latency:** 850 ms → **440 ms** (−48.2%)
- **p99 latency:** 1,400 ms → **810 ms** (−42.1%)
- **Average latency:** 864 ms → **310 ms** (−64%)

#### Test Setup[​](#test-setup "Direct link to Test Setup")

**Locust**

- **Concurrent users:** 1,000
- **Ramp-up:** 500

**System Specs**

- **CPU:** 4 vCPUs
- **Memory:** 8 GB RAM
- **LiteLLM Workers:** 4
- **Instances**: 4

**Configuration (config.yaml)**

View the complete configuration: [gist.github.com/AlexsanderHamir/config.yaml](https://gist.github.com/AlexsanderHamir/53f7d554a5d2afcf2c4edb5b6be68ff4)

**Load Script (no\_cache\_hits.py)**

View the complete load testing script: [gist.github.com/AlexsanderHamir/no\_cache\_hits.py](https://gist.github.com/AlexsanderHamir/42c33d7a4dc7a57f56a78b560dee3a42)

### MCP OAuth 2.0 Support[​](#mcp-oauth-20-support "Direct link to MCP OAuth 2.0 Support")

This release adds support for OAuth 2.0 Client Credentials for MCP servers. This is great for **Internal Dev Tools** use-cases, as it enables your users to call MCP servers, with their own credentials. E.g. Allowing your developers to call the Github MCP, with their own credentials.

[Set it up today on Claude Code](https://docs.litellm.ai/docs/tutorials/claude_responses_api#connecting-mcp-servers)

### Scheduled Key Rotations[​](#scheduled-key-rotations "Direct link to Scheduled Key Rotations")

This release brings support for scheduling virtual key rotations on LiteLLM AI Gateway.

From this release you can enforce Virtual Keys to rotate on a schedule of your choice e.g every 15 days/30 days/60 days etc.

This is great for Proxy Admins who need to enforce security policies for production workloads.

[Get Started](https://docs.litellm.ai/docs/proxy/virtual_keys#scheduled-key-rotations)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesAnthropic`claude-sonnet-4-5`200K$3.00$15.00Chat, reasoning, vision, function calling, prompt cachingAnthropic`claude-sonnet-4-5-20250929`200K$3.00$15.00Chat, reasoning, vision, function calling, prompt cachingBedrock`eu.anthropic.claude-sonnet-4-5-20250929-v1:0`200K$3.00$15.00Chat, reasoning, vision, function calling, prompt cachingAzure AI`azure_ai/grok-4`131K$5.50$27.50Chat, reasoning, function calling, web searchAzure AI`azure_ai/grok-4-fast-reasoning`131K$0.43$1.73Chat, reasoning, function calling, web searchAzure AI`azure_ai/grok-4-fast-non-reasoning`131K$0.43$1.73Chat, function calling, web searchAzure AI`azure_ai/grok-code-fast-1`131K$3.50$17.50Chat, function calling, web searchGroq`groq/moonshotai/kimi-k2-instruct-0905`Context variesPricing variesPricing variesChat, function callingOllamaOllama Cloud modelsVariesFreeFreeSelf-hosted models via Ollama Cloud

#### Features[​](#features "Direct link to Features")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Add new claude-sonnet-4-5 model family with tiered pricing above 200K tokens - [PR #15041](https://github.com/BerriAI/litellm/pull/15041)
  - Add anthropic/claude-sonnet-4-5 to model price json with prompt caching support - [PR #15049](https://github.com/BerriAI/litellm/pull/15049)
  - Add 200K prices for Sonnet 4.5 - [PR #15140](https://github.com/BerriAI/litellm/pull/15140)
  - Add cost tracking for /v1/messages in streaming response - [PR #15102](https://github.com/BerriAI/litellm/pull/15102)
  - Add /v1/messages/count\_tokens to Anthropic routes for non-admin user access - [PR #15034](https://github.com/BerriAI/litellm/pull/15034)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Ignore type param for gemini tools - [PR #15022](https://github.com/BerriAI/litellm/pull/15022)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add LiteLLM Overhead metric for VertexAI - [PR #15040](https://github.com/BerriAI/litellm/pull/15040)
  - Support googlemap grounding in vertex ai - [PR #15179](https://github.com/BerriAI/litellm/pull/15179)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Add azure\_ai grok-4 model family - [PR #15137](https://github.com/BerriAI/litellm/pull/15137)
  - Use the `extra_query` parameter for GET requests in Azure Batch - [PR #14997](https://github.com/BerriAI/litellm/pull/14997)
  - Use extra\_query for download results (Batch API) - [PR #15025](https://github.com/BerriAI/litellm/pull/15025)
  - Add support for Azure AD token-based authorization - [PR #14813](https://github.com/BerriAI/litellm/pull/14813)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Add ollama cloud models - [PR #15008](https://github.com/BerriAI/litellm/pull/15008)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Add groq/moonshotai/kimi-k2-instruct-0905 - [PR #15079](https://github.com/BerriAI/litellm/pull/15079)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Add support for GPT 5 codex models - [PR #14841](https://github.com/BerriAI/litellm/pull/14841)
- [**DeepInfra**](https://docs.litellm.ai/docs/providers/deepinfra)
  
  - Update DeepInfra model data refresh with latest pricing - [PR #14939](https://github.com/BerriAI/litellm/pull/14939)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add JP Cross-Region Inference - [PR #15188](https://github.com/BerriAI/litellm/pull/15188)
  - Add "eu.anthropic.claude-sonnet-4-5-20250929-v1:0" - [PR #15181](https://github.com/BerriAI/litellm/pull/15181)
  - Add twelvelabs bedrock Async Invoke Support - [PR #14871](https://github.com/BerriAI/litellm/pull/14871)
- [**Nvidia NIM**](https://docs.litellm.ai/docs/providers/nvidia_nim)
  
  - Add Nvidia NIM Rerank Support - [PR #15152](https://github.com/BerriAI/litellm/pull/15152)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Fix response\_format bug in hosted vllm audio\_transcription - [PR #15010](https://github.com/BerriAI/litellm/pull/15010)
  - Fix passthrough of atranscription into kwargs going to upstream provider - [PR #15005](https://github.com/BerriAI/litellm/pull/15005)
- [**OCI**](https://docs.litellm.ai/docs/providers/oci)
  
  - Fix OCI Generative AI Integration when using Proxy - [PR #15072](https://github.com/BerriAI/litellm/pull/15072)
- **General**
  
  - Fix: Authorization header to use correct "Bearer" capitalization - [PR #14764](https://github.com/BerriAI/litellm/pull/14764)
  - Bug fix: gpt-5-chat-latest has incorrect max\_input\_tokens value - [PR #15116](https://github.com/BerriAI/litellm/pull/15116)
  - Update request handling for original exceptions - [PR #15013](https://github.com/BerriAI/litellm/pull/15013)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**AMD Lemonade**](https://docs.litellm.ai/docs/providers/lemonade)
  
  - Add AMD Lemonade provider support - [PR #14840](https://github.com/BerriAI/litellm/pull/14840)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Return Cost for Responses API Streaming requests - [PR #15053](https://github.com/BerriAI/litellm/pull/15053)
- [**/generateContent**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Add full support for native Gemini API translation - [PR #15029](https://github.com/BerriAI/litellm/pull/15029)
- **Passthrough Gemini Routes**
  
  - Add Gemini generateContent passthrough cost tracking - [PR #15014](https://github.com/BerriAI/litellm/pull/15014)
  - Add streamGenerateContent cost tracking in passthrough - [PR #15199](https://github.com/BerriAI/litellm/pull/15199)
- **Passthrough Vertex AI Routes**
  
  - Add cost tracking for Vertex AI Passthrough `/predict` endpoint - [PR #15019](https://github.com/BerriAI/litellm/pull/15019)
  - Add cost tracking for Vertex AI Live API WebSocket Passthrough - [PR #14956](https://github.com/BerriAI/litellm/pull/14956)
- **General**
  
  - Preserve Whitespace Characters in Model Response Streams - [PR #15160](https://github.com/BerriAI/litellm/pull/15160)
  - Add provider name to payload specification - [PR #15130](https://github.com/BerriAI/litellm/pull/15130)
  - Ensure query params are forwarded from origin url to downstream request - [PR #15087](https://github.com/BerriAI/litellm/pull/15087)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Virtual Keys**
  
  - Ensure LLM\_API\_KEYs can access pass through routes - [PR #15115](https://github.com/BerriAI/litellm/pull/15115)
  - Support 'guaranteed\_throughput' when setting limits on keys belonging to a team - [PR #15120](https://github.com/BerriAI/litellm/pull/15120)
- **Models + Endpoints**
  
  - Ensure OCI secret fields not shared on /models and /v1/models endpoints - [PR #15085](https://github.com/BerriAI/litellm/pull/15085)
  - Add snowflake on UI - [PR #15083](https://github.com/BerriAI/litellm/pull/15083)
  - Make UI theme settings publicly accessible for custom branding - [PR #15074](https://github.com/BerriAI/litellm/pull/15074)
- **Admin Settings**
  
  - Ensure OTEL settings are saved in DB after set on UI - [PR #15118](https://github.com/BerriAI/litellm/pull/15118)
  - Top api key tags - [PR #15151](https://github.com/BerriAI/litellm/pull/15151), [PR #15156](https://github.com/BerriAI/litellm/pull/15156)
- **MCP**
  
  - show health status of MCP servers - [PR #15185](https://github.com/BerriAI/litellm/pull/15185)
  - allow setting extra headers on the UI - [PR #15185](https://github.com/BerriAI/litellm/pull/15185)
  - allow editing allowed tools on the UI - [PR #15185](https://github.com/BerriAI/litellm/pull/15185)

### Bug Fixes[​](#bug-fixes-1 "Direct link to Bug Fixes")

- **Virtual Keys**
  
  - (security) prevent user key from updating other user keys - [PR #15201](https://github.com/BerriAI/litellm/pull/15201)
  - (security) don't return all keys with blank key alias on /v2/key/info - [PR #15201](https://github.com/BerriAI/litellm/pull/15201)
  - Fix Session Token Cookie Infinite Logout Loop - [PR #15146](https://github.com/BerriAI/litellm/pull/15146)
- **Models + Endpoints**
  
  - Make UI theme settings publicly accessible for custom branding - [PR #15074](https://github.com/BerriAI/litellm/pull/15074)
- **Teams**
  
  - fix failed copy to clipboard for http ui - [PR #15195](https://github.com/BerriAI/litellm/pull/15195)
- **Logs**
  
  - fix logs page render logs on filter lookup - [PR #15195](https://github.com/BerriAI/litellm/pull/15195)
  - fix lookup list of end users (migrate to more efficient /customers/list lookup) - [PR #15195](https://github.com/BerriAI/litellm/pull/15195)
- **Test key**
  
  - update selected model on key change - [PR #15197](https://github.com/BerriAI/litellm/pull/15197)
- **Dashboard**
  
  - Fix LiteLLM model name fallback in dashboard overview - [PR #14998](https://github.com/BerriAI/litellm/pull/14998)

* * *

## Logging / Guardrail / Prompt Management Integrations[​](#logging--guardrail--prompt-management-integrations "Direct link to Logging / Guardrail / Prompt Management Integrations")

#### Features[​](#features-3 "Direct link to Features")

- [**OpenTelemetry**](https://docs.litellm.ai/docs/observability/otel)
  
  - Use generation\_name for span naming in logging method - [PR #14799](https://github.com/BerriAI/litellm/pull/14799)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Handle non-serializable objects in Langfuse logging - [PR #15148](https://github.com/BerriAI/litellm/pull/15148)
  - Set usage\_details.total in langfuse integration - [PR #15015](https://github.com/BerriAI/litellm/pull/15015)
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - support custom metadata labels on key/team - [PR #15094](https://github.com/BerriAI/litellm/pull/15094)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**Javelin**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Add Javelin standalone guardrails integration for LiteLLM Proxy - [PR #14983](https://github.com/BerriAI/litellm/pull/14983)
  - Add logging for important status fields in guardrails - [PR #15090](https://github.com/BerriAI/litellm/pull/15090)
  - Don't run post\_call guardrail if no text returned from Bedrock - [PR #15106](https://github.com/BerriAI/litellm/pull/15106)

#### Prompt Management[​](#prompt-management "Direct link to Prompt Management")

- [**GitLab**](https://docs.litellm.ai/docs/proxy/prompt_management)
  
  - GitLab based Prompt manager - [PR #14988](https://github.com/BerriAI/litellm/pull/14988)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Cost Tracking**
  
  - Proxy: end user cost tracking in the responses API - [PR #15124](https://github.com/BerriAI/litellm/pull/15124)
- **Parallel Request Limiter v3**
  
  - Use well known redis cluster hashing algorithm - [PR #15052](https://github.com/BerriAI/litellm/pull/15052)
  - Fixes to dynamic rate limiter v3 - add saturation detection - [PR #15119](https://github.com/BerriAI/litellm/pull/15119)
  - Dynamic Rate Limiter v3 - fixes for detecting saturation + fixes for post saturation behavior - [PR #15192](https://github.com/BerriAI/litellm/pull/15192)
- **Teams**
  
  - Add model specific tpm/rpm limits to teams on LiteLLM - [PR #15044](https://github.com/BerriAI/litellm/pull/15044)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **Server Configuration**
  
  - Specify forwardable headers, specify allowed/disallowed tools for MCP servers - [PR #15002](https://github.com/BerriAI/litellm/pull/15002)
  - Enforce server permissions on call tools - [PR #15044](https://github.com/BerriAI/litellm/pull/15044)
  - MCP Gateway Fine-grained Tools Addition - [PR #15153](https://github.com/BerriAI/litellm/pull/15153)
- **Bug Fixes**
  
  - Remove servername prefix mcp tools tests - [PR #14986](https://github.com/BerriAI/litellm/pull/14986)
  - Resolve regression with duplicate Mcp-Protocol-Version header - [PR #15050](https://github.com/BerriAI/litellm/pull/15050)
  - Fix test\_mcp\_server.py - [PR #15183](https://github.com/BerriAI/litellm/pull/15183)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Router Optimizations**
  
  - **+62.5% P99 Latency Improvement** - Remove router inefficiencies (from O(M\*N) to O(1)) - [PR #15046](https://github.com/BerriAI/litellm/pull/15046)
  - Remove hasattr checks in Router - [PR #15082](https://github.com/BerriAI/litellm/pull/15082)
  - Remove Double Lookups - [PR #15084](https://github.com/BerriAI/litellm/pull/15084)
  - Optimize \_filter\_cooldown\_deployments from O(n×m + k×n) to O(n) - [PR #15091](https://github.com/BerriAI/litellm/pull/15091)
  - Optimize unhealthy deployment filtering in retry path (O(n\*m) → O(n+m)) - [PR #15110](https://github.com/BerriAI/litellm/pull/15110)
- **Cache Optimizations**
  
  - Reduce complexity of InMemoryCache.evict\_cache from O(n\*log(n)) to O(log(n)) - [PR #15000](https://github.com/BerriAI/litellm/pull/15000)
  - Avoiding expensive operations when cache isn't available - [PR #15182](https://github.com/BerriAI/litellm/pull/15182)
- **Worker Management**
  
  - Add proxy CLI option to recycle workers after N requests - [PR #15007](https://github.com/BerriAI/litellm/pull/15007)
- **Metrics & Monitoring**
  
  - LiteLLM Overhead metric tracking - Add support for tracking litellm overhead on cache hits - [PR #15045](https://github.com/BerriAI/litellm/pull/15045)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation**
  
  - Update litellm docs from latest release - [PR #15004](https://github.com/BerriAI/litellm/pull/15004)
  - Add missing api\_key parameter - [PR #15058](https://github.com/BerriAI/litellm/pull/15058)
- **General Documentation**
  
  - Use docker compose instead of docker-compose - [PR #15024](https://github.com/BerriAI/litellm/pull/15024)
  - Add railtracks to projects that are using litellm - [PR #15144](https://github.com/BerriAI/litellm/pull/15144)
  - Perf: Last week improvement - [PR #15193](https://github.com/BerriAI/litellm/pull/15193)
  - Sync models GitHub documentation with Loom video and cross-reference - [PR #15191](https://github.com/BerriAI/litellm/pull/15191)

* * *

## Security Fixes[​](#security-fixes "Direct link to Security Fixes")

- **JWT Token Security** - Don't log JWT SSO token on .info() log - [PR #15145](https://github.com/BerriAI/litellm/pull/15145)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @herve-ves made their first contribution in [PR #14998](https://github.com/BerriAI/litellm/pull/14998)
- @wenxi-onyx made their first contribution in [PR #15008](https://github.com/BerriAI/litellm/pull/15008)
- @jpetrucciani made their first contribution in [PR #15005](https://github.com/BerriAI/litellm/pull/15005)
- @abhijitjavelin made their first contribution in [PR #14983](https://github.com/BerriAI/litellm/pull/14983)
- @ZeroClover made their first contribution in [PR #15039](https://github.com/BerriAI/litellm/pull/15039)
- @cedarm made their first contribution in [PR #15043](https://github.com/BerriAI/litellm/pull/15043)
- @Isydmr made their first contribution in [PR #15025](https://github.com/BerriAI/litellm/pull/15025)
- @serializer made their first contribution in [PR #15013](https://github.com/BerriAI/litellm/pull/15013)
- @eddierichter-amd made their first contribution in [PR #14840](https://github.com/BerriAI/litellm/pull/14840)
- @malags made their first contribution in [PR #15000](https://github.com/BerriAI/litellm/pull/15000)
- @henryhwang made their first contribution in [PR #15029](https://github.com/BerriAI/litellm/pull/15029)
- @plafleur made their first contribution in [PR #15111](https://github.com/BerriAI/litellm/pull/15111)
- @tyler-liner made their first contribution in [PR #14799](https://github.com/BerriAI/litellm/pull/14799)
- @Amir-R25 made their first contribution in [PR #15144](https://github.com/BerriAI/litellm/pull/15144)
- @georg-wolflein made their first contribution in [PR #15124](https://github.com/BerriAI/litellm/pull/15124)
- @niharm made their first contribution in [PR #15140](https://github.com/BerriAI/litellm/pull/15140)
- @anthony-liner made their first contribution in [PR #15015](https://github.com/BerriAI/litellm/pull/15015)
- @rishiganesh2002 made their first contribution in [PR #15153](https://github.com/BerriAI/litellm/pull/15153)
- @danielaskdd made their first contribution in [PR #15160](https://github.com/BerriAI/litellm/pull/15160)
- @JVenberg made their first contribution in [PR #15146](https://github.com/BerriAI/litellm/pull/15146)
- @speglich made their first contribution in [PR #15072](https://github.com/BerriAI/litellm/pull/15072)
- @daily-kim made their first contribution in [PR #14764](https://github.com/BerriAI/litellm/pull/14764)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.77.5.rc.4...v1.77.7.rc.1)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.77.5-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **MCP OAuth 2.0 Support** - Enhanced authentication for Model Context Protocol integrations
- **Scheduled Key Rotations** - Automated key rotation capabilities for enhanced security
- **New Gemini 2.5 Flash & Flash-lite Models** - Latest September 2025 preview models with improved pricing and features
- **Performance Improvements** - 54% RPS improvement

* * *

### Performance Improvements - 54% RPS Improvement[​](#performance-improvements---54-rps-improvement "Direct link to Performance Improvements - 54% RPS Improvement")

This release brings a 54% RPS improvement (1,040 → 1,602 RPS, aggregated) per instance.

The improvement comes from fixing O(n²) inefficiencies in the LiteLLM Router, primarily caused by repeated use of `in` statements inside loops over large arrays.

Tests were run with a database-only setup (no cache hits).

#### Test Setup[​](#test-setup "Direct link to Test Setup")

All benchmarks were executed using Locust with 1,000 concurrent users and a ramp-up of 500. The environment was configured to stress the routing layer and eliminate caching as a variable.

**System Specs**

- **CPU:** 8 vCPUs
- **Memory:** 32 GB RAM

**Configuration (config.yaml)**

View the complete configuration: [gist.github.com/AlexsanderHamir/config.yaml](https://gist.github.com/AlexsanderHamir/53f7d554a5d2afcf2c4edb5b6be68ff4)

**Load Script (no\_cache\_hits.py)**

View the complete load testing script: [gist.github.com/AlexsanderHamir/no\_cache\_hits.py](https://gist.github.com/AlexsanderHamir/42c33d7a4dc7a57f56a78b560dee3a42)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesGemini`gemini-2.5-flash-preview-09-2025`1M$0.30$2.50Chat, reasoning, vision, audioGemini`gemini-2.5-flash-lite-preview-09-2025`1M$0.10$0.40Chat, reasoning, vision, audioGemini`gemini-flash-latest`1M$0.30$2.50Chat, reasoning, vision, audioGemini`gemini-flash-lite-latest`1M$0.10$0.40Chat, reasoning, vision, audioDeepSeek`deepseek-chat`131K$0.60$1.70Chat, function calling, cachingDeepSeek`deepseek-reasoner`131K$0.60$1.70Chat, reasoningBedrock`deepseek.v3-v1:0`164K$0.58$1.68Chat, reasoning, function callingAzure`azure/gpt-5-codex`272K$1.25$10.00Responses API, reasoning, visionOpenAI`gpt-5-codex`272K$1.25$10.00Responses API, reasoning, visionSambaNova`sambanova/DeepSeek-V3.1`33K$3.00$4.50Chat, reasoning, function callingSambaNova`sambanova/gpt-oss-120b`131K$3.00$4.50Chat, reasoning, function callingBedrock`qwen.qwen3-coder-480b-a35b-v1:0`262K$0.22$1.80Chat, reasoning, function callingBedrock`qwen.qwen3-235b-a22b-2507-v1:0`262K$0.22$0.88Chat, reasoning, function callingBedrock`qwen.qwen3-coder-30b-a3b-v1:0`262K$0.15$0.60Chat, reasoning, function callingBedrock`qwen.qwen3-32b-v1:0`131K$0.15$0.60Chat, reasoning, function callingVertex AI`vertex_ai/qwen/qwen3-next-80b-a3b-instruct-maas`262K$0.15$1.20Chat, function callingVertex AI`vertex_ai/qwen/qwen3-next-80b-a3b-thinking-maas`262K$0.15$1.20Chat, function callingVertex AI`vertex_ai/deepseek-ai/deepseek-v3.1-maas`164K$1.35$5.40Chat, reasoning, function callingOpenRouter`openrouter/x-ai/grok-4-fast:free`2M$0.00$0.00Chat, reasoning, function callingXAI`xai/grok-4-fast-reasoning`2M$0.20$0.50Chat, reasoning, function callingXAI`xai/grok-4-fast-non-reasoning`2M$0.20$0.50Chat, function calling

#### Features[​](#features "Direct link to Features")

- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Added Gemini 2.5 Flash and Flash-lite preview models (September 2025 release) with improved pricing - [PR #14948](https://github.com/BerriAI/litellm/pull/14948)
  - Added new Anthropic web fetch tool support - [PR #14951](https://github.com/BerriAI/litellm/pull/14951)
- [**XAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - Add xai/grok-4-fast models - [PR #14833](https://github.com/BerriAI/litellm/pull/14833)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Updated Claude Sonnet 4 configs to reflect million-token context window pricing - [PR #14639](https://github.com/BerriAI/litellm/pull/14639)
  - Added supported text field to anthropic citation response - [PR #14164](https://github.com/BerriAI/litellm/pull/14164)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Added support for Qwen models family & Deepseek 3.1 to Amazon Bedrock - [PR #14845](https://github.com/BerriAI/litellm/pull/14845)
  - Support requestMetadata in Bedrock Converse API - [PR #14570](https://github.com/BerriAI/litellm/pull/14570)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Added vertex\_ai/qwen models and azure/gpt-5-codex - [PR #14844](https://github.com/BerriAI/litellm/pull/14844)
  - Update vertex ai qwen model pricing - [PR #14828](https://github.com/BerriAI/litellm/pull/14828)
  - Vertex AI Context Caching: use Vertex ai API v1 instead of v1beta1 and accept 'cachedContent' param - [PR #14831](https://github.com/BerriAI/litellm/pull/14831)
- [**SambaNova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Add sambanova deepseek v3.1 and gpt-oss-120b - [PR #14866](https://github.com/BerriAI/litellm/pull/14866)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Fix inconsistent token configs for gpt-5 models - [PR #14942](https://github.com/BerriAI/litellm/pull/14942)
  - GPT-3.5-Turbo price updated - [PR #14858](https://github.com/BerriAI/litellm/pull/14858)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Add gpt-5 and gpt-5-codex to OpenRouter cost map - [PR #14879](https://github.com/BerriAI/litellm/pull/14879)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Fix vllm passthrough - [PR #14778](https://github.com/BerriAI/litellm/pull/14778)
- [**Flux**](https://docs.litellm.ai/docs/image_generation)
  
  - Support flux image edit - [PR #14790](https://github.com/BerriAI/litellm/pull/14790)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Fix: Support claude code auth via subscription (anthropic) - [PR #14821](https://github.com/BerriAI/litellm/pull/14821)
  - Fix Anthropic streaming IDs - [PR #14965](https://github.com/BerriAI/litellm/pull/14965)
  - Revert incorrect changes to sonnet-4 max output tokens - [PR #14933](https://github.com/BerriAI/litellm/pull/14933)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Fix a bug where openai image edit silently ignores multiple images - [PR #14893](https://github.com/BerriAI/litellm/pull/14893)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Fix: vLLM provider's rerank endpoint from /v1/rerank to /rerank - [PR #14938](https://github.com/BerriAI/litellm/pull/14938)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**W&B Inference**](https://docs.litellm.ai/docs/providers/wandb)
  
  - Add W&B Inference to LiteLLM - [PR #14416](https://github.com/BerriAI/litellm/pull/14416)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- **General**
  
  - Add SDK support for additional headers - [PR #14761](https://github.com/BerriAI/litellm/pull/14761)
  - Add shared\_session parameter for aiohttp ClientSession reuse - [PR #14721](https://github.com/BerriAI/litellm/pull/14721)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Fix: Streaming tool call index assignment for multiple tool calls - [PR #14587](https://github.com/BerriAI/litellm/pull/14587)
  - Fix load credentials in token counter proxy - [PR #14808](https://github.com/BerriAI/litellm/pull/14808)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Proxy CLI Auth**
  
  - Allow re-using cli auth token - [PR #14780](https://github.com/BerriAI/litellm/pull/14780)
  - Create a python method to login using litellm proxy - [PR #14782](https://github.com/BerriAI/litellm/pull/14782)
  - Fixes for LiteLLM Proxy CLI to Auth to Gateway - [PR #14836](https://github.com/BerriAI/litellm/pull/14836)

**Virtual Keys**

- Initial support for scheduled key rotations - [PR #14877](https://github.com/BerriAI/litellm/pull/14877)
- Allow scheduling key rotations when creating virtual keys - [PR #14960](https://github.com/BerriAI/litellm/pull/14960)

**Models + Endpoints**

- Fix: added Oracle to provider's list - [PR #14835](https://github.com/BerriAI/litellm/pull/14835)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **SSO** - Fix: SSO "Clear" button writes empty values instead of removing SSO config - [PR #14826](https://github.com/BerriAI/litellm/pull/14826)
- **Admin Settings** - Remove useful links from admin settings - [PR #14918](https://github.com/BerriAI/litellm/pull/14918)
- **Management Routes** - Add /user/list to management routes - [PR #14868](https://github.com/BerriAI/litellm/pull/14868)

* * *

## Logging / Guardrail / Prompt Management Integrations[​](#logging--guardrail--prompt-management-integrations "Direct link to Logging / Guardrail / Prompt Management Integrations")

#### Features[​](#features-3 "Direct link to Features")

- [**DataDog**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Logging - `datadog` callback Log message content w/o sending to datadog - [PR #14909](https://github.com/BerriAI/litellm/pull/14909)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Adding langfuse usage details for cached tokens - [PR #10955](https://github.com/BerriAI/litellm/pull/10955)
- [**Opik**](https://docs.litellm.ai/docs/proxy/logging#opik)
  
  - Improve opik integration code - [PR #14888](https://github.com/BerriAI/litellm/pull/14888)
- [**SQS**](https://docs.litellm.ai/docs/proxy/logging#sqs)
  
  - Error logging support for SQS Logger - [PR #14974](https://github.com/BerriAI/litellm/pull/14974)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- **LakeraAI v2 Guardrail** - Ensure exception is raised correctly - [PR #14867](https://github.com/BerriAI/litellm/pull/14867)
- **Presidio Guardrail** - Support custom entity types in Presidio guardrail with Union\[PiiEntityType, str] - [PR #14899](https://github.com/BerriAI/litellm/pull/14899)
- **Noma Guardrail** - Add noma guardrail provider to ui - [PR #14415](https://github.com/BerriAI/litellm/pull/14415)

#### Prompt Management[​](#prompt-management "Direct link to Prompt Management")

- **BitBucket Integration** - Add BitBucket Integration for Prompt Management - [PR #14882](https://github.com/BerriAI/litellm/pull/14882)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Service Tier Pricing** - Add service\_tier based pricing support for openai (BOTH Service & Priority Support) - [PR #14796](https://github.com/BerriAI/litellm/pull/14796)
- **Cost Tracking** - Show input, output, tool call cost breakdown in StandardLoggingPayload - [PR #14921](https://github.com/BerriAI/litellm/pull/14921)
- **Parallel Request Limiter v3**
  
  - Ensure Lua scripts can execute on redis cluster - [PR #14968](https://github.com/BerriAI/litellm/pull/14968)
  - Fix: get metadata info from both metadata and litellm\_metadata fields - [PR #14783](https://github.com/BerriAI/litellm/pull/14783)
- **Priority Reservation** - Fix: Priority Reservation: keys without priority metadata receive higher priority than keys with explicit priority configurations - [PR #14832](https://github.com/BerriAI/litellm/pull/14832)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **MCP Configuration** - Enable custom fields in mcp\_info configuration - [PR #14794](https://github.com/BerriAI/litellm/pull/14794)
- **MCP Tools** - Remove server\_name prefix from list\_tools - [PR #14720](https://github.com/BerriAI/litellm/pull/14720)
- **OAuth Flow** - Initial commit for v2 oauth flow - [PR #14964](https://github.com/BerriAI/litellm/pull/14964)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Memory Leak Fix** - Fix InMemoryCache unbounded growth when TTLs are set - [PR #14869](https://github.com/BerriAI/litellm/pull/14869)
- **Cache Performance** - Fix: cache root cause - [PR #14827](https://github.com/BerriAI/litellm/pull/14827)
- **Concurrency Fix** - Fix concurrency/scaling when many Python threads do streaming using *sync* completions - [PR #14816](https://github.com/BerriAI/litellm/pull/14816)
- **Performance Optimization** - Fix: reduce get\_deployment cost to O(1) - [PR #14967](https://github.com/BerriAI/litellm/pull/14967)
- **Performance Optimization** - Fix: remove slow string operation - [PR #14955](https://github.com/BerriAI/litellm/pull/14955)
- **DB Connection Management** - Fix: DB connection state retries - [PR #14925](https://github.com/BerriAI/litellm/pull/14925)

* * *

## Documentation Updates[​](#documentation-updates "Direct link to Documentation Updates")

- **Provider Documentation** - Fix docs for provider\_specific\_params.md - [PR #14787](https://github.com/BerriAI/litellm/pull/14787)
- **Model References** - Update model references from gemini-pro to gemini-2.5-pro - [PR #14775](https://github.com/BerriAI/litellm/pull/14775)
- **Letta Guide** - Add Letta Guide documentation - [PR #14798](https://github.com/BerriAI/litellm/pull/14798)
- **README** - Make the README document clearer - [PR #14860](https://github.com/BerriAI/litellm/pull/14860)
- **Session Management** - Update docs for session management availability - [PR #14914](https://github.com/BerriAI/litellm/pull/14914)
- **Cost Documentation** - Add documentation for additional cost-related keys in custom pricing - [PR #14949](https://github.com/BerriAI/litellm/pull/14949)
- **Azure Passthrough** - Add azure passthrough documentation - [PR #14958](https://github.com/BerriAI/litellm/pull/14958)
- **General Documentation** - Doc updates sept 2025 - [PR #14769](https://github.com/BerriAI/litellm/pull/14769)
  
  - Clarified bridging between endpoints and mode in docs.
  - Added Vertex AI Gemini API configuration as an alternative in relevant guides. Linked AWS authentication info in the Bedrock guardrails documentation.
  - Added Cancel Response API usage with code snippets
  - Clarified that SSO (Single Sign-On) is free for up to 5 users:
  - Alphabetized sidebar, leaving quick start / intros at top of categories
  - Documented max\_connections under cache\_params.
  - Clarified IAM AssumeRole Policy requirements.
  - Added transform utilities example to Getting Started (showing request transformation).
  - Added references to models.litellm.ai as the full models list in various docs.
  - Added a code snippet for async\_post\_call\_success\_hook.
  - Removed broken links to callbacks management guide. - Reformatted and linked cookbooks + other relevant docs
- **Documentation Corrections** - Corrected docs updates sept 2025 - [PR #14916](https://github.com/BerriAI/litellm/pull/14916)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @uzaxirr made their first contribution in [PR #14761](https://github.com/BerriAI/litellm/pull/14761)
- @xprilion made their first contribution in [PR #14416](https://github.com/BerriAI/litellm/pull/14416)
- @CH-GAGANRAJ made their first contribution in [PR #14779](https://github.com/BerriAI/litellm/pull/14779)
- @otaviofbrito made their first contribution in [PR #14778](https://github.com/BerriAI/litellm/pull/14778)
- @danielmklein made their first contribution in [PR #14639](https://github.com/BerriAI/litellm/pull/14639)
- @Jetemple made their first contribution in [PR #14826](https://github.com/BerriAI/litellm/pull/14826)
- @akshoop made their first contribution in [PR #14818](https://github.com/BerriAI/litellm/pull/14818)
- @hazyone made their first contribution in [PR #14821](https://github.com/BerriAI/litellm/pull/14821)
- @leventov made their first contribution in [PR #14816](https://github.com/BerriAI/litellm/pull/14816)
- @fabriciojoc made their first contribution in [PR #10955](https://github.com/BerriAI/litellm/pull/10955)
- @onlylonly made their first contribution in [PR #14845](https://github.com/BerriAI/litellm/pull/14845)
- @Copilot made their first contribution in [PR #14869](https://github.com/BerriAI/litellm/pull/14869)
- @arsh72 made their first contribution in [PR #14899](https://github.com/BerriAI/litellm/pull/14899)
- @berri-teddy made their first contribution in [PR #14914](https://github.com/BerriAI/litellm/pull/14914)
- @vpbill made their first contribution in [PR #14415](https://github.com/BerriAI/litellm/pull/14415)
- @kgritesh made their first contribution in [PR #14893](https://github.com/BerriAI/litellm/pull/14893)
- @oytunkutrup1 made their first contribution in [PR #14858](https://github.com/BerriAI/litellm/pull/14858)
- @nherment made their first contribution in [PR #14933](https://github.com/BerriAI/litellm/pull/14933)
- @deepanshululla made their first contribution in [PR #14974](https://github.com/BerriAI/litellm/pull/14974)
- @TeddyAmkie made their first contribution in [PR #14758](https://github.com/BerriAI/litellm/pull/14758)
- @SmartManoj made their first contribution in [PR #14775](https://github.com/BerriAI/litellm/pull/14775)
- @uc4w6c made their first contribution in [PR #14720](https://github.com/BerriAI/litellm/pull/14720)
- @luizrennocosta made their first contribution in [PR #14783](https://github.com/BerriAI/litellm/pull/14783)
- @AlexsanderHamir made their first contribution in [PR #14827](https://github.com/BerriAI/litellm/pull/14827)
- @dharamendrak made their first contribution in [PR #14721](https://github.com/BerriAI/litellm/pull/14721)
- @TomeHirata made their first contribution in [PR #14164](https://github.com/BerriAI/litellm/pull/14164)
- @mrFranklin made their first contribution in [PR #14860](https://github.com/BerriAI/litellm/pull/14860)
- @luisfucros made their first contribution in [PR #14866](https://github.com/BerriAI/litellm/pull/14866)
- @huangyafei made their first contribution in [PR #14879](https://github.com/BerriAI/litellm/pull/14879)
- @thiswillbeyourgithub made their first contribution in [PR #14949](https://github.com/BerriAI/litellm/pull/14949)
- @Maximgitman made their first contribution in [PR #14965](https://github.com/BerriAI/litellm/pull/14965)
- @subnet-dev made their first contribution in [PR #14938](https://github.com/BerriAI/litellm/pull/14938)
- @22mSqRi made their first contribution in [PR #14972](https://github.com/BerriAI/litellm/pull/14972)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.77.3.rc.1...v1.77.5.rc.1)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.77.3-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **+550 RPS Performance Improvements** - Optimizations in request handling and object initialization.
- **Priority Quota Reservation** - Proxy admins can now reserve TPM/RPM capacity for specific keys.

## Priority Quota Reservation[​](#priority-quota-reservation "Direct link to Priority Quota Reservation")

This release adds support for priority quota reservation. This allows Proxy Admins to reserve specific percentages of model capacity for different use cases.

This is great for use cases where you want to ensure your realtime use cases must always get priority responses and background development jobs can take longer.

This release adds support for priority quota reservation. This allows **Proxy Admins** to reserve TPM/RPM capacity for keys based on metadata priority levels, ensuring critical production workloads get guaranteed access regardless of development traffic volume.

Get started [here](https://docs.litellm.ai/docs/proxy/dynamic_rate_limit#priority-quota-reservation)

## +550 RPS Performance Improvements[​](#550-rps-performance-improvements "Direct link to +550 RPS Performance Improvements")

This release delivers significant RPS improvements through targeted optimizations.

We've achieved a +500 RPS boost by fixing cache type inconsistencies that were causing frequent cache misses, plus an additional +50 RPS by removing unnecessary coroutine checks from the hot path.

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesSambaNova`sambanova/deepseek-v3.1`128K$0.90$0.90Chat completionsSambaNova`sambanova/gpt-oss-120b`128K$0.72$0.72Chat completionsOVHCloudVarious modelsVariesContact providerContact providerChat completionsCompactifAIVarious modelsVariesContact providerContact providerChat completionsTwelveLabs`twelvelabs/marengo-embed-2.7`32K$0.12$0.00Embeddings

#### Features[​](#features "Direct link to Features")

- [**OVHCloud AI Endpoints**](https://docs.litellm.ai/docs/providers/ovhcloud)
  
  - New provider support with comprehensive model catalog - [PR #14494](https://github.com/BerriAI/litellm/pull/14494)
- [**CompactifAI**](https://docs.litellm.ai/docs/providers/compactifai)
  
  - New provider integration - [PR #14532](https://github.com/BerriAI/litellm/pull/14532)
- [**SambaNova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Added DeepSeek v3.1 and GPT-OSS-120B models - [PR #14500](https://github.com/BerriAI/litellm/pull/14500)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Cross-region inference profile cost calculation - [PR #14566](https://github.com/BerriAI/litellm/pull/14566)
  - AWS external ID parameter support for authentication - [PR #14582](https://github.com/BerriAI/litellm/pull/14582)
  - CountTokens API implementation - [PR #14557](https://github.com/BerriAI/litellm/pull/14557)
  - Titan V2 encoding\_format parameter support - [PR #14687](https://github.com/BerriAI/litellm/pull/14687)
  - Nova Canvas image generation inference profiles - [PR #14578](https://github.com/BerriAI/litellm/pull/14578)
  - Bedrock Batches API - batch processing support with file upload and request transformation - [PR #14618](https://github.com/BerriAI/litellm/pull/14618)
  - Bedrock Twelve Labs embedding provider support - [PR #14697](https://github.com/BerriAI/litellm/pull/14697)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Gemini labels field provider-aware filtering - [PR #14563](https://github.com/BerriAI/litellm/pull/14563)
  - Gemini Batch API support - [PR #14733](https://github.com/BerriAI/litellm/pull/14733)
- [**Volcengine**](https://docs.litellm.ai/docs/providers/volcengine)
  
  - Fixed thinking parameters when disabled - [PR #14569](https://github.com/BerriAI/litellm/pull/14569)
- [**Cohere**](https://docs.litellm.ai/docs/providers/cohere)
  
  - Handle Generate API deprecation, default to chat endpoints - [PR #14676](https://github.com/BerriAI/litellm/pull/14676)
- [**TwelveLabs**](https://docs.litellm.ai/docs/providers/twelvelabs)
  
  - Added Marengo Embed 2.7 embedding support - [PR #14674](https://github.com/BerriAI/litellm/pull/14674)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Empty arguments handling in tool call invocation - [PR #14583](https://github.com/BerriAI/litellm/pull/14583)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Avoid deepcopy crash with non-pickleables in Gemini/Vertex - [PR #14418](https://github.com/BerriAI/litellm/pull/14418)
- [**XAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - Fix unsupported stop parameter for grok-code models - [PR #14565](https://github.com/BerriAI/litellm/pull/14565)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Updated error message for Gemini API - [PR #14589](https://github.com/BerriAI/litellm/pull/14589)
  - Fixed 2.5 Flash Image Preview model routing - [PR #14715](https://github.com/BerriAI/litellm/pull/14715)
  - API key passing for token counting endpoints - [PR #14744](https://github.com/BerriAI/litellm/pull/14744)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**OVHCloud AI Endpoints**](https://docs.litellm.ai/docs/providers/ovhcloud)
  
  - Complete provider integration with model catalog and authentication - [PR #14494](https://github.com/BerriAI/litellm/pull/14494)
- [**CompactifAI**](https://docs.litellm.ai/docs/providers/compactifai)
  
  - New provider support with documentation - [PR #14532](https://github.com/BerriAI/litellm/pull/14532)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/responses**](https://docs.litellm.ai/docs/response_api)
  
  - Added cancel endpoint support for non-admin users - [PR #14594](https://github.com/BerriAI/litellm/pull/14594)
  - Improved response session handling and cold storage configuration with s3 - [PR #14534](https://github.com/BerriAI/litellm/pull/14534)
  - Added OpenAI & Azure /responses/cancel endpoint support - [PR #14561](https://github.com/BerriAI/litellm/pull/14561)
- **General**
  
  - Enhanced rate limit error messages with details - [PR #14736](https://github.com/BerriAI/litellm/pull/14736)
  - Middle-truncation for spend log payloads - [PR #14637](https://github.com/BerriAI/litellm/pull/14637)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**/chat/completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Fixed completion chat ID handling - [PR #14548](https://github.com/BerriAI/litellm/pull/14548)
  - Prevent AttributeError for \_get\_tags\_from\_request\_kwargs - [PR #14735](https://github.com/BerriAI/litellm/pull/14735)
- [**/responses**](https://docs.litellm.ai/docs/response_api)
  
  - Fixed cost calculation - [PR #14675](https://github.com/BerriAI/litellm/pull/14675)
- **General**
  
  - Rate limiter AttributeError fix - [PR #14609](https://github.com/BerriAI/litellm/pull/14609)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Responses API Cost Calculation** fix - [PR #14675](https://github.com/BerriAI/litellm/pull/14675)
- **Anthropic Cache Token Pricing** - Separate 1-hour vs 5-minute cache creation costs - [PR #14620](https://github.com/BerriAI/litellm/pull/14620), [PR #14652](https://github.com/BerriAI/litellm/pull/14652)
- **Indochina Time Timezone** support for budget resets - [PR #14666](https://github.com/BerriAI/litellm/pull/14666)
- **Soft Budget Alert Cache Issues** - Resolved soft budget alert cache issues - [PR #14491](https://github.com/BerriAI/litellm/pull/14491)
- **Dynamic Rate Limiter v3** - Priority routing improvements - [PR #14734](https://github.com/BerriAI/litellm/pull/14734)
- **Enhanced Rate Limit Errors** - More detailed error messages - [PR #14736](https://github.com/BerriAI/litellm/pull/14736)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Team Member Service Account Keys** - Allow team members to view keys they create - [PR #14619](https://github.com/BerriAI/litellm/pull/14619)
- **Default Budget for JWT Teams** - Auto-assign budgets to generated teams - [PR #14514](https://github.com/BerriAI/litellm/pull/14514)
- **SSO Access Control Groups** - Enhanced token info endpoint integration - [PR #14738](https://github.com/BerriAI/litellm/pull/14738)
- **Health Test Connect Protection** - Restrict access based on model creation permissions - [PR #14650](https://github.com/BerriAI/litellm/pull/14650)
- **Amazon Bedrock Guardrail Info View** - Enhanced logging visualization - [PR #14696](https://github.com/BerriAI/litellm/pull/14696)

#### Bug Fixes[​](#bug-fixes-1 "Direct link to Bug Fixes")

- **SCIM v2** - Fix group PUSH and PUT operations for non-existent members - [PR #14581](https://github.com/BerriAI/litellm/pull/14581)
- **Guardrail View/Edit/Delete** behavior fixes - [PR #14622](https://github.com/BerriAI/litellm/pull/14622)
- **In-Memory Guardrail** update failures - [PR #14653](https://github.com/BerriAI/litellm/pull/14653)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-3 "Direct link to Features")

- [**DataDog**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Enhanced spend tracking metrics - [PR #14555](https://github.com/BerriAI/litellm/pull/14555)
  - Stream support with is\_streamed\_request parameter - [PR #14673](https://github.com/BerriAI/litellm/pull/14673)
  - Fixed tool calls metadata passing - [PR #14531](https://github.com/BerriAI/litellm/pull/14531)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Added logging support for Responses API - [PR #14597](https://github.com/BerriAI/litellm/pull/14597)
- [**Langsmith**](https://docs.litellm.ai/docs/proxy/logging#langsmith)
  
  - Langsmith Sampling Rate - Key/Team-level tracing configuration - [PR #14740](https://github.com/BerriAI/litellm/pull/14740)
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/logging#prometheus)
  
  - Multi-worker support improvements - [PR #14530](https://github.com/BerriAI/litellm/pull/14530)
  - User email labels in monitoring - [PR #14520](https://github.com/BerriAI/litellm/pull/14520)
- [**Opik**](https://docs.litellm.ai/docs/proxy/logging#opik)
  
  - Fixed timezone issue - [PR #14708](https://github.com/BerriAI/litellm/pull/14708)

### Bug Fixes[​](#bug-fixes-2 "Direct link to Bug Fixes")

- [**S3**](https://docs.litellm.ai/docs/proxy/logging#s3-buckets)
  
  - Fixed 404 error when using s3\_endpoint\_url - [PR #14559](https://github.com/BerriAI/litellm/pull/14559)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- **Tool Permission Guardrail** - Fine-grained tool access control - [PR #14519](https://github.com/BerriAI/litellm/pull/14519)
- **Bedrock Guardrails** - Selective guarding support with runtime endpoint configuration - [PR #14575](https://github.com/BerriAI/litellm/pull/14575), [PR #14650](https://github.com/BerriAI/litellm/pull/14650)
- **Default Last Message** in guardrails - [PR #14640](https://github.com/BerriAI/litellm/pull/14640)
- **AWS exceptions handling despite 200 response** - [PR #14658](https://github.com/BerriAI/litellm/pull/14658)

#### New Integration[​](#new-integration "Direct link to New Integration")

- [**PostHog**](https://docs.litellm.ai/docs/observability/posthog) - Complete observability integration for LiteLLM usage tracking and analytics - [PR #14610](https://github.com/BerriAI/litellm/pull/14610)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **MCP Server Alias Parsing** - Multi-part URL path support - [PR #14558](https://github.com/BerriAI/litellm/pull/14558)
- **MCP Filter Recomputation** - After server deletion - [PR #14542](https://github.com/BerriAI/litellm/pull/14542)
- **MCP Gateway Tools List** improvements - [PR #14695](https://github.com/BerriAI/litellm/pull/14695)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **+500 RPS Performance Boost** when sending the `user` field - [PR #14616](https://github.com/BerriAI/litellm/pull/14616)
- **+50 RPS** by removing iscoroutine from hot path - [PR #14649](https://github.com/BerriAI/litellm/pull/14649)
- **7% reduction** in **init** overhead - [PR #14689](https://github.com/BerriAI/litellm/pull/14689)
- **Generic Object Pool** implementation for better resource management - [PR #14702](https://github.com/BerriAI/litellm/pull/14702)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Middle-Truncation** for spend log payloads - [PR #14637](https://github.com/BerriAI/litellm/pull/14637)

#### Security[​](#security "Direct link to Security")

- **Security Update** - Bump aiohttp==3.12.14, fix CVE-2025-53643 - [PR #14638](https://github.com/BerriAI/litellm/pull/14638)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @luisfucros made their first contribution in [PR #14500](https://github.com/BerriAI/litellm/pull/14500)
- @hanakannzashi made their first contribution in [PR #14548](https://github.com/BerriAI/litellm/pull/14548)
- @eliasto made their first contribution in [PR #14494](https://github.com/BerriAI/litellm/pull/14494)
- @Rasmusafj made their first contribution in [PR #14491](https://github.com/BerriAI/litellm/pull/14491)
- @LingXuanYin made their first contribution in [PR #14569](https://github.com/BerriAI/litellm/pull/14569)
- @ronaldpereira made their first contribution in [PR #14613](https://github.com/BerriAI/litellm/pull/14613)
- @hula-la made their first contribution in [PR #14534](https://github.com/BerriAI/litellm/pull/14534)
- @carlos-marchal-ph made their first contribution in [PR #14610](https://github.com/BerriAI/litellm/pull/14610)
- @akraines made their first contribution in [PR #14637](https://github.com/BerriAI/litellm/pull/14637)
- @mrFranklin made their first contribution in [PR #14708](https://github.com/BerriAI/litellm/pull/14708)
- @tcx4c70 made their first contribution in [PR #14675](https://github.com/BerriAI/litellm/pull/14675)
- @michaeltansg made their first contribution in [PR #14666](https://github.com/BerriAI/litellm/pull/14666)
- @tosi29 made their first contribution in [PR #14725](https://github.com/BerriAI/litellm/pull/14725)
- @gmdfalk made their first contribution in [PR #14735](https://github.com/BerriAI/litellm/pull/14735)
- @FelipeRodriguesGare made their first contribution in [PR #14733](https://github.com/BerriAI/litellm/pull/14733)
- @mritunjaysharma394 made their first contribution in [PR #14678](https://github.com/BerriAI/litellm/pull/14678)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.77.2.rc.1...v1.77.3.rc.1)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:main-v1.77.2-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Bedrock Batches API** - Support for creating Batch Inference Jobs on Bedrock using LiteLLM's unified batch API (OpenAI compatible)
- **Qwen API Tiered Pricing** - Cost tracking support for Dashscope (Qwen) models with multiple pricing tiers

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowPricing ($/1M tokens)FeaturesDeepInfra`deepinfra/deepseek-ai/DeepSeek-R1`164K**Input:** $0.70  
**Output:** $2.40Chat completions, tool callingHeroku`heroku/claude-4-sonnet`8KContact provider for pricingFunction calling, tool choiceHeroku`heroku/claude-3-7-sonnet`8KContact provider for pricingFunction calling, tool choiceHeroku`heroku/claude-3-5-sonnet-latest`8KContact provider for pricingFunction calling, tool choiceHeroku`heroku/claude-3-5-haiku`4KContact provider for pricingFunction calling, tool choiceDashscope`dashscope/qwen-plus-latest`1M**Tiered Pricing:**  
• 0-256K tokens: $0.40 / $1.20  
• 256K-1M tokens: $1.20 / $3.60Function calling, reasoningDashscope`dashscope/qwen3-max-preview`262K**Tiered Pricing:**  
• 0-32K tokens: $1.20 / $6.00  
• 32K-128K tokens: $2.40 / $12.00  
• 128K-252K tokens: $3.00 / $15.00Function calling, reasoningDashscope`dashscope/qwen-flash`1M**Tiered Pricing:**  
• 0-256K tokens: $0.05 / $0.40  
• 256K-1M tokens: $0.25 / $2.00Function calling, reasoningDashscope`dashscope/qwen3-coder-plus`1M**Tiered Pricing:**  
• 0-32K tokens: $1.00 / $5.00  
• 32K-128K tokens: $1.80 / $9.00  
• 128K-256K tokens: $3.00 / $15.00  
• 256K-1M tokens: $6.00 / $60.00Function calling, reasoning, cachingDashscope`dashscope/qwen3-coder-flash`1M**Tiered Pricing:**  
• 0-32K tokens: $0.30 / $1.50  
• 32K-128K tokens: $0.50 / $2.50  
• 128K-256K tokens: $0.80 / $4.00  
• 256K-1M tokens: $1.60 / $9.60Function calling, reasoning, caching

* * *

#### Features[​](#features "Direct link to Features")

- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock_batches)
  
  - Bedrock Batches API - batch processing support with file upload and request transformation - [PR #14518](https://github.com/BerriAI/litellm/pull/14518), [PR #14522](https://github.com/BerriAI/litellm/pull/14522)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Added transcription endpoint support - [PR #14523](https://github.com/BerriAI/litellm/pull/14523)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - `ollama_chat/` - images, thinking, and content as list handling - [PR #14523](https://github.com/BerriAI/litellm/pull/14523)
- **General**
  
  - New debug flag for detailed request/response logging [PR #14482](https://github.com/BerriAI/litellm/pull/14482)

#### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure)
  
  - Fixed extra\_body injection causing payload rejection in image generation - [PR #14475](https://github.com/BerriAI/litellm/pull/14475)
- [**LM Studio**](https://docs.litellm.ai/docs/providers/lm-studio)
  
  - Resolved illegal Bearer header value issue - [PR #14512](https://github.com/BerriAI/litellm/pull/14512)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Bug Fixes[​](#bug-fixes-1 "Direct link to Bug Fixes")

- [**/messages**](https://docs.litellm.ai/docs/anthropic_unified)
  
  - Don't send content block after message w/ finish reason + usage block - [PR #14477](https://github.com/BerriAI/litellm/pull/14477)
- [**/generateContent**](https://docs.litellm.ai/docs/generateContent)
  
  - Gemini CLI Integration - Fixed token count errors - [PR #14451](https://github.com/BerriAI/litellm/pull/14451), [PR #14417](https://github.com/BerriAI/litellm/pull/14417)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

#### Features[​](#features-1 "Direct link to Features")

- [**Qwen API Tiered Pricing**](https://docs.litellm.ai/docs/providers/dashscope) - Added comprehensive tiered cost tracking for Dashscope/Qwen models - [PR #14471](https://github.com/BerriAI/litellm/pull/14471), [PR #14479](https://github.com/BerriAI/litellm/pull/14479)

#### Bug Fixes[​](#bug-fixes-2 "Direct link to Bug Fixes")

- **Provider Budgets** - Fixed provider budget calculations - [PR #14459](https://github.com/BerriAI/litellm/pull/14459)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **User Headers Mapping** - New X-LiteLLM Users mapping feature for enhanced user tracking - [PR #14485](https://github.com/BerriAI/litellm/pull/14485)
- **Key Unblocking** - Support for hashed tokens in `/key/unblock` endpoint - [PR #14477](https://github.com/BerriAI/litellm/pull/14477)
- **Model Group Header Forwarding** - Enhanced wildcard model support with documentation - [PR #14528](https://github.com/BerriAI/litellm/pull/14528)

#### Bug Fixes[​](#bug-fixes-3 "Direct link to Bug Fixes")

- **Log Tab Key Alias** - Fixed filtering inaccuracies for failed logs - [PR #14469](https://github.com/BerriAI/litellm/pull/14469), [PR #14529](https://github.com/BerriAI/litellm/pull/14529)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-3 "Direct link to Features")

- **Noma Integration** - Added non-blocking monitor mode with anonymize input support - [PR #14401](https://github.com/BerriAI/litellm/pull/14401)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Performance[​](#performance "Direct link to Performance")

- Removed dynamic creation of static values - [PR #14538](https://github.com/BerriAI/litellm/pull/14538)
- Using `_PROXY_MaxParallelRequestsHandler_v3` by default for optimal throughput - [PR #14450](https://github.com/BerriAI/litellm/pull/14450)
- Improved execution context propagation into logging tasks - [PR #14455](https://github.com/BerriAI/litellm/pull/14455)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @Sameerlite made their first contribution in [PR #14460](https://github.com/BerriAI/litellm/pull/14460)
- @holzman made their first contribution in [PR #14459](https://github.com/BerriAI/litellm/pull/14459)
- @sashank5644 made their first contribution in [PR #14469](https://github.com/BerriAI/litellm/pull/14469)
- @TomAlon made their first contribution in [PR #14401](https://github.com/BerriAI/litellm/pull/14401)
- @AlexsanderHamir made their first contribution in [PR #14538](https://github.com/BerriAI/litellm/pull/14538)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.77.1.dev.2...v1.77.2.dev)[​](#full-changelog "Direct link to full-changelog")

warning

This release has a known issue where startup is leading to Out of Memory errors when deploying on Kubernetes. We recommend waiting before upgrading to this version.

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.76.3
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Major Performance Improvements** +400 RPS when using correct amount of workers + CPU cores combination
- **Video Generation Support** - Added Google AI Studio and Vertex AI Veo Video Generation through LiteLLM Pass through routes
- **CloudZero Integration** - New cost tracking integration for exporting LiteLLM Usage and Spend data to CloudZero.

## Major Changes[​](#major-changes "Direct link to Major Changes")

- **Performance Optimization**: LiteLLM Proxy now achieves +400 RPS when using correct amount of CPU cores - [PR #14153](https://github.com/BerriAI/litellm/pull/14153), [PR #14242](https://github.com/BerriAI/litellm/pull/14242)
  
  By default, LiteLLM will now use `num_workers = os.cpu_count()` to achieve optimal performance.
  
  **Override Options:**
  
  Set environment variable:
  
  ```
  DEFAULT_NUM_WORKERS_LITELLM_PROXY=1
  ```
  
  Or start LiteLLM Proxy with:
- **Security Fix**: Fixed memory\_usage\_in\_mem\_cache cache endpoint vulnerability - [PR #14229](https://github.com/BerriAI/litellm/pull/14229)

* * *

## Performance Improvements[​](#performance-improvements "Direct link to Performance Improvements")

This release includes significant performance optimizations. On our internal benchmarks we saw 1 instance get +400 RPS when using correct amount of workers + CPU cores combination.

- **+400 RPS Performance Boost** - LiteLLM Proxy now uses correct amount of CPU cores for optimal performance - [PR #14153](https://github.com/BerriAI/litellm/pull/14153)
- **Default CPU Workers** - Changed DEFAULT\_NUM\_WORKERS\_LITELLM\_PROXY default to number of CPUs - [PR #14242](https://github.com/BerriAI/litellm/pull/14242)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesOpenRouter`openrouter/openai/gpt-4.1`1M$2.00$8.00Chat completions with visionOpenRouter`openrouter/openai/gpt-4.1-mini`1M$0.40$1.60Efficient chat completionsOpenRouter`openrouter/openai/gpt-4.1-nano`1M$0.10$0.40Ultra-efficient chatVertex AI`vertex_ai/openai/gpt-oss-20b-maas`131K$0.075$0.30Reasoning supportVertex AI`vertex_ai/openai/gpt-oss-120b-maas`131K$0.15$0.60Advanced reasoningGemini`gemini/veo-3.0-generate-preview`1K-$0.75/secVideo generationGemini`gemini/veo-3.0-fast-generate-preview`1K-$0.40/secFast video generationGemini`gemini/veo-2.0-generate-001`1K-$0.35/secVideo generationVolcengine`doubao-embedding-large`4KFreeFree2048-dim embeddingsTogether AI`together_ai/deepseek-ai/DeepSeek-V3.1`128K$0.60$1.70Reasoning support

#### Features[​](#features "Direct link to Features")

- [**Google Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Added 'thoughtSignature' support via 'thinking\_blocks' - [PR #14122](https://github.com/BerriAI/litellm/pull/14122)
  - Added support for reasoning\_effort='minimal' for Gemini models - [PR #14262](https://github.com/BerriAI/litellm/pull/14262)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Added GPT-4.1 model family - [PR #14101](https://github.com/BerriAI/litellm/pull/14101)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Added support for reasoning\_effort parameter - [PR #14207](https://github.com/BerriAI/litellm/pull/14207)
- [**X.AI**](https://docs.litellm.ai/docs/providers/xai)
  
  - Fixed XAI cost calculation - [PR #14127](https://github.com/BerriAI/litellm/pull/14127)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Added support for GPT-OSS models on Vertex AI - [PR #14184](https://github.com/BerriAI/litellm/pull/14184)
  - Added additionalProperties to Vertex AI Schema definition - [PR #14252](https://github.com/BerriAI/litellm/pull/14252)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Handle output parsing responses API output - [PR #14121](https://github.com/BerriAI/litellm/pull/14121)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Added unified 'thinking' param support via `reasoning_content` - [PR #14121](https://github.com/BerriAI/litellm/pull/14121)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Added supported text field to anthropic citation response - [PR #14126](https://github.com/BerriAI/litellm/pull/14126)
- [**OCI Provider**](https://docs.litellm.ai/docs/providers/oci)
  
  - Handle assistant messages with both content and tool\_calls - [PR #14171](https://github.com/BerriAI/litellm/pull/14171)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fixed structure output - [PR #14130](https://github.com/BerriAI/litellm/pull/14130)
  - Added initial support for Bedrock Batches API - [PR #14190](https://github.com/BerriAI/litellm/pull/14190)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks)
  
  - Added support for anthropic citation API in Databricks - [PR #14077](https://github.com/BerriAI/litellm/pull/14077)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Google Gemini (Google AI Studio + Vertex AI)**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fixed Gemini 2.5 Pro schema validation with OpenAI-style type arrays in tools - [PR #14154](https://github.com/BerriAI/litellm/pull/14154)
  - Fixed Gemini Tool Calling empty enum property - [PR #14155](https://github.com/BerriAI/litellm/pull/14155)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**Volcengine**](https://docs.litellm.ai/docs/providers/volcengine)
  
  - Added Volcengine embedding module with handler and transformation logic - [PR #14028](https://github.com/BerriAI/litellm/pull/14028)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Images API**](https://docs.litellm.ai/docs/image_generation)
  
  - Added pass through image generation and image editing on OpenAI - [PR #14292](https://github.com/BerriAI/litellm/pull/14292)
  - Support extra\_body parameter for image generation - [PR #14211](https://github.com/BerriAI/litellm/pull/14211)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Fixed response API for reasoning item in input for litellm proxy - [PR #14200](https://github.com/BerriAI/litellm/pull/14200)
  - Added structured output for SDK - [PR #14206](https://github.com/BerriAI/litellm/pull/14206)
- [**Bedrock Passthrough**](https://docs.litellm.ai/docs/pass_through/bedrock)
  
  - Support AWS\_BEDROCK\_RUNTIME\_ENDPOINT on bedrock passthrough - [PR #14156](https://github.com/BerriAI/litellm/pull/14156)
- [**Google AI Studio Passthrough**](https://docs.litellm.ai/docs/pass_through/google_ai_studio)
  
  - Allow using Veo Video Generation through LiteLLM Pass through routes - [PR #14228](https://github.com/BerriAI/litellm/pull/14228)
- **General**
  
  - Added support for safety\_identifier parameter in chat.completions.create - [PR #14174](https://github.com/BerriAI/litellm/pull/14174)
  - Fixed misclassified 500 error on invalid image\_url in /chat/completions request - [PR #14149](https://github.com/BerriAI/litellm/pull/14149)
  - Fixed token count error for Gemini CLI - [PR #14133](https://github.com/BerriAI/litellm/pull/14133)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Remove "/" or ":" from model name when being used as h11 header name - [PR #14191](https://github.com/BerriAI/litellm/pull/14191)
  - Bug fix for openai.gpt-oss when using reasoning\_effort parameter - [PR #14300](https://github.com/BerriAI/litellm/pull/14300)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

### Features[​](#features-2 "Direct link to Features")

- Added header support for spend\_logs\_metadata - [PR #14186](https://github.com/BerriAI/litellm/pull/14186)
- Litellm passthrough cost tracking for chat completion - [PR #14256](https://github.com/BerriAI/litellm/pull/14256)

### Bug Fixes[​](#bug-fixes-1 "Direct link to Bug Fixes")

- Fixed TPM Rate Limit Bug - [PR #14237](https://github.com/BerriAI/litellm/pull/14237)
- Fixed Key Budget not resets at expectable times - [PR #14241](https://github.com/BerriAI/litellm/pull/14241)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **UI Improvements**
  
  - Logs page screen size fixed - [PR #14135](https://github.com/BerriAI/litellm/pull/14135)
  - Create Organization Tooltip added on Success - [PR #14132](https://github.com/BerriAI/litellm/pull/14132)
  - Back to Keys should say Back to Logs - [PR #14134](https://github.com/BerriAI/litellm/pull/14134)
  - Add client side pagination on All Models table - [PR #14136](https://github.com/BerriAI/litellm/pull/14136)
  - Model Filters UI improvement - [PR #14131](https://github.com/BerriAI/litellm/pull/14131)
  - Remove table filter on user info page - [PR #14169](https://github.com/BerriAI/litellm/pull/14169)
  - Team name badge added on the User Details - [PR #14003](https://github.com/BerriAI/litellm/pull/14003)
  - Fix: Log page parameter passing error - [PR #14193](https://github.com/BerriAI/litellm/pull/14193)
- **Authentication & Authorization**
  
  - Support for ES256/ES384/ES512 and EdDSA JWT verification - [PR #14118](https://github.com/BerriAI/litellm/pull/14118)
  - Ensure `team_id` is a required field for generating service account keys - [PR #14270](https://github.com/BerriAI/litellm/pull/14270)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **General**
  
  - Validate store model in db setting - [PR #14269](https://github.com/BerriAI/litellm/pull/14269)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Datadog**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Ensure `apm_id` is set on DD LLM Observability traces - [PR #14272](https://github.com/BerriAI/litellm/pull/14272)
- [**Braintrust**](https://docs.litellm.ai/docs/proxy/logging#braintrust)
  
  - Fix logging when OTEL is enabled - [PR #14122](https://github.com/BerriAI/litellm/pull/14122)
- [**OTEL**](https://docs.litellm.ai/docs/proxy/logging#otel)
  
  - Optional Metrics and Logs following semantic conventions - [PR #14179](https://github.com/BerriAI/litellm/pull/14179)
- [**Slack Alerting**](https://docs.litellm.ai/docs/proxy/alerting)
  
  - Added alert type to alert message to slack for easier handling - [PR #14176](https://github.com/BerriAI/litellm/pull/14176)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- Added guardrail to the Anthropic API endpoint - [PR #14107](https://github.com/BerriAI/litellm/pull/14107)

#### New Integration[​](#new-integration "Direct link to New Integration")

- [**CloudZero**](https://docs.litellm.ai/docs/proxy/cost_tracking)
  
  - LiteLLM x CloudZero Integration for Cost Tracking - [PR #14296](https://github.com/BerriAI/litellm/pull/14296)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-5 "Direct link to Features")

- **Performance**
  
  - LiteLLM Proxy: +400 RPS when using correct amount of CPU cores - [PR #14153](https://github.com/BerriAI/litellm/pull/14153)
  - Allow using `x-litellm-stream-timeout` header for stream timeout in requests - [PR #14147](https://github.com/BerriAI/litellm/pull/14147)
  - Change DEFAULT\_NUM\_WORKERS\_LITELLM\_PROXY default to number CPUs - [PR #14242](https://github.com/BerriAI/litellm/pull/14242)
- **Monitoring**
  
  - Added Prometheus missing metrics - [PR #14139](https://github.com/BerriAI/litellm/pull/14139)
- **Timeout**
  
  - **Stream Timeout Control** - Allow using `x-litellm-stream-timeout` header for stream timeout in requests - [PR #14147](https://github.com/BerriAI/litellm/pull/14147)
- **Routing**
  
  - Fixed x-litellm-tags not routing with Responses API - [PR #14289](https://github.com/BerriAI/litellm/pull/14289)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **Security**
  
  - Fixed memory\_usage\_in\_mem\_cache cache endpoint vulnerability - [PR #14229](https://github.com/BerriAI/litellm/pull/14229)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-6 "Direct link to Features")

- **SCIM Support**
  
  - Added better SCIM debugging - [PR #14221](https://github.com/BerriAI/litellm/pull/14221)
  - Bug fixes for handling SCIM Group Memberships - [PR #14226](https://github.com/BerriAI/litellm/pull/14226)
- **Kubernetes**
  
  - Added optional PodDisruptionBudget for litellm proxy - [PR #14093](https://github.com/BerriAI/litellm/pull/14093)
- **Error Handling**
  
  - Add model to azure error message - [PR #14294](https://github.com/BerriAI/litellm/pull/14294)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @iabhi4 made their first contribution in [PR #14093](https://github.com/BerriAI/litellm/pull/14093)
- @zainhas made their first contribution in [PR #14087](https://github.com/BerriAI/litellm/pull/14087)
- @LifeDJIK made their first contribution in [PR #14146](https://github.com/BerriAI/litellm/pull/14146)
- @retanoj made their first contribution in [PR #14133](https://github.com/BerriAI/litellm/pull/14133)
- @zhxlp made their first contribution in [PR #14193](https://github.com/BerriAI/litellm/pull/14193)
- @kayoch1n made their first contribution in [PR #14191](https://github.com/BerriAI/litellm/pull/14191)
- @kutsushitaneko made their first contribution in [PR #14171](https://github.com/BerriAI/litellm/pull/14171)
- @mjmendo made their first contribution in [PR #14176](https://github.com/BerriAI/litellm/pull/14176)
- @HarshavardhanK made their first contribution in [PR #14213](https://github.com/BerriAI/litellm/pull/14213)
- @eycjur made their first contribution in [PR #14207](https://github.com/BerriAI/litellm/pull/14207)
- @22mSqRi made their first contribution in [PR #14241](https://github.com/BerriAI/litellm/pull/14241)
- @onlylhf made their first contribution in [PR #14028](https://github.com/BerriAI/litellm/pull/14028)
- @btpemercier made their first contribution in [PR #11319](https://github.com/BerriAI/litellm/pull/11319)
- @tremlin made their first contribution in [PR #14287](https://github.com/BerriAI/litellm/pull/14287)
- @TobiMayr made their first contribution in [PR #14262](https://github.com/BerriAI/litellm/pull/14262)
- @Eitan1112 made their first contribution in [PR #14252](https://github.com/BerriAI/litellm/pull/14252)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.76.1-nightly...v1.76.3-nightly)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.76.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Major Performance Improvements** - 6.5x faster LiteLLM Python SDK completion with fastuuid integration.
- **New Model Support** - Gemini 2.5 Flash Image Preview, Grok Code Fast, and GPT Realtime models
- **Enhanced Provider Support** - DeepSeek-v3.1 pricing on Fireworks AI, Vercel AI Gateway, and improved Anthropic/GitHub Copilot integration
- **MCP Improvements** - Better connection testing and SSE MCP tools bug fixes

## Major Changes[​](#major-changes "Direct link to Major Changes")

- Added support for using Gemini 2.5 Flash Image Preview with /chat/completions. **🚨 Warning** If you were using `gemini-2.0-flash-exp-image-generation` please follow this migration guide. [Gemini Image Generation Migration Guide](https://docs.litellm.ai/docs/extras/gemini_img_migration)

* * *

## Performance Improvements[​](#performance-improvements "Direct link to Performance Improvements")

This release includes significant performance optimizations:

- **6.5x faster LiteLLM Python SDK Completion** - Major performance boost for completion operations - [PR #13990](https://github.com/BerriAI/litellm/pull/13990)
- **fastuuid Integration** - 2.1x faster UUID generation with +80 RPS improvement for /chat/completions and other LLM endpoints - [PR #13992](https://github.com/BerriAI/litellm/pull/13992), [PR #14016](https://github.com/BerriAI/litellm/pull/14016)
- **Optimized Request Logging** - Don't print request params by default for +50 RPS improvement - [PR #14015](https://github.com/BerriAI/litellm/pull/14015)
- **Cache Performance** - 21% speedup in InMemoryCache.evict\_cache and 45% speedup in `_is_debugging_on` function - [PR #14012](https://github.com/BerriAI/litellm/pull/14012), [PR #13988](https://github.com/BerriAI/litellm/pull/13988)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesGoogle`gemini-2.5-flash-image-preview`1M$0.30$2.50Chat completions + image generation ($0.039/image)X.AI`xai/grok-code-fast`256K$0.20$1.50Code generationOpenAI`gpt-realtime`32K$4.00$16.00Real-time conversation + audioVercel AI Gateway`vercel_ai_gateway/openai/o3`200K$2.00$8.00Advanced reasoningVercel AI Gateway`vercel_ai_gateway/openai/o3-mini`200K$1.10$4.40Efficient reasoningVercel AI Gateway`vercel_ai_gateway/openai/o4-mini`200K$1.10$4.40Latest mini modelDeepInfra`deepinfra/zai-org/GLM-4.5`131K$0.55$2.00Chat completionsPerplexity`perplexity/codellama-34b-instruct`16K$0.35$1.40Code generationFireworks AI`fireworks_ai/accounts/fireworks/models/deepseek-v3p1`128K$0.56$1.68Chat completions

**Additional Models Added:** Various other Vercel AI Gateway models were added too. See [models.litellm.ai](https://models.litellm.ai) for the full list.

#### Features[​](#features "Direct link to Features")

- [**Google Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Added support for `gemini-2.5-flash-image-preview` with image return capability - [PR #13979](https://github.com/BerriAI/litellm/pull/13979), [PR #13983](https://github.com/BerriAI/litellm/pull/13983)
  - Support for requests with only system prompt - [PR #14010](https://github.com/BerriAI/litellm/pull/14010)
  - Fixed invalid model name error for Gemini Imagen models - [PR #13991](https://github.com/BerriAI/litellm/pull/13991)
- [**X.AI**](https://docs.litellm.ai/docs/providers/xai)
  
  - Added `xai/grok-code-fast` model family support - [PR #14054](https://github.com/BerriAI/litellm/pull/14054)
  - Fixed frequency\_penalty parameter for grok-4 models - [PR #14078](https://github.com/BerriAI/litellm/pull/14078)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Added support for gpt-realtime models - [PR #14082](https://github.com/BerriAI/litellm/pull/14082)
  - Support for reasoning and reasoning\_effort parameters by default - [PR #12865](https://github.com/BerriAI/litellm/pull/12865)
- [**Fireworks AI**](https://docs.litellm.ai/docs/providers/fireworks_ai)
  
  - Added DeepSeek-v3.1 pricing - [PR #13958](https://github.com/BerriAI/litellm/pull/13958)
- [**DeepInfra**](https://docs.litellm.ai/docs/providers/deepinfra)
  
  - Fixed reasoning\_effort setting for DeepSeek-V3.1 - [PR #14053](https://github.com/BerriAI/litellm/pull/14053)
- [**GitHub Copilot**](https://docs.litellm.ai/docs/providers/github_copilot)
  
  - Added support for thinking and reasoning\_effort parameters - [PR #13691](https://github.com/BerriAI/litellm/pull/13691)
  - Added image headers support - [PR #13955](https://github.com/BerriAI/litellm/pull/13955)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Support for custom Anthropic-compatible API endpoints - [PR #13945](https://github.com/BerriAI/litellm/pull/13945)
  - Fixed /messages fallback from Anthropic API to Bedrock API - [PR #13946](https://github.com/BerriAI/litellm/pull/13946)
- [**Nebius**](https://docs.litellm.ai/docs/providers/nebius)
  
  - Expanded provider models and normalized model IDs - [PR #13965](https://github.com/BerriAI/litellm/pull/13965)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Fixed Vertex Mistral streaming issues - [PR #13952](https://github.com/BerriAI/litellm/pull/13952)
  - Fixed anyOf corner cases for Gemini tool calls - [PR #12797](https://github.com/BerriAI/litellm/pull/12797)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fixed structure output issues - [PR #14005](https://github.com/BerriAI/litellm/pull/14005)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Added GPT-5 family models pricing - [PR #13536](https://github.com/BerriAI/litellm/pull/13536)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**Vercel AI Gateway**](https://docs.litellm.ai/docs/providers/vercel_ai_gateway)
  
  - New provider support added - [PR #13144](https://github.com/BerriAI/litellm/pull/13144)
- [**DataRobot**](https://docs.litellm.ai/docs/providers/datarobot)
  
  - Added provider documentation - [PR #14038](https://github.com/BerriAI/litellm/pull/14038), [PR #14074](https://github.com/BerriAI/litellm/pull/14074)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Images API**](https://docs.litellm.ai/docs/image_generation)
  
  - Support for multiple images in OpenAI images/edits endpoint - [PR #13916](https://github.com/BerriAI/litellm/pull/13916)
  - Allow using dynamic `api_key` for image generation requests - [PR #14007](https://github.com/BerriAI/litellm/pull/14007)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Fixed `/responses` endpoint ignoring extra\_headers in GitHub Copilot - [PR #13775](https://github.com/BerriAI/litellm/pull/13775)
  - Added support for new web\_search tool - [PR #14083](https://github.com/BerriAI/litellm/pull/14083)
- [**Azure Passthrough**](https://docs.litellm.ai/docs/providers/azure/azure)
  
  - Fixed Azure Passthrough request with streaming - [PR #13831](https://github.com/BerriAI/litellm/pull/13831)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Fixed handling of None metadata in batch requests - [PR #13996](https://github.com/BerriAI/litellm/pull/13996)
  - Fixed token\_counter with special token input - [PR #13374](https://github.com/BerriAI/litellm/pull/13374)
  - Removed incorrect web search support for azure/gpt-4.1 family - [PR #13566](https://github.com/BerriAI/litellm/pull/13566)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-2 "Direct link to Features")

- **SSE MCP Tools**
  
  - Bug fix for adding SSE MCP tools - improved connection testing when adding MCPs - [PR #14048](https://github.com/BerriAI/litellm/pull/14048)

[Read More](https://docs.litellm.ai/docs/mcp)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Team Management**
  
  - Allow setting Team Member RPM/TPM limits when creating a team - [PR #13943](https://github.com/BerriAI/litellm/pull/13943)
- **UI Improvements**
  
  - Fixed Next.js Security Vulnerabilities in UI Dashboard - [PR #14084](https://github.com/BerriAI/litellm/pull/14084)
  - Fixed collapsible navbar design - [PR #14075](https://github.com/BerriAI/litellm/pull/14075)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **Authentication**
  
  - Fixed Virtual keys with llm\_api type causing Internal Server Error for /anthropic/* and other LLM passthrough routes - [PR #14046](https://github.com/BerriAI/litellm/pull/14046)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Langfuse OTEL**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Allow using LANGFUSE\_OTEL\_HOST for configuring host - [PR #14013](https://github.com/BerriAI/litellm/pull/14013)
- [**Braintrust**](https://docs.litellm.ai/docs/proxy/logging#braintrust)
  
  - Added span name metadata feature - [PR #13573](https://github.com/BerriAI/litellm/pull/13573)
  - Fixed tests to reference moved attributes in `braintrust_logging` module - [PR #13978](https://github.com/BerriAI/litellm/pull/13978)
- [**OpenMeter**](https://docs.litellm.ai/docs/proxy/logging#openmeter)
  
  - Set user from token user\_id for OpenMeter integration - [PR #13152](https://github.com/BerriAI/litellm/pull/13152)

#### New Guardrail Support[​](#new-guardrail-support "Direct link to New Guardrail Support")

- [**Noma Security**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Added Noma Security guardrail support - [PR #13572](https://github.com/BerriAI/litellm/pull/13572)
- [**Pangea**](https://docs.litellm.ai/docs/proxy/guardrails)
  
  - Updated Pangea Guardrail to support new AIDR endpoint - [PR #13160](https://github.com/BerriAI/litellm/pull/13160)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-5 "Direct link to Features")

- **Caching**
  
  - Verify if cache entry has expired prior to serving it to client - [PR #13933](https://github.com/BerriAI/litellm/pull/13933)
  - Fixed error saving latency as timedelta on Redis - [PR #14040](https://github.com/BerriAI/litellm/pull/14040)
- **Router**
  
  - Refactored router to choose weights by 'weight', 'rpm', 'tpm' in one loop for simple\_shuffle - [PR #13562](https://github.com/BerriAI/litellm/pull/13562)
- **Logging**
  
  - Fixed LoggingWorker graceful shutdown to prevent CancelledError warnings - [PR #14050](https://github.com/BerriAI/litellm/pull/14050)
  - Enhanced logging for containers to log on files both with usual format and json format - [PR #13394](https://github.com/BerriAI/litellm/pull/13394)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **Dependencies**
  
  - Bumped `orjson` version to "3.11.2" - [PR #13969](https://github.com/BerriAI/litellm/pull/13969)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-6 "Direct link to Features")

- **AWS**
  
  - Add support for AWS assume\_role with a session token - [PR #13919](https://github.com/BerriAI/litellm/pull/13919)
- **OCI Provider**
  
  - Added oci\_key\_file as an optional\_parameter - [PR #14036](https://github.com/BerriAI/litellm/pull/14036)
- **Configuration**
  
  - Allow configuration to set threshold before request entry in spend log gets truncated - [PR #14042](https://github.com/BerriAI/litellm/pull/14042)
  - Enhanced proxy\_config configuration: add support for existing configmap in Helm charts - [PR #14041](https://github.com/BerriAI/litellm/pull/14041)
- **Docker**
  
  - Added back supervisor to non-root image - [PR #13922](https://github.com/BerriAI/litellm/pull/13922)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @ArthurRenault made their first contribution in [PR #13922](https://github.com/BerriAI/litellm/pull/13922)
- @stevenmanton made their first contribution in [PR #13919](https://github.com/BerriAI/litellm/pull/13919)
- @uc4w6c made their first contribution in [PR #13914](https://github.com/BerriAI/litellm/pull/13914)
- @nielsbosma made their first contribution in [PR #13573](https://github.com/BerriAI/litellm/pull/13573)
- @Yuki-Imajuku made their first contribution in [PR #13567](https://github.com/BerriAI/litellm/pull/13567)
- @codeflash-ai\[bot] made their first contribution in [PR #13988](https://github.com/BerriAI/litellm/pull/13988)
- @ColeFrench made their first contribution in [PR #13978](https://github.com/BerriAI/litellm/pull/13978)
- @dttran-glo made their first contribution in [PR #13969](https://github.com/BerriAI/litellm/pull/13969)
- @manascb1344 made their first contribution in [PR #13965](https://github.com/BerriAI/litellm/pull/13965)
- @DorZion made their first contribution in [PR #13572](https://github.com/BerriAI/litellm/pull/13572)
- @edwardsamuel made their first contribution in [PR #13536](https://github.com/BerriAI/litellm/pull/13536)
- @blahgeek made their first contribution in [PR #13374](https://github.com/BerriAI/litellm/pull/13374)
- @Deviad made their first contribution in [PR #13394](https://github.com/BerriAI/litellm/pull/13394)
- @XSAM made their first contribution in [PR #13775](https://github.com/BerriAI/litellm/pull/13775)
- @KRRT7 made their first contribution in [PR #14012](https://github.com/BerriAI/litellm/pull/14012)
- @ikaadil made their first contribution in [PR #13991](https://github.com/BerriAI/litellm/pull/13991)
- @timelfrink made their first contribution in [PR #13691](https://github.com/BerriAI/litellm/pull/13691)
- @qidu made their first contribution in [PR #13562](https://github.com/BerriAI/litellm/pull/13562)
- @nagyv made their first contribution in [PR #13243](https://github.com/BerriAI/litellm/pull/13243)
- @xywei made their first contribution in [PR #12885](https://github.com/BerriAI/litellm/pull/12885)
- @ericgtkb made their first contribution in [PR #12797](https://github.com/BerriAI/litellm/pull/12797)
- @NoWall57 made their first contribution in [PR #13945](https://github.com/BerriAI/litellm/pull/13945)
- @lmwang9527 made their first contribution in [PR #14050](https://github.com/BerriAI/litellm/pull/14050)
- @WilsonSunBritten made their first contribution in [PR #14042](https://github.com/BerriAI/litellm/pull/14042)
- @Const-antine made their first contribution in [PR #14041](https://github.com/BerriAI/litellm/pull/14041)
- @dmvieira made their first contribution in [PR #14040](https://github.com/BerriAI/litellm/pull/14040)
- @gotsysdba made their first contribution in [PR #14036](https://github.com/BerriAI/litellm/pull/14036)
- @moshemorad made their first contribution in [PR #14005](https://github.com/BerriAI/litellm/pull/14005)
- @joshualipman123 made their first contribution in [PR #13144](https://github.com/BerriAI/litellm/pull/13144)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.76.0-nightly...v1.76.1)[​](#full-changelog "Direct link to full-changelog")

info

LiteLLM is hiring a **Founding Backend Engineer**, in San Francisco.

[Apply here](https://www.ycombinator.com/companies/litellm/jobs/6uvoBp3-founding-backend-engineer) if you're interested!

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

info

This release is not live yet.

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### Bugs[​](#bugs "Direct link to Bugs")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Gpt-5 chat: clarify does not support function calling [PR #13612](https://github.com/BerriAI/litellm/pull/13612), s/o  @[superpoussin22](https://github.com/superpoussin22)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - fix vertexai batch file format by @[thiagosalvatore](https://github.com/thiagosalvatore) in [PR #13576](https://github.com/BerriAI/litellm/pull/13576)
- [**LiteLLM Proxy**](https://docs.litellm.ai/docs/providers/litellm_proxy)
  
  - Add support for calling image\_edits + image\_generations via SDK to Proxy - [PR #13735](https://github.com/BerriAI/litellm/pull/13735)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Fix max\_output\_tokens value for anthropic Claude 4 - [PR #13526](https://github.com/BerriAI/litellm/pull/13526)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix prompt caching cost calculation - [PR #13742](https://github.com/BerriAI/litellm/pull/13742)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Support `../openai/v1/respones` api base - [PR #13526](https://github.com/BerriAI/litellm/pull/13526)
  - Fix azure/gpt-5-chat max\_input\_tokens - [PR #13660](https://github.com/BerriAI/litellm/pull/13660)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - streaming ASCII encoding issue - [PR #13675](https://github.com/BerriAI/litellm/pull/13675)
- [**Baseten**](https://docs.litellm.ai/docs/providers/baseten)
  
  - Refactored integration to use new openai-compatible endpoints - [PR #13783](https://github.com/BerriAI/litellm/pull/13783)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - fix application inference profile for pass-through endpoints for bedrock - [PR #13881](https://github.com/BerriAI/litellm/pull/13881)
- [**DataRobot**](https://docs.litellm.ai/docs/providers/datarobot)
  
  - Updated URL handling for DataRobot provider URL - [PR #13880](https://github.com/BerriAI/litellm/pull/13880)

#### Features[​](#features "Direct link to Features")

- [**Together AI**](https://docs.litellm.ai/docs/providers/together)
  
  - Added Qwen3, Deepseek R1 0528 Throughput, GLM 4.5 and GPT-OSS models cost tracking - [PR #13637](https://github.com/BerriAI/litellm/pull/13637), s/o  @[Tasmay-Tibrewal](https://github.com/Tasmay-Tibrewal)
- [**Fireworks AI**](https://docs.litellm.ai/docs/providers/fireworks_ai)
  
  - add fireworks\_ai/accounts/fireworks/models/deepseek-v3-0324 - [PR #13821](https://github.com/BerriAI/litellm/pull/13821)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add VertexAI qwen API Service - [PR #13828](https://github.com/BerriAI/litellm/pull/13828)
  - Add new VertexAI image models vertex\_ai/imagen-4.0-generate-001, vertex\_ai/imagen-4.0-ultra-generate-001, vertex\_ai/imagen-4.0-fast-generate-001  - [PR #13874](https://github.com/BerriAI/litellm/pull/13874)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Add long context support w/ cost tracking - [PR #13759](https://github.com/BerriAI/litellm/pull/13759)
- [**DeepInfra**](https://docs.litellm.ai/docs/providers/deepinfra)
  
  - Add rerank endpoint support for deepinfra - [PR #13820](https://github.com/BerriAI/litellm/pull/13820)
  - Add new models for cost tracking - [PR #13883](https://github.com/BerriAI/litellm/pull/13883), s/o  @[Toy-97](https://github.com/Toy-97)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add tool prompt caching on async calls - [PR #13803](https://github.com/BerriAI/litellm/pull/13803), s/o  @[UlookEE](https://github.com/UlookEE)
  - role chaining and session name with webauthentication for aws bedrock - [PR #13753](https://github.com/BerriAI/litellm/pull/13753), s/o @[RichardoC](https://github.com/RichardoC)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Handle Ollama null response when using tool calling with non-tool trained models - [PR #13902](https://github.com/BerriAI/litellm/pull/13902)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Add deepseek/deepseek-chat-v3.1 support - [PR #13897](https://github.com/BerriAI/litellm/pull/13897)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Add support for calling mistral files via chat completions - [PR #13866](https://github.com/BerriAI/litellm/pull/13866), s/o  @[jinskjoy](https://github.com/jinskjoy)
  - Handle empty assistant content - [PR #13671](https://github.com/BerriAI/litellm/pull/13671)
  - Support new ‘thinking’ response block - [PR #13671](https://github.com/BerriAI/litellm/pull/13671)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks)
  
  - remove deprecated dbrx models (dbrx-instruct, llama 3.1) - [PR #13843](https://github.com/BerriAI/litellm/pull/13843)
- [**AI/ML API**](https://docs.litellm.ai/docs/providers/ai_ml_api)
  
  - Image gen api support - [PR #13893](https://github.com/BerriAI/litellm/pull/13893)

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - add default api version for openai responses api calls - [PR #13526](https://github.com/BerriAI/litellm/pull/13526)
  - support allowed\_openai\_params - [PR #13671](https://github.com/BerriAI/litellm/pull/13671)

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- fix StreamableHTTPSessionManager .run() error - [PR #13666](https://github.com/BerriAI/litellm/pull/13666)

## Vector Stores[​](#vector-stores "Direct link to Vector Stores")

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Using LiteLLM Managed Credentials for Query - [PR #13787](https://github.com/BerriAI/litellm/pull/13787)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- [**Passthrough**](https://docs.litellm.ai/docs/pass_through/intro)
  
  - Fix query passthrough deletion - [PR #13622](https://github.com/BerriAI/litellm/pull/13622)

#### Features[​](#features-1 "Direct link to Features")

- **Models**
  
  - Add Search Functionality for Public Model Names in Model Dashboard - [PR #13687](https://github.com/BerriAI/litellm/pull/13687)
  - Auto-Add `azure/` to deployment Name in UI - [PR #13685](https://github.com/BerriAI/litellm/pull/13685)
  - Models page row UI restructure - [PR #13771](https://github.com/BerriAI/litellm/pull/13771)
- **Notifications**
  
  - Add new notifications toast UI everywhere - [PR #13813](https://github.com/BerriAI/litellm/pull/13813)
- **Keys**
  
  - Fix key edit settings after regenerating a key - [PR #13815](https://github.com/BerriAI/litellm/pull/13815)
  - Require team\_id when creating service account keys - [PR #13873](https://github.com/BerriAI/litellm/pull/13873)
  - Filter - show all options on filter option click - [PR #13858](https://github.com/BerriAI/litellm/pull/13858)
- **Usage**
  
  - Fix ‘Cannot read properties of undefined’ exception on user agent activity tab - [PR #13892](https://github.com/BerriAI/litellm/pull/13892)
- **SSO**
  
  - Free SSO usage for up to 5 users - [PR #13843](https://github.com/BerriAI/litellm/pull/13843)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/bedrock)
  
  - Add bedrock api key support - [PR #13835](https://github.com/BerriAI/litellm/pull/13835)

#### Features[​](#features-2 "Direct link to Features")

- [**Datadog LLM Observability**](https://docs.litellm.ai/docs/integrations/datadog)
  
  - Add support for Failure Logging [PR #13726](https://github.com/BerriAI/litellm/pull/13726)
  - Add time to first token, litellm overhead, guardrail overhead latency metrics - [PR #13734](https://github.com/BerriAI/litellm/pull/13734)
  - Add support for tracing guardrail input/output - [PR #13767](https://github.com/BerriAI/litellm/pull/13767)
- [**Langfuse OTEL**](https://docs.litellm.ai/docs/integrations/langfuse)
  
  - Allow using Key/Team Based Logging - [PR #13791](https://github.com/BerriAI/litellm/pull/13791)
- [**AIM**](https://docs.litellm.ai/docs/integrations/aim)
  
  - Migrate to new firewall API - [PR #13748](https://github.com/BerriAI/litellm/pull/13748)
- [**OTEL**](https://docs.litellm.ai/docs/observability/opentelemetry_integration)
  
  - Add OTEL tracing for actual LLM API call - [PR #13836](https://github.com/BerriAI/litellm/pull/13836)
- [**MLFlow**](https://docs.litellm.ai/docs/observability/mlflow_integration)
  
  - Include predicted output in MLflow tracing - [PR #13795](https://github.com/BerriAI/litellm/pull/13795), s/o @TomeHirata

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Bugs[​](#bugs-6 "Direct link to Bugs")

- [**Cooldowns**](https://docs.litellm.ai/docs/routing#how-cooldowns-work)
  
  - don't return raw Azure Exceptions to client (can contain prompt leakage) - [PR #13529](https://github.com/BerriAI/litellm/pull/13529)
- [**Auto-router**](https://docs.litellm.ai/docs/proxy/auto_routing)
  
  - Ensures the relevant dependencies for auto router existing on LiteLLM Docker - [PR #13788](https://github.com/BerriAI/litellm/pull/13788)
- **Model Alias**
  
  - Fix calling key with access to model alias - [PR #13830](https://github.com/BerriAI/litellm/pull/13830)

#### Features[​](#features-3 "Direct link to Features")

- [**S3 Caching**](https://docs.litellm.ai/docs/proxy/caching)
  
  - Use namespace as prefix for s3 cache - [PR #13704](https://github.com/BerriAI/litellm/pull/13704)
  - Async S3 Caching support (4x RPS improvement) - [PR #13852](https://github.com/BerriAI/litellm/pull/13852), s/o @[michal-otmianowski](https://github.com/michal-otmianowski)
- **Model Group header forwarding**
  
  - reuse same logic as global header forwarding - [PR #13741](https://github.com/BerriAI/litellm/pull/13741)
  - add support for hosted\_vllm on UI - [PR #13885](https://github.com/BerriAI/litellm/pull/13885)
- **Performance**
  
  - Improve LiteLLM Python SDK RPS by +200 RPS (braintrust import + aiohttp transport fixes) - [PR #13839](https://github.com/BerriAI/litellm/pull/13839)
  - Use O(1) Set lookups for model routing - [PR #13879](https://github.com/BerriAI/litellm/pull/13879)
  - Reduce Significant CPU overhead from litellm\_logging.py - [PR #13895](https://github.com/BerriAI/litellm/pull/13895)
  - Improvements for Async Success Handler (Logging Callbacks) - Approx +130 RPS - [PR #13905](https://github.com/BerriAI/litellm/pull/13905)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Bugs[​](#bugs-7 "Direct link to Bugs")

- **SDK**
  
  - Fix litellm compatibility with newest release of openAI (&gt;v1.100.0) - [PR #13728](https://github.com/BerriAI/litellm/pull/13728)
- **Helm**
  
  - Add possibility to configure resources for migrations-job - [PR #13617](https://github.com/BerriAI/litellm/pull/13617)
  - Ensure Helm chart auto generated master keys follow sk-xxxx format - [PR #13871](https://github.com/BerriAI/litellm/pull/13871)
  - Enhance database configuration: add support for optional endpointKey - [PR #13763](https://github.com/BerriAI/litellm/pull/13763)
- **Rate Limits**
  
  - fixing descriptor/response size mismatch on parallel\_request\_limiter\_v3 - [PR #13863](https://github.com/BerriAI/litellm/pull/13863), s/o  @[luizrennocosta](https://github.com/luizrennocosta)
- **Non-root**
  
  - fix permission access on prisma migrate in non-root image - [PR #13848](https://github.com/BerriAI/litellm/pull/13848), s/o @[Ithanil](https://github.com/Ithanil)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.75.8-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Team Member Rate Limits** - Individual rate limiting for team members with JWT authentication support.
- **Performance Improvements** - New experimental HTTP handler flag for 100+ RPS improvement on OpenAI calls.
- **GPT-5 Model Family Support** - Full support for OpenAI's GPT-5 models with `reasoning_effort` parameter and Azure OpenAI integration.
- **Azure AI Flux Image Generation** - Support for Azure AI's Flux image generation models.

* * *

## Team Member Rate Limits[​](#team-member-rate-limits "Direct link to Team Member Rate Limits")

LiteLLM MCP Architecture: Use MCP tools with all LiteLLM supported models

This release adds support for setting rate limits on individual members (including machine users) within a team. Teams can now give each agent its own rate limits—so that heavy-traffic agents don’t impact other agents or human users.

Agents can authenticate with LiteLLM using JWT and the same team role as human users, while still enforcing per-agent rate limits.

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesAzure AI`azure_ai/FLUX-1.1-pro`--$40/imageImage generationAzure AI`azure_ai/FLUX.1-Kontext-pro`--$40/imageImage generationVertex AI`vertex_ai/deepseek-ai/deepseek-r1-0528-maas`65k$1.35$5.4Chat completions + reasoningOpenRouter`openrouter/deepseek/deepseek-chat-v3-0324`65k$0.14$0.28Chat completions

#### Features[​](#features "Direct link to Features")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Added `reasoning_effort` parameter support for GPT-5 model family - [PR #13475](https://github.com/BerriAI/litellm/pull/13475), [Get Started](https://docs.litellm.ai/docs/providers/openai#openai-chat-completion-models)
  - Support for `reasoning` parameter in Responses API - [PR #13475](https://github.com/BerriAI/litellm/pull/13475), [Get Started](https://docs.litellm.ai/docs/response_api)
- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure/azure)
  
  - GPT-5 support with max\_tokens and `reasoning` parameter - [PR #13510](https://github.com/BerriAI/litellm/pull/13510), [Get Started](https://docs.litellm.ai/docs/providers/azure/azure#gpt-5-models)
- [**AWS Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Streaming support for bedrock gpt-oss model family - [PR #13346](https://github.com/BerriAI/litellm/pull/13346), [Get Started](https://docs.litellm.ai/docs/providers/bedrock#openai-gpt-oss)
  - `/messages` endpoint compatibility with `bedrock/converse/<model>` - [PR #13627](https://github.com/BerriAI/litellm/pull/13627)
  - Cache point support for assistant and tool messages - [PR #13640](https://github.com/BerriAI/litellm/pull/13640)
- [**Azure AI**](https://docs.litellm.ai/docs/providers/azure)
  
  - New Azure AI Flux Image Generation provider - [PR #13592](https://github.com/BerriAI/litellm/pull/13592), [Get Started](https://docs.litellm.ai/docs/providers/azure_ai_img)
  - Fixed Content-Type header for image generation - [PR #13584](https://github.com/BerriAI/litellm/pull/13584)
- [**CometAPI**](https://docs.litellm.ai/docs/providers/comet)
  
  - New provider support with chat completions and streaming - [PR #13458](https://github.com/BerriAI/litellm/pull/13458)
- [**SambaNova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Added embedding model support - [PR #13308](https://github.com/BerriAI/litellm/pull/13308), [Get Started](https://docs.litellm.ai/docs/providers/sambanova#sambanova---embeddings)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Added `/countTokens` endpoint support for Gemini CLI integration - [PR #13545](https://github.com/BerriAI/litellm/pull/13545)
  - Token counter support for VertexAI models - [PR #13558](https://github.com/BerriAI/litellm/pull/13558)
- [**hosted\_vllm**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Added `reasoning_effort` parameter support - [PR #13620](https://github.com/BerriAI/litellm/pull/13620), [Get Started](https://docs.litellm.ai/docs/providers/vllm#reasoning-effort)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**OCI**](https://docs.litellm.ai/docs/providers/oci)
  
  - Fixed streaming issues - [PR #13437](https://github.com/BerriAI/litellm/pull/13437)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Fixed GPT-OSS streaming with 'thinking' field - [PR #13375](https://github.com/BerriAI/litellm/pull/13375)
- [**VolcEngine**](https://docs.litellm.ai/docs/providers/volcengine)
  
  - Fixed thinking disabled parameter handling - [PR #13598](https://github.com/BerriAI/litellm/pull/13598)
- [**Streaming**](https://docs.litellm.ai/docs/completion/stream)
  
  - Consistent 'finish\_reason' chunk indexing - [PR #13560](https://github.com/BerriAI/litellm/pull/13560)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/messages**](https://docs.litellm.ai/docs/anthropic/messages)
  
  - Tool use arguments properly returned for non-anthropic models - [PR #13638](https://github.com/BerriAI/litellm/pull/13638)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**Real-time API**](https://docs.litellm.ai/docs/realtime)
  
  - Fixed endpoint for no intent scenarios - [PR #13476](https://github.com/BerriAI/litellm/pull/13476)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Fixed `stream=True` + `background=True` with Responses API - [PR #13654](https://github.com/BerriAI/litellm/pull/13654)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-2 "Direct link to Features")

- **Access Control & Configuration**
  
  - Enhanced MCPServerManager with access groups and description support - [PR #13549](https://github.com/BerriAI/litellm/pull/13549)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **Authentication**
  
  - Fixed MCP gateway key authentication - [PR #13630](https://github.com/BerriAI/litellm/pull/13630)

[Read More](https://docs.litellm.ai/docs/mcp)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Team Management**
  
  - Team Member Rate Limits implementation - [PR #13601](https://github.com/BerriAI/litellm/pull/13601)
  - JWT authentication support for team member rate limits - [PR #13601](https://github.com/BerriAI/litellm/pull/13601)
  - Show team member TPM/RPM limits in UI - [PR #13662](https://github.com/BerriAI/litellm/pull/13662)
  - Allow editing team member RPM/TPM limits - [PR #13669](https://github.com/BerriAI/litellm/pull/13669)
  - Allow unsetting TPM and RPM in Teams Settings - [PR #13430](https://github.com/BerriAI/litellm/pull/13430)
  - Team Member Permissions Page access column changes - [PR #13145](https://github.com/BerriAI/litellm/pull/13145)
- **Key Management**
  
  - Display errors from backend on the UI Keys page - [PR #13435](https://github.com/BerriAI/litellm/pull/13435)
  - Added confirmation modal before deleting keys - [PR #13655](https://github.com/BerriAI/litellm/pull/13655)
  - Support for `user` parameter in LiteLLM SDK to Proxy communication - [PR #13555](https://github.com/BerriAI/litellm/pull/13555)
- **UI Improvements**
  
  - Fixed internal users table overflow - [PR #12736](https://github.com/BerriAI/litellm/pull/12736)
  - Enhanced chart readability with short-form notation for large numbers - [PR #12370](https://github.com/BerriAI/litellm/pull/12370)
  - Fixed image overflow in LiteLLM model display - [PR #13639](https://github.com/BerriAI/litellm/pull/13639)
  - Removed ambiguous network response errors - [PR #13582](https://github.com/BerriAI/litellm/pull/13582)
- **Credentials**
  
  - Added CredentialDeleteModal component and integration with CredentialsPanel - [PR #13550](https://github.com/BerriAI/litellm/pull/13550)
- **Admin & Permissions**
  
  - Allow routes for admin viewer - [PR #13588](https://github.com/BerriAI/litellm/pull/13588)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- **SCIM Integration**
  
  - Fixed SCIM Team Memberships metadata handling - [PR #13553](https://github.com/BerriAI/litellm/pull/13553)
- **Authentication**
  
  - Fixed incorrect key info endpoint - [PR #13633](https://github.com/BerriAI/litellm/pull/13633)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Langfuse OTEL**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Added key/team logging for Langfuse OTEL Logger - [PR #13512](https://github.com/BerriAI/litellm/pull/13512)
  - Fixed LangfuseOtelSpanAttributes constants to match expected values - [PR #13659](https://github.com/BerriAI/litellm/pull/13659)
- [**MLflow**](https://docs.litellm.ai/docs/proxy/logging#mlflow)
  
  - Updated MLflow logger usage span attributes - [PR #13561](https://github.com/BerriAI/litellm/pull/13561)

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- **Security**
  
  - Hide sensitive data in `/model/info` - azure entra client\_secret - [PR #13577](https://github.com/BerriAI/litellm/pull/13577)
  - Fixed trivy/secrets false positives - [PR #13631](https://github.com/BerriAI/litellm/pull/13631)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-5 "Direct link to Features")

- **HTTP Performance**
  
  - New 'EXPERIMENTAL\_OPENAI\_BASE\_LLM\_HTTP\_HANDLER' flag for +100 RPS improvement on OpenAI calls - [PR #13625](https://github.com/BerriAI/litellm/pull/13625)
- **Database Monitoring**
  
  - Added DB metrics to Prometheus - [PR #13626](https://github.com/BerriAI/litellm/pull/13626)
- **Error Handling**
  
  - Added safe divide by 0 protection to prevent crashes - [PR #13624](https://github.com/BerriAI/litellm/pull/13624)

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- **Dependencies**
  
  - Updated boto3 to 1.36.0 and aioboto3 to 13.4.0 - [PR #13665](https://github.com/BerriAI/litellm/pull/13665)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-6 "Direct link to Features")

- **Database**
  
  - Removed redundant `use_prisma_migrate` flag - now default - [PR #13555](https://github.com/BerriAI/litellm/pull/13555)
- **LLM Translation**
  
  - Added model ID check - [PR #13507](https://github.com/BerriAI/litellm/pull/13507)
  - Refactored Anthropic configurations and added support for `anthropic_beta` headers - [PR #13590](https://github.com/BerriAI/litellm/pull/13590)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @TensorNull made their first contribution in [PR #13458](https://github.com/BerriAI/litellm/pull/13458)
- @MajorD00m made their first contribution in [PR #13577](https://github.com/BerriAI/litellm/pull/13577)
- @VerunicaM made their first contribution in [PR #13584](https://github.com/BerriAI/litellm/pull/13584)
- @huangyafei made their first contribution in [PR #13607](https://github.com/BerriAI/litellm/pull/13607)
- @TomeHirata made their first contribution in [PR #13561](https://github.com/BerriAI/litellm/pull/13561)
- @willfinnigan made their first contribution in [PR #13659](https://github.com/BerriAI/litellm/pull/13659)
- @dcbark01 made their first contribution in [PR #13633](https://github.com/BerriAI/litellm/pull/13633)
- @javacruft made their first contribution in [PR #13631](https://github.com/BerriAI/litellm/pull/13631)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.75.5-stable.rc-draft...v1.75.8-nightly)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.75.5-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Redis - Latency Improvements** - Reduces P99 latency by 50% with Redis enabled.
- **Responses API Session Management** - Support for managing responses API sessions with images.
- **Oracle Cloud Infrastructure** - New LLM provider for calling models on Oracle Cloud Infrastructure.
- **Digital Ocean's Gradient AI** - New LLM provider for calling models on Digital Ocean's Gradient AI platform.

* * *

### Risk of Upgrade[​](#risk-of-upgrade "Direct link to Risk of Upgrade")

If you build the proxy from the pip package, you should hold off on upgrading. This version makes `prisma migrate deploy` our default for managing the DB. This is safer, as it doesn't reset the DB, but it requires a manual `prisma generate` step.

Users of our Docker image, are **not** affected by this change.

* * *

## Redis Latency Improvements[​](#redis-latency-improvements "Direct link to Redis Latency Improvements")

This release adds in-memory caching for Redis requests, enabling faster response times in high-traffic. Now, LiteLLM instances will check their in-memory cache for a cache hit, before checking Redis. This reduces caching-related latency from 100ms for LLM API calls to sub-1ms, on cache hits.

* * *

## Responses API Session Management w/ Images[​](#responses-api-session-management-w-images "Direct link to Responses API Session Management w/ Images")

LiteLLM now supports session management for Responses API requests with images. This is great for use-cases like chatbots, that are using the Responses API to track the state of a conversation. LiteLLM session management works across **ALL** LLM API's (including Anthropic, Bedrock, OpenAI, etc). LiteLLM session management works by storing the request and response content in an s3 bucket, you can specify.

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)Bedrock`bedrock/us.anthropic.claude-opus-4-1-20250805-v1:0`200k$15$75Bedrock`bedrock/openai.gpt-oss-20b-1:0`200k0.070.3Bedrock`bedrock/openai.gpt-oss-120b-1:0`200k0.150.6Fireworks AI`fireworks_ai/accounts/fireworks/models/glm-4p5`128k0.552.19Fireworks AI`fireworks_ai/accounts/fireworks/models/glm-4p5-air`128k0.220.88Fireworks AI`fireworks_ai/accounts/fireworks/models/gpt-oss-120b`1310720.150.6Fireworks AI`fireworks_ai/accounts/fireworks/models/gpt-oss-20b`1310720.050.2Groq`groq/openai/gpt-oss-20b`1310720.10.5Groq`groq/openai/gpt-oss-120b`1310720.150.75OpenAI`openai/gpt-5`400k1.2510OpenAI`openai/gpt-5-2025-08-07`400k1.2510OpenAI`openai/gpt-5-mini`400k0.252OpenAI`openai/gpt-5-mini-2025-08-07`400k0.252OpenAI`openai/gpt-5-nano`400k0.050.4OpenAI`openai/gpt-5-nano-2025-08-07`400k0.050.4OpenAI`openai/gpt-5-chat`400k1.2510OpenAI`openai/gpt-5-chat-latest`400k1.2510Azure`azure/gpt-5`400k1.2510Azure`azure/gpt-5-2025-08-07`400k1.2510Azure`azure/gpt-5-mini`400k0.252Azure`azure/gpt-5-mini-2025-08-07`400k0.252Azure`azure/gpt-5-nano-2025-08-07`400k0.050.4Azure`azure/gpt-5-nano`400k0.050.4Azure`azure/gpt-5-chat`400k1.2510Azure`azure/gpt-5-chat-latest`400k1.2510

#### Features[​](#features "Direct link to Features")

- [**OCI**](https://docs.litellm.ai/docs/providers/oci)
  
  - New LLM provider - [PR #13206](https://github.com/BerriAI/litellm/pull/13206)
- [**JinaAI**](https://docs.litellm.ai/docs/providers/jina_ai)
  
  - support multimodal embedding models - [PR #13181](https://github.com/BerriAI/litellm/pull/13181)
- **GPT-5 ([OpenAI](https://docs.litellm.ai/docs/providers/openai)/[Azure](https://docs.litellm.ai/docs/providers/azure))**
  
  - Support drop\_params for temperature - [PR #13390](https://github.com/BerriAI/litellm/pull/13390)
  - Map max\_tokens to max\_completion\_tokens - [PR #13390](https://github.com/BerriAI/litellm/pull/13390)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Add claude-opus-4-1 on model cost map - [PR #13384](https://github.com/BerriAI/litellm/pull/13384)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Add gpt-oss to model cost map - [PR #13442](https://github.com/BerriAI/litellm/pull/13442)
- [**Cerebras**](https://docs.litellm.ai/docs/providers/cerebras)
  
  - Add gpt-oss to model cost map - [PR #13442](https://github.com/BerriAI/litellm/pull/13442)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Support drop params for ‘temperature’ on o-series models - [PR #13353](https://github.com/BerriAI/litellm/pull/13353)
- [**GradientAI**](https://docs.litellm.ai/docs/providers/gradient_ai)
  
  - New LLM Provider - [PR #12169](https://github.com/BerriAI/litellm/pull/12169)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Add ‘service\_tier’ and ‘safety\_identifier’ as supported responses api params - [PR #13258](https://github.com/BerriAI/litellm/pull/13258)
  - Correct pricing for web search on 4o-mini - [PR #13269](https://github.com/BerriAI/litellm/pull/13269)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Handle $id and $schema fields when calling mistral - [PR #13389](https://github.com/BerriAI/litellm/pull/13389)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- `/responses`
  
  - Responses API Session Handling w/ support for images - [PR #13347](https://github.com/BerriAI/litellm/pull/13347)
  - failed if input containing ResponseReasoningItem - [PR #13465](https://github.com/BerriAI/litellm/pull/13465)
  - Support custom tools - [PR #13418](https://github.com/BerriAI/litellm/pull/13418)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- `/chat/completions`
  
  - Fix completion\_token\_details usage object missing ‘text’ tokens - [PR #13234](https://github.com/BerriAI/litellm/pull/13234)
  - (SDK) handle tool being a pydantic object - [PR #13274](https://github.com/BerriAI/litellm/pull/13274)
  - include cost in streaming usage object - [PR #13418](https://github.com/BerriAI/litellm/pull/13418)
  - Exclude none fields on /chat/completion - allows usage with n8n - [PR #13320](https://github.com/BerriAI/litellm/pull/13320)
- `/responses`
  
  - Transform function call in response for non-openai models (gemini/anthropic) - [PR #13260](https://github.com/BerriAI/litellm/pull/13260)
  - Fix unsupported operand error with model groups - [PR #13293](https://github.com/BerriAI/litellm/pull/13293)
  - Responses api session management for streaming responses - [PR #13396](https://github.com/BerriAI/litellm/pull/13396)
- `/v1/messages`
  
  - Added litellm claude code count tokens - [PR #13261](https://github.com/BerriAI/litellm/pull/13261)
- `/vector_stores`
  
  - Fix create/search vector store errors - [PR #13285](https://github.com/BerriAI/litellm/pull/13285)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-2 "Direct link to Features")

- Add route check for internal users - [PR #13350](https://github.com/BerriAI/litellm/pull/13350)
- MCP Guardrails - docs - [PR #13392](https://github.com/BerriAI/litellm/pull/13392)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- Fix auth on UI for bearer token servers - [PR #13312](https://github.com/BerriAI/litellm/pull/13312)
- allow access group on mcp tool retrieval - [PR #13425](https://github.com/BerriAI/litellm/pull/13425)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Teams**
  
  - Add team deletion check for teams with keys - [PR #12953](https://github.com/BerriAI/litellm/pull/12953)
- **Models**
  
  - Add ability to set model alias per key/team - [PR #13276](https://github.com/BerriAI/litellm/pull/13276)
  - New button to reload model pricing from model cost map - [PR #13464](https://github.com/BerriAI/litellm/pull/13464), [PR #13470](https://github.com/BerriAI/litellm/pull/13470)
- **Keys**
  
  - Make ‘team’ field required when creating service account keys - [PR #13302](https://github.com/BerriAI/litellm/pull/13302)
  - Gray out key-based logging settings for non-enterprise users - prevents confusion on if ‘logging’ all up is supported - [PR #13431](https://github.com/BerriAI/litellm/pull/13431)
- **Navbar**
  
  - Add logo customization for LiteLLM admin UI - [PR #12958](https://github.com/BerriAI/litellm/pull/12958)
- **Logs**
  
  - Add token breakdowns on logs + session page - [PR #13357](https://github.com/BerriAI/litellm/pull/13357)
- **Usage**
  
  - Ensure Usage Page loads after the DB has large entries - [PR #13400](https://github.com/BerriAI/litellm/pull/13400)
- **Test Key Page**
  
  - allow uploading images for /chat/completions and /responses - [PR #13445](https://github.com/BerriAI/litellm/pull/13445)
- **MCP**
  
  - Add auth tokens to local storage auth - [PR #13473](https://github.com/BerriAI/litellm/pull/13473)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- **Custom Root Path**
  
  - Fix login route when SSO is enabled - [PR #13267](https://github.com/BerriAI/litellm/pull/13267)
- **Customers/End-users**
  
  - Allow calling /v1/models when end user over budget - allows model listing to work on OpenWebUI when customer over budget - [PR #13320](https://github.com/BerriAI/litellm/pull/13320)
- **Teams**
  
  - Remove user - team membership, when user removed from team - [PR #13433](https://github.com/BerriAI/litellm/pull/13433)
- **Errors**
  
  - Bubble up network errors to user for Logging and Alerts page - [PR #13427](https://github.com/BerriAI/litellm/pull/13427)
- **Model Hub**
  
  - Show pricing for azure models, when base model is set - [PR #13418](https://github.com/BerriAI/litellm/pull/13418)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- **Bedrock Guardrails**
  
  - Redacted sensitive information in bedrock guardrails error message - [PR #13356](https://github.com/BerriAI/litellm/pull/13356)
- **Standard Logging Payload**
  
  - Fix ‘can’t register atextexit’ bug - [PR #13436](https://github.com/BerriAI/litellm/pull/13436)

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- **Braintrust**
  
  - Allow setting of braintrust callback base url - [PR #13368](https://github.com/BerriAI/litellm/pull/13368)
- **OTEL**
  
  - Track pre\_call hook latency - [PR #13362](https://github.com/BerriAI/litellm/pull/13362)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-5 "Direct link to Features")

- **Team-BYOK models**
  
  - Add wildcard model support - [PR #13278](https://github.com/BerriAI/litellm/pull/13278)
- **Caching**
  
  - GCP IAM auth support for caching - [PR #13275](https://github.com/BerriAI/litellm/pull/13275)
- **Latency**
  
  - reduce p99 latency w/ redis enabled by 50% - only updates model usage if tpm/rpm limits set - [PR #13362](https://github.com/BerriAI/litellm/pull/13362)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-6 "Direct link to Features")

- **Models**
  
  - Support /v1/models/{model\_id} retrieval - [PR #13268](https://github.com/BerriAI/litellm/pull/13268)
- **Multi-instance**
  
  - Ensure disable\_llm\_api\_endpoints works - [PR #13278](https://github.com/BerriAI/litellm/pull/13278)
- **Logs**
  
  - Add apscheduler log suppress - [PR #13299](https://github.com/BerriAI/litellm/pull/13299)
- **Helm**
  
  - Add labels to migrations job template - [PR #13343](https://github.com/BerriAI/litellm/pull/13343) s/o [@unique-jakub](https://github.com/unique-jakub)

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- **Non-root image**
  
  - Fix non-root image for migration - [PR #13379](https://github.com/BerriAI/litellm/pull/13379)
- **Get Routes**
  
  - Load get routes when using fastapi-offline - [PR #13466](https://github.com/BerriAI/litellm/pull/13466)
- **Health checks**
  
  - Generate unique trace IDs for Langfuse health checks - [PR #13468](https://github.com/BerriAI/litellm/pull/13468)
- **Swagger**
  
  - Allow using Swagger for /chat/completions - [PR #13469](https://github.com/BerriAI/litellm/pull/13469)
- **Auth**
  
  - Fix JWTs access not working with model access groups - [PR #13474](https://github.com/BerriAI/litellm/pull/13474)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @bbartels made their first contribution in [https://github.com/BerriAI/litellm/pull/13244](https://github.com/BerriAI/litellm/pull/13244)
- @breno-aumo made their first contribution in [https://github.com/BerriAI/litellm/pull/13206](https://github.com/BerriAI/litellm/pull/13206)
- @pascalwhoop made their first contribution in [https://github.com/BerriAI/litellm/pull/13122](https://github.com/BerriAI/litellm/pull/13122)
- @ZPerling made their first contribution in [https://github.com/BerriAI/litellm/pull/13045](https://github.com/BerriAI/litellm/pull/13045)
- @zjx20 made their first contribution in [https://github.com/BerriAI/litellm/pull/13181](https://github.com/BerriAI/litellm/pull/13181)
- @edwarddamato made their first contribution in [https://github.com/BerriAI/litellm/pull/13368](https://github.com/BerriAI/litellm/pull/13368)
- @msannan2 made their first contribution in [https://github.com/BerriAI/litellm/pull/12169](https://github.com/BerriAI/litellm/pull/12169)

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.74.15-stable...v1.75.5-stable.rc-draft)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.74.15-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **User Agent Activity Tracking** - Track how much usage each coding tool gets.
- **Prompt Management** - Use Git-Ops style prompt management with prompt templates.
- **MCP Gateway: Guardrails** - Support for using Guardrails with MCP servers.
- **Google AI Studio Imagen4** - Support for using Imagen4 models on Google AI Studio.

* * *

## User Agent Activity Tracking[​](#user-agent-activity-tracking "Direct link to User Agent Activity Tracking")

This release brings support for tracking usage and costs for AI-powered coding tools like Claude Code, Roo Code, Gemini CLI through LiteLLM. You can now track LLM cost, total tokens used, and DAU/WAU/MAU for each coding tool.

This is great to central AI Platform teams looking to track how they are helping developer productivity.

[Read More](https://docs.litellm.ai/docs/tutorials/cost_tracking_coding)

* * *

## Prompt Management[​](#prompt-management "Direct link to Prompt Management")

[Read More](https://docs.litellm.ai/docs/proxy/prompt_management)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)Cost per ImageOpenRouter`openrouter/x-ai/grok-4`256k$3$15N/AGoogle AI Studio`gemini/imagen-4.0-generate-001`N/AN/AN/A$0.04Google AI Studio`gemini/imagen-4.0-ultra-generate-001`N/AN/AN/A$0.06Google AI Studio`gemini/imagen-4.0-fast-generate-001`N/AN/AN/A$0.02Google AI Studio`gemini/imagen-3.0-generate-002`N/AN/AN/A$0.04Google AI Studio`gemini/imagen-3.0-generate-001`N/AN/AN/A$0.04Google AI Studio`gemini/imagen-3.0-fast-generate-001`N/AN/AN/A$0.02

#### Features[​](#features "Direct link to Features")

- [**Google AI Studio**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Added Google AI Studio Imagen4 model family support - [PR #13065](https://github.com/BerriAI/litellm/pull/13065), [Get Started](https://docs.litellm.ai/docs/providers/google_ai_studio/image_gen)
- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure/azure)
  
  - Azure `api_version="preview"` support - [PR #13072](https://github.com/BerriAI/litellm/pull/13072), [Get Started](https://docs.litellm.ai/docs/providers/azure/azure#setting-api-version)
  - Password protected certificate files support - [PR #12995](https://github.com/BerriAI/litellm/pull/12995), [Get Started](https://docs.litellm.ai/docs/providers/azure/azure#authentication)
- [**AWS Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Cost tracking via Anthropic `/v1/messages` - [PR #13072](https://github.com/BerriAI/litellm/pull/13072)
  - Computer use support - [PR #13150](https://github.com/BerriAI/litellm/pull/13150)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Added Grok4 model support - [PR #13018](https://github.com/BerriAI/litellm/pull/13018)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Auto Cache Control Injection - Improved cache\_control\_injection\_points with negative index support - [PR #13187](https://github.com/BerriAI/litellm/pull/13187), [Get Started](https://docs.litellm.ai/docs/tutorials/prompt_caching)
  - Working mid-stream fallbacks with token usage tracking - [PR #13149](https://github.com/BerriAI/litellm/pull/13149), [PR #13170](https://github.com/BerriAI/litellm/pull/13170)
- [**Perplexity**](https://docs.litellm.ai/docs/providers/perplexity)
  
  - Citation annotations support - [PR #13225](https://github.com/BerriAI/litellm/pull/13225)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix merge\_reasoning\_content\_in\_choices parameter issue - [PR #13066](https://github.com/BerriAI/litellm/pull/13066), [Get Started](https://docs.litellm.ai/docs/tutorials/openweb_ui#render-thinking-content-on-open-webui)
  - Added support for using `GOOGLE_API_KEY` environment variable for Google AI Studio - [PR #12507](https://github.com/BerriAI/litellm/pull/12507)
- [**vLLM/OpenAI-like**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Fix missing extra\_headers support for embeddings - [PR #13198](https://github.com/BerriAI/litellm/pull/13198)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**/generateContent**](https://docs.litellm.ai/docs/generateContent)
  
  - Support for query\_params in generateContent routes for API Key setting - [PR #13100](https://github.com/BerriAI/litellm/pull/13100)
  - Ensure "x-goog-api-key" is used for auth to google ai studio when using /generateContent on LiteLLM - [PR #13098](https://github.com/BerriAI/litellm/pull/13098)
  - Ensure tool calling works as expected on generateContent - [PR #13189](https://github.com/BerriAI/litellm/pull/13189)
- [**/vertex\_ai (Passthrough)**](https://docs.litellm.ai/docs/pass_through/vertex_ai)
  
  - Ensure multimodal embedding responses are logged properly - [PR #13050](https://github.com/BerriAI/litellm/pull/13050)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-1 "Direct link to Features")

- **Health Check Improvements**
  
  - Add health check endpoints for MCP servers - [PR #13106](https://github.com/BerriAI/litellm/pull/13106)
- **Guardrails Integration**
  
  - Add pre and during call hooks initialization - [PR #13067](https://github.com/BerriAI/litellm/pull/13067)
  - Move pre and during hooks to ProxyLogging - [PR #13109](https://github.com/BerriAI/litellm/pull/13109)
  - MCP pre and during guardrails implementation - [PR #13188](https://github.com/BerriAI/litellm/pull/13188)
- **Protocol & Header Support**
  
  - Add protocol headers support - [PR #13062](https://github.com/BerriAI/litellm/pull/13062)
- **URL & Namespacing**
  
  - Improve MCP server URL validation for internal/Kubernetes URLs - [PR #13099](https://github.com/BerriAI/litellm/pull/13099)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **UI**
  
  - Fix scrolling issue with MCP tools - [PR #13015](https://github.com/BerriAI/litellm/pull/13015)
  - Fix MCP client list failure - [PR #13114](https://github.com/BerriAI/litellm/pull/13114)

[Read More](https://docs.litellm.ai/docs/mcp)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Usage Analytics**
  
  - New tab for user agent activity tracking - [PR #13146](https://github.com/BerriAI/litellm/pull/13146)
  - Daily usage per user analytics - [PR #13147](https://github.com/BerriAI/litellm/pull/13147)
  - Default usage chart date range set to last 7 days - [PR #12917](https://github.com/BerriAI/litellm/pull/12917)
  - New advanced date range picker component - [PR #13141](https://github.com/BerriAI/litellm/pull/13141), [PR #13221](https://github.com/BerriAI/litellm/pull/13221)
  - Show loader on usage cost charts after date selection - [PR #13113](https://github.com/BerriAI/litellm/pull/13113)
- **Models**
  
  - Added Voyage, Jinai, Deepinfra and VolcEngine providers on UI - [PR #13131](https://github.com/BerriAI/litellm/pull/13131)
  - Added Sagemaker on UI - [PR #13117](https://github.com/BerriAI/litellm/pull/13117)
  - Preserve model order in `/v1/models` and `/model_group/info` endpoints - [PR #13178](https://github.com/BerriAI/litellm/pull/13178)
- **Key Management**
  
  - Properly parse JSON options for key generation in UI - [PR #12989](https://github.com/BerriAI/litellm/pull/12989)
- **Authentication**
  
  - **JWT Fields**
    
    - Add dot notation support for all JWT fields - [PR #13013](https://github.com/BerriAI/litellm/pull/13013)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- **Permissions**
  
  - Fix object permission for organizations - [PR #13142](https://github.com/BerriAI/litellm/pull/13142)
  - Fix list team v2 security check - [PR #13094](https://github.com/BerriAI/litellm/pull/13094)
- **Models**
  
  - Fix model reload on model update - [PR #13216](https://github.com/BerriAI/litellm/pull/13216)
- **Router Settings**
  
  - Fix displaying models for fallbacks in UI - [PR #13191](https://github.com/BerriAI/litellm/pull/13191)
  - Fix wildcard model name handling with custom values - [PR #13116](https://github.com/BerriAI/litellm/pull/13116)
  - Fix fallback delete functionality - [PR #12606](https://github.com/BerriAI/litellm/pull/12606)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-3 "Direct link to Features")

- [**MLFlow**](https://docs.litellm.ai/docs/proxy/logging#mlflow)
  
  - Allow adding tags for MLFlow logging requests - [PR #13108](https://github.com/BerriAI/litellm/pull/13108)
- [**Langfuse OTEL**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Add comprehensive metadata support to Langfuse OpenTelemetry integration - [PR #12956](https://github.com/BerriAI/litellm/pull/12956)
- [**Datadog LLM Observability**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Allow redacting message/response content for specific logging integrations - [PR #13158](https://github.com/BerriAI/litellm/pull/13158)

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- **API Key Logging**
  
  - Fix API Key being logged inappropriately - [PR #12978](https://github.com/BerriAI/litellm/pull/12978)
- **MCP Spend Tracking**
  
  - Set default value for MCP namespace tool name in spend table - [PR #12894](https://github.com/BerriAI/litellm/pull/12894)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-4 "Direct link to Features")

- **Background Health Checks**
  
  - Allow disabling background health checks for specific deployments - [PR #13186](https://github.com/BerriAI/litellm/pull/13186)
- **Database Connection Management**
  
  - Ensure stale Prisma clients disconnect DB connections properly - [PR #13140](https://github.com/BerriAI/litellm/pull/13140)
- **Jitter Improvements**
  
  - Fix jitter calculation (should be added not multiplied) - [PR #12901](https://github.com/BerriAI/litellm/pull/12901)

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- **Anthropic Streaming**
  
  - Always use choice index=0 for Anthropic streaming responses - [PR #12666](https://github.com/BerriAI/litellm/pull/12666)
- **Custom Auth**
  
  - Bubble up custom exceptions properly - [PR #13093](https://github.com/BerriAI/litellm/pull/13093)
- **OTEL with Managed Files**
  
  - Fix using managed files with OTEL integration - [PR #13171](https://github.com/BerriAI/litellm/pull/13171)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-5 "Direct link to Features")

- **Database Migration**
  
  - Move to use\_prisma\_migrate by default - [PR #13117](https://github.com/BerriAI/litellm/pull/13117)
  - Resolve team-only models on auth checks - [PR #13117](https://github.com/BerriAI/litellm/pull/13117)
- **Infrastructure**
  
  - Loosened MCP Python version restrictions - [PR #13102](https://github.com/BerriAI/litellm/pull/13102)
  - Migrate build\_and\_test to CI/CD Postgres DB - [PR #13166](https://github.com/BerriAI/litellm/pull/13166)
- **Helm Charts**
  
  - Allow Helm hooks for migration jobs - [PR #13174](https://github.com/BerriAI/litellm/pull/13174)
  - Fix Helm migration job schema updates - [PR #12809](https://github.com/BerriAI/litellm/pull/12809)

#### Bugs[​](#bugs-6 "Direct link to Bugs")

- **Docker**
  
  - Remove obsolete `version` attribute in docker-compose - [PR #13172](https://github.com/BerriAI/litellm/pull/13172)
  - Add openssl in runtime stage for non-root Dockerfile - [PR #13168](https://github.com/BerriAI/litellm/pull/13168)
- **Database Configuration**
  
  - Fix DB config through environment variables - [PR #13111](https://github.com/BerriAI/litellm/pull/13111)
- **Logging**
  
  - Suppress httpx logging - [PR #13217](https://github.com/BerriAI/litellm/pull/13217)
- **Token Counting**
  
  - Ignore unsupported keys like prefix in token counter - [PR #11954](https://github.com/BerriAI/litellm/pull/11954)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @5731la made their first contribution in [https://github.com/BerriAI/litellm/pull/12989](https://github.com/BerriAI/litellm/pull/12989)
- @restato made their first contribution in [https://github.com/BerriAI/litellm/pull/12980](https://github.com/BerriAI/litellm/pull/12980)
- @strickvl made their first contribution in [https://github.com/BerriAI/litellm/pull/12956](https://github.com/BerriAI/litellm/pull/12956)
- @Ne0-1 made their first contribution in [https://github.com/BerriAI/litellm/pull/12995](https://github.com/BerriAI/litellm/pull/12995)
- @maxrabin made their first contribution in [https://github.com/BerriAI/litellm/pull/13079](https://github.com/BerriAI/litellm/pull/13079)
- @lvuna made their first contribution in [https://github.com/BerriAI/litellm/pull/12894](https://github.com/BerriAI/litellm/pull/12894)
- @Maximgitman made their first contribution in [https://github.com/BerriAI/litellm/pull/12666](https://github.com/BerriAI/litellm/pull/12666)
- @pathikrit made their first contribution in [https://github.com/BerriAI/litellm/pull/12901](https://github.com/BerriAI/litellm/pull/12901)
- @huetterma made their first contribution in [https://github.com/BerriAI/litellm/pull/12809](https://github.com/BerriAI/litellm/pull/12809)
- @betterthanbreakfast made their first contribution in [https://github.com/BerriAI/litellm/pull/13029](https://github.com/BerriAI/litellm/pull/13029)
- @phosae made their first contribution in [https://github.com/BerriAI/litellm/pull/12606](https://github.com/BerriAI/litellm/pull/12606)
- @sahusiddharth made their first contribution in [https://github.com/BerriAI/litellm/pull/12507](https://github.com/BerriAI/litellm/pull/12507)
- @Amit-kr26 made their first contribution in [https://github.com/BerriAI/litellm/pull/11954](https://github.com/BerriAI/litellm/pull/11954)
- @kowyo made their first contribution in [https://github.com/BerriAI/litellm/pull/13172](https://github.com/BerriAI/litellm/pull/13172)
- @AnandKhinvasara made their first contribution in [https://github.com/BerriAI/litellm/pull/13187](https://github.com/BerriAI/litellm/pull/13187)
- @unique-jakub made their first contribution in [https://github.com/BerriAI/litellm/pull/13174](https://github.com/BerriAI/litellm/pull/13174)
- @tyumentsev4 made their first contribution in [https://github.com/BerriAI/litellm/pull/13134](https://github.com/BerriAI/litellm/pull/13134)
- @aayush-malviya-acquia made their first contribution in [https://github.com/BerriAI/litellm/pull/12978](https://github.com/BerriAI/litellm/pull/12978)
- @kankute-sameer made their first contribution in [https://github.com/BerriAI/litellm/pull/13225](https://github.com/BerriAI/litellm/pull/13225)
- @AlexanderYastrebov made their first contribution in [https://github.com/BerriAI/litellm/pull/13178](https://github.com/BerriAI/litellm/pull/13178)

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.74.9-stable...v1.74.15.rc)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.74.9-stable.patch.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Auto-Router** - Automatically route requests to specific models based on request content.
- **Model-level Guardrails** - Only run guardrails when specific models are used.
- **MCP Header Propagation** - Propagate headers from client to backend MCP.
- **New LLM Providers** - Added Bedrock inpainting support and Recraft API image generation / image edits support.

* * *

## Auto-Router[​](#auto-router "Direct link to Auto-Router")

This release introduces auto-routing to models based on request content. This means **Proxy Admins** can define a set of keywords that always routes to specific models when **users** opt in to using the auto-router.

This is great for internal use cases where you don't want **users** to think about which model to use - for example, use Claude models for coding vs GPT models for generating ad copy.

[Read More](https://docs.litellm.ai/docs/proxy/auto_routing)

* * *

## Model-level Guardrails[​](#model-level-guardrails "Direct link to Model-level Guardrails")

This release brings model-level guardrails support to your config.yaml + UI. This is great for cases when you have an on-prem and hosted model, and just want to run prevent sending PII to the hosted model.

```
model_list:
-model_name: claude-sonnet-4
litellm_params:
model: anthropic/claude-sonnet-4-20250514
api_key: os.environ/ANTHROPIC_API_KEY
api_base: https://api.anthropic.com/v1
guardrails:["azure-text-moderation"]# 👈 KEY CHANGE

guardrails:
-guardrail_name: azure-text-moderation
litellm_params:
guardrail: azure/text_moderations
mode:"post_call"
api_key: os.environ/AZURE_GUARDRAIL_API_KEY
api_base: os.environ/AZURE_GUARDRAIL_API_BASE 
```

[Read More](https://docs.litellm.ai/docs/proxy/guardrails/quick_start#model-level-guardrails)

* * *

v1.74.9-stable allows you to propagate MCP server specific authentication headers via LiteLLM

- Allowing users to specify which `header_name` is to be propagated to which `mcp_server` via headers
- Allows adding of different deployments of same MCP server type to use different authentication headers

[Read More](https://docs.litellm.ai/docs/mcp#new-server-specific-auth-headers-recommended)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)Fireworks AI`fireworks/models/kimi-k2-instruct`131k$0.6$2.5OpenRouter`openrouter/qwen/qwen-vl-plus`8192$0.21$0.63OpenRouter`openrouter/qwen/qwen3-coder`8192$1$5OpenRouter`openrouter/bytedance/ui-tars-1.5-7b`128k$0.10$0.20Groq`groq/qwen/qwen3-32b`131k$0.29$0.59VertexAI`vertex_ai/meta/llama-3.1-8b-instruct-maas`128k$0.00$0.00VertexAI`vertex_ai/meta/llama-3.1-405b-instruct-maas`128k$5$16VertexAI`vertex_ai/meta/llama-3.2-90b-vision-instruct-maas`128k$0.00$0.00Google AI Studio`gemini/gemini-2.0-flash-live-001`1,048,576$0.35$1.5Google AI Studio`gemini/gemini-2.5-flash-lite`1,048,576$0.1$0.4VertexAI`vertex_ai/gemini-2.0-flash-lite-001`1,048,576$0.35$1.5OpenAI`gpt-4o-realtime-preview-2025-06-03`128k$5$20

#### Features[​](#features "Direct link to Features")

- [**Lambda AI**](https://docs.litellm.ai/docs/providers/lambda_ai)
  
  - New LLM API provider - [PR #12817](https://github.com/BerriAI/litellm/pull/12817)
- [**Github Copilot**](https://docs.litellm.ai/docs/providers/github_copilot)
  
  - Dynamic endpoint support - [PR #12827](https://github.com/BerriAI/litellm/pull/12827)
- [**Morph**](https://docs.litellm.ai/docs/providers/morph)
  
  - New LLM API provider - [PR #12821](https://github.com/BerriAI/litellm/pull/12821)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Remove deprecated groq/qwen-qwq-32b - [PR #12832](https://github.com/BerriAI/litellm/pull/12831)
- [**Recraft**](https://docs.litellm.ai/docs/providers/recraft)
  
  - New image generation API - [PR #12832](https://github.com/BerriAI/litellm/pull/12832)
  - New image edits api - [PR #12874](https://github.com/BerriAI/litellm/pull/12874)
- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure/azure)
  
  - Support DefaultAzureCredential without hard-coded environment variables - [PR #12841](https://github.com/BerriAI/litellm/pull/12841)
- [**Hyperbolic**](https://docs.litellm.ai/docs/providers/hyperbolic)
  
  - New LLM API provider - [PR #12826](https://github.com/BerriAI/litellm/pull/12826)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - `/realtime` API - pass through intent query param - [PR #12838](https://github.com/BerriAI/litellm/pull/12838)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add inpainting support for Amazon Nova Canvas - [PR #12949](https://github.com/BerriAI/litellm/pull/12949) s/o @[SantoshDhaladhuli](https://github.com/SantoshDhaladhuli)

#### Bugs[​](#bugs "Direct link to Bugs")

- **Gemini ([Google AI Studio](https://docs.litellm.ai/docs/providers/gemini) + [VertexAI](https://docs.litellm.ai/docs/providers/vertex))**
  
  - Fix leaking file descriptor error on sync calls - [PR #12824](https://github.com/BerriAI/litellm/pull/12824)
- **IBM Watsonx**
  
  - use correct parameter name for tool choice - [PR #9980](https://github.com/BerriAI/litellm/pull/9980)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Only show ‘reasoning\_effort’ for supported models - [PR #12847](https://github.com/BerriAI/litellm/pull/12847)
  - Handle $id and $schema in tool call requests (Anthropic API stopped accepting them) - [PR #12959](https://github.com/BerriAI/litellm/pull/12959)
- [**Openrouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - filter out cache\_control flag for non-anthropic models (allows usage with claude code) [https://github.com/BerriAI/litellm/pull/12850](https://github.com/BerriAI/litellm/pull/12850)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Shorten Gemini tool\_call\_id for Open AI compatibility - [PR #12941](https://github.com/BerriAI/litellm/pull/12941) s/o @[tonga54](https://github.com/tonga54)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Passthrough endpoints**](https://docs.litellm.ai/docs/pass_through/)
  
  - Make key/user/team cost tracking OSS - [PR #12847](https://github.com/BerriAI/litellm/pull/12847)
- [**/v1/models**](https://docs.litellm.ai/docs/providers/passthrough)
  
  - Return fallback models as part of api response - [PR #12811](https://github.com/BerriAI/litellm/pull/12811) s/o @[murad-khafizov](https://github.com/murad-khafizov)
- [**/vector\_stores**](https://docs.litellm.ai/docs/providers/passthrough)
  
  - Make permission management OSS - [PR #12990](https://github.com/BerriAI/litellm/pull/12990)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

1. `/batches`
   
   1. Skip invalid batch during cost tracking check (prev. Would stop all checks) - [PR #12782](https://github.com/BerriAI/litellm/pull/12782)
2. `/chat/completions`
   
   1. Fix async retryer on .acompletion() - [PR #12886](https://github.com/BerriAI/litellm/pull/12886)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-2 "Direct link to Features")

- [**Permission Management**](https://docs.litellm.ai/docs/mcp#grouping-mcps-access-groups)
  
  - Make permission management by key/team OSS - [PR #12988](https://github.com/BerriAI/litellm/pull/12988)
- [**MCP Alias**](https://docs.litellm.ai/docs/mcp#mcp-aliases)
  
  - Support mcp server aliases (useful for calling long mcp server names on Cursor) - [PR #12994](https://github.com/BerriAI/litellm/pull/12994)
- **Header Propagation**
  
  - Support propagating headers from client to backend MCP (useful for sending personal access tokens to backend MCP) - [PR #13003](https://github.com/BerriAI/litellm/pull/13003)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Usage**
  
  - Support viewing usage by model group - [PR #12890](https://github.com/BerriAI/litellm/pull/12890)
- **Virtual Keys**
  
  - New `key_type` field on `/key/generate` - allows specifying if key can call LLM API vs. Management routes - [PR #12909](https://github.com/BerriAI/litellm/pull/12909)
- **Models**
  
  - Add ‘auto router’ on UI - [PR #12960](https://github.com/BerriAI/litellm/pull/12960)
  - Show global retry policy on UI - [PR #12969](https://github.com/BerriAI/litellm/pull/12969)
  - Add model-level guardrails on create + update - [PR #13006](https://github.com/BerriAI/litellm/pull/13006)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **SSO**
  
  - Fix logout when SSO is enabled - [PR #12703](https://github.com/BerriAI/litellm/pull/12703)
  - Fix reset SSO when ui\_access\_mode is updated - [PR #13011](https://github.com/BerriAI/litellm/pull/13011)
- **Guardrails**
  
  - Show correct guardrails when editing a team - [PR #12823](https://github.com/BerriAI/litellm/pull/12823)
- **Virtual Keys**
  
  - Get updated token on regenerate key - [PR #12788](https://github.com/BerriAI/litellm/pull/12788)
  - Fix CVE with key injection - [PR #12840](https://github.com/BerriAI/litellm/pull/12840)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Google Cloud Model Armor**](https://docs.litellm.ai/docs/proxy/guardrails/model_armor)
  
  - Document new guardrail - [PR #12492](https://github.com/BerriAI/litellm/pull/12492)
- [**Pillar Security**](https://docs.litellm.ai/docs/proxy/guardrails/pillar_security)
  
  - New LLM Guardrail - [PR #12791](https://github.com/BerriAI/litellm/pull/12791)
- **CloudZero**
  
  - Allow exporting spend to cloudzero - [PR #12908](https://github.com/BerriAI/litellm/pull/12908)
- **Model-level Guardrails**
  
  - Support model-level guardrails - [PR #12968](https://github.com/BerriAI/litellm/pull/12968)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Fix `[tag]=false` when tag is set for tag-based metrics - [PR #12916](https://github.com/BerriAI/litellm/pull/12916)
- [**Guardrails AI**](https://docs.litellm.ai/docs/proxy/guardrails/guardrails_ai)
  
  - Use ‘validatedOutput’ to allow usage of “fix” guards - [PR #12891](https://github.com/BerriAI/litellm/pull/12891) s/o @[DmitriyAlergant](https://github.com/DmitriyAlergant)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-5 "Direct link to Features")

- [**Auto-Router**](https://docs.litellm.ai/docs/proxy/auto_routing)
  
  - New auto-router powered by `semantic-router` - [PR #12955](https://github.com/BerriAI/litellm/pull/12955)

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- **forward\_clientside\_headers**
  
  - Filter out `content-length` from headers (caused backend requests to hang) - [PR #12886](https://github.com/BerriAI/litellm/pull/12886/files)
- **Message Redaction**
  
  - Fix cannot pickle coroutine object error - [PR #13005](https://github.com/BerriAI/litellm/pull/13005)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-6 "Direct link to Features")

- **Benchmarks**
  
  - Updated litellm proxy benchmarks (p50, p90, p99 overhead) - [PR #12842](https://github.com/BerriAI/litellm/pull/12842)
- **Request Headers**
  
  - Added new `x-litellm-num-retries` request header
- **Swagger**
  
  - Support local swagger on custom root paths - [PR #12911](https://github.com/BerriAI/litellm/pull/12911)
- **Health**
  
  - Track cost + add tags for health checks done by LiteLLM Proxy - [PR #12880](https://github.com/BerriAI/litellm/pull/12880)

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- **Proxy Startup**
  
  - Fixes issue on startup where team member budget is None would block startup - [PR #12843](https://github.com/BerriAI/litellm/pull/12843)
- **Docker**
  
  - Move non-root docker to chain guard image (fewer vulnerabilities) - [PR #12707](https://github.com/BerriAI/litellm/pull/12707)
  - add azure-keyvault==4.2.0 to Docker img - [PR #12873](https://github.com/BerriAI/litellm/pull/12873)
- **Separate Health App**
  
  - Pass through cmd args via supervisord (enables user config to still work via docker) - [PR #12871](https://github.com/BerriAI/litellm/pull/12871)
- **Swagger**
  
  - Bump DOMPurify version (fixes vulnerability) - [PR #12911](https://github.com/BerriAI/litellm/pull/12911)
  - Add back local swagger bundle (enables swagger to work in air gapped env.) - [PR #12911](https://github.com/BerriAI/litellm/pull/12911)
- **Request Headers**
  
  - Make ‘user\_header\_name’ field check case insensitive (fixes customer budget enforcement for OpenWebUi) - [PR #12950](https://github.com/BerriAI/litellm/pull/12950)
- **SpendLogs**
  
  - Fix issues writing to DB when custom\_llm\_provider is None - [PR #13001](https://github.com/BerriAI/litellm/pull/13001)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @magicalne made their first contribution in [https://github.com/BerriAI/litellm/pull/12804](https://github.com/BerriAI/litellm/pull/12804)
- @pavangudiwada made their first contribution in [https://github.com/BerriAI/litellm/pull/12798](https://github.com/BerriAI/litellm/pull/12798)
- @mdiloreto made their first contribution in [https://github.com/BerriAI/litellm/pull/12707](https://github.com/BerriAI/litellm/pull/12707)
- @murad-khafizov made their first contribution in [https://github.com/BerriAI/litellm/pull/12811](https://github.com/BerriAI/litellm/pull/12811)
- @eagle-p made their first contribution in [https://github.com/BerriAI/litellm/pull/12791](https://github.com/BerriAI/litellm/pull/12791)
- @apoorv-sharma made their first contribution in [https://github.com/BerriAI/litellm/pull/12920](https://github.com/BerriAI/litellm/pull/12920)
- @SantoshDhaladhuli made their first contribution in [https://github.com/BerriAI/litellm/pull/12949](https://github.com/BerriAI/litellm/pull/12949)
- @tonga54 made their first contribution in [https://github.com/BerriAI/litellm/pull/12941](https://github.com/BerriAI/litellm/pull/12941)
- @sings-to-bees-on-wednesdays made their first contribution in [https://github.com/BerriAI/litellm/pull/12950](https://github.com/BerriAI/litellm/pull/12950)

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.74.7-stable...v1.74.9.rc-draft)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.74.7-stable.patch.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Vector Stores** - Support for Vertex RAG Engine, PG Vector, OpenAI & Azure OpenAI Vector Stores.
- **Bulk Editing Users** - Bulk editing users on the UI.
- **Health Check Improvements** - Prevent unnecessary pod restarts during high traffic.
- **New LLM Providers** - Added Moonshot AI and Vercel v0 provider support.

* * *

## Vector Stores API[​](#vector-stores-api "Direct link to Vector Stores API")

This release introduces support for using VertexAI RAG Engine, PG Vector, Bedrock Knowledge Bases, and OpenAI Vector Stores with LiteLLM.

This is ideal for use cases requiring external knowledge sources with LLMs.

This brings the following benefits for LiteLLM users:

**Proxy Admin Benefits:**

- Fine-grained access control: determine which Keys and Teams can access specific Vector Stores
- Complete usage tracking and monitoring across all vector store operations

**Developer Benefits:**

- Simple, unified interface for querying vector stores and using them with LLM API requests
- Consistent API experience across all supported vector store providers

[Get started](https://docs.litellm.ai/docs/completion/knowledgebase)

* * *

## Bulk Editing Users[​](#bulk-editing-users "Direct link to Bulk Editing Users")

v1.74.7-stable introduces Bulk Editing Users on the UI. This is useful for:

- granting all existing users to a default team (useful for controlling access / tracking spend by team)
- controlling personal model access for existing users

[Read more](https://docs.litellm.ai/docs/proxy/ui/bulk_edit_users)

* * *

## Health Check Server[​](#health-check-server "Direct link to Health Check Server")

This release brings reliability improvements that prevent unnecessary pod restarts during high traffic. Previously, when the main LiteLLM app was busy serving traffic, health endpoints would timeout even when pods were healthy.

Starting with this release, you can run health endpoints on an isolated process with a dedicated port. This ensures liveness and readiness probes remain responsive even when the main LiteLLM app is under heavy load.

[Read More](https://docs.litellm.ai/docs/proxy/prod#10-use-a-separate-health-check-app)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)Azure AI`azure_ai/grok-3`131k$3.30$16.50Azure AI`azure_ai/global/grok-3`131k$3.00$15.00Azure AI`azure_ai/global/grok-3-mini`131k$0.25$1.27Azure AI`azure_ai/grok-3-mini`131k$0.275$1.38Azure AI`azure_ai/jais-30b-chat`8k$3200$9710Groq`groq/moonshotai-kimi-k2-instruct`131k$1.00$3.00AI21`jamba-large-1.7`256k$2.00$8.00AI21`jamba-mini-1.7`256k$0.20$0.40Together.ai`together_ai/moonshotai/Kimi-K2-Instruct`131k$1.00$3.00v0`v0/v0-1.0-md`128k$3.00$15.00v0`v0/v0-1.5-md`128k$3.00$15.00v0`v0/v0-1.5-lg`512k$15.00$75.00Moonshot`moonshot/moonshot-v1-8k`8k$0.20$2.00Moonshot`moonshot/moonshot-v1-32k`32k$1.00$3.00Moonshot`moonshot/moonshot-v1-128k`131k$2.00$5.00Moonshot`moonshot/moonshot-v1-auto`131k$2.00$5.00Moonshot`moonshot/kimi-k2-0711-preview`131k$0.60$2.50Moonshot`moonshot/moonshot-v1-32k-0430`32k$1.00$3.00Moonshot`moonshot/moonshot-v1-128k-0430`131k$2.00$5.00Moonshot`moonshot/moonshot-v1-8k-0430`8k$0.20$2.00Moonshot`moonshot/kimi-latest`131k$2.00$5.00Moonshot`moonshot/kimi-latest-8k`8k$0.20$2.00Moonshot`moonshot/kimi-latest-32k`32k$1.00$3.00Moonshot`moonshot/kimi-latest-128k`131k$2.00$5.00Moonshot`moonshot/kimi-thinking-preview`131k$30.00$30.00Moonshot`moonshot/moonshot-v1-8k-vision-preview`8k$0.20$2.00Moonshot`moonshot/moonshot-v1-32k-vision-preview`32k$1.00$3.00Moonshot`moonshot/moonshot-v1-128k-vision-preview`131k$2.00$5.00

#### Features[​](#features "Direct link to Features")

- [**🆕 Moonshot API (Kimi)**](https://docs.litellm.ai/docs/providers/moonshot)
  
  - New LLM API integration for accessing Kimi models - [PR #12592](https://github.com/BerriAI/litellm/pull/12592), [Get Started](https://docs.litellm.ai/docs/providers/moonshot)
- [**🆕 v0 Provider**](https://docs.litellm.ai/docs/providers/v0)
  
  - New provider integration for v0.dev - [PR #12751](https://github.com/BerriAI/litellm/pull/12751), [Get Started](https://docs.litellm.ai/docs/providers/v0)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Use OpenAI DeepResearch models with `litellm.completion` (`/chat/completions`) - [PR #12627](https://github.com/BerriAI/litellm/pull/12627) **DOC NEEDED**
- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure_openai)
  
  - Use Azure OpenAI DeepResearch models with `litellm.completion` (`/chat/completions`) - [PR #12627](https://github.com/BerriAI/litellm/pull/12627) **DOC NEEDED**
  - Added `response_format` support for openai gpt-4.1 models - [PR #12745](https://github.com/BerriAI/litellm/pull/12745)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Tool cache control support - [PR #12668](https://github.com/BerriAI/litellm/pull/12668)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Claude 4 /invoke route support - [PR #12599](https://github.com/BerriAI/litellm/pull/12599), [Get Started](https://docs.litellm.ai/docs/providers/bedrock)
  - Application inference profile tool choice support - [PR #12599](https://github.com/BerriAI/litellm/pull/12599)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Custom TTL support for context caching - [PR #12541](https://github.com/BerriAI/litellm/pull/12541)
  - Fix implicit caching cost calculation for Gemini 2.x models - [PR #12585](https://github.com/BerriAI/litellm/pull/12585)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Added Vertex AI RAG Engine support (use with OpenAI compatible `/vector_stores` API) - [PR #12752](https://github.com/BerriAI/litellm/pull/12595), [Get Started](https://docs.litellm.ai/docs/completion/knowledgebase)
- [**vLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Added support for using Rerank endpoints with vLLM - [PR #12738](https://github.com/BerriAI/litellm/pull/12738), [Get Started](https://docs.litellm.ai/docs/providers/vllm#rerank)
- [**AI21**](https://docs.litellm.ai/docs/providers/ai21)
  
  - Added ai21/jamba-1.7 model family pricing - [PR #12593](https://github.com/BerriAI/litellm/pull/12593), [Get Started](https://docs.litellm.ai/docs/providers/ai21)
- [**Together.ai**](https://docs.litellm.ai/docs/providers/together_ai)
  
  - \[New Model] add together\_ai/moonshotai/Kimi-K2-Instruct - [PR #12645](https://github.com/BerriAI/litellm/pull/12645), [Get Started](https://docs.litellm.ai/docs/providers/together_ai)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Add groq/moonshotai-kimi-k2-instruct model configuration - [PR #12648](https://github.com/BerriAI/litellm/pull/12648), [Get Started](https://docs.litellm.ai/docs/providers/groq)
- [**Github Copilot**](https://docs.litellm.ai/docs/providers/github_copilot)
  
  - Change System prompts to assistant prompts for GH Copilot - [PR #12742](https://github.com/BerriAI/litellm/pull/12742), [Get Started](https://docs.litellm.ai/docs/providers/github_copilot)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Fix streaming + response\_format + tools bug - [PR #12463](https://github.com/BerriAI/litellm/pull/12463)
- [**XAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - grok-4 does not support the `stop` param - [PR #12646](https://github.com/BerriAI/litellm/pull/12646)
- [**AWS**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Role chaining with web authentication for AWS Bedrock - [PR #12607](https://github.com/BerriAI/litellm/pull/12607)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add project\_id to cached credentials - [PR #12661](https://github.com/BerriAI/litellm/pull/12661)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fix bedrock nova micro and nova lite context window info in [PR #12619](https://github.com/BerriAI/litellm/pull/12619)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/chat/completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Include tool calls in output of trim\_messages - [PR #11517](https://github.com/BerriAI/litellm/pull/11517)
- [**/v1/vector\_stores**](https://docs.litellm.ai/docs/vector_stores/search)
  
  - New OpenAI-compatible vector store endpoints - [PR #12699](https://github.com/BerriAI/litellm/pull/12699), [Get Started](https://docs.litellm.ai/docs/vector_stores/search)
  - Vector store search endpoint - [PR #12749](https://github.com/BerriAI/litellm/pull/12749), [Get Started](https://docs.litellm.ai/docs/vector_stores/search)
  - Support for using PG Vector as a vector store - [PR #12667](https://github.com/BerriAI/litellm/pull/12667), [Get Started](https://docs.litellm.ai/docs/completion/knowledgebase)
- [**/streamGenerateContent**](https://docs.litellm.ai/docs/generateContent)
  
  - Non-gemini model support - [PR #12647](https://github.com/BerriAI/litellm/pull/12647)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**/vector\_stores**](https://docs.litellm.ai/docs/vector_stores/search)
  
  - Knowledge Base Call returning error when passing as `tools` - [PR #12628](https://github.com/BerriAI/litellm/pull/12628)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-2 "Direct link to Features")

- [**Access Groups**](https://docs.litellm.ai/docs/mcp#grouping-mcps-access-groups)
  
  - Allow MCP access groups to be added via litellm proxy config.yaml - [PR #12654](https://github.com/BerriAI/litellm/pull/12654)
  - List tools from access list for keys - [PR #12657](https://github.com/BerriAI/litellm/pull/12657)
- [**Namespacing**](https://docs.litellm.ai/docs/mcp#mcp-namespacing)
  
  - URL-based namespacing for better segregation - [PR #12658](https://github.com/BerriAI/litellm/pull/12658)
  - Make MCP\_TOOL\_PREFIX\_SEPARATOR configurable from env - [PR #12603](https://github.com/BerriAI/litellm/pull/12603)
- [**Gateway Features**](https://docs.litellm.ai/docs/mcp#mcp-gateway-features)
  
  - Allow using MCPs with all LLM APIs (VertexAI, Gemini, Groq, etc.) when using /responses - [PR #12546](https://github.com/BerriAI/litellm/pull/12546)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- Fix to update object permission on update/delete key/team - [PR #12701](https://github.com/BerriAI/litellm/pull/12701)
- Include /mcp in list of available routes on proxy - [PR #12612](https://github.com/BerriAI/litellm/pull/12612)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Keys**
  
  - Regenerate Key State Management improvements - [PR #12729](https://github.com/BerriAI/litellm/pull/12729)
- **Models**
  
  - Wildcard model filter support - [PR #12597](https://github.com/BerriAI/litellm/pull/12597)
  - Fixes for handling team only models on UI - [PR #12632](https://github.com/BerriAI/litellm/pull/12632)
- **Usage Page**
  
  - Fix Y-axis labels overlap on Spend per Tag chart - [PR #12754](https://github.com/BerriAI/litellm/pull/12754)
- **Teams**
  
  - Allow setting custom key duration + show key creation stats - [PR #12722](https://github.com/BerriAI/litellm/pull/12722)
  - Enable team admins to update member roles - [PR #12629](https://github.com/BerriAI/litellm/pull/12629)
- **Users**
  
  - New `/user/bulk_update` endpoint - [PR #12720](https://github.com/BerriAI/litellm/pull/12720)
- **Logs Page**
  
  - Add `end_user` filter on UI Logs Page - [PR #12663](https://github.com/BerriAI/litellm/pull/12663)
- **MCP Servers**
  
  - Copy MCP Server name functionality - [PR #12760](https://github.com/BerriAI/litellm/pull/12760)
- **Vector Stores**
  
  - UI support for clicking into Vector Stores - [PR #12741](https://github.com/BerriAI/litellm/pull/12741)
  - Allow adding Vertex RAG Engine, OpenAI, Azure through UI - [PR #12752](https://github.com/BerriAI/litellm/pull/12752)
- **General**
  
  - Add Copy-on-Click for all IDs (Key, Team, Organization, MCP Server) - [PR #12615](https://github.com/BerriAI/litellm/pull/12615)
- [**SCIM**](https://docs.litellm.ai/docs/proxy/scim)
  
  - Add GET /ServiceProviderConfig endpoint - [PR #12664](https://github.com/BerriAI/litellm/pull/12664)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- **Teams**
  
  - Ensure user id correctly added when creating new teams - [PR #12719](https://github.com/BerriAI/litellm/pull/12719)
  - Fixes for handling team-only models on UI - [PR #12632](https://github.com/BerriAI/litellm/pull/12632)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Google Cloud Model Armor**](https://docs.litellm.ai/docs/proxy/guardrails/google_cloud_model_armor)
  
  - New guardrails integration - [PR #12492](https://github.com/BerriAI/litellm/pull/12492)
- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/bedrock)
  
  - Allow disabling exception on 'BLOCKED' action - [PR #12693](https://github.com/BerriAI/litellm/pull/12693)
- [**Guardrails AI**](https://docs.litellm.ai/docs/proxy/guardrails/guardrails_ai)
  
  - Support `llmOutput` based guardrails as pre-call hooks - [PR #12674](https://github.com/BerriAI/litellm/pull/12674)
- [**DataDog LLM Observability**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Add support for tracking the correct span type based on LLM Endpoint used - [PR #12652](https://github.com/BerriAI/litellm/pull/12652)
- [**Custom Logging**](https://docs.litellm.ai/docs/proxy/logging)
  
  - Allow reading custom logger python scripts from S3 or GCS Bucket - [PR #12623](https://github.com/BerriAI/litellm/pull/12623)

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- [**General Logging**](https://docs.litellm.ai/docs/proxy/logging)
  
  - StandardLoggingPayload on cache\_hits should track custom llm provider - [PR #12652](https://github.com/BerriAI/litellm/pull/12652)
- [**S3 Buckets**](https://docs.litellm.ai/docs/proxy/logging#s3-buckets)
  
  - S3 v2 log uploader crashes when using with guardrails - [PR #12733](https://github.com/BerriAI/litellm/pull/12733)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-5 "Direct link to Features")

- **Health Checks**
  
  - Separate health app for liveness probes - [PR #12669](https://github.com/BerriAI/litellm/pull/12669)
  - Health check app on separate port - [PR #12718](https://github.com/BerriAI/litellm/pull/12718)
- **Caching**
  
  - Add Azure Blob cache support - [PR #12587](https://github.com/BerriAI/litellm/pull/12587)
- **Router**
  
  - Handle ZeroDivisionError with zero completion tokens in lowest\_latency strategy - [PR #12734](https://github.com/BerriAI/litellm/pull/12734)

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- **Database**
  
  - Use upsert for managed object table to avoid UniqueViolationError - [PR #11795](https://github.com/BerriAI/litellm/pull/11795)
  - Refactor to support use\_prisma\_migrate for helm hook - [PR #12600](https://github.com/BerriAI/litellm/pull/12600)
- **Cache**
  
  - Fix: redis caching for embedding response models - [PR #12750](https://github.com/BerriAI/litellm/pull/12750)

* * *

## Helm Chart[​](#helm-chart "Direct link to Helm Chart")

- DB Migration Hook: refactor to support use\_prisma\_migrate - for helm hook [PR](https://github.com/BerriAI/litellm/pull/12600)
- Add envVars and extraEnvVars support to Helm migrations job - [PR #12591](https://github.com/BerriAI/litellm/pull/12591)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-6 "Direct link to Features")

- **Control Plane + Data Plane Architecture**
  
  - Control Plane + Data Plane support - [PR #12601](https://github.com/BerriAI/litellm/pull/12601)
- **Proxy CLI**
  
  - Add "keys import" command to CLI - [PR #12620](https://github.com/BerriAI/litellm/pull/12620)
- **Swagger Documentation**
  
  - Add swagger docs for LiteLLM /chat/completions, /embeddings, /responses - [PR #12618](https://github.com/BerriAI/litellm/pull/12618)
- **Dependencies**
  
  - Loosen rich version from ==13.7.1 to &gt;=13.7.1 - [PR #12704](https://github.com/BerriAI/litellm/pull/12704)

#### Bugs[​](#bugs-6 "Direct link to Bugs")

- Verbose log is enabled by default fix - [PR #12596](https://github.com/BerriAI/litellm/pull/12596)
- Add support for disabling callbacks in request body - [PR #12762](https://github.com/BerriAI/litellm/pull/12762)
- Handle circular references in spend tracking metadata JSON serialization - [PR #12643](https://github.com/BerriAI/litellm/pull/12643)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @AntonioKL made their first contribution in [https://github.com/BerriAI/litellm/pull/12591](https://github.com/BerriAI/litellm/pull/12591)
- @marcelodiaz558 made their first contribution in [https://github.com/BerriAI/litellm/pull/12541](https://github.com/BerriAI/litellm/pull/12541)
- @dmcaulay made their first contribution in [https://github.com/BerriAI/litellm/pull/12463](https://github.com/BerriAI/litellm/pull/12463)
- @demoray made their first contribution in [https://github.com/BerriAI/litellm/pull/12587](https://github.com/BerriAI/litellm/pull/12587)
- @staeiou made their first contribution in [https://github.com/BerriAI/litellm/pull/12631](https://github.com/BerriAI/litellm/pull/12631)
- @stefanc-ai2 made their first contribution in [https://github.com/BerriAI/litellm/pull/12622](https://github.com/BerriAI/litellm/pull/12622)
- @RichardoC made their first contribution in [https://github.com/BerriAI/litellm/pull/12607](https://github.com/BerriAI/litellm/pull/12607)
- @yeahyung made their first contribution in [https://github.com/BerriAI/litellm/pull/11795](https://github.com/BerriAI/litellm/pull/11795)
- @mnguyen96 made their first contribution in [https://github.com/BerriAI/litellm/pull/12619](https://github.com/BerriAI/litellm/pull/12619)
- @rgambee made their first contribution in [https://github.com/BerriAI/litellm/pull/11517](https://github.com/BerriAI/litellm/pull/11517)
- @jvanmelckebeke made their first contribution in [https://github.com/BerriAI/litellm/pull/12725](https://github.com/BerriAI/litellm/pull/12725)
- @jlaurendi made their first contribution in [https://github.com/BerriAI/litellm/pull/12704](https://github.com/BerriAI/litellm/pull/12704)
- @doublerr made their first contribution in [https://github.com/BerriAI/litellm/pull/12661](https://github.com/BerriAI/litellm/pull/12661)

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.74.3-stable...v1.74.7-stable)[​](#full-changelog "Direct link to full-changelog")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.74.3-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **MCP: Model Access Groups** - Add mcp servers to access groups, for easily managing access to users and teams.
- **MCP: Tool Cost Tracking** - Set prices for each MCP tool.
- **Model Hub v2** - New OSS Model Hub for telling developers what models are available on the proxy.
- **Bytez** - New LLM API Provider.
- **Dashscope API** - Call Alibaba's qwen models via new Dashscope API Provider.

* * *

## MCP Gateway: Model Access Groups[​](#mcp-gateway-model-access-groups "Direct link to MCP Gateway: Model Access Groups")

v1.74.3-stable adds support for adding MCP servers to access groups, this makes it **easier for Proxy Admins** to manage access to MCP servers across users and teams.

For **developers**, this means you can now connect to multiple MCP servers by passing the access group name in the `x-mcp-servers` header.

Read more [here](https://docs.litellm.ai/docs/mcp#grouping-mcps-access-groups)

* * *

This release adds cost tracking for MCP tool calls. This is great for **Proxy Admins** giving MCP access to developers as you can now attribute MCP tool call costs to specific LiteLLM keys and teams.

You can set:

- **Uniform server cost**: Set a uniform cost for all tools from a server
- **Individual tool cost**: Define individual costs for specific tools (e.g., search\_tool costs $10, get\_weather costs $5).
- **Dynamic costs**: For use cases where you want to set costs based on the MCP's response, you can write a custom post mcp call hook to parse responses and set costs dynamically.

[Get started](https://docs.litellm.ai/docs/mcp#mcp-cost-tracking)

* * *

## Model Hub v2[​](#model-hub-v2 "Direct link to Model Hub v2")

v1.74.3-stable introduces a new OSS Model Hub for telling developers what models are available on the proxy.

This is great for **Proxy Admins** as you can now tell developers what models are available on the proxy.

This improves on the previous model hub by enabling:

- The ability to show **Developers** models, even if they don't have a LiteLLM key.
- The ability for **Proxy Admins** to select specific models to be public on the model hub.
- Improved search and filtering capabilities:
  
  - search for models by partial name (e.g. `xai grok-4`)
  - filter by provider and feature (e.g. 'vision' models)
  - sort by cost (e.g. cheapest vision model from OpenAI)

[Get started](https://docs.litellm.ai/docs/proxy/model_hub)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)TypeXai`xai/grok-4`256k$3.00$15.00NewXai`xai/grok-4-0709`256k$3.00$15.00NewXai`xai/grok-4-latest`256k$3.00$15.00NewMistral`mistral/devstral-small-2507`128k$0.1$0.3NewMistral`mistral/devstral-medium-2507`128k$0.4$2NewAzure OpenAI`azure/o3-deep-research`200k$10$40New

#### Features[​](#features "Direct link to Features")

- [**Xinference**](https://docs.litellm.ai/docs/providers/xinference)
  
  - Image generation API support - [PR](https://github.com/BerriAI/litellm/pull/12439)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - API Key Auth support for AWS Bedrock API - [PR](https://github.com/BerriAI/litellm/pull/12495)
- [**🆕 Dashscope**](https://docs.litellm.ai/docs/providers/dashscope)
  
  - New integration from Alibaba (enables qwen usage) - [PR](https://github.com/BerriAI/litellm/pull/12361)
- [**🆕 Bytez**](https://docs.litellm.ai/docs/providers/bytez)
  
  - New /chat/completion integration - [PR](https://github.com/BerriAI/litellm/pull/12121)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Github Copilot**](https://docs.litellm.ai/docs/providers/github_copilot)
  
  - Fix API base url for Github Copilot - [PR](https://github.com/BerriAI/litellm/pull/12418)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Ensure supported bedrock/converse/ params = bedrock/ params - [PR](https://github.com/BerriAI/litellm/pull/12466)
  - Fix cache token cost calculation - [PR](https://github.com/BerriAI/litellm/pull/12488)
- [**XAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - ensure finish\_reason includes tool calls when xai responses with tool calls - [PR](https://github.com/BerriAI/litellm/pull/12545)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/completions**](https://docs.litellm.ai/docs/text_completion)
  
  - Return ‘reasoning\_content’ on streaming - [PR](https://github.com/BerriAI/litellm/pull/12377)
- [**/chat/completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Add 'thinking blocks' to stream chunk builder - [PR](https://github.com/BerriAI/litellm/pull/12395)
- [**/v1/messages**](https://docs.litellm.ai/docs/anthropic_unified)
  
  - Fallbacks support - [PR](https://github.com/BerriAI/litellm/pull/12440)
  - tool call handling for non-anthropic models (/v1/messages to /chat/completion bridge) - [PR](https://github.com/BerriAI/litellm/pull/12473)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-2 "Direct link to Features")

- [**Cost Tracking**](https://docs.litellm.ai/docs/mcp#-mcp-cost-tracking)
  
  - Add Cost Tracking - [PR](https://github.com/BerriAI/litellm/pull/12385)
  - Add usage tracking - [PR](https://github.com/BerriAI/litellm/pull/12397)
  - Add custom cost configuration for each MCP tool - [PR](https://github.com/BerriAI/litellm/pull/12499)
  - Add support for editing MCP cost per tool - [PR](https://github.com/BerriAI/litellm/pull/12501)
  - Allow using custom post call MCP hook for cost tracking - [PR](https://github.com/BerriAI/litellm/pull/12469)
- [**Auth**](https://docs.litellm.ai/docs/mcp#using-your-mcp-with-client-side-credentials)
  
  - Allow customizing what client side auth header to use - [PR](https://github.com/BerriAI/litellm/pull/12460)
  - Raises error when MCP server header is malformed in the request - [PR](https://github.com/BerriAI/litellm/pull/12494)
- [**MCP Server**](https://docs.litellm.ai/docs/mcp#adding-your-mcp)
  
  - Allow using stdio MCPs with LiteLLM (enables using Circle CI MCP w/ LiteLLM) - [PR](https://github.com/BerriAI/litellm/pull/12530), [Get Started](https://docs.litellm.ai/docs/mcp#adding-a-stdio-mcp-server)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **General**
  
  - Fix task group is not initialized error - [PR](https://github.com/BerriAI/litellm/pull/12411) s/o [@juancarlosm](https://github.com/juancarlosm)
- [**MCP Server**](https://docs.litellm.ai/docs/mcp#adding-your-mcp)
  
  - Fix mcp tool separator to work with Claude code - [PR](https://github.com/BerriAI/litellm/pull/12430), [Get Started](https://docs.litellm.ai/docs/mcp#adding-your-mcp)
  - Add validation to mcp server name to not allow "-" (enables namespaces to work) - [PR](https://github.com/BerriAI/litellm/pull/12515)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Model Hub**
  
  - new model hub table view - [PR](https://github.com/BerriAI/litellm/pull/12468)
  - new /public/model\_hub endpoint - [PR](https://github.com/BerriAI/litellm/pull/12468)
  - Make Model Hub OSS - [PR](https://github.com/BerriAI/litellm/pull/12553)
  - New ‘make public’ modal flow for showing proxy models on public model hub - [PR](https://github.com/BerriAI/litellm/pull/12555)
- **MCP**
  
  - support for internal users to use and manage MCP servers - [PR](https://github.com/BerriAI/litellm/pull/12458)
  - Adds UI support to add MCP access groups (similar to namespaces) - [PR](https://github.com/BerriAI/litellm/pull/12470)
  - MCP Tool Testing Playground - [PR](https://github.com/BerriAI/litellm/pull/12520)
  - Show cost config on root of MCP settings - [PR](https://github.com/BerriAI/litellm/pull/12526)
- **Test Key**
  
  - Stick sessions - [PR](https://github.com/BerriAI/litellm/pull/12365)
  - MCP Access Groups - allow mcp access groups - [PR](https://github.com/BerriAI/litellm/pull/12529)
- **Usage**
  
  - Truncate long labels and improve tooltip in Top API Keys chart - [PR](https://github.com/BerriAI/litellm/pull/12371)
  - Improve Chart Readability for Tag Usage - [PR](https://github.com/BerriAI/litellm/pull/12378)
- **Teams**
  
  - Prevent navigation reset after team member operations - [PR](https://github.com/BerriAI/litellm/pull/12424)
  - Team Members - reset budget, if duration set - [PR](https://github.com/BerriAI/litellm/pull/12534)
  - Use central team member budget when max\_budget\_in\_team set on UI - [PR](https://github.com/BerriAI/litellm/pull/12533)
- **SSO**
  
  - Allow users to run a custom sso login handler - [PR](https://github.com/BerriAI/litellm/pull/12465)
- **Navbar**
  
  - improve user dropdown UI with premium badge and cleaner layout - [PR](https://github.com/BerriAI/litellm/pull/12502)
- **General**
  
  - Consistent layout for Create and Back buttons on all the pages - [PR](https://github.com/BerriAI/litellm/pull/12542)
  - Align Show Password with Checkbox - [PR](https://github.com/BerriAI/litellm/pull/12538)
  - Prevent writing default user setting updates to yaml (causes error in non-root env) - [PR](https://github.com/BerriAI/litellm/pull/12533)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **Model Hub**
  
  - fix duplicates in /model\_group/info - [PR](https://github.com/BerriAI/litellm/pull/12468)
- **MCP**
  
  - Fix UI not syncing MCP access groups properly with object permissions - [PR](https://github.com/BerriAI/litellm/pull/12523)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Langfuse**](https://docs.litellm.ai/docs/observability/langfuse_integration)
  
  - Version bump - [PR](https://github.com/BerriAI/litellm/pull/12376)
  - LANGFUSE\_TRACING\_ENVIRONMENT support - [PR](https://github.com/BerriAI/litellm/pull/12376)
- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/bedrock)
  
  - Raise Bedrock output text on 'BLOCKED' actions from guardrail - [PR](https://github.com/BerriAI/litellm/pull/12435)
- [**OTEL**](https://docs.litellm.ai/docs/observability/opentelemetry_integration)
  
  - `OTEL_RESOURCE_ATTRIBUTES` support - [PR](https://github.com/BerriAI/litellm/pull/12468)
- [**Guardrails AI**](https://docs.litellm.ai/docs/proxy/guardrails/guardrails_ai)
  
  - pre-call + logging only guardrail (pii detection/competitor names) support - [PR](https://github.com/BerriAI/litellm/pull/12506)
- [**Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)
  
  - \[Enterprise] Support tag based mode for guardrails - [PR](https://github.com/BerriAI/litellm/pull/12508), [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/quick_start#-tag-based-guardrail-modes)
- [**OpenAI Moderations API**](https://docs.litellm.ai/docs/proxy/guardrails/openai_moderation)
  
  - New guardrail integration - [PR](https://github.com/BerriAI/litellm/pull/12519)
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - support tag based metrics (enables prometheus metrics for measuring roo-code/cline/claude code engagement) - [PR](https://github.com/BerriAI/litellm/pull/12534), [Get Started](https://docs.litellm.ai/docs/proxy/prometheus#custom-tags)
- [**Datadog LLM Observability**](https://docs.litellm.ai/docs/observability/datadog)
  
  - Added `total_cost` field to track costs in DataDog LLM observability metrics - [PR](https://github.com/BerriAI/litellm/pull/12467)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Remove experimental `_by_tag` metrics (fixes cardinality issue) - [PR](https://github.com/BerriAI/litellm/pull/12395)
- [**Slack Alerting**](https://docs.litellm.ai/docs/proxy/alerting)
  
  - Fix slack alerting for outage and region outage alerts - [PR](https://github.com/BerriAI/litellm/pull/12464), [Get Started](https://docs.litellm.ai/docs/proxy/alerting#region-outage-alerting--enterprise-feature)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- [**Responses API Bridge**](https://docs.litellm.ai/docs/response_api#calling-non-responses-api-endpoints-responses-to-chatcompletions-bridge)
  
  - add image support for Responses API when falling back on Chat Completions - [PR](https://github.com/BerriAI/litellm/pull/12204) s/o [@ryan-castner](https://github.com/ryan-castner)
- **aiohttp**
  
  - Properly close aiohttp client sessions to prevent resource leaks - [PR](https://github.com/BerriAI/litellm/pull/12251)
- **Router**
  
  - don't add invalid deployment to router pattern match - [PR](https://github.com/BerriAI/litellm/pull/12459)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- **S3**
  
  - s3 config.yaml file - ensure yaml safe load is used - [PR](https://github.com/BerriAI/litellm/pull/12373)
- **Audit Logs**
  
  - Add audit logs for model updates - [PR](https://github.com/BerriAI/litellm/pull/12396)
- **Startup**
  
  - Multiple API Keys Created on Startup when max\_budget is enabled - [PR](https://github.com/BerriAI/litellm/pull/12436)
- **Auth**
  
  - Resolve model group alias on Auth (if user has access to underlying model, allow alias request to work) - [PR](https://github.com/BerriAI/litellm/pull/12440)
- **config.yaml**
  
  - fix parsing environment\_variables from config.yaml - [PR](https://github.com/BerriAI/litellm/pull/12482)
- **Security**
  
  - Log hashed jwt w/ prefix instead of actual value - [PR](https://github.com/BerriAI/litellm/pull/12524)

#### Features[​](#features-5 "Direct link to Features")

- **MCP**
  
  - Bump mcp version on docker img - [PR](https://github.com/BerriAI/litellm/pull/12362)
- **Request Headers**
  
  - Forward ‘anthropic-beta’ header when forward\_client\_headers\_to\_llm\_api is true - [PR](https://github.com/BerriAI/litellm/pull/12462)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @kanaka made their first contribution in [https://github.com/BerriAI/litellm/pull/12418](https://github.com/BerriAI/litellm/pull/12418)
- @juancarlosm made their first contribution in [https://github.com/BerriAI/litellm/pull/12411](https://github.com/BerriAI/litellm/pull/12411)
- @DmitriyAlergant made their first contribution in [https://github.com/BerriAI/litellm/pull/12356](https://github.com/BerriAI/litellm/pull/12356)
- @Rayshard made their first contribution in [https://github.com/BerriAI/litellm/pull/12487](https://github.com/BerriAI/litellm/pull/12487)
- @minghao51 made their first contribution in [https://github.com/BerriAI/litellm/pull/12361](https://github.com/BerriAI/litellm/pull/12361)
- @jdietzsch91 made their first contribution in [https://github.com/BerriAI/litellm/pull/12488](https://github.com/BerriAI/litellm/pull/12488)
- @iwinux made their first contribution in [https://github.com/BerriAI/litellm/pull/12473](https://github.com/BerriAI/litellm/pull/12473)
- @andresC98 made their first contribution in [https://github.com/BerriAI/litellm/pull/12413](https://github.com/BerriAI/litellm/pull/12413)
- @EmaSuriano made their first contribution in [https://github.com/BerriAI/litellm/pull/12509](https://github.com/BerriAI/litellm/pull/12509)
- @strawgate made their first contribution in [https://github.com/BerriAI/litellm/pull/12528](https://github.com/BerriAI/litellm/pull/12528)
- @inf3rnus made their first contribution in [https://github.com/BerriAI/litellm/pull/12121](https://github.com/BerriAI/litellm/pull/12121)

## [**Git Diff**](https://github.com/BerriAI/litellm/compare/v1.74.0-stable...v1.74.3-stable)[​](#git-diff "Direct link to git-diff")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.74.0-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **MCP Gateway Namespace Servers** - Clients connecting to LiteLLM can now specify which MCP servers to use.
- **Key/Team Based Logging on UI** - Proxy Admins can configure team or key-based logging settings directly in the UI.
- **Azure Content Safety Guardrails** - Added support for prompt injection and text moderation with Azure Content Safety Guardrails.
- **VertexAI Deepseek Models** - Support for calling VertexAI Deepseek models with LiteLLM's/chat/completions or /responses API.
- **Github Copilot API** - You can now use Github Copilot as an LLM API provider.

### MCP Gateway: Namespaced MCP Servers[​](#mcp-gateway-namespaced-mcp-servers "Direct link to MCP Gateway: Namespaced MCP Servers")

This release brings support for namespacing MCP Servers on LiteLLM MCP Gateway. This means you can specify the `x-mcp-servers` header to specify which servers to list tools from.

This is useful when you want to point MCP clients to specific MCP Servers on LiteLLM.

#### Usage[​](#usage "Direct link to Usage")

- OpenAI API
- LiteLLM Proxy
- Cursor IDE

cURL Example with Server Segregation

```
curl --location 'https://api.openai.com/v1/responses' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $OPENAI_API_KEY" \
--data '{
    "model": "gpt-4o",
    "tools": [
        {
            "type": "mcp",
            "server_label": "litellm",
            "server_url": "<your-litellm-proxy-base-url>/mcp",
            "require_approval": "never",
            "headers": {
                "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",
                "x-mcp-servers": "Zapier_Gmail"
            }
        }
    ],
    "input": "Run available tools",
    "tool_choice": "required"
}'
```

In this example, the request will only have access to tools from the "Zapier\_Gmail" MCP server.

### Team / Key Based Logging on UI[​](#team--key-based-logging-on-ui "Direct link to Team / Key Based Logging on UI")

This release brings support for Proxy Admins to configure Team/Key Based Logging Settings on the UI. This allows routing LLM request/response logs to different Langfuse/Arize projects based on the team or key.

For developers using LiteLLM, their logs are automatically routed to their specific Arize/Langfuse projects. On this release, we support the following integrations for key/team based logging:

- `langfuse`
- `arize`
- `langsmith`

### Azure Content Safety Guardrails[​](#azure-content-safety-guardrails "Direct link to Azure Content Safety Guardrails")

LiteLLM now supports **Azure Content Safety Guardrails** for Prompt Injection and Text Moderation. This is **great for internal chat-ui** use cases, as you can now create guardrails with detection for Azure’s Harm Categories, specify custom severity thresholds and run them across 100+ LLMs for just that use-case (or across all your calls).

[Get Started](https://docs.litellm.ai/docs/proxy/guardrails/azure_content_guardrail)

### Python SDK: 2.3 Second Faster Import Times[​](#python-sdk-23-second-faster-import-times "Direct link to Python SDK: 2.3 Second Faster Import Times")

This release brings significant performance improvements to the Python SDK with 2.3 seconds faster import times. We've refactored the initialization process to reduce startup overhead, making LiteLLM more efficient for applications that need quick initialization. This is a major improvement for applications that need to initialize LiteLLM quickly.

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)TypeWatsonx`watsonx/mistralai/mistral-large`131k$3.00$10.00NewAzure AI`azure_ai/cohere-rerank-v3.5`4k$2.00/1k queries-New (Rerank)

#### Features[​](#features "Direct link to Features")

- [**🆕 GitHub Copilot**](https://docs.litellm.ai/docs/providers/github_copilot) - Use GitHub Copilot API with LiteLLM - [PR](https://github.com/BerriAI/litellm/pull/12325), [Get Started](https://docs.litellm.ai/docs/providers/github_copilot)
- [**🆕 VertexAI DeepSeek**](https://docs.litellm.ai/docs/providers/vertex) - Add support for VertexAI DeepSeek models - [PR](https://github.com/BerriAI/litellm/pull/12312), [Get Started](https://docs.litellm.ai/docs/providers/vertex_partner#vertexai-deepseek)
- [**Azure AI**](https://docs.litellm.ai/docs/providers/azure_ai)
  
  - Add azure\_ai cohere rerank v3.5 - [PR](https://github.com/BerriAI/litellm/pull/12283), [Get Started](https://docs.litellm.ai/docs/providers/azure_ai#rerank-endpoint)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add size parameter support for image generation - [PR](https://github.com/BerriAI/litellm/pull/12292), [Get Started](https://docs.litellm.ai/docs/providers/vertex_image)
- [**Custom LLM**](https://docs.litellm.ai/docs/providers/custom_llm_server)
  
  - Pass through extra_ properties on "custom" llm provider - [PR](https://github.com/BerriAI/litellm/pull/12185)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Fix transform\_response handling for empty string content - [PR](https://github.com/BerriAI/litellm/pull/12202)
  - Turn Mistral to use llm\_http\_handler - [PR](https://github.com/BerriAI/litellm/pull/12245)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix tool call sequence - [PR](https://github.com/BerriAI/litellm/pull/11999)
  - Fix custom api\_base path preservation - [PR](https://github.com/BerriAI/litellm/pull/12215)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Fix user\_id validation logic - [PR](https://github.com/BerriAI/litellm/pull/11432)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Support optional args for bedrock - [PR](https://github.com/BerriAI/litellm/pull/12287)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Fix default parameters for ollama-chat - [PR](https://github.com/BerriAI/litellm/pull/12201)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Add 'audio\_url' message type support - [PR](https://github.com/BerriAI/litellm/pull/12270)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/batches**](https://docs.litellm.ai/docs/batches)
  
  - Support batch retrieve with target model Query Param - [PR](https://github.com/BerriAI/litellm/pull/12228)
  - Anthropic completion bridge improvements - [PR](https://github.com/BerriAI/litellm/pull/12228)
- [**/responses**](https://docs.litellm.ai/docs/response_api)
  
  - Azure responses api bridge improvements - [PR](https://github.com/BerriAI/litellm/pull/12224)
  - Fix responses api error handling - [PR](https://github.com/BerriAI/litellm/pull/12225)
- [**/mcp (MCP Gateway)**](https://docs.litellm.ai/docs/mcp)
  
  - Add MCP url masking on frontend - [PR](https://github.com/BerriAI/litellm/pull/12247)
  - Add MCP servers header to scope - [PR](https://github.com/BerriAI/litellm/pull/12266)
  - Litellm mcp tool prefix - [PR](https://github.com/BerriAI/litellm/pull/12289)
  - Segregate MCP tools on connections using headers - [PR](https://github.com/BerriAI/litellm/pull/12296)
  - Added changes to mcp url wrapping - [PR](https://github.com/BerriAI/litellm/pull/12207)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**/v1/messages**](https://docs.litellm.ai/docs/anthropic_unified)
  
  - Remove hardcoded model name on streaming - [PR](https://github.com/BerriAI/litellm/pull/12131)
  - Support lowest latency routing - [PR](https://github.com/BerriAI/litellm/pull/12180)
  - Non-anthropic models token usage returned - [PR](https://github.com/BerriAI/litellm/pull/12184)
- [**/chat/completions**](https://docs.litellm.ai/docs/providers/anthropic_unified)
  
  - Support Cursor IDE tool\_choice format `{"type": "auto"}` - [PR](https://github.com/BerriAI/litellm/pull/12168)
- [**/generateContent**](https://docs.litellm.ai/docs/generate_content)
  
  - Allow passing litellm\_params - [PR](https://github.com/BerriAI/litellm/pull/12177)
  - Only pass supported params when using OpenAI models - [PR](https://github.com/BerriAI/litellm/pull/12297)
  - Fix using gemini-cli with Vertex Anthropic Models - [PR](https://github.com/BerriAI/litellm/pull/12246)
- **Streaming**
  
  - Fix Error code: 307 for LlamaAPI Streaming Chat - [PR](https://github.com/BerriAI/litellm/pull/11946)
  - Store finish reason even if is\_finished - [PR](https://github.com/BerriAI/litellm/pull/12250)

* * *

## Spend Tracking / Budget Improvements[​](#spend-tracking--budget-improvements "Direct link to Spend Tracking / Budget Improvements")

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- Fix allow strings in calculate cost - [PR](https://github.com/BerriAI/litellm/pull/12200)
- VertexAI Anthropic streaming cost tracking with prompt caching fixes - [PR](https://github.com/BerriAI/litellm/pull/12188)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- **Team Management**
  
  - Prevent team model reset on model add - [PR](https://github.com/BerriAI/litellm/pull/12144)
  - Return team-only models on /v2/model/info - [PR](https://github.com/BerriAI/litellm/pull/12144)
  - Render team member budget correctly - [PR](https://github.com/BerriAI/litellm/pull/12144)
- **UI Rendering**
  
  - Fix rendering ui on non-root images - [PR](https://github.com/BerriAI/litellm/pull/12226)
  - Correctly display 'Internal Viewer' user role - [PR](https://github.com/BerriAI/litellm/pull/12284)
- **Configuration**
  
  - Handle empty config.yaml - [PR](https://github.com/BerriAI/litellm/pull/12189)
  - Fix gemini /models - replace models/ as expected - [PR](https://github.com/BerriAI/litellm/pull/12189)

#### Features[​](#features-2 "Direct link to Features")

- **Team Management**
  
  - Allow adding team specific logging callbacks - [PR](https://github.com/BerriAI/litellm/pull/12261)
  - Add Arize Team Based Logging - [PR](https://github.com/BerriAI/litellm/pull/12264)
  - Allow Viewing/Editing Team Based Callbacks - [PR](https://github.com/BerriAI/litellm/pull/12265)
- **UI Improvements**
  
  - Comma separated spend and budget display - [PR](https://github.com/BerriAI/litellm/pull/12317)
  - Add logos to callback list - [PR](https://github.com/BerriAI/litellm/pull/12244)
- **CLI**
  
  - Add litellm-proxy cli login for starting to use litellm proxy - [PR](https://github.com/BerriAI/litellm/pull/12216)
- **Email Templates**
  
  - Customizable Email template - Subject and Signature - [PR](https://github.com/BerriAI/litellm/pull/12218)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-3 "Direct link to Features")

- Guardrails
  
  - All guardrails are now supported on the UI - [PR](https://github.com/BerriAI/litellm/pull/12349)
- [**Azure Content Safety**](https://docs.litellm.ai/docs/guardrails/azure_content_safety)
  
  - Add Azure Content Safety Guardrails to LiteLLM proxy - [PR](https://github.com/BerriAI/litellm/pull/12268)
  - Add azure content safety guardrails to the UI - [PR](https://github.com/BerriAI/litellm/pull/12309)
- [**DeepEval**](https://docs.litellm.ai/docs/observability/deepeval_integration)
  
  - Fix DeepEval logging format for failure events - [PR](https://github.com/BerriAI/litellm/pull/12303)
- [**Arize**](https://docs.litellm.ai/docs/proxy/logging#arize)
  
  - Add Arize Team Based Logging - [PR](https://github.com/BerriAI/litellm/pull/12264)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Langfuse prompt\_version support - [PR](https://github.com/BerriAI/litellm/pull/12301)
- [**Sentry Integration**](https://docs.litellm.ai/docs/observability/sentry)
  
  - Add sentry scrubbing - [PR](https://github.com/BerriAI/litellm/pull/12210)
- [**AWS SQS Logging**](https://docs.litellm.ai/docs/proxy/logging#aws-sqs)
  
  - New AWS SQS Logging Integration - [PR](https://github.com/BerriAI/litellm/pull/12176)
- [**S3 Logger**](https://docs.litellm.ai/docs/proxy/logging#s3-buckets)
  
  - Add failure logging support - [PR](https://github.com/BerriAI/litellm/pull/12299)
- [**Prometheus Metrics**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Add better error validation for prometheus metrics and labels - [PR](https://github.com/BerriAI/litellm/pull/12182)

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- **Security**
  
  - Ensure only LLM API route fails get logged on Langfuse - [PR](https://github.com/BerriAI/litellm/pull/12308)
- **OpenMeter**
  
  - Integration error handling fix - [PR](https://github.com/BerriAI/litellm/pull/12147)
- **Message Redaction**
  
  - Ensure message redaction works for responses API logging - [PR](https://github.com/BerriAI/litellm/pull/12291)
- **Bedrock Guardrails**
  
  - Fix bedrock guardrails post\_call for streaming responses - [PR](https://github.com/BerriAI/litellm/pull/12252)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-4 "Direct link to Features")

- **Python SDK**
  
  - 2 second faster import times - [PR](https://github.com/BerriAI/litellm/pull/12135)
  - Reduce python sdk import time by .3s - [PR](https://github.com/BerriAI/litellm/pull/12140)
- **Error Handling**
  
  - Add error handling for MCP tools not found or invalid server - [PR](https://github.com/BerriAI/litellm/pull/12223)
- **SSL/TLS**
  
  - Fix SSL certificate error - [PR](https://github.com/BerriAI/litellm/pull/12327)
  - Fix custom ca bundle support in aiohttp transport - [PR](https://github.com/BerriAI/litellm/pull/12281)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Startup**
  
  - Add new banner on startup - [PR](https://github.com/BerriAI/litellm/pull/12328)
- **Dependencies**
  
  - Update pydantic version - [PR](https://github.com/BerriAI/litellm/pull/12213)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @wildcard made their first contribution in [https://github.com/BerriAI/litellm/pull/12157](https://github.com/BerriAI/litellm/pull/12157)
- @colesmcintosh made their first contribution in [https://github.com/BerriAI/litellm/pull/12168](https://github.com/BerriAI/litellm/pull/12168)
- @seyeong-han made their first contribution in [https://github.com/BerriAI/litellm/pull/11946](https://github.com/BerriAI/litellm/pull/11946)
- @dinggh made their first contribution in [https://github.com/BerriAI/litellm/pull/12162](https://github.com/BerriAI/litellm/pull/12162)
- @raz-alon made their first contribution in [https://github.com/BerriAI/litellm/pull/11432](https://github.com/BerriAI/litellm/pull/11432)
- @tofarr made their first contribution in [https://github.com/BerriAI/litellm/pull/12200](https://github.com/BerriAI/litellm/pull/12200)
- @szafranek made their first contribution in [https://github.com/BerriAI/litellm/pull/12179](https://github.com/BerriAI/litellm/pull/12179)
- @SamBoyd made their first contribution in [https://github.com/BerriAI/litellm/pull/12147](https://github.com/BerriAI/litellm/pull/12147)
- @lizzij made their first contribution in [https://github.com/BerriAI/litellm/pull/12219](https://github.com/BerriAI/litellm/pull/12219)
- @cipri-tom made their first contribution in [https://github.com/BerriAI/litellm/pull/12201](https://github.com/BerriAI/litellm/pull/12201)
- @zsimjee made their first contribution in [https://github.com/BerriAI/litellm/pull/12185](https://github.com/BerriAI/litellm/pull/12185)
- @jroberts2600 made their first contribution in [https://github.com/BerriAI/litellm/pull/12175](https://github.com/BerriAI/litellm/pull/12175)
- @njbrake made their first contribution in [https://github.com/BerriAI/litellm/pull/12202](https://github.com/BerriAI/litellm/pull/12202)
- @NANDINI-star made their first contribution in [https://github.com/BerriAI/litellm/pull/12244](https://github.com/BerriAI/litellm/pull/12244)
- @utsumi-fj made their first contribution in [https://github.com/BerriAI/litellm/pull/12230](https://github.com/BerriAI/litellm/pull/12230)
- @dcieslak19973 made their first contribution in [https://github.com/BerriAI/litellm/pull/12283](https://github.com/BerriAI/litellm/pull/12283)
- @hanouticelina made their first contribution in [https://github.com/BerriAI/litellm/pull/12286](https://github.com/BerriAI/litellm/pull/12286)
- @lowjiansheng made their first contribution in [https://github.com/BerriAI/litellm/pull/11999](https://github.com/BerriAI/litellm/pull/11999)
- @JoostvDoorn made their first contribution in [https://github.com/BerriAI/litellm/pull/12281](https://github.com/BerriAI/litellm/pull/12281)
- @takashiishida made their first contribution in [https://github.com/BerriAI/litellm/pull/12239](https://github.com/BerriAI/litellm/pull/12239)

## [**Git Diff**](https://github.com/BerriAI/litellm/compare/v1.73.6-stable...v1.74.0-stable)[​](#git-diff "Direct link to git-diff")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.73.6-stable.patch.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

### Claude on gemini-cli[​](#claude-on-gemini-cli "Direct link to Claude on gemini-cli")

This release brings support for using gemini-cli with LiteLLM.

You can use claude-sonnet-4, gemini-2.5-flash (Vertex AI & Google AI Studio), gpt-4.1 and any LiteLLM supported model on gemini-cli.

When you use gemini-cli with LiteLLM you get the following benefits:

**Developer Benefits:**

- Universal Model Access: Use any LiteLLM supported model (Anthropic, OpenAI, Vertex AI, Bedrock, etc.) through the gemini-cli interface.
- Higher Rate Limits & Reliability: Load balance across multiple models and providers to avoid hitting individual provider limits, with fallbacks to ensure you get responses even if one provider fails.

**Proxy Admin Benefits:**

- Centralized Management: Control access to all models through a single LiteLLM proxy instance without giving your developers API Keys to each provider.
- Budget Controls: Set spending limits and track costs across all gemini-cli usage.

[Get Started](https://docs.litellm.ai/docs/tutorials/litellm_gemini_cli)

### Batch API Cost Tracking[​](#batch-api-cost-tracking "Direct link to Batch API Cost Tracking")

v1.73.6 brings cost tracking for [LiteLLM Managed Batch API](https://docs.litellm.ai/docs/proxy/managed_batches) calls to LiteLLM. Previously, this was not being done for Batch API calls using LiteLLM Managed Files. Now, LiteLLM will store the status of each batch call in the DB and poll incomplete batch jobs in the background, emitting a spend log for cost tracking once the batch is complete.

There is no new flag / change needed on your end. Over the next few weeks we hope to extend this to cover batch cost tracking for the Anthropic passthrough as well.

[Get Started](https://docs.litellm.ai/docs/proxy/managed_batches)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)TypeAzure OpenAI`azure/o3-pro`200k$20.00$80.00NewOpenRouter`openrouter/mistralai/mistral-small-3.2-24b-instruct`32k$0.1$0.3NewOpenAI`o3-deep-research`200k$10.00$40.00NewOpenAI`o3-deep-research-2025-06-26`200k$10.00$40.00NewOpenAI`o4-mini-deep-research`200k$2.00$8.00NewOpenAI`o4-mini-deep-research-2025-06-26`200k$2.00$8.00NewDeepseek`deepseek-r1`65k$0.55$2.19NewDeepseek`deepseek-v3`65k$0.27$0.07New

### Updated Models[​](#updated-models "Direct link to Updated Models")

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Sambanova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Handle float timestamps - [PR](https://github.com/BerriAI/litellm/pull/11971) s/o [@neubig](https://github.com/neubig)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - support Azure Authentication method (azure ad token, api keys) on Responses API - [PR](https://github.com/BerriAI/litellm/pull/11941) s/o [@hsuyuming](https://github.com/hsuyuming)
  - Map ‘image\_url’ str as nested dict - [PR](https://github.com/BerriAI/litellm/pull/12075) s/o [@davis-featherstone](https://github.com/davis-featherstone)
- [**Watsonx**](https://docs.litellm.ai/docs/providers/watsonx)
  
  - Set ‘model’ field to None when model is part of a custom deployment - fixes error raised by WatsonX in those cases - [PR](https://github.com/BerriAI/litellm/pull/11854) s/o [@cbjuan](https://github.com/cbjuan)
- [**Perplexity**](https://docs.litellm.ai/docs/providers/perplexity)
  
  - Support web\_search\_options - [PR](https://github.com/BerriAI/litellm/pull/11983)
  - Support citation token and search queries cost calculation - [PR](https://github.com/BerriAI/litellm/pull/11938)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Null value in usage block handling - [PR](https://github.com/BerriAI/litellm/pull/12068)
- **Gemini ([Google AI Studio](https://docs.litellm.ai/docs/providers/gemini) + [VertexAI](https://docs.litellm.ai/docs/providers/vertex))**
  
  - Only use accepted format values (enum and datetime) - else gemini raises errors - [PR](https://github.com/BerriAI/litellm/pull/11989)
  - Cache tools if passed alongside cached content (else gemini raises an error) - [PR](https://github.com/BerriAI/litellm/pull/11989)
  - Json schema translation improvement: Fix unpack\_def handling of nested $ref inside anyof items - [PR](https://github.com/BerriAI/litellm/pull/11964)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Fix thinking prompt to match hugging face recommendation - [PR](https://github.com/BerriAI/litellm/pull/12007)
  - Add `supports_response_schema: true` for all mistral models except codestral-mamba - [PR](https://github.com/BerriAI/litellm/pull/12024)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Fix unnecessary await on embedding calls - [PR](https://github.com/BerriAI/litellm/pull/12024)

#### Features[​](#features "Direct link to Features")

- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure)
  
  - Check if o-series model supports reasoning effort (enables drop\_params to work for o1 models)
  - Assistant + tool use cost tracking - [PR](https://github.com/BerriAI/litellm/pull/12045)
- [**Nvidia Nim**](https://docs.litellm.ai/docs/providers/nvidia_nim)
  
  - Add ‘response\_format’ param support - [PR](https://github.com/BerriAI/litellm/pull/12003) @shagunb-acn
- [**ElevenLabs**](https://docs.litellm.ai/docs/providers/elevenlabs)
  
  - New STT provider - [PR](https://github.com/BerriAI/litellm/pull/12119)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/mcp**](https://docs.litellm.ai/docs/mcp)
  
  - Send appropriate auth string value to `/tool/call` endpoint with `x-mcp-auth` - [PR](https://github.com/BerriAI/litellm/pull/11968) s/o [@wagnerjt](https://github.com/wagnerjt)
- [**/v1/messages**](https://docs.litellm.ai/docs/anthropic_unified)
  
  - [Custom LLM](https://docs.litellm.ai/docs/providers/custom_llm_server#anthropic-v1messages) support - [PR](https://github.com/BerriAI/litellm/pull/12016)
- [**/chat/completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Azure Responses API via chat completion support - [PR](https://github.com/BerriAI/litellm/pull/12016)
- [**/responses**](https://docs.litellm.ai/docs/response_api)
  
  - Add reasoning content support for non-openai providers - [PR](https://github.com/BerriAI/litellm/pull/12055)
- **\[NEW] /generateContent**
  
  - New endpoints for gemini cli support - [PR](https://github.com/BerriAI/litellm/pull/12040)
  - Support calling Google AI Studio / VertexAI Gemini models in their native format - [PR](https://github.com/BerriAI/litellm/pull/12046)
  - Add logging + cost tracking for stream + non-stream vertex/google ai studio routes - [PR](https://github.com/BerriAI/litellm/pull/12058)
  - Add Bridge from generateContent to /chat/completions - [PR](https://github.com/BerriAI/litellm/pull/12081)
- [**/batches**](https://docs.litellm.ai/docs/batches)
  
  - Filter deployments to only those where managed file was written to - [PR](https://github.com/BerriAI/litellm/pull/12048)
  - Save all model / file id mappings in db (previously it was just the first one) - enables ‘true’ loadbalancing - [PR](https://github.com/BerriAI/litellm/pull/12048)
  - Support List Batches with target model name specified - [PR](https://github.com/BerriAI/litellm/pull/12049)

* * *

## Spend Tracking / Budget Improvements[​](#spend-tracking--budget-improvements "Direct link to Spend Tracking / Budget Improvements")

#### Features[​](#features-2 "Direct link to Features")

- [**Passthrough**](https://docs.litellm.ai/docs/pass_through)
  
  - [Bedrock](https://docs.litellm.ai/docs/pass_through/bedrock) - cost tracking (`/invoke` + `/converse` routes) on streaming + non-streaming - [PR](https://github.com/BerriAI/litellm/pull/12123)
  - [VertexAI](https://docs.litellm.ai/docs/pass_through/vertex_ai) - anthropic cost calculation support - [PR](https://github.com/BerriAI/litellm/pull/11992)
- [**Batches**](https://docs.litellm.ai/docs/batches)
  
  - Background job for cost tracking LiteLLM Managed batches - [PR](https://github.com/BerriAI/litellm/pull/12125)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **General UI**
  
  - Fix today selector date mutation in dashboard components - [PR](https://github.com/BerriAI/litellm/pull/12042)
- **Usage**
  
  - Aggregate usage data across all pages of paginated endpoint - [PR](https://github.com/BerriAI/litellm/pull/12033)
- **Teams**
  
  - De-duplicate models in team settings dropdown - [PR](https://github.com/BerriAI/litellm/pull/12074)
- **Models**
  
  - Preserve public model name when selecting ‘test connect’ with azure model (previously would reset) - [PR](https://github.com/BerriAI/litellm/pull/11713)
- **Invitation Links**
  
  - Ensure Invite links email contain the correct invite id when using tf provider - [PR](https://github.com/BerriAI/litellm/pull/12130)

#### Features[​](#features-3 "Direct link to Features")

- **Models**
  
  - Add ‘last success’ column to health check table - [PR](https://github.com/BerriAI/litellm/pull/11903)
- **MCP**
  
  - New UI component to support auth types: api key, bearer token, basic auth - [PR](https://github.com/BerriAI/litellm/pull/11968) s/o [@wagnerjt](https://github.com/wagnerjt)
  - Ensure internal users can access /mcp and /mcp/ routes - [PR](https://github.com/BerriAI/litellm/pull/12106)
- **SCIM**
  
  - Ensure default\_internal\_user\_params are applied for new users - [PR](https://github.com/BerriAI/litellm/pull/12015)
- **Team**
  
  - Support default key expiry for team member keys - [PR](https://github.com/BerriAI/litellm/pull/12023)
  - Expand team member add check to cover user email - [PR](https://github.com/BerriAI/litellm/pull/12082)
- **UI**
  
  - Restrict UI access by SSO group - [PR](https://github.com/BerriAI/litellm/pull/12023)
- **Keys**
  
  - Add new new\_key param for regenerating key - [PR](https://github.com/BerriAI/litellm/pull/12087)
- **Test Keys**
  
  - New ‘get code’ button for getting runnable python code snippet based on ui configuration - [PR](https://github.com/BerriAI/litellm/pull/11629)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **Braintrust**
  
  - Adds model to metadata to enable braintrust cost estimation - [PR](https://github.com/BerriAI/litellm/pull/12022)

#### Features[​](#features-4 "Direct link to Features")

- **Callbacks**
  
  - (Enterprise) - disable logging callbacks in request headers - [PR](https://github.com/BerriAI/litellm/pull/11985)
  - Add List Callbacks API Endpoint - [PR](https://github.com/BerriAI/litellm/pull/11987)
- **Bedrock Guardrail**
  
  - Don't raise exception on intervene action - [PR](https://github.com/BerriAI/litellm/pull/11875)
  - Ensure PII Masking is applied on response streaming or non streaming content when using post call - [PR](https://github.com/BerriAI/litellm/pull/12086)
- **\[NEW] Palo Alto Networks Prisma AIRS Guardrail**
  
  - [PR](https://github.com/BerriAI/litellm/pull/12116)
- **ElasticSearch**
  
  - New Elasticsearch Logging Tutorial - [PR](https://github.com/BerriAI/litellm/pull/11761)
- **Message Redaction**
  
  - Preserve usage / model information for Embedding redaction - [PR](https://github.com/BerriAI/litellm/pull/12088)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- **Team-only models**
  
  - Filter team-only models from routing logic for non-team calls
- **Context Window Exceeded error**
  
  - Catch anthropic exceptions - [PR](https://github.com/BerriAI/litellm/pull/12113)

#### Features[​](#features-5 "Direct link to Features")

- **Router**
  
  - allow using dynamic cooldown time for a specific deployment - [PR](https://github.com/BerriAI/litellm/pull/12037)
  - handle cooldown\_time = 0 for deployments - [PR](https://github.com/BerriAI/litellm/pull/12108)
- **Redis**
  
  - Add better debugging to see what variables are set - [PR](https://github.com/BerriAI/litellm/pull/12073)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- **aiohttp**
  
  - Check HTTP\_PROXY vars in networking requests
  - Allow using HTTP_ Proxy settings with trust\_env

#### Features[​](#features-6 "Direct link to Features")

- **Docs**
  
  - Add recommended spec - [PR](https://github.com/BerriAI/litellm/pull/11980)
- **Swagger**
  
  - Introduce new environment variable NO\_REDOC to opt-out Redoc - [PR](https://github.com/BerriAI/litellm/pull/12092)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @mukesh-dream11 made their first contribution in [https://github.com/BerriAI/litellm/pull/11969](https://github.com/BerriAI/litellm/pull/11969)
- @cbjuan made their first contribution in [https://github.com/BerriAI/litellm/pull/11854](https://github.com/BerriAI/litellm/pull/11854)
- @ryan-castner made their first contribution in [https://github.com/BerriAI/litellm/pull/12055](https://github.com/BerriAI/litellm/pull/12055)
- @davis-featherstone made their first contribution in [https://github.com/BerriAI/litellm/pull/12075](https://github.com/BerriAI/litellm/pull/12075)
- @Gum-Joe made their first contribution in [https://github.com/BerriAI/litellm/pull/12068](https://github.com/BerriAI/litellm/pull/12068)
- @jroberts2600 made their first contribution in [https://github.com/BerriAI/litellm/pull/12116](https://github.com/BerriAI/litellm/pull/12116)
- @ohmeow made their first contribution in [https://github.com/BerriAI/litellm/pull/12022](https://github.com/BerriAI/litellm/pull/12022)
- @amarrella made their first contribution in [https://github.com/BerriAI/litellm/pull/11942](https://github.com/BerriAI/litellm/pull/11942)
- @zhangyoufu made their first contribution in [https://github.com/BerriAI/litellm/pull/12092](https://github.com/BerriAI/litellm/pull/12092)
- @bougou made their first contribution in [https://github.com/BerriAI/litellm/pull/12088](https://github.com/BerriAI/litellm/pull/12088)
- @codeugar made their first contribution in [https://github.com/BerriAI/litellm/pull/11972](https://github.com/BerriAI/litellm/pull/11972)
- @glgh made their first contribution in [https://github.com/BerriAI/litellm/pull/12133](https://github.com/BerriAI/litellm/pull/12133)

## [**Git Diff**](https://github.com/BerriAI/litellm/compare/v1.73.0-stable...v1.73.6.rc-draft)[​](#git-diff "Direct link to git-diff")

warning

## Known Issues[​](#known-issues "Direct link to Known Issues")

The `non-root` docker image has a known issue around the UI not loading. If you use the `non-root` docker image we recommend waiting before upgrading to this version. We will post a patch fix for this.

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.73.0-stable
```

## TLDR[​](#tldr "Direct link to TLDR")

- **Why Upgrade**
  
  - User Management: Set default team for new users - enables giving all users $10 API keys for exploration.
  - Passthrough Endpoints v2: Enhanced support for subroutes and custom cost tracking for passthrough endpoints.
  - Health Check Dashboard: New frontend UI for monitoring model health and status.
- **Who Should Read**
  
  - Teams using **Passthrough Endpoints**
  - Teams using **User Management** on LiteLLM
  - Teams using **Health Check Dashboard** for models
  - Teams using **Claude Code** with LiteLLM
- **Risk of Upgrade**
  
  - **Low**
    
    - No major breaking changes to existing functionality.

<!--THE END-->

- **Major Changes**
  
  - `User Agent` will be auto-tracked as a tag in LiteLLM UI Logs Page. This means for all LLM requests you will see a `User Agent` tag in the logs page.

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

### Set Default Team for New Users[​](#set-default-team-for-new-users "Direct link to Set Default Team for New Users")

v1.73.0 introduces the ability to assign new users to Default Teams. This makes it much easier to enable experimentation with LLMs within your company, while also **ensuring spend for exploration is tracked correctly.**

What this means for **Proxy Admins**:

- Set a max budget per team member: This sets a max amount an individual can spend within a team.
- Set a default team for new users: When a new user signs in via SSO / invitation link, they will be automatically added to this team.

What this means for **Developers**:

- View models across teams: You can now go to `Models + Endpoints` and view the models you have access to, across all teams you're a member of.
- Safe create key modal: If you have no model access outside of a team (default behaviour), you are now nudged to select a team on the Create Key modal. This resolves a common confusion point for new users onboarding to the proxy.

[Get Started](https://docs.litellm.ai/docs/tutorials/default_team_self_serve)

### Passthrough Endpoints v2[​](#passthrough-endpoints-v2 "Direct link to Passthrough Endpoints v2")

This release brings support for adding billing and full URL forwarding for passthrough endpoints.

Previously, you could only map simple endpoints, but now you can add just `/bria` and all subroutes automatically get forwarded - for example, `/bria/v1/text-to-image/base/model` and `/bria/v1/enhance_image` will both be forwarded to the target URL with the same path structure.

This means you as Proxy Admin can onboard third-party endpoints like Bria API and Mistral OCR, set a cost per request, and give your developers access to the complete API functionality.

[Learn more about Passthrough Endpoints](https://docs.litellm.ai/docs/proxy/pass_through)

### v2 Health Checks[​](#v2-health-checks "Direct link to v2 Health Checks")

This release brings support for Proxy Admins to select which specific models to health check and see the health status as soon as its individual check completes, along with last check times.

This allows Proxy Admins to immediately identify which specific models are in a bad state and view the full error stack trace for faster troubleshooting.

* * *

## New / Updated Models[​](#new--updated-models "Direct link to New / Updated Models")

### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)TypeGoogle VertexAI`vertex_ai/imagen-4`N/AImage GenerationImage GenerationNewGoogle VertexAI`vertex_ai/imagen-4-preview`N/AImage GenerationImage GenerationNewGemini`gemini-2.5-pro`2M$1.25$5.00NewGemini`gemini-2.5-flash-lite`1M$0.075$0.30NewOpenRouterVarious modelsUpdatedUpdatedUpdatedUpdatedAzure`azure/o3`200k$2.00$8.00UpdatedAzure`azure/o3-pro`200k$2.00$8.00UpdatedAzure OpenAIAzure Codex ModelsVariousVariousVariousNew

### Updated Models[​](#updated-models "Direct link to Updated Models")

#### Features[​](#features "Direct link to Features")

- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Support for new /v1 preview Azure OpenAI API - [PR](https://github.com/BerriAI/litellm/pull/11934), [Get Started](https://docs.litellm.ai/docs/providers/azure/azure_responses#azure-codex-models)
  - Add Azure Codex Models support - [PR](https://github.com/BerriAI/litellm/pull/11934), [Get Started](https://docs.litellm.ai/docs/providers/azure/azure_responses#azure-codex-models)
  - Make Azure AD scope configurable - [PR](https://github.com/BerriAI/litellm/pull/11621)
  - Handle more GPT custom naming patterns - [PR](https://github.com/BerriAI/litellm/pull/11914)
  - Update o3 pricing to match OpenAI pricing - [PR](https://github.com/BerriAI/litellm/pull/11937)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add Vertex Imagen-4 models - [PR](https://github.com/BerriAI/litellm/pull/11767), [Get Started](https://docs.litellm.ai/docs/providers/vertex_image)
  - Anthropic streaming passthrough cost tracking - [PR](https://github.com/BerriAI/litellm/pull/11734)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Working Gemini TTS support via `/v1/speech` endpoint - [PR](https://github.com/BerriAI/litellm/pull/11832)
  - Fix gemini 2.5 flash config - [PR](https://github.com/BerriAI/litellm/pull/11830)
  - Add missing `flash-2.5-flash-lite` model and fix pricing - [PR](https://github.com/BerriAI/litellm/pull/11901)
  - Mark all gemini-2.5 models as supporting PDF input - [PR](https://github.com/BerriAI/litellm/pull/11907)
  - Add `gemini-2.5-pro` with reasoning support - [PR](https://github.com/BerriAI/litellm/pull/11927)
- [**AWS Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - AWS credentials no longer mandatory - [PR](https://github.com/BerriAI/litellm/pull/11765)
  - Add AWS Bedrock profiles for APAC region - [PR](https://github.com/BerriAI/litellm/pull/11883)
  - Fix AWS Bedrock Claude tool call index - [PR](https://github.com/BerriAI/litellm/pull/11842)
  - Handle base64 file data with `qs:..` prefix - [PR](https://github.com/BerriAI/litellm/pull/11908)
  - Add Mistral Small to BEDROCK\_CONVERSE\_MODELS - [PR](https://github.com/BerriAI/litellm/pull/11760)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Enhance Mistral API with parallel tool calls support - [PR](https://github.com/BerriAI/litellm/pull/11770)
- [**Meta Llama API**](https://docs.litellm.ai/docs/providers/meta_llama)
  
  - Enable tool calling for meta\_llama models - [PR](https://github.com/BerriAI/litellm/pull/11895)
- [**Volcengine**](https://docs.litellm.ai/docs/providers/volcengine)
  
  - Add thinking parameter support - [PR](https://github.com/BerriAI/litellm/pull/11914)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Handle missing tokenCount in promptTokensDetails - [PR](https://github.com/BerriAI/litellm/pull/11896)
  - Fix vertex AI claude thinking params - [PR](https://github.com/BerriAI/litellm/pull/11796)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix web search error with responses API - [PR](https://github.com/BerriAI/litellm/pull/11894), [Get Started](https://docs.litellm.ai/docs/completion/web_search#responses-litellmresponses)
- [**Custom LLM**](https://docs.litellm.ai/docs/providers/custom_llm_server)
  
  - Set anthropic custom LLM provider property - [PR](https://github.com/BerriAI/litellm/pull/11907)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Bump anthropic package version - [PR](https://github.com/BerriAI/litellm/pull/11851)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Update ollama\_embeddings to work on sync API - [PR](https://github.com/BerriAI/litellm/pull/11746)
  - Fix response\_format not working - [PR](https://github.com/BerriAI/litellm/pull/11880)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Day-0 support for OpenAI re-usable prompts Responses API - [PR](https://github.com/BerriAI/litellm/pull/11782), [Get Started](https://docs.litellm.ai/docs/providers/openai/responses_api#reusable-prompts)
  - Support passing image URLs in Completion-to-Responses bridge - [PR](https://github.com/BerriAI/litellm/pull/11833)
- [**MCP Gateway**](https://docs.litellm.ai/docs/mcp)
  
  - Add Allowed MCPs to Creating/Editing Organizations - [PR](https://github.com/BerriAI/litellm/pull/11893), [Get Started](https://docs.litellm.ai/docs/mcp#-mcp-permission-management)
  - Allow connecting to MCP with authentication headers - [PR](https://github.com/BerriAI/litellm/pull/11891), [Get Started](https://docs.litellm.ai/docs/mcp#using-your-mcp-with-client-side-credentials)
- [**Speech API**](https://docs.litellm.ai/docs/speech)
  
  - Working Gemini TTS support via OpenAI's `/v1/speech` endpoint - [PR](https://github.com/BerriAI/litellm/pull/11832)
- [**Passthrough Endpoints**](https://docs.litellm.ai/docs/proxy/pass_through)
  
  - Add support for subroutes for passthrough endpoints - [PR](https://github.com/BerriAI/litellm/pull/11827)
  - Support for setting custom cost per passthrough request - [PR](https://github.com/BerriAI/litellm/pull/11870)
  - Ensure "Request" is tracked for passthrough requests on LiteLLM Proxy - [PR](https://github.com/BerriAI/litellm/pull/11873)
  - Add V2 Passthrough endpoints on UI - [PR](https://github.com/BerriAI/litellm/pull/11905)
  - Move passthrough endpoints under Models + Endpoints in UI - [PR](https://github.com/BerriAI/litellm/pull/11871)
  - QA improvements for adding passthrough endpoints - [PR](https://github.com/BerriAI/litellm/pull/11909), [PR](https://github.com/BerriAI/litellm/pull/11939)
- [**Models API**](https://docs.litellm.ai/docs/completion/model_alias)
  
  - Allow `/models` to return correct models for custom wildcard prefixes - [PR](https://github.com/BerriAI/litellm/pull/11784)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**Messages API**](https://docs.litellm.ai/docs/anthropic_unified)
  
  - Fix `/v1/messages` endpoint always using us-central1 with vertex\_ai-anthropic models - [PR](https://github.com/BerriAI/litellm/pull/11831)
  - Fix model\_group tracking for `/v1/messages` and `/moderations` - [PR](https://github.com/BerriAI/litellm/pull/11933)
  - Fix cost tracking and logging via `/v1/messages` API when using Claude Code - [PR](https://github.com/BerriAI/litellm/pull/11928)
- [**MCP Gateway**](https://docs.litellm.ai/docs/mcp)
  
  - Fix using MCPs defined on config.yaml - [PR](https://github.com/BerriAI/litellm/pull/11824)
- [**Chat Completion API**](https://docs.litellm.ai/docs/completion/input)
  
  - Allow dict for tool\_choice argument in acompletion - [PR](https://github.com/BerriAI/litellm/pull/11860)
- [**Passthrough Endpoints**](https://docs.litellm.ai/docs/pass_through/langfuse)
  
  - Don't log request to Langfuse passthrough on Langfuse - [PR](https://github.com/BerriAI/litellm/pull/11768)

* * *

## Spend Tracking[​](#spend-tracking "Direct link to Spend Tracking")

#### Features[​](#features-2 "Direct link to Features")

- [**User Agent Tracking**](https://docs.litellm.ai/docs/proxy/cost_tracking)
  
  - Automatically track spend by user agent (allows cost tracking for Claude Code) - [PR](https://github.com/BerriAI/litellm/pull/11781)
  - Add user agent tags in spend logs payload - [PR](https://github.com/BerriAI/litellm/pull/11872)
- [**Tag Management**](https://docs.litellm.ai/docs/proxy/cost_tracking)
  
  - Support adding public model names in tag management - [PR](https://github.com/BerriAI/litellm/pull/11908)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Test Key Page**
  
  - Allow testing `/v1/messages` on the Test Key Page - [PR](https://github.com/BerriAI/litellm/pull/11930)
- [**SSO**](https://docs.litellm.ai/docs/proxy/sso)
  
  - Allow passing additional headers - [PR](https://github.com/BerriAI/litellm/pull/11781)
- [**JWT Auth**](https://docs.litellm.ai/docs/proxy/jwt_auth)
  
  - Correctly return user email - [PR](https://github.com/BerriAI/litellm/pull/11783)
- [**Model Management**](https://docs.litellm.ai/docs/proxy/model_management)
  
  - Allow editing model access group for existing model - [PR](https://github.com/BerriAI/litellm/pull/11783)
- [**Team Management**](https://docs.litellm.ai/docs/proxy/team_management)
  
  - Allow setting default team for new users - [PR](https://github.com/BerriAI/litellm/pull/11874), [PR](https://github.com/BerriAI/litellm/pull/11877)
  - Fix default team settings - [PR](https://github.com/BerriAI/litellm/pull/11887)
- [**SCIM**](https://docs.litellm.ai/docs/proxy/scim)
  
  - Add error handling for existing user on SCIM - [PR](https://github.com/BerriAI/litellm/pull/11862)
  - Add SCIM PATCH and PUT operations for users - [PR](https://github.com/BerriAI/litellm/pull/11863)
- **Health Check Dashboard**
  
  - Implement health check backend API and storage functionality - [PR](https://github.com/BerriAI/litellm/pull/11852)
  - Add LiteLLM\_HealthCheckTable to database schema - [PR](https://github.com/BerriAI/litellm/pull/11677)
  - Implement health check frontend UI components and dashboard integration - [PR](https://github.com/BerriAI/litellm/pull/11679)
  - Add success modal for health check responses - [PR](https://github.com/BerriAI/litellm/pull/11899)
  - Fix clickable model ID in health check table - [PR](https://github.com/BerriAI/litellm/pull/11898)
  - Fix health check UI table design - [PR](https://github.com/BerriAI/litellm/pull/11897)

* * *

## Logging / Guardrails Integrations[​](#logging--guardrails-integrations "Direct link to Logging / Guardrails Integrations")

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- [**Prometheus**](https://docs.litellm.ai/docs/observability/prometheus)
  
  - Fix bug for using prometheus metrics config - [PR](https://github.com/BerriAI/litellm/pull/11779)

* * *

## Security & Reliability[​](#security--reliability "Direct link to Security & Reliability")

#### Security Fixes[​](#security-fixes "Direct link to Security Fixes")

- [**Documentation Security**](https://docs.litellm.ai/docs)
  
  - Security fixes for docs - [PR](https://github.com/BerriAI/litellm/pull/11776)
  - Add Trivy Security Scan for UI + Docs folder - remove all vulnerabilities - [PR](https://github.com/BerriAI/litellm/pull/11778)

#### Reliability Improvements[​](#reliability-improvements "Direct link to Reliability Improvements")

- [**Dependencies**](https://docs.litellm.ai/docs)
  
  - Fix aiohttp version requirement - [PR](https://github.com/BerriAI/litellm/pull/11777)
  - Bump next from 14.2.26 to 14.2.30 in UI dashboard - [PR](https://github.com/BerriAI/litellm/pull/11720)
- [**Networking**](https://docs.litellm.ai/docs)
  
  - Allow using CA Bundles - [PR](https://github.com/BerriAI/litellm/pull/11906)
  - Add workload identity federation between GCP and AWS - [PR](https://github.com/BerriAI/litellm/pull/10210)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-4 "Direct link to Features")

- [**Deployment**](https://docs.litellm.ai/docs/proxy/deploy)
  
  - Add deployment annotations for Kubernetes - [PR](https://github.com/BerriAI/litellm/pull/11849)
  - Add ciphers in command and pass to hypercorn for proxy - [PR](https://github.com/BerriAI/litellm/pull/11916)
- [**Custom Root Path**](https://docs.litellm.ai/docs/proxy/deploy)
  
  - Fix loading UI on custom root path - [PR](https://github.com/BerriAI/litellm/pull/11912)
- [**SDK Improvements**](https://docs.litellm.ai/docs/proxy/reliability)
  
  - LiteLLM SDK / Proxy improvement (don't transform message client-side) - [PR](https://github.com/BerriAI/litellm/pull/11908)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- [**Observability**](https://docs.litellm.ai/docs/observability)
  
  - Fix boto3 tracer wrapping for observability - [PR](https://github.com/BerriAI/litellm/pull/11869)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @kjoth made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11621)
- @shagunb-acn made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11760)
- @MadsRC made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11765)
- @Abiji-2020 made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11746)
- @salzubi401 made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11803)
- @orolega made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11826)
- @X4tar made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11796)
- @karen-veigas made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11858)
- @Shankyg made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11859)
- @pascallim made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/10210)
- @lgruen-vcgs made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11883)
- @rinormaloku made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11851)
- @InvisibleMan1306 made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11849)
- @ervwalter made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11937)
- @ThakeeNathees made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11880)
- @jnhyperion made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11842)
- @Jannchie made their first contribution in [PR](https://github.com/BerriAI/litellm/pull/11860)

* * *

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## [Git Diff](https://github.com/BerriAI/litellm/compare/v1.72.6-stable...v1.73.0.rc)[​](#git-diff "Direct link to git-diff")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.72.6-stable
```

## TLDR[​](#tldr "Direct link to TLDR")

- **Why Upgrade**
  
  - Codex-mini on Claude Code: You can now use `codex-mini` (OpenAI’s code assistant model) via Claude Code.
  - MCP Permissions Management: Manage permissions for MCP Servers by Keys, Teams, Organizations (entities) on LiteLLM.
  - UI: Turn on/off auto refresh on logs view.
  - Rate Limiting: Support for output token-only rate limiting.
- **Who Should Read**
  
  - Teams using `/v1/messages` API (Claude Code)
  - Teams using **MCP**
  - Teams giving access to self-hosted models and setting rate limits
- **Risk of Upgrade**
  
  - **Low**
    
    - No major changes to existing functionality or package updates.

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

### MCP Permissions Management[​](#mcp-permissions-management "Direct link to MCP Permissions Management")

This release brings support for managing permissions for MCP Servers by Keys, Teams, Organizations (entities) on LiteLLM. When a MCP client attempts to list tools, LiteLLM will only return the tools the entity has permissions to access.

This is great for use cases that require access to restricted data (e.g Jira MCP) that you don't want everyone to use.

For Proxy Admins, this enables centralized management of all MCP Servers with access control. For developers, this means you'll only see the MCP tools assigned to you.

### Codex-mini on Claude Code[​](#codex-mini-on-claude-code "Direct link to Codex-mini on Claude Code")

This release brings support for calling `codex-mini` (OpenAI’s code assistant model) via Claude Code.

This is done by LiteLLM enabling any Responses API model (including `o3-pro`) to be called via `/chat/completions` and `/v1/messages` endpoints. This includes:

- Streaming calls
- Non-streaming calls
- Cost Tracking on success + failure for Responses API models

Here's how to use it [today](https://docs.litellm.ai/docs/tutorials/claude_responses_api)

* * *

## New / Updated Models[​](#new--updated-models "Direct link to New / Updated Models")

### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)TypeVertexAI`vertex_ai/claude-opus-4`200K$15.00$75.00NewOpenAI`gpt-4o-audio-preview-2025-06-03`128k$2.5 (text), $40 (audio)$10 (text), $80 (audio)NewOpenAI`o3-pro`200k2080NewOpenAI`o3-pro-2025-06-10`200k2080NewOpenAI`o3`200k28UpdatedOpenAI`o3-2025-04-16`200k28UpdatedAzure`azure/gpt-4o-mini-transcribe`16k1.25 (text), 3 (audio)5 (text)NewMistral`mistral/magistral-medium-latest`40k25NewMistral`mistral/magistral-small-latest`40k0.51.5New

- Deepgram: `nova-3` cost per second pricing is [now supported](https://github.com/BerriAI/litellm/pull/11634).

### Updated Models[​](#updated-models "Direct link to Updated Models")

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Watsonx**](https://docs.litellm.ai/docs/providers/watsonx)
  
  - Ignore space id on Watsonx deployments (throws json errors) - [PR](https://github.com/BerriAI/litellm/pull/11527)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Set tool call id for streaming calls - [PR](https://github.com/BerriAI/litellm/pull/11528)
- **Gemini ([VertexAI](https://docs.litellm.ai/docs/providers/vertex) + [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini))**
  
  - Fix tool call indexes - [PR](https://github.com/BerriAI/litellm/pull/11558)
  - Handle empty string for arguments in function calls - [PR](https://github.com/BerriAI/litellm/pull/11601)
  - Add audio/ogg mime type support when inferring from file url’s - [PR](https://github.com/BerriAI/litellm/pull/11635)
- [**Custom LLM**](https://docs.litellm.ai/docs/providers/custom_llm_server)
  
  - Fix passing api\_base, api\_key, litellm\_params\_dict to custom\_llm embedding methods - [PR](https://github.com/BerriAI/litellm/pull/11450) s/o [ElefHead](https://github.com/ElefHead)
- [**Huggingface**](https://docs.litellm.ai/docs/providers/huggingface)
  
  - Add /chat/completions to endpoint url when missing - [PR](https://github.com/BerriAI/litellm/pull/11630)
- [**Deepgram**](https://docs.litellm.ai/docs/providers/deepgram)
  
  - Support async httpx calls - [PR](https://github.com/BerriAI/litellm/pull/11641)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Append prefix (if set) to assistant content start - [PR](https://github.com/BerriAI/litellm/pull/11719)

#### Features[​](#features "Direct link to Features")

- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Support vertex credentials set via env var on passthrough - [PR](https://github.com/BerriAI/litellm/pull/11527)
  - Support for choosing ‘global’ region when model is only available there - [PR](https://github.com/BerriAI/litellm/pull/11566)
  - Anthropic passthrough cost calculation + token tracking - [PR](https://github.com/BerriAI/litellm/pull/11611)
  - Support ‘global’ vertex region on passthrough - [PR](https://github.com/BerriAI/litellm/pull/11661)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - ‘none’ tool choice param support - [PR](https://github.com/BerriAI/litellm/pull/11695), [Get Started](https://docs.litellm.ai/docs/providers/anthropic#disable-tool-calling)
- [**Perplexity**](https://docs.litellm.ai/docs/providers/perplexity)
  
  - Add ‘reasoning\_effort’ support - [PR](https://github.com/BerriAI/litellm/pull/11562), [Get Started](https://docs.litellm.ai/docs/providers/perplexity#reasoning-effort)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Add mistral reasoning support - [PR](https://github.com/BerriAI/litellm/pull/11642), [Get Started](https://docs.litellm.ai/docs/providers/mistral#reasoning)
- [**SGLang**](https://docs.litellm.ai/docs/providers/openai_compatible)
  
  - Map context window exceeded error for proper handling - [PR](https://github.com/BerriAI/litellm/pull/11575/)
- [**Deepgram**](https://docs.litellm.ai/docs/providers/deepgram)
  
  - Provider specific params support - [PR](https://github.com/BerriAI/litellm/pull/11638)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Return content safety filter results - [PR](https://github.com/BerriAI/litellm/pull/11655)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**Chat Completion**](https://docs.litellm.ai/docs/completion/input)
  
  - Streaming - Ensure consistent ‘created’ across chunks - [PR](https://github.com/BerriAI/litellm/pull/11528)

#### Features[​](#features-1 "Direct link to Features")

- **MCP**
  
  - Add controls for MCP Permission Management - [PR](https://github.com/BerriAI/litellm/pull/11598), [Docs](https://docs.litellm.ai/docs/mcp#-mcp-permission-management)
  - Add permission management for MCP List + Call Tool operations - [PR](https://github.com/BerriAI/litellm/pull/11682), [Docs](https://docs.litellm.ai/docs/mcp#-mcp-permission-management)
  - Streamable HTTP server support - [PR](https://github.com/BerriAI/litellm/pull/11628), [PR](https://github.com/BerriAI/litellm/pull/11645), [Docs](https://docs.litellm.ai/docs/mcp#using-your-mcp)
  - Use Experimental dedicated Rest endpoints for list, calling MCP tools - [PR](https://github.com/BerriAI/litellm/pull/11684)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - NEW API Endpoint - List input items - [PR](https://github.com/BerriAI/litellm/pull/11602)
  - Background mode for OpenAI + Azure OpenAI - [PR](https://github.com/BerriAI/litellm/pull/11640)
  - Langfuse/other Logging support on responses api requests - [PR](https://github.com/BerriAI/litellm/pull/11685)
- [**Chat Completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Bridge for Responses API - allows calling codex-mini via `/chat/completions` and `/v1/messages` - [PR](https://github.com/BerriAI/litellm/pull/11632), [PR](https://github.com/BerriAI/litellm/pull/11685)

* * *

## Spend Tracking[​](#spend-tracking "Direct link to Spend Tracking")

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- [**End Users**](https://docs.litellm.ai/docs/proxy/customers)
  
  - Update enduser spend and budget reset date based on budget duration - [PR](https://github.com/BerriAI/litellm/pull/8460) (s/o [laurien16](https://github.com/laurien16))
- [**Custom Pricing**](https://docs.litellm.ai/docs/proxy/custom_pricing)
  
  - Convert scientific notation str to int - [PR](https://github.com/BerriAI/litellm/pull/11655)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- [**Users**](https://docs.litellm.ai/docs/proxy/users)
  
  - `/user/info` - fix passing user with `+` in user id
  - Add admin-initiated password reset flow - [PR](https://github.com/BerriAI/litellm/pull/11618)
  - Fixes default user settings UI rendering error - [PR](https://github.com/BerriAI/litellm/pull/11674)
- [**Budgets**](https://docs.litellm.ai/docs/proxy/users)
  
  - Correct success message when new user budget is created - [PR](https://github.com/BerriAI/litellm/pull/11608)

#### Features[​](#features-2 "Direct link to Features")

- **Leftnav**
  
  - Show remaining Enterprise users on UI
- **MCP**
  
  - New server add form - [PR](https://github.com/BerriAI/litellm/pull/11604)
  - Allow editing mcp servers - [PR](https://github.com/BerriAI/litellm/pull/11693)
- **Models**
  
  - Add deepgram models on UI
  - Model Access Group support on UI - [PR](https://github.com/BerriAI/litellm/pull/11719)
- **Keys**
  
  - Trim long user id’s - [PR](https://github.com/BerriAI/litellm/pull/11488)
- **Logs**
  
  - Add live tail feature to logs view, allows user to disable auto refresh in high traffic - [PR](https://github.com/BerriAI/litellm/pull/11712)
  - Audit Logs - preview screenshot - [PR](https://github.com/BerriAI/litellm/pull/11715)

* * *

## Logging / Guardrails Integrations[​](#logging--guardrails-integrations "Direct link to Logging / Guardrails Integrations")

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- [**Arize**](https://docs.litellm.ai/docs/observability/arize_integration)
  
  - Change space\_key header to space\_id - [PR](https://github.com/BerriAI/litellm/pull/11595) (s/o [vanities](https://github.com/vanities))
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Fix total requests increment - [PR](https://github.com/BerriAI/litellm/pull/11718)

#### Features[​](#features-3 "Direct link to Features")

- [**Lasso Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/lasso_security)
  
  - \[NEW] Lasso Guardrails support - [PR](https://github.com/BerriAI/litellm/pull/11565)
- [**Users**](https://docs.litellm.ai/docs/proxy/users)
  
  - New `organizations` param on `/user/new` - allows adding users to orgs on creation - [PR](https://github.com/BerriAI/litellm/pull/11572/files)
- **Prevent double logging when using bridge logic** - [PR](https://github.com/BerriAI/litellm/pull/11687)

* * *

## Performance / Reliability Improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- [**Tag based routing**](https://docs.litellm.ai/docs/proxy/tag_routing)
  
  - Do not consider ‘default’ models when request specifies a tag - [PR](https://github.com/BerriAI/litellm/pull/11454) (s/o [thiagosalvatore](https://github.com/thiagosalvatore))

#### Features[​](#features-4 "Direct link to Features")

- [**Caching**](https://docs.litellm.ai/docs/caching/all_caches)
  
  - New optional ‘litellm\[caching]’ pip install for adding disk cache dependencies - [PR](https://github.com/BerriAI/litellm/pull/11600)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Bugs[​](#bugs-6 "Direct link to Bugs")

- **aiohttp**
  
  - fixes for transfer encoding error on aiohttp transport - [PR](https://github.com/BerriAI/litellm/pull/11561)

#### Features[​](#features-5 "Direct link to Features")

- **aiohttp**
  
  - Enable System Proxy Support for aiohttp transport - [PR](https://github.com/BerriAI/litellm/pull/11616) (s/o [idootop](https://github.com/idootop))
- **CLI**
  
  - Make all commands show server URL - [PR](https://github.com/BerriAI/litellm/pull/10801)
- **Unicorn**
  
  - Allow setting keep alive timeout - [PR](https://github.com/BerriAI/litellm/pull/11594)
- **Experimental Rate Limiting v2** (enable via `EXPERIMENTAL_MULTI_INSTANCE_RATE_LIMITING="True"`)
  
  - Support specifying rate limit by output\_tokens only - [PR](https://github.com/BerriAI/litellm/pull/11646)
  - Decrement parallel requests on call failure - [PR](https://github.com/BerriAI/litellm/pull/11646)
  - In-memory only rate limiting support - [PR](https://github.com/BerriAI/litellm/pull/11646)
  - Return remaining rate limits by key/user/team - [PR](https://github.com/BerriAI/litellm/pull/11646)
- **Helm**
  
  - support extraContainers in migrations-job.yaml - [PR](https://github.com/BerriAI/litellm/pull/11649)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @laurien16 made their first contribution in [https://github.com/BerriAI/litellm/pull/8460](https://github.com/BerriAI/litellm/pull/8460)
- @fengbohello made their first contribution in [https://github.com/BerriAI/litellm/pull/11547](https://github.com/BerriAI/litellm/pull/11547)
- @lapinek made their first contribution in [https://github.com/BerriAI/litellm/pull/11570](https://github.com/BerriAI/litellm/pull/11570)
- @yanwork made their first contribution in [https://github.com/BerriAI/litellm/pull/11586](https://github.com/BerriAI/litellm/pull/11586)
- @dhs-shine made their first contribution in [https://github.com/BerriAI/litellm/pull/11575](https://github.com/BerriAI/litellm/pull/11575)
- @ElefHead made their first contribution in [https://github.com/BerriAI/litellm/pull/11450](https://github.com/BerriAI/litellm/pull/11450)
- @idootop made their first contribution in [https://github.com/BerriAI/litellm/pull/11616](https://github.com/BerriAI/litellm/pull/11616)
- @stevenaldinger made their first contribution in [https://github.com/BerriAI/litellm/pull/11649](https://github.com/BerriAI/litellm/pull/11649)
- @thiagosalvatore made their first contribution in [https://github.com/BerriAI/litellm/pull/11454](https://github.com/BerriAI/litellm/pull/11454)
- @vanities made their first contribution in [https://github.com/BerriAI/litellm/pull/11595](https://github.com/BerriAI/litellm/pull/11595)
- @alvarosevilla95 made their first contribution in [https://github.com/BerriAI/litellm/pull/11661](https://github.com/BerriAI/litellm/pull/11661)

* * *

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## [Git Diff](https://github.com/BerriAI/litellm/compare/v1.72.2-stable...1.72.6.rc)[​](#git-diff "Direct link to git-diff")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.72.2-stable
```

## TLDR[​](#tldr "Direct link to TLDR")

- **Why Upgrade**
  
  - Performance Improvements for /v1/messages: For this endpoint LiteLLM Proxy overhead is now down to 50ms at 250 RPS.
  - Accurate Rate Limiting: Multi-instance rate limiting now tracks rate limits across keys, models, teams, and users with 0 spillover.
  - Audit Logs on UI: Track when Keys, Teams, and Models were deleted by viewing Audit Logs on the LiteLLM UI.
  - /v1/messages all models support: You can now use all LiteLLM models (`gpt-4.1`, `o1-pro`, `gemini-2.5-pro`) with /v1/messages API.
  - [Anthropic MCP](https://docs.litellm.ai/docs/providers/anthropic#mcp-tool-calling): Use remote MCP Servers with Anthropic Models.
- **Who Should Read**
  
  - Teams using `/v1/messages` API (Claude Code)
  - Proxy Admins using LiteLLM Virtual Keys and setting rate limits
- **Risk of Upgrade**
  
  - **Medium**
    
    - Upgraded `ddtrace==3.8.0`, if you use DataDog tracing this is a medium level risk. We recommend monitoring logs for any issues.

* * *

## `/v1/messages` Performance Improvements[​](#v1messages-performance-improvements "Direct link to v1messages-performance-improvements")

This release brings significant performance improvements to the /v1/messages API on LiteLLM.

For this endpoint LiteLLM Proxy overhead latency is now down to 50ms, and each instance can handle 250 RPS. We validated these improvements through load testing with payloads containing over 1,000 streaming chunks.

This is great for real time use cases with large requests (eg. multi turn conversations, Claude Code, etc.).

## Multi-Instance Rate Limiting Improvements[​](#multi-instance-rate-limiting-improvements "Direct link to Multi-Instance Rate Limiting Improvements")

LiteLLM now accurately tracks rate limits across keys, models, teams, and users with 0 spillover.

This is a significant improvement over the previous version, which faced issues with leakage and spillover in high traffic, multi-instance setups.

**Key Changes:**

- Redis is now part of the rate limit check, instead of being a background sync. This ensures accuracy and reduces read/write operations during low activity.
- LiteLLM now uses Lua scripts to ensure all checks are atomic.
- In-memory caching uses Redis values. This prevents drift, and reduces Redis queries once objects are over their limit.

These changes are currently behind the feature flag - `EXPERIMENTAL_ENABLE_MULTI_INSTANCE_RATE_LIMITING=True`. We plan to GA this in our next release - subject to feedback.

## Audit Logs on UI[​](#audit-logs-on-ui "Direct link to Audit Logs on UI")

This release introduces support for viewing audit logs in the UI. As a Proxy Admin, you can now check if and when a key was deleted, along with who performed the action.

LiteLLM tracks changes to the following entities and actions:

- **Entities:** Keys, Teams, Users, Models
- **Actions:** Create, Update, Delete, Regenerate

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

**Newly Added Models**

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)Anthropic`claude-4-opus-20250514`200K$15.00$75.00Anthropic`claude-4-sonnet-20250514`200K$3.00$15.00VertexAI, Google AI Studio`gemini-2.5-pro-preview-06-05`1M$1.25$10.00OpenAI`codex-mini-latest`200K$1.50$6.00Cerebras`qwen-3-32b`128K$0.40$0.80SambaNova`DeepSeek-R1`32K$5.00$7.00SambaNova`DeepSeek-R1-Distill-Llama-70B`131K$0.70$1.40

### Model Updates[​](#model-updates "Direct link to Model Updates")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Cost tracking added for new Claude models - [PR](https://github.com/BerriAI/litellm/pull/11339)
    
    - `claude-4-opus-20250514`
    - `claude-4-sonnet-20250514`
  - Support for MCP tool calling with Anthropic models - [PR](https://github.com/BerriAI/litellm/pull/11474)
- [**Google AI Studio**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Google Gemini 2.5 Pro Preview 06-05 support - [PR](https://github.com/BerriAI/litellm/pull/11447)
  - Gemini streaming thinking content parsing with `reasoning_content` - [PR](https://github.com/BerriAI/litellm/pull/11298)
  - Support for no reasoning option for Gemini models - [PR](https://github.com/BerriAI/litellm/pull/11393)
  - URL context support for Gemini models - [PR](https://github.com/BerriAI/litellm/pull/11351)
  - Gemini embeddings-001 model prices and context window - [PR](https://github.com/BerriAI/litellm/pull/11332)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Cost tracking for `codex-mini-latest` - [PR](https://github.com/BerriAI/litellm/pull/11492)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Cache token tracking on streaming calls - [PR](https://github.com/BerriAI/litellm/pull/11387)
  - Return response\_id matching upstream response ID for stream and non-stream - [PR](https://github.com/BerriAI/litellm/pull/11456)
- [**Cerebras**](https://docs.litellm.ai/docs/providers/cerebras)
  
  - Cerebras/qwen-3-32b model pricing and context window - [PR](https://github.com/BerriAI/litellm/pull/11373)
- [**HuggingFace**](https://docs.litellm.ai/docs/providers/huggingface)
  
  - Fixed embeddings using non-default `input_type` - [PR](https://github.com/BerriAI/litellm/pull/11452)
- [**DataRobot**](https://docs.litellm.ai/docs/providers/datarobot)
  
  - New provider integration for enterprise AI workflows - [PR](https://github.com/BerriAI/litellm/pull/10385)
- [**DeepSeek**](https://docs.litellm.ai/docs/providers/together_ai)
  
  - DeepSeek R1 family model configuration via Together AI - [PR](https://github.com/BerriAI/litellm/pull/11394)
  - DeepSeek R1 pricing and context window configuration - [PR](https://github.com/BerriAI/litellm/pull/11339)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

- [**Images API**](https://docs.litellm.ai/docs/image_generation)
  
  - Azure endpoint support for image endpoints - [PR](https://github.com/BerriAI/litellm/pull/11482)
- [**Anthropic Messages API**](https://docs.litellm.ai/docs/completion/chat)
  
  - Support for ALL LiteLLM Providers (OpenAI, Azure, Bedrock, Vertex, DeepSeek, etc.) on /v1/messages API Spec - [PR](https://github.com/BerriAI/litellm/pull/11502)
  - Performance improvements for /v1/messages route - [PR](https://github.com/BerriAI/litellm/pull/11421)
  - Return streaming usage statistics when using LiteLLM with Bedrock models - [PR](https://github.com/BerriAI/litellm/pull/11469)
- [**Embeddings API**](https://docs.litellm.ai/docs/embedding/supported_embedding)
  
  - Provider-specific optional params handling for embedding calls - [PR](https://github.com/BerriAI/litellm/pull/11346)
  - Proper Sagemaker request attribute usage for embeddings - [PR](https://github.com/BerriAI/litellm/pull/11362)
- [**Rerank API**](https://docs.litellm.ai/docs/rerank/supported_rerank)
  
  - New HuggingFace rerank provider support - [PR](https://github.com/BerriAI/litellm/pull/11438), [Guide](https://docs.litellm.ai/docs/providers/huggingface_rerank)

* * *

## Spend Tracking[​](#spend-tracking "Direct link to Spend Tracking")

- Added token tracking for anthropic batch calls via /anthropic passthrough route- [PR](https://github.com/BerriAI/litellm/pull/11388)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **SSO/Authentication**
  
  - SSO configuration endpoints and UI integration with persistent settings - [PR](https://github.com/BerriAI/litellm/pull/11417)
  - Update proxy admin ID role in DB + Handle SSO redirects with custom root path - [PR](https://github.com/BerriAI/litellm/pull/11384)
  - Support returning virtual key in custom auth - [PR](https://github.com/BerriAI/litellm/pull/11346)
  - User ID validation to ensure it is not an email or phone number - [PR](https://github.com/BerriAI/litellm/pull/10102)
- **Teams**
  
  - Fixed Create/Update team member API 500 error - [PR](https://github.com/BerriAI/litellm/pull/10479)
  - Enterprise feature gating for RegenerateKeyModal in KeyInfoView - [PR](https://github.com/BerriAI/litellm/pull/11400)
- **SCIM**
  
  - Fixed SCIM running patch operation case sensitivity - [PR](https://github.com/BerriAI/litellm/pull/11335)
- **General**
  
  - Converted action buttons to sticky footer action buttons - [PR](https://github.com/BerriAI/litellm/pull/11293)
  - Custom Server Root Path - support for serving UI on a custom root path - [Guide](https://docs.litellm.ai/docs/proxy/custom_root_ui)

* * *

## Logging / Guardrails Integrations[​](#logging--guardrails-integrations "Direct link to Logging / Guardrails Integrations")

#### Logging[​](#logging "Direct link to Logging")

- [**S3**](https://docs.litellm.ai/docs/proxy/logging#s3)
  
  - Async + Batched S3 Logging for improved performance - [PR](https://github.com/BerriAI/litellm/pull/11340)
- [**DataDog**](https://docs.litellm.ai/docs/observability/datadog_integration)
  
  - Add instrumentation for streaming chunks - [PR](https://github.com/BerriAI/litellm/pull/11338)
  - Add DD profiler to monitor Python profile of LiteLLM CPU% - [PR](https://github.com/BerriAI/litellm/pull/11375)
  - Bump DD trace version - [PR](https://github.com/BerriAI/litellm/pull/11426)
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Pass custom metadata labels in litellm\_total\_token metrics - [PR](https://github.com/BerriAI/litellm/pull/11414)
- [**GCS**](https://docs.litellm.ai/docs/proxy/logging#google-cloud-storage)
  
  - Update GCSBucketBase to handle GSM project ID if passed - [PR](https://github.com/BerriAI/litellm/pull/11409)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**Presidio**](https://docs.litellm.ai/docs/proxy/guardrails/presidio)
  
  - Add presidio\_language yaml configuration support for guardrails - [PR](https://github.com/BerriAI/litellm/pull/11331)

* * *

## Performance / Reliability Improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

- **Performance Optimizations**
  
  - Don't run auth on /health/liveliness endpoints - [PR](https://github.com/BerriAI/litellm/pull/11378)
  - Don't create 1 task for every hanging request alert - [PR](https://github.com/BerriAI/litellm/pull/11385)
  - Add debugging endpoint to track active /asyncio-tasks - [PR](https://github.com/BerriAI/litellm/pull/11382)
  - Make batch size for maximum retention in spend logs controllable - [PR](https://github.com/BerriAI/litellm/pull/11459)
  - Expose flag to disable token counter - [PR](https://github.com/BerriAI/litellm/pull/11344)
  - Support pipeline redis lpop for older redis versions - [PR](https://github.com/BerriAI/litellm/pull/11425)

* * *

## Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- **LLM API Fixes**
  
  - **Anthropic**: Fix regression when passing file url's to the 'file\_id' parameter - [PR](https://github.com/BerriAI/litellm/pull/11387)
  - **Vertex AI**: Fix Vertex AI any\_of issues for Description and Default. - [PR](https://github.com/BerriAI/litellm/issues/11383)
  - Fix transcription model name mapping - [PR](https://github.com/BerriAI/litellm/pull/11333)
  - **Image Generation**: Fix None values in usage field for gpt-image-1 model responses - [PR](https://github.com/BerriAI/litellm/pull/11448)
  - **Responses API**: Fix \_transform\_responses\_api\_content\_to\_chat\_completion\_content doesn't support file content type - [PR](https://github.com/BerriAI/litellm/pull/11494)
  - **Fireworks AI**: Fix rate limit exception mapping - detect "rate limit" text in error messages - [PR](https://github.com/BerriAI/litellm/pull/11455)
- **Spend Tracking/Budgets**
  
  - Respect user\_header\_name property for budget selection and user identification - [PR](https://github.com/BerriAI/litellm/pull/11419)
- **MCP Server**
  
  - Remove duplicate server\_id MCP config servers - [PR](https://github.com/BerriAI/litellm/pull/11327)
- **Function Calling**
  
  - supports\_function\_calling works with llm\_proxy models - [PR](https://github.com/BerriAI/litellm/pull/11381)
- **Knowledge Base**
  
  - Fixed Knowledge Base Call returning error - [PR](https://github.com/BerriAI/litellm/pull/11467)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- [@mjnitz02](https://github.com/mjnitz02) made their first contribution in [#10385](https://github.com/BerriAI/litellm/pull/10385)
- [@hagan](https://github.com/hagan) made their first contribution in [#10479](https://github.com/BerriAI/litellm/pull/10479)
- [@wwells](https://github.com/wwells) made their first contribution in [#11409](https://github.com/BerriAI/litellm/pull/11409)
- [@likweitan](https://github.com/likweitan) made their first contribution in [#11400](https://github.com/BerriAI/litellm/pull/11400)
- [@raz-alon](https://github.com/raz-alon) made their first contribution in [#10102](https://github.com/BerriAI/litellm/pull/10102)
- [@jtsai-quid](https://github.com/jtsai-quid) made their first contribution in [#11394](https://github.com/BerriAI/litellm/pull/11394)
- [@tmbo](https://github.com/tmbo) made their first contribution in [#11362](https://github.com/BerriAI/litellm/pull/11362)
- [@wangsha](https://github.com/wangsha) made their first contribution in [#11351](https://github.com/BerriAI/litellm/pull/11351)
- [@seankwalker](https://github.com/seankwalker) made their first contribution in [#11452](https://github.com/BerriAI/litellm/pull/11452)
- [@pazevedo-hyland](https://github.com/pazevedo-hyland) made their first contribution in [#11381](https://github.com/BerriAI/litellm/pull/11381)
- [@cainiaoit](https://github.com/cainiaoit) made their first contribution in [#11438](https://github.com/BerriAI/litellm/pull/11438)
- [@vuanhtu52](https://github.com/vuanhtu52) made their first contribution in [#11508](https://github.com/BerriAI/litellm/pull/11508)

* * *

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## [Git Diff](https://github.com/BerriAI/litellm/releases/tag/v1.72.2-stable)[​](#git-diff "Direct link to git-diff")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.72.0-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

LiteLLM v1.72.0-stable.rc is live now. Here are the key highlights of this release:

- **Vector Store Permissions**: Control Vector Store access at the Key, Team, and Organization level.
- **Rate Limiting Sliding Window support**: Improved accuracy for Key/Team/User rate limits with request tracking across minutes.
- **Aiohttp Transport used by default**: Aiohttp transport is now the default transport for LiteLLM networking requests. This gives users 2x higher RPS per instance with a 40ms median latency overhead.
- **Bedrock Agents**: Call Bedrock Agents with `/chat/completions`, `/response` endpoints.
- **Anthropic File API**: Upload and analyze CSV files with Claude-4 on Anthropic via LiteLLM.
- **Prometheus**: End users (`end_user`) will no longer be tracked by default on Prometheus. Tracking end\_users on prometheus is now opt-in. This is done to prevent the response from `/metrics` from becoming too large. [Read More](https://docs.litellm.ai/docs/proxy/prometheus#tracking-end_user-on-prometheus)

* * *

## Vector Store Permissions[​](#vector-store-permissions "Direct link to Vector Store Permissions")

This release brings support for managing permissions for vector stores by Keys, Teams, Organizations (entities) on LiteLLM. When a request attempts to query a vector store, LiteLLM will block it if the requesting entity lacks the proper permissions.

This is great for use cases that require access to restricted data that you don't want everyone to use.

Over the next week we plan on adding permission management for MCP Servers.

* * *

## Aiohttp Transport used by default[​](#aiohttp-transport-used-by-default "Direct link to Aiohttp Transport used by default")

Aiohttp transport is now the default transport for LiteLLM networking requests. This gives users 2x higher RPS per instance with a 40ms median latency overhead. This has been live on LiteLLM Cloud for a week + gone through alpha users testing for a week.

If you encounter any issues, you can disable using the aiohttp transport in the following ways:

**On LiteLLM Proxy**

Set the `DISABLE_AIOHTTP_TRANSPORT=True` in the environment variables.

Environment Variable

```
export DISABLE_AIOHTTP_TRANSPORT="True"
```

**On LiteLLM Python SDK**

Set the `disable_aiohttp_transport=True` to disable aiohttp transport.

Python SDK

```
import litellm

litellm.disable_aiohttp_transport =True# default is False, enable this to disable aiohttp transport
result = litellm.completion(
    model="openai/gpt-4o",
    messages=[{"role":"user","content":"Hello, world!"}],
)
print(result)
```

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Video support for Bedrock Converse - [PR](https://github.com/BerriAI/litellm/pull/11166)
  - InvokeAgents support as /chat/completions route - [PR](https://github.com/BerriAI/litellm/pull/11239), [Get Started](https://docs.litellm.ai/docs/providers/bedrock_agents)
  - AI21 Jamba models compatibility fixes - [PR](https://github.com/BerriAI/litellm/pull/11233)
  - Fixed duplicate maxTokens parameter for Claude with thinking - [PR](https://github.com/BerriAI/litellm/pull/11181)
- [**Gemini (Google AI Studio + Vertex AI)**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Parallel tool calling support with `parallel_tool_calls` parameter - [PR](https://github.com/BerriAI/litellm/pull/11125)
  - All Gemini models now support parallel function calling - [PR](https://github.com/BerriAI/litellm/pull/11225)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - codeExecution tool support and anyOf handling - [PR](https://github.com/BerriAI/litellm/pull/11195)
  - Vertex AI Anthropic support on /v1/messages - [PR](https://github.com/BerriAI/litellm/pull/11246)
  - Thinking, global regions, and parallel tool calling improvements - [PR](https://github.com/BerriAI/litellm/pull/11194)
  - Web Search Support [PR](https://github.com/BerriAI/litellm/commit/06484f6e5a7a2f4e45c490266782ed28b51b7db6)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Thinking blocks on streaming support - [PR](https://github.com/BerriAI/litellm/pull/11194)
  - Files API with form-data support on passthrough - [PR](https://github.com/BerriAI/litellm/pull/11256)
  - File ID support on /chat/completion - [PR](https://github.com/BerriAI/litellm/pull/11256)
- [**xAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - Web Search Support [PR](https://github.com/BerriAI/litellm/commit/06484f6e5a7a2f4e45c490266782ed28b51b7db6)
- [**Google AI Studio**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Web Search Support [PR](https://github.com/BerriAI/litellm/commit/06484f6e5a7a2f4e45c490266782ed28b51b7db6)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Updated mistral-medium prices and context sizes - [PR](https://github.com/BerriAI/litellm/pull/10729)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Tool calls parsing on streaming - [PR](https://github.com/BerriAI/litellm/pull/11171)
- [**Cohere**](https://docs.litellm.ai/docs/providers/cohere)
  
  - Swapped Cohere and Cohere Chat provider positioning - [PR](https://github.com/BerriAI/litellm/pull/11173)
- [**Nebius AI Studio**](https://docs.litellm.ai/docs/providers/nebius)
  
  - New provider integration - [PR](https://github.com/BerriAI/litellm/pull/11143)

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

- [**Image Edits API**](https://docs.litellm.ai/docs/image_generation)
  
  - Azure support for /v1/images/edits - [PR](https://github.com/BerriAI/litellm/pull/11160)
  - Cost tracking for image edits endpoint (OpenAI, Azure) - [PR](https://github.com/BerriAI/litellm/pull/11186)
- [**Completions API**](https://docs.litellm.ai/docs/completion/chat)
  
  - Codestral latency overhead tracking on /v1/completions - [PR](https://github.com/BerriAI/litellm/pull/10879)
- [**Audio Transcriptions API**](https://docs.litellm.ai/docs/audio/speech)
  
  - GPT-4o mini audio preview pricing without date - [PR](https://github.com/BerriAI/litellm/pull/11207)
  - Non-default params support for audio transcription - [PR](https://github.com/BerriAI/litellm/pull/11212)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Session management fixes for using Non-OpenAI models - [PR](https://github.com/BerriAI/litellm/pull/11254)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Vector Stores**
  
  - Permission management for LiteLLM Keys, Teams, and Organizations - [PR](https://github.com/BerriAI/litellm/pull/11213)
  - UI display of vector store permissions - [PR](https://github.com/BerriAI/litellm/pull/11277)
  - Vector store access controls enforcement - [PR](https://github.com/BerriAI/litellm/pull/11281)
  - Object permissions fixes and QA improvements - [PR](https://github.com/BerriAI/litellm/pull/11291)
- **Teams**
  
  - "All proxy models" display when no models selected - [PR](https://github.com/BerriAI/litellm/pull/11187)
  - Removed redundant teamInfo call, using existing teamsList - [PR](https://github.com/BerriAI/litellm/pull/11051)
  - Improved model tags display on Keys, Teams and Org pages - [PR](https://github.com/BerriAI/litellm/pull/11022)
- **SSO/SCIM**
  
  - Bug fixes for showing SCIM token on UI - [PR](https://github.com/BerriAI/litellm/pull/11220)
- **General UI**
  
  - Fix "UI Session Expired. Logging out" - [PR](https://github.com/BerriAI/litellm/pull/11279)
  - Support for forwarding /sso/key/generate to server root path URL - [PR](https://github.com/BerriAI/litellm/pull/11165)

## Logging / Guardrails Integrations[​](#logging--guardrails-integrations "Direct link to Logging / Guardrails Integrations")

#### Logging[​](#logging "Direct link to Logging")

- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - End users will no longer be tracked by default on Prometheus. Tracking end\_users on prometheus is now opt-in. [PR](https://github.com/BerriAI/litellm/pull/11192)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Performance improvements: Fixed "Max langfuse clients reached" issue - [PR](https://github.com/BerriAI/litellm/pull/11285)
- [**Helicone**](https://docs.litellm.ai/docs/observability/helicone_integration)
  
  - Base URL support - [PR](https://github.com/BerriAI/litellm/pull/11211)
- [**Sentry**](https://docs.litellm.ai/docs/proxy/logging#sentry)
  
  - Added sentry sample rate configuration - [PR](https://github.com/BerriAI/litellm/pull/10283)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/bedrock)
  
  - Streaming support for bedrock post guard - [PR](https://github.com/BerriAI/litellm/pull/11247)
  - Auth parameter persistence fixes - [PR](https://github.com/BerriAI/litellm/pull/11270)
- [**Pangea Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/pangea)
  
  - Added Pangea provider to Guardrails hook - [PR](https://github.com/BerriAI/litellm/pull/10775)

## Performance / Reliability Improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

- **aiohttp Transport**
  
  - Handling for aiohttp.ClientPayloadError - [PR](https://github.com/BerriAI/litellm/pull/11162)
  - SSL verification settings support - [PR](https://github.com/BerriAI/litellm/pull/11162)
  - Rollback to httpx==0.27.0 for stability - [PR](https://github.com/BerriAI/litellm/pull/11146)
- **Request Limiting**
  
  - Sliding window logic for parallel request limiter v2 - [PR](https://github.com/BerriAI/litellm/pull/11283)

## Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- **LLM API Fixes**
  
  - Added missing request\_kwargs to get\_available\_deployment call - [PR](https://github.com/BerriAI/litellm/pull/11202)
  - Fixed calling Azure O-series models - [PR](https://github.com/BerriAI/litellm/pull/11212)
  - Support for dropping non-OpenAI params via additional\_drop\_params - [PR](https://github.com/BerriAI/litellm/pull/11246)
  - Fixed frequency\_penalty to repeat\_penalty parameter mapping - [PR](https://github.com/BerriAI/litellm/pull/11284)
  - Fix for embedding cache hits on string input - [PR](https://github.com/BerriAI/litellm/pull/11211)
- **General**
  
  - OIDC provider improvements and audience bug fix - [PR](https://github.com/BerriAI/litellm/pull/10054)
  - Removed AzureCredentialType restriction on AZURE\_CREDENTIAL - [PR](https://github.com/BerriAI/litellm/pull/11272)
  - Prevention of sensitive key leakage to Langfuse - [PR](https://github.com/BerriAI/litellm/pull/11165)
  - Fixed healthcheck test using curl when curl not in image - [PR](https://github.com/BerriAI/litellm/pull/9737)

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- [@agajdosi](https://github.com/agajdosi) made their first contribution in [#9737](https://github.com/BerriAI/litellm/pull/9737)
- [@ketangangal](https://github.com/ketangangal) made their first contribution in [#11161](https://github.com/BerriAI/litellm/pull/11161)
- [@Aktsvigun](https://github.com/Aktsvigun) made their first contribution in [#11143](https://github.com/BerriAI/litellm/pull/11143)
- [@ryanmeans](https://github.com/ryanmeans) made their first contribution in [#10775](https://github.com/BerriAI/litellm/pull/10775)
- [@nikoizs](https://github.com/nikoizs) made their first contribution in [#10054](https://github.com/BerriAI/litellm/pull/10054)
- [@Nitro963](https://github.com/Nitro963) made their first contribution in [#11202](https://github.com/BerriAI/litellm/pull/11202)
- [@Jacobh2](https://github.com/Jacobh2) made their first contribution in [#11207](https://github.com/BerriAI/litellm/pull/11207)
- [@regismesquita](https://github.com/regismesquita) made their first contribution in [#10729](https://github.com/BerriAI/litellm/pull/10729)
- [@Vinnie-Singleton-NN](https://github.com/Vinnie-Singleton-NN) made their first contribution in [#10283](https://github.com/BerriAI/litellm/pull/10283)
- [@trashhalo](https://github.com/trashhalo) made their first contribution in [#11219](https://github.com/BerriAI/litellm/pull/11219)
- [@VigneshwarRajasekaran](https://github.com/VigneshwarRajasekaran) made their first contribution in [#11223](https://github.com/BerriAI/litellm/pull/11223)
- [@AnilAren](https://github.com/AnilAren) made their first contribution in [#11233](https://github.com/BerriAI/litellm/pull/11233)
- [@fadil4u](https://github.com/fadil4u) made their first contribution in [#11242](https://github.com/BerriAI/litellm/pull/11242)
- [@whitfin](https://github.com/whitfin) made their first contribution in [#11279](https://github.com/BerriAI/litellm/pull/11279)
- [@hcoona](https://github.com/hcoona) made their first contribution in [#11272](https://github.com/BerriAI/litellm/pull/11272)
- [@keyute](https://github.com/keyute) made their first contribution in [#11173](https://github.com/BerriAI/litellm/pull/11173)
- [@emmanuel-ferdman](https://github.com/emmanuel-ferdman) made their first contribution in [#11230](https://github.com/BerriAI/litellm/pull/11230)

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## [Git Diff](https://github.com/BerriAI/litellm/releases)[​](#git-diff "Direct link to git-diff")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.71.1-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

LiteLLM v1.71.1-stable is live now. Here are the key highlights of this release:

- **Performance improvements**: LiteLLM can now scale to 200 RPS per instance with a 74ms median response time.
- **File Permissions**: Control file access across OpenAI, Azure, VertexAI.
- **MCP x OpenAI**: Use MCP servers with OpenAI Responses API.

## Performance Improvements[​](#performance-improvements "Direct link to Performance Improvements")

This release brings aiohttp support for all LLM api providers. This means that LiteLLM can now scale to 200 RPS per instance with a 40ms median latency overhead.

This change doubles the RPS LiteLLM can scale to at this latency overhead.

You can opt into this by enabling the flag below. (We expect to make this the default in 1 week.)

### Flag to enable[​](#flag-to-enable "Direct link to Flag to enable")

**On LiteLLM Proxy**

Set the `USE_AIOHTTP_TRANSPORT=True` in the environment variables.

Environment Variable

```
export USE_AIOHTTP_TRANSPORT="True"
```

**On LiteLLM Python SDK**

Set the `use_aiohttp_transport=True` to enable aiohttp transport.

Python SDK

```
import litellm

litellm.use_aiohttp_transport =True# default is False, enable this to use aiohttp transport
result = litellm.completion(
    model="openai/gpt-4o",
    messages=[{"role":"user","content":"Hello, world!"}],
)
print(result)
```

## File Permissions[​](#file-permissions "Direct link to File Permissions")

This release brings support for [File Permissions](https://docs.litellm.ai/docs/proxy/litellm_managed_files#file-permissions) and [Finetuning APIs](https://docs.litellm.ai/docs/proxy/managed_finetuning) to [LiteLLM Managed Files](https://docs.litellm.ai/docs/proxy/litellm_managed_files). This is great for:

- **Proxy Admins**: as users can only view/edit/delete files they’ve created - even when using shared OpenAI/Azure/Vertex deployments.
- **Developers**: get a standard interface to use Files across Chat/Finetuning/Batch APIs.

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **Gemini [VertexAI](https://docs.litellm.ai/docs/providers/vertex), [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini)**
  
  - New gemini models - [PR 1](https://github.com/BerriAI/litellm/pull/10991), [PR 2](https://github.com/BerriAI/litellm/pull/10998)
    
    - `gemini-2.5-flash-preview-tts`
    - `gemini-2.0-flash-preview-image-generation`
    - `gemini/gemini-2.5-flash-preview-05-20`
    - `gemini-2.5-flash-preview-05-20`
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Claude-4 model family support - [PR](https://github.com/BerriAI/litellm/pull/11060)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Claude-4 model family support - [PR](https://github.com/BerriAI/litellm/pull/11060)
  - Support for `reasoning_effort` and `thinking` parameters for Claude-4 - [PR](https://github.com/BerriAI/litellm/pull/11114)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Claude-4 model family support - [PR](https://github.com/BerriAI/litellm/pull/11060)
  - Global endpoints support - [PR](https://github.com/BerriAI/litellm/pull/10658)
  - authorized\_user credentials type support - [PR](https://github.com/BerriAI/litellm/pull/10899)
- [**xAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - `xai/grok-3` pricing information - [PR](https://github.com/BerriAI/litellm/pull/11028)
- [**LM Studio**](https://docs.litellm.ai/docs/providers/lm_studio)
  
  - Structured JSON schema outputs support - [PR](https://github.com/BerriAI/litellm/pull/10929)
- [**SambaNova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Updated models and parameters - [PR](https://github.com/BerriAI/litellm/pull/10900)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks)
  
  - Llama 4 Maverick model cost - [PR](https://github.com/BerriAI/litellm/pull/11008)
  - Claude 3.7 Sonnet output token cost correction - [PR](https://github.com/BerriAI/litellm/pull/11007)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Mistral Medium 25.05 support - [PR](https://github.com/BerriAI/litellm/pull/11063)
  - Certificate-based authentication support - [PR](https://github.com/BerriAI/litellm/pull/11069)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - devstral-small-2505 model pricing and context window - [PR](https://github.com/BerriAI/litellm/pull/11103)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Wildcard model support - [PR](https://github.com/BerriAI/litellm/pull/10982)
- [**CustomLLM**](https://docs.litellm.ai/docs/providers/custom_llm_server)
  
  - Embeddings support added - [PR](https://github.com/BerriAI/litellm/pull/10980)
- [**Featherless AI**](https://docs.litellm.ai/docs/providers/featherless_ai)
  
  - Access to 4200+ models - [PR](https://github.com/BerriAI/litellm/pull/10596)

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

- [**Image Edits**](https://docs.litellm.ai/docs/image_generation)
  
  - `/v1/images/edits` - Support for /images/edits endpoint - [PR](https://github.com/BerriAI/litellm/pull/11020) [PR](https://github.com/BerriAI/litellm/pull/11123)
  - Content policy violation error mapping - [PR](https://github.com/BerriAI/litellm/pull/11113)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - MCP support for Responses API - [PR](https://github.com/BerriAI/litellm/pull/11029)
- [**Files API**](https://docs.litellm.ai/docs/fine_tuning)
  
  - LiteLLM Managed Files support for finetuning - [PR](https://github.com/BerriAI/litellm/pull/11039) [PR](https://github.com/BerriAI/litellm/pull/11040)
  - Validation for file operations (retrieve/list/delete) - [PR](https://github.com/BerriAI/litellm/pull/11081)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Teams**
  
  - Key and member count display - [PR](https://github.com/BerriAI/litellm/pull/10950)
  - Spend rounded to 4 decimal points - [PR](https://github.com/BerriAI/litellm/pull/11013)
  - Organization and team create buttons repositioned - [PR](https://github.com/BerriAI/litellm/pull/10948)
- **Keys**
  
  - Key reassignment and 'updated at' column - [PR](https://github.com/BerriAI/litellm/pull/10960)
  - Show model access groups during creation - [PR](https://github.com/BerriAI/litellm/pull/10965)
- **Logs**
  
  - Model filter on logs - [PR](https://github.com/BerriAI/litellm/pull/11048)
  - Passthrough endpoint error logs support - [PR](https://github.com/BerriAI/litellm/pull/10990)
- **Guardrails**
  
  - Config.yaml guardrails display - [PR](https://github.com/BerriAI/litellm/pull/10959)
- **Organizations/Users**
  
  - Spend rounded to 4 decimal points - [PR](https://github.com/BerriAI/litellm/pull/11023)
  - Show clear error when adding a user to a team - [PR](https://github.com/BerriAI/litellm/pull/10978)
- **Audit Logs**
  
  - `/list` and `/info` endpoints for Audit Logs - [PR](https://github.com/BerriAI/litellm/pull/11102)

## Logging / Alerting Integrations[​](#logging--alerting-integrations "Direct link to Logging / Alerting Integrations")

- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Track `route` on proxy\_* metrics - [PR](https://github.com/BerriAI/litellm/pull/10992)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Support for `prompt_label` parameter - [PR](https://github.com/BerriAI/litellm/pull/11018)
  - Consistent modelParams logging - [PR](https://github.com/BerriAI/litellm/pull/11018)
- [**DeepEval/ConfidentAI**](https://docs.litellm.ai/docs/proxy/logging#deepeval)
  
  - Logging enabled for proxy and SDK - [PR](https://github.com/BerriAI/litellm/pull/10649)
- [**Logfire**](https://docs.litellm.ai/docs/proxy/logging)
  
  - Fix otel proxy server initialization when using Logfire - [PR](https://github.com/BerriAI/litellm/pull/11091)

## Authentication & Security[​](#authentication--security "Direct link to Authentication & Security")

- [**JWT Authentication**](https://docs.litellm.ai/docs/proxy/token_auth)
  
  - Support for applying default internal user parameters when upserting a user via JWT authentication - [PR](https://github.com/BerriAI/litellm/pull/10995)
  - Map a user to a team when upserting a user via JWT authentication - [PR](https://github.com/BerriAI/litellm/pull/11108)
- **Custom Auth**
  
  - Support for switching between custom auth and API key auth - [PR](https://github.com/BerriAI/litellm/pull/11070)

## Performance / Reliability Improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

- **aiohttp Transport**
  
  - 97% lower median latency (feature flagged) - [PR](https://github.com/BerriAI/litellm/pull/11097) [PR](https://github.com/BerriAI/litellm/pull/11132)
- **Background Health Checks**
  
  - Improved reliability - [PR](https://github.com/BerriAI/litellm/pull/10887)
- **Response Handling**
  
  - Better streaming status code detection - [PR](https://github.com/BerriAI/litellm/pull/10962)
  - Response ID propagation improvements - [PR](https://github.com/BerriAI/litellm/pull/11006)
- **Thread Management**
  
  - Removed error-creating threads for reliability - [PR](https://github.com/BerriAI/litellm/pull/11066)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- [**Proxy CLI**](https://docs.litellm.ai/docs/proxy/cli)
  
  - Skip server startup flag - [PR](https://github.com/BerriAI/litellm/pull/10665)
  - Avoid DATABASE\_URL override when provided - [PR](https://github.com/BerriAI/litellm/pull/11076)
- **Model Management**
  
  - Clear cache and reload after model updates - [PR](https://github.com/BerriAI/litellm/pull/10853)
  - Computer use support tracking - [PR](https://github.com/BerriAI/litellm/pull/10881)
- **Helm Chart**
  
  - LoadBalancer class support - [PR](https://github.com/BerriAI/litellm/pull/11064)

## Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

This release includes numerous bug fixes to improve stability and reliability:

- **LLM Provider Fixes**
  
  - VertexAI:
    
    - Fixed quota\_project\_id parameter issue - [PR](https://github.com/BerriAI/litellm/pull/10915)
    - Fixed credential refresh exceptions - [PR](https://github.com/BerriAI/litellm/pull/10969)
  - Cohere: Fixes for adding Cohere models through LiteLLM UI - [PR](https://github.com/BerriAI/litellm/pull/10822)
  - Anthropic:
    
    - Fixed streaming dict object handling for /v1/messages - [PR](https://github.com/BerriAI/litellm/pull/11032)
  - OpenRouter:
    
    - Fixed stream usage ID issues - [PR](https://github.com/BerriAI/litellm/pull/11004)
- **Authentication & Users**
  
  - Fixed invitation email link generation - [PR](https://github.com/BerriAI/litellm/pull/10958)
  - Fixed JWT authentication default role - [PR](https://github.com/BerriAI/litellm/pull/10995)
  - Fixed user budget reset functionality - [PR](https://github.com/BerriAI/litellm/pull/10993)
  - Fixed SSO user compatibility and email validation - [PR](https://github.com/BerriAI/litellm/pull/11106)
- **Database & Infrastructure**
  
  - Fixed DB connection parameter handling - [PR](https://github.com/BerriAI/litellm/pull/10842)
  - Fixed email invitation link - [PR](https://github.com/BerriAI/litellm/pull/11031)
- **UI & Display**
  
  - Fixed MCP tool rendering when no arguments required - [PR](https://github.com/BerriAI/litellm/pull/11012)
  - Fixed team model alias deletion - [PR](https://github.com/BerriAI/litellm/pull/11121)
  - Fixed team viewer permissions - [PR](https://github.com/BerriAI/litellm/pull/11127)
- **Model & Routing**
  
  - Fixed team model mapping in route requests - [PR](https://github.com/BerriAI/litellm/pull/11111)
  - Fixed standard optional parameter passing - [PR](https://github.com/BerriAI/litellm/pull/11124)

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- [@DarinVerheijke](https://github.com/DarinVerheijke) made their first contribution in PR [#10596](https://github.com/BerriAI/litellm/pull/10596)
- [@estsauver](https://github.com/estsauver) made their first contribution in PR [#10929](https://github.com/BerriAI/litellm/pull/10929)
- [@mohittalele](https://github.com/mohittalele) made their first contribution in PR [#10665](https://github.com/BerriAI/litellm/pull/10665)
- [@pselden](https://github.com/pselden) made their first contribution in PR [#10899](https://github.com/BerriAI/litellm/pull/10899)
- [@unrealandychan](https://github.com/unrealandychan) made their first contribution in PR [#10842](https://github.com/BerriAI/litellm/pull/10842)
- [@dastaiger](https://github.com/dastaiger) made their first contribution in PR [#10946](https://github.com/BerriAI/litellm/pull/10946)
- [@slytechnical](https://github.com/slytechnical) made their first contribution in PR [#10881](https://github.com/BerriAI/litellm/pull/10881)
- [@daarko10](https://github.com/daarko10) made their first contribution in PR [#11006](https://github.com/BerriAI/litellm/pull/11006)
- [@sorenmat](https://github.com/sorenmat) made their first contribution in PR [#10658](https://github.com/BerriAI/litellm/pull/10658)
- [@matthid](https://github.com/matthid) made their first contribution in PR [#10982](https://github.com/BerriAI/litellm/pull/10982)
- [@jgowdy-godaddy](https://github.com/jgowdy-godaddy) made their first contribution in PR [#11032](https://github.com/BerriAI/litellm/pull/11032)
- [@bepotp](https://github.com/bepotp) made their first contribution in PR [#11008](https://github.com/BerriAI/litellm/pull/11008)
- [@jmorenoc-o](https://github.com/jmorenoc-o) made their first contribution in PR [#11031](https://github.com/BerriAI/litellm/pull/11031)
- [@martin-liu](https://github.com/martin-liu) made their first contribution in PR [#11076](https://github.com/BerriAI/litellm/pull/11076)
- [@gunjan-solanki](https://github.com/gunjan-solanki) made their first contribution in PR [#11064](https://github.com/BerriAI/litellm/pull/11064)
- [@tokoko](https://github.com/tokoko) made their first contribution in PR [#10980](https://github.com/BerriAI/litellm/pull/10980)
- [@spike-spiegel-21](https://github.com/spike-spiegel-21) made their first contribution in PR [#10649](https://github.com/BerriAI/litellm/pull/10649)
- [@kreatoo](https://github.com/kreatoo) made their first contribution in PR [#10927](https://github.com/BerriAI/litellm/pull/10927)
- [@baejooc](https://github.com/baejooc) made their first contribution in PR [#10887](https://github.com/BerriAI/litellm/pull/10887)
- [@keykbd](https://github.com/keykbd) made their first contribution in PR [#11114](https://github.com/BerriAI/litellm/pull/11114)
- [@dalssoft](https://github.com/dalssoft) made their first contribution in PR [#11088](https://github.com/BerriAI/litellm/pull/11088)
- [@jtong99](https://github.com/jtong99) made their first contribution in PR [#10853](https://github.com/BerriAI/litellm/pull/10853)

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## [Git Diff](https://github.com/BerriAI/litellm/releases)[​](#git-diff "Direct link to git-diff")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.70.1-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

LiteLLM v1.70.1-stable is live now. Here are the key highlights of this release:

- **Gemini Realtime API**: You can now call Gemini's Live API via the OpenAI /v1/realtime API
- **Spend Logs Retention Period**: Enable deleting spend logs older than a certain period.
- **PII Masking 2.0**: Easily configure masking or blocking specific PII/PHI entities on the UI

## Gemini Realtime API[​](#gemini-realtime-api "Direct link to Gemini Realtime API")

This release brings support for calling Gemini's realtime models (e.g. gemini-2.0-flash-live) via OpenAI's /v1/realtime API. This is great for developers as it lets them easily switch from OpenAI to Gemini by just changing the model name.

Key Highlights:

- Support for text + audio input/output
- Support for setting session configurations (modality, instructions, activity detection) in the OpenAI format
- Support for logging + usage tracking for realtime sessions

This is currently supported via Google AI Studio. We plan to release VertexAI support over the coming week.

[**Read more**](https://docs.litellm.ai/docs/providers/google_ai_studio/realtime)

## Spend Logs Retention Period[​](#spend-logs-retention-period "Direct link to Spend Logs Retention Period")

This release enables deleting LiteLLM Spend Logs older than a certain period. Since we now enable storing the raw request/response in the logs, deleting old logs ensures the database remains performant in production.

[**Read more**](https://docs.litellm.ai/docs/proxy/spend_logs_deletion)

## PII Masking 2.0[​](#pii-masking-20 "Direct link to PII Masking 2.0")

This release brings improvements to our Presidio PII Integration. As a Proxy Admin, you now have the ability to:

- Mask or block specific entities (e.g., block medical licenses while masking other entities like emails).
- Monitor guardrails in production. LiteLLM Logs will now show you the guardrail run, the entities it detected, and its confidence score for each entity.

[**Read more**](https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **Gemini ([VertexAI](https://docs.litellm.ai/docs/providers/vertex#usage-with-litellm-proxy-server) + [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini))**
  
  - `/chat/completion`
    
    - Handle audio input - [PR](https://github.com/BerriAI/litellm/pull/10739)
    - Fixes maximum recursion depth issue when using deeply nested response schemas with Vertex AI by Increasing DEFAULT\_MAX\_RECURSE\_DEPTH from 10 to 100 in constants. [PR](https://github.com/BerriAI/litellm/pull/10798)
    - Capture reasoning tokens in streaming mode - [PR](https://github.com/BerriAI/litellm/pull/10789)
- [**Google AI Studio**](https://docs.litellm.ai/docs/providers/google_ai_studio/realtime)
  
  - `/realtime`
    
    - Gemini Multimodal Live API support
    - Audio input/output support, optional param mapping, accurate usage calculation - [PR](https://github.com/BerriAI/litellm/pull/10909)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex#metallama-api)
  
  - `/chat/completion`
    
    - Fix llama streaming error - where model response was nested in returned streaming chunk - [PR](https://github.com/BerriAI/litellm/pull/10878)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - `/chat/completion`
    
    - structure responses fix - [PR](https://github.com/BerriAI/litellm/pull/10617)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock#litellm-proxy-usage)
  
  - [`/chat/completion`](https://docs.litellm.ai/docs/providers/bedrock#litellm-proxy-usage)
    
    - Handle thinking\_blocks when assistant.content is None - [PR](https://github.com/BerriAI/litellm/pull/10688)
    - Fixes to only allow accepted fields for tool json schema - [PR](https://github.com/BerriAI/litellm/pull/10062)
    - Add bedrock sonnet prompt caching cost information
    - Mistral Pixtral support - [PR](https://github.com/BerriAI/litellm/pull/10439)
    - Tool caching support - [PR](https://github.com/BerriAI/litellm/pull/10897)
  - [`/messages`](https://docs.litellm.ai/docs/anthropic_unified)
    
    - allow using dynamic AWS Params - [PR](https://github.com/BerriAI/litellm/pull/10769)
- [**Nvidia NIM**](https://docs.litellm.ai/docs/providers/nvidia_nim)
  
  - [`/chat/completion`](https://docs.litellm.ai/docs/providers/nvidia_nim#usage---litellm-proxy-server)
    
    - Add tools, tool\_choice, parallel\_tool\_calls support - [PR](https://github.com/BerriAI/litellm/pull/10763)
- [**Novita AI**](https://docs.litellm.ai/docs/providers/novita)
  
  - New Provider added for `/chat/completion` routes - [PR](https://github.com/BerriAI/litellm/pull/9527)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - [`/image/generation`](https://docs.litellm.ai/docs/providers/azure#image-generation)
    
    - Fix azure dall e 3 call with custom model name - [PR](https://github.com/BerriAI/litellm/pull/10776)
- [**Cohere**](https://docs.litellm.ai/docs/providers/cohere)
  
  - [`/embeddings`](https://docs.litellm.ai/docs/providers/cohere#embedding)
    
    - Migrate embedding to use `/v2/embed` - adds support for output\_dimensions param - [PR](https://github.com/BerriAI/litellm/pull/10809)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - [`/chat/completion`](https://docs.litellm.ai/docs/providers/anthropic#usage-with-litellm-proxy)
    
    - Web search tool support - native + openai format - [Get Started](https://docs.litellm.ai/docs/providers/anthropic#anthropic-hosted-tools-computer-text-editor-web-search)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - [`/embeddings`](https://docs.litellm.ai/docs/providers/vllm#embeddings)
    
    - Support embedding input as list of integers
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - [`/chat/completion`](https://docs.litellm.ai/docs/providers/openai#usage---litellm-proxy-server)
    
    - Fix - b64 file data input handling - [Get Started](https://docs.litellm.ai/docs/providers/openai#pdf-file-parsing)
    - Add ‘supports\_pdf\_input’ to all vision models - [PR](https://github.com/BerriAI/litellm/pull/10897)

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Fix delete API support - [PR](https://github.com/BerriAI/litellm/pull/10845)
- [**Rerank API**](https://docs.litellm.ai/docs/rerank)
  
  - `/v2/rerank` now registered as ‘llm\_api\_route’ - enabling non-admins to call it - [PR](https://github.com/BerriAI/litellm/pull/10861)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- **`/chat/completion`, `/messages`**
  
  - Anthropic - web search tool cost tracking - [PR](https://github.com/BerriAI/litellm/pull/10846)
  - Groq - update model max tokens + cost information - [PR](https://github.com/BerriAI/litellm/pull/10077)
- **`/audio/transcription`**
  
  - Azure - Add gpt-4o-mini-tts pricing - [PR](https://github.com/BerriAI/litellm/pull/10807)
  - Proxy - Fix tracking spend by tag - [PR](https://github.com/BerriAI/litellm/pull/10832)
- **`/embeddings`**
  
  - Azure AI - Add cohere embed v4 pricing - [PR](https://github.com/BerriAI/litellm/pull/10806)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Models**
  
  - Ollama - adds api base param to UI
- **Logs**
  
  - Add team id, key alias, key hash filter on logs - [https://github.com/BerriAI/litellm/pull/10831](https://github.com/BerriAI/litellm/pull/10831)
  - Guardrail tracing now in Logs UI - [https://github.com/BerriAI/litellm/pull/10893](https://github.com/BerriAI/litellm/pull/10893)
- **Teams**
  
  - Patch for updating team info when team in org and members not in org - [https://github.com/BerriAI/litellm/pull/10835](https://github.com/BerriAI/litellm/pull/10835)
- **Guardrails**
  
  - Add Bedrock, Presidio, Lakers guardrails on UI - [https://github.com/BerriAI/litellm/pull/10874](https://github.com/BerriAI/litellm/pull/10874)
  - See guardrail info page - [https://github.com/BerriAI/litellm/pull/10904](https://github.com/BerriAI/litellm/pull/10904)
  - Allow editing guardrails on UI - [https://github.com/BerriAI/litellm/pull/10907](https://github.com/BerriAI/litellm/pull/10907)
- **Test Key**
  
  - select guardrails to test on UI

## Logging / Alerting Integrations[​](#logging--alerting-integrations "Direct link to Logging / Alerting Integrations")

- [**StandardLoggingPayload**](https://docs.litellm.ai/docs/proxy/logging_spec)
  
  - Log any `x-` headers in requester metadata - [Get Started](https://docs.litellm.ai/docs/proxy/logging_spec#standardloggingmetadata)
  - Guardrail tracing now in standard logging payload - [Get Started](https://docs.litellm.ai/docs/proxy/logging_spec#standardloggingguardrailinformation)
- [**Generic API Logger**](https://docs.litellm.ai/docs/proxy/logging#custom-callback-apis-async)
  
  - Support passing application/json header
- [**Arize Phoenix**](https://docs.litellm.ai/docs/observability/phoenix_integration)
  
  - fix: URL encode OTEL\_EXPORTER\_OTLP\_TRACES\_HEADERS for Phoenix Integration - [PR](https://github.com/BerriAI/litellm/pull/10654)
  - add guardrail tracing to OTEL, Arize phoenix - [PR](https://github.com/BerriAI/litellm/pull/10896)
- [**PagerDuty**](https://docs.litellm.ai/docs/proxy/pagerduty)
  
  - Pagerduty is now a free feature - [PR](https://github.com/BerriAI/litellm/pull/10857)
- [**Alerting**](https://docs.litellm.ai/docs/proxy/alerting)
  
  - Sending slack alerts on virtual key/user/team updates is now free - [PR](https://github.com/BerriAI/litellm/pull/10863)

## Guardrails[​](#guardrails "Direct link to Guardrails")

- **Guardrails**
  
  - New `/apply_guardrail` endpoint for directly testing a guardrail - [PR](https://github.com/BerriAI/litellm/pull/10867)
- [**Lakera**](https://docs.litellm.ai/docs/proxy/guardrails/lakera_ai)
  
  - `/v2` endpoints support - [PR](https://github.com/BerriAI/litellm/pull/10880)
- [**Presidio**](https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2)
  
  - Fixes handling of message content on presidio guardrail integration - [PR](https://github.com/BerriAI/litellm/pull/10197)
  - Allow specifying PII Entities Config - [PR](https://github.com/BerriAI/litellm/pull/10810)
- [**Aim Security**](https://docs.litellm.ai/docs/proxy/guardrails/aim_security)
  
  - Support for anonymization in AIM Guardrails - [PR](https://github.com/BerriAI/litellm/pull/10757)

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **Allow overriding all constants using a .env variable** - [PR](https://github.com/BerriAI/litellm/pull/10803)
- [**Maximum retention period for spend logs**](https://docs.litellm.ai/docs/proxy/spend_logs_deletion)
  
  - Add retention flag to config - [PR](https://github.com/BerriAI/litellm/pull/10815)
  - Support for cleaning up logs based on configured time period - [PR](https://github.com/BerriAI/litellm/pull/10872)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Authentication**
  
  - Handle Bearer $LITELLM\_API\_KEY in x-litellm-api-key custom header [PR](https://github.com/BerriAI/litellm/pull/10776)
- **New Enterprise pip package** - `litellm-enterprise` - fixes issue where `enterprise` folder was not found when using pip package
- [**Proxy CLI**](https://docs.litellm.ai/docs/proxy/management_cli)
  
  - Add `models import` command - [PR](https://github.com/BerriAI/litellm/pull/10581)
- [**OpenWebUI**](https://docs.litellm.ai/docs/tutorials/openweb_ui#per-user-tracking)
  
  - Configure LiteLLM to Parse User Headers from Open Web UI
- [**LiteLLM Proxy w/ LiteLLM SDK**](https://docs.litellm.ai/docs/providers/litellm_proxy#send-all-sdk-requests-to-litellm-proxy)
  
  - Option to force/always use the litellm proxy when calling via LiteLLM SDK

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- [@imdigitalashish](https://github.com/imdigitalashish) made their first contribution in PR [#10617](https://github.com/BerriAI/litellm/pull/10617)
- [@LouisShark](https://github.com/LouisShark) made their first contribution in PR [#10688](https://github.com/BerriAI/litellm/pull/10688)
- [@OscarSavNS](https://github.com/OscarSavNS) made their first contribution in PR [#10764](https://github.com/BerriAI/litellm/pull/10764)
- [@arizedatngo](https://github.com/arizedatngo) made their first contribution in PR [#10654](https://github.com/BerriAI/litellm/pull/10654)
- [@jugaldb](https://github.com/jugaldb) made their first contribution in PR [#10805](https://github.com/BerriAI/litellm/pull/10805)
- [@daikeren](https://github.com/daikeren) made their first contribution in PR [#10781](https://github.com/BerriAI/litellm/pull/10781)
- [@naliotopier](https://github.com/naliotopier) made their first contribution in PR [#10077](https://github.com/BerriAI/litellm/pull/10077)
- [@damienpontifex](https://github.com/damienpontifex) made their first contribution in PR [#10813](https://github.com/BerriAI/litellm/pull/10813)
- [@Dima-Mediator](https://github.com/Dima-Mediator) made their first contribution in PR [#10789](https://github.com/BerriAI/litellm/pull/10789)
- [@igtm](https://github.com/igtm) made their first contribution in PR [#10814](https://github.com/BerriAI/litellm/pull/10814)
- [@shibaboy](https://github.com/shibaboy) made their first contribution in PR [#10752](https://github.com/BerriAI/litellm/pull/10752)
- [@camfarineau](https://github.com/camfarineau) made their first contribution in PR [#10629](https://github.com/BerriAI/litellm/pull/10629)
- [@ajac-zero](https://github.com/ajac-zero) made their first contribution in PR [#10439](https://github.com/BerriAI/litellm/pull/10439)
- [@damgem](https://github.com/damgem) made their first contribution in PR [#9802](https://github.com/BerriAI/litellm/pull/9802)
- [@hxdror](https://github.com/hxdror) made their first contribution in PR [#10757](https://github.com/BerriAI/litellm/pull/10757)
- [@wwwillchen](https://github.com/wwwillchen) made their first contribution in PR [#10894](https://github.com/BerriAI/litellm/pull/10894)

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## [Git Diff](https://github.com/BerriAI/litellm/releases)[​](#git-diff "Direct link to git-diff")

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.69.0-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

LiteLLM v1.69.0-stable brings the following key improvements:

- **Loadbalance Batch API Models**: Easily loadbalance across multiple azure batch deployments using LiteLLM Managed Files
- **Email Invites 2.0**: Send new users onboarded to LiteLLM an email invite.
- **Nscale**: LLM API for compliance with European regulations.
- **Bedrock /v1/messages**: Use Bedrock Anthropic models with Anthropic's /v1/messages.

## Batch API Load Balancing[​](#batch-api-load-balancing "Direct link to Batch API Load Balancing")

This release brings LiteLLM Managed File support to Batches. This is great for:

- Proxy Admins: You can now control which Batch models users can call.
- Developers: You no longer need to know the Azure deployment name when creating your batch .jsonl files - just specify the model your LiteLLM key has access to.

Over time, we expect LiteLLM Managed Files to be the way most teams use Files across `/chat/completions`, `/batch`, `/fine_tuning` endpoints.

[Read more here](https://docs.litellm.ai/docs/proxy/managed_batches)

## Email Invites[​](#email-invites "Direct link to Email Invites")

This release brings the following improvements to our email invite integration:

- New templates for user invited and key created events.
- Fixes for using SMTP email providers.
- Native support for Resend API.
- Ability for Proxy Admins to control email events.

For LiteLLM Cloud Users, please reach out to us if you want this enabled for your instance.

[Read more here](https://docs.litellm.ai/docs/proxy/email)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **Gemini ([VertexAI](https://docs.litellm.ai/docs/providers/vertex#usage-with-litellm-proxy-server) + [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini))**
  
  - Added `gemini-2.5-pro-preview-05-06` models with pricing and context window info - [PR](https://github.com/BerriAI/litellm/pull/10597)
  - Set correct context window length for all Gemini 2.5 variants - [PR](https://github.com/BerriAI/litellm/pull/10690)
- [**Perplexity**](https://docs.litellm.ai/docs/providers/perplexity):
  
  - Added new Perplexity models - [PR](https://github.com/BerriAI/litellm/pull/10652)
  - Added sonar-deep-research model pricing - [PR](https://github.com/BerriAI/litellm/pull/10537)
- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure):
  
  - Fixed passing through of azure\_ad\_token\_provider parameter - [PR](https://github.com/BerriAI/litellm/pull/10694)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai):
  
  - Added support for pdf url's in 'file' parameter - [PR](https://github.com/BerriAI/litellm/pull/10640)
- [**Sagemaker**](https://docs.litellm.ai/docs/providers/aws_sagemaker):
  
  - Fix content length for `sagemaker_chat` provider - [PR](https://github.com/BerriAI/litellm/pull/10607)
- [**Azure AI Foundry**](https://docs.litellm.ai/docs/providers/azure_ai):
  
  - Added cost tracking for the following models [PR](https://github.com/BerriAI/litellm/pull/9956)
    
    - DeepSeek V3 0324
    - Llama 4 Scout
    - Llama 4 Maverick
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock):
  
  - Added cost tracking for Bedrock Llama 4 models - [PR](https://github.com/BerriAI/litellm/pull/10582)
  - Fixed template conversion for Llama 4 models in Bedrock - [PR](https://github.com/BerriAI/litellm/pull/10582)
  - Added support for using Bedrock Anthropic models with /v1/messages format - [PR](https://github.com/BerriAI/litellm/pull/10681)
  - Added streaming support for Bedrock Anthropic models with /v1/messages format - [PR](https://github.com/BerriAI/litellm/pull/10710)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai): Added `reasoning_effort` support for `o3` models - [PR](https://github.com/BerriAI/litellm/pull/10591)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks):
  
  - Fixed issue when Databricks uses external model and delta could be empty - [PR](https://github.com/BerriAI/litellm/pull/10540)
- [**Cerebras**](https://docs.litellm.ai/docs/providers/cerebras): Fixed Llama-3.1-70b model pricing and context window - [PR](https://github.com/BerriAI/litellm/pull/10648)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama):
  
  - Fixed custom price cost tracking and added 'max\_completion\_token' support - [PR](https://github.com/BerriAI/litellm/pull/10636)
  - Fixed KeyError when using JSON response format - [PR](https://github.com/BerriAI/litellm/pull/10611)
- 🆕 [**Nscale**](https://docs.litellm.ai/docs/providers/nscale):
  
  - Added support for chat, image generation endpoints - [PR](https://github.com/BerriAI/litellm/pull/10638)

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

- [**Messages API**](https://docs.litellm.ai/docs/anthropic_unified):
  
  - 🆕 Added support for using Bedrock Anthropic models with /v1/messages format - [PR](https://github.com/BerriAI/litellm/pull/10681) and streaming support - [PR](https://github.com/BerriAI/litellm/pull/10710)
- [**Moderations API**](https://docs.litellm.ai/docs/moderations):
  
  - Fixed bug to allow using LiteLLM UI credentials for /moderations API - [PR](https://github.com/BerriAI/litellm/pull/10723)
- [**Realtime API**](https://docs.litellm.ai/docs/realtime):
  
  - Fixed setting 'headers' in scope for websocket auth requests and infinite loop issues - [PR](https://github.com/BerriAI/litellm/pull/10679)
- [**Files API**](https://docs.litellm.ai/docs/proxy/litellm_managed_files):
  
  - Unified File ID output support - [PR](https://github.com/BerriAI/litellm/pull/10713)
  - Support for writing files to all deployments - [PR](https://github.com/BerriAI/litellm/pull/10708)
  - Added target model name validation - [PR](https://github.com/BerriAI/litellm/pull/10722)
- [**Batches API**](https://docs.litellm.ai/docs/batches):
  
  - Complete unified batch ID support - replacing model in jsonl to be deployment model name - [PR](https://github.com/BerriAI/litellm/pull/10719)
  - Beta support for unified file ID (managed files) for batches - [PR](https://github.com/BerriAI/litellm/pull/10650)

## Spend Tracking / Budget Improvements[​](#spend-tracking--budget-improvements "Direct link to Spend Tracking / Budget Improvements")

- Bug Fix - PostgreSQL Integer Overflow Error in DB Spend Tracking - [PR](https://github.com/BerriAI/litellm/pull/10697)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Models**
  
  - Fixed model info overwriting when editing a model on UI - [PR](https://github.com/BerriAI/litellm/pull/10726)
  - Fixed team admin model updates and organization creation with specific models - [PR](https://github.com/BerriAI/litellm/pull/10539)
- **Logs**:
  
  - Bug Fix - copying Request/Response on Logs Page - [PR](https://github.com/BerriAI/litellm/pull/10720)
  - Bug Fix - log did not remain in focus on QA Logs page + text overflow on error logs - [PR](https://github.com/BerriAI/litellm/pull/10725)
  - Added index for session\_id on LiteLLM\_SpendLogs for better query performance - [PR](https://github.com/BerriAI/litellm/pull/10727)
- **User Management**:
  
  - Added user management functionality to Python client library & CLI - [PR](https://github.com/BerriAI/litellm/pull/10627)
  - Bug Fix - Fixed SCIM token creation on Admin UI - [PR](https://github.com/BerriAI/litellm/pull/10628)
  - Bug Fix - Added 404 response when trying to delete verification tokens that don't exist - [PR](https://github.com/BerriAI/litellm/pull/10605)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- **Custom Logger API**: v2 Custom Callback API (send llm logs to custom api) - [PR](https://github.com/BerriAI/litellm/pull/10575), [Get Started](https://docs.litellm.ai/docs/proxy/logging#custom-callback-apis-async)
- **OpenTelemetry**:
  
  - Fixed OpenTelemetry to follow genai semantic conventions + support for 'instructions' param for TTS - [PR](https://github.com/BerriAI/litellm/pull/10608)
- \** Bedrock PII\*\*:
  
  - Add support for PII Masking with bedrock guardrails - [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/bedrock#pii-masking-with-bedrock-guardrails), [PR](https://github.com/BerriAI/litellm/pull/10608)
- **Documentation**:
  
  - Added documentation for StandardLoggingVectorStoreRequest - [PR](https://github.com/BerriAI/litellm/pull/10535)

## Performance / Reliability Improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

- **Python Compatibility**:
  
  - Added support for Python 3.11- (fixed datetime UTC handling) - [PR](https://github.com/BerriAI/litellm/pull/10701)
  - Fixed UnicodeDecodeError: 'charmap' on Windows during litellm import - [PR](https://github.com/BerriAI/litellm/pull/10542)
- **Caching**:
  
  - Fixed embedding string caching result - [PR](https://github.com/BerriAI/litellm/pull/10700)
  - Fixed cache miss for Gemini models with response\_format - [PR](https://github.com/BerriAI/litellm/pull/10635)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Proxy CLI**:
  
  - Added `--version` flag to `litellm-proxy` CLI - [PR](https://github.com/BerriAI/litellm/pull/10704)
  - Added dedicated `litellm-proxy` CLI - [PR](https://github.com/BerriAI/litellm/pull/10578)
- **Alerting**:
  
  - Fixed Slack alerting not working when using a DB - [PR](https://github.com/BerriAI/litellm/pull/10370)
- **Email Invites**:
  
  - Added V2 Emails with fixes for sending emails when creating keys + Resend API support - [PR](https://github.com/BerriAI/litellm/pull/10602)
  - Added user invitation emails - [PR](https://github.com/BerriAI/litellm/pull/10615)
  - Added endpoints to manage email settings - [PR](https://github.com/BerriAI/litellm/pull/10646)
- **General**:
  
  - Fixed bug where duplicate JSON logs were getting emitted - [PR](https://github.com/BerriAI/litellm/pull/10580)

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- [@zoltan-ongithub](https://github.com/zoltan-ongithub) made their first contribution in [PR #10568](https://github.com/BerriAI/litellm/pull/10568)
- [@mkavinkumar1](https://github.com/mkavinkumar1) made their first contribution in [PR #10548](https://github.com/BerriAI/litellm/pull/10548)
- [@thomelane](https://github.com/thomelane) made their first contribution in [PR #10549](https://github.com/BerriAI/litellm/pull/10549)
- [@frankzye](https://github.com/frankzye) made their first contribution in [PR #10540](https://github.com/BerriAI/litellm/pull/10540)
- [@aholmberg](https://github.com/aholmberg) made their first contribution in [PR #10591](https://github.com/BerriAI/litellm/pull/10591)
- [@aravindkarnam](https://github.com/aravindkarnam) made their first contribution in [PR #10611](https://github.com/BerriAI/litellm/pull/10611)
- [@xsg22](https://github.com/xsg22) made their first contribution in [PR #10648](https://github.com/BerriAI/litellm/pull/10648)
- [@casparhsws](https://github.com/casparhsws) made their first contribution in [PR #10635](https://github.com/BerriAI/litellm/pull/10635)
- [@hypermoose](https://github.com/hypermoose) made their first contribution in [PR #10370](https://github.com/BerriAI/litellm/pull/10370)
- [@tomukmatthews](https://github.com/tomukmatthews) made their first contribution in [PR #10638](https://github.com/BerriAI/litellm/pull/10638)
- [@keyute](https://github.com/keyute) made their first contribution in [PR #10652](https://github.com/BerriAI/litellm/pull/10652)
- [@GPTLocalhost](https://github.com/GPTLocalhost) made their first contribution in [PR #10687](https://github.com/BerriAI/litellm/pull/10687)
- [@husnain7766](https://github.com/husnain7766) made their first contribution in [PR #10697](https://github.com/BerriAI/litellm/pull/10697)
- [@claralp](https://github.com/claralp) made their first contribution in [PR #10694](https://github.com/BerriAI/litellm/pull/10694)
- [@mollux](https://github.com/mollux) made their first contribution in [PR #10690](https://github.com/BerriAI/litellm/pull/10690)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.68.0-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

LiteLLM v1.68.0-stable will be live soon. Here are the key highlights of this release:

- **Bedrock Knowledge Base**: You can now call query your Bedrock Knowledge Base with all LiteLLM models via `/chat/completion` or `/responses` API.
- **Rate Limits**: This release brings accurate rate limiting across multiple instances, reducing spillover to at most 10 additional requests in high traffic.
- **Meta Llama API**: Added support for Meta Llama API [Get Started](https://docs.litellm.ai/docs/providers/meta_llama)
- **LlamaFile**: Added support for LlamaFile [Get Started](https://docs.litellm.ai/docs/providers/llamafile)

## Bedrock Knowledge Base (Vector Store)[​](#bedrock-knowledge-base-vector-store "Direct link to Bedrock Knowledge Base (Vector Store)")

This release adds support for Bedrock vector stores (knowledge bases) in LiteLLM. With this update, you can:

- Use Bedrock vector stores in the OpenAI /chat/completions spec with all LiteLLM supported models.
- View all available vector stores through the LiteLLM UI or API.
- Configure vector stores to be always active for specific models.
- Track vector store usage in LiteLLM Logs.

For the next release we plan on allowing you to set key, user, team, org permissions for vector stores.

[Read more here](https://docs.litellm.ai/docs/completion/knowledgebase)

## Rate Limiting[​](#rate-limiting "Direct link to Rate Limiting")

This release brings accurate multi-instance rate limiting across keys/users/teams. Outlining key engineering changes below:

- **Change**: Instances now increment cache value instead of setting it. To avoid calling Redis on each request, this is synced every 0.01s.
- **Accuracy**: In testing, we saw a maximum spill over from expected of 10 requests, in high traffic (100 RPS, 3 instances), vs. current 189 request spillover
- **Performance**: Our load tests show this to reduce median response time by 100ms in high traffic

This is currently behind a feature flag, and we plan to have this be the default by next week. To enable this today, just add this environment variable:

```
export LITELLM_RATE_LIMIT_ACCURACY=true
```

[Read more here](https://docs.litellm.ai/docs/proxy/users#beta-multi-instance-rate-limiting)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **Gemini ([VertexAI](https://docs.litellm.ai/docs/providers/vertex#usage-with-litellm-proxy-server) + [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini))**
  
  - Handle more json schema - openapi schema conversion edge cases [PR](https://github.com/BerriAI/litellm/pull/10351)
  - Tool calls - return ‘finish\_reason=“tool\_calls”’ on gemini tool calling response [PR](https://github.com/BerriAI/litellm/pull/10485)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex#metallama-api)
  
  - Meta/llama-4 model support [PR](https://github.com/BerriAI/litellm/pull/10492)
  - Meta/llama3 - handle tool call result in content [PR](https://github.com/BerriAI/litellm/pull/10492)
  - Meta/* - return ‘finish\_reason=“tool\_calls”’ on tool calling response [PR](https://github.com/BerriAI/litellm/pull/10492)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock#litellm-proxy-usage)
  
  - [Image Generation](https://docs.litellm.ai/docs/providers/bedrock#image-generation) - Support new ‘stable-image-core’ models - [PR](https://github.com/BerriAI/litellm/pull/10351)
  - [Knowledge Bases](https://docs.litellm.ai/docs/completion/knowledgebase) - support using Bedrock knowledge bases with `/chat/completions` [PR](https://github.com/BerriAI/litellm/pull/10413)
  - [Anthropic](https://docs.litellm.ai/docs/providers/bedrock#litellm-proxy-usage) - add ‘supports\_pdf\_input’ for claude-3.7-bedrock models [PR](https://github.com/BerriAI/litellm/pull/9917), [Get Started](https://docs.litellm.ai/docs/completion/document_understanding#checking-if-a-model-supports-pdf-input)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Support OPENAI\_BASE\_URL in addition to OPENAI\_API\_BASE [PR](https://github.com/BerriAI/litellm/pull/10423)
  - Correctly re-raise 504 timeout errors [PR](https://github.com/BerriAI/litellm/pull/10462)
  - Native Gpt-4o-mini-tts support [PR](https://github.com/BerriAI/litellm/pull/10462)
- 🆕 [**Meta Llama API**](https://docs.litellm.ai/docs/providers/meta_llama) provider [PR](https://github.com/BerriAI/litellm/pull/10451)
- 🆕 [**LlamaFile**](https://docs.litellm.ai/docs/providers/llamafile) provider [PR](https://github.com/BerriAI/litellm/pull/10482)

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

- [**Response API**](https://docs.litellm.ai/docs/response_api)
  
  - Fix for handling multi turn sessions [PR](https://github.com/BerriAI/litellm/pull/10415)
- [**Embeddings**](https://docs.litellm.ai/docs/embedding/supported_embedding)
  
  - Caching fixes - [PR](https://github.com/BerriAI/litellm/pull/10424)
    
    - handle str -&gt; list cache
    - Return usage tokens for cache hit
    - Combine usage tokens on partial cache hits
- 🆕 [**Vector Stores**](https://docs.litellm.ai/docs/completion/knowledgebase)
  
  - Allow defining Vector Store Configs - [PR](https://github.com/BerriAI/litellm/pull/10448)
  - New StandardLoggingPayload field for requests made when a vector store is used - [PR](https://github.com/BerriAI/litellm/pull/10509)
  - Show Vector Store / KB Request on LiteLLM Logs Page - [PR](https://github.com/BerriAI/litellm/pull/10514)
  - Allow using vector store in OpenAI API spec with tools - [PR](https://github.com/BerriAI/litellm/pull/10516)
- [**MCP**](https://docs.litellm.ai/docs/mcp)
  
  - Ensure Non-Admin virtual keys can access /mcp routes - [PR](https://github.com/BerriAI/litellm/pull/10473)
    
    **Note:** Currently, all Virtual Keys are able to access the MCP endpoints. We are working on a feature to allow restricting MCP access by keys/teams/users/orgs. Follow [here](https://github.com/BerriAI/litellm/discussions/9891) for updates.
- **Moderations**
  
  - Add logging callback support for `/moderations` API - [PR](https://github.com/BerriAI/litellm/pull/10390)

## Spend Tracking / Budget Improvements[​](#spend-tracking--budget-improvements "Direct link to Spend Tracking / Budget Improvements")

- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - [computer-use-preview](https://docs.litellm.ai/docs/providers/openai/responses_api#computer-use) cost tracking / pricing [PR](https://github.com/BerriAI/litellm/pull/10422)
  - [gpt-4o-mini-tts](https://docs.litellm.ai/docs/providers/openai/text_to_speech) input cost tracking - [PR](https://github.com/BerriAI/litellm/pull/10462)
- [**Fireworks AI**](https://docs.litellm.ai/docs/providers/fireworks_ai) - pricing updates - new `0-4b` model pricing tier + llama4 model pricing
- [**Budgets**](https://docs.litellm.ai/docs/proxy/users#set-budgets)
  
  - [Budget resets](https://docs.litellm.ai/docs/proxy/users#reset-budgets) now happen as start of day/week/month - [PR](https://github.com/BerriAI/litellm/pull/10333)
  - Trigger [Soft Budget Alerts](https://docs.litellm.ai/docs/proxy/alerting#soft-budget-alerts-for-virtual-keys) When Key Crosses Threshold - [PR](https://github.com/BerriAI/litellm/pull/10491)
- [**Token Counting**](https://docs.litellm.ai/docs/completion/token_usage#3-token_counter)
  
  - Rewrite of token\_counter() function to handle to prevent undercounting tokens - [PR](https://github.com/BerriAI/litellm/pull/10409)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Virtual Keys**
  
  - Fix filtering on key alias - [PR](https://github.com/BerriAI/litellm/pull/10455)
  - Support global filtering on keys - [PR](https://github.com/BerriAI/litellm/pull/10455)
  - Pagination - fix clicking on next/back buttons on table - [PR](https://github.com/BerriAI/litellm/pull/10528)
- **Models**
  
  - Triton - Support adding model/provider on UI - [PR](https://github.com/BerriAI/litellm/pull/10456)
  - VertexAI - Fix adding vertex models with reusable credentials - [PR](https://github.com/BerriAI/litellm/pull/10528)
  - LLM Credentials - show existing credentials for easy editing - [PR](https://github.com/BerriAI/litellm/pull/10519)
- **Teams**
  
  - Allow reassigning team to other org - [PR](https://github.com/BerriAI/litellm/pull/10527)
- **Organizations**
  
  - Fix showing org budget on table - [PR](https://github.com/BerriAI/litellm/pull/10528)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- [**Langsmith**](https://docs.litellm.ai/docs/observability/langsmith_integration)
  
  - Respect [langsmith\_batch\_size](https://docs.litellm.ai/docs/observability/langsmith_integration#local-testing---control-batch-size) param - [PR](https://github.com/BerriAI/litellm/pull/10411)

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- [**Redis**](https://docs.litellm.ai/docs/proxy/caching)
  
  - Ensure all redis queues are periodically flushed, this fixes an issue where redis queue size was growing indefinitely when request tags were used - [PR](https://github.com/BerriAI/litellm/pull/10393)
- [**Rate Limits**](https://docs.litellm.ai/docs/proxy/users#set-rate-limit)
  
  - [Multi-instance rate limiting](https://docs.litellm.ai/docs/proxy/users#beta-multi-instance-rate-limiting) support across keys/teams/users/customers - [PR](https://github.com/BerriAI/litellm/pull/10458), [PR](https://github.com/BerriAI/litellm/pull/10497), [PR](https://github.com/BerriAI/litellm/pull/10500)
- [**Azure OpenAI OIDC**](https://docs.litellm.ai/docs/providers/azure#entra-id---use-azure_ad_token)
  
  - allow using litellm defined params for [OIDC Auth](https://docs.litellm.ai/docs/providers/azure#entra-id---use-azure_ad_token) - [PR](https://github.com/BerriAI/litellm/pull/10394)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Security**
  
  - Allow [blocking web crawlers](https://docs.litellm.ai/docs/proxy/enterprise#blocking-web-crawlers) - [PR](https://github.com/BerriAI/litellm/pull/10420)
- **Auth**
  
  - Support [`x-litellm-api-key` header param by default](https://docs.litellm.ai/docs/pass_through/vertex_ai#use-with-virtual-keys), this fixes an issue from the prior release where `x-litellm-api-key` was not being used on vertex ai passthrough requests - [PR](https://github.com/BerriAI/litellm/pull/10392)
  - Allow key at max budget to call non-llm api endpoints - [PR](https://github.com/BerriAI/litellm/pull/10392)
- 🆕 **[Python Client Library](https://docs.litellm.ai/docs/proxy/management_cli) for LiteLLM Proxy management endpoints**
  
  - Initial PR - [PR](https://github.com/BerriAI/litellm/pull/10445)
  - Support for doing HTTP requests - [PR](https://github.com/BerriAI/litellm/pull/10452)
- **Dependencies**
  
  - Don’t require uvloop for windows - [PR](https://github.com/BerriAI/litellm/pull/10483)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.67.4-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Improved User Management**: This release enables search and filtering across users, keys, teams, and models.
- **Responses API Load Balancing**: Route requests across provider regions and ensure session continuity.
- **UI Session Logs**: Group several requests to LiteLLM into a session.

## Improved User Management[​](#improved-user-management "Direct link to Improved User Management")

This release makes it easier to manage users and keys on LiteLLM. You can now search and filter across users, keys, teams, and models, and control user settings more easily.

New features include:

- Search for users by email, ID, role, or team.
- See all of a user's models, teams, and keys in one place.
- Change user roles and model access right from the Users Tab.

These changes help you spend less time on user setup and management on LiteLLM.

## Responses API Load Balancing[​](#responses-api-load-balancing "Direct link to Responses API Load Balancing")

This release introduces load balancing for the Responses API, allowing you to route requests across provider regions and ensure session continuity. It works as follows:

- If a `previous_response_id` is provided, LiteLLM will route the request to the original deployment that generated the prior response — ensuring session continuity.
- If no `previous_response_id` is provided, LiteLLM will load-balance requests across your available deployments.

[Read more](https://docs.litellm.ai/docs/response_api#load-balancing-with-session-continuity)

## UI Session Logs[​](#ui-session-logs "Direct link to UI Session Logs")

This release allow you to group requests to LiteLLM proxy into a session. If you specify a litellm\_session\_id in your request LiteLLM will automatically group all logs in the same session. This allows you to easily track usage and request content per session.

[Read more](https://docs.litellm.ai/docs/proxy/ui_logs_sessions)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **OpenAI**
  
  1. Added `gpt-image-1` cost tracking [Get Started](https://docs.litellm.ai/docs/image_generation)
  2. Bug fix: added cost tracking for gpt-image-1 when quality is unspecified [PR](https://github.com/BerriAI/litellm/pull/10247)
- **Azure**
  
  1. Fixed timestamp granularities passing to whisper in Azure [Get Started](https://docs.litellm.ai/docs/audio_transcription)
  2. Added azure/gpt-image-1 pricing [Get Started](https://docs.litellm.ai/docs/image_generation), [PR](https://github.com/BerriAI/litellm/pull/10327)
  3. Added cost tracking for `azure/computer-use-preview`, `azure/gpt-4o-audio-preview-2024-12-17`, `azure/gpt-4o-mini-audio-preview-2024-12-17` [PR](https://github.com/BerriAI/litellm/pull/10178)
- **Bedrock**
  
  1. Added support for all compatible Bedrock parameters when model="arn:.." (Bedrock application inference profile models) [Get started](https://docs.litellm.ai/docs/providers/bedrock#bedrock-application-inference-profile), [PR](https://github.com/BerriAI/litellm/pull/10256)
  2. Fixed wrong system prompt transformation [PR](https://github.com/BerriAI/litellm/pull/10120)
- **VertexAI / Google AI Studio**
  
  1. Allow setting `budget_tokens=0` for `gemini-2.5-flash` [Get Started](https://docs.litellm.ai/docs/providers/gemini#usage---thinking--reasoning_content),[PR](https://github.com/BerriAI/litellm/pull/10198)
  2. Ensure returned `usage` includes thinking token usage [PR](https://github.com/BerriAI/litellm/pull/10198)
  3. Added cost tracking for `gemini-2.5-pro-preview-03-25` [PR](https://github.com/BerriAI/litellm/pull/10178)
- **Cohere**
  
  1. Added support for cohere command-a-03-2025 [Get Started](https://docs.litellm.ai/docs/providers/cohere), [PR](https://github.com/BerriAI/litellm/pull/10295)
- **SageMaker**
  
  1. Added support for max\_completion\_tokens parameter [Get Started](https://docs.litellm.ai/docs/providers/sagemaker), [PR](https://github.com/BerriAI/litellm/pull/10300)
- **Responses API**
  
  1. Added support for GET and DELETE operations - `/v1/responses/{response_id}` [Get Started](https://docs.litellm.ai/docs/response_api)
  2. Added session management support for all supported models [PR](https://github.com/BerriAI/litellm/pull/10321)
  3. Added routing affinity to maintain model consistency within sessions [Get Started](https://docs.litellm.ai/docs/response_api#load-balancing-with-routing-affinity), [PR](https://github.com/BerriAI/litellm/pull/10193)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- **Bug Fix**: Fixed spend tracking bug, ensuring default litellm params aren't modified in memory [PR](https://github.com/BerriAI/litellm/pull/10167)
- **Deprecation Dates**: Added deprecation dates for Azure, VertexAI models [PR](https://github.com/BerriAI/litellm/pull/10308)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Users[​](#users "Direct link to Users")

- **Filtering and Searching**:
  
  - Filter users by user\_id, role, team, sso\_id
  - Search users by email
- **User Info Panel**: Added a new user information pane [PR](https://github.com/BerriAI/litellm/pull/10213)
  
  - View teams, keys, models associated with User
  - Edit user role, model permissions

#### Teams[​](#teams "Direct link to Teams")

- **Filtering and Searching**:
  
  - Filter teams by Organization, Team ID [PR](https://github.com/BerriAI/litellm/pull/10324)
  - Search teams by Team Name [PR](https://github.com/BerriAI/litellm/pull/10324)

#### Keys[​](#keys "Direct link to Keys")

- **Key Management**:
  
  - Support for cross-filtering and filtering by key hash [PR](https://github.com/BerriAI/litellm/pull/10322)
  - Fixed key alias reset when resetting filters [PR](https://github.com/BerriAI/litellm/pull/10099)
  - Fixed table rendering on key creation [PR](https://github.com/BerriAI/litellm/pull/10224)

#### UI Logs Page[​](#ui-logs-page "Direct link to UI Logs Page")

- **Session Logs**: Added UI Session Logs [Get Started](https://docs.litellm.ai/docs/proxy/ui_logs_sessions)

#### UI Authentication & Security[​](#ui-authentication--security "Direct link to UI Authentication & Security")

- **Required Authentication**: Authentication now required for all dashboard pages [PR](https://github.com/BerriAI/litellm/pull/10229)
- **SSO Fixes**: Fixed SSO user login invalid token error [PR](https://github.com/BerriAI/litellm/pull/10298)
- \[BETA] **Encrypted Tokens**: Moved UI to encrypted token usage [PR](https://github.com/BerriAI/litellm/pull/10302)
- **Token Expiry**: Support token refresh by re-routing to login page (fixes issue where expired token would show a blank page) [PR](https://github.com/BerriAI/litellm/pull/10250)

#### UI General fixes[​](#ui-general-fixes "Direct link to UI General fixes")

- **Fixed UI Flicker**: Addressed UI flickering issues in Dashboard [PR](https://github.com/BerriAI/litellm/pull/10261)
- **Improved Terminology**: Better loading and no-data states on Keys and Tools pages [PR](https://github.com/BerriAI/litellm/pull/10253)
- **Azure Model Support**: Fixed editing Azure public model names and changing model names after creation [PR](https://github.com/BerriAI/litellm/pull/10249)
- **Team Model Selector**: Bug fix for team model selection [PR](https://github.com/BerriAI/litellm/pull/10171)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- **Datadog**:
  
  1. Fixed Datadog LLM observability logging [Get Started](https://docs.litellm.ai/docs/proxy/logging#datadog), [PR](https://github.com/BerriAI/litellm/pull/10206)
- **Prometheus / Grafana**:
  
  1. Enable datasource selection on LiteLLM Grafana Template [Get Started](https://docs.litellm.ai/docs/proxy/prometheus#-litellm-maintained-grafana-dashboards-), [PR](https://github.com/BerriAI/litellm/pull/10257)
- **AgentOps**:
  
  1. Added AgentOps Integration [Get Started](https://docs.litellm.ai/docs/observability/agentops_integration), [PR](https://github.com/BerriAI/litellm/pull/9685)
- **Arize**:
  
  1. Added missing attributes for Arize & Phoenix Integration [Get Started](https://docs.litellm.ai/docs/observability/arize_integration), [PR](https://github.com/BerriAI/litellm/pull/10215)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Caching**: Fixed caching to account for `thinking` or `reasoning_effort` when calculating cache key [PR](https://github.com/BerriAI/litellm/pull/10140)
- **Model Groups**: Fixed handling for cases where user sets model\_group inside model\_info [PR](https://github.com/BerriAI/litellm/pull/10191)
- **Passthrough Endpoints**: Ensured `PassthroughStandardLoggingPayload` is logged with method, URL, request/response body [PR](https://github.com/BerriAI/litellm/pull/10194)
- **Fix SQL Injection**: Fixed potential SQL injection vulnerability in spend\_management\_endpoints.py [PR](https://github.com/BerriAI/litellm/pull/9878)

## Helm[​](#helm "Direct link to Helm")

- Fixed serviceAccountName on migration job [PR](https://github.com/BerriAI/litellm/pull/10258)

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

The complete list of changes can be found in the [GitHub release notes](https://github.com/BerriAI/litellm/compare/v1.67.0-stable...v1.67.4-stable).

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **SCIM Integration**: Enables identity providers (Okta, Azure AD, OneLogin, etc.) to automate user and team (group) provisioning, updates, and deprovisioning
- **Team and Tag based usage tracking**: You can now see usage and spend by team and tag at 1M+ spend logs.
- **Unified Responses API**: Support for calling Anthropic, Gemini, Groq, etc. via OpenAI's new Responses API.

Let's dive in.

## SCIM Integration[​](#scim-integration "Direct link to SCIM Integration")

This release adds SCIM support to LiteLLM. This allows your SSO provider (Okta, Azure AD, etc) to automatically create/delete users, teams, and memberships on LiteLLM. This means that when you remove a team on your SSO provider, your SSO provider will automatically delete the corresponding team on LiteLLM.

[Read more](https://docs.litellm.ai/docs/tutorials/scim_litellm)

## Team and Tag based usage tracking[​](#team-and-tag-based-usage-tracking "Direct link to Team and Tag based usage tracking")

This release improves team and tag based usage tracking at 1m+ spend logs, making it easy to monitor your LLM API Spend in production. This covers:

- View **daily spend** by teams + tags
- View **usage / spend by key**, within teams
- View **spend by multiple tags**
- Allow **internal users** to view spend of teams they're a member of

[Read more](#management-endpoints--ui)

## Unified Responses API[​](#unified-responses-api "Direct link to Unified Responses API")

This release allows you to call Azure OpenAI, Anthropic, AWS Bedrock, and Google Vertex AI models via the POST /v1/responses endpoint on LiteLLM. This means you can now use popular tools like [OpenAI Codex](https://docs.litellm.ai/docs/tutorials/openai_codex) with your own models.

[Read more](https://docs.litellm.ai/docs/response_api)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **OpenAI**
  
  1. gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, o3, o3-mini, o4-mini pricing - [Get Started](https://docs.litellm.ai/docs/providers/openai#usage), [PR](https://github.com/BerriAI/litellm/pull/9990)
  2. o4 - correctly map o4 to openai o\_series model
- **Azure AI**
  
  1. Phi-4 output cost per token fix - [PR](https://github.com/BerriAI/litellm/pull/9880)
  2. Responses API support [Get Started](https://docs.litellm.ai/docs/providers/azure#azure-responses-api),[PR](https://github.com/BerriAI/litellm/pull/10116)
- **Anthropic**
  
  1. redacted message thinking support - [Get Started](https://docs.litellm.ai/docs/providers/anthropic#usage---thinking--reasoning_content),[PR](https://github.com/BerriAI/litellm/pull/10129)
- **Cohere**
  
  1. `/v2/chat` Passthrough endpoint support w/ cost tracking - [Get Started](https://docs.litellm.ai/docs/pass_through/cohere), [PR](https://github.com/BerriAI/litellm/pull/9997)
- **Azure**
  
  1. Support azure tenant\_id/client\_id env vars - [Get Started](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret), [PR](https://github.com/BerriAI/litellm/pull/9993)
  2. Fix response\_format check for 2025+ api versions - [PR](https://github.com/BerriAI/litellm/pull/9993)
  3. Add gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, o3, o3-mini, o4-mini pricing
- **VLLM**
  
  1. Files - Support 'file' message type for VLLM video url's - [Get Started](https://docs.litellm.ai/docs/providers/vllm#send-video-url-to-vllm), [PR](https://github.com/BerriAI/litellm/pull/10129)
  2. Passthrough - new `/vllm/` passthrough endpoint support [Get Started](https://docs.litellm.ai/docs/pass_through/vllm), [PR](https://github.com/BerriAI/litellm/pull/10002)
- **Mistral**
  
  1. new `/mistral` passthrough endpoint support [Get Started](https://docs.litellm.ai/docs/pass_through/mistral), [PR](https://github.com/BerriAI/litellm/pull/10002)
- **AWS**
  
  1. New mapped bedrock regions - [PR](https://github.com/BerriAI/litellm/pull/9430)
- **VertexAI / Google AI Studio**
  
  1. Gemini - Response format - Retain schema field ordering for google gemini and vertex by specifying propertyOrdering - [Get Started](https://docs.litellm.ai/docs/providers/vertex#json-schema), [PR](https://github.com/BerriAI/litellm/pull/9828)
  2. Gemini-2.5-flash - return reasoning content [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini#usage---thinking--reasoning_content), [Vertex AI](https://docs.litellm.ai/docs/providers/vertex#thinking--reasoning_content)
  3. Gemini-2.5-flash - pricing + model information [PR](https://github.com/BerriAI/litellm/pull/10125)
  4. Passthrough - new `/vertex_ai/discovery` route - enables calling AgentBuilder API routes [Get Started](https://docs.litellm.ai/docs/pass_through/vertex_ai#supported-api-endpoints), [PR](https://github.com/BerriAI/litellm/pull/10084)
- **Fireworks AI**
  
  1. return tool calling responses in `tool_calls` field (fireworks incorrectly returns this as a json str in content) [PR](https://github.com/BerriAI/litellm/pull/10130)
- **Triton**
  
  1. Remove fixed remove bad\_words / stop words from `/generate` call - [Get Started](https://docs.litellm.ai/docs/providers/triton-inference-server#triton-generate---chat-completion), [PR](https://github.com/BerriAI/litellm/pull/10163)
- **Other**
  
  1. Support for all litellm providers on Responses API (works with Codex) - [Get Started](https://docs.litellm.ai/docs/tutorials/openai_codex), [PR](https://github.com/BerriAI/litellm/pull/10132)
  2. Fix combining multiple tool calls in streaming response - [Get Started](https://docs.litellm.ai/docs/completion/stream#helper-function), [PR](https://github.com/BerriAI/litellm/pull/10040)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- **Cost Control** - inject cache control points in prompt for cost reduction [Get Started](https://docs.litellm.ai/docs/tutorials/prompt_caching), [PR](https://github.com/BerriAI/litellm/pull/10000)
- **Spend Tags** - spend tags in headers - support x-litellm-tags even if tag based routing not enabled [Get Started](https://docs.litellm.ai/docs/proxy/request_headers#litellm-headers), [PR](https://github.com/BerriAI/litellm/pull/10000)
- **Gemini-2.5-flash** - support cost calculation for reasoning tokens [PR](https://github.com/BerriAI/litellm/pull/10141)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Users**
  
  1. Show created\_at and updated\_at on users page - [PR](https://github.com/BerriAI/litellm/pull/10033)
- **Virtual Keys**
  
  1. Filter by key alias - [https://github.com/BerriAI/litellm/pull/10085](https://github.com/BerriAI/litellm/pull/10085)
- **Usage Tab**
  
  1. Team based usage
     
     - New `LiteLLM_DailyTeamSpend` Table for aggregate team based usage logging - [PR](https://github.com/BerriAI/litellm/pull/10039)
     - New Team based usage dashboard + new `/team/daily/activity` API - [PR](https://github.com/BerriAI/litellm/pull/10081)
     - Return team alias on /team/daily/activity API - [PR](https://github.com/BerriAI/litellm/pull/10157)
     - allow internal user view spend for teams they belong to - [PR](https://github.com/BerriAI/litellm/pull/10157)
     - allow viewing top keys by team - [PR](https://github.com/BerriAI/litellm/pull/10157)
  2. Tag Based Usage
     
     - New `LiteLLM_DailyTagSpend` Table for aggregate tag based usage logging - [PR](https://github.com/BerriAI/litellm/pull/10071)
     - Restrict to only Proxy Admins - [PR](https://github.com/BerriAI/litellm/pull/10157)
     - allow viewing top keys by tag
     - Return tags passed in request (i.e. dynamic tags) on `/tag/list` API - [PR](https://github.com/BerriAI/litellm/pull/10157)
  3. Track prompt caching metrics in daily user, team, tag tables - [PR](https://github.com/BerriAI/litellm/pull/10029)
  4. Show usage by key (on all up, team, and tag usage dashboards) - [PR](https://github.com/BerriAI/litellm/pull/10157)
  5. swap old usage with new usage tab
- **Models**
  
  1. Make columns resizable/hideable - [PR](https://github.com/BerriAI/litellm/pull/10119)
- **API Playground**
  
  1. Allow internal user to call api playground - [PR](https://github.com/BerriAI/litellm/pull/10157)
- **SCIM**
  
  1. Add LiteLLM SCIM Integration for Team and User management - [Get Started](https://docs.litellm.ai/docs/tutorials/scim_litellm), [PR](https://github.com/BerriAI/litellm/pull/10072)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- **GCS**
  
  1. Fix gcs pub sub logging with env var GCS\_PROJECT\_ID - [Get Started](https://docs.litellm.ai/docs/observability/gcs_bucket_integration#usage), [PR](https://github.com/BerriAI/litellm/pull/10042)
- **AIM**
  
  1. Add litellm call id passing to Aim guardrails on pre and post-hooks calls - [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/aim_security), [PR](https://github.com/BerriAI/litellm/pull/10021)
- **Azure blob storage**
  
  1. Ensure logging works in high throughput scenarios - [Get Started](https://docs.litellm.ai/docs/proxy/logging#azure-blob-storage), [PR](https://github.com/BerriAI/litellm/pull/9962)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Support setting `litellm.modify_params` via env var** [PR](https://github.com/BerriAI/litellm/pull/9964)
- **Model Discovery** - Check provider’s `/models` endpoints when calling proxy’s `/v1/models` endpoint - [Get Started](https://docs.litellm.ai/docs/proxy/model_discovery), [PR](https://github.com/BerriAI/litellm/pull/9958)
- **`/utils/token_counter`** - fix retrieving custom tokenizer for db models - [Get Started](https://docs.litellm.ai/docs/proxy/configs#set-custom-tokenizer), [PR](https://github.com/BerriAI/litellm/pull/10047)
- **Prisma migrate** - handle existing columns in db table - [PR](https://github.com/BerriAI/litellm/pull/10138)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.66.0-stable
```

v1.66.0-stable is live now, here are the key highlights of this release

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Realtime API Cost Tracking**: Track cost of realtime API calls
- **Microsoft SSO Auto-sync**: Auto-sync groups and group members from Azure Entra ID to LiteLLM
- **xAI grok-3**: Added support for `xai/grok-3` models
- **Security Fixes**: Fixed [CVE-2025-0330](https://www.cve.org/CVERecord?id=CVE-2025-0330) and [CVE-2024-6825](https://www.cve.org/CVERecord?id=CVE-2024-6825) vulnerabilities

Let's dive in.

## Realtime API Cost Tracking[​](#realtime-api-cost-tracking "Direct link to Realtime API Cost Tracking")

This release adds Realtime API logging + cost tracking.

- **Logging**: LiteLLM now logs the complete response from realtime calls to all logging integrations (DB, S3, Langfuse, etc.)
- **Cost Tracking**: You can now set 'base\_model' and custom pricing for realtime models. [Custom Pricing](https://docs.litellm.ai/docs/proxy/custom_pricing)
- **Budgets**: Your key/user/team budgets now work for realtime models as well.

Start [here](https://docs.litellm.ai/docs/realtime)

## Microsoft SSO Auto-sync[​](#microsoft-sso-auto-sync "Direct link to Microsoft SSO Auto-sync")

Auto-sync groups and members from Azure Entra ID to LiteLLM

This release adds support for auto-syncing groups and members on Microsoft Entra ID with LiteLLM. This means that LiteLLM proxy administrators can spend less time managing teams and members and LiteLLM handles the following:

- Auto-create teams that exist on Microsoft Entra ID
- Sync team members on Microsoft Entra ID with LiteLLM teams

Get started with this [here](https://docs.litellm.ai/docs/tutorials/msft_sso)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **xAI**
  
  1. Added reasoning\_effort support for `xai/grok-3-mini-beta` [Get Started](https://docs.litellm.ai/docs/providers/xai#reasoning-usage)
  2. Added cost tracking for `xai/grok-3` models [PR](https://github.com/BerriAI/litellm/pull/9920)
- **Hugging Face**
  
  1. Added inference providers support [Get Started](https://docs.litellm.ai/docs/providers/huggingface#serverless-inference-providers)
- **Azure**
  
  1. Added azure/gpt-4o-realtime-audio cost tracking [PR](https://github.com/BerriAI/litellm/pull/9893)
- **VertexAI**
  
  1. Added enterpriseWebSearch tool support [Get Started](https://docs.litellm.ai/docs/providers/vertex#grounding---web-search)
  2. Moved to only passing keys accepted by the Vertex AI response schema [PR](https://github.com/BerriAI/litellm/pull/8992)
- **Google AI Studio**
  
  1. Added cost tracking for `gemini-2.5-pro` [PR](https://github.com/BerriAI/litellm/pull/9837)
  2. Fixed pricing for 'gemini/gemini-2.5-pro-preview-03-25' [PR](https://github.com/BerriAI/litellm/pull/9896)
  3. Fixed handling file\_data being passed in [PR](https://github.com/BerriAI/litellm/pull/9786)
- **Azure**
  
  1. Updated Azure Phi-4 pricing [PR](https://github.com/BerriAI/litellm/pull/9862)
  2. Added azure/gpt-4o-realtime-audio cost tracking [PR](https://github.com/BerriAI/litellm/pull/9893)
- **Databricks**
  
  1. Removed reasoning\_effort from parameters [PR](https://github.com/BerriAI/litellm/pull/9811)
  2. Fixed custom endpoint check for Databricks [PR](https://github.com/BerriAI/litellm/pull/9925)
- **General**
  
  1. Added litellm.supports\_reasoning() util to track if an llm supports reasoning [Get Started](https://docs.litellm.ai/docs/providers/anthropic#reasoning)
  2. Function Calling - Handle pydantic base model in message tool calls, handle tools = \[], and support fake streaming on tool calls for meta.llama3-3-70b-instruct-v1:0 [PR](https://github.com/BerriAI/litellm/pull/9774)
  3. LiteLLM Proxy - Allow passing `thinking` param to litellm proxy via client sdk [PR](https://github.com/BerriAI/litellm/pull/9386)
  4. Fixed correctly translating 'thinking' param for litellm [PR](https://github.com/BerriAI/litellm/pull/9904)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- **OpenAI, Azure**
  
  1. Realtime API Cost tracking with token usage metrics in spend logs [Get Started](https://docs.litellm.ai/docs/realtime)
- **Anthropic**
  
  1. Fixed Claude Haiku cache read pricing per token [PR](https://github.com/BerriAI/litellm/pull/9834)
  2. Added cost tracking for Claude responses with base\_model [PR](https://github.com/BerriAI/litellm/pull/9897)
  3. Fixed Anthropic prompt caching cost calculation and trimmed logged message in db [PR](https://github.com/BerriAI/litellm/pull/9838)
- **General**
  
  1. Added token tracking and log usage object in spend logs [PR](https://github.com/BerriAI/litellm/pull/9843)
  2. Handle custom pricing at deployment level [PR](https://github.com/BerriAI/litellm/pull/9855)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Test Key Tab**
  
  1. Added rendering of Reasoning content, ttft, usage metrics on test key page [PR](https://github.com/BerriAI/litellm/pull/9931)
  
  View input, output, reasoning tokens, ttft metrics.
- **Tag / Policy Management**
  
  1. Added Tag/Policy Management. Create routing rules based on request metadata. This allows you to enforce that requests with `tags="private"` only go to specific models. [Get Started](https://docs.litellm.ai/docs/tutorials/tag_management)
  
  Create and manage tags.
- **Redesigned Login Screen**
  
  1. Polished login screen [PR](https://github.com/BerriAI/litellm/pull/9778)
- **Microsoft SSO Auto-Sync**
  
  1. Added debug route to allow admins to debug SSO JWT fields [PR](https://github.com/BerriAI/litellm/pull/9835)
  2. Added ability to use MSFT Graph API to assign users to teams [PR](https://github.com/BerriAI/litellm/pull/9865)
  3. Connected litellm to Azure Entra ID Enterprise Application [PR](https://github.com/BerriAI/litellm/pull/9872)
  4. Added ability for admins to set `default_team_params` for when litellm SSO creates default teams [PR](https://github.com/BerriAI/litellm/pull/9895)
  5. Fixed MSFT SSO to use correct field for user email [PR](https://github.com/BerriAI/litellm/pull/9886)
  6. Added UI support for setting Default Team setting when litellm SSO auto creates teams [PR](https://github.com/BerriAI/litellm/pull/9918)
- **UI Bug Fixes**
  
  1. Prevented team, key, org, model numerical values changing on scrolling [PR](https://github.com/BerriAI/litellm/pull/9776)
  2. Instantly reflect key and team updates in UI [PR](https://github.com/BerriAI/litellm/pull/9825)

## Logging / Guardrail Improvements[​](#logging--guardrail-improvements "Direct link to Logging / Guardrail Improvements")

- **Prometheus**
  
  1. Emit Key and Team Budget metrics on a cron job schedule [Get Started](https://docs.litellm.ai/docs/proxy/prometheus#initialize-budget-metrics-on-startup)

## Security Fixes[​](#security-fixes "Direct link to Security Fixes")

- Fixed [CVE-2025-0330](https://www.cve.org/CVERecord?id=CVE-2025-0330) - Leakage of Langfuse API keys in team exception handling [PR](https://github.com/BerriAI/litellm/pull/9830)
- Fixed [CVE-2024-6825](https://www.cve.org/CVERecord?id=CVE-2024-6825) - Remote code execution in post call rules [PR](https://github.com/BerriAI/litellm/pull/9826)

## Helm[​](#helm "Direct link to Helm")

- Added service annotations to litellm-helm chart [PR](https://github.com/BerriAI/litellm/pull/9840)
- Added extraEnvVars to the helm deployment [PR](https://github.com/BerriAI/litellm/pull/9292)

## Demo[​](#demo "Direct link to Demo")

Try this on the demo instance [today](https://docs.litellm.ai/docs/proxy/demo)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

See the complete git diff since v1.65.4-stable, [here](https://github.com/BerriAI/litellm/releases/tag/v1.66.0-stable)

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.65.4-stable
```

v1.65.4-stable is live. Here are the improvements since v1.65.0-stable.

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Preventing DB Deadlocks**: Fixes a high-traffic issue when multiple instances were writing to the DB at the same time.
- **New Usage Tab**: Enables viewing spend by model and customizing date range

Let's dive in.

### Preventing DB Deadlocks[​](#preventing-db-deadlocks "Direct link to Preventing DB Deadlocks")

This release fixes the DB deadlocking issue that users faced in high traffic (10K+ RPS). This is great because it enables user/key/team spend tracking works at that scale.

Read more about the new architecture [here](https://docs.litellm.ai/docs/proxy/db_deadlocks)

### New Usage Tab[​](#new-usage-tab "Direct link to New Usage Tab")

The new Usage tab now brings the ability to track daily spend by model. This makes it easier to catch any spend tracking or token counting errors, when combined with the ability to view successful requests, and token usage.

To test this out, just go to Experimental &gt; New Usage &gt; Activity.

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

1. Databricks - claude-3-7-sonnet cost tracking [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L10350)
2. VertexAI - `gemini-2.5-pro-exp-03-25` cost tracking [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L4492)
3. VertexAI - `gemini-2.0-flash` cost tracking [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L4689)
4. Groq - add whisper ASR models to model cost map [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L3324)
5. IBM - Add watsonx/ibm/granite-3-8b-instruct to model cost map [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L91)
6. Google AI Studio - add gemini/gemini-2.5-pro-preview-03-25 to model cost map [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L4850)

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

01. Vertex AI - Support anyOf param for OpenAI json schema translation [Get Started](https://docs.litellm.ai/docs/providers/vertex#json-schema)
02. Anthropic- response\_format + thinking param support (works across Anthropic API, Bedrock, Vertex) [Get Started](https://docs.litellm.ai/docs/reasoning_content)
03. Anthropic - if thinking token is specified and max tokens is not - ensure max token to anthropic is higher than thinking tokens (works across Anthropic API, Bedrock, Vertex) [PR](https://github.com/BerriAI/litellm/pull/9594)
04. Bedrock - latency optimized inference support [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---latency-optimized-inference)
05. Sagemaker - handle special tokens + multibyte character code in response [Get Started](https://docs.litellm.ai/docs/providers/aws_sagemaker)
06. MCP - add support for using SSE MCP servers [Get Started](https://docs.litellm.ai/docs/mcp#usage)
07. Anthropic - new `litellm.messages.create` interface for calling Anthropic `/v1/messages` via passthrough [Get Started](https://docs.litellm.ai/docs/anthropic_unified#usage)
08. Anthropic - support ‘file’ content type in message param (works across Anthropic API, Bedrock, Vertex) [Get Started](https://docs.litellm.ai/docs/providers/anthropic#usage---pdf)
09. Anthropic - map openai 'reasoning\_effort' to anthropic 'thinking' param (works across Anthropic API, Bedrock, Vertex) [Get Started](https://docs.litellm.ai/docs/providers/anthropic#usage---thinking--reasoning_content)
10. Google AI Studio (Gemini) - \[BETA] `/v1/files` upload support [Get Started](https://docs.litellm.ai/docs/providers/google_ai_studio/files)
11. Azure - fix o-series tool calling [Get Started](https://docs.litellm.ai/docs/providers/azure#tool-calling--function-calling)
12. Unified file id - \[ALPHA] allow calling multiple providers with same file id [PR](https://github.com/BerriAI/litellm/pull/9718)
    
    - This is experimental, and not recommended for production use.
    - We plan to have a production-ready implementation by next week.
13. Google AI Studio (Gemini) - return logprobs [PR](https://github.com/BerriAI/litellm/pull/9713)
14. Anthropic - Support prompt caching for Anthropic tool calls [Get Started](https://docs.litellm.ai/docs/completion/prompt_caching)
15. OpenRouter - unwrap extra body on open router calls [PR](https://github.com/BerriAI/litellm/pull/9747)
16. VertexAI - fix credential caching issue [PR](https://github.com/BerriAI/litellm/pull/9756)
17. XAI - filter out 'name' param for XAI [PR](https://github.com/BerriAI/litellm/pull/9761)
18. Gemini - image generation output support [Get Started](https://docs.litellm.ai/docs/providers/gemini#image-generation)
19. Databricks - support claude-3-7-sonnet w/ thinking + response\_format [Get Started](https://docs.litellm.ai/docs/providers/databricks#usage---thinking--reasoning_content)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Reliability fix - Check sent and received model for cost calculation [PR](https://github.com/BerriAI/litellm/pull/9669)
2. Vertex AI - Multimodal embedding cost tracking [Get Started](https://docs.litellm.ai/docs/providers/vertex#multi-modal-embeddings), [PR](https://github.com/BerriAI/litellm/pull/9623)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

1. New Usage Tab
   
   - Report 'total\_tokens' + report success/failure calls
   - Remove double bars on scroll
   - Ensure ‘daily spend’ chart ordered from earliest to latest date
   - showing spend per model per day
   - show key alias on usage tab
   - Allow non-admins to view their activity
   - Add date picker to new usage tab
2. Virtual Keys Tab
   
   - remove 'default key' on user signup
   - fix showing user models available for personal key creation
3. Test Key Tab
   
   - Allow testing image generation models
4. Models Tab
   
   - Fix bulk adding models
   - support reusable credentials for passthrough endpoints
   - Allow team members to see team models
5. Teams Tab
   
   - Fix json serialization error on update team metadata
6. Request Logs Tab
   
   - Add reasoning\_content token tracking across all providers on streaming
7. API
   
   - return key alias on /user/daily/activity [Get Started](https://docs.litellm.ai/docs/proxy/cost_tracking#daily-spend-breakdown-api)
8. SSO
   
   - Allow assigning SSO users to teams on MSFT SSO [PR](https://github.com/BerriAI/litellm/pull/9745)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Console Logs - Add json formatting for uncaught exceptions [PR](https://github.com/BerriAI/litellm/pull/9619)
2. Guardrails - AIM Guardrails support for virtual key based policies [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/aim_security)
3. Logging - fix completion start time tracking [PR](https://github.com/BerriAI/litellm/pull/9688)
4. Prometheus
   
   - Allow adding authentication on Prometheus /metrics endpoints [PR](https://github.com/BerriAI/litellm/pull/9766)
   - Distinguish LLM Provider Exception vs. LiteLLM Exception in metric naming [PR](https://github.com/BerriAI/litellm/pull/9760)
   - Emit operational metrics for new DB Transaction architecture [PR](https://github.com/BerriAI/litellm/pull/9719)

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

1. Preventing Deadlocks
   
   - Reduce DB Deadlocks by storing spend updates in Redis and then committing to DB [PR](https://github.com/BerriAI/litellm/pull/9608)
   - Ensure no deadlocks occur when updating DailyUserSpendTransaction [PR](https://github.com/BerriAI/litellm/pull/9690)
   - High Traffic fix - ensure new DB + Redis architecture accurately tracks spend [PR](https://github.com/BerriAI/litellm/pull/9673)
   - Use Redis for PodLock Manager instead of PG (ensures no deadlocks occur) [PR](https://github.com/BerriAI/litellm/pull/9715)
   - v2 DB Deadlock Reduction Architecture – Add Max Size for In-Memory Queue + Backpressure Mechanism [PR](https://github.com/BerriAI/litellm/pull/9759)
2. Prisma Migrations [Get Started](https://docs.litellm.ai/docs/proxy/prod#9-use-prisma-migrate-deploy)
   
   - connects litellm proxy to litellm's prisma migration files
   - Handle db schema updates from new `litellm-proxy-extras` sdk
3. Redis - support password for sync sentinel clients [PR](https://github.com/BerriAI/litellm/pull/9622)
4. Fix "Circular reference detected" error when max\_parallel\_requests = 0 [PR](https://github.com/BerriAI/litellm/pull/9671)
5. Code QA - Ban hardcoded numbers [PR](https://github.com/BerriAI/litellm/pull/9709)

## Helm[​](#helm "Direct link to Helm")

1. fix: wrong indentation of ttlSecondsAfterFinished in chart [PR](https://github.com/BerriAI/litellm/pull/9611)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Fix - only apply service\_account\_settings.enforced\_params on service accounts [PR](https://github.com/BerriAI/litellm/pull/9683)
2. Fix - handle metadata null on `/chat/completion` [PR](https://github.com/BerriAI/litellm/issues/9717)
3. Fix - Move daily user transaction logging outside of 'disable\_spend\_logs' flag, as they’re unrelated [PR](https://github.com/BerriAI/litellm/pull/9772)

## Demo[​](#demo "Direct link to Demo")

Try this on the demo instance [today](https://docs.litellm.ai/docs/proxy/demo)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

See the complete git diff since v1.65.0-stable, [here](https://github.com/BerriAI/litellm/releases/tag/v1.65.4-stable)

v1.65.0-stable is live now. Here are the key highlights of this release:

- **MCP Support**: Support for adding and using MCP servers on the LiteLLM proxy.
- **UI view total usage after 1M+ logs**: You can now view usage analytics after crossing 1M+ logs in DB.

## Model Context Protocol (MCP)[​](#model-context-protocol-mcp "Direct link to Model Context Protocol (MCP)")

This release introduces support for centrally adding MCP servers on LiteLLM. This allows you to add MCP server endpoints and your developers can `list` and `call` MCP tools through LiteLLM.

Read more about MCP [here](https://docs.litellm.ai/docs/mcp).

Expose and use MCP servers through LiteLLM

## UI view total usage after 1M+ logs[​](#ui-view-total-usage-after-1m-logs "Direct link to UI view total usage after 1M+ logs")

This release brings the ability to view total usage analytics even after exceeding 1M+ logs in your database. We've implemented a scalable architecture that stores only aggregate usage data, resulting in significantly more efficient queries and reduced database CPU utilization.

View total usage after 1M+ logs

- How this works:
  
  - We now aggregate usage data into a dedicated DailyUserSpend table, significantly reducing query load and CPU usage even beyond 1M+ logs.
- Daily Spend Breakdown API:
  
  - Retrieve granular daily usage data (by model, provider, and API key) with a single endpoint. Example Request:
  
  Daily Spend Breakdown API
  
  ```
  curl -L -X GET 'http://localhost:4000/user/daily/activity?start_date=2025-03-20&end_date=2025-03-27' \
  -H 'Authorization: Bearer sk-...'
  ```
  
  Daily Spend Breakdown API Response
  
  ```
  {
  "results":[
  {
  "date":"2025-03-27",
  "metrics":{
  "spend":0.0177072,
  "prompt_tokens":111,
  "completion_tokens":1711,
  "total_tokens":1822,
  "api_requests":11
  },
  "breakdown":{
  "models":{
  "gpt-4o-mini":{
  "spend":1.095e-05,
  "prompt_tokens":37,
  "completion_tokens":9,
  "total_tokens":46,
  "api_requests":1
  },
  "providers":{"openai":{ ... },"azure_ai":{ ... }},
  "api_keys":{"3126b6eaf1...":{ ... }}
  }
  }
  ],
  "metadata":{
  "total_spend":0.7274667,
  "total_prompt_tokens":280990,
  "total_completion_tokens":376674,
  "total_api_requests":14
  }
  }
  ```

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- Support for Vertex AI gemini-2.0-flash-lite & Google AI Studio gemini-2.0-flash-lite [PR](https://github.com/BerriAI/litellm/pull/9523)
- Support for Vertex AI Fine-Tuned LLMs [PR](https://github.com/BerriAI/litellm/pull/9542)
- Nova Canvas image generation support [PR](https://github.com/BerriAI/litellm/pull/9525)
- OpenAI gpt-4o-transcribe support [PR](https://github.com/BerriAI/litellm/pull/9517)
- Added new Vertex AI text embedding model [PR](https://github.com/BerriAI/litellm/pull/9476)

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

- OpenAI Web Search Tool Call Support [PR](https://github.com/BerriAI/litellm/pull/9465)
- Vertex AI topLogprobs support [PR](https://github.com/BerriAI/litellm/pull/9518)
- Support for sending images and video to Vertex AI multimodal embedding [Doc](https://docs.litellm.ai/docs/providers/vertex#multi-modal-embeddings)
- Support litellm.api\_base for Vertex AI + Gemini across completion, embedding, image\_generation [PR](https://github.com/BerriAI/litellm/pull/9516)
- Bug fix for returning `response_cost` when using litellm python SDK with LiteLLM Proxy [PR](https://github.com/BerriAI/litellm/commit/6fd18651d129d606182ff4b980e95768fc43ca3d)
- Support for `max_completion_tokens` on Mistral API [PR](https://github.com/BerriAI/litellm/pull/9606)
- Refactored Vertex AI passthrough routes - fixes unpredictable behaviour with auto-setting default\_vertex\_region on router model add [PR](https://github.com/BerriAI/litellm/pull/9467)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- Log 'api\_base' on spend logs [PR](https://github.com/BerriAI/litellm/pull/9509)
- Support for Gemini audio token cost tracking [PR](https://github.com/BerriAI/litellm/pull/9535)
- Fixed OpenAI audio input token cost tracking [PR](https://github.com/BerriAI/litellm/pull/9535)

## UI[​](#ui "Direct link to UI")

### Model Management[​](#model-management "Direct link to Model Management")

- Allowed team admins to add/update/delete models on UI [PR](https://github.com/BerriAI/litellm/pull/9572)
- Added render supports\_web\_search on model hub [PR](https://github.com/BerriAI/litellm/pull/9469)

### Request Logs[​](#request-logs "Direct link to Request Logs")

- Show API base and model ID on request logs [PR](https://github.com/BerriAI/litellm/pull/9572)
- Allow viewing keyinfo on request logs [PR](https://github.com/BerriAI/litellm/pull/9568)

### Usage Tab[​](#usage-tab "Direct link to Usage Tab")

- Added Daily User Spend Aggregate view - allows UI Usage tab to work &gt; 1m rows [PR](https://github.com/BerriAI/litellm/pull/9538)
- Connected UI to "LiteLLM\_DailyUserSpend" spend table [PR](https://github.com/BerriAI/litellm/pull/9603)

## Logging Integrations[​](#logging-integrations "Direct link to Logging Integrations")

- Fixed StandardLoggingPayload for GCS Pub Sub Logging Integration [PR](https://github.com/BerriAI/litellm/pull/9508)
- Track `litellm_model_name` on `StandardLoggingPayload` [Docs](https://docs.litellm.ai/docs/proxy/logging_spec#standardlogginghiddenparams)

## Performance / Reliability Improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

- LiteLLM Redis semantic caching implementation [PR](https://github.com/BerriAI/litellm/pull/9356)
- Gracefully handle exceptions when DB is having an outage [PR](https://github.com/BerriAI/litellm/pull/9533)
- Allow Pods to startup + passing /health/readiness when allow\_requests\_on\_db\_unavailable: True and DB is down [PR](https://github.com/BerriAI/litellm/pull/9569)

## General Improvements[​](#general-improvements "Direct link to General Improvements")

- Support for exposing MCP tools on litellm proxy [PR](https://github.com/BerriAI/litellm/pull/9426)
- Support discovering Gemini, Anthropic, xAI models by calling their /v1/model endpoint [PR](https://github.com/BerriAI/litellm/pull/9530)
- Fixed route check for non-proxy admins on JWT auth [PR](https://github.com/BerriAI/litellm/pull/9454)
- Added baseline Prisma database migrations [PR](https://github.com/BerriAI/litellm/pull/9565)
- View all wildcard models on /model/info [PR](https://github.com/BerriAI/litellm/pull/9572)

## Security[​](#security "Direct link to Security")

- Bumped next from 14.2.21 to 14.2.25 in UI dashboard [PR](https://github.com/BerriAI/litellm/pull/9458)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.63.14-stable.patch1...v1.65.0-stable)

v1.65.0 updates the `/model/new` endpoint to prevent non-team admins from creating team models.

This means that only proxy admins or team admins can create team models.

## Additional Changes[​](#additional-changes "Direct link to Additional Changes")

- Allows team admins to call `/model/update` to update team models.
- Allows team admins to call `/model/delete` to delete team models.
- Introduces new `user_models_only` param to `/v2/model/info` - only return models added by this user.

These changes enable team admins to add and manage models for their team on the LiteLLM UI + API.

These are the changes since `v1.63.11-stable`.

This release brings:

- LLM Translation Improvements (MCP Support and Bedrock Application Profiles)
- Perf improvements for Usage-based Routing
- Streaming guardrail support via websockets
- Azure OpenAI client perf fix (from previous release)

## Docker Run LiteLLM Proxy[​](#docker-run-litellm-proxy "Direct link to Docker Run LiteLLM Proxy")

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.63.14-stable.patch1
```

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- Azure gpt-4o - fixed pricing to latest global pricing - [PR](https://github.com/BerriAI/litellm/pull/9361)
- O1-Pro - add pricing + model information - [PR](https://github.com/BerriAI/litellm/pull/9397)
- Azure AI - mistral 3.1 small pricing added - [PR](https://github.com/BerriAI/litellm/pull/9453)
- Azure - gpt-4.5-preview pricing added - [PR](https://github.com/BerriAI/litellm/pull/9453)

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

1. **New LLM Features**

<!--THE END-->

- Bedrock: Support bedrock application inference profiles [Docs](https://docs.litellm.ai/docs/providers/bedrock#bedrock-application-inference-profile)
  
  - Infer aws region from bedrock application profile id - (`arn:aws:bedrock:us-east-1:...`)
- Ollama - support calling via `/v1/completions` [Get Started](https://docs.litellm.ai/docs/providers/ollama#using-ollama-fim-on-v1completions)
- Bedrock - support `us.deepseek.r1-v1:0` model name [Docs](https://docs.litellm.ai/docs/providers/bedrock#supported-aws-bedrock-models)
- OpenRouter - `OPENROUTER_API_BASE` env var support [Docs](https://docs.litellm.ai/docs/providers/openrouter.md)
- Azure - add audio model parameter support - [Docs](https://docs.litellm.ai/docs/providers/azure#azure-audio-model)
- OpenAI - PDF File support [Docs](https://docs.litellm.ai/docs/completion/document_understanding#openai-file-message-type)
- OpenAI - o1-pro Responses API streaming support [Docs](https://docs.litellm.ai/docs/response_api.md#streaming)
- \[BETA] MCP - Use MCP Tools with LiteLLM SDK [Docs](https://docs.litellm.ai/docs/mcp)

<!--THE END-->

2. **Bug Fixes**

<!--THE END-->

- Voyage: prompt token on embedding tracking fix - [PR](https://github.com/BerriAI/litellm/commit/56d3e75b330c3c3862dc6e1c51c1210e48f1068e)
- Sagemaker - Fix ‘Too little data for declared Content-Length’ error - [PR](https://github.com/BerriAI/litellm/pull/9326)
- OpenAI-compatible models - fix issue when calling openai-compatible models w/ custom\_llm\_provider set - [PR](https://github.com/BerriAI/litellm/pull/9355)
- VertexAI - Embedding ‘outputDimensionality’ support - [PR](https://github.com/BerriAI/litellm/commit/437dbe724620675295f298164a076cbd8019d304)
- Anthropic - return consistent json response format on streaming/non-streaming - [PR](https://github.com/BerriAI/litellm/pull/9437)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- `litellm_proxy/` - support reading litellm response cost header from proxy, when using client sdk
- Reset Budget Job - fix budget reset error on keys/teams/users [PR](https://github.com/BerriAI/litellm/pull/9329)
- Streaming - Prevents final chunk w/ usage from being ignored (impacted bedrock streaming + cost tracking) [PR](https://github.com/BerriAI/litellm/pull/9314)

## UI[​](#ui "Direct link to UI")

1. Users Page
   
   - Feature: Control default internal user settings [PR](https://github.com/BerriAI/litellm/pull/9328)
2. Icons:
   
   - Feature: Replace external "artificialanalysis.ai" icons by local svg [PR](https://github.com/BerriAI/litellm/pull/9374)
3. Sign In/Sign Out
   
   - Fix: Default login when `default_user_id` user does not exist in DB [PR](https://github.com/BerriAI/litellm/pull/9395)

## Logging Integrations[​](#logging-integrations "Direct link to Logging Integrations")

- Support post-call guardrails for streaming responses [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#1-write-a-customguardrail-class)
- Arize [Get Started](https://docs.litellm.ai/docs/observability/arize_integration)
  
  - fix invalid package import [PR](https://github.com/BerriAI/litellm/pull/9338)
  - migrate to using standardloggingpayload for metadata, ensures spans land successfully [PR](https://github.com/BerriAI/litellm/pull/9338)
  - fix logging to just log the LLM I/O [PR](https://github.com/BerriAI/litellm/pull/9353)
  - Dynamic API Key/Space param support [Get Started](https://docs.litellm.ai/docs/observability/arize_integration#pass-arize-spacekey-per-request)
- StandardLoggingPayload - Log litellm\_model\_name in payload. Allows knowing what the model sent to API provider was [Get Started](https://docs.litellm.ai/docs/proxy/logging_spec#standardlogginghiddenparams)
- Prompt Management - Allow building custom prompt management integration [Get Started](https://docs.litellm.ai/docs/proxy/custom_prompt_management.md)

## Performance / Reliability improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability improvements")

- Redis Caching - add 5s default timeout, prevents hanging redis connection from impacting llm calls [PR](https://github.com/BerriAI/litellm/commit/db92956ae33ed4c4e3233d7e1b0c7229817159bf)
- Allow disabling all spend updates / writes to DB - patch to allow disabling all spend updates to DB with a flag [PR](https://github.com/BerriAI/litellm/pull/9331)
- Azure OpenAI - correctly re-use azure openai client, fixes perf issue from previous Stable release [PR](https://github.com/BerriAI/litellm/commit/f2026ef907c06d94440930917add71314b901413)
- Azure OpenAI - uses litellm.ssl\_verify on Azure/OpenAI clients [PR](https://github.com/BerriAI/litellm/commit/f2026ef907c06d94440930917add71314b901413)
- Usage-based routing - Wildcard model support [Get Started](https://docs.litellm.ai/docs/proxy/usage_based_routing#wildcard-model-support)
- Usage-based routing - Support batch writing increments to redis - reduces latency to same as ‘simple-shuffle’ [PR](https://github.com/BerriAI/litellm/pull/9357)
- Router - show reason for model cooldown on ‘no healthy deployments available error’ [PR](https://github.com/BerriAI/litellm/pull/9438)
- Caching - add max value limit to an item in in-memory cache (1MB) - prevents OOM errors on large image url’s being sent through proxy [PR](https://github.com/BerriAI/litellm/pull/9448)

## General Improvements[​](#general-improvements "Direct link to General Improvements")

- Passthrough Endpoints - support returning api-base on pass-through endpoints Response Headers [Docs](https://docs.litellm.ai/docs/proxy/response_headers#litellm-specific-headers)
- SSL - support reading ssl security level from env var - Allows user to specify lower security settings [Get Started](https://docs.litellm.ai/docs/guides/security_settings)
- Credentials - only poll Credentials table when `STORE_MODEL_IN_DB` is True [PR](https://github.com/BerriAI/litellm/pull/9376)
- Image URL Handling - new architecture doc on image url handling [Docs](https://docs.litellm.ai/docs/proxy/image_handling)
- OpenAI - bump to pip install "openai==1.68.2" [PR](https://github.com/BerriAI/litellm/commit/e85e3bc52a9de86ad85c3dbb12d87664ee567a5a)
- Gunicorn - security fix - bump gunicorn==23.0.0 [PR](https://github.com/BerriAI/litellm/commit/7e9fc92f5c7fea1e7294171cd3859d55384166eb)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.63.11-stable...v1.63.14.rc)

These are the changes since `v1.63.2-stable`.

This release is primarily focused on:

- \[Beta] Responses API Support
- Snowflake Cortex Support, Amazon Nova Image Generation
- UI - Credential Management, re-use credentials when adding new models
- UI - Test Connection to LLM Provider before adding a model

## Known Issues[​](#known-issues "Direct link to Known Issues")

- 🚨 Known issue on Azure OpenAI - We don't recommend upgrading if you use Azure OpenAI. This version failed our Azure OpenAI load test

## Docker Run LiteLLM Proxy[​](#docker-run-litellm-proxy "Direct link to Docker Run LiteLLM Proxy")

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.63.11-stable
```

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- Image Generation support for Amazon Nova Canvas [Getting Started](https://docs.litellm.ai/docs/providers/bedrock#image-generation)
- Add pricing for Jamba new models [PR](https://github.com/BerriAI/litellm/pull/9032/files)
- Add pricing for Amazon EU models [PR](https://github.com/BerriAI/litellm/pull/9056/files)
- Add Bedrock Deepseek R1 model pricing [PR](https://github.com/BerriAI/litellm/pull/9108/files)
- Update Gemini pricing: Gemma 3, Flash 2 thinking update, LearnLM [PR](https://github.com/BerriAI/litellm/pull/9190/files)
- Mark Cohere Embedding 3 models as Multimodal [PR](https://github.com/BerriAI/litellm/pull/9176/commits/c9a576ce4221fc6e50dc47cdf64ab62736c9da41)
- Add Azure Data Zone pricing [PR](https://github.com/BerriAI/litellm/pull/9185/files#diff-19ad91c53996e178c1921cbacadf6f3bae20cfe062bd03ee6bfffb72f847ee37)
  
  - LiteLLM Tracks cost for `azure/eu` and `azure/us` models

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

1. **New Endpoints**

<!--THE END-->

- \[Beta] POST `/responses` API. [Getting Started](https://docs.litellm.ai/docs/response_api)

<!--THE END-->

2. **New LLM Providers**

<!--THE END-->

- Snowflake Cortex [Getting Started](https://docs.litellm.ai/docs/providers/snowflake)

<!--THE END-->

3. **New LLM Features**

<!--THE END-->

- Support OpenRouter `reasoning_content` on streaming [Getting Started](https://docs.litellm.ai/docs/reasoning_content)

<!--THE END-->

4. **Bug Fixes**

<!--THE END-->

- OpenAI: Return `code`, `param` and `type` on bad request error [More information on litellm exceptions](https://docs.litellm.ai/docs/exception_mapping)
- Bedrock: Fix converse chunk parsing to only return empty dict on tool use [PR](https://github.com/BerriAI/litellm/pull/9166)
- Bedrock: Support extra\_headers [PR](https://github.com/BerriAI/litellm/pull/9113)
- Azure: Fix Function Calling Bug & Update Default API Version to `2025-02-01-preview` [PR](https://github.com/BerriAI/litellm/pull/9191)
- Azure: Fix AI services URL [PR](https://github.com/BerriAI/litellm/pull/9185)
- Vertex AI: Handle HTTP 201 status code in response [PR](https://github.com/BerriAI/litellm/pull/9193)
- Perplexity: Fix incorrect streaming response [PR](https://github.com/BerriAI/litellm/pull/9081)
- Triton: Fix streaming completions bug [PR](https://github.com/BerriAI/litellm/pull/8386)
- Deepgram: Support bytes.IO when handling audio files for transcription [PR](https://github.com/BerriAI/litellm/pull/9071)
- Ollama: Fix "system" role has become unacceptable [PR](https://github.com/BerriAI/litellm/pull/9261)
- All Providers (Streaming): Fix String `data:` stripped from entire content in streamed responses [PR](https://github.com/BerriAI/litellm/pull/9070)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Support Bedrock converse cache token tracking [Getting Started](https://docs.litellm.ai/docs/completion/prompt_caching)
2. Cost Tracking for Responses API [Getting Started](https://docs.litellm.ai/docs/response_api)
3. Fix Azure Whisper cost tracking [Getting Started](https://docs.litellm.ai/docs/audio_transcription)

## UI[​](#ui "Direct link to UI")

### Re-Use Credentials on UI[​](#re-use-credentials-on-ui "Direct link to Re-Use Credentials on UI")

You can now onboard LLM provider credentials on LiteLLM UI. Once these credentials are added you can re-use them when adding new models [Getting Started](https://docs.litellm.ai/docs/proxy/ui_credentials)

### Test Connections before adding models[​](#test-connections-before-adding-models "Direct link to Test Connections before adding models")

Before adding a model you can test the connection to the LLM provider to verify you have setup your API Base + API Key correctly

![](https://docs.litellm.ai/assets/images/litellm_test_connection-029765a2de4dcabccfe3be9a8d33dbdd.gif)

### General UI Improvements[​](#general-ui-improvements "Direct link to General UI Improvements")

1. Add Models Page
   
   - Allow adding Cerebras, Sambanova, Perplexity, Fireworks, Openrouter, TogetherAI Models, Text-Completion OpenAI on Admin UI
   - Allow adding EU OpenAI models
   - Fix: Instantly show edit + deletes to models
2. Keys Page
   
   - Fix: Instantly show newly created keys on Admin UI (don't require refresh)
   - Fix: Allow clicking into Top Keys when showing users Top API Key
   - Fix: Allow Filter Keys by Team Alias, Key Alias and Org
   - UI Improvements: Show 100 Keys Per Page, Use full height, increase width of key alias
3. Users Page
   
   - Fix: Show correct count of internal user keys on Users Page
   - Fix: Metadata not updating in Team UI
4. Logs Page
   
   - UI Improvements: Keep expanded log in focus on LiteLLM UI
   - UI Improvements: Minor improvements to logs page
   - Fix: Allow internal user to query their own logs
   - Allow switching off storing Error Logs in DB [Getting Started](https://docs.litellm.ai/docs/proxy/ui_logs)
5. Sign In/Sign Out
   
   - Fix: Correctly use `PROXY_LOGOUT_URL` when set [Getting Started](https://docs.litellm.ai/docs/proxy/self_serve#setting-custom-logout-urls)

## Security[​](#security "Direct link to Security")

1. Support for Rotating Master Keys [Getting Started](https://docs.litellm.ai/docs/proxy/master_key_rotations)
2. Fix: Internal User Viewer Permissions, don't allow `internal_user_viewer` role to see `Test Key Page` or `Create Key Button` [More information on role based access controls](https://docs.litellm.ai/docs/proxy/access_control)
3. Emit audit logs on All user + model Create/Update/Delete endpoints [Getting Started](https://docs.litellm.ai/docs/proxy/multiple_admins)
4. JWT
   
   - Support multiple JWT OIDC providers [Getting Started](https://docs.litellm.ai/docs/proxy/token_auth)
   - Fix JWT access with Groups not working when team is assigned All Proxy Models access
5. Using K/V pairs in 1 AWS Secret [Getting Started](https://docs.litellm.ai/docs/secret#using-kv-pairs-in-1-aws-secret)

## Logging Integrations[​](#logging-integrations "Direct link to Logging Integrations")

1. Prometheus: Track Azure LLM API latency metric [Getting Started](https://docs.litellm.ai/docs/proxy/prometheus#request-latency-metrics)
2. Athina: Added tags, user\_feedback and model\_options to additional\_keys which can be sent to Athina [Getting Started](https://docs.litellm.ai/docs/observability/athina_integration)

## Performance / Reliability improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability improvements")

1. Redis + litellm router - Fix Redis cluster mode for litellm router [PR](https://github.com/BerriAI/litellm/pull/9010)

## General Improvements[​](#general-improvements "Direct link to General Improvements")

1. OpenWebUI Integration - display `thinking` tokens

<!--THE END-->

- Guide on getting started with LiteLLM x OpenWebUI. [Getting Started](https://docs.litellm.ai/docs/tutorials/openweb_ui)
- Display `thinking` tokens on OpenWebUI (Bedrock, Anthropic, Deepseek) [Getting Started](https://docs.litellm.ai/docs/tutorials/openweb_ui#render-thinking-content-on-openweb-ui)

![](https://docs.litellm.ai/assets/images/litellm_thinking_openweb-5ec7dddb7e7b6a10252694c27cfc177d.gif)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.63.2-stable...v1.63.11-stable)

These are the changes since `v1.61.20-stable`.

This release is primarily focused on:

- LLM Translation improvements (more `thinking` content improvements)
- UI improvements (Error logs now shown on UI)

info

This release will be live on 03/09/2025

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

1. Add `supports_pdf_input` for specific Bedrock Claude models [PR](https://github.com/BerriAI/litellm/commit/f63cf0030679fe1a43d03fb196e815a0f28dae92)
2. Add pricing for amazon `eu` models [PR](https://github.com/BerriAI/litellm/commits/main/model_prices_and_context_window.json)
3. Fix Azure O1 mini pricing [PR](https://github.com/BerriAI/litellm/commit/52de1949ef2f76b8572df751f9c868a016d4832c)

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

01. Support `/openai/` passthrough for Assistant endpoints. [Get Started](https://docs.litellm.ai/docs/pass_through/openai_passthrough)
02. Bedrock Claude - fix tool calling transformation on invoke route. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---function-calling--tool-calling)
03. Bedrock Claude - response\_format support for claude on invoke route. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---structured-output--json-mode)
04. Bedrock - pass `description` if set in response\_format. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---structured-output--json-mode)
05. Bedrock - Fix passing response\_format: `{"type": "text"}`. [PR](https://github.com/BerriAI/litellm/commit/c84b489d5897755139aa7d4e9e54727ebe0fa540)
06. OpenAI - Handle sending image\_url as str to openai. [Get Started](https://docs.litellm.ai/docs/completion/vision)
07. Deepseek - return 'reasoning\_content' missing on streaming. [Get Started](https://docs.litellm.ai/docs/reasoning_content)
08. Caching - Support caching on reasoning content. [Get Started](https://docs.litellm.ai/docs/proxy/caching)
09. Bedrock - handle thinking blocks in assistant message. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)
10. Anthropic - Return `signature` on streaming. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)

<!--THE END-->

- Note: We've also migrated from `signature_delta` to `signature`. [Read more](https://docs.litellm.ai/release_notes/v1.63.0)

<!--THE END-->

11. Support format param for specifying image type. [Get Started](https://docs.litellm.ai/docs/completion/vision.md#explicitly-specify-image-type)
12. Anthropic - `/v1/messages` endpoint - `thinking` param support. [Get Started](https://docs.litellm.ai/docs/anthropic_unified.md)

<!--THE END-->

- Note: this refactors the \[BETA] unified `/v1/messages` endpoint, to just work for the Anthropic API.

<!--THE END-->

13. Vertex AI - handle $id in response schema when calling vertex ai. [Get Started](https://docs.litellm.ai/docs/providers/vertex#json-schema)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Batches API - Fix cost calculation to run on retrieve\_batch. [Get Started](https://docs.litellm.ai/docs/batches)
2. Batches API - Log batch models in spend logs / standard logging payload. [Get Started](https://docs.litellm.ai/docs/proxy/logging_spec.md#standardlogginghiddenparams)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

1. Virtual Keys Page
   
   - Allow team/org filters to be searchable on the Create Key Page
   - Add created\_by and updated\_by fields to Keys table
   - Show 'user\_email' on key table
   - Show 100 Keys Per Page, Use full height, increase width of key alias
2. Logs Page
   
   - Show Error Logs on LiteLLM UI
   - Allow Internal Users to View their own logs
3. Internal Users Page
   
   - Allow admin to control default model access for internal users
4. Fix session handling with cookies

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Fix prometheus metrics w/ custom metrics, when keys containing team\_id make requests. [PR](https://github.com/BerriAI/litellm/pull/8935)

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

1. Cooldowns - Support cooldowns on models called with client side credentials. [Get Started](https://docs.litellm.ai/docs/proxy/clientside_auth#pass-user-llm-api-keys--api-base)
2. Tag-based Routing - ensures tag-based routing across all endpoints (`/embeddings`, `/image_generation`, etc.). [Get Started](https://docs.litellm.ai/docs/proxy/tag_routing)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Raise BadRequestError when unknown model passed in request
2. Enforce model access restrictions on Azure OpenAI proxy route
3. Reliability fix - Handle emoji’s in text - fix orjson error
4. Model Access Patch - don't overwrite litellm.anthropic\_models when running auth checks
5. Enable setting timezone information in docker image

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.61.20-stable...v1.63.2-stable)

v1.63.0 fixes Anthropic 'thinking' response on streaming to return the `signature` block. [Github Issue](https://github.com/BerriAI/litellm/issues/8964)

It also moves the response structure from `signature_delta` to `signature` to be the same as Anthropic. [Anthropic Docs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#implementing-extended-thinking)

## Diff[​](#diff "Direct link to Diff")

```
"message": {
    ...
    "reasoning_content": "The capital of France is Paris.",
    "thinking_blocks": [
        {
            "type": "thinking",
            "thinking": "The capital of France is Paris.",
-            "signature_delta": "EqoBCkgIARABGAIiQL2UoU0b1OHYi+..." # 👈 OLD FORMAT
+            "signature": "EqoBCkgIARABGAIiQL2UoU0b1OHYi+..." # 👈 KEY CHANGE
        }
    ]
}
```

These are the changes since `v1.61.13-stable`.

This release is primarily focused on:

- LLM Translation improvements (claude-3-7-sonnet + 'thinking'/'reasoning\_content' support)
- UI improvements (add model flow, user management, etc)

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

1. Anthropic 3-7 sonnet support + cost tracking (Anthropic API + Bedrock + Vertex AI + OpenRouter)
   
   1. Anthropic API [Start here](https://docs.litellm.ai/docs/providers/anthropic#usage---thinking--reasoning_content)
   2. Bedrock API [Start here](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)
   3. Vertex AI API [See here](https://docs.litellm.ai/docs/providers/vertex#usage---thinking--reasoning_content)
   4. OpenRouter [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L5626)
2. Gpt-4.5-preview support + cost tracking [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L79)
3. Azure AI - Phi-4 cost tracking [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L1773)
4. Claude-3.5-sonnet - vision support updated on Anthropic API [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L2888)
5. Bedrock llama vision support [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L7714)
6. Cerebras llama3.3-70b pricing [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L2697)

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

1. Infinity Rerank - support returning documents when return\_documents=True [Start here](https://docs.litellm.ai/docs/providers/infinity#usage---returning-documents)
2. Amazon Deepseek - `<think>` param extraction into ‘reasoning\_content’ [Start here](https://docs.litellm.ai/docs/providers/bedrock#bedrock-imported-models-deepseek-deepseek-r1)
3. Amazon Titan Embeddings - filter out ‘aws\_’ params from request body [Start here](https://docs.litellm.ai/docs/providers/bedrock#bedrock-embedding)
4. Anthropic ‘thinking’ + ‘reasoning\_content’ translation support (Anthropic API, Bedrock, Vertex AI) [Start here](https://docs.litellm.ai/docs/reasoning_content)
5. VLLM - support ‘video\_url’ [Start here](https://docs.litellm.ai/docs/providers/vllm#send-video-url-to-vllm)
6. Call proxy via litellm SDK: Support `litellm_proxy/` for embedding, image\_generation, transcription, speech, rerank [Start here](https://docs.litellm.ai/docs/providers/litellm_proxy)
7. OpenAI Pass-through - allow using Assistants GET, DELETE on /openai pass through routes [Start here](https://docs.litellm.ai/docs/pass_through/openai_passthrough)
8. Message Translation - fix openai message for assistant msg if role is missing - openai allows this
9. O1/O3 - support ‘drop\_params’ for o3-mini and o1 parallel\_tool\_calls param (not supported currently) [See here](https://docs.litellm.ai/docs/completion/drop_params)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Cost tracking for rerank via Bedrock [See PR](https://github.com/BerriAI/litellm/commit/b682dc4ec8fd07acf2f4c981d2721e36ae2a49c5)
2. Anthropic pass-through - fix race condition causing cost to not be tracked [See PR](https://github.com/BerriAI/litellm/pull/8874)
3. Anthropic pass-through: Ensure accurate token counting [See PR](https://github.com/BerriAI/litellm/pull/8880)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

01. Models Page - Allow sorting models by ‘created at’
02. Models Page - Edit Model Flow Improvements
03. Models Page - Fix Adding Azure, Azure AI Studio models on UI
04. Internal Users Page - Allow Bulk Adding Internal Users on UI
05. Internal Users Page - Allow sorting users by ‘created at’
06. Virtual Keys Page - Allow searching for UserIDs on the dropdown when assigning a user to a team [See PR](https://github.com/BerriAI/litellm/pull/8844)
07. Virtual Keys Page - allow creating a user when assigning keys to users [See PR](https://github.com/BerriAI/litellm/pull/8844)
08. Model Hub Page - fix text overflow issue [See PR](https://github.com/BerriAI/litellm/pull/8749)
09. Admin Settings Page - Allow adding MSFT SSO on UI
10. Backend - don't allow creating duplicate internal users in DB

## Helm[​](#helm "Direct link to Helm")

1. support ttlSecondsAfterFinished on the migration job - [See PR](https://github.com/BerriAI/litellm/pull/8593)
2. enhance migrations job with additional configurable properties - [See PR](https://github.com/BerriAI/litellm/pull/8636)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Arize Phoenix support
2. ‘No-log’ - fix ‘no-log’ param support on embedding calls

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

1. Single Deployment Cooldown logic - Use allowed\_fails or allowed\_fail\_policy if set [Start here](https://docs.litellm.ai/docs/routing#advanced-custom-retries-cooldowns-based-on-error-type)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Hypercorn - fix reading / parsing request body
2. Windows - fix running proxy in windows
3. DD-Trace - fix dd-trace enablement on proxy

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

View the complete git diff [here](https://github.com/BerriAI/litellm/compare/v1.61.13-stable...v1.61.20-stable).

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

1. New OpenAI `/image/variations` endpoint BETA support [Docs](https://docs.litellm.ai/docs/image_variations)
2. Topaz API support on OpenAI `/image/variations` BETA endpoint [Docs](https://docs.litellm.ai/docs/providers/topaz)
3. Deepseek - r1 support w/ reasoning\_content ([Deepseek API](https://docs.litellm.ai/docs/providers/deepseek#reasoning-models), [Vertex AI](https://docs.litellm.ai/docs/providers/vertex#model-garden), [Bedrock](https://docs.litellm.ai/docs/providers/bedrock#deepseek))
4. Azure - Add azure o1 pricing [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L952)
5. Anthropic - handle `-latest` tag in model for cost calculation
6. Gemini-2.0-flash-thinking - add model pricing (it’s 0.0) [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L3393)
7. Bedrock - add stability sd3 model pricing [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L6814) (s/o [Marty Sullivan](https://github.com/marty-sullivan))
8. Bedrock - add us.amazon.nova-lite-v1:0 to model cost map [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L5619)
9. TogetherAI - add new together\_ai llama3.3 models [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L6985)

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

01. LM Studio -&gt; fix async embedding call
02. Gpt 4o models - fix response\_format translation
03. Bedrock nova - expand supported document types to include .md, .csv, etc. [Start Here](https://docs.litellm.ai/docs/providers/bedrock#usage---pdf--document-understanding)
04. Bedrock - docs on IAM role based access for bedrock - [Start Here](https://docs.litellm.ai/docs/providers/bedrock#sts-role-based-auth)
05. Bedrock - cache IAM role credentials when used
06. Google AI Studio (`gemini/`) - support gemini 'frequency\_penalty' and 'presence\_penalty'
07. Azure O1 - fix model name check
08. WatsonX - ZenAPIKey support for WatsonX [Docs](https://docs.litellm.ai/docs/providers/watsonx)
09. Ollama Chat - support json schema response format [Start Here](https://docs.litellm.ai/docs/providers/ollama#json-schema-support)
10. Bedrock - return correct bedrock status code and error message if error during streaming
11. Anthropic - Supported nested json schema on anthropic calls
12. OpenAI - `metadata` param preview support
    
    1. SDK - enable via `litellm.enable_preview_features = True`
    2. PROXY - enable via `litellm_settings::enable_preview_features: true`
13. Replicate - retry completion response on status=processing

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Bedrock - QA asserts all bedrock regional models have same `supported_` as base model
2. Bedrock - fix bedrock converse cost tracking w/ region name specified
3. Spend Logs reliability fix - when `user` passed in request body is int instead of string
4. Ensure ‘base\_model’ cost tracking works across all endpoints
5. Fixes for Image generation cost tracking
6. Anthropic - fix anthropic end user cost tracking
7. JWT / OIDC Auth - add end user id tracking from jwt auth

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

01. allows team member to become admin post-add (ui + endpoints)
02. New edit/delete button for updating team membership on UI
03. If team admin - show all team keys
04. Model Hub - clarify cost of models is per 1m tokens
05. Invitation Links - fix invalid url generated
06. New - SpendLogs Table Viewer - allows proxy admin to view spend logs on UI
    
    1. New spend logs - allow proxy admin to ‘opt in’ to logging request/response in spend logs table - enables easier abuse detection
    2. Show country of origin in spend logs
    3. Add pagination + filtering by key name/team name
07. `/key/delete` - allow team admin to delete team keys
08. Internal User ‘view’ - fix spend calculation when team selected
09. Model Analytics is now on Free
10. Usage page - shows days when spend = 0, and round spend on charts to 2 sig figs
11. Public Teams - allow admins to expose teams for new users to ‘join’ on UI - [Start Here](https://docs.litellm.ai/docs/proxy/public_teams)
12. Guardrails
    
    1. set/edit guardrails on a virtual key
    2. Allow setting guardrails on a team
    3. Set guardrails on team create + edit page
13. Support temporary budget increases on `/key/update` - new `temp_budget_increase` and `temp_budget_expiry` fields - [Start Here](https://docs.litellm.ai/docs/proxy/virtual_keys#temporary-budget-increase)
14. Support writing new key alias to AWS Secret Manager - on key rotation [Start Here](https://docs.litellm.ai/docs/secret#aws-secret-manager)

## Helm[​](#helm "Direct link to Helm")

1. add securityContext and pull policy values to migration job (s/o [https://github.com/Hexoplon](https://github.com/Hexoplon))
2. allow specifying envVars on values.yaml
3. new helm lint test

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Log the used prompt when prompt management used. [Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)
2. Support s3 logging with team alias prefixes - [Start Here](https://docs.litellm.ai/docs/proxy/logging#team-alias-prefix-in-object-key)
3. Prometheus [Start Here](https://docs.litellm.ai/docs/proxy/prometheus)
   
   1. fix litellm\_llm\_api\_time\_to\_first\_token\_metric not populating for bedrock models
   2. emit remaining team budget metric on regular basis (even when call isn’t made) - allows for more stable metrics on Grafana/etc.
   3. add key and team level budget metrics
   4. emit `litellm_overhead_latency_metric`
   5. Emit `litellm_team_budget_reset_at_metric` and `litellm_api_key_budget_remaining_hours_metric`
4. Datadog - support logging spend tags to Datadog. [Start Here](https://docs.litellm.ai/docs/proxy/enterprise#tracking-spend-for-custom-tags)
5. Langfuse - fix logging request tags, read from standard logging payload
6. GCS - don’t truncate payload on logging
7. New GCS Pub/Sub logging support [Start Here](https://docs.litellm.ai/docs/proxy/logging#google-cloud-storage---pubsub-topic)
8. Add AIM Guardrails support [Start Here](https://docs.litellm.ai/docs/proxy/guardrails/aim_security)

## Security[​](#security "Direct link to Security")

1. New Enterprise SLA for patching security vulnerabilities. [See Here](https://docs.litellm.ai/docs/enterprise#slas--professional-support)
2. Hashicorp - support using vault namespace for TLS auth. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)
3. Azure - DefaultAzureCredential support

## Health Checks[​](#health-checks "Direct link to Health Checks")

1. Cleanup pricing-only model names from wildcard route list - prevent bad health checks
2. Allow specifying a health check model for wildcard routes - [https://docs.litellm.ai/docs/proxy/health#wildcard-routes](https://docs.litellm.ai/docs/proxy/health#wildcard-routes)
3. New ‘health\_check\_timeout ‘ param with default 1min upperbound to prevent bad model from health check to hang and cause pod restarts. [Start Here](https://docs.litellm.ai/docs/proxy/health#health-check-timeout)
4. Datadog - add data dog service health check + expose new `/health/services` endpoint. [Start Here](https://docs.litellm.ai/docs/proxy/health#healthservices)

## Performance / Reliability improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability improvements")

01. 3x increase in RPS - moving to orjson for reading request body
02. LLM Routing speedup - using cached get model group info
03. SDK speedup - using cached get model info helper - reduces CPU work to get model info
04. Proxy speedup - only read request body 1 time per request
05. Infinite loop detection scripts added to codebase
06. Bedrock - pure async image transformation requests
07. Cooldowns - single deployment model group if 100% calls fail in high traffic - prevents an o1 outage from impacting other calls
08. Response Headers - return
    
    1. `x-litellm-timeout`
    2. `x-litellm-attempted-retries`
    3. `x-litellm-overhead-duration-ms`
    4. `x-litellm-response-duration-ms`
09. ensure duplicate callbacks are not added to proxy
10. Requirements.txt - bump certifi version

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

1. JWT / OIDC Auth - new `enforce_rbac` param,allows proxy admin to prevent any unmapped yet authenticated jwt tokens from calling proxy. [Start Here](https://docs.litellm.ai/docs/proxy/token_auth#enforce-role-based-access-control-rbac)
2. fix custom openapi schema generation for customized swagger’s
3. Request Headers - support reading `x-litellm-timeout` param from request headers. Enables model timeout control when using Vercel’s AI SDK + LiteLLM Proxy. [Start Here](https://docs.litellm.ai/docs/proxy/request_headers#litellm-headers)
4. JWT / OIDC Auth - new `role` based permissions for model authentication. [See Here](https://docs.litellm.ai/docs/proxy/jwt_auth_arch)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

This is the diff between v1.57.8-stable and v1.59.8-stable.

Use this to see the changes in the codebase.

[**Git Diff**](https://github.com/BerriAI/litellm/compare/v1.57.8-stable...v1.59.8-stable)

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## UI Improvements[​](#ui-improvements "Direct link to UI Improvements")

### \[Opt In] Admin UI - view messages / responses[​](#opt-in-admin-ui---view-messages--responses "Direct link to [Opt In] Admin UI - view messages / responses")

You can now view messages and response logs on Admin UI.

How to enable it - add `store_prompts_in_spend_logs: true` to your `proxy_config.yaml`

Once this flag is enabled, your `messages` and `responses` will be stored in the `LiteLLM_Spend_Logs` table.

```
general_settings:
store_prompts_in_spend_logs:true
```

## DB Schema Change[​](#db-schema-change "Direct link to DB Schema Change")

Added `messages` and `responses` to the `LiteLLM_Spend_Logs` table.

**By default this is not logged.** If you want `messages` and `responses` to be logged, you need to opt in with this setting

```
general_settings:
store_prompts_in_spend_logs:true
```

`alerting`, `prometheus`, `secret management`, `management endpoints`, `ui`, `prompt management`, `finetuning`, `batch`

## New / Updated Models[​](#new--updated-models "Direct link to New / Updated Models")

1. Mistral large pricing - [https://github.com/BerriAI/litellm/pull/7452](https://github.com/BerriAI/litellm/pull/7452)
2. Cohere command-r7b-12-2024 pricing - [https://github.com/BerriAI/litellm/pull/7553/files](https://github.com/BerriAI/litellm/pull/7553/files)
3. Voyage - new models, prices and context window information - [https://github.com/BerriAI/litellm/pull/7472](https://github.com/BerriAI/litellm/pull/7472)
4. Anthropic - bump Bedrock claude-3-5-haiku max\_output\_tokens to 8192

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Health check support for realtime models
2. Support calling Azure realtime routes via virtual keys
3. Support custom tokenizer on `/utils/token_counter` - useful when checking token count for self-hosted models
4. Request Prioritization - support on `/v1/completion` endpoint as well

## LLM Translation Improvements[​](#llm-translation-improvements "Direct link to LLM Translation Improvements")

1. Deepgram STT support. [Start Here](https://docs.litellm.ai/docs/providers/deepgram)
2. OpenAI Moderations - `omni-moderation-latest` support. [Start Here](https://docs.litellm.ai/docs/moderation)
3. Azure O1 - fake streaming support. This ensures if a `stream=true` is passed, the response is streamed. [Start Here](https://docs.litellm.ai/docs/providers/azure)
4. Anthropic - non-whitespace char stop sequence handling - [PR](https://github.com/BerriAI/litellm/pull/7484)
5. Azure OpenAI - support Entra ID username + password based auth. [Start Here](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret)
6. LM Studio - embedding route support. [Start Here](https://docs.litellm.ai/docs/providers/lm-studio)
7. WatsonX - ZenAPIKeyAuth support. [Start Here](https://docs.litellm.ai/docs/providers/watsonx)

## Prompt Management Improvements[​](#prompt-management-improvements "Direct link to Prompt Management Improvements")

1. Langfuse integration
2. HumanLoop integration
3. Support for using load balanced models
4. Support for loading optional params from prompt manager

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Finetuning + Batch APIs Improvements[​](#finetuning--batch-apis-improvements "Direct link to Finetuning + Batch APIs Improvements")

1. Improved unified endpoint support for Vertex AI finetuning - [PR](https://github.com/BerriAI/litellm/pull/7487)
2. Add support for retrieving vertex api batch jobs - [PR](https://github.com/BerriAI/litellm/commit/13f364682d28a5beb1eb1b57f07d83d5ef50cbdc)

## *NEW* Alerting Integration[​](#new-alerting-integration "Direct link to new-alerting-integration")

PagerDuty Alerting Integration.

Handles two types of alerts:

- High LLM API Failure Rate. Configure X fails in Y seconds to trigger an alert.
- High Number of Hanging LLM Requests. Configure X hangs in Y seconds to trigger an alert.

[Start Here](https://docs.litellm.ai/docs/proxy/pagerduty)

## Prometheus Improvements[​](#prometheus-improvements "Direct link to Prometheus Improvements")

Added support for tracking latency/spend/tokens based on custom metrics. [Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## *NEW* Hashicorp Secret Manager Support[​](#new-hashicorp-secret-manager-support "Direct link to new-hashicorp-secret-manager-support")

Support for reading credentials + writing LLM API keys. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)

## Management Endpoints / UI Improvements[​](#management-endpoints--ui-improvements "Direct link to Management Endpoints / UI Improvements")

1. Create and view organizations + assign org admins on the Proxy UI
2. Support deleting keys by key\_alias
3. Allow assigning teams to org on UI
4. Disable using ui session token for 'test key' pane
5. Show model used in 'test key' pane
6. Support markdown output in 'test key' pane

## Helm Improvements[​](#helm-improvements "Direct link to Helm Improvements")

1. Prevent istio injection for db migrations cron job
2. allow using migrationJob.enabled variable within job

## Logging Improvements[​](#logging-improvements "Direct link to Logging Improvements")

1. braintrust logging: respect project\_id, add more metrics - [https://github.com/BerriAI/litellm/pull/7613](https://github.com/BerriAI/litellm/pull/7613)
2. Athina - support base url - `ATHINA_BASE_URL`
3. Lunary - Allow passing custom parent run id to LLM Calls

## Git Diff[​](#git-diff "Direct link to Git Diff")

This is the diff between v1.56.3-stable and v1.57.8-stable.

Use this to see the changes in the codebase.

[Git Diff](https://github.com/BerriAI/litellm/compare/v1.56.3-stable...189b67760011ea313ca58b1f8bd43aa74fbd7f55)

`langfuse`, `management endpoints`, `ui`, `prometheus`, `secret management`

## Langfuse Prompt Management[​](#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

Langfuse Prompt Management is being labelled as BETA. This allows us to iterate quickly on the feedback we're receiving, and making the status clearer to users. We expect to make this feature to be stable by next month (February 2025).

Changes:

- Include the client message in the LLM API Request. (Previously only the prompt template was sent, and the client message was ignored).
- Log the prompt template in the logged request (e.g. to s3/langfuse).
- Log the 'prompt\_id' and 'prompt\_variables' in the logged request (e.g. to s3/langfuse).

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Team/Organization Management + UI Improvements[​](#teamorganization-management--ui-improvements "Direct link to Team/Organization Management + UI Improvements")

Managing teams and organizations on the UI is now easier.

Changes:

- Support for editing user role within team on UI.
- Support updating team member role to admin via api - `/team/member_update`
- Show team admins all keys for their team.
- Add organizations with budgets
- Assign teams to orgs on the UI
- Auto-assign SSO users to teams

[Start Here](https://docs.litellm.ai/docs/proxy/self_serve)

## Hashicorp Vault Support[​](#hashicorp-vault-support "Direct link to Hashicorp Vault Support")

We now support writing LiteLLM Virtual API keys to Hashicorp Vault.

[Start Here](https://docs.litellm.ai/docs/proxy/vault)

## Custom Prometheus Metrics[​](#custom-prometheus-metrics "Direct link to Custom Prometheus Metrics")

Define custom prometheus metrics, and track usage/latency/no. of requests against them

This allows for more fine-grained tracking - e.g. on prompt template passed in request metadata

[Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

`docker image`, `security`, `vulnerability`

## What changed?[​](#what-changed "Direct link to What changed?")

- LiteLLMBase image now uses `cgr.dev/chainguard/python:latest-dev`

## Why the change?[​](#why-the-change "Direct link to Why the change?")

To ensure there are 0 critical/high vulnerabilities on LiteLLM Docker Image

## Migration Guide[​](#migration-guide "Direct link to Migration Guide")

- If you use a custom dockerfile with litellm as a base image + `apt-get`

Instead of `apt-get` use `apk`, the base litellm image will no longer have `apt-get` installed.

**You are only impacted if you use `apt-get` in your Dockerfile**

```
# Use the provided base image
FROM docker.litellm.ai/berriai/litellm:main-latest

# Set the working directory
WORKDIR /app

# Install dependencies - CHANGE THIS to `apk`
RUN apt-get update && apt-get install -y dumb-init 
```

Before Change

```
RUN apt-get update && apt-get install -y dumb-init
```

After Change

```
RUN apk update && apk add --no-cache dumb-init
```

`deepgram`, `fireworks ai`, `vision`, `admin ui`, `dependency upgrades`

## New Models[​](#new-models "Direct link to New Models")

### **Deepgram Speech to Text**[​](#deepgram-speech-to-text "Direct link to deepgram-speech-to-text")

New Speech to Text support for Deepgram models. [**Start Here**](https://docs.litellm.ai/docs/providers/deepgram)

```
from litellm import transcription
import os 

# set api keys 
os.environ["DEEPGRAM_API_KEY"]=""
audio_file =open("/path/to/audio.mp3","rb")

response = transcription(model="deepgram/nova-2",file=audio_file)

print(f"response: {response}")
```

### **Fireworks AI - Vision** support for all models[​](#fireworks-ai---vision-support-for-all-models "Direct link to fireworks-ai---vision-support-for-all-models")

LiteLLM supports document inlining for Fireworks AI models. This is useful for models that are not vision models, but still need to parse documents/images/etc. LiteLLM will add `#transform=inline` to the url of the image\_url, if the model is not a vision model [See Code](https://github.com/BerriAI/litellm/blob/1ae9d45798bdaf8450f2dfdec703369f3d2212b7/litellm/llms/fireworks_ai/chat/transformation.py#L114)

## Proxy Admin UI[​](#proxy-admin-ui "Direct link to Proxy Admin UI")

- `Test Key` Tab displays `model` used in response

<!--THE END-->

- `Test Key` Tab renders content in `.md`, `.py` (any code/markdown format)

## Dependency Upgrades[​](#dependency-upgrades "Direct link to Dependency Upgrades")

- (Security fix) Upgrade to `fastapi==0.115.5` [https://github.com/BerriAI/litellm/pull/7447](https://github.com/BerriAI/litellm/pull/7447)

## Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- Add health check support for realtime models [Here](https://docs.litellm.ai/docs/proxy/health#realtime-models)
- Health check error with audio\_transcription model [https://github.com/BerriAI/litellm/issues/5999](https://github.com/BerriAI/litellm/issues/5999)

`guardrails`, `logging`, `virtual key management`, `new models`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Features[​](#new-features "Direct link to New Features")

### ✨ Log Guardrail Traces[​](#-log-guardrail-traces "Direct link to ✨ Log Guardrail Traces")

Track guardrail failure rate and if a guardrail is going rogue and failing requests. [Start here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

#### Traced Guardrail Success[​](#traced-guardrail-success "Direct link to Traced Guardrail Success")

#### Traced Guardrail Failure[​](#traced-guardrail-failure "Direct link to Traced Guardrail Failure")

### `/guardrails/list`[​](#guardrailslist "Direct link to guardrailslist")

`/guardrails/list` allows clients to view available guardrails + supported guardrail params

```
curl -X GET 'http://0.0.0.0:4000/guardrails/list'
```

Expected response

```
{
"guardrails":[
{
"guardrail_name":"aporia-post-guard",
"guardrail_info":{
"params":[
{
"name":"toxicity_score",
"type":"float",
"description":"Score between 0-1 indicating content toxicity level"
},
{
"name":"pii_detection",
"type":"boolean"
}
]
}
}
]
}
```

### ✨ Guardrails with Mock LLM[​](#-guardrails-with-mock-llm "Direct link to ✨ Guardrails with Mock LLM")

Send `mock_response` to test guardrails without making an LLM call. More info on `mock_response` [here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "hi my email is ishaan@berri.ai"}
    ],
    "mock_response": "This is a mock response",
    "guardrails": ["aporia-pre-guard", "aporia-post-guard"]
  }'
```

### Assign Keys to Users[​](#assign-keys-to-users "Direct link to Assign Keys to Users")

You can now assign keys to users via Proxy UI

## New Models[​](#new-models "Direct link to New Models")

- `openrouter/openai/o1`
- `vertex_ai/mistral-large@2411`

## Fixes[​](#fixes "Direct link to Fixes")

- Fix `vertex_ai/` mistral model pricing: [https://github.com/BerriAI/litellm/pull/7345](https://github.com/BerriAI/litellm/pull/7345)
- Missing model\_group field in logs for aspeech call types [https://github.com/BerriAI/litellm/pull/7392](https://github.com/BerriAI/litellm/pull/7392)

`key management`, `budgets/rate limits`, `logging`, `guardrails`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## ✨ Budget / Rate Limit Tiers[​](#-budget--rate-limit-tiers "Direct link to ✨ Budget / Rate Limit Tiers")

Define tiers with rate limits. Assign them to keys.

Use this to control access and budgets across a lot of keys.

[**Start here**](https://docs.litellm.ai/docs/proxy/rate_limit_tiers)

```
curl -L -X POST 'http://0.0.0.0:4000/budget/new' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "budget_id": "high-usage-tier",
    "model_max_budget": {
        "gpt-4o": {"rpm_limit": 1000000}
    }
}'
```

## OTEL Bug Fix[​](#otel-bug-fix "Direct link to OTEL Bug Fix")

LiteLLM was double logging litellm\_request span. This is now fixed.

[Relevant PR](https://github.com/BerriAI/litellm/pull/7435)

## Logging for Finetuning Endpoints[​](#logging-for-finetuning-endpoints "Direct link to Logging for Finetuning Endpoints")

Logs for finetuning requests are now available on all logging providers (e.g. Datadog).

What's logged per request:

- file\_id
- finetuning\_job\_id
- any key/team metadata

**Start Here:**

- [Setup Finetuning](https://docs.litellm.ai/docs/fine_tuning)
- [Setup Logging](https://docs.litellm.ai/docs/proxy/logging#datadog)

## Dynamic Params for Guardrails[​](#dynamic-params-for-guardrails "Direct link to Dynamic Params for Guardrails")

You can now set custom parameters (like success threshold) for your guardrails in each request.

[See guardrails spec for more details](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#-pass-additional-parameters-to-guardrail)

`batches`, `guardrails`, `team management`, `custom auth`

info

Get a free 7-day LiteLLM Enterprise trial here. [Start here](https://www.litellm.ai/enterprise#trial)

**No call needed**

## ✨ Cost Tracking, Logging for Batches API (`/batches`)[​](#-cost-tracking-logging-for-batches-api-batches "Direct link to -cost-tracking-logging-for-batches-api-batches")

Track cost, usage for Batch Creation Jobs. [Start here](https://docs.litellm.ai/docs/batches)

## ✨ `/guardrails/list` endpoint[​](#-guardrailslist-endpoint "Direct link to -guardrailslist-endpoint")

Show available guardrails to users. [Start here](https://litellm-api.up.railway.app/#/Guardrails)

## ✨ Allow teams to add models[​](#-allow-teams-to-add-models "Direct link to ✨ Allow teams to add models")

This enables team admins to call their own finetuned models via litellm proxy. [Start here](https://docs.litellm.ai/docs/proxy/team_model_add)

## ✨ Common checks for custom auth[​](#-common-checks-for-custom-auth "Direct link to ✨ Common checks for custom auth")

Calling the internal common\_checks function in custom auth is now enforced as an enterprise feature. This allows admins to use litellm's default budget/auth checks within their custom auth implementation. [Start here](https://docs.litellm.ai/docs/proxy/virtual_keys#custom-auth)

## ✨ Assigning team admins[​](#-assigning-team-admins "Direct link to ✨ Assigning team admins")

Team admins is graduating from beta and moving to our enterprise tier. This allows proxy admins to allow others to manage keys/models for their own teams (useful for projects in production). [Start here](https://docs.litellm.ai/docs/proxy/virtual_keys#restricting-key-generation)

A new LiteLLM Stable release [just went out](https://github.com/BerriAI/litellm/releases/tag/v1.55.8-stable). Here are 5 updates since v1.52.2-stable.

`langfuse`, `fallbacks`, `new models`, `azure_storage`

## Langfuse Prompt Management[​](#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

This makes it easy to run experiments or change the specific models `gpt-4o` to `gpt-4o-mini` on Langfuse, instead of making changes in your applications. [Start here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Control fallback prompts client-side[​](#control-fallback-prompts-client-side "Direct link to Control fallback prompts client-side")

> Claude prompts are different than OpenAI

Pass in prompts specific to model when doing fallbacks. [Start here](https://docs.litellm.ai/docs/proxy/reliability#control-fallback-prompts)

## New Providers / Models[​](#new-providers--models "Direct link to New Providers / Models")

- [NVIDIA Triton](https://developer.nvidia.com/triton-inference-server) `/infer` endpoint. [Start here](https://docs.litellm.ai/docs/providers/triton-inference-server)
- [Infinity](https://github.com/michaelfeil/infinity) Rerank Models [Start here](https://docs.litellm.ai/docs/providers/infinity)

## ✨ Azure Data Lake Storage Support[​](#-azure-data-lake-storage-support "Direct link to ✨ Azure Data Lake Storage Support")

Send LLM usage (spend, tokens) data to [Azure Data Lake](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction). This makes it easy to consume usage data on other services (eg. Databricks) [Start here](https://docs.litellm.ai/docs/proxy/logging#azure-blob-storage)

## Docker Run LiteLLM[​](#docker-run-litellm "Direct link to Docker Run LiteLLM")

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:litellm_stable_release_branch-v1.55.8-stable
```

## Get Daily Updates[​](#get-daily-updates "Direct link to Get Daily Updates")

LiteLLM ships new releases every day. [Follow us on LinkedIn](https://www.linkedin.com/company/berri-ai/) to get daily updates.