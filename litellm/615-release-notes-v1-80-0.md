---
title: 'v1.80.0-stable - Introducing Agent Hub: Register, Publish, and Share Agents'
url: https://docs.litellm.ai/release_notes/v1-80-0
source: sitemap
fetched_at: 2026-01-21T19:42:57.117609175-03:00
rendered_js: false
word_count: 1912
summary: This document details the v1.80.0 release of LiteLLM, highlighting new features like Agent Hub, RunwayML integration, and the OpenAI-compatible Vector Store Files API. It also includes performance benchmarks for embeddings and a list of newly supported AI models.
tags:
    - litellm
    - release-notes
    - vector-store-api
    - runwayml
    - api-gateway
    - performance-optimization
    - model-support
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