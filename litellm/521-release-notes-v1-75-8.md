---
title: v1.75.8-stable - Team Member Rate Limits
url: https://docs.litellm.ai/release_notes/v1-75-8
source: sitemap
fetched_at: 2026-01-21T19:42:40.055478132-03:00
rendered_js: false
word_count: 830
summary: This document outlines the updates and new features in LiteLLM version 1.75.8, including support for GPT-5 models, team member rate limits, and expanded provider integrations. It also details performance enhancements and improvements to the management UI and MCP gateway.
tags:
    - litellm-release
    - model-support
    - rate-limiting
    - api-gateway
    - llm-providers
    - gpt-5
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