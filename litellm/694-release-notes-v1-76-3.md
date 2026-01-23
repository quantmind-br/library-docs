---
title: v1.76.3-stable - Performance, Video Generation & CloudZero Integration
url: https://docs.litellm.ai/release_notes/v1-76-3
source: sitemap
fetched_at: 2026-01-21T19:42:43.234929447-03:00
rendered_js: false
word_count: 1086
summary: Release notes for LiteLLM v1.76.3 detailing performance optimizations, video generation support, new model integrations, and critical security updates.
tags:
    - litellm
    - release-notes
    - performance-optimization
    - video-generation
    - model-support
    - bug-fixes
category: other
---

warning

This release has a known issue where startup is leading to Out of Memory errors when deploying on Kubernetes. We recommend waiting before upgrading to this version.

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:v1.76.3
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Major Performance Improvements** +400 RPS when using correct amount of workers + CPU cores combination
- **Video Generation Support** - Added Google AI Studio and Vertex AI Veo Video Generation through LiteLLM Pass through routes
- **CloudZero Integration** - New cost tracking integration for exporting LiteLLM Usage and Spend data to CloudZero.

## Major Changes[​](#major-changes "Direct link to Major Changes")

- **Performance Optimization**: LiteLLM Proxy now achieves +400 RPS when using correct amount of CPU cores - [PR #14153](https://github.com/BerriAI/litellm/pull/14153), [PR #14242](https://github.com/BerriAI/litellm/pull/14242)
  
  By default, LiteLLM will now use `num_workers = os.cpu_count()` to achieve optimal performance.
  
  **Override Options:**
  
  Set environment variable:
  
  ```
  DEFAULT_NUM_WORKERS_LITELLM_PROXY=1
  ```
  
  Or start LiteLLM Proxy with:
- **Security Fix**: Fixed memory\_usage\_in\_mem\_cache cache endpoint vulnerability - [PR #14229](https://github.com/BerriAI/litellm/pull/14229)

* * *

## Performance Improvements[​](#performance-improvements "Direct link to Performance Improvements")

This release includes significant performance optimizations. On our internal benchmarks we saw 1 instance get +400 RPS when using correct amount of workers + CPU cores combination.

- **+400 RPS Performance Boost** - LiteLLM Proxy now uses correct amount of CPU cores for optimal performance - [PR #14153](https://github.com/BerriAI/litellm/pull/14153)
- **Default CPU Workers** - Changed DEFAULT\_NUM\_WORKERS\_LITELLM\_PROXY default to number of CPUs - [PR #14242](https://github.com/BerriAI/litellm/pull/14242)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesOpenRouter`openrouter/openai/gpt-4.1`1M$2.00$8.00Chat completions with visionOpenRouter`openrouter/openai/gpt-4.1-mini`1M$0.40$1.60Efficient chat completionsOpenRouter`openrouter/openai/gpt-4.1-nano`1M$0.10$0.40Ultra-efficient chatVertex AI`vertex_ai/openai/gpt-oss-20b-maas`131K$0.075$0.30Reasoning supportVertex AI`vertex_ai/openai/gpt-oss-120b-maas`131K$0.15$0.60Advanced reasoningGemini`gemini/veo-3.0-generate-preview`1K-$0.75/secVideo generationGemini`gemini/veo-3.0-fast-generate-preview`1K-$0.40/secFast video generationGemini`gemini/veo-2.0-generate-001`1K-$0.35/secVideo generationVolcengine`doubao-embedding-large`4KFreeFree2048-dim embeddingsTogether AI`together_ai/deepseek-ai/DeepSeek-V3.1`128K$0.60$1.70Reasoning support

#### Features[​](#features "Direct link to Features")

- [**Google Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Added 'thoughtSignature' support via 'thinking\_blocks' - [PR #14122](https://github.com/BerriAI/litellm/pull/14122)
  - Added support for reasoning\_effort='minimal' for Gemini models - [PR #14262](https://github.com/BerriAI/litellm/pull/14262)
- [**OpenRouter**](https://docs.litellm.ai/docs/providers/openrouter)
  
  - Added GPT-4.1 model family - [PR #14101](https://github.com/BerriAI/litellm/pull/14101)
- [**Groq**](https://docs.litellm.ai/docs/providers/groq)
  
  - Added support for reasoning\_effort parameter - [PR #14207](https://github.com/BerriAI/litellm/pull/14207)
- [**X.AI**](https://docs.litellm.ai/docs/providers/xai)
  
  - Fixed XAI cost calculation - [PR #14127](https://github.com/BerriAI/litellm/pull/14127)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Added support for GPT-OSS models on Vertex AI - [PR #14184](https://github.com/BerriAI/litellm/pull/14184)
  - Added additionalProperties to Vertex AI Schema definition - [PR #14252](https://github.com/BerriAI/litellm/pull/14252)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Handle output parsing responses API output - [PR #14121](https://github.com/BerriAI/litellm/pull/14121)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Added unified 'thinking' param support via `reasoning_content` - [PR #14121](https://github.com/BerriAI/litellm/pull/14121)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Added supported text field to anthropic citation response - [PR #14126](https://github.com/BerriAI/litellm/pull/14126)
- [**OCI Provider**](https://docs.litellm.ai/docs/providers/oci)
  
  - Handle assistant messages with both content and tool\_calls - [PR #14171](https://github.com/BerriAI/litellm/pull/14171)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Fixed structure output - [PR #14130](https://github.com/BerriAI/litellm/pull/14130)
  - Added initial support for Bedrock Batches API - [PR #14190](https://github.com/BerriAI/litellm/pull/14190)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks)
  
  - Added support for anthropic citation API in Databricks - [PR #14077](https://github.com/BerriAI/litellm/pull/14077)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Google Gemini (Google AI Studio + Vertex AI)**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fixed Gemini 2.5 Pro schema validation with OpenAI-style type arrays in tools - [PR #14154](https://github.com/BerriAI/litellm/pull/14154)
  - Fixed Gemini Tool Calling empty enum property - [PR #14155](https://github.com/BerriAI/litellm/pull/14155)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**Volcengine**](https://docs.litellm.ai/docs/providers/volcengine)
  
  - Added Volcengine embedding module with handler and transformation logic - [PR #14028](https://github.com/BerriAI/litellm/pull/14028)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**Images API**](https://docs.litellm.ai/docs/image_generation)
  
  - Added pass through image generation and image editing on OpenAI - [PR #14292](https://github.com/BerriAI/litellm/pull/14292)
  - Support extra\_body parameter for image generation - [PR #14211](https://github.com/BerriAI/litellm/pull/14211)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - Fixed response API for reasoning item in input for litellm proxy - [PR #14200](https://github.com/BerriAI/litellm/pull/14200)
  - Added structured output for SDK - [PR #14206](https://github.com/BerriAI/litellm/pull/14206)
- [**Bedrock Passthrough**](https://docs.litellm.ai/docs/pass_through/bedrock)
  
  - Support AWS\_BEDROCK\_RUNTIME\_ENDPOINT on bedrock passthrough - [PR #14156](https://github.com/BerriAI/litellm/pull/14156)
- [**Google AI Studio Passthrough**](https://docs.litellm.ai/docs/pass_through/google_ai_studio)
  
  - Allow using Veo Video Generation through LiteLLM Pass through routes - [PR #14228](https://github.com/BerriAI/litellm/pull/14228)
- **General**
  
  - Added support for safety\_identifier parameter in chat.completions.create - [PR #14174](https://github.com/BerriAI/litellm/pull/14174)
  - Fixed misclassified 500 error on invalid image\_url in /chat/completions request - [PR #14149](https://github.com/BerriAI/litellm/pull/14149)
  - Fixed token count error for Gemini CLI - [PR #14133](https://github.com/BerriAI/litellm/pull/14133)

#### Bugs[​](#bugs "Direct link to Bugs")

- **General**
  
  - Remove "/" or ":" from model name when being used as h11 header name - [PR #14191](https://github.com/BerriAI/litellm/pull/14191)
  - Bug fix for openai.gpt-oss when using reasoning\_effort parameter - [PR #14300](https://github.com/BerriAI/litellm/pull/14300)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

### Features[​](#features-2 "Direct link to Features")

- Added header support for spend\_logs\_metadata - [PR #14186](https://github.com/BerriAI/litellm/pull/14186)
- Litellm passthrough cost tracking for chat completion - [PR #14256](https://github.com/BerriAI/litellm/pull/14256)

### Bug Fixes[​](#bug-fixes-1 "Direct link to Bug Fixes")

- Fixed TPM Rate Limit Bug - [PR #14237](https://github.com/BerriAI/litellm/pull/14237)
- Fixed Key Budget not resets at expectable times - [PR #14241](https://github.com/BerriAI/litellm/pull/14241)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **UI Improvements**
  
  - Logs page screen size fixed - [PR #14135](https://github.com/BerriAI/litellm/pull/14135)
  - Create Organization Tooltip added on Success - [PR #14132](https://github.com/BerriAI/litellm/pull/14132)
  - Back to Keys should say Back to Logs - [PR #14134](https://github.com/BerriAI/litellm/pull/14134)
  - Add client side pagination on All Models table - [PR #14136](https://github.com/BerriAI/litellm/pull/14136)
  - Model Filters UI improvement - [PR #14131](https://github.com/BerriAI/litellm/pull/14131)
  - Remove table filter on user info page - [PR #14169](https://github.com/BerriAI/litellm/pull/14169)
  - Team name badge added on the User Details - [PR #14003](https://github.com/BerriAI/litellm/pull/14003)
  - Fix: Log page parameter passing error - [PR #14193](https://github.com/BerriAI/litellm/pull/14193)
- **Authentication & Authorization**
  
  - Support for ES256/ES384/ES512 and EdDSA JWT verification - [PR #14118](https://github.com/BerriAI/litellm/pull/14118)
  - Ensure `team_id` is a required field for generating service account keys - [PR #14270](https://github.com/BerriAI/litellm/pull/14270)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **General**
  
  - Validate store model in db setting - [PR #14269](https://github.com/BerriAI/litellm/pull/14269)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Datadog**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Ensure `apm_id` is set on DD LLM Observability traces - [PR #14272](https://github.com/BerriAI/litellm/pull/14272)
- [**Braintrust**](https://docs.litellm.ai/docs/proxy/logging#braintrust)
  
  - Fix logging when OTEL is enabled - [PR #14122](https://github.com/BerriAI/litellm/pull/14122)
- [**OTEL**](https://docs.litellm.ai/docs/proxy/logging#otel)
  
  - Optional Metrics and Logs following semantic conventions - [PR #14179](https://github.com/BerriAI/litellm/pull/14179)
- [**Slack Alerting**](https://docs.litellm.ai/docs/proxy/alerting)
  
  - Added alert type to alert message to slack for easier handling - [PR #14176](https://github.com/BerriAI/litellm/pull/14176)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- Added guardrail to the Anthropic API endpoint - [PR #14107](https://github.com/BerriAI/litellm/pull/14107)

#### New Integration[​](#new-integration "Direct link to New Integration")

- [**CloudZero**](https://docs.litellm.ai/docs/proxy/cost_tracking)
  
  - LiteLLM x CloudZero Integration for Cost Tracking - [PR #14296](https://github.com/BerriAI/litellm/pull/14296)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-5 "Direct link to Features")

- **Performance**
  
  - LiteLLM Proxy: +400 RPS when using correct amount of CPU cores - [PR #14153](https://github.com/BerriAI/litellm/pull/14153)
  - Allow using `x-litellm-stream-timeout` header for stream timeout in requests - [PR #14147](https://github.com/BerriAI/litellm/pull/14147)
  - Change DEFAULT\_NUM\_WORKERS\_LITELLM\_PROXY default to number CPUs - [PR #14242](https://github.com/BerriAI/litellm/pull/14242)
- **Monitoring**
  
  - Added Prometheus missing metrics - [PR #14139](https://github.com/BerriAI/litellm/pull/14139)
- **Timeout**
  
  - **Stream Timeout Control** - Allow using `x-litellm-stream-timeout` header for stream timeout in requests - [PR #14147](https://github.com/BerriAI/litellm/pull/14147)
- **Routing**
  
  - Fixed x-litellm-tags not routing with Responses API - [PR #14289](https://github.com/BerriAI/litellm/pull/14289)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **Security**
  
  - Fixed memory\_usage\_in\_mem\_cache cache endpoint vulnerability - [PR #14229](https://github.com/BerriAI/litellm/pull/14229)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Features[​](#features-6 "Direct link to Features")

- **SCIM Support**
  
  - Added better SCIM debugging - [PR #14221](https://github.com/BerriAI/litellm/pull/14221)
  - Bug fixes for handling SCIM Group Memberships - [PR #14226](https://github.com/BerriAI/litellm/pull/14226)
- **Kubernetes**
  
  - Added optional PodDisruptionBudget for litellm proxy - [PR #14093](https://github.com/BerriAI/litellm/pull/14093)
- **Error Handling**
  
  - Add model to azure error message - [PR #14294](https://github.com/BerriAI/litellm/pull/14294)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @iabhi4 made their first contribution in [PR #14093](https://github.com/BerriAI/litellm/pull/14093)
- @zainhas made their first contribution in [PR #14087](https://github.com/BerriAI/litellm/pull/14087)
- @LifeDJIK made their first contribution in [PR #14146](https://github.com/BerriAI/litellm/pull/14146)
- @retanoj made their first contribution in [PR #14133](https://github.com/BerriAI/litellm/pull/14133)
- @zhxlp made their first contribution in [PR #14193](https://github.com/BerriAI/litellm/pull/14193)
- @kayoch1n made their first contribution in [PR #14191](https://github.com/BerriAI/litellm/pull/14191)
- @kutsushitaneko made their first contribution in [PR #14171](https://github.com/BerriAI/litellm/pull/14171)
- @mjmendo made their first contribution in [PR #14176](https://github.com/BerriAI/litellm/pull/14176)
- @HarshavardhanK made their first contribution in [PR #14213](https://github.com/BerriAI/litellm/pull/14213)
- @eycjur made their first contribution in [PR #14207](https://github.com/BerriAI/litellm/pull/14207)
- @22mSqRi made their first contribution in [PR #14241](https://github.com/BerriAI/litellm/pull/14241)
- @onlylhf made their first contribution in [PR #14028](https://github.com/BerriAI/litellm/pull/14028)
- @btpemercier made their first contribution in [PR #11319](https://github.com/BerriAI/litellm/pull/11319)
- @tremlin made their first contribution in [PR #14287](https://github.com/BerriAI/litellm/pull/14287)
- @TobiMayr made their first contribution in [PR #14262](https://github.com/BerriAI/litellm/pull/14262)
- @Eitan1112 made their first contribution in [PR #14252](https://github.com/BerriAI/litellm/pull/14252)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.76.1-nightly...v1.76.3-nightly)[​](#full-changelog "Direct link to full-changelog")