---
title: v1.74.7-stable
url: https://docs.litellm.ai/release_notes/v1-74-7
source: sitemap
fetched_at: 2026-01-21T19:42:35.741913559-03:00
rendered_js: false
word_count: 1268
summary: This document outlines the updates in LiteLLM version 1.74.7, featuring the introduction of a Vector Stores API, bulk user management tools, and enhanced health check reliability.
tags:
    - litellm
    - release-notes
    - vector-stores
    - llm-providers
    - health-check
    - user-management
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
docker.litellm.ai/berriai/litellm:v1.74.7-stable.patch.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Vector Stores** - Support for Vertex RAG Engine, PG Vector, OpenAI & Azure OpenAI Vector Stores.
- **Bulk Editing Users** - Bulk editing users on the UI.
- **Health Check Improvements** - Prevent unnecessary pod restarts during high traffic.
- **New LLM Providers** - Added Moonshot AI and Vercel v0 provider support.

* * *

## Vector Stores API[​](#vector-stores-api "Direct link to Vector Stores API")

This release introduces support for using VertexAI RAG Engine, PG Vector, Bedrock Knowledge Bases, and OpenAI Vector Stores with LiteLLM.

This is ideal for use cases requiring external knowledge sources with LLMs.

This brings the following benefits for LiteLLM users:

**Proxy Admin Benefits:**

- Fine-grained access control: determine which Keys and Teams can access specific Vector Stores
- Complete usage tracking and monitoring across all vector store operations

**Developer Benefits:**

- Simple, unified interface for querying vector stores and using them with LLM API requests
- Consistent API experience across all supported vector store providers

[Get started](https://docs.litellm.ai/docs/completion/knowledgebase)

* * *

## Bulk Editing Users[​](#bulk-editing-users "Direct link to Bulk Editing Users")

v1.74.7-stable introduces Bulk Editing Users on the UI. This is useful for:

- granting all existing users to a default team (useful for controlling access / tracking spend by team)
- controlling personal model access for existing users

[Read more](https://docs.litellm.ai/docs/proxy/ui/bulk_edit_users)

* * *

## Health Check Server[​](#health-check-server "Direct link to Health Check Server")

This release brings reliability improvements that prevent unnecessary pod restarts during high traffic. Previously, when the main LiteLLM app was busy serving traffic, health endpoints would timeout even when pods were healthy.

Starting with this release, you can run health endpoints on an isolated process with a dedicated port. This ensures liveness and readiness probes remain responsive even when the main LiteLLM app is under heavy load.

[Read More](https://docs.litellm.ai/docs/proxy/prod#10-use-a-separate-health-check-app)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)Azure AI`azure_ai/grok-3`131k$3.30$16.50Azure AI`azure_ai/global/grok-3`131k$3.00$15.00Azure AI`azure_ai/global/grok-3-mini`131k$0.25$1.27Azure AI`azure_ai/grok-3-mini`131k$0.275$1.38Azure AI`azure_ai/jais-30b-chat`8k$3200$9710Groq`groq/moonshotai-kimi-k2-instruct`131k$1.00$3.00AI21`jamba-large-1.7`256k$2.00$8.00AI21`jamba-mini-1.7`256k$0.20$0.40Together.ai`together_ai/moonshotai/Kimi-K2-Instruct`131k$1.00$3.00v0`v0/v0-1.0-md`128k$3.00$15.00v0`v0/v0-1.5-md`128k$3.00$15.00v0`v0/v0-1.5-lg`512k$15.00$75.00Moonshot`moonshot/moonshot-v1-8k`8k$0.20$2.00Moonshot`moonshot/moonshot-v1-32k`32k$1.00$3.00Moonshot`moonshot/moonshot-v1-128k`131k$2.00$5.00Moonshot`moonshot/moonshot-v1-auto`131k$2.00$5.00Moonshot`moonshot/kimi-k2-0711-preview`131k$0.60$2.50Moonshot`moonshot/moonshot-v1-32k-0430`32k$1.00$3.00Moonshot`moonshot/moonshot-v1-128k-0430`131k$2.00$5.00Moonshot`moonshot/moonshot-v1-8k-0430`8k$0.20$2.00Moonshot`moonshot/kimi-latest`131k$2.00$5.00Moonshot`moonshot/kimi-latest-8k`8k$0.20$2.00Moonshot`moonshot/kimi-latest-32k`32k$1.00$3.00Moonshot`moonshot/kimi-latest-128k`131k$2.00$5.00Moonshot`moonshot/kimi-thinking-preview`131k$30.00$30.00Moonshot`moonshot/moonshot-v1-8k-vision-preview`8k$0.20$2.00Moonshot`moonshot/moonshot-v1-32k-vision-preview`32k$1.00$3.00Moonshot`moonshot/moonshot-v1-128k-vision-preview`131k$2.00$5.00

#### Features[​](#features "Direct link to Features")

- [**🆕 Moonshot API (Kimi)**](https://docs.litellm.ai/docs/providers/moonshot)
  
  - New LLM API integration for accessing Kimi models - [PR #12592](https://github.com/BerriAI/litellm/pull/12592), [Get Started](https://docs.litellm.ai/docs/providers/moonshot)
- [**🆕 v0 Provider**](https://docs.litellm.ai/docs/providers/v0)
  
  - New provider integration for v0.dev - [PR #12751](https://github.com/BerriAI/litellm/pull/12751), [Get Started](https://docs.litellm.ai/docs/providers/v0)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - Use OpenAI DeepResearch models with `litellm.completion` (`/chat/completions`) - [PR #12627](https://github.com/BerriAI/litellm/pull/12627) **DOC NEEDED**
- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure_openai)
  
  - Use Azure OpenAI DeepResearch models with `litellm.completion` (`/chat/completions`) - [PR #12627](https://github.com/BerriAI/litellm/pull/12627) **DOC NEEDED**
  - Added `response_format` support for openai gpt-4.1 models - [PR #12745](https://github.com/BerriAI/litellm/pull/12745)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Tool cache control support - [PR #12668](https://github.com/BerriAI/litellm/pull/12668)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Claude 4 /invoke route support - [PR #12599](https://github.com/BerriAI/litellm/pull/12599), [Get Started](https://docs.litellm.ai/docs/providers/bedrock)
  - Application inference profile tool choice support - [PR #12599](https://github.com/BerriAI/litellm/pull/12599)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Custom TTL support for context caching - [PR #12541](https://github.com/BerriAI/litellm/pull/12541)
  - Fix implicit caching cost calculation for Gemini 2.x models - [PR #12585](https://github.com/BerriAI/litellm/pull/12585)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Added Vertex AI RAG Engine support (use with OpenAI compatible `/vector_stores` API) - [PR #12752](https://github.com/BerriAI/litellm/pull/12595), [Get Started](https://docs.litellm.ai/docs/completion/knowledgebase)
- [**vLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Added support for using Rerank endpoints with vLLM - [PR #12738](https://github.com/BerriAI/litellm/pull/12738), [Get Started](https://docs.litellm.ai/docs/providers/vllm#rerank)
- [**AI21**](https://docs.litellm.ai/docs/providers/ai21)
  
  - Added ai21/jamba-1.7 model family pricing - [PR #12593](https://github.com/BerriAI/litellm/pull/12593), [Get Started](https://docs.litellm.ai/docs/providers/ai21)
- [**Together.ai**](https://docs.litellm.ai/docs/providers/together_ai)
  
  - \[New Model] add together\_ai/moonshotai/Kimi-K2-Instruct - [PR #12645](https://github.com/BerriAI/litellm/pull/12645), [Get Started](https://docs.litellm.ai/docs/providers/together_ai)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Add groq/moonshotai-kimi-k2-instruct model configuration - [PR #12648](https://github.com/BerriAI/litellm/pull/12648), [Get Started](https://docs.litellm.ai/docs/providers/groq)
- [**Github Copilot**](https://docs.litellm.ai/docs/providers/github_copilot)
  
  - Change System prompts to assistant prompts for GH Copilot - [PR #12742](https://github.com/BerriAI/litellm/pull/12742), [Get Started](https://docs.litellm.ai/docs/providers/github_copilot)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Fix streaming + response\_format + tools bug - [PR #12463](https://github.com/BerriAI/litellm/pull/12463)
- [**XAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - grok-4 does not support the `stop` param - [PR #12646](https://github.com/BerriAI/litellm/pull/12646)
- [**AWS**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Role chaining with web authentication for AWS Bedrock - [PR #12607](https://github.com/BerriAI/litellm/pull/12607)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add project\_id to cached credentials - [PR #12661](https://github.com/BerriAI/litellm/pull/12661)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fix bedrock nova micro and nova lite context window info in [PR #12619](https://github.com/BerriAI/litellm/pull/12619)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/chat/completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Include tool calls in output of trim\_messages - [PR #11517](https://github.com/BerriAI/litellm/pull/11517)
- [**/v1/vector\_stores**](https://docs.litellm.ai/docs/vector_stores/search)
  
  - New OpenAI-compatible vector store endpoints - [PR #12699](https://github.com/BerriAI/litellm/pull/12699), [Get Started](https://docs.litellm.ai/docs/vector_stores/search)
  - Vector store search endpoint - [PR #12749](https://github.com/BerriAI/litellm/pull/12749), [Get Started](https://docs.litellm.ai/docs/vector_stores/search)
  - Support for using PG Vector as a vector store - [PR #12667](https://github.com/BerriAI/litellm/pull/12667), [Get Started](https://docs.litellm.ai/docs/completion/knowledgebase)
- [**/streamGenerateContent**](https://docs.litellm.ai/docs/generateContent)
  
  - Non-gemini model support - [PR #12647](https://github.com/BerriAI/litellm/pull/12647)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**/vector\_stores**](https://docs.litellm.ai/docs/vector_stores/search)
  
  - Knowledge Base Call returning error when passing as `tools` - [PR #12628](https://github.com/BerriAI/litellm/pull/12628)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-2 "Direct link to Features")

- [**Access Groups**](https://docs.litellm.ai/docs/mcp#grouping-mcps-access-groups)
  
  - Allow MCP access groups to be added via litellm proxy config.yaml - [PR #12654](https://github.com/BerriAI/litellm/pull/12654)
  - List tools from access list for keys - [PR #12657](https://github.com/BerriAI/litellm/pull/12657)
- [**Namespacing**](https://docs.litellm.ai/docs/mcp#mcp-namespacing)
  
  - URL-based namespacing for better segregation - [PR #12658](https://github.com/BerriAI/litellm/pull/12658)
  - Make MCP\_TOOL\_PREFIX\_SEPARATOR configurable from env - [PR #12603](https://github.com/BerriAI/litellm/pull/12603)
- [**Gateway Features**](https://docs.litellm.ai/docs/mcp#mcp-gateway-features)
  
  - Allow using MCPs with all LLM APIs (VertexAI, Gemini, Groq, etc.) when using /responses - [PR #12546](https://github.com/BerriAI/litellm/pull/12546)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- Fix to update object permission on update/delete key/team - [PR #12701](https://github.com/BerriAI/litellm/pull/12701)
- Include /mcp in list of available routes on proxy - [PR #12612](https://github.com/BerriAI/litellm/pull/12612)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Keys**
  
  - Regenerate Key State Management improvements - [PR #12729](https://github.com/BerriAI/litellm/pull/12729)
- **Models**
  
  - Wildcard model filter support - [PR #12597](https://github.com/BerriAI/litellm/pull/12597)
  - Fixes for handling team only models on UI - [PR #12632](https://github.com/BerriAI/litellm/pull/12632)
- **Usage Page**
  
  - Fix Y-axis labels overlap on Spend per Tag chart - [PR #12754](https://github.com/BerriAI/litellm/pull/12754)
- **Teams**
  
  - Allow setting custom key duration + show key creation stats - [PR #12722](https://github.com/BerriAI/litellm/pull/12722)
  - Enable team admins to update member roles - [PR #12629](https://github.com/BerriAI/litellm/pull/12629)
- **Users**
  
  - New `/user/bulk_update` endpoint - [PR #12720](https://github.com/BerriAI/litellm/pull/12720)
- **Logs Page**
  
  - Add `end_user` filter on UI Logs Page - [PR #12663](https://github.com/BerriAI/litellm/pull/12663)
- **MCP Servers**
  
  - Copy MCP Server name functionality - [PR #12760](https://github.com/BerriAI/litellm/pull/12760)
- **Vector Stores**
  
  - UI support for clicking into Vector Stores - [PR #12741](https://github.com/BerriAI/litellm/pull/12741)
  - Allow adding Vertex RAG Engine, OpenAI, Azure through UI - [PR #12752](https://github.com/BerriAI/litellm/pull/12752)
- **General**
  
  - Add Copy-on-Click for all IDs (Key, Team, Organization, MCP Server) - [PR #12615](https://github.com/BerriAI/litellm/pull/12615)
- [**SCIM**](https://docs.litellm.ai/docs/proxy/scim)
  
  - Add GET /ServiceProviderConfig endpoint - [PR #12664](https://github.com/BerriAI/litellm/pull/12664)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- **Teams**
  
  - Ensure user id correctly added when creating new teams - [PR #12719](https://github.com/BerriAI/litellm/pull/12719)
  - Fixes for handling team-only models on UI - [PR #12632](https://github.com/BerriAI/litellm/pull/12632)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Google Cloud Model Armor**](https://docs.litellm.ai/docs/proxy/guardrails/google_cloud_model_armor)
  
  - New guardrails integration - [PR #12492](https://github.com/BerriAI/litellm/pull/12492)
- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/bedrock)
  
  - Allow disabling exception on 'BLOCKED' action - [PR #12693](https://github.com/BerriAI/litellm/pull/12693)
- [**Guardrails AI**](https://docs.litellm.ai/docs/proxy/guardrails/guardrails_ai)
  
  - Support `llmOutput` based guardrails as pre-call hooks - [PR #12674](https://github.com/BerriAI/litellm/pull/12674)
- [**DataDog LLM Observability**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Add support for tracking the correct span type based on LLM Endpoint used - [PR #12652](https://github.com/BerriAI/litellm/pull/12652)
- [**Custom Logging**](https://docs.litellm.ai/docs/proxy/logging)
  
  - Allow reading custom logger python scripts from S3 or GCS Bucket - [PR #12623](https://github.com/BerriAI/litellm/pull/12623)

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- [**General Logging**](https://docs.litellm.ai/docs/proxy/logging)
  
  - StandardLoggingPayload on cache\_hits should track custom llm provider - [PR #12652](https://github.com/BerriAI/litellm/pull/12652)
- [**S3 Buckets**](https://docs.litellm.ai/docs/proxy/logging#s3-buckets)
  
  - S3 v2 log uploader crashes when using with guardrails - [PR #12733](https://github.com/BerriAI/litellm/pull/12733)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-5 "Direct link to Features")

- **Health Checks**
  
  - Separate health app for liveness probes - [PR #12669](https://github.com/BerriAI/litellm/pull/12669)
  - Health check app on separate port - [PR #12718](https://github.com/BerriAI/litellm/pull/12718)
- **Caching**
  
  - Add Azure Blob cache support - [PR #12587](https://github.com/BerriAI/litellm/pull/12587)
- **Router**
  
  - Handle ZeroDivisionError with zero completion tokens in lowest\_latency strategy - [PR #12734](https://github.com/BerriAI/litellm/pull/12734)

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- **Database**
  
  - Use upsert for managed object table to avoid UniqueViolationError - [PR #11795](https://github.com/BerriAI/litellm/pull/11795)
  - Refactor to support use\_prisma\_migrate for helm hook - [PR #12600](https://github.com/BerriAI/litellm/pull/12600)
- **Cache**
  
  - Fix: redis caching for embedding response models - [PR #12750](https://github.com/BerriAI/litellm/pull/12750)

* * *

## Helm Chart[​](#helm-chart "Direct link to Helm Chart")

- DB Migration Hook: refactor to support use\_prisma\_migrate - for helm hook [PR](https://github.com/BerriAI/litellm/pull/12600)
- Add envVars and extraEnvVars support to Helm migrations job - [PR #12591](https://github.com/BerriAI/litellm/pull/12591)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-6 "Direct link to Features")

- **Control Plane + Data Plane Architecture**
  
  - Control Plane + Data Plane support - [PR #12601](https://github.com/BerriAI/litellm/pull/12601)
- **Proxy CLI**
  
  - Add "keys import" command to CLI - [PR #12620](https://github.com/BerriAI/litellm/pull/12620)
- **Swagger Documentation**
  
  - Add swagger docs for LiteLLM /chat/completions, /embeddings, /responses - [PR #12618](https://github.com/BerriAI/litellm/pull/12618)
- **Dependencies**
  
  - Loosen rich version from ==13.7.1 to &gt;=13.7.1 - [PR #12704](https://github.com/BerriAI/litellm/pull/12704)

#### Bugs[​](#bugs-6 "Direct link to Bugs")

- Verbose log is enabled by default fix - [PR #12596](https://github.com/BerriAI/litellm/pull/12596)
- Add support for disabling callbacks in request body - [PR #12762](https://github.com/BerriAI/litellm/pull/12762)
- Handle circular references in spend tracking metadata JSON serialization - [PR #12643](https://github.com/BerriAI/litellm/pull/12643)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @AntonioKL made their first contribution in [https://github.com/BerriAI/litellm/pull/12591](https://github.com/BerriAI/litellm/pull/12591)
- @marcelodiaz558 made their first contribution in [https://github.com/BerriAI/litellm/pull/12541](https://github.com/BerriAI/litellm/pull/12541)
- @dmcaulay made their first contribution in [https://github.com/BerriAI/litellm/pull/12463](https://github.com/BerriAI/litellm/pull/12463)
- @demoray made their first contribution in [https://github.com/BerriAI/litellm/pull/12587](https://github.com/BerriAI/litellm/pull/12587)
- @staeiou made their first contribution in [https://github.com/BerriAI/litellm/pull/12631](https://github.com/BerriAI/litellm/pull/12631)
- @stefanc-ai2 made their first contribution in [https://github.com/BerriAI/litellm/pull/12622](https://github.com/BerriAI/litellm/pull/12622)
- @RichardoC made their first contribution in [https://github.com/BerriAI/litellm/pull/12607](https://github.com/BerriAI/litellm/pull/12607)
- @yeahyung made their first contribution in [https://github.com/BerriAI/litellm/pull/11795](https://github.com/BerriAI/litellm/pull/11795)
- @mnguyen96 made their first contribution in [https://github.com/BerriAI/litellm/pull/12619](https://github.com/BerriAI/litellm/pull/12619)
- @rgambee made their first contribution in [https://github.com/BerriAI/litellm/pull/11517](https://github.com/BerriAI/litellm/pull/11517)
- @jvanmelckebeke made their first contribution in [https://github.com/BerriAI/litellm/pull/12725](https://github.com/BerriAI/litellm/pull/12725)
- @jlaurendi made their first contribution in [https://github.com/BerriAI/litellm/pull/12704](https://github.com/BerriAI/litellm/pull/12704)
- @doublerr made their first contribution in [https://github.com/BerriAI/litellm/pull/12661](https://github.com/BerriAI/litellm/pull/12661)

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.74.3-stable...v1.74.7-stable)[​](#full-changelog "Direct link to full-changelog")