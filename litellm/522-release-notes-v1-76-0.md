---
title: v1.76.0-stable - RPS Improvements
url: https://docs.litellm.ai/release_notes/v1-76-0
source: sitemap
fetched_at: 2026-01-21T19:42:41.17070227-03:00
rendered_js: false
word_count: 849
summary: Release notes detailing recent bug fixes, new model integrations, and feature updates for the LiteLLM proxy and supported AI providers.
tags:
    - litellm
    - changelog
    - release-notes
    - model-updates
    - bug-fixes
    - llm-proxy
category: other
---

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

<!--THE END-->

- [Deploy this version](#deploy-this-version)
- [New Models / Updated Models](#new-models--updated-models)
- [LLM API Endpoints](#llm-api-endpoints)
- [MCP Gateway](#mcp-gateway)
- [Vector Stores](#vector-stores)
- [Management Endpoints / UI](#management-endpoints--ui)
- [Logging / Guardrail Integrations](#logging--guardrail-integrations)
- [Performance / Loadbalancing / Reliability improvements](#performance--loadbalancing--reliability-improvements)
- [General Proxy Improvements](#general-proxy-improvements)