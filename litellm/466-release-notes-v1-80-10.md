---
title: '[Preview] v1.80.10.rc.1 - Agent Gateway: Azure Foundry & Bedrock AgentCore'
url: https://docs.litellm.ai/release_notes/v1-80-10
source: sitemap
fetched_at: 2026-01-21T19:42:58.154486994-03:00
rendered_js: false
word_count: 2588
summary: This document details the release notes for LiteLLM version 1.80.10.rc.1, focusing on the new Agent Gateway features, expanded provider integrations, and the addition of over 270 new language models.
tags:
    - litellm
    - release-notes
    - agent-gateway
    - llm-providers
    - model-updates
    - api-endpoints
    - a2a-tracking
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