---
title: v1.80.11-stable - Google Interactions API
url: https://docs.litellm.ai/release_notes/v1-80-11
source: sitemap
fetched_at: 2026-01-21T19:43:01.337198928-03:00
rendered_js: false
word_count: 1860
summary: Release notes for LiteLLM v1.80.11 detailing performance optimizations, extensive new provider support including Gemini and Stability AI, and significant memory reductions through component lazy loading.
tags:
    - litellm-release
    - model-providers
    - performance-optimization
    - lazy-loading
    - image-generation
    - ai-guardrails
    - api-reference
    - cloud-integration
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