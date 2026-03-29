---
title: v1.77.2-stable - Bedrock Batches API
url: https://docs.litellm.ai/release_notes/v1-77-2
source: sitemap
fetched_at: 2026-01-21T19:42:43.751710816-03:00
rendered_js: false
word_count: 509
summary: This document provides the release notes for LiteLLM version 1.77.2, detailing new model support, Bedrock Batches API integration, and enhanced tiered pricing for Qwen models.
tags:
    - litellm-release
    - changelog
    - api-integration
    - model-deployment
    - cost-tracking
    - performance-optimization
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
docker.litellm.ai/berriai/litellm:main-v1.77.2-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Bedrock Batches API** - Support for creating Batch Inference Jobs on Bedrock using LiteLLM's unified batch API (OpenAI compatible)
- **Qwen API Tiered Pricing** - Cost tracking support for Dashscope (Qwen) models with multiple pricing tiers

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### New Model Support[​](#new-model-support "Direct link to New Model Support")

ProviderModelContext WindowPricing ($/1M tokens)FeaturesDeepInfra`deepinfra/deepseek-ai/DeepSeek-R1`164K**Input:** $0.70  
**Output:** $2.40Chat completions, tool callingHeroku`heroku/claude-4-sonnet`8KContact provider for pricingFunction calling, tool choiceHeroku`heroku/claude-3-7-sonnet`8KContact provider for pricingFunction calling, tool choiceHeroku`heroku/claude-3-5-sonnet-latest`8KContact provider for pricingFunction calling, tool choiceHeroku`heroku/claude-3-5-haiku`4KContact provider for pricingFunction calling, tool choiceDashscope`dashscope/qwen-plus-latest`1M**Tiered Pricing:**  
• 0-256K tokens: $0.40 / $1.20  
• 256K-1M tokens: $1.20 / $3.60Function calling, reasoningDashscope`dashscope/qwen3-max-preview`262K**Tiered Pricing:**  
• 0-32K tokens: $1.20 / $6.00  
• 32K-128K tokens: $2.40 / $12.00  
• 128K-252K tokens: $3.00 / $15.00Function calling, reasoningDashscope`dashscope/qwen-flash`1M**Tiered Pricing:**  
• 0-256K tokens: $0.05 / $0.40  
• 256K-1M tokens: $0.25 / $2.00Function calling, reasoningDashscope`dashscope/qwen3-coder-plus`1M**Tiered Pricing:**  
• 0-32K tokens: $1.00 / $5.00  
• 32K-128K tokens: $1.80 / $9.00  
• 128K-256K tokens: $3.00 / $15.00  
• 256K-1M tokens: $6.00 / $60.00Function calling, reasoning, cachingDashscope`dashscope/qwen3-coder-flash`1M**Tiered Pricing:**  
• 0-32K tokens: $0.30 / $1.50  
• 32K-128K tokens: $0.50 / $2.50  
• 128K-256K tokens: $0.80 / $4.00  
• 256K-1M tokens: $1.60 / $9.60Function calling, reasoning, caching

* * *

#### Features[​](#features "Direct link to Features")

- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock_batches)
  
  - Bedrock Batches API - batch processing support with file upload and request transformation - [PR #14518](https://github.com/BerriAI/litellm/pull/14518), [PR #14522](https://github.com/BerriAI/litellm/pull/14522)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Added transcription endpoint support - [PR #14523](https://github.com/BerriAI/litellm/pull/14523)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - `ollama_chat/` - images, thinking, and content as list handling - [PR #14523](https://github.com/BerriAI/litellm/pull/14523)
- **General**
  
  - New debug flag for detailed request/response logging [PR #14482](https://github.com/BerriAI/litellm/pull/14482)

#### Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure)
  
  - Fixed extra\_body injection causing payload rejection in image generation - [PR #14475](https://github.com/BerriAI/litellm/pull/14475)
- [**LM Studio**](https://docs.litellm.ai/docs/providers/lm-studio)
  
  - Resolved illegal Bearer header value issue - [PR #14512](https://github.com/BerriAI/litellm/pull/14512)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Bug Fixes[​](#bug-fixes-1 "Direct link to Bug Fixes")

- [**/messages**](https://docs.litellm.ai/docs/anthropic_unified)
  
  - Don't send content block after message w/ finish reason + usage block - [PR #14477](https://github.com/BerriAI/litellm/pull/14477)
- [**/generateContent**](https://docs.litellm.ai/docs/generateContent)
  
  - Gemini CLI Integration - Fixed token count errors - [PR #14451](https://github.com/BerriAI/litellm/pull/14451), [PR #14417](https://github.com/BerriAI/litellm/pull/14417)

* * *

## Spend Tracking, Budgets and Rate Limiting[​](#spend-tracking-budgets-and-rate-limiting "Direct link to Spend Tracking, Budgets and Rate Limiting")

#### Features[​](#features-1 "Direct link to Features")

- [**Qwen API Tiered Pricing**](https://docs.litellm.ai/docs/providers/dashscope) - Added comprehensive tiered cost tracking for Dashscope/Qwen models - [PR #14471](https://github.com/BerriAI/litellm/pull/14471), [PR #14479](https://github.com/BerriAI/litellm/pull/14479)

#### Bug Fixes[​](#bug-fixes-2 "Direct link to Bug Fixes")

- **Provider Budgets** - Fixed provider budget calculations - [PR #14459](https://github.com/BerriAI/litellm/pull/14459)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-2 "Direct link to Features")

- **User Headers Mapping** - New X-LiteLLM Users mapping feature for enhanced user tracking - [PR #14485](https://github.com/BerriAI/litellm/pull/14485)
- **Key Unblocking** - Support for hashed tokens in `/key/unblock` endpoint - [PR #14477](https://github.com/BerriAI/litellm/pull/14477)
- **Model Group Header Forwarding** - Enhanced wildcard model support with documentation - [PR #14528](https://github.com/BerriAI/litellm/pull/14528)

#### Bug Fixes[​](#bug-fixes-3 "Direct link to Bug Fixes")

- **Log Tab Key Alias** - Fixed filtering inaccuracies for failed logs - [PR #14469](https://github.com/BerriAI/litellm/pull/14469), [PR #14529](https://github.com/BerriAI/litellm/pull/14529)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-3 "Direct link to Features")

- **Noma Integration** - Added non-blocking monitor mode with anonymize input support - [PR #14401](https://github.com/BerriAI/litellm/pull/14401)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Performance[​](#performance "Direct link to Performance")

- Removed dynamic creation of static values - [PR #14538](https://github.com/BerriAI/litellm/pull/14538)
- Using `_PROXY_MaxParallelRequestsHandler_v3` by default for optimal throughput - [PR #14450](https://github.com/BerriAI/litellm/pull/14450)
- Improved execution context propagation into logging tasks - [PR #14455](https://github.com/BerriAI/litellm/pull/14455)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @Sameerlite made their first contribution in [PR #14460](https://github.com/BerriAI/litellm/pull/14460)
- @holzman made their first contribution in [PR #14459](https://github.com/BerriAI/litellm/pull/14459)
- @sashank5644 made their first contribution in [PR #14469](https://github.com/BerriAI/litellm/pull/14469)
- @TomAlon made their first contribution in [PR #14401](https://github.com/BerriAI/litellm/pull/14401)
- @AlexsanderHamir made their first contribution in [PR #14538](https://github.com/BerriAI/litellm/pull/14538)

* * *

## [**Full Changelog**](https://github.com/BerriAI/litellm/compare/v1.77.1.dev.2...v1.77.2.dev)[​](#full-changelog "Direct link to full-changelog")