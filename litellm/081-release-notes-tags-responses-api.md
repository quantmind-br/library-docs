---
title: 3 posts tagged with "responses_api" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/responses-api
source: sitemap
fetched_at: 2026-01-21T19:42:00.203515855-03:00
rendered_js: false
word_count: 2059
summary: This document details the release notes for LiteLLM version 1.67.4-stable, featuring improvements in user management, Responses API load balancing, and UI session logging.
tags:
    - litellm
    - release-notes
    - load-balancing
    - user-management
    - session-logs
    - model-tracking
category: reference
---

## Deploy this version[​](#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.67.4-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **Improved User Management**: This release enables search and filtering across users, keys, teams, and models.
- **Responses API Load Balancing**: Route requests across provider regions and ensure session continuity.
- **UI Session Logs**: Group several requests to LiteLLM into a session.

## Improved User Management[​](#improved-user-management "Direct link to Improved User Management")

This release makes it easier to manage users and keys on LiteLLM. You can now search and filter across users, keys, teams, and models, and control user settings more easily.

New features include:

- Search for users by email, ID, role, or team.
- See all of a user's models, teams, and keys in one place.
- Change user roles and model access right from the Users Tab.

These changes help you spend less time on user setup and management on LiteLLM.

## Responses API Load Balancing[​](#responses-api-load-balancing "Direct link to Responses API Load Balancing")

This release introduces load balancing for the Responses API, allowing you to route requests across provider regions and ensure session continuity. It works as follows:

- If a `previous_response_id` is provided, LiteLLM will route the request to the original deployment that generated the prior response — ensuring session continuity.
- If no `previous_response_id` is provided, LiteLLM will load-balance requests across your available deployments.

[Read more](https://docs.litellm.ai/docs/response_api#load-balancing-with-session-continuity)

## UI Session Logs[​](#ui-session-logs "Direct link to UI Session Logs")

This release allow you to group requests to LiteLLM proxy into a session. If you specify a litellm\_session\_id in your request LiteLLM will automatically group all logs in the same session. This allows you to easily track usage and request content per session.

[Read more](https://docs.litellm.ai/docs/proxy/ui_logs_sessions)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **OpenAI**
  
  1. Added `gpt-image-1` cost tracking [Get Started](https://docs.litellm.ai/docs/image_generation)
  2. Bug fix: added cost tracking for gpt-image-1 when quality is unspecified [PR](https://github.com/BerriAI/litellm/pull/10247)
- **Azure**
  
  1. Fixed timestamp granularities passing to whisper in Azure [Get Started](https://docs.litellm.ai/docs/audio_transcription)
  2. Added azure/gpt-image-1 pricing [Get Started](https://docs.litellm.ai/docs/image_generation), [PR](https://github.com/BerriAI/litellm/pull/10327)
  3. Added cost tracking for `azure/computer-use-preview`, `azure/gpt-4o-audio-preview-2024-12-17`, `azure/gpt-4o-mini-audio-preview-2024-12-17` [PR](https://github.com/BerriAI/litellm/pull/10178)
- **Bedrock**
  
  1. Added support for all compatible Bedrock parameters when model="arn:.." (Bedrock application inference profile models) [Get started](https://docs.litellm.ai/docs/providers/bedrock#bedrock-application-inference-profile), [PR](https://github.com/BerriAI/litellm/pull/10256)
  2. Fixed wrong system prompt transformation [PR](https://github.com/BerriAI/litellm/pull/10120)
- **VertexAI / Google AI Studio**
  
  1. Allow setting `budget_tokens=0` for `gemini-2.5-flash` [Get Started](https://docs.litellm.ai/docs/providers/gemini#usage---thinking--reasoning_content),[PR](https://github.com/BerriAI/litellm/pull/10198)
  2. Ensure returned `usage` includes thinking token usage [PR](https://github.com/BerriAI/litellm/pull/10198)
  3. Added cost tracking for `gemini-2.5-pro-preview-03-25` [PR](https://github.com/BerriAI/litellm/pull/10178)
- **Cohere**
  
  1. Added support for cohere command-a-03-2025 [Get Started](https://docs.litellm.ai/docs/providers/cohere), [PR](https://github.com/BerriAI/litellm/pull/10295)
- **SageMaker**
  
  1. Added support for max\_completion\_tokens parameter [Get Started](https://docs.litellm.ai/docs/providers/sagemaker), [PR](https://github.com/BerriAI/litellm/pull/10300)
- **Responses API**
  
  1. Added support for GET and DELETE operations - `/v1/responses/{response_id}` [Get Started](https://docs.litellm.ai/docs/response_api)
  2. Added session management support for all supported models [PR](https://github.com/BerriAI/litellm/pull/10321)
  3. Added routing affinity to maintain model consistency within sessions [Get Started](https://docs.litellm.ai/docs/response_api#load-balancing-with-routing-affinity), [PR](https://github.com/BerriAI/litellm/pull/10193)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- **Bug Fix**: Fixed spend tracking bug, ensuring default litellm params aren't modified in memory [PR](https://github.com/BerriAI/litellm/pull/10167)
- **Deprecation Dates**: Added deprecation dates for Azure, VertexAI models [PR](https://github.com/BerriAI/litellm/pull/10308)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Users[​](#users "Direct link to Users")

- **Filtering and Searching**:
  
  - Filter users by user\_id, role, team, sso\_id
  - Search users by email
- **User Info Panel**: Added a new user information pane [PR](https://github.com/BerriAI/litellm/pull/10213)
  
  - View teams, keys, models associated with User
  - Edit user role, model permissions

#### Teams[​](#teams "Direct link to Teams")

- **Filtering and Searching**:
  
  - Filter teams by Organization, Team ID [PR](https://github.com/BerriAI/litellm/pull/10324)
  - Search teams by Team Name [PR](https://github.com/BerriAI/litellm/pull/10324)

#### Keys[​](#keys "Direct link to Keys")

- **Key Management**:
  
  - Support for cross-filtering and filtering by key hash [PR](https://github.com/BerriAI/litellm/pull/10322)
  - Fixed key alias reset when resetting filters [PR](https://github.com/BerriAI/litellm/pull/10099)
  - Fixed table rendering on key creation [PR](https://github.com/BerriAI/litellm/pull/10224)

#### UI Logs Page[​](#ui-logs-page "Direct link to UI Logs Page")

- **Session Logs**: Added UI Session Logs [Get Started](https://docs.litellm.ai/docs/proxy/ui_logs_sessions)

#### UI Authentication & Security[​](#ui-authentication--security "Direct link to UI Authentication & Security")

- **Required Authentication**: Authentication now required for all dashboard pages [PR](https://github.com/BerriAI/litellm/pull/10229)
- **SSO Fixes**: Fixed SSO user login invalid token error [PR](https://github.com/BerriAI/litellm/pull/10298)
- \[BETA] **Encrypted Tokens**: Moved UI to encrypted token usage [PR](https://github.com/BerriAI/litellm/pull/10302)
- **Token Expiry**: Support token refresh by re-routing to login page (fixes issue where expired token would show a blank page) [PR](https://github.com/BerriAI/litellm/pull/10250)

#### UI General fixes[​](#ui-general-fixes "Direct link to UI General fixes")

- **Fixed UI Flicker**: Addressed UI flickering issues in Dashboard [PR](https://github.com/BerriAI/litellm/pull/10261)
- **Improved Terminology**: Better loading and no-data states on Keys and Tools pages [PR](https://github.com/BerriAI/litellm/pull/10253)
- **Azure Model Support**: Fixed editing Azure public model names and changing model names after creation [PR](https://github.com/BerriAI/litellm/pull/10249)
- **Team Model Selector**: Bug fix for team model selection [PR](https://github.com/BerriAI/litellm/pull/10171)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- **Datadog**:
  
  1. Fixed Datadog LLM observability logging [Get Started](https://docs.litellm.ai/docs/proxy/logging#datadog), [PR](https://github.com/BerriAI/litellm/pull/10206)
- **Prometheus / Grafana**:
  
  1. Enable datasource selection on LiteLLM Grafana Template [Get Started](https://docs.litellm.ai/docs/proxy/prometheus#-litellm-maintained-grafana-dashboards-), [PR](https://github.com/BerriAI/litellm/pull/10257)
- **AgentOps**:
  
  1. Added AgentOps Integration [Get Started](https://docs.litellm.ai/docs/observability/agentops_integration), [PR](https://github.com/BerriAI/litellm/pull/9685)
- **Arize**:
  
  1. Added missing attributes for Arize & Phoenix Integration [Get Started](https://docs.litellm.ai/docs/observability/arize_integration), [PR](https://github.com/BerriAI/litellm/pull/10215)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Caching**: Fixed caching to account for `thinking` or `reasoning_effort` when calculating cache key [PR](https://github.com/BerriAI/litellm/pull/10140)
- **Model Groups**: Fixed handling for cases where user sets model\_group inside model\_info [PR](https://github.com/BerriAI/litellm/pull/10191)
- **Passthrough Endpoints**: Ensured `PassthroughStandardLoggingPayload` is logged with method, URL, request/response body [PR](https://github.com/BerriAI/litellm/pull/10194)
- **Fix SQL Injection**: Fixed potential SQL injection vulnerability in spend\_management\_endpoints.py [PR](https://github.com/BerriAI/litellm/pull/9878)

## Helm[​](#helm "Direct link to Helm")

- Fixed serviceAccountName on migration job [PR](https://github.com/BerriAI/litellm/pull/10258)

## Full Changelog[​](#full-changelog "Direct link to Full Changelog")

The complete list of changes can be found in the [GitHub release notes](https://github.com/BerriAI/litellm/compare/v1.67.0-stable...v1.67.4-stable).

These are the changes since `v1.63.11-stable`.

This release brings:

- LLM Translation Improvements (MCP Support and Bedrock Application Profiles)
- Perf improvements for Usage-based Routing
- Streaming guardrail support via websockets
- Azure OpenAI client perf fix (from previous release)

## Docker Run LiteLLM Proxy[​](#docker-run-litellm-proxy "Direct link to Docker Run LiteLLM Proxy")

```
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
docker.litellm.ai/berriai/litellm:main-v1.63.14-stable.patch1
```

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- Azure gpt-4o - fixed pricing to latest global pricing - [PR](https://github.com/BerriAI/litellm/pull/9361)
- O1-Pro - add pricing + model information - [PR](https://github.com/BerriAI/litellm/pull/9397)
- Azure AI - mistral 3.1 small pricing added - [PR](https://github.com/BerriAI/litellm/pull/9453)
- Azure - gpt-4.5-preview pricing added - [PR](https://github.com/BerriAI/litellm/pull/9453)

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

1. **New LLM Features**

<!--THE END-->

- Bedrock: Support bedrock application inference profiles [Docs](https://docs.litellm.ai/docs/providers/bedrock#bedrock-application-inference-profile)
  
  - Infer aws region from bedrock application profile id - (`arn:aws:bedrock:us-east-1:...`)
- Ollama - support calling via `/v1/completions` [Get Started](https://docs.litellm.ai/docs/providers/ollama#using-ollama-fim-on-v1completions)
- Bedrock - support `us.deepseek.r1-v1:0` model name [Docs](https://docs.litellm.ai/docs/providers/bedrock#supported-aws-bedrock-models)
- OpenRouter - `OPENROUTER_API_BASE` env var support [Docs](https://docs.litellm.ai/docs/providers/openrouter.md)
- Azure - add audio model parameter support - [Docs](https://docs.litellm.ai/docs/providers/azure#azure-audio-model)
- OpenAI - PDF File support [Docs](https://docs.litellm.ai/docs/completion/document_understanding#openai-file-message-type)
- OpenAI - o1-pro Responses API streaming support [Docs](https://docs.litellm.ai/docs/response_api.md#streaming)
- \[BETA] MCP - Use MCP Tools with LiteLLM SDK [Docs](https://docs.litellm.ai/docs/mcp)

<!--THE END-->

2. **Bug Fixes**

<!--THE END-->

- Voyage: prompt token on embedding tracking fix - [PR](https://github.com/BerriAI/litellm/commit/56d3e75b330c3c3862dc6e1c51c1210e48f1068e)
- Sagemaker - Fix ‘Too little data for declared Content-Length’ error - [PR](https://github.com/BerriAI/litellm/pull/9326)
- OpenAI-compatible models - fix issue when calling openai-compatible models w/ custom\_llm\_provider set - [PR](https://github.com/BerriAI/litellm/pull/9355)
- VertexAI - Embedding ‘outputDimensionality’ support - [PR](https://github.com/BerriAI/litellm/commit/437dbe724620675295f298164a076cbd8019d304)
- Anthropic - return consistent json response format on streaming/non-streaming - [PR](https://github.com/BerriAI/litellm/pull/9437)

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- `litellm_proxy/` - support reading litellm response cost header from proxy, when using client sdk
- Reset Budget Job - fix budget reset error on keys/teams/users [PR](https://github.com/BerriAI/litellm/pull/9329)
- Streaming - Prevents final chunk w/ usage from being ignored (impacted bedrock streaming + cost tracking) [PR](https://github.com/BerriAI/litellm/pull/9314)

## UI[​](#ui "Direct link to UI")

1. Users Page
   
   - Feature: Control default internal user settings [PR](https://github.com/BerriAI/litellm/pull/9328)
2. Icons:
   
   - Feature: Replace external "artificialanalysis.ai" icons by local svg [PR](https://github.com/BerriAI/litellm/pull/9374)
3. Sign In/Sign Out
   
   - Fix: Default login when `default_user_id` user does not exist in DB [PR](https://github.com/BerriAI/litellm/pull/9395)

## Logging Integrations[​](#logging-integrations "Direct link to Logging Integrations")

- Support post-call guardrails for streaming responses [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#1-write-a-customguardrail-class)
- Arize [Get Started](https://docs.litellm.ai/docs/observability/arize_integration)
  
  - fix invalid package import [PR](https://github.com/BerriAI/litellm/pull/9338)
  - migrate to using standardloggingpayload for metadata, ensures spans land successfully [PR](https://github.com/BerriAI/litellm/pull/9338)
  - fix logging to just log the LLM I/O [PR](https://github.com/BerriAI/litellm/pull/9353)
  - Dynamic API Key/Space param support [Get Started](https://docs.litellm.ai/docs/observability/arize_integration#pass-arize-spacekey-per-request)
- StandardLoggingPayload - Log litellm\_model\_name in payload. Allows knowing what the model sent to API provider was [Get Started](https://docs.litellm.ai/docs/proxy/logging_spec#standardlogginghiddenparams)
- Prompt Management - Allow building custom prompt management integration [Get Started](https://docs.litellm.ai/docs/proxy/custom_prompt_management.md)

## Performance / Reliability improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability improvements")

- Redis Caching - add 5s default timeout, prevents hanging redis connection from impacting llm calls [PR](https://github.com/BerriAI/litellm/commit/db92956ae33ed4c4e3233d7e1b0c7229817159bf)
- Allow disabling all spend updates / writes to DB - patch to allow disabling all spend updates to DB with a flag [PR](https://github.com/BerriAI/litellm/pull/9331)
- Azure OpenAI - correctly re-use azure openai client, fixes perf issue from previous Stable release [PR](https://github.com/BerriAI/litellm/commit/f2026ef907c06d94440930917add71314b901413)
- Azure OpenAI - uses litellm.ssl\_verify on Azure/OpenAI clients [PR](https://github.com/BerriAI/litellm/commit/f2026ef907c06d94440930917add71314b901413)
- Usage-based routing - Wildcard model support [Get Started](https://docs.litellm.ai/docs/proxy/usage_based_routing#wildcard-model-support)
- Usage-based routing - Support batch writing increments to redis - reduces latency to same as ‘simple-shuffle’ [PR](https://github.com/BerriAI/litellm/pull/9357)
- Router - show reason for model cooldown on ‘no healthy deployments available error’ [PR](https://github.com/BerriAI/litellm/pull/9438)
- Caching - add max value limit to an item in in-memory cache (1MB) - prevents OOM errors on large image url’s being sent through proxy [PR](https://github.com/BerriAI/litellm/pull/9448)

## General Improvements[​](#general-improvements "Direct link to General Improvements")

- Passthrough Endpoints - support returning api-base on pass-through endpoints Response Headers [Docs](https://docs.litellm.ai/docs/proxy/response_headers#litellm-specific-headers)
- SSL - support reading ssl security level from env var - Allows user to specify lower security settings [Get Started](https://docs.litellm.ai/docs/guides/security_settings)
- Credentials - only poll Credentials table when `STORE_MODEL_IN_DB` is True [PR](https://github.com/BerriAI/litellm/pull/9376)
- Image URL Handling - new architecture doc on image url handling [Docs](https://docs.litellm.ai/docs/proxy/image_handling)
- OpenAI - bump to pip install "openai==1.68.2" [PR](https://github.com/BerriAI/litellm/commit/e85e3bc52a9de86ad85c3dbb12d87664ee567a5a)
- Gunicorn - security fix - bump gunicorn==23.0.0 [PR](https://github.com/BerriAI/litellm/commit/7e9fc92f5c7fea1e7294171cd3859d55384166eb)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.63.11-stable...v1.63.14.rc)

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