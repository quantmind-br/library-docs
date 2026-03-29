---
title: 4 posts tagged with "logging" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/logging
source: sitemap
fetched_at: 2026-01-21T19:41:49.223461934-03:00
rendered_js: false
word_count: 1216
summary: This document details recent updates and new features for LiteLLM, including support for new models, improvements to spend tracking, and enhanced management UI capabilities.
tags:
    - litellm
    - release-notes
    - llm-proxy
    - spend-tracking
    - model-integration
    - cloud-logging
    - api-updates
category: reference
---

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

1. New OpenAI `/image/variations` endpoint BETA support [Docs](https://docs.litellm.ai/docs/image_variations)
2. Topaz API support on OpenAI `/image/variations` BETA endpoint [Docs](https://docs.litellm.ai/docs/providers/topaz)
3. Deepseek - r1 support w/ reasoning\_content ([Deepseek API](https://docs.litellm.ai/docs/providers/deepseek#reasoning-models), [Vertex AI](https://docs.litellm.ai/docs/providers/vertex#model-garden), [Bedrock](https://docs.litellm.ai/docs/providers/bedrock#deepseek))
4. Azure - Add azure o1 pricing [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L952)
5. Anthropic - handle `-latest` tag in model for cost calculation
6. Gemini-2.0-flash-thinking - add model pricing (it’s 0.0) [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L3393)
7. Bedrock - add stability sd3 model pricing [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L6814) (s/o [Marty Sullivan](https://github.com/marty-sullivan))
8. Bedrock - add us.amazon.nova-lite-v1:0 to model cost map [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L5619)
9. TogetherAI - add new together\_ai llama3.3 models [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L6985)

## LLM Translation[​](#llm-translation "Direct link to LLM Translation")

01. LM Studio -&gt; fix async embedding call
02. Gpt 4o models - fix response\_format translation
03. Bedrock nova - expand supported document types to include .md, .csv, etc. [Start Here](https://docs.litellm.ai/docs/providers/bedrock#usage---pdf--document-understanding)
04. Bedrock - docs on IAM role based access for bedrock - [Start Here](https://docs.litellm.ai/docs/providers/bedrock#sts-role-based-auth)
05. Bedrock - cache IAM role credentials when used
06. Google AI Studio (`gemini/`) - support gemini 'frequency\_penalty' and 'presence\_penalty'
07. Azure O1 - fix model name check
08. WatsonX - ZenAPIKey support for WatsonX [Docs](https://docs.litellm.ai/docs/providers/watsonx)
09. Ollama Chat - support json schema response format [Start Here](https://docs.litellm.ai/docs/providers/ollama#json-schema-support)
10. Bedrock - return correct bedrock status code and error message if error during streaming
11. Anthropic - Supported nested json schema on anthropic calls
12. OpenAI - `metadata` param preview support
    
    1. SDK - enable via `litellm.enable_preview_features = True`
    2. PROXY - enable via `litellm_settings::enable_preview_features: true`
13. Replicate - retry completion response on status=processing

## Spend Tracking Improvements[​](#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Bedrock - QA asserts all bedrock regional models have same `supported_` as base model
2. Bedrock - fix bedrock converse cost tracking w/ region name specified
3. Spend Logs reliability fix - when `user` passed in request body is int instead of string
4. Ensure ‘base\_model’ cost tracking works across all endpoints
5. Fixes for Image generation cost tracking
6. Anthropic - fix anthropic end user cost tracking
7. JWT / OIDC Auth - add end user id tracking from jwt auth

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

01. allows team member to become admin post-add (ui + endpoints)
02. New edit/delete button for updating team membership on UI
03. If team admin - show all team keys
04. Model Hub - clarify cost of models is per 1m tokens
05. Invitation Links - fix invalid url generated
06. New - SpendLogs Table Viewer - allows proxy admin to view spend logs on UI
    
    1. New spend logs - allow proxy admin to ‘opt in’ to logging request/response in spend logs table - enables easier abuse detection
    2. Show country of origin in spend logs
    3. Add pagination + filtering by key name/team name
07. `/key/delete` - allow team admin to delete team keys
08. Internal User ‘view’ - fix spend calculation when team selected
09. Model Analytics is now on Free
10. Usage page - shows days when spend = 0, and round spend on charts to 2 sig figs
11. Public Teams - allow admins to expose teams for new users to ‘join’ on UI - [Start Here](https://docs.litellm.ai/docs/proxy/public_teams)
12. Guardrails
    
    1. set/edit guardrails on a virtual key
    2. Allow setting guardrails on a team
    3. Set guardrails on team create + edit page
13. Support temporary budget increases on `/key/update` - new `temp_budget_increase` and `temp_budget_expiry` fields - [Start Here](https://docs.litellm.ai/docs/proxy/virtual_keys#temporary-budget-increase)
14. Support writing new key alias to AWS Secret Manager - on key rotation [Start Here](https://docs.litellm.ai/docs/secret#aws-secret-manager)

## Helm[​](#helm "Direct link to Helm")

1. add securityContext and pull policy values to migration job (s/o [https://github.com/Hexoplon](https://github.com/Hexoplon))
2. allow specifying envVars on values.yaml
3. new helm lint test

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Log the used prompt when prompt management used. [Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)
2. Support s3 logging with team alias prefixes - [Start Here](https://docs.litellm.ai/docs/proxy/logging#team-alias-prefix-in-object-key)
3. Prometheus [Start Here](https://docs.litellm.ai/docs/proxy/prometheus)
   
   1. fix litellm\_llm\_api\_time\_to\_first\_token\_metric not populating for bedrock models
   2. emit remaining team budget metric on regular basis (even when call isn’t made) - allows for more stable metrics on Grafana/etc.
   3. add key and team level budget metrics
   4. emit `litellm_overhead_latency_metric`
   5. Emit `litellm_team_budget_reset_at_metric` and `litellm_api_key_budget_remaining_hours_metric`
4. Datadog - support logging spend tags to Datadog. [Start Here](https://docs.litellm.ai/docs/proxy/enterprise#tracking-spend-for-custom-tags)
5. Langfuse - fix logging request tags, read from standard logging payload
6. GCS - don’t truncate payload on logging
7. New GCS Pub/Sub logging support [Start Here](https://docs.litellm.ai/docs/proxy/logging#google-cloud-storage---pubsub-topic)
8. Add AIM Guardrails support [Start Here](https://docs.litellm.ai/docs/proxy/guardrails/aim_security)

## Security[​](#security "Direct link to Security")

1. New Enterprise SLA for patching security vulnerabilities. [See Here](https://docs.litellm.ai/docs/enterprise#slas--professional-support)
2. Hashicorp - support using vault namespace for TLS auth. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)
3. Azure - DefaultAzureCredential support

## Health Checks[​](#health-checks "Direct link to Health Checks")

1. Cleanup pricing-only model names from wildcard route list - prevent bad health checks
2. Allow specifying a health check model for wildcard routes - [https://docs.litellm.ai/docs/proxy/health#wildcard-routes](https://docs.litellm.ai/docs/proxy/health#wildcard-routes)
3. New ‘health\_check\_timeout ‘ param with default 1min upperbound to prevent bad model from health check to hang and cause pod restarts. [Start Here](https://docs.litellm.ai/docs/proxy/health#health-check-timeout)
4. Datadog - add data dog service health check + expose new `/health/services` endpoint. [Start Here](https://docs.litellm.ai/docs/proxy/health#healthservices)

## Performance / Reliability improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability improvements")

01. 3x increase in RPS - moving to orjson for reading request body
02. LLM Routing speedup - using cached get model group info
03. SDK speedup - using cached get model info helper - reduces CPU work to get model info
04. Proxy speedup - only read request body 1 time per request
05. Infinite loop detection scripts added to codebase
06. Bedrock - pure async image transformation requests
07. Cooldowns - single deployment model group if 100% calls fail in high traffic - prevents an o1 outage from impacting other calls
08. Response Headers - return
    
    1. `x-litellm-timeout`
    2. `x-litellm-attempted-retries`
    3. `x-litellm-overhead-duration-ms`
    4. `x-litellm-response-duration-ms`
09. ensure duplicate callbacks are not added to proxy
10. Requirements.txt - bump certifi version

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

1. JWT / OIDC Auth - new `enforce_rbac` param,allows proxy admin to prevent any unmapped yet authenticated jwt tokens from calling proxy. [Start Here](https://docs.litellm.ai/docs/proxy/token_auth#enforce-role-based-access-control-rbac)
2. fix custom openapi schema generation for customized swagger’s
3. Request Headers - support reading `x-litellm-timeout` param from request headers. Enables model timeout control when using Vercel’s AI SDK + LiteLLM Proxy. [Start Here](https://docs.litellm.ai/docs/proxy/request_headers#litellm-headers)
4. JWT / OIDC Auth - new `role` based permissions for model authentication. [See Here](https://docs.litellm.ai/docs/proxy/jwt_auth_arch)

## Complete Git Diff[​](#complete-git-diff "Direct link to Complete Git Diff")

This is the diff between v1.57.8-stable and v1.59.8-stable.

Use this to see the changes in the codebase.

[**Git Diff**](https://github.com/BerriAI/litellm/compare/v1.57.8-stable...v1.59.8-stable)

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## UI Improvements[​](#ui-improvements "Direct link to UI Improvements")

### \[Opt In] Admin UI - view messages / responses[​](#opt-in-admin-ui---view-messages--responses "Direct link to [Opt In] Admin UI - view messages / responses")

You can now view messages and response logs on Admin UI.

How to enable it - add `store_prompts_in_spend_logs: true` to your `proxy_config.yaml`

Once this flag is enabled, your `messages` and `responses` will be stored in the `LiteLLM_Spend_Logs` table.

```
general_settings:
store_prompts_in_spend_logs:true
```

## DB Schema Change[​](#db-schema-change "Direct link to DB Schema Change")

Added `messages` and `responses` to the `LiteLLM_Spend_Logs` table.

**By default this is not logged.** If you want `messages` and `responses` to be logged, you need to opt in with this setting

```
general_settings:
store_prompts_in_spend_logs:true
```

`guardrails`, `logging`, `virtual key management`, `new models`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Features[​](#new-features "Direct link to New Features")

### ✨ Log Guardrail Traces[​](#-log-guardrail-traces "Direct link to ✨ Log Guardrail Traces")

Track guardrail failure rate and if a guardrail is going rogue and failing requests. [Start here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

#### Traced Guardrail Success[​](#traced-guardrail-success "Direct link to Traced Guardrail Success")

#### Traced Guardrail Failure[​](#traced-guardrail-failure "Direct link to Traced Guardrail Failure")

### `/guardrails/list`[​](#guardrailslist "Direct link to guardrailslist")

`/guardrails/list` allows clients to view available guardrails + supported guardrail params

```
curl -X GET 'http://0.0.0.0:4000/guardrails/list'
```

Expected response

```
{
"guardrails":[
{
"guardrail_name":"aporia-post-guard",
"guardrail_info":{
"params":[
{
"name":"toxicity_score",
"type":"float",
"description":"Score between 0-1 indicating content toxicity level"
},
{
"name":"pii_detection",
"type":"boolean"
}
]
}
}
]
}
```

### ✨ Guardrails with Mock LLM[​](#-guardrails-with-mock-llm "Direct link to ✨ Guardrails with Mock LLM")

Send `mock_response` to test guardrails without making an LLM call. More info on `mock_response` [here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "hi my email is ishaan@berri.ai"}
    ],
    "mock_response": "This is a mock response",
    "guardrails": ["aporia-pre-guard", "aporia-post-guard"]
  }'
```

### Assign Keys to Users[​](#assign-keys-to-users "Direct link to Assign Keys to Users")

You can now assign keys to users via Proxy UI

## New Models[​](#new-models "Direct link to New Models")

- `openrouter/openai/o1`
- `vertex_ai/mistral-large@2411`

## Fixes[​](#fixes "Direct link to Fixes")

- Fix `vertex_ai/` mistral model pricing: [https://github.com/BerriAI/litellm/pull/7345](https://github.com/BerriAI/litellm/pull/7345)
- Missing model\_group field in logs for aspeech call types [https://github.com/BerriAI/litellm/pull/7392](https://github.com/BerriAI/litellm/pull/7392)

`key management`, `budgets/rate limits`, `logging`, `guardrails`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## ✨ Budget / Rate Limit Tiers[​](#-budget--rate-limit-tiers "Direct link to ✨ Budget / Rate Limit Tiers")

Define tiers with rate limits. Assign them to keys.

Use this to control access and budgets across a lot of keys.

[**Start here**](https://docs.litellm.ai/docs/proxy/rate_limit_tiers)

```
curl -L -X POST 'http://0.0.0.0:4000/budget/new' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "budget_id": "high-usage-tier",
    "model_max_budget": {
        "gpt-4o": {"rpm_limit": 1000000}
    }
}'
```

## OTEL Bug Fix[​](#otel-bug-fix "Direct link to OTEL Bug Fix")

LiteLLM was double logging litellm\_request span. This is now fixed.

[Relevant PR](https://github.com/BerriAI/litellm/pull/7435)

## Logging for Finetuning Endpoints[​](#logging-for-finetuning-endpoints "Direct link to Logging for Finetuning Endpoints")

Logs for finetuning requests are now available on all logging providers (e.g. Datadog).

What's logged per request:

- file\_id
- finetuning\_job\_id
- any key/team metadata

**Start Here:**

- [Setup Finetuning](https://docs.litellm.ai/docs/fine_tuning)
- [Setup Logging](https://docs.litellm.ai/docs/proxy/logging#datadog)

## Dynamic Params for Guardrails[​](#dynamic-params-for-guardrails "Direct link to Dynamic Params for Guardrails")

You can now set custom parameters (like success threshold) for your guardrails in each request.

[See guardrails spec for more details](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#-pass-additional-parameters-to-guardrail)