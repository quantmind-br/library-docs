---
title: v1.65.4-stable
url: https://docs.litellm.ai/release_notes/v1.65.4-stable
source: sitemap
fetched_at: 2026-01-21T19:43:31.324120868-03:00
rendered_js: false
word_count: 844
summary: This document outlines the v1.65.4-stable release updates for LiteLLM, focusing on database deadlock fixes, enhanced usage tracking features, and expanded model compatibility.
tags:
    - release-notes
    - litellm
    - changelog
    - database-optimization
    - spend-tracking
    - llm-support
category: other
---

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.65.4-stable
```

v1.65.4-stable is live. Here are the improvements since v1.65.0-stable.

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Preventing DB Deadlocks**: Fixes a high-traffic issue when multiple instances were writing to the DB at the same time.
- **New Usage Tab**: Enables viewing spend by model and customizing date range

Let's dive in.

### Preventing DB Deadlocks[​](#preventing-db-deadlocks "Direct link to Preventing DB Deadlocks")

This release fixes the DB deadlocking issue that users faced in high traffic (10K+ RPS). This is great because it enables user/key/team spend tracking works at that scale.

Read more about the new architecture [here](https://docs.litellm.ai/docs/proxy/db_deadlocks)

### New Usage Tab[​](#new-usage-tab "Direct link to New Usage Tab")

The new Usage tab now brings the ability to track daily spend by model. This makes it easier to catch any spend tracking or token counting errors, when combined with the ability to view successful requests, and token usage.

To test this out, just go to Experimental &gt; New Usage &gt; Activity.

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

1. Databricks - claude-3-7-sonnet cost tracking [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L10350)
2. VertexAI - `gemini-2.5-pro-exp-03-25` cost tracking [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L4492)
3. VertexAI - `gemini-2.0-flash` cost tracking [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L4689)
4. Groq - add whisper ASR models to model cost map [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L3324)
5. IBM - Add watsonx/ibm/granite-3-8b-instruct to model cost map [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L91)
6. Google AI Studio - add gemini/gemini-2.5-pro-preview-03-25 to model cost map [PR](https://github.com/BerriAI/litellm/blob/52b35cd8093b9ad833987b24f494586a1e923209/model_prices_and_context_window.json#L4850)

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

01. Vertex AI - Support anyOf param for OpenAI json schema translation [Get Started](https://docs.litellm.ai/docs/providers/vertex#json-schema)
02. Anthropic- response\_format + thinking param support (works across Anthropic API, Bedrock, Vertex) [Get Started](https://docs.litellm.ai/docs/reasoning_content)
03. Anthropic - if thinking token is specified and max tokens is not - ensure max token to anthropic is higher than thinking tokens (works across Anthropic API, Bedrock, Vertex) [PR](https://github.com/BerriAI/litellm/pull/9594)
04. Bedrock - latency optimized inference support [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---latency-optimized-inference)
05. Sagemaker - handle special tokens + multibyte character code in response [Get Started](https://docs.litellm.ai/docs/providers/aws_sagemaker)
06. MCP - add support for using SSE MCP servers [Get Started](https://docs.litellm.ai/docs/mcp#usage)
07. Anthropic - new `litellm.messages.create` interface for calling Anthropic `/v1/messages` via passthrough [Get Started](https://docs.litellm.ai/docs/anthropic_unified#usage)
08. Anthropic - support ‘file’ content type in message param (works across Anthropic API, Bedrock, Vertex) [Get Started](https://docs.litellm.ai/docs/providers/anthropic#usage---pdf)
09. Anthropic - map openai 'reasoning\_effort' to anthropic 'thinking' param (works across Anthropic API, Bedrock, Vertex) [Get Started](https://docs.litellm.ai/docs/providers/anthropic#usage---thinking--reasoning_content)
10. Google AI Studio (Gemini) - \[BETA] `/v1/files` upload support [Get Started](https://docs.litellm.ai/docs/providers/google_ai_studio/files)
11. Azure - fix o-series tool calling [Get Started](https://docs.litellm.ai/docs/providers/azure#tool-calling--function-calling)
12. Unified file id - \[ALPHA] allow calling multiple providers with same file id [PR](https://github.com/BerriAI/litellm/pull/9718)
    
    - This is experimental, and not recommended for production use.
    - We plan to have a production-ready implementation by next week.
13. Google AI Studio (Gemini) - return logprobs [PR](https://github.com/BerriAI/litellm/pull/9713)
14. Anthropic - Support prompt caching for Anthropic tool calls [Get Started](https://docs.litellm.ai/docs/completion/prompt_caching)
15. OpenRouter - unwrap extra body on open router calls [PR](https://github.com/BerriAI/litellm/pull/9747)
16. VertexAI - fix credential caching issue [PR](https://github.com/BerriAI/litellm/pull/9756)
17. XAI - filter out 'name' param for XAI [PR](https://github.com/BerriAI/litellm/pull/9761)
18. Gemini - image generation output support [Get Started](https://docs.litellm.ai/docs/providers/gemini#image-generation)
19. Databricks - support claude-3-7-sonnet w/ thinking + response\_format [Get Started](https://docs.litellm.ai/docs/providers/databricks#usage---thinking--reasoning_content)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Reliability fix - Check sent and received model for cost calculation [PR](https://github.com/BerriAI/litellm/pull/9669)
2. Vertex AI - Multimodal embedding cost tracking [Get Started](https://docs.litellm.ai/docs/providers/vertex#multi-modal-embeddings), [PR](https://github.com/BerriAI/litellm/pull/9623)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

1. New Usage Tab
   
   - Report 'total\_tokens' + report success/failure calls
   - Remove double bars on scroll
   - Ensure ‘daily spend’ chart ordered from earliest to latest date
   - showing spend per model per day
   - show key alias on usage tab
   - Allow non-admins to view their activity
   - Add date picker to new usage tab
2. Virtual Keys Tab
   
   - remove 'default key' on user signup
   - fix showing user models available for personal key creation
3. Test Key Tab
   
   - Allow testing image generation models
4. Models Tab
   
   - Fix bulk adding models
   - support reusable credentials for passthrough endpoints
   - Allow team members to see team models
5. Teams Tab
   
   - Fix json serialization error on update team metadata
6. Request Logs Tab
   
   - Add reasoning\_content token tracking across all providers on streaming
7. API
   
   - return key alias on /user/daily/activity [Get Started](https://docs.litellm.ai/docs/proxy/cost_tracking#daily-spend-breakdown-api)
8. SSO
   
   - Allow assigning SSO users to teams on MSFT SSO [PR](https://github.com/BerriAI/litellm/pull/9745)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Console Logs - Add json formatting for uncaught exceptions [PR](https://github.com/BerriAI/litellm/pull/9619)
2. Guardrails - AIM Guardrails support for virtual key based policies [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/aim_security)
3. Logging - fix completion start time tracking [PR](https://github.com/BerriAI/litellm/pull/9688)
4. Prometheus
   
   - Allow adding authentication on Prometheus /metrics endpoints [PR](https://github.com/BerriAI/litellm/pull/9766)
   - Distinguish LLM Provider Exception vs. LiteLLM Exception in metric naming [PR](https://github.com/BerriAI/litellm/pull/9760)
   - Emit operational metrics for new DB Transaction architecture [PR](https://github.com/BerriAI/litellm/pull/9719)

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

1. Preventing Deadlocks
   
   - Reduce DB Deadlocks by storing spend updates in Redis and then committing to DB [PR](https://github.com/BerriAI/litellm/pull/9608)
   - Ensure no deadlocks occur when updating DailyUserSpendTransaction [PR](https://github.com/BerriAI/litellm/pull/9690)
   - High Traffic fix - ensure new DB + Redis architecture accurately tracks spend [PR](https://github.com/BerriAI/litellm/pull/9673)
   - Use Redis for PodLock Manager instead of PG (ensures no deadlocks occur) [PR](https://github.com/BerriAI/litellm/pull/9715)
   - v2 DB Deadlock Reduction Architecture – Add Max Size for In-Memory Queue + Backpressure Mechanism [PR](https://github.com/BerriAI/litellm/pull/9759)
2. Prisma Migrations [Get Started](https://docs.litellm.ai/docs/proxy/prod#9-use-prisma-migrate-deploy)
   
   - connects litellm proxy to litellm's prisma migration files
   - Handle db schema updates from new `litellm-proxy-extras` sdk
3. Redis - support password for sync sentinel clients [PR](https://github.com/BerriAI/litellm/pull/9622)
4. Fix "Circular reference detected" error when max\_parallel\_requests = 0 [PR](https://github.com/BerriAI/litellm/pull/9671)
5. Code QA - Ban hardcoded numbers [PR](https://github.com/BerriAI/litellm/pull/9709)

## Helm[​](#helm "Direct link to Helm")

1. fix: wrong indentation of ttlSecondsAfterFinished in chart [PR](https://github.com/BerriAI/litellm/pull/9611)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Fix - only apply service\_account\_settings.enforced\_params on service accounts [PR](https://github.com/BerriAI/litellm/pull/9683)
2. Fix - handle metadata null on `/chat/completion` [PR](https://github.com/BerriAI/litellm/issues/9717)
3. Fix - Move daily user transaction logging outside of 'disable\_spend\_logs' flag, as they’re unrelated [PR](https://github.com/BerriAI/litellm/pull/9772)

## Demo[​](#demo "Direct link to Demo")

Try this on the demo instance [today](https://docs.litellm.ai/docs/proxy/demo)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

See the complete git diff since v1.65.0-stable, [here](https://github.com/BerriAI/litellm/releases/tag/v1.65.4-stable)