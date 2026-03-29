---
title: v1.72.6-stable - MCP Gateway Permission Management
url: https://docs.litellm.ai/release_notes/v1-72-6-stable
source: sitemap
fetched_at: 2026-01-21T19:42:26.299972941-03:00
rendered_js: false
word_count: 995
summary: Detailed release notes for LiteLLM version 1.72.6 outlining new features like MCP permissions management, Codex-mini support on Claude Code, and various model and pricing updates.
tags:
    - litellm
    - release-notes
    - mcp-server
    - model-updates
    - api-integration
    - llm-proxy
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
docker.litellm.ai/berriai/litellm:main-v1.72.6-stable
```

## TLDR[​](#tldr "Direct link to TLDR")

- **Why Upgrade**
  
  - Codex-mini on Claude Code: You can now use `codex-mini` (OpenAI’s code assistant model) via Claude Code.
  - MCP Permissions Management: Manage permissions for MCP Servers by Keys, Teams, Organizations (entities) on LiteLLM.
  - UI: Turn on/off auto refresh on logs view.
  - Rate Limiting: Support for output token-only rate limiting.
- **Who Should Read**
  
  - Teams using `/v1/messages` API (Claude Code)
  - Teams using **MCP**
  - Teams giving access to self-hosted models and setting rate limits
- **Risk of Upgrade**
  
  - **Low**
    
    - No major changes to existing functionality or package updates.

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

### MCP Permissions Management[​](#mcp-permissions-management "Direct link to MCP Permissions Management")

This release brings support for managing permissions for MCP Servers by Keys, Teams, Organizations (entities) on LiteLLM. When a MCP client attempts to list tools, LiteLLM will only return the tools the entity has permissions to access.

This is great for use cases that require access to restricted data (e.g Jira MCP) that you don't want everyone to use.

For Proxy Admins, this enables centralized management of all MCP Servers with access control. For developers, this means you'll only see the MCP tools assigned to you.

### Codex-mini on Claude Code[​](#codex-mini-on-claude-code "Direct link to Codex-mini on Claude Code")

This release brings support for calling `codex-mini` (OpenAI’s code assistant model) via Claude Code.

This is done by LiteLLM enabling any Responses API model (including `o3-pro`) to be called via `/chat/completions` and `/v1/messages` endpoints. This includes:

- Streaming calls
- Non-streaming calls
- Cost Tracking on success + failure for Responses API models

Here's how to use it [today](https://docs.litellm.ai/docs/tutorials/claude_responses_api)

* * *

## New / Updated Models[​](#new--updated-models "Direct link to New / Updated Models")

### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)TypeVertexAI`vertex_ai/claude-opus-4`200K$15.00$75.00NewOpenAI`gpt-4o-audio-preview-2025-06-03`128k$2.5 (text), $40 (audio)$10 (text), $80 (audio)NewOpenAI`o3-pro`200k2080NewOpenAI`o3-pro-2025-06-10`200k2080NewOpenAI`o3`200k28UpdatedOpenAI`o3-2025-04-16`200k28UpdatedAzure`azure/gpt-4o-mini-transcribe`16k1.25 (text), 3 (audio)5 (text)NewMistral`mistral/magistral-medium-latest`40k25NewMistral`mistral/magistral-small-latest`40k0.51.5New

- Deepgram: `nova-3` cost per second pricing is [now supported](https://github.com/BerriAI/litellm/pull/11634).

### Updated Models[​](#updated-models "Direct link to Updated Models")

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Watsonx**](https://docs.litellm.ai/docs/providers/watsonx)
  
  - Ignore space id on Watsonx deployments (throws json errors) - [PR](https://github.com/BerriAI/litellm/pull/11527)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Set tool call id for streaming calls - [PR](https://github.com/BerriAI/litellm/pull/11528)
- **Gemini ([VertexAI](https://docs.litellm.ai/docs/providers/vertex) + [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini))**
  
  - Fix tool call indexes - [PR](https://github.com/BerriAI/litellm/pull/11558)
  - Handle empty string for arguments in function calls - [PR](https://github.com/BerriAI/litellm/pull/11601)
  - Add audio/ogg mime type support when inferring from file url’s - [PR](https://github.com/BerriAI/litellm/pull/11635)
- [**Custom LLM**](https://docs.litellm.ai/docs/providers/custom_llm_server)
  
  - Fix passing api\_base, api\_key, litellm\_params\_dict to custom\_llm embedding methods - [PR](https://github.com/BerriAI/litellm/pull/11450) s/o [ElefHead](https://github.com/ElefHead)
- [**Huggingface**](https://docs.litellm.ai/docs/providers/huggingface)
  
  - Add /chat/completions to endpoint url when missing - [PR](https://github.com/BerriAI/litellm/pull/11630)
- [**Deepgram**](https://docs.litellm.ai/docs/providers/deepgram)
  
  - Support async httpx calls - [PR](https://github.com/BerriAI/litellm/pull/11641)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Append prefix (if set) to assistant content start - [PR](https://github.com/BerriAI/litellm/pull/11719)

#### Features[​](#features "Direct link to Features")

- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Support vertex credentials set via env var on passthrough - [PR](https://github.com/BerriAI/litellm/pull/11527)
  - Support for choosing ‘global’ region when model is only available there - [PR](https://github.com/BerriAI/litellm/pull/11566)
  - Anthropic passthrough cost calculation + token tracking - [PR](https://github.com/BerriAI/litellm/pull/11611)
  - Support ‘global’ vertex region on passthrough - [PR](https://github.com/BerriAI/litellm/pull/11661)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - ‘none’ tool choice param support - [PR](https://github.com/BerriAI/litellm/pull/11695), [Get Started](https://docs.litellm.ai/docs/providers/anthropic#disable-tool-calling)
- [**Perplexity**](https://docs.litellm.ai/docs/providers/perplexity)
  
  - Add ‘reasoning\_effort’ support - [PR](https://github.com/BerriAI/litellm/pull/11562), [Get Started](https://docs.litellm.ai/docs/providers/perplexity#reasoning-effort)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Add mistral reasoning support - [PR](https://github.com/BerriAI/litellm/pull/11642), [Get Started](https://docs.litellm.ai/docs/providers/mistral#reasoning)
- [**SGLang**](https://docs.litellm.ai/docs/providers/openai_compatible)
  
  - Map context window exceeded error for proper handling - [PR](https://github.com/BerriAI/litellm/pull/11575/)
- [**Deepgram**](https://docs.litellm.ai/docs/providers/deepgram)
  
  - Provider specific params support - [PR](https://github.com/BerriAI/litellm/pull/11638)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Return content safety filter results - [PR](https://github.com/BerriAI/litellm/pull/11655)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**Chat Completion**](https://docs.litellm.ai/docs/completion/input)
  
  - Streaming - Ensure consistent ‘created’ across chunks - [PR](https://github.com/BerriAI/litellm/pull/11528)

#### Features[​](#features-1 "Direct link to Features")

- **MCP**
  
  - Add controls for MCP Permission Management - [PR](https://github.com/BerriAI/litellm/pull/11598), [Docs](https://docs.litellm.ai/docs/mcp#-mcp-permission-management)
  - Add permission management for MCP List + Call Tool operations - [PR](https://github.com/BerriAI/litellm/pull/11682), [Docs](https://docs.litellm.ai/docs/mcp#-mcp-permission-management)
  - Streamable HTTP server support - [PR](https://github.com/BerriAI/litellm/pull/11628), [PR](https://github.com/BerriAI/litellm/pull/11645), [Docs](https://docs.litellm.ai/docs/mcp#using-your-mcp)
  - Use Experimental dedicated Rest endpoints for list, calling MCP tools - [PR](https://github.com/BerriAI/litellm/pull/11684)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - NEW API Endpoint - List input items - [PR](https://github.com/BerriAI/litellm/pull/11602)
  - Background mode for OpenAI + Azure OpenAI - [PR](https://github.com/BerriAI/litellm/pull/11640)
  - Langfuse/other Logging support on responses api requests - [PR](https://github.com/BerriAI/litellm/pull/11685)
- [**Chat Completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Bridge for Responses API - allows calling codex-mini via `/chat/completions` and `/v1/messages` - [PR](https://github.com/BerriAI/litellm/pull/11632), [PR](https://github.com/BerriAI/litellm/pull/11685)

* * *

## Spend Tracking[​](#spend-tracking "Direct link to Spend Tracking")

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- [**End Users**](https://docs.litellm.ai/docs/proxy/customers)
  
  - Update enduser spend and budget reset date based on budget duration - [PR](https://github.com/BerriAI/litellm/pull/8460) (s/o [laurien16](https://github.com/laurien16))
- [**Custom Pricing**](https://docs.litellm.ai/docs/proxy/custom_pricing)
  
  - Convert scientific notation str to int - [PR](https://github.com/BerriAI/litellm/pull/11655)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- [**Users**](https://docs.litellm.ai/docs/proxy/users)
  
  - `/user/info` - fix passing user with `+` in user id
  - Add admin-initiated password reset flow - [PR](https://github.com/BerriAI/litellm/pull/11618)
  - Fixes default user settings UI rendering error - [PR](https://github.com/BerriAI/litellm/pull/11674)
- [**Budgets**](https://docs.litellm.ai/docs/proxy/users)
  
  - Correct success message when new user budget is created - [PR](https://github.com/BerriAI/litellm/pull/11608)

#### Features[​](#features-2 "Direct link to Features")

- **Leftnav**
  
  - Show remaining Enterprise users on UI
- **MCP**
  
  - New server add form - [PR](https://github.com/BerriAI/litellm/pull/11604)
  - Allow editing mcp servers - [PR](https://github.com/BerriAI/litellm/pull/11693)
- **Models**
  
  - Add deepgram models on UI
  - Model Access Group support on UI - [PR](https://github.com/BerriAI/litellm/pull/11719)
- **Keys**
  
  - Trim long user id’s - [PR](https://github.com/BerriAI/litellm/pull/11488)
- **Logs**
  
  - Add live tail feature to logs view, allows user to disable auto refresh in high traffic - [PR](https://github.com/BerriAI/litellm/pull/11712)
  - Audit Logs - preview screenshot - [PR](https://github.com/BerriAI/litellm/pull/11715)

* * *

## Logging / Guardrails Integrations[​](#logging--guardrails-integrations "Direct link to Logging / Guardrails Integrations")

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- [**Arize**](https://docs.litellm.ai/docs/observability/arize_integration)
  
  - Change space\_key header to space\_id - [PR](https://github.com/BerriAI/litellm/pull/11595) (s/o [vanities](https://github.com/vanities))
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Fix total requests increment - [PR](https://github.com/BerriAI/litellm/pull/11718)

#### Features[​](#features-3 "Direct link to Features")

- [**Lasso Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/lasso_security)
  
  - \[NEW] Lasso Guardrails support - [PR](https://github.com/BerriAI/litellm/pull/11565)
- [**Users**](https://docs.litellm.ai/docs/proxy/users)
  
  - New `organizations` param on `/user/new` - allows adding users to orgs on creation - [PR](https://github.com/BerriAI/litellm/pull/11572/files)
- **Prevent double logging when using bridge logic** - [PR](https://github.com/BerriAI/litellm/pull/11687)

* * *

## Performance / Reliability Improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- [**Tag based routing**](https://docs.litellm.ai/docs/proxy/tag_routing)
  
  - Do not consider ‘default’ models when request specifies a tag - [PR](https://github.com/BerriAI/litellm/pull/11454) (s/o [thiagosalvatore](https://github.com/thiagosalvatore))

#### Features[​](#features-4 "Direct link to Features")

- [**Caching**](https://docs.litellm.ai/docs/caching/all_caches)
  
  - New optional ‘litellm\[caching]’ pip install for adding disk cache dependencies - [PR](https://github.com/BerriAI/litellm/pull/11600)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Bugs[​](#bugs-6 "Direct link to Bugs")

- **aiohttp**
  
  - fixes for transfer encoding error on aiohttp transport - [PR](https://github.com/BerriAI/litellm/pull/11561)

#### Features[​](#features-5 "Direct link to Features")

- **aiohttp**
  
  - Enable System Proxy Support for aiohttp transport - [PR](https://github.com/BerriAI/litellm/pull/11616) (s/o [idootop](https://github.com/idootop))
- **CLI**
  
  - Make all commands show server URL - [PR](https://github.com/BerriAI/litellm/pull/10801)
- **Unicorn**
  
  - Allow setting keep alive timeout - [PR](https://github.com/BerriAI/litellm/pull/11594)
- **Experimental Rate Limiting v2** (enable via `EXPERIMENTAL_MULTI_INSTANCE_RATE_LIMITING="True"`)
  
  - Support specifying rate limit by output\_tokens only - [PR](https://github.com/BerriAI/litellm/pull/11646)
  - Decrement parallel requests on call failure - [PR](https://github.com/BerriAI/litellm/pull/11646)
  - In-memory only rate limiting support - [PR](https://github.com/BerriAI/litellm/pull/11646)
  - Return remaining rate limits by key/user/team - [PR](https://github.com/BerriAI/litellm/pull/11646)
- **Helm**
  
  - support extraContainers in migrations-job.yaml - [PR](https://github.com/BerriAI/litellm/pull/11649)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @laurien16 made their first contribution in [https://github.com/BerriAI/litellm/pull/8460](https://github.com/BerriAI/litellm/pull/8460)
- @fengbohello made their first contribution in [https://github.com/BerriAI/litellm/pull/11547](https://github.com/BerriAI/litellm/pull/11547)
- @lapinek made their first contribution in [https://github.com/BerriAI/litellm/pull/11570](https://github.com/BerriAI/litellm/pull/11570)
- @yanwork made their first contribution in [https://github.com/BerriAI/litellm/pull/11586](https://github.com/BerriAI/litellm/pull/11586)
- @dhs-shine made their first contribution in [https://github.com/BerriAI/litellm/pull/11575](https://github.com/BerriAI/litellm/pull/11575)
- @ElefHead made their first contribution in [https://github.com/BerriAI/litellm/pull/11450](https://github.com/BerriAI/litellm/pull/11450)
- @idootop made their first contribution in [https://github.com/BerriAI/litellm/pull/11616](https://github.com/BerriAI/litellm/pull/11616)
- @stevenaldinger made their first contribution in [https://github.com/BerriAI/litellm/pull/11649](https://github.com/BerriAI/litellm/pull/11649)
- @thiagosalvatore made their first contribution in [https://github.com/BerriAI/litellm/pull/11454](https://github.com/BerriAI/litellm/pull/11454)
- @vanities made their first contribution in [https://github.com/BerriAI/litellm/pull/11595](https://github.com/BerriAI/litellm/pull/11595)
- @alvarosevilla95 made their first contribution in [https://github.com/BerriAI/litellm/pull/11661](https://github.com/BerriAI/litellm/pull/11661)

* * *

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## [Git Diff](https://github.com/BerriAI/litellm/compare/v1.72.2-stable...1.72.6.rc)[​](#git-diff "Direct link to git-diff")