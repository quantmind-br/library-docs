---
title: v1.74.15-stable
url: https://docs.litellm.ai/release_notes/v1-74-15
source: sitemap
fetched_at: 2026-01-21T19:42:32.132602093-03:00
rendered_js: false
word_count: 1020
summary: This document outlines the updates in LiteLLM version 1.74.15-stable, highlighting new features such as user agent activity tracking, MCP gateway guardrails, and expanded model support for Google AI Studio and OpenRouter.
tags:
    - litellm
    - release-notes
    - model-deployment
    - usage-tracking
    - mcp-gateway
    - prompt-management
    - ai-infrastructure
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