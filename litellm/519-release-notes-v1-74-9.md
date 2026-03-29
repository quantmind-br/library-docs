---
title: v1.74.9-stable - Auto-Router
url: https://docs.litellm.ai/release_notes/v1-74-9
source: sitemap
fetched_at: 2026-01-21T19:42:35.842042532-03:00
rendered_js: false
word_count: 987
summary: This document details the updates in LiteLLM version 1.74.9-stable, focusing on new features like content-based auto-routing, model-level guardrails, and expanded LLM provider integrations. It also includes deployment instructions, pricing updates for various models, and bug fixes for the proxy and MCP gateway.
tags:
    - litellm
    - release-notes
    - auto-routing
    - guardrails
    - mcp-gateway
    - llm-proxy
    - model-management
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
docker.litellm.ai/berriai/litellm:v1.74.9-stable.patch.1
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Auto-Router** - Automatically route requests to specific models based on request content.
- **Model-level Guardrails** - Only run guardrails when specific models are used.
- **MCP Header Propagation** - Propagate headers from client to backend MCP.
- **New LLM Providers** - Added Bedrock inpainting support and Recraft API image generation / image edits support.

* * *

## Auto-Router[​](#auto-router "Direct link to Auto-Router")

This release introduces auto-routing to models based on request content. This means **Proxy Admins** can define a set of keywords that always routes to specific models when **users** opt in to using the auto-router.

This is great for internal use cases where you don't want **users** to think about which model to use - for example, use Claude models for coding vs GPT models for generating ad copy.

[Read More](https://docs.litellm.ai/docs/proxy/auto_routing)

* * *

## Model-level Guardrails[​](#model-level-guardrails "Direct link to Model-level Guardrails")

This release brings model-level guardrails support to your config.yaml + UI. This is great for cases when you have an on-prem and hosted model, and just want to run prevent sending PII to the hosted model.

```
model_list:
-model_name: claude-sonnet-4
litellm_params:
model: anthropic/claude-sonnet-4-20250514
api_key: os.environ/ANTHROPIC_API_KEY
api_base: https://api.anthropic.com/v1
guardrails:["azure-text-moderation"]# 👈 KEY CHANGE

guardrails:
-guardrail_name: azure-text-moderation
litellm_params:
guardrail: azure/text_moderations
mode:"post_call"
api_key: os.environ/AZURE_GUARDRAIL_API_KEY
api_base: os.environ/AZURE_GUARDRAIL_API_BASE 
```

[Read More](https://docs.litellm.ai/docs/proxy/guardrails/quick_start#model-level-guardrails)

* * *

v1.74.9-stable allows you to propagate MCP server specific authentication headers via LiteLLM

- Allowing users to specify which `header_name` is to be propagated to which `mcp_server` via headers
- Allows adding of different deployments of same MCP server type to use different authentication headers

[Read More](https://docs.litellm.ai/docs/mcp#new-server-specific-auth-headers-recommended)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)Fireworks AI`fireworks/models/kimi-k2-instruct`131k$0.6$2.5OpenRouter`openrouter/qwen/qwen-vl-plus`8192$0.21$0.63OpenRouter`openrouter/qwen/qwen3-coder`8192$1$5OpenRouter`openrouter/bytedance/ui-tars-1.5-7b`128k$0.10$0.20Groq`groq/qwen/qwen3-32b`131k$0.29$0.59VertexAI`vertex_ai/meta/llama-3.1-8b-instruct-maas`128k$0.00$0.00VertexAI`vertex_ai/meta/llama-3.1-405b-instruct-maas`128k$5$16VertexAI`vertex_ai/meta/llama-3.2-90b-vision-instruct-maas`128k$0.00$0.00Google AI Studio`gemini/gemini-2.0-flash-live-001`1,048,576$0.35$1.5Google AI Studio`gemini/gemini-2.5-flash-lite`1,048,576$0.1$0.4VertexAI`vertex_ai/gemini-2.0-flash-lite-001`1,048,576$0.35$1.5OpenAI`gpt-4o-realtime-preview-2025-06-03`128k$5$20

#### Features[​](#features "Direct link to Features")

- [**Lambda AI**](https://docs.litellm.ai/docs/providers/lambda_ai)
  
  - New LLM API provider - [PR #12817](https://github.com/BerriAI/litellm/pull/12817)
- [**Github Copilot**](https://docs.litellm.ai/docs/providers/github_copilot)
  
  - Dynamic endpoint support - [PR #12827](https://github.com/BerriAI/litellm/pull/12827)
- [**Morph**](https://docs.litellm.ai/docs/providers/morph)
  
  - New LLM API provider - [PR #12821](https://github.com/BerriAI/litellm/pull/12821)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Remove deprecated groq/qwen-qwq-32b - [PR #12832](https://github.com/BerriAI/litellm/pull/12831)
- [**Recraft**](https://docs.litellm.ai/docs/providers/recraft)
  
  - New image generation API - [PR #12832](https://github.com/BerriAI/litellm/pull/12832)
  - New image edits api - [PR #12874](https://github.com/BerriAI/litellm/pull/12874)
- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure/azure)
  
  - Support DefaultAzureCredential without hard-coded environment variables - [PR #12841](https://github.com/BerriAI/litellm/pull/12841)
- [**Hyperbolic**](https://docs.litellm.ai/docs/providers/hyperbolic)
  
  - New LLM API provider - [PR #12826](https://github.com/BerriAI/litellm/pull/12826)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai)
  
  - `/realtime` API - pass through intent query param - [PR #12838](https://github.com/BerriAI/litellm/pull/12838)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Add inpainting support for Amazon Nova Canvas - [PR #12949](https://github.com/BerriAI/litellm/pull/12949) s/o @[SantoshDhaladhuli](https://github.com/SantoshDhaladhuli)

#### Bugs[​](#bugs "Direct link to Bugs")

- **Gemini ([Google AI Studio](https://docs.litellm.ai/docs/providers/gemini) + [VertexAI](https://docs.litellm.ai/docs/providers/vertex))**
  
  - Fix leaking file descriptor error on sync calls - [PR #12824](https://github.com/BerriAI/litellm/pull/12824)
- **IBM Watsonx**
  
  - use correct parameter name for tool choice - [PR #9980](https://github.com/BerriAI/litellm/pull/9980)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Only show ‘reasoning\_effort’ for supported models - [PR #12847](https://github.com/BerriAI/litellm/pull/12847)
  - Handle $id and $schema in tool call requests (Anthropic API stopped accepting them) - [PR #12959](https://github.com/BerriAI/litellm/pull/12959)
- [**Openrouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - filter out cache\_control flag for non-anthropic models (allows usage with claude code) [https://github.com/BerriAI/litellm/pull/12850](https://github.com/BerriAI/litellm/pull/12850)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Shorten Gemini tool\_call\_id for Open AI compatibility - [PR #12941](https://github.com/BerriAI/litellm/pull/12941) s/o @[tonga54](https://github.com/tonga54)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Passthrough endpoints**](https://docs.litellm.ai/docs/pass_through/)
  
  - Make key/user/team cost tracking OSS - [PR #12847](https://github.com/BerriAI/litellm/pull/12847)
- [**/v1/models**](https://docs.litellm.ai/docs/providers/passthrough)
  
  - Return fallback models as part of api response - [PR #12811](https://github.com/BerriAI/litellm/pull/12811) s/o @[murad-khafizov](https://github.com/murad-khafizov)
- [**/vector\_stores**](https://docs.litellm.ai/docs/providers/passthrough)
  
  - Make permission management OSS - [PR #12990](https://github.com/BerriAI/litellm/pull/12990)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

1. `/batches`
   
   1. Skip invalid batch during cost tracking check (prev. Would stop all checks) - [PR #12782](https://github.com/BerriAI/litellm/pull/12782)
2. `/chat/completions`
   
   1. Fix async retryer on .acompletion() - [PR #12886](https://github.com/BerriAI/litellm/pull/12886)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-2 "Direct link to Features")

- [**Permission Management**](https://docs.litellm.ai/docs/mcp#grouping-mcps-access-groups)
  
  - Make permission management by key/team OSS - [PR #12988](https://github.com/BerriAI/litellm/pull/12988)
- [**MCP Alias**](https://docs.litellm.ai/docs/mcp#mcp-aliases)
  
  - Support mcp server aliases (useful for calling long mcp server names on Cursor) - [PR #12994](https://github.com/BerriAI/litellm/pull/12994)
- **Header Propagation**
  
  - Support propagating headers from client to backend MCP (useful for sending personal access tokens to backend MCP) - [PR #13003](https://github.com/BerriAI/litellm/pull/13003)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Usage**
  
  - Support viewing usage by model group - [PR #12890](https://github.com/BerriAI/litellm/pull/12890)
- **Virtual Keys**
  
  - New `key_type` field on `/key/generate` - allows specifying if key can call LLM API vs. Management routes - [PR #12909](https://github.com/BerriAI/litellm/pull/12909)
- **Models**
  
  - Add ‘auto router’ on UI - [PR #12960](https://github.com/BerriAI/litellm/pull/12960)
  - Show global retry policy on UI - [PR #12969](https://github.com/BerriAI/litellm/pull/12969)
  - Add model-level guardrails on create + update - [PR #13006](https://github.com/BerriAI/litellm/pull/13006)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **SSO**
  
  - Fix logout when SSO is enabled - [PR #12703](https://github.com/BerriAI/litellm/pull/12703)
  - Fix reset SSO when ui\_access\_mode is updated - [PR #13011](https://github.com/BerriAI/litellm/pull/13011)
- **Guardrails**
  
  - Show correct guardrails when editing a team - [PR #12823](https://github.com/BerriAI/litellm/pull/12823)
- **Virtual Keys**
  
  - Get updated token on regenerate key - [PR #12788](https://github.com/BerriAI/litellm/pull/12788)
  - Fix CVE with key injection - [PR #12840](https://github.com/BerriAI/litellm/pull/12840)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Google Cloud Model Armor**](https://docs.litellm.ai/docs/proxy/guardrails/model_armor)
  
  - Document new guardrail - [PR #12492](https://github.com/BerriAI/litellm/pull/12492)
- [**Pillar Security**](https://docs.litellm.ai/docs/proxy/guardrails/pillar_security)
  
  - New LLM Guardrail - [PR #12791](https://github.com/BerriAI/litellm/pull/12791)
- **CloudZero**
  
  - Allow exporting spend to cloudzero - [PR #12908](https://github.com/BerriAI/litellm/pull/12908)
- **Model-level Guardrails**
  
  - Support model-level guardrails - [PR #12968](https://github.com/BerriAI/litellm/pull/12968)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Fix `[tag]=false` when tag is set for tag-based metrics - [PR #12916](https://github.com/BerriAI/litellm/pull/12916)
- [**Guardrails AI**](https://docs.litellm.ai/docs/proxy/guardrails/guardrails_ai)
  
  - Use ‘validatedOutput’ to allow usage of “fix” guards - [PR #12891](https://github.com/BerriAI/litellm/pull/12891) s/o @[DmitriyAlergant](https://github.com/DmitriyAlergant)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-5 "Direct link to Features")

- [**Auto-Router**](https://docs.litellm.ai/docs/proxy/auto_routing)
  
  - New auto-router powered by `semantic-router` - [PR #12955](https://github.com/BerriAI/litellm/pull/12955)

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- **forward\_clientside\_headers**
  
  - Filter out `content-length` from headers (caused backend requests to hang) - [PR #12886](https://github.com/BerriAI/litellm/pull/12886/files)
- **Message Redaction**
  
  - Fix cannot pickle coroutine object error - [PR #13005](https://github.com/BerriAI/litellm/pull/13005)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-6 "Direct link to Features")

- **Benchmarks**
  
  - Updated litellm proxy benchmarks (p50, p90, p99 overhead) - [PR #12842](https://github.com/BerriAI/litellm/pull/12842)
- **Request Headers**
  
  - Added new `x-litellm-num-retries` request header
- **Swagger**
  
  - Support local swagger on custom root paths - [PR #12911](https://github.com/BerriAI/litellm/pull/12911)
- **Health**
  
  - Track cost + add tags for health checks done by LiteLLM Proxy - [PR #12880](https://github.com/BerriAI/litellm/pull/12880)

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- **Proxy Startup**
  
  - Fixes issue on startup where team member budget is None would block startup - [PR #12843](https://github.com/BerriAI/litellm/pull/12843)
- **Docker**
  
  - Move non-root docker to chain guard image (fewer vulnerabilities) - [PR #12707](https://github.com/BerriAI/litellm/pull/12707)
  - add azure-keyvault==4.2.0 to Docker img - [PR #12873](https://github.com/BerriAI/litellm/pull/12873)
- **Separate Health App**
  
  - Pass through cmd args via supervisord (enables user config to still work via docker) - [PR #12871](https://github.com/BerriAI/litellm/pull/12871)
- **Swagger**
  
  - Bump DOMPurify version (fixes vulnerability) - [PR #12911](https://github.com/BerriAI/litellm/pull/12911)
  - Add back local swagger bundle (enables swagger to work in air gapped env.) - [PR #12911](https://github.com/BerriAI/litellm/pull/12911)
- **Request Headers**
  
  - Make ‘user\_header\_name’ field check case insensitive (fixes customer budget enforcement for OpenWebUi) - [PR #12950](https://github.com/BerriAI/litellm/pull/12950)
- **SpendLogs**
  
  - Fix issues writing to DB when custom\_llm\_provider is None - [PR #13001](https://github.com/BerriAI/litellm/pull/13001)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @magicalne made their first contribution in [https://github.com/BerriAI/litellm/pull/12804](https://github.com/BerriAI/litellm/pull/12804)
- @pavangudiwada made their first contribution in [https://github.com/BerriAI/litellm/pull/12798](https://github.com/BerriAI/litellm/pull/12798)
- @mdiloreto made their first contribution in [https://github.com/BerriAI/litellm/pull/12707](https://github.com/BerriAI/litellm/pull/12707)
- @murad-khafizov made their first contribution in [https://github.com/BerriAI/litellm/pull/12811](https://github.com/BerriAI/litellm/pull/12811)
- @eagle-p made their first contribution in [https://github.com/BerriAI/litellm/pull/12791](https://github.com/BerriAI/litellm/pull/12791)
- @apoorv-sharma made their first contribution in [https://github.com/BerriAI/litellm/pull/12920](https://github.com/BerriAI/litellm/pull/12920)
- @SantoshDhaladhuli made their first contribution in [https://github.com/BerriAI/litellm/pull/12949](https://github.com/BerriAI/litellm/pull/12949)
- @tonga54 made their first contribution in [https://github.com/BerriAI/litellm/pull/12941](https://github.com/BerriAI/litellm/pull/12941)
- @sings-to-bees-on-wednesdays made their first contribution in [https://github.com/BerriAI/litellm/pull/12950](https://github.com/BerriAI/litellm/pull/12950)

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.74.7-stable...v1.74.9.rc-draft)[​](#full-changelog "Direct link to full-changelog")