---
title: 'v1.78.0-stable - MCP Gateway: Control Tool Access by Team, Key'
url: https://docs.litellm.ai/release_notes/v1-78-0
source: sitemap
fetched_at: 2026-01-21T19:42:50.105131459-03:00
rendered_js: false
word_count: 1546
summary: This document provides the release notes for LiteLLM version 1.78.0-stable, detailing performance enhancements, new model integrations, and administrative controls for tool access.
tags:
    - litellm-release
    - ai-gateway
    - performance-optimization
    - model-deployment
    - latency-reduction
    - mcp-control
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