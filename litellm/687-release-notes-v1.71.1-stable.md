---
title: v1.71.1-stable - 2x Higher Requests Per Second (RPS)
url: https://docs.litellm.ai/release_notes/v1.71.1-stable
source: sitemap
fetched_at: 2026-01-21T19:43:40.973498843-03:00
rendered_js: false
word_count: 986
summary: This document outlines the release notes for LiteLLM v1.71.1-stable, detailing performance enhancements via aiohttp, new file permission features, and updated support for numerous LLM providers and models.
tags:
    - litellm-release
    - performance-scaling
    - aiohttp-transport
    - file-permissions
    - model-updates
    - api-reference
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
docker.litellm.ai/berriai/litellm:main-v1.71.1-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

LiteLLM v1.71.1-stable is live now. Here are the key highlights of this release:

- **Performance improvements**: LiteLLM can now scale to 200 RPS per instance with a 74ms median response time.
- **File Permissions**: Control file access across OpenAI, Azure, VertexAI.
- **MCP x OpenAI**: Use MCP servers with OpenAI Responses API.

## Performance Improvements[​](#performance-improvements "Direct link to Performance Improvements")

This release brings aiohttp support for all LLM api providers. This means that LiteLLM can now scale to 200 RPS per instance with a 40ms median latency overhead.

This change doubles the RPS LiteLLM can scale to at this latency overhead.

You can opt into this by enabling the flag below. (We expect to make this the default in 1 week.)

### Flag to enable[​](#flag-to-enable "Direct link to Flag to enable")

**On LiteLLM Proxy**

Set the `USE_AIOHTTP_TRANSPORT=True` in the environment variables.

Environment Variable

```
export USE_AIOHTTP_TRANSPORT="True"
```

**On LiteLLM Python SDK**

Set the `use_aiohttp_transport=True` to enable aiohttp transport.

Python SDK

```
import litellm

litellm.use_aiohttp_transport =True# default is False, enable this to use aiohttp transport
result = litellm.completion(
    model="openai/gpt-4o",
    messages=[{"role":"user","content":"Hello, world!"}],
)
print(result)
```

## File Permissions[​](#file-permissions "Direct link to File Permissions")

This release brings support for [File Permissions](https://docs.litellm.ai/docs/proxy/litellm_managed_files#file-permissions) and [Finetuning APIs](https://docs.litellm.ai/docs/proxy/managed_finetuning) to [LiteLLM Managed Files](https://docs.litellm.ai/docs/proxy/litellm_managed_files). This is great for:

- **Proxy Admins**: as users can only view/edit/delete files they’ve created - even when using shared OpenAI/Azure/Vertex deployments.
- **Developers**: get a standard interface to use Files across Chat/Finetuning/Batch APIs.

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **Gemini [VertexAI](https://docs.litellm.ai/docs/providers/vertex), [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini)**
  
  - New gemini models - [PR 1](https://github.com/BerriAI/litellm/pull/10991), [PR 2](https://github.com/BerriAI/litellm/pull/10998)
    
    - `gemini-2.5-flash-preview-tts`
    - `gemini-2.0-flash-preview-image-generation`
    - `gemini/gemini-2.5-flash-preview-05-20`
    - `gemini-2.5-flash-preview-05-20`
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Claude-4 model family support - [PR](https://github.com/BerriAI/litellm/pull/11060)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Claude-4 model family support - [PR](https://github.com/BerriAI/litellm/pull/11060)
  - Support for `reasoning_effort` and `thinking` parameters for Claude-4 - [PR](https://github.com/BerriAI/litellm/pull/11114)
- [**VertexAI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Claude-4 model family support - [PR](https://github.com/BerriAI/litellm/pull/11060)
  - Global endpoints support - [PR](https://github.com/BerriAI/litellm/pull/10658)
  - authorized\_user credentials type support - [PR](https://github.com/BerriAI/litellm/pull/10899)
- [**xAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - `xai/grok-3` pricing information - [PR](https://github.com/BerriAI/litellm/pull/11028)
- [**LM Studio**](https://docs.litellm.ai/docs/providers/lm_studio)
  
  - Structured JSON schema outputs support - [PR](https://github.com/BerriAI/litellm/pull/10929)
- [**SambaNova**](https://docs.litellm.ai/docs/providers/sambanova)
  
  - Updated models and parameters - [PR](https://github.com/BerriAI/litellm/pull/10900)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks)
  
  - Llama 4 Maverick model cost - [PR](https://github.com/BerriAI/litellm/pull/11008)
  - Claude 3.7 Sonnet output token cost correction - [PR](https://github.com/BerriAI/litellm/pull/11007)
- [**Azure**](https://docs.litellm.ai/docs/providers/azure)
  
  - Mistral Medium 25.05 support - [PR](https://github.com/BerriAI/litellm/pull/11063)
  - Certificate-based authentication support - [PR](https://github.com/BerriAI/litellm/pull/11069)
- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - devstral-small-2505 model pricing and context window - [PR](https://github.com/BerriAI/litellm/pull/11103)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Wildcard model support - [PR](https://github.com/BerriAI/litellm/pull/10982)
- [**CustomLLM**](https://docs.litellm.ai/docs/providers/custom_llm_server)
  
  - Embeddings support added - [PR](https://github.com/BerriAI/litellm/pull/10980)
- [**Featherless AI**](https://docs.litellm.ai/docs/providers/featherless_ai)
  
  - Access to 4200+ models - [PR](https://github.com/BerriAI/litellm/pull/10596)

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

- [**Image Edits**](https://docs.litellm.ai/docs/image_generation)
  
  - `/v1/images/edits` - Support for /images/edits endpoint - [PR](https://github.com/BerriAI/litellm/pull/11020) [PR](https://github.com/BerriAI/litellm/pull/11123)
  - Content policy violation error mapping - [PR](https://github.com/BerriAI/litellm/pull/11113)
- [**Responses API**](https://docs.litellm.ai/docs/response_api)
  
  - MCP support for Responses API - [PR](https://github.com/BerriAI/litellm/pull/11029)
- [**Files API**](https://docs.litellm.ai/docs/fine_tuning)
  
  - LiteLLM Managed Files support for finetuning - [PR](https://github.com/BerriAI/litellm/pull/11039) [PR](https://github.com/BerriAI/litellm/pull/11040)
  - Validation for file operations (retrieve/list/delete) - [PR](https://github.com/BerriAI/litellm/pull/11081)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Teams**
  
  - Key and member count display - [PR](https://github.com/BerriAI/litellm/pull/10950)
  - Spend rounded to 4 decimal points - [PR](https://github.com/BerriAI/litellm/pull/11013)
  - Organization and team create buttons repositioned - [PR](https://github.com/BerriAI/litellm/pull/10948)
- **Keys**
  
  - Key reassignment and 'updated at' column - [PR](https://github.com/BerriAI/litellm/pull/10960)
  - Show model access groups during creation - [PR](https://github.com/BerriAI/litellm/pull/10965)
- **Logs**
  
  - Model filter on logs - [PR](https://github.com/BerriAI/litellm/pull/11048)
  - Passthrough endpoint error logs support - [PR](https://github.com/BerriAI/litellm/pull/10990)
- **Guardrails**
  
  - Config.yaml guardrails display - [PR](https://github.com/BerriAI/litellm/pull/10959)
- **Organizations/Users**
  
  - Spend rounded to 4 decimal points - [PR](https://github.com/BerriAI/litellm/pull/11023)
  - Show clear error when adding a user to a team - [PR](https://github.com/BerriAI/litellm/pull/10978)
- **Audit Logs**
  
  - `/list` and `/info` endpoints for Audit Logs - [PR](https://github.com/BerriAI/litellm/pull/11102)

## Logging / Alerting Integrations[​](#logging--alerting-integrations "Direct link to Logging / Alerting Integrations")

- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Track `route` on proxy\_* metrics - [PR](https://github.com/BerriAI/litellm/pull/10992)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Support for `prompt_label` parameter - [PR](https://github.com/BerriAI/litellm/pull/11018)
  - Consistent modelParams logging - [PR](https://github.com/BerriAI/litellm/pull/11018)
- [**DeepEval/ConfidentAI**](https://docs.litellm.ai/docs/proxy/logging#deepeval)
  
  - Logging enabled for proxy and SDK - [PR](https://github.com/BerriAI/litellm/pull/10649)
- [**Logfire**](https://docs.litellm.ai/docs/proxy/logging)
  
  - Fix otel proxy server initialization when using Logfire - [PR](https://github.com/BerriAI/litellm/pull/11091)

## Authentication & Security[​](#authentication--security "Direct link to Authentication & Security")

- [**JWT Authentication**](https://docs.litellm.ai/docs/proxy/token_auth)
  
  - Support for applying default internal user parameters when upserting a user via JWT authentication - [PR](https://github.com/BerriAI/litellm/pull/10995)
  - Map a user to a team when upserting a user via JWT authentication - [PR](https://github.com/BerriAI/litellm/pull/11108)
- **Custom Auth**
  
  - Support for switching between custom auth and API key auth - [PR](https://github.com/BerriAI/litellm/pull/11070)

## Performance / Reliability Improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

- **aiohttp Transport**
  
  - 97% lower median latency (feature flagged) - [PR](https://github.com/BerriAI/litellm/pull/11097) [PR](https://github.com/BerriAI/litellm/pull/11132)
- **Background Health Checks**
  
  - Improved reliability - [PR](https://github.com/BerriAI/litellm/pull/10887)
- **Response Handling**
  
  - Better streaming status code detection - [PR](https://github.com/BerriAI/litellm/pull/10962)
  - Response ID propagation improvements - [PR](https://github.com/BerriAI/litellm/pull/11006)
- **Thread Management**
  
  - Removed error-creating threads for reliability - [PR](https://github.com/BerriAI/litellm/pull/11066)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- [**Proxy CLI**](https://docs.litellm.ai/docs/proxy/cli)
  
  - Skip server startup flag - [PR](https://github.com/BerriAI/litellm/pull/10665)
  - Avoid DATABASE\_URL override when provided - [PR](https://github.com/BerriAI/litellm/pull/11076)
- **Model Management**
  
  - Clear cache and reload after model updates - [PR](https://github.com/BerriAI/litellm/pull/10853)
  - Computer use support tracking - [PR](https://github.com/BerriAI/litellm/pull/10881)
- **Helm Chart**
  
  - LoadBalancer class support - [PR](https://github.com/BerriAI/litellm/pull/11064)

## Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

This release includes numerous bug fixes to improve stability and reliability:

- **LLM Provider Fixes**
  
  - VertexAI:
    
    - Fixed quota\_project\_id parameter issue - [PR](https://github.com/BerriAI/litellm/pull/10915)
    - Fixed credential refresh exceptions - [PR](https://github.com/BerriAI/litellm/pull/10969)
  - Cohere: Fixes for adding Cohere models through LiteLLM UI - [PR](https://github.com/BerriAI/litellm/pull/10822)
  - Anthropic:
    
    - Fixed streaming dict object handling for /v1/messages - [PR](https://github.com/BerriAI/litellm/pull/11032)
  - OpenRouter:
    
    - Fixed stream usage ID issues - [PR](https://github.com/BerriAI/litellm/pull/11004)
- **Authentication & Users**
  
  - Fixed invitation email link generation - [PR](https://github.com/BerriAI/litellm/pull/10958)
  - Fixed JWT authentication default role - [PR](https://github.com/BerriAI/litellm/pull/10995)
  - Fixed user budget reset functionality - [PR](https://github.com/BerriAI/litellm/pull/10993)
  - Fixed SSO user compatibility and email validation - [PR](https://github.com/BerriAI/litellm/pull/11106)
- **Database & Infrastructure**
  
  - Fixed DB connection parameter handling - [PR](https://github.com/BerriAI/litellm/pull/10842)
  - Fixed email invitation link - [PR](https://github.com/BerriAI/litellm/pull/11031)
- **UI & Display**
  
  - Fixed MCP tool rendering when no arguments required - [PR](https://github.com/BerriAI/litellm/pull/11012)
  - Fixed team model alias deletion - [PR](https://github.com/BerriAI/litellm/pull/11121)
  - Fixed team viewer permissions - [PR](https://github.com/BerriAI/litellm/pull/11127)
- **Model & Routing**
  
  - Fixed team model mapping in route requests - [PR](https://github.com/BerriAI/litellm/pull/11111)
  - Fixed standard optional parameter passing - [PR](https://github.com/BerriAI/litellm/pull/11124)

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- [@DarinVerheijke](https://github.com/DarinVerheijke) made their first contribution in PR [#10596](https://github.com/BerriAI/litellm/pull/10596)
- [@estsauver](https://github.com/estsauver) made their first contribution in PR [#10929](https://github.com/BerriAI/litellm/pull/10929)
- [@mohittalele](https://github.com/mohittalele) made their first contribution in PR [#10665](https://github.com/BerriAI/litellm/pull/10665)
- [@pselden](https://github.com/pselden) made their first contribution in PR [#10899](https://github.com/BerriAI/litellm/pull/10899)
- [@unrealandychan](https://github.com/unrealandychan) made their first contribution in PR [#10842](https://github.com/BerriAI/litellm/pull/10842)
- [@dastaiger](https://github.com/dastaiger) made their first contribution in PR [#10946](https://github.com/BerriAI/litellm/pull/10946)
- [@slytechnical](https://github.com/slytechnical) made their first contribution in PR [#10881](https://github.com/BerriAI/litellm/pull/10881)
- [@daarko10](https://github.com/daarko10) made their first contribution in PR [#11006](https://github.com/BerriAI/litellm/pull/11006)
- [@sorenmat](https://github.com/sorenmat) made their first contribution in PR [#10658](https://github.com/BerriAI/litellm/pull/10658)
- [@matthid](https://github.com/matthid) made their first contribution in PR [#10982](https://github.com/BerriAI/litellm/pull/10982)
- [@jgowdy-godaddy](https://github.com/jgowdy-godaddy) made their first contribution in PR [#11032](https://github.com/BerriAI/litellm/pull/11032)
- [@bepotp](https://github.com/bepotp) made their first contribution in PR [#11008](https://github.com/BerriAI/litellm/pull/11008)
- [@jmorenoc-o](https://github.com/jmorenoc-o) made their first contribution in PR [#11031](https://github.com/BerriAI/litellm/pull/11031)
- [@martin-liu](https://github.com/martin-liu) made their first contribution in PR [#11076](https://github.com/BerriAI/litellm/pull/11076)
- [@gunjan-solanki](https://github.com/gunjan-solanki) made their first contribution in PR [#11064](https://github.com/BerriAI/litellm/pull/11064)
- [@tokoko](https://github.com/tokoko) made their first contribution in PR [#10980](https://github.com/BerriAI/litellm/pull/10980)
- [@spike-spiegel-21](https://github.com/spike-spiegel-21) made their first contribution in PR [#10649](https://github.com/BerriAI/litellm/pull/10649)
- [@kreatoo](https://github.com/kreatoo) made their first contribution in PR [#10927](https://github.com/BerriAI/litellm/pull/10927)
- [@baejooc](https://github.com/baejooc) made their first contribution in PR [#10887](https://github.com/BerriAI/litellm/pull/10887)
- [@keykbd](https://github.com/keykbd) made their first contribution in PR [#11114](https://github.com/BerriAI/litellm/pull/11114)
- [@dalssoft](https://github.com/dalssoft) made their first contribution in PR [#11088](https://github.com/BerriAI/litellm/pull/11088)
- [@jtong99](https://github.com/jtong99) made their first contribution in PR [#10853](https://github.com/BerriAI/litellm/pull/10853)

## Demo Instance[​](#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  
  - Username: admin
  - Password: sk-1234

## [Git Diff](https://github.com/BerriAI/litellm/releases)[​](#git-diff "Direct link to git-diff")