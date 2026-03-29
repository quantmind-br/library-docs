---
title: v1.73.6-stable
url: https://docs.litellm.ai/release_notes/v1-73-6-stable
source: sitemap
fetched_at: 2026-01-21T19:42:28.295178055-03:00
rendered_js: false
word_count: 1101
summary: This document outlines the release notes for LiteLLM v1.73.6, detailing new features such as gemini-cli support, batch API cost tracking, and various model pricing updates.
tags:
    - litellm
    - release-notes
    - gemini-cli
    - batch-api
    - cost-tracking
    - model-updates
    - llm-proxy
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
docker.litellm.ai/berriai/litellm:v1.73.6-stable.patch.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

### Claude on gemini-cli[​](#claude-on-gemini-cli "Direct link to Claude on gemini-cli")

This release brings support for using gemini-cli with LiteLLM.

You can use claude-sonnet-4, gemini-2.5-flash (Vertex AI & Google AI Studio), gpt-4.1 and any LiteLLM supported model on gemini-cli.

When you use gemini-cli with LiteLLM you get the following benefits:

**Developer Benefits:**

- Universal Model Access: Use any LiteLLM supported model (Anthropic, OpenAI, Vertex AI, Bedrock, etc.) through the gemini-cli interface.
- Higher Rate Limits & Reliability: Load balance across multiple models and providers to avoid hitting individual provider limits, with fallbacks to ensure you get responses even if one provider fails.

**Proxy Admin Benefits:**

- Centralized Management: Control access to all models through a single LiteLLM proxy instance without giving your developers API Keys to each provider.
- Budget Controls: Set spending limits and track costs across all gemini-cli usage.

[Get Started](https://docs.litellm.ai/docs/tutorials/litellm_gemini_cli)

### Batch API Cost Tracking[​](#batch-api-cost-tracking "Direct link to Batch API Cost Tracking")

v1.73.6 brings cost tracking for [LiteLLM Managed Batch API](https://docs.litellm.ai/docs/proxy/managed_batches) calls to LiteLLM. Previously, this was not being done for Batch API calls using LiteLLM Managed Files. Now, LiteLLM will store the status of each batch call in the DB and poll incomplete batch jobs in the background, emitting a spend log for cost tracking once the batch is complete.

There is no new flag / change needed on your end. Over the next few weeks we hope to extend this to cover batch cost tracking for the Anthropic passthrough as well.

[Get Started](https://docs.litellm.ai/docs/proxy/managed_batches)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)TypeAzure OpenAI`azure/o3-pro`200k$20.00$80.00NewOpenRouter`openrouter/mistralai/mistral-small-3.2-24b-instruct`32k$0.1$0.3NewOpenAI`o3-deep-research`200k$10.00$40.00NewOpenAI`o3-deep-research-2025-06-26`200k$10.00$40.00NewOpenAI`o4-mini-deep-research`200k$2.00$8.00NewOpenAI`o4-mini-deep-research-2025-06-26`200k$2.00$8.00NewDeepseek`deepseek-r1`65k$0.55$2.19NewDeepseek`deepseek-v3`65k$0.27$0.07New

### Updated Models[​](#updated-models "Direct link to Updated Models")

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Sambanova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Handle float timestamps - [PR](https://github.com/BerriAI/litellm/pull/11971) s/o [@neubig](https://github.com/neubig)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - support Azure Authentication method (azure ad token, api keys) on Responses API - [PR](https://github.com/BerriAI/litellm/pull/11941) s/o [@hsuyuming](https://github.com/hsuyuming)
  - Map ‘image\_url’ str as nested dict - [PR](https://github.com/BerriAI/litellm/pull/12075) s/o [@davis-featherstone](https://github.com/davis-featherstone)
- [**Watsonx**](https://docs.litellm.ai/docs/providers/watsonx)
  
  - Set ‘model’ field to None when model is part of a custom deployment - fixes error raised by WatsonX in those cases - [PR](https://github.com/BerriAI/litellm/pull/11854) s/o [@cbjuan](https://github.com/cbjuan)
- [**Perplexity**](https://docs.litellm.ai/docs/providers/perplexity)
  
  - Support web\_search\_options - [PR](https://github.com/BerriAI/litellm/pull/11983)
  - Support citation token and search queries cost calculation - [PR](https://github.com/BerriAI/litellm/pull/11938)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Null value in usage block handling - [PR](https://github.com/BerriAI/litellm/pull/12068)
- **Gemini ([Google AI Studio](https://docs.litellm.ai/docs/providers/gemini) + [VertexAI](https://docs.litellm.ai/docs/providers/vertex))**
  
  - Only use accepted format values (enum and datetime) - else gemini raises errors - [PR](https://github.com/BerriAI/litellm/pull/11989)
  - Cache tools if passed alongside cached content (else gemini raises an error) - [PR](https://github.com/BerriAI/litellm/pull/11989)
  - Json schema translation improvement: Fix unpack\_def handling of nested $ref inside anyof items - [PR](https://github.com/BerriAI/litellm/pull/11964)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Fix thinking prompt to match hugging face recommendation - [PR](https://github.com/BerriAI/litellm/pull/12007)
  - Add `supports_response_schema: true` for all mistral models except codestral-mamba - [PR](https://github.com/BerriAI/litellm/pull/12024)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Fix unnecessary await on embedding calls - [PR](https://github.com/BerriAI/litellm/pull/12024)

#### Features[​](#features "Direct link to Features")

- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure)
  
  - Check if o-series model supports reasoning effort (enables drop\_params to work for o1 models)
  - Assistant + tool use cost tracking - [PR](https://github.com/BerriAI/litellm/pull/12045)
- [**Nvidia Nim**](https://docs.litellm.ai/docs/providers/nvidia_nim)
  
  - Add ‘response\_format’ param support - [PR](https://github.com/BerriAI/litellm/pull/12003) @shagunb-acn
- [**ElevenLabs**](https://docs.litellm.ai/docs/providers/elevenlabs)
  
  - New STT provider - [PR](https://github.com/BerriAI/litellm/pull/12119)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/mcp**](https://docs.litellm.ai/docs/mcp)
  
  - Send appropriate auth string value to `/tool/call` endpoint with `x-mcp-auth` - [PR](https://github.com/BerriAI/litellm/pull/11968) s/o [@wagnerjt](https://github.com/wagnerjt)
- [**/v1/messages**](https://docs.litellm.ai/docs/anthropic_unified)
  
  - [Custom LLM](https://docs.litellm.ai/docs/providers/custom_llm_server#anthropic-v1messages) support - [PR](https://github.com/BerriAI/litellm/pull/12016)
- [**/chat/completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Azure Responses API via chat completion support - [PR](https://github.com/BerriAI/litellm/pull/12016)
- [**/responses**](https://docs.litellm.ai/docs/response_api)
  
  - Add reasoning content support for non-openai providers - [PR](https://github.com/BerriAI/litellm/pull/12055)
- **\[NEW] /generateContent**
  
  - New endpoints for gemini cli support - [PR](https://github.com/BerriAI/litellm/pull/12040)
  - Support calling Google AI Studio / VertexAI Gemini models in their native format - [PR](https://github.com/BerriAI/litellm/pull/12046)
  - Add logging + cost tracking for stream + non-stream vertex/google ai studio routes - [PR](https://github.com/BerriAI/litellm/pull/12058)
  - Add Bridge from generateContent to /chat/completions - [PR](https://github.com/BerriAI/litellm/pull/12081)
- [**/batches**](https://docs.litellm.ai/docs/batches)
  
  - Filter deployments to only those where managed file was written to - [PR](https://github.com/BerriAI/litellm/pull/12048)
  - Save all model / file id mappings in db (previously it was just the first one) - enables ‘true’ loadbalancing - [PR](https://github.com/BerriAI/litellm/pull/12048)
  - Support List Batches with target model name specified - [PR](https://github.com/BerriAI/litellm/pull/12049)

* * *

## Spend Tracking / Budget Improvements[​](#spend-tracking--budget-improvements "Direct link to Spend Tracking / Budget Improvements")

#### Features[​](#features-2 "Direct link to Features")

- [**Passthrough**](https://docs.litellm.ai/docs/pass_through)
  
  - [Bedrock](https://docs.litellm.ai/docs/pass_through/bedrock) - cost tracking (`/invoke` + `/converse` routes) on streaming + non-streaming - [PR](https://github.com/BerriAI/litellm/pull/12123)
  - [VertexAI](https://docs.litellm.ai/docs/pass_through/vertex_ai) - anthropic cost calculation support - [PR](https://github.com/BerriAI/litellm/pull/11992)
- [**Batches**](https://docs.litellm.ai/docs/batches)
  
  - Background job for cost tracking LiteLLM Managed batches - [PR](https://github.com/BerriAI/litellm/pull/12125)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **General UI**
  
  - Fix today selector date mutation in dashboard components - [PR](https://github.com/BerriAI/litellm/pull/12042)
- **Usage**
  
  - Aggregate usage data across all pages of paginated endpoint - [PR](https://github.com/BerriAI/litellm/pull/12033)
- **Teams**
  
  - De-duplicate models in team settings dropdown - [PR](https://github.com/BerriAI/litellm/pull/12074)
- **Models**
  
  - Preserve public model name when selecting ‘test connect’ with azure model (previously would reset) - [PR](https://github.com/BerriAI/litellm/pull/11713)
- **Invitation Links**
  
  - Ensure Invite links email contain the correct invite id when using tf provider - [PR](https://github.com/BerriAI/litellm/pull/12130)

#### Features[​](#features-3 "Direct link to Features")

- **Models**
  
  - Add ‘last success’ column to health check table - [PR](https://github.com/BerriAI/litellm/pull/11903)
- **MCP**
  
  - New UI component to support auth types: api key, bearer token, basic auth - [PR](https://github.com/BerriAI/litellm/pull/11968) s/o [@wagnerjt](https://github.com/wagnerjt)
  - Ensure internal users can access /mcp and /mcp/ routes - [PR](https://github.com/BerriAI/litellm/pull/12106)
- **SCIM**
  
  - Ensure default\_internal\_user\_params are applied for new users - [PR](https://github.com/BerriAI/litellm/pull/12015)
- **Team**
  
  - Support default key expiry for team member keys - [PR](https://github.com/BerriAI/litellm/pull/12023)
  - Expand team member add check to cover user email - [PR](https://github.com/BerriAI/litellm/pull/12082)
- **UI**
  
  - Restrict UI access by SSO group - [PR](https://github.com/BerriAI/litellm/pull/12023)
- **Keys**
  
  - Add new new\_key param for regenerating key - [PR](https://github.com/BerriAI/litellm/pull/12087)
- **Test Keys**
  
  - New ‘get code’ button for getting runnable python code snippet based on ui configuration - [PR](https://github.com/BerriAI/litellm/pull/11629)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **Braintrust**
  
  - Adds model to metadata to enable braintrust cost estimation - [PR](https://github.com/BerriAI/litellm/pull/12022)

#### Features[​](#features-4 "Direct link to Features")

- **Callbacks**
  
  - (Enterprise) - disable logging callbacks in request headers - [PR](https://github.com/BerriAI/litellm/pull/11985)
  - Add List Callbacks API Endpoint - [PR](https://github.com/BerriAI/litellm/pull/11987)
- **Bedrock Guardrail**
  
  - Don't raise exception on intervene action - [PR](https://github.com/BerriAI/litellm/pull/11875)
  - Ensure PII Masking is applied on response streaming or non streaming content when using post call - [PR](https://github.com/BerriAI/litellm/pull/12086)
- **\[NEW] Palo Alto Networks Prisma AIRS Guardrail**
  
  - [PR](https://github.com/BerriAI/litellm/pull/12116)
- **ElasticSearch**
  
  - New Elasticsearch Logging Tutorial - [PR](https://github.com/BerriAI/litellm/pull/11761)
- **Message Redaction**
  
  - Preserve usage / model information for Embedding redaction - [PR](https://github.com/BerriAI/litellm/pull/12088)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- **Team-only models**
  
  - Filter team-only models from routing logic for non-team calls
- **Context Window Exceeded error**
  
  - Catch anthropic exceptions - [PR](https://github.com/BerriAI/litellm/pull/12113)

#### Features[​](#features-5 "Direct link to Features")

- **Router**
  
  - allow using dynamic cooldown time for a specific deployment - [PR](https://github.com/BerriAI/litellm/pull/12037)
  - handle cooldown\_time = 0 for deployments - [PR](https://github.com/BerriAI/litellm/pull/12108)
- **Redis**
  
  - Add better debugging to see what variables are set - [PR](https://github.com/BerriAI/litellm/pull/12073)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- **aiohttp**
  
  - Check HTTP\_PROXY vars in networking requests
  - Allow using HTTP_ Proxy settings with trust\_env

#### Features[​](#features-6 "Direct link to Features")

- **Docs**
  
  - Add recommended spec - [PR](https://github.com/BerriAI/litellm/pull/11980)
- **Swagger**
  
  - Introduce new environment variable NO\_REDOC to opt-out Redoc - [PR](https://github.com/BerriAI/litellm/pull/12092)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @mukesh-dream11 made their first contribution in [https://github.com/BerriAI/litellm/pull/11969](https://github.com/BerriAI/litellm/pull/11969)
- @cbjuan made their first contribution in [https://github.com/BerriAI/litellm/pull/11854](https://github.com/BerriAI/litellm/pull/11854)
- @ryan-castner made their first contribution in [https://github.com/BerriAI/litellm/pull/12055](https://github.com/BerriAI/litellm/pull/12055)
- @davis-featherstone made their first contribution in [https://github.com/BerriAI/litellm/pull/12075](https://github.com/BerriAI/litellm/pull/12075)
- @Gum-Joe made their first contribution in [https://github.com/BerriAI/litellm/pull/12068](https://github.com/BerriAI/litellm/pull/12068)
- @jroberts2600 made their first contribution in [https://github.com/BerriAI/litellm/pull/12116](https://github.com/BerriAI/litellm/pull/12116)
- @ohmeow made their first contribution in [https://github.com/BerriAI/litellm/pull/12022](https://github.com/BerriAI/litellm/pull/12022)
- @amarrella made their first contribution in [https://github.com/BerriAI/litellm/pull/11942](https://github.com/BerriAI/litellm/pull/11942)
- @zhangyoufu made their first contribution in [https://github.com/BerriAI/litellm/pull/12092](https://github.com/BerriAI/litellm/pull/12092)
- @bougou made their first contribution in [https://github.com/BerriAI/litellm/pull/12088](https://github.com/BerriAI/litellm/pull/12088)
- @codeugar made their first contribution in [https://github.com/BerriAI/litellm/pull/11972](https://github.com/BerriAI/litellm/pull/11972)
- @glgh made their first contribution in [https://github.com/BerriAI/litellm/pull/12133](https://github.com/BerriAI/litellm/pull/12133)

## [**Git Diff**](https://github.com/BerriAI/litellm/compare/v1.73.0-stable...v1.73.6.rc-draft)[​](#git-diff "Direct link to git-diff")