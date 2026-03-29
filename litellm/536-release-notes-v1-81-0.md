---
title: v1.81.0 - Claude Code - Web Search Across All Providers
url: https://docs.litellm.ai/release_notes/v1-81-0
source: sitemap
fetched_at: 2026-01-21T19:43:07.240753388-03:00
rendered_js: false
word_count: 2325
summary: This document outlines the updates and new features in LiteLLM version 1.81.0, including cross-provider web search support, image download size restrictions, and CPU performance optimizations.
tags:
    - release-notes
    - litellm-proxy
    - image-processing
    - performance-optimization
    - claude-code
    - audit-logs
    - llm-gateway
category: other
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