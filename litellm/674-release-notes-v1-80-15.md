---
title: v1.80.15-stable - Manus API Support
url: https://docs.litellm.ai/release_notes/v1-80-15
source: sitemap
fetched_at: 2026-01-21T19:43:02.233902752-03:00
rendered_js: false
word_count: 3522
summary: This document outlines the release highlights for LiteLLM version 1.80.15-stable.1, detailing performance improvements, new model provider integrations, and updated API endpoints.
tags:
    - litellm
    - release-notes
    - llm-proxy
    - model-providers
    - api-updates
    - performance-optimization
    - deployment
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