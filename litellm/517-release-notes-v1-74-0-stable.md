---
title: v1.74.0-stable
url: https://docs.litellm.ai/release_notes/v1-74-0-stable
source: sitemap
fetched_at: 2026-01-21T19:42:30.142128695-03:00
rendered_js: false
word_count: 1172
summary: This document outlines the updates in LiteLLM version 1.74.0, detailing new features such as MCP Gateway namespacing, Azure Content Safety guardrails, and significant Python SDK performance improvements.
tags:
    - litellm
    - release-notes
    - mcp-gateway
    - azure-content-safety
    - python-sdk
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
docker.litellm.ai/berriai/litellm:v1.74.0-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **MCP Gateway Namespace Servers** - Clients connecting to LiteLLM can now specify which MCP servers to use.
- **Key/Team Based Logging on UI** - Proxy Admins can configure team or key-based logging settings directly in the UI.
- **Azure Content Safety Guardrails** - Added support for prompt injection and text moderation with Azure Content Safety Guardrails.
- **VertexAI Deepseek Models** - Support for calling VertexAI Deepseek models with LiteLLM's/chat/completions or /responses API.
- **Github Copilot API** - You can now use Github Copilot as an LLM API provider.

### MCP Gateway: Namespaced MCP Servers[​](#mcp-gateway-namespaced-mcp-servers "Direct link to MCP Gateway: Namespaced MCP Servers")

This release brings support for namespacing MCP Servers on LiteLLM MCP Gateway. This means you can specify the `x-mcp-servers` header to specify which servers to list tools from.

This is useful when you want to point MCP clients to specific MCP Servers on LiteLLM.

#### Usage[​](#usage "Direct link to Usage")

- OpenAI API
- LiteLLM Proxy
- Cursor IDE

cURL Example with Server Segregation

```
curl --location 'https://api.openai.com/v1/responses' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $OPENAI_API_KEY" \
--data '{
    "model": "gpt-4o",
    "tools": [
        {
            "type": "mcp",
            "server_label": "litellm",
            "server_url": "<your-litellm-proxy-base-url>/mcp",
            "require_approval": "never",
            "headers": {
                "x-litellm-api-key": "Bearer YOUR_LITELLM_API_KEY",
                "x-mcp-servers": "Zapier_Gmail"
            }
        }
    ],
    "input": "Run available tools",
    "tool_choice": "required"
}'
```

In this example, the request will only have access to tools from the "Zapier\_Gmail" MCP server.

### Team / Key Based Logging on UI[​](#team--key-based-logging-on-ui "Direct link to Team / Key Based Logging on UI")

This release brings support for Proxy Admins to configure Team/Key Based Logging Settings on the UI. This allows routing LLM request/response logs to different Langfuse/Arize projects based on the team or key.

For developers using LiteLLM, their logs are automatically routed to their specific Arize/Langfuse projects. On this release, we support the following integrations for key/team based logging:

- `langfuse`
- `arize`
- `langsmith`

### Azure Content Safety Guardrails[​](#azure-content-safety-guardrails "Direct link to Azure Content Safety Guardrails")

LiteLLM now supports **Azure Content Safety Guardrails** for Prompt Injection and Text Moderation. This is **great for internal chat-ui** use cases, as you can now create guardrails with detection for Azure’s Harm Categories, specify custom severity thresholds and run them across 100+ LLMs for just that use-case (or across all your calls).

[Get Started](https://docs.litellm.ai/docs/proxy/guardrails/azure_content_guardrail)

### Python SDK: 2.3 Second Faster Import Times[​](#python-sdk-23-second-faster-import-times "Direct link to Python SDK: 2.3 Second Faster Import Times")

This release brings significant performance improvements to the Python SDK with 2.3 seconds faster import times. We've refactored the initialization process to reduce startup overhead, making LiteLLM more efficient for applications that need quick initialization. This is a major improvement for applications that need to initialize LiteLLM quickly.

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)TypeWatsonx`watsonx/mistralai/mistral-large`131k$3.00$10.00NewAzure AI`azure_ai/cohere-rerank-v3.5`4k$2.00/1k queries-New (Rerank)

#### Features[​](#features "Direct link to Features")

- [**🆕 GitHub Copilot**](https://docs.litellm.ai/docs/providers/github_copilot) - Use GitHub Copilot API with LiteLLM - [PR](https://github.com/BerriAI/litellm/pull/12325), [Get Started](https://docs.litellm.ai/docs/providers/github_copilot)
- [**🆕 VertexAI DeepSeek**](https://docs.litellm.ai/docs/providers/vertex) - Add support for VertexAI DeepSeek models - [PR](https://github.com/BerriAI/litellm/pull/12312), [Get Started](https://docs.litellm.ai/docs/providers/vertex_partner#vertexai-deepseek)
- [**Azure AI**](https://docs.litellm.ai/docs/providers/azure_ai)
  
  - Add azure\_ai cohere rerank v3.5 - [PR](https://github.com/BerriAI/litellm/pull/12283), [Get Started](https://docs.litellm.ai/docs/providers/azure_ai#rerank-endpoint)
- [**Vertex AI**](https://docs.litellm.ai/docs/providers/vertex)
  
  - Add size parameter support for image generation - [PR](https://github.com/BerriAI/litellm/pull/12292), [Get Started](https://docs.litellm.ai/docs/providers/vertex_image)
- [**Custom LLM**](https://docs.litellm.ai/docs/providers/custom_llm_server)
  
  - Pass through extra_ properties on "custom" llm provider - [PR](https://github.com/BerriAI/litellm/pull/12185)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Mistral**](https://docs.litellm.ai/docs/providers/mistral)
  
  - Fix transform\_response handling for empty string content - [PR](https://github.com/BerriAI/litellm/pull/12202)
  - Turn Mistral to use llm\_http\_handler - [PR](https://github.com/BerriAI/litellm/pull/12245)
- [**Gemini**](https://docs.litellm.ai/docs/providers/gemini)
  
  - Fix tool call sequence - [PR](https://github.com/BerriAI/litellm/pull/11999)
  - Fix custom api\_base path preservation - [PR](https://github.com/BerriAI/litellm/pull/12215)
- [**Anthropic**](https://docs.litellm.ai/docs/providers/anthropic)
  
  - Fix user\_id validation logic - [PR](https://github.com/BerriAI/litellm/pull/11432)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Support optional args for bedrock - [PR](https://github.com/BerriAI/litellm/pull/12287)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama)
  
  - Fix default parameters for ollama-chat - [PR](https://github.com/BerriAI/litellm/pull/12201)
- [**VLLM**](https://docs.litellm.ai/docs/providers/vllm)
  
  - Add 'audio\_url' message type support - [PR](https://github.com/BerriAI/litellm/pull/12270)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/batches**](https://docs.litellm.ai/docs/batches)
  
  - Support batch retrieve with target model Query Param - [PR](https://github.com/BerriAI/litellm/pull/12228)
  - Anthropic completion bridge improvements - [PR](https://github.com/BerriAI/litellm/pull/12228)
- [**/responses**](https://docs.litellm.ai/docs/response_api)
  
  - Azure responses api bridge improvements - [PR](https://github.com/BerriAI/litellm/pull/12224)
  - Fix responses api error handling - [PR](https://github.com/BerriAI/litellm/pull/12225)
- [**/mcp (MCP Gateway)**](https://docs.litellm.ai/docs/mcp)
  
  - Add MCP url masking on frontend - [PR](https://github.com/BerriAI/litellm/pull/12247)
  - Add MCP servers header to scope - [PR](https://github.com/BerriAI/litellm/pull/12266)
  - Litellm mcp tool prefix - [PR](https://github.com/BerriAI/litellm/pull/12289)
  - Segregate MCP tools on connections using headers - [PR](https://github.com/BerriAI/litellm/pull/12296)
  - Added changes to mcp url wrapping - [PR](https://github.com/BerriAI/litellm/pull/12207)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- [**/v1/messages**](https://docs.litellm.ai/docs/anthropic_unified)
  
  - Remove hardcoded model name on streaming - [PR](https://github.com/BerriAI/litellm/pull/12131)
  - Support lowest latency routing - [PR](https://github.com/BerriAI/litellm/pull/12180)
  - Non-anthropic models token usage returned - [PR](https://github.com/BerriAI/litellm/pull/12184)
- [**/chat/completions**](https://docs.litellm.ai/docs/providers/anthropic_unified)
  
  - Support Cursor IDE tool\_choice format `{"type": "auto"}` - [PR](https://github.com/BerriAI/litellm/pull/12168)
- [**/generateContent**](https://docs.litellm.ai/docs/generate_content)
  
  - Allow passing litellm\_params - [PR](https://github.com/BerriAI/litellm/pull/12177)
  - Only pass supported params when using OpenAI models - [PR](https://github.com/BerriAI/litellm/pull/12297)
  - Fix using gemini-cli with Vertex Anthropic Models - [PR](https://github.com/BerriAI/litellm/pull/12246)
- **Streaming**
  
  - Fix Error code: 307 for LlamaAPI Streaming Chat - [PR](https://github.com/BerriAI/litellm/pull/11946)
  - Store finish reason even if is\_finished - [PR](https://github.com/BerriAI/litellm/pull/12250)

* * *

## Spend Tracking / Budget Improvements[​](#spend-tracking--budget-improvements "Direct link to Spend Tracking / Budget Improvements")

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- Fix allow strings in calculate cost - [PR](https://github.com/BerriAI/litellm/pull/12200)
- VertexAI Anthropic streaming cost tracking with prompt caching fixes - [PR](https://github.com/BerriAI/litellm/pull/12188)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- **Team Management**
  
  - Prevent team model reset on model add - [PR](https://github.com/BerriAI/litellm/pull/12144)
  - Return team-only models on /v2/model/info - [PR](https://github.com/BerriAI/litellm/pull/12144)
  - Render team member budget correctly - [PR](https://github.com/BerriAI/litellm/pull/12144)
- **UI Rendering**
  
  - Fix rendering ui on non-root images - [PR](https://github.com/BerriAI/litellm/pull/12226)
  - Correctly display 'Internal Viewer' user role - [PR](https://github.com/BerriAI/litellm/pull/12284)
- **Configuration**
  
  - Handle empty config.yaml - [PR](https://github.com/BerriAI/litellm/pull/12189)
  - Fix gemini /models - replace models/ as expected - [PR](https://github.com/BerriAI/litellm/pull/12189)

#### Features[​](#features-2 "Direct link to Features")

- **Team Management**
  
  - Allow adding team specific logging callbacks - [PR](https://github.com/BerriAI/litellm/pull/12261)
  - Add Arize Team Based Logging - [PR](https://github.com/BerriAI/litellm/pull/12264)
  - Allow Viewing/Editing Team Based Callbacks - [PR](https://github.com/BerriAI/litellm/pull/12265)
- **UI Improvements**
  
  - Comma separated spend and budget display - [PR](https://github.com/BerriAI/litellm/pull/12317)
  - Add logos to callback list - [PR](https://github.com/BerriAI/litellm/pull/12244)
- **CLI**
  
  - Add litellm-proxy cli login for starting to use litellm proxy - [PR](https://github.com/BerriAI/litellm/pull/12216)
- **Email Templates**
  
  - Customizable Email template - Subject and Signature - [PR](https://github.com/BerriAI/litellm/pull/12218)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-3 "Direct link to Features")

- Guardrails
  
  - All guardrails are now supported on the UI - [PR](https://github.com/BerriAI/litellm/pull/12349)
- [**Azure Content Safety**](https://docs.litellm.ai/docs/guardrails/azure_content_safety)
  
  - Add Azure Content Safety Guardrails to LiteLLM proxy - [PR](https://github.com/BerriAI/litellm/pull/12268)
  - Add azure content safety guardrails to the UI - [PR](https://github.com/BerriAI/litellm/pull/12309)
- [**DeepEval**](https://docs.litellm.ai/docs/observability/deepeval_integration)
  
  - Fix DeepEval logging format for failure events - [PR](https://github.com/BerriAI/litellm/pull/12303)
- [**Arize**](https://docs.litellm.ai/docs/proxy/logging#arize)
  
  - Add Arize Team Based Logging - [PR](https://github.com/BerriAI/litellm/pull/12264)
- [**Langfuse**](https://docs.litellm.ai/docs/proxy/logging#langfuse)
  
  - Langfuse prompt\_version support - [PR](https://github.com/BerriAI/litellm/pull/12301)
- [**Sentry Integration**](https://docs.litellm.ai/docs/observability/sentry)
  
  - Add sentry scrubbing - [PR](https://github.com/BerriAI/litellm/pull/12210)
- [**AWS SQS Logging**](https://docs.litellm.ai/docs/proxy/logging#aws-sqs)
  
  - New AWS SQS Logging Integration - [PR](https://github.com/BerriAI/litellm/pull/12176)
- [**S3 Logger**](https://docs.litellm.ai/docs/proxy/logging#s3-buckets)
  
  - Add failure logging support - [PR](https://github.com/BerriAI/litellm/pull/12299)
- [**Prometheus Metrics**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Add better error validation for prometheus metrics and labels - [PR](https://github.com/BerriAI/litellm/pull/12182)

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- **Security**
  
  - Ensure only LLM API route fails get logged on Langfuse - [PR](https://github.com/BerriAI/litellm/pull/12308)
- **OpenMeter**
  
  - Integration error handling fix - [PR](https://github.com/BerriAI/litellm/pull/12147)
- **Message Redaction**
  
  - Ensure message redaction works for responses API logging - [PR](https://github.com/BerriAI/litellm/pull/12291)
- **Bedrock Guardrails**
  
  - Fix bedrock guardrails post\_call for streaming responses - [PR](https://github.com/BerriAI/litellm/pull/12252)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Features[​](#features-4 "Direct link to Features")

- **Python SDK**
  
  - 2 second faster import times - [PR](https://github.com/BerriAI/litellm/pull/12135)
  - Reduce python sdk import time by .3s - [PR](https://github.com/BerriAI/litellm/pull/12140)
- **Error Handling**
  
  - Add error handling for MCP tools not found or invalid server - [PR](https://github.com/BerriAI/litellm/pull/12223)
- **SSL/TLS**
  
  - Fix SSL certificate error - [PR](https://github.com/BerriAI/litellm/pull/12327)
  - Fix custom ca bundle support in aiohttp transport - [PR](https://github.com/BerriAI/litellm/pull/12281)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Startup**
  
  - Add new banner on startup - [PR](https://github.com/BerriAI/litellm/pull/12328)
- **Dependencies**
  
  - Update pydantic version - [PR](https://github.com/BerriAI/litellm/pull/12213)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @wildcard made their first contribution in [https://github.com/BerriAI/litellm/pull/12157](https://github.com/BerriAI/litellm/pull/12157)
- @colesmcintosh made their first contribution in [https://github.com/BerriAI/litellm/pull/12168](https://github.com/BerriAI/litellm/pull/12168)
- @seyeong-han made their first contribution in [https://github.com/BerriAI/litellm/pull/11946](https://github.com/BerriAI/litellm/pull/11946)
- @dinggh made their first contribution in [https://github.com/BerriAI/litellm/pull/12162](https://github.com/BerriAI/litellm/pull/12162)
- @raz-alon made their first contribution in [https://github.com/BerriAI/litellm/pull/11432](https://github.com/BerriAI/litellm/pull/11432)
- @tofarr made their first contribution in [https://github.com/BerriAI/litellm/pull/12200](https://github.com/BerriAI/litellm/pull/12200)
- @szafranek made their first contribution in [https://github.com/BerriAI/litellm/pull/12179](https://github.com/BerriAI/litellm/pull/12179)
- @SamBoyd made their first contribution in [https://github.com/BerriAI/litellm/pull/12147](https://github.com/BerriAI/litellm/pull/12147)
- @lizzij made their first contribution in [https://github.com/BerriAI/litellm/pull/12219](https://github.com/BerriAI/litellm/pull/12219)
- @cipri-tom made their first contribution in [https://github.com/BerriAI/litellm/pull/12201](https://github.com/BerriAI/litellm/pull/12201)
- @zsimjee made their first contribution in [https://github.com/BerriAI/litellm/pull/12185](https://github.com/BerriAI/litellm/pull/12185)
- @jroberts2600 made their first contribution in [https://github.com/BerriAI/litellm/pull/12175](https://github.com/BerriAI/litellm/pull/12175)
- @njbrake made their first contribution in [https://github.com/BerriAI/litellm/pull/12202](https://github.com/BerriAI/litellm/pull/12202)
- @NANDINI-star made their first contribution in [https://github.com/BerriAI/litellm/pull/12244](https://github.com/BerriAI/litellm/pull/12244)
- @utsumi-fj made their first contribution in [https://github.com/BerriAI/litellm/pull/12230](https://github.com/BerriAI/litellm/pull/12230)
- @dcieslak19973 made their first contribution in [https://github.com/BerriAI/litellm/pull/12283](https://github.com/BerriAI/litellm/pull/12283)
- @hanouticelina made their first contribution in [https://github.com/BerriAI/litellm/pull/12286](https://github.com/BerriAI/litellm/pull/12286)
- @lowjiansheng made their first contribution in [https://github.com/BerriAI/litellm/pull/11999](https://github.com/BerriAI/litellm/pull/11999)
- @JoostvDoorn made their first contribution in [https://github.com/BerriAI/litellm/pull/12281](https://github.com/BerriAI/litellm/pull/12281)
- @takashiishida made their first contribution in [https://github.com/BerriAI/litellm/pull/12239](https://github.com/BerriAI/litellm/pull/12239)

## [**Git Diff**](https://github.com/BerriAI/litellm/compare/v1.73.6-stable...v1.74.0-stable)[​](#git-diff "Direct link to git-diff")