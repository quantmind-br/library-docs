---
title: v1.69.0-stable - Loadbalance Batch API Models
url: https://docs.litellm.ai/release_notes/v1.69.0-stable
source: sitemap
fetched_at: 2026-01-21T19:43:39.413311833-03:00
rendered_js: false
word_count: 951
summary: This document provides the release notes for LiteLLM version 1.69.0-stable, detailing new features like Batch API load balancing and support for providers such as Nscale and updated Gemini models. It also highlights bug fixes and performance enhancements across the proxy's management UI and various LLM endpoints.
tags:
    - litellm
    - release-notes
    - batch-api
    - model-updates
    - llm-proxy
    - api-integration
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
docker.litellm.ai/berriai/litellm:main-v1.69.0-stable
```

## Key Highlights[​](#key-highlights "Direct link to Key Highlights")

LiteLLM v1.69.0-stable brings the following key improvements:

- **Loadbalance Batch API Models**: Easily loadbalance across multiple azure batch deployments using LiteLLM Managed Files
- **Email Invites 2.0**: Send new users onboarded to LiteLLM an email invite.
- **Nscale**: LLM API for compliance with European regulations.
- **Bedrock /v1/messages**: Use Bedrock Anthropic models with Anthropic's /v1/messages.

## Batch API Load Balancing[​](#batch-api-load-balancing "Direct link to Batch API Load Balancing")

This release brings LiteLLM Managed File support to Batches. This is great for:

- Proxy Admins: You can now control which Batch models users can call.
- Developers: You no longer need to know the Azure deployment name when creating your batch .jsonl files - just specify the model your LiteLLM key has access to.

Over time, we expect LiteLLM Managed Files to be the way most teams use Files across `/chat/completions`, `/batch`, `/fine_tuning` endpoints.

[Read more here](https://docs.litellm.ai/docs/proxy/managed_batches)

## Email Invites[​](#email-invites "Direct link to Email Invites")

This release brings the following improvements to our email invite integration:

- New templates for user invited and key created events.
- Fixes for using SMTP email providers.
- Native support for Resend API.
- Ability for Proxy Admins to control email events.

For LiteLLM Cloud Users, please reach out to us if you want this enabled for your instance.

[Read more here](https://docs.litellm.ai/docs/proxy/email)

## New Models / Updated Models[​](#new-models--updated-models "Direct link to New Models / Updated Models")

- **Gemini ([VertexAI](https://docs.litellm.ai/docs/providers/vertex#usage-with-litellm-proxy-server) + [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini))**
  
  - Added `gemini-2.5-pro-preview-05-06` models with pricing and context window info - [PR](https://github.com/BerriAI/litellm/pull/10597)
  - Set correct context window length for all Gemini 2.5 variants - [PR](https://github.com/BerriAI/litellm/pull/10690)
- [**Perplexity**](https://docs.litellm.ai/docs/providers/perplexity):
  
  - Added new Perplexity models - [PR](https://github.com/BerriAI/litellm/pull/10652)
  - Added sonar-deep-research model pricing - [PR](https://github.com/BerriAI/litellm/pull/10537)
- [**Azure OpenAI**](https://docs.litellm.ai/docs/providers/azure):
  
  - Fixed passing through of azure\_ad\_token\_provider parameter - [PR](https://github.com/BerriAI/litellm/pull/10694)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai):
  
  - Added support for pdf url's in 'file' parameter - [PR](https://github.com/BerriAI/litellm/pull/10640)
- [**Sagemaker**](https://docs.litellm.ai/docs/providers/aws_sagemaker):
  
  - Fix content length for `sagemaker_chat` provider - [PR](https://github.com/BerriAI/litellm/pull/10607)
- [**Azure AI Foundry**](https://docs.litellm.ai/docs/providers/azure_ai):
  
  - Added cost tracking for the following models [PR](https://github.com/BerriAI/litellm/pull/9956)
    
    - DeepSeek V3 0324
    - Llama 4 Scout
    - Llama 4 Maverick
- [**Bedrock**](https://docs.litellm.ai/docs/providers/bedrock):
  
  - Added cost tracking for Bedrock Llama 4 models - [PR](https://github.com/BerriAI/litellm/pull/10582)
  - Fixed template conversion for Llama 4 models in Bedrock - [PR](https://github.com/BerriAI/litellm/pull/10582)
  - Added support for using Bedrock Anthropic models with /v1/messages format - [PR](https://github.com/BerriAI/litellm/pull/10681)
  - Added streaming support for Bedrock Anthropic models with /v1/messages format - [PR](https://github.com/BerriAI/litellm/pull/10710)
- [**OpenAI**](https://docs.litellm.ai/docs/providers/openai): Added `reasoning_effort` support for `o3` models - [PR](https://github.com/BerriAI/litellm/pull/10591)
- [**Databricks**](https://docs.litellm.ai/docs/providers/databricks):
  
  - Fixed issue when Databricks uses external model and delta could be empty - [PR](https://github.com/BerriAI/litellm/pull/10540)
- [**Cerebras**](https://docs.litellm.ai/docs/providers/cerebras): Fixed Llama-3.1-70b model pricing and context window - [PR](https://github.com/BerriAI/litellm/pull/10648)
- [**Ollama**](https://docs.litellm.ai/docs/providers/ollama):
  
  - Fixed custom price cost tracking and added 'max\_completion\_token' support - [PR](https://github.com/BerriAI/litellm/pull/10636)
  - Fixed KeyError when using JSON response format - [PR](https://github.com/BerriAI/litellm/pull/10611)
- 🆕 [**Nscale**](https://docs.litellm.ai/docs/providers/nscale):
  
  - Added support for chat, image generation endpoints - [PR](https://github.com/BerriAI/litellm/pull/10638)

## LLM API Endpoints[​](#llm-api-endpoints "Direct link to LLM API Endpoints")

- [**Messages API**](https://docs.litellm.ai/docs/anthropic_unified):
  
  - 🆕 Added support for using Bedrock Anthropic models with /v1/messages format - [PR](https://github.com/BerriAI/litellm/pull/10681) and streaming support - [PR](https://github.com/BerriAI/litellm/pull/10710)
- [**Moderations API**](https://docs.litellm.ai/docs/moderations):
  
  - Fixed bug to allow using LiteLLM UI credentials for /moderations API - [PR](https://github.com/BerriAI/litellm/pull/10723)
- [**Realtime API**](https://docs.litellm.ai/docs/realtime):
  
  - Fixed setting 'headers' in scope for websocket auth requests and infinite loop issues - [PR](https://github.com/BerriAI/litellm/pull/10679)
- [**Files API**](https://docs.litellm.ai/docs/proxy/litellm_managed_files):
  
  - Unified File ID output support - [PR](https://github.com/BerriAI/litellm/pull/10713)
  - Support for writing files to all deployments - [PR](https://github.com/BerriAI/litellm/pull/10708)
  - Added target model name validation - [PR](https://github.com/BerriAI/litellm/pull/10722)
- [**Batches API**](https://docs.litellm.ai/docs/batches):
  
  - Complete unified batch ID support - replacing model in jsonl to be deployment model name - [PR](https://github.com/BerriAI/litellm/pull/10719)
  - Beta support for unified file ID (managed files) for batches - [PR](https://github.com/BerriAI/litellm/pull/10650)

## Spend Tracking / Budget Improvements[​](#spend-tracking--budget-improvements "Direct link to Spend Tracking / Budget Improvements")

- Bug Fix - PostgreSQL Integer Overflow Error in DB Spend Tracking - [PR](https://github.com/BerriAI/litellm/pull/10697)

## Management Endpoints / UI[​](#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Models**
  
  - Fixed model info overwriting when editing a model on UI - [PR](https://github.com/BerriAI/litellm/pull/10726)
  - Fixed team admin model updates and organization creation with specific models - [PR](https://github.com/BerriAI/litellm/pull/10539)
- **Logs**:
  
  - Bug Fix - copying Request/Response on Logs Page - [PR](https://github.com/BerriAI/litellm/pull/10720)
  - Bug Fix - log did not remain in focus on QA Logs page + text overflow on error logs - [PR](https://github.com/BerriAI/litellm/pull/10725)
  - Added index for session\_id on LiteLLM\_SpendLogs for better query performance - [PR](https://github.com/BerriAI/litellm/pull/10727)
- **User Management**:
  
  - Added user management functionality to Python client library & CLI - [PR](https://github.com/BerriAI/litellm/pull/10627)
  - Bug Fix - Fixed SCIM token creation on Admin UI - [PR](https://github.com/BerriAI/litellm/pull/10628)
  - Bug Fix - Added 404 response when trying to delete verification tokens that don't exist - [PR](https://github.com/BerriAI/litellm/pull/10605)

## Logging / Guardrail Integrations[​](#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- **Custom Logger API**: v2 Custom Callback API (send llm logs to custom api) - [PR](https://github.com/BerriAI/litellm/pull/10575), [Get Started](https://docs.litellm.ai/docs/proxy/logging#custom-callback-apis-async)
- **OpenTelemetry**:
  
  - Fixed OpenTelemetry to follow genai semantic conventions + support for 'instructions' param for TTS - [PR](https://github.com/BerriAI/litellm/pull/10608)
- \** Bedrock PII\*\*:
  
  - Add support for PII Masking with bedrock guardrails - [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/bedrock#pii-masking-with-bedrock-guardrails), [PR](https://github.com/BerriAI/litellm/pull/10608)
- **Documentation**:
  
  - Added documentation for StandardLoggingVectorStoreRequest - [PR](https://github.com/BerriAI/litellm/pull/10535)

## Performance / Reliability Improvements[​](#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

- **Python Compatibility**:
  
  - Added support for Python 3.11- (fixed datetime UTC handling) - [PR](https://github.com/BerriAI/litellm/pull/10701)
  - Fixed UnicodeDecodeError: 'charmap' on Windows during litellm import - [PR](https://github.com/BerriAI/litellm/pull/10542)
- **Caching**:
  
  - Fixed embedding string caching result - [PR](https://github.com/BerriAI/litellm/pull/10700)
  - Fixed cache miss for Gemini models with response\_format - [PR](https://github.com/BerriAI/litellm/pull/10635)

## General Proxy Improvements[​](#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Proxy CLI**:
  
  - Added `--version` flag to `litellm-proxy` CLI - [PR](https://github.com/BerriAI/litellm/pull/10704)
  - Added dedicated `litellm-proxy` CLI - [PR](https://github.com/BerriAI/litellm/pull/10578)
- **Alerting**:
  
  - Fixed Slack alerting not working when using a DB - [PR](https://github.com/BerriAI/litellm/pull/10370)
- **Email Invites**:
  
  - Added V2 Emails with fixes for sending emails when creating keys + Resend API support - [PR](https://github.com/BerriAI/litellm/pull/10602)
  - Added user invitation emails - [PR](https://github.com/BerriAI/litellm/pull/10615)
  - Added endpoints to manage email settings - [PR](https://github.com/BerriAI/litellm/pull/10646)
- **General**:
  
  - Fixed bug where duplicate JSON logs were getting emitted - [PR](https://github.com/BerriAI/litellm/pull/10580)

## New Contributors[​](#new-contributors "Direct link to New Contributors")

- [@zoltan-ongithub](https://github.com/zoltan-ongithub) made their first contribution in [PR #10568](https://github.com/BerriAI/litellm/pull/10568)
- [@mkavinkumar1](https://github.com/mkavinkumar1) made their first contribution in [PR #10548](https://github.com/BerriAI/litellm/pull/10548)
- [@thomelane](https://github.com/thomelane) made their first contribution in [PR #10549](https://github.com/BerriAI/litellm/pull/10549)
- [@frankzye](https://github.com/frankzye) made their first contribution in [PR #10540](https://github.com/BerriAI/litellm/pull/10540)
- [@aholmberg](https://github.com/aholmberg) made their first contribution in [PR #10591](https://github.com/BerriAI/litellm/pull/10591)
- [@aravindkarnam](https://github.com/aravindkarnam) made their first contribution in [PR #10611](https://github.com/BerriAI/litellm/pull/10611)
- [@xsg22](https://github.com/xsg22) made their first contribution in [PR #10648](https://github.com/BerriAI/litellm/pull/10648)
- [@casparhsws](https://github.com/casparhsws) made their first contribution in [PR #10635](https://github.com/BerriAI/litellm/pull/10635)
- [@hypermoose](https://github.com/hypermoose) made their first contribution in [PR #10370](https://github.com/BerriAI/litellm/pull/10370)
- [@tomukmatthews](https://github.com/tomukmatthews) made their first contribution in [PR #10638](https://github.com/BerriAI/litellm/pull/10638)
- [@keyute](https://github.com/keyute) made their first contribution in [PR #10652](https://github.com/BerriAI/litellm/pull/10652)
- [@GPTLocalhost](https://github.com/GPTLocalhost) made their first contribution in [PR #10687](https://github.com/BerriAI/litellm/pull/10687)
- [@husnain7766](https://github.com/husnain7766) made their first contribution in [PR #10697](https://github.com/BerriAI/litellm/pull/10697)
- [@claralp](https://github.com/claralp) made their first contribution in [PR #10694](https://github.com/BerriAI/litellm/pull/10694)
- [@mollux](https://github.com/mollux) made their first contribution in [PR #10690](https://github.com/BerriAI/litellm/pull/10690)