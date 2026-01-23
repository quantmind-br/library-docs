---
title: v1.76.1-stable - Gemini 2.5 Flash Image
url: https://docs.litellm.ai/release_notes/v1-76-1
source: sitemap
fetched_at: 2026-01-21T19:42:41.843091318-03:00
rendered_js: false
word_count: 1089
summary: Release notes for LiteLLM v1.76.1 detailing major performance optimizations, support for new models like Gemini 2.5 and GPT Realtime, and new provider integrations.
tags:
    - litellm
    - release-notes
    - performance-optimization
    - model-support
    - ai-proxy
    - api-updates
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