---
title: v1.74.3-stable
url: https://docs.litellm.ai/release_notes/v1-74-3-stable
source: sitemap
fetched_at: 2026-01-21T19:42:32.327895331-03:00
rendered_js: false
word_count: 1207
summary: This document outlines the features and improvements introduced in LiteLLM v1.74.3-stable, focusing on enhanced Model Context Protocol (MCP) management, cost tracking, and the new Model Hub v2. It provides technical details on new model provider integrations and administrative controls for managing LLM proxy access.
tags:
    - litellm
    - release-notes
    - mcp-gateway
    - model-hub
    - cost-tracking
    - api-integration
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
docker.litellm.ai/berriai/litellm:v1.74.3-stable
```

* * *

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

- **MCP: Model Access Groups** - Add mcp servers to access groups, for easily managing access to users and teams.
- **MCP: Tool Cost Tracking** - Set prices for each MCP tool.
- **Model Hub v2** - New OSS Model Hub for telling developers what models are available on the proxy.
- **Bytez** - New LLM API Provider.
- **Dashscope API** - Call Alibaba's qwen models via new Dashscope API Provider.

* * *

## MCP Gateway: Model Access Groups[​](#mcp-gateway-model-access-groups "Direct link to MCP Gateway: Model Access Groups")

v1.74.3-stable adds support for adding MCP servers to access groups, this makes it **easier for Proxy Admins** to manage access to MCP servers across users and teams.

For **developers**, this means you can now connect to multiple MCP servers by passing the access group name in the `x-mcp-servers` header.

Read more [here](https://docs.litellm.ai/docs/mcp#grouping-mcps-access-groups)

* * *

This release adds cost tracking for MCP tool calls. This is great for **Proxy Admins** giving MCP access to developers as you can now attribute MCP tool call costs to specific LiteLLM keys and teams.

You can set:

- **Uniform server cost**: Set a uniform cost for all tools from a server
- **Individual tool cost**: Define individual costs for specific tools (e.g., search\_tool costs $10, get\_weather costs $5).
- **Dynamic costs**: For use cases where you want to set costs based on the MCP's response, you can write a custom post mcp call hook to parse responses and set costs dynamically.

[Get started](https://docs.litellm.ai/docs/mcp#mcp-cost-tracking)

* * *

## Model Hub v2[​](#model-hub-v2 "Direct link to Model Hub v2")

v1.74.3-stable introduces a new OSS Model Hub for telling developers what models are available on the proxy.

This is great for **Proxy Admins** as you can now tell developers what models are available on the proxy.

This improves on the previous model hub by enabling:

- The ability to show **Developers** models, even if they don't have a LiteLLM key.
- The ability for **Proxy Admins** to select specific models to be public on the model hub.
- Improved search and filtering capabilities:
  
  - search for models by partial name (e.g. `xai grok-4`)
  - filter by provider and feature (e.g. 'vision' models)
  - sort by cost (e.g. cheapest vision model from OpenAI)

[Get started](https://docs.litellm.ai/docs/proxy/model_hub)

* * *

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

#### Pricing / Context Window Updates[​](#pricing--context-window-updates "Direct link to Pricing / Context Window Updates")

ProviderModelContext WindowInput ($/1M tokens)Output ($/1M tokens)TypeXai`xai/grok-4`256k$3.00$15.00NewXai`xai/grok-4-0709`256k$3.00$15.00NewXai`xai/grok-4-latest`256k$3.00$15.00NewMistral`mistral/devstral-small-2507`128k$0.1$0.3NewMistral`mistral/devstral-medium-2507`128k$0.4$2NewAzure OpenAI`azure/o3-deep-research`200k$10$40New

#### Features[​](#features "Direct link to Features")

- [**Xinference**](https://docs.litellm.ai/docs/providers/xinference)
  
  - Image generation API support - [PR](https://github.com/BerriAI/litellm/pull/12439)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - API Key Auth support for AWS Bedrock API - [PR](https://github.com/BerriAI/litellm/pull/12495)
- [**🆕 Dashscope**](https://docs.litellm.ai/docs/providers/dashscope)
  
  - New integration from Alibaba (enables qwen usage) - [PR](https://github.com/BerriAI/litellm/pull/12361)
- [**🆕 Bytez**](https://docs.litellm.ai/docs/providers/bytez)
  
  - New /chat/completion integration - [PR](https://github.com/BerriAI/litellm/pull/12121)

#### Bugs[​](#bugs "Direct link to Bugs")

- [**Github Copilot**](https://docs.litellm.ai/docs/providers/github_copilot)
  
  - Fix API base url for Github Copilot - [PR](https://github.com/BerriAI/litellm/pull/12418)
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock)
  
  - Ensure supported bedrock/converse/ params = bedrock/ params - [PR](https://github.com/BerriAI/litellm/pull/12466)
  - Fix cache token cost calculation - [PR](https://github.com/BerriAI/litellm/pull/12488)
- [**XAI**](https://docs.litellm.ai/docs/providers/xai)
  
  - ensure finish\_reason includes tool calls when xai responses with tool calls - [PR](https://github.com/BerriAI/litellm/pull/12545)

* * *

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

#### Features[​](#features-1 "Direct link to Features")

- [**/completions**](https://docs.litellm.ai/docs/text_completion)
  
  - Return ‘reasoning\_content’ on streaming - [PR](https://github.com/BerriAI/litellm/pull/12377)
- [**/chat/completions**](https://docs.litellm.ai/docs/completion/input)
  
  - Add 'thinking blocks' to stream chunk builder - [PR](https://github.com/BerriAI/litellm/pull/12395)
- [**/v1/messages**](https://docs.litellm.ai/docs/anthropic_unified)
  
  - Fallbacks support - [PR](https://github.com/BerriAI/litellm/pull/12440)
  - tool call handling for non-anthropic models (/v1/messages to /chat/completion bridge) - [PR](https://github.com/BerriAI/litellm/pull/12473)

* * *

## [MCP Gateway](https://docs.litellm.ai/docs/mcp)[​](#mcp-gateway "Direct link to mcp-gateway")

#### Features[​](#features-2 "Direct link to Features")

- [**Cost Tracking**](https://docs.litellm.ai/docs/mcp#-mcp-cost-tracking)
  
  - Add Cost Tracking - [PR](https://github.com/BerriAI/litellm/pull/12385)
  - Add usage tracking - [PR](https://github.com/BerriAI/litellm/pull/12397)
  - Add custom cost configuration for each MCP tool - [PR](https://github.com/BerriAI/litellm/pull/12499)
  - Add support for editing MCP cost per tool - [PR](https://github.com/BerriAI/litellm/pull/12501)
  - Allow using custom post call MCP hook for cost tracking - [PR](https://github.com/BerriAI/litellm/pull/12469)
- [**Auth**](https://docs.litellm.ai/docs/mcp#using-your-mcp-with-client-side-credentials)
  
  - Allow customizing what client side auth header to use - [PR](https://github.com/BerriAI/litellm/pull/12460)
  - Raises error when MCP server header is malformed in the request - [PR](https://github.com/BerriAI/litellm/pull/12494)
- [**MCP Server**](https://docs.litellm.ai/docs/mcp#adding-your-mcp)
  
  - Allow using stdio MCPs with LiteLLM (enables using Circle CI MCP w/ LiteLLM) - [PR](https://github.com/BerriAI/litellm/pull/12530), [Get Started](https://docs.litellm.ai/docs/mcp#adding-a-stdio-mcp-server)

#### Bugs[​](#bugs-1 "Direct link to Bugs")

- **General**
  
  - Fix task group is not initialized error - [PR](https://github.com/BerriAI/litellm/pull/12411) s/o [@juancarlosm](https://github.com/juancarlosm)
- [**MCP Server**](https://docs.litellm.ai/docs/mcp#adding-your-mcp)
  
  - Fix mcp tool separator to work with Claude code - [PR](https://github.com/BerriAI/litellm/pull/12430), [Get Started](https://docs.litellm.ai/docs/mcp#adding-your-mcp)
  - Add validation to mcp server name to not allow "-" (enables namespaces to work) - [PR](https://github.com/BerriAI/litellm/pull/12515)

* * *

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Features[​](#features-3 "Direct link to Features")

- **Model Hub**
  
  - new model hub table view - [PR](https://github.com/BerriAI/litellm/pull/12468)
  - new /public/model\_hub endpoint - [PR](https://github.com/BerriAI/litellm/pull/12468)
  - Make Model Hub OSS - [PR](https://github.com/BerriAI/litellm/pull/12553)
  - New ‘make public’ modal flow for showing proxy models on public model hub - [PR](https://github.com/BerriAI/litellm/pull/12555)
- **MCP**
  
  - support for internal users to use and manage MCP servers - [PR](https://github.com/BerriAI/litellm/pull/12458)
  - Adds UI support to add MCP access groups (similar to namespaces) - [PR](https://github.com/BerriAI/litellm/pull/12470)
  - MCP Tool Testing Playground - [PR](https://github.com/BerriAI/litellm/pull/12520)
  - Show cost config on root of MCP settings - [PR](https://github.com/BerriAI/litellm/pull/12526)
- **Test Key**
  
  - Stick sessions - [PR](https://github.com/BerriAI/litellm/pull/12365)
  - MCP Access Groups - allow mcp access groups - [PR](https://github.com/BerriAI/litellm/pull/12529)
- **Usage**
  
  - Truncate long labels and improve tooltip in Top API Keys chart - [PR](https://github.com/BerriAI/litellm/pull/12371)
  - Improve Chart Readability for Tag Usage - [PR](https://github.com/BerriAI/litellm/pull/12378)
- **Teams**
  
  - Prevent navigation reset after team member operations - [PR](https://github.com/BerriAI/litellm/pull/12424)
  - Team Members - reset budget, if duration set - [PR](https://github.com/BerriAI/litellm/pull/12534)
  - Use central team member budget when max\_budget\_in\_team set on UI - [PR](https://github.com/BerriAI/litellm/pull/12533)
- **SSO**
  
  - Allow users to run a custom sso login handler - [PR](https://github.com/BerriAI/litellm/pull/12465)
- **Navbar**
  
  - improve user dropdown UI with premium badge and cleaner layout - [PR](https://github.com/BerriAI/litellm/pull/12502)
- **General**
  
  - Consistent layout for Create and Back buttons on all the pages - [PR](https://github.com/BerriAI/litellm/pull/12542)
  - Align Show Password with Checkbox - [PR](https://github.com/BerriAI/litellm/pull/12538)
  - Prevent writing default user setting updates to yaml (causes error in non-root env) - [PR](https://github.com/BerriAI/litellm/pull/12533)

#### Bugs[​](#bugs-2 "Direct link to Bugs")

- **Model Hub**
  
  - fix duplicates in /model\_group/info - [PR](https://github.com/BerriAI/litellm/pull/12468)
- **MCP**
  
  - Fix UI not syncing MCP access groups properly with object permissions - [PR](https://github.com/BerriAI/litellm/pull/12523)

* * *

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

#### Features[​](#features-4 "Direct link to Features")

- [**Langfuse**](https://docs.litellm.ai/docs/observability/langfuse_integration)
  
  - Version bump - [PR](https://github.com/BerriAI/litellm/pull/12376)
  - LANGFUSE\_TRACING\_ENVIRONMENT support - [PR](https://github.com/BerriAI/litellm/pull/12376)
- [**Bedrock Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/bedrock)
  
  - Raise Bedrock output text on 'BLOCKED' actions from guardrail - [PR](https://github.com/BerriAI/litellm/pull/12435)
- [**OTEL**](https://docs.litellm.ai/docs/observability/opentelemetry_integration)
  
  - `OTEL_RESOURCE_ATTRIBUTES` support - [PR](https://github.com/BerriAI/litellm/pull/12468)
- [**Guardrails AI**](https://docs.litellm.ai/docs/proxy/guardrails/guardrails_ai)
  
  - pre-call + logging only guardrail (pii detection/competitor names) support - [PR](https://github.com/BerriAI/litellm/pull/12506)
- [**Guardrails**](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)
  
  - \[Enterprise] Support tag based mode for guardrails - [PR](https://github.com/BerriAI/litellm/pull/12508), [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/quick_start#-tag-based-guardrail-modes)
- [**OpenAI Moderations API**](https://docs.litellm.ai/docs/proxy/guardrails/openai_moderation)
  
  - New guardrail integration - [PR](https://github.com/BerriAI/litellm/pull/12519)
- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - support tag based metrics (enables prometheus metrics for measuring roo-code/cline/claude code engagement) - [PR](https://github.com/BerriAI/litellm/pull/12534), [Get Started](https://docs.litellm.ai/docs/proxy/prometheus#custom-tags)
- [**Datadog LLM Observability**](https://docs.litellm.ai/docs/observability/datadog)
  
  - Added `total_cost` field to track costs in DataDog LLM observability metrics - [PR](https://github.com/BerriAI/litellm/pull/12467)

#### Bugs[​](#bugs-3 "Direct link to Bugs")

- [**Prometheus**](https://docs.litellm.ai/docs/proxy/prometheus)
  
  - Remove experimental `_by_tag` metrics (fixes cardinality issue) - [PR](https://github.com/BerriAI/litellm/pull/12395)
- [**Slack Alerting**](https://docs.litellm.ai/docs/proxy/alerting)
  
  - Fix slack alerting for outage and region outage alerts - [PR](https://github.com/BerriAI/litellm/pull/12464), [Get Started](https://docs.litellm.ai/docs/proxy/alerting#region-outage-alerting--enterprise-feature)

* * *

## Performance / Loadbalancing / Reliability improvements[​](#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

#### Bugs[​](#bugs-4 "Direct link to Bugs")

- [**Responses API Bridge**](https://docs.litellm.ai/docs/response_api#calling-non-responses-api-endpoints-responses-to-chatcompletions-bridge)
  
  - add image support for Responses API when falling back on Chat Completions - [PR](https://github.com/BerriAI/litellm/pull/12204) s/o [@ryan-castner](https://github.com/ryan-castner)
- **aiohttp**
  
  - Properly close aiohttp client sessions to prevent resource leaks - [PR](https://github.com/BerriAI/litellm/pull/12251)
- **Router**
  
  - don't add invalid deployment to router pattern match - [PR](https://github.com/BerriAI/litellm/pull/12459)

* * *

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

#### Bugs[​](#bugs-5 "Direct link to Bugs")

- **S3**
  
  - s3 config.yaml file - ensure yaml safe load is used - [PR](https://github.com/BerriAI/litellm/pull/12373)
- **Audit Logs**
  
  - Add audit logs for model updates - [PR](https://github.com/BerriAI/litellm/pull/12396)
- **Startup**
  
  - Multiple API Keys Created on Startup when max\_budget is enabled - [PR](https://github.com/BerriAI/litellm/pull/12436)
- **Auth**
  
  - Resolve model group alias on Auth (if user has access to underlying model, allow alias request to work) - [PR](https://github.com/BerriAI/litellm/pull/12440)
- **config.yaml**
  
  - fix parsing environment\_variables from config.yaml - [PR](https://github.com/BerriAI/litellm/pull/12482)
- **Security**
  
  - Log hashed jwt w/ prefix instead of actual value - [PR](https://github.com/BerriAI/litellm/pull/12524)

#### Features[​](#features-5 "Direct link to Features")

- **MCP**
  
  - Bump mcp version on docker img - [PR](https://github.com/BerriAI/litellm/pull/12362)
- **Request Headers**
  
  - Forward ‘anthropic-beta’ header when forward\_client\_headers\_to\_llm\_api is true - [PR](https://github.com/BerriAI/litellm/pull/12462)

* * *

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- @kanaka made their first contribution in [https://github.com/BerriAI/litellm/pull/12418](https://github.com/BerriAI/litellm/pull/12418)
- @juancarlosm made their first contribution in [https://github.com/BerriAI/litellm/pull/12411](https://github.com/BerriAI/litellm/pull/12411)
- @DmitriyAlergant made their first contribution in [https://github.com/BerriAI/litellm/pull/12356](https://github.com/BerriAI/litellm/pull/12356)
- @Rayshard made their first contribution in [https://github.com/BerriAI/litellm/pull/12487](https://github.com/BerriAI/litellm/pull/12487)
- @minghao51 made their first contribution in [https://github.com/BerriAI/litellm/pull/12361](https://github.com/BerriAI/litellm/pull/12361)
- @jdietzsch91 made their first contribution in [https://github.com/BerriAI/litellm/pull/12488](https://github.com/BerriAI/litellm/pull/12488)
- @iwinux made their first contribution in [https://github.com/BerriAI/litellm/pull/12473](https://github.com/BerriAI/litellm/pull/12473)
- @andresC98 made their first contribution in [https://github.com/BerriAI/litellm/pull/12413](https://github.com/BerriAI/litellm/pull/12413)
- @EmaSuriano made their first contribution in [https://github.com/BerriAI/litellm/pull/12509](https://github.com/BerriAI/litellm/pull/12509)
- @strawgate made their first contribution in [https://github.com/BerriAI/litellm/pull/12528](https://github.com/BerriAI/litellm/pull/12528)
- @inf3rnus made their first contribution in [https://github.com/BerriAI/litellm/pull/12121](https://github.com/BerriAI/litellm/pull/12121)

## [**Git Diff**](https://github.com/BerriAI/litellm/compare/v1.74.0-stable...v1.74.3-stable)[​](#git-diff "Direct link to git-diff")