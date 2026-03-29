---
title: v1.77.3-stable - Priority Based Rate Limiting
url: https://docs.litellm.ai/release_notes/v1-77-3
source: sitemap
fetched_at: 2026-01-21T19:42:47.62802492-03:00
rendered_js: false
word_count: 1086
summary: This document outlines the release notes for LiteLLM version 1.77.3, highlighting performance improvements, priority quota reservation, and new provider integrations. It also details specific bug fixes and feature updates across various LLM providers and API endpoints.
tags:
    - litellm
    - release-notes
    - performance-optimization
    - rate-limiting
    - model-support
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
docker.litellm.ai/berriai/litellm:v1.77.3-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **+550 RPS Performance Improvements** - Optimizations in request handling and object initialization.
- **Priority Quota Reservation** - Proxy admins can now reserve TPM/RPM capacity for specific keys.

## Priority Quota Reservation[​](#priority-quota-reservation "Direct link to Priority Quota Reservation")

This release adds support for priority quota reservation. This allows Proxy Admins to reserve specific percentages of model capacity for different use cases.

This is great for use cases where you want to ensure your realtime use cases must always get priority responses and background development jobs can take longer.

This release adds support for priority quota reservation. This allows **Proxy Admins** to reserve TPM/RPM capacity for keys based on metadata priority levels, ensuring critical production workloads get guaranteed access regardless of development traffic volume.

Get started [here](https://docs.litellm.ai/docs/proxy/dynamic_rate_limit#priority-quota-reservation)

## +550 RPS Performance Improvements[​](#550-rps-performance-improvements "Direct link to +550 RPS Performance Improvements")

This release delivers significant RPS improvements through targeted optimizations.

We've achieved a +500 RPS boost by fixing cache type inconsistencies that were causing frequent cache misses, plus an additional +50 RPS by removing unnecessary coroutine checks from the hot path.

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)FeaturesSambaNova`sambanova/deepseek-v3.1`128K$0.90$0.90Chat completionsSambaNova`sambanova/gpt-oss-120b`128K$0.72$0.72Chat completionsOVHCloudVarious modelsVariesContact providerContact providerChat completionsCompactifAIVarious modelsVariesContact providerContact providerChat completionsTwelveLabs`twelvelabs/marengo-embed-2.7`32K$0.12$0.00Embeddings

#### Features[​](#features "Direct link to Features")

- [**OVHCloud AI Endpoints**](https://docs.litellm.ai/docs/providers/ovhcloud)
  
  - New provider support with comprehensive model catalog - [PR #14494](https://github.com/BerriAI/litellm/pull/14494)
- [**CompactifAI**](https://docs.litellm.ai/docs/providers/compactifai)
  
  - New provider integration - [PR #14532](https://github.com/BerriAI/litellm/pull/14532)
- [**SambaNova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Added DeepSeek v3.1 and GPT-OSS-120B models - [PR #14500](https://github.com/BerriAI/litellm/pull/14500)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Cross-region inference profile cost calculation - [PR #14566](https://github.com/BerriAI/litellm/pull/14566)
  - AWS external ID parameter support for authentication - [PR #14582](https://github.com/BerriAI/litellm/pull/14582)
  - CountTokens API implementation - [PR #14557](https://github.com/BerriAI/litellm/pull/14557)
  - Titan V2 encoding\_format parameter support - [PR #14687](https://github.com/BerriAI/litellm/pull/14687)
  - Nova Canvas image generation inference profiles - [PR #14578](https://github.com/BerriAI/litellm/pull/14578)
  - Bedrock Batches API - batch processing support with file upload and request transformation - [PR #14618](https://github.com/BerriAI/litellm/pull/14618)
  - Bedrock Twelve Labs embedding provider support - [PR #14697](https://github.com/BerriAI/litellm/pull/14697)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Gemini labels field provider-aware filtering - [PR #14563](https://github.com/BerriAI/litellm/pull/14563)
  - Gemini Batch API support - [PR #14733](https://github.com/BerriAI/litellm/pull/14733)
- [**Volcengine**](https://docs.litellm.ai/docs/providers/volcengine)
  
  - Fixed thinking parameters when disabled - [PR #14569](https://github.com/BerriAI/litellm/pull/14569)
- [**Cohere**](https://docs.litellm.ai/docs/providers/cohere)
  
  - Handle Generate API deprecation, default to chat endpoints - [PR #14676](https://github.com/BerriAI/litellm/pull/14676)
- [**TwelveLabs**](https://docs.litellm.ai/docs/providers/twelvelabs)
  
  - Added Marengo Embed 2.7 embedding support - [PR #14674](https://github.com/BerriAI/litellm/pull/14674)

### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Empty arguments handling in tool call invocation - [PR #14583](https://github.com/BerriAI/litellm/pull/14583)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Avoid deepcopy crash with non-pickleables in Gemini/Vertex - [PR #14418](https://github.com/BerriAI/litellm/pull/14418)
- [**XAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - Fix unsupported stop parameter for grok-code models - [PR #14565](https://github.com/BerriAI/litellm/pull/14565)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Updated error message for Gemini API - [PR #14589](https://github.com/BerriAI/litellm/pull/14589)
  - Fixed 2.5 Flash Image Preview model routing - [PR #14715](https://github.com/BerriAI/litellm/pull/14715)
  - API key passing for token counting endpoints - [PR #14744](https://github.com/BerriAI/litellm/pull/14744)

#### New Provider Support[​](#new-provider-support "Direct link to New Provider Support")

- [**OVHCloud AI Endpoints**](https://docs.litellm.ai/docs/providers/ovhcloud)
  
  - Complete provider integration with model catalog and authentication - [PR #14494](https://github.com/BerriAI/litellm/pull/14494)
- [**CompactifAI**](https://docs.litellm.ai/docs/providers/compactifai)
  
  - New provider support with documentation - [PR #14532](https://github.com/BerriAI/litellm/pull/14532)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/responses**](https://docs.litellm.ai/docs/response_api)
  
  - Added cancel endpoint support for non-admin users - [PR #14594](https://github.com/BerriAI/litellm/pull/14594)
  - Improved response session handling and cold storage configuration with s3 - [PR #14534](https://github.com/BerriAI/litellm/pull/14534)
  - Added OpenAI & Azure /responses/cancel endpoint support - [PR #14561](https://github.com/BerriAI/litellm/pull/14561)
- **General**
  
  - Enhanced rate limit error messages with details - [PR #14736](https://github.com/BerriAI/litellm/pull/14736)
  - Middle-truncation for spend log payloads - [PR #14637](https://github.com/BerriAI/litellm/pull/14637)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**/chat/completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Fixed completion chat ID handling - [PR #14548](https://github.com/BerriAI/litellm/pull/14548)
  - Prevent AttributeError for \_get\_tags\_from\_request\_kwargs - [PR #14735](https://github.com/BerriAI/litellm/pull/14735)
- [**/responses**](https://docs.litellm.ai/docs/response_api)
  
  - Fixed cost calculation - [PR #14675](https://github.com/BerriAI/litellm/pull/14675)
- **General**
  
  - Rate limiter AttributeError fix - [PR #14609](https://github.com/BerriAI/litellm/pull/14609)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

- **Responses API Cost Calculation** fix - [PR #14675](https://github.com/BerriAI/litellm/pull/14675)
- **Anthropic Cache Token Pricing** - Separate 1-hour vs 5-minute cache creation costs - [PR #14620](https://github.com/BerriAI/litellm/pull/14620), [PR #14652](https://github.com/BerriAI/litellm/pull/14652)
- **Indochina Time Timezone** support for budget resets - [PR #14666](https://github.com/BerriAI/litellm/pull/14666)
- **Soft Budget Alert Cache Issues** - Resolved soft budget alert cache issues - [PR #14491](https://github.com/BerriAI/litellm/pull/14491)
- **Dynamic Rate Limiter v3** - Priority routing improvements - [PR #14734](https://github.com/BerriAI/litellm/pull/14734)
- **Enhanced Rate Limit Errors** - More detailed error messages - [PR #14736](https://github.com/BerriAI/litellm/pull/14736)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **Team Member Service Account Keys** - Allow team members to view keys they create - [PR #14619](https://github.com/BerriAI/litellm/pull/14619)
- **Default Budget for JWT Teams** - Auto-assign budgets to generated teams - [PR #14514](https://github.com/BerriAI/litellm/pull/14514)
- **SSO Access Control Groups** - Enhanced token info endpoint integration - [PR #14738](https://github.com/BerriAI/litellm/pull/14738)
- **Health Test Connect Protection** - Restrict access based on model creation permissions - [PR #14650](https://github.com/BerriAI/litellm/pull/14650)
- **Amazon Bedrock Guardrail Info View** - Enhanced logging visualization - [PR #14696](https://github.com/BerriAI/litellm/pull/14696)

#### Bug Fixes[​](#bug-fixes-1 "Direct link to Bug Fixes")

- **SCIM v2** - Fix group PUSH and PUT operations for non-existent members - [PR #14581](https://github.com/BerriAI/litellm/pull/14581)
- **Guardrail View/Edit/Delete** behavior fixes - [PR #14622](https://github.com/BerriAI/litellm/pull/14622)
- **In-Memory Guardrail** update failures - [PR #14653](https://github.com/BerriAI/litellm/pull/14653)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-3 "Direct link to Features")

- [**DataDog**](https://docs.litellm.ai/docs/proxy/logging#datadog)
  
  - Enhanced spend tracking metrics - [PR #14555](https://github.com/BerriAI/litellm/pull/14555)
  - Stream support with is\_streamed\_request parameter - [PR #14673](https://github.com/BerriAI/litellm/pull/14673)
  - Fixed tool calls metadata passing - [PR #14531](https://github.com/BerriAI/litellm/pull/14531)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Added logging support for Responses API - [PR #14597](https://github.com/BerriAI/litellm/pull/14597)
- [**Langsmith**](https://docs.litellm.ai/docs/proxy/logging#langsmith)
  
  - Langsmith Sampling Rate - Key/Team-level tracing configuration - [PR #14740](https://github.com/BerriAI/litellm/pull/14740)
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/logging#prometheus)
  
  - Multi-worker support improvements - [PR #14530](https://github.com/BerriAI/litellm/pull/14530)
  - User email labels in monitoring - [PR #14520](https://github.com/BerriAI/litellm/pull/14520)
- [**Opik**](https://docs.litellm.ai/docs/proxy/logging#opik)
  
  - Fixed timezone issue - [PR #14708](https://github.com/BerriAI/litellm/pull/14708)

### Bug Fixes[​](#bug-fixes-2 "Direct link to Bug Fixes")

- [**S3**](https://docs.litellm.ai/docs/proxy/logging#s3-buckets)
  
  - Fixed 404 error when using s3\_endpoint\_url - [PR #14559](https://github.com/BerriAI/litellm/pull/14559)

#### Guardrails[​](#guardrails "Direct link to Guardrails")

- **Tool Permission Guardrail** - Fine-grained tool access control - [PR #14519](https://github.com/BerriAI/litellm/pull/14519)
- **Bedrock Guardrails** - Selective guarding support with runtime endpoint configuration - [PR #14575](https://github.com/BerriAI/litellm/pull/14575), [PR #14650](https://github.com/BerriAI/litellm/pull/14650)
- **Default Last Message** in guardrails - [PR #14640](https://github.com/BerriAI/litellm/pull/14640)
- **AWS exceptions handling despite 200 response** - [PR #14658](https://github.com/BerriAI/litellm/pull/14658)

#### New Integration[​](#new-integration "Direct link to New Integration")

- [**PostHog**](https://docs.litellm.ai/docs/observability/posthog) - Complete observability integration for LiteLLM usage tracking and analytics - [PR #14610](https://github.com/BerriAI/litellm/pull/14610)

* * *

## MCP Gateway[​](#mcp-gateway "Direct link to MCP Gateway")

- **MCP Server Alias Parsing** - Multi-part URL path support - [PR #14558](https://github.com/BerriAI/litellm/pull/14558)
- **MCP Filter Recomputation** - After server deletion - [PR #14542](https://github.com/BerriAI/litellm/pull/14542)
- **MCP Gateway Tools List** improvements - [PR #14695](https://github.com/BerriAI/litellm/pull/14695)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

- **+500 RPS Performance Boost** when sending the `user` field - [PR #14616](https://github.com/BerriAI/litellm/pull/14616)
- **+50 RPS** by removing iscoroutine from hot path - [PR #14649](https://github.com/BerriAI/litellm/pull/14649)
- **7% reduction** in **init** overhead - [PR #14689](https://github.com/BerriAI/litellm/pull/14689)
- **Generic Object Pool** implementation for better resource management - [PR #14702](https://github.com/BerriAI/litellm/pull/14702)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Middle-Truncation** for spend log payloads - [PR #14637](https://github.com/BerriAI/litellm/pull/14637)

#### Security[​](#security "Direct link to Security")

- **Security Update** - Bump aiohttp==3.12.14, fix CVE-2025-53643 - [PR #14638](https://github.com/BerriAI/litellm/pull/14638)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @luisfucros made their first contribution in [PR #14500](https://github.com/BerriAI/litellm/pull/14500)
- @hanakannzashi made their first contribution in [PR #14548](https://github.com/BerriAI/litellm/pull/14548)
- @eliasto made their first contribution in [PR #14494](https://github.com/BerriAI/litellm/pull/14494)
- @Rasmusafj made their first contribution in [PR #14491](https://github.com/BerriAI/litellm/pull/14491)
- @LingXuanYin made their first contribution in [PR #14569](https://github.com/BerriAI/litellm/pull/14569)
- @ronaldpereira made their first contribution in [PR #14613](https://github.com/BerriAI/litellm/pull/14613)
- @hula-la made their first contribution in [PR #14534](https://github.com/BerriAI/litellm/pull/14534)
- @carlos-marchal-ph made their first contribution in [PR #14610](https://github.com/BerriAI/litellm/pull/14610)
- @akraines made their first contribution in [PR #14637](https://github.com/BerriAI/litellm/pull/14637)
- @mrFranklin made their first contribution in [PR #14708](https://github.com/BerriAI/litellm/pull/14708)
- @tcx4c70 made their first contribution in [PR #14675](https://github.com/BerriAI/litellm/pull/14675)
- @michaeltansg made their first contribution in [PR #14666](https://github.com/BerriAI/litellm/pull/14666)
- @tosi29 made their first contribution in [PR #14725](https://github.com/BerriAI/litellm/pull/14725)
- @gmdfalk made their first contribution in [PR #14735](https://github.com/BerriAI/litellm/pull/14735)
- @FelipeRodriguesGare made their first contribution in [PR #14733](https://github.com/BerriAI/litellm/pull/14733)
- @mritunjaysharma394 made their first contribution in [PR #14678](https://github.com/BerriAI/litellm/pull/14678)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.77.2.rc.1...v1.77.3.rc.1)[​](#full-changelog "Direct link to full-changelog")