---
title: v1.63.11-stable
url: https://docs.litellm.ai/release_notes/v1.63.11-stable
source: sitemap
fetched_at: 2026-01-21T19:43:23.738714413-03:00
rendered_js: false
word_count: 706
summary: This document details the release notes for LiteLLM version 1.63.11-stable, highlighting new support for Snowflake Cortex and Amazon Nova, the introduction of a Responses API, and significant UI and security enhancements. It provides a comprehensive list of bug fixes, model pricing updates, and improvements to credential management and spend tracking.
tags:
    - litellm-release
    - responses-api
    - snowflake-cortex
    - amazon-nova
    - credential-management
    - security-updates
    - spend-tracking
category: other
---

These are the changes since `v1.63.2-stable`.

This release is primarily focused on:

- \[Beta] Responses API Support
- Snowflake Cortex Support, Amazon Nova Image Generation
- UI - Credential Management, re-use credentials when adding new models
- UI - Test Connection to LLM Provider before adding a model

## Known Issues[​](#known-issues "Direct link to Known Issues")

- 🚨 Known issue on Azure OpenAI - We don't recommend upgrading if you use Azure OpenAI. This version failed our Azure OpenAI load test

## Docker Run LiteLLM Proxy[​](#docker-run-litellm-proxy "Direct link to Docker Run LiteLLM Proxy")

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.63.11-stable
```

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- Image Generation support for Amazon Nova Canvas [Getting Started](https://docs.litellm.ai/docs/providers/bedrock#image-generation)
- Add pricing for Jamba new models [PR](https://github.com/BerriAI/litellm/pull/9032/files)
- Add pricing for Amazon EU models [PR](https://github.com/BerriAI/litellm/pull/9056/files)
- Add Bedrock Deepseek R1 model pricing [PR](https://github.com/BerriAI/litellm/pull/9108/files)
- Update Gemini pricing: Gemma 3, Flash 2 thinking update, LearnLM [PR](https://github.com/BerriAI/litellm/pull/9190/files)
- Mark Cohere Embedding 3 models as Multimodal [PR](https://github.com/BerriAI/litellm/pull/9176/commits/c9a576ce4221fc6e50dc47cdf64ab62736c9da41)
- Add Azure Data Zone pricing [PR](https://github.com/BerriAI/litellm/pull/9185/files#diff-19ad91c53996e178c1921cbacadf6f3bae20cfe062bd03ee6bfffb72f847ee37)
  
  - LiteLLM Tracks cost for `azure/eu` and `azure/us` models

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

1. **New Endpoints**

<!--THE END-->

- \[Beta] POST `/responses` API. [Getting Started](https://docs.litellm.ai/docs/response_api)

<!--THE END-->

2. **New LLM Providers**

<!--THE END-->

- Snowflake Cortex [Getting Started](https://docs.litellm.ai/docs/providers/snowflake)

<!--THE END-->

3. **New LLM Features**

<!--THE END-->

- Support OpenRouter `reasoning_content` on streaming [Getting Started](https://docs.litellm.ai/docs/reasoning_content)

<!--THE END-->

4. **Bug Fixes**

<!--THE END-->

- OpenAI: Return `code`, `param` and `type` on bad request error [More information on litellm exceptions](https://docs.litellm.ai/docs/exception_mapping)
- Bedrock: Fix converse chunk parsing to only return empty dict on tool use [PR](https://github.com/BerriAI/litellm/pull/9166)
- Bedrock: Support extra\_headers [PR](https://github.com/BerriAI/litellm/pull/9113)
- Azure: Fix Function Calling Bug & Update Default API Version to `2025-02-01-preview` [PR](https://github.com/BerriAI/litellm/pull/9191)
- Azure: Fix AI services URL [PR](https://github.com/BerriAI/litellm/pull/9185)
- Vertex AI: Handle HTTP 201 status code in response [PR](https://github.com/BerriAI/litellm/pull/9193)
- Perplexity: Fix incorrect streaming response [PR](https://github.com/BerriAI/litellm/pull/9081)
- Triton: Fix streaming completions bug [PR](https://github.com/BerriAI/litellm/pull/8386)
- Deepgram: Support bytes.IO when handling audio files for transcription [PR](https://github.com/BerriAI/litellm/pull/9071)
- Ollama: Fix "system" role has become unacceptable [PR](https://github.com/BerriAI/litellm/pull/9261)
- All Providers (Streaming): Fix String `data:` stripped from entire content in streamed responses [PR](https://github.com/BerriAI/litellm/pull/9070)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Support Bedrock converse cache token tracking [Getting Started](https://docs.litellm.ai/docs/completion/prompt_caching)
2. Cost Tracking for Responses API [Getting Started](https://docs.litellm.ai/docs/response_api)
3. Fix Azure Whisper cost tracking [Getting Started](https://docs.litellm.ai/docs/audio_transcription)

## UI[​](#ui "Direct link to UI")

### Re-Use Credentials on UI[​](#re-use-credentials-on-ui "Direct link to Re-Use Credentials on UI")

You can now onboard LLM provider credentials on LiteLLM UI. Once these credentials are added you can re-use them when adding new models [Getting Started](https://docs.litellm.ai/docs/proxy/ui_credentials)

### Test Connections before adding models[​](#test-connections-before-adding-models "Direct link to Test Connections before adding models")

Before adding a model you can test the connection to the LLM provider to verify you have setup your API Base + API Key correctly

![](https://docs.litellm.ai/assets/images/litellm_test_connection-029765a2de4dcabccfe3be9a8d33dbdd.gif)

### General UI Improvements[​](#general-ui-improvements "Direct link to General UI Improvements")

1. Add Models Page
   
   - Allow adding Cerebras, Sambanova, Perplexity, Fireworks, Openrouter, TogetherAI Models, Text-Completion OpenAI on Admin UI
   - Allow adding EU OpenAI models
   - Fix: Instantly show edit + deletes to models
2. Keys Page
   
   - Fix: Instantly show newly created keys on Admin UI (don't require refresh)
   - Fix: Allow clicking into Top Keys when showing users Top API Key
   - Fix: Allow Filter Keys by Team Alias, Key Alias and Org
   - UI Improvements: Show 100 Keys Per Page, Use full height, increase width of key alias
3. Users Page
   
   - Fix: Show correct count of internal user keys on Users Page
   - Fix: Metadata not updating in Team UI
4. Logs Page
   
   - UI Improvements: Keep expanded log in focus on LiteLLM UI
   - UI Improvements: Minor improvements to logs page
   - Fix: Allow internal user to query their own logs
   - Allow switching off storing Error Logs in DB [Getting Started](https://docs.litellm.ai/docs/proxy/ui_logs)
5. Sign In/Sign Out
   
   - Fix: Correctly use `PROXY_LOGOUT_URL` when set [Getting Started](https://docs.litellm.ai/docs/proxy/self_serve#setting-custom-logout-urls)

## Security[​](#security "Direct link to Security")

1. Support for Rotating Master Keys [Getting Started](https://docs.litellm.ai/docs/proxy/master_key_rotations)
2. Fix: Internal User Viewer Permissions, don't allow `internal_user_viewer` role to see `Test Key Page` or `Create Key Button` [More information on role based access controls](https://docs.litellm.ai/docs/proxy/access_control)
3. Emit audit logs on All user + model Create/Update/Delete endpoints [Getting Started](https://docs.litellm.ai/docs/proxy/multiple_admins)
4. JWT
   
   - Support multiple JWT OIDC providers [Getting Started](https://docs.litellm.ai/docs/proxy/token_auth)
   - Fix JWT access with Groups not working when team is assigned All Proxy Models access
5. Using K/V pairs in 1 AWS Secret [Getting Started](https://docs.litellm.ai/docs/secret#using-kv-pairs-in-1-aws-secret)

## Logging Integrations[​](#logging-integrations "Direct link to Logging Integrations")

1. Prometheus: Track Azure LLM API latency metric [Getting Started](https://docs.litellm.ai/docs/proxy/prometheus#request-latency-metrics)
2. Athina: Added tags, user\_feedback and model\_options to additional\_keys which can be sent to Athina [Getting Started](https://docs.litellm.ai/docs/observability/athina_integration)

## Performance / Reliability improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability improvements")

1. Redis + litellm router - Fix Redis cluster mode for litellm router [PR](https://github.com/BerriAI/litellm/pull/9010)

## General Improvements[​](#general-improvements "Direct link to General Improvements")

1. OpenWebUI Integration - display `thinking` tokens

<!--THE END-->

- Guide on getting started with LiteLLM x OpenWebUI. [Getting Started](https://docs.litellm.ai/docs/tutorials/openweb_ui)
- Display `thinking` tokens on OpenWebUI (Bedrock, Anthropic, Deepseek) [Getting Started](https://docs.litellm.ai/docs/tutorials/openweb_ui#render-thinking-content-on-openweb-ui)

![](https://docs.litellm.ai/assets/images/litellm_thinking_openweb-5ec7dddb7e7b6a10252694c27cfc177d.gif)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.63.2-stable...v1.63.11-stable)