---
title: AWS Bedrock | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock
source: crawler
fetched_at: 2026-04-24T17:00:22.351681309-03:00
rendered_js: false
word_count: 454
summary: This document details how Hermes Agent integrates natively with Amazon Bedrock via the Converse API, outlining prerequisites like AWS credentials and permissions, and providing guides on configuration for regions, guardrails, and model discovery.
tags:
    - bedrock-integration
    - hermes-agent
    - aws-setup
    - configuration
    - model-discovery
    - api-usage
category: guide
---

Hermes Agent supports Amazon Bedrock as a native provider using the **Converse API** — not the OpenAI-compatible endpoint. This gives you full access to the Bedrock ecosystem: IAM authentication, Guardrails, cross-region inference profiles, and all foundation models.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- **AWS credentials** — any source supported by the [boto3 credential chain](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html):
  
  - IAM instance role (EC2, ECS, Lambda — zero config)
  - `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY` environment variables
  - `AWS_PROFILE` for SSO or named profiles
  - `aws configure` for local development
- **boto3** — install with `pip install hermes-agent[bedrock]`
- **IAM permissions** — at minimum:
  
  - `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` (for inference)
  - `bedrock:ListFoundationModels` and `bedrock:ListInferenceProfiles` (for model discovery)

EC2 / ECS / Lambda

On AWS compute, attach an IAM role with `AmazonBedrockFullAccess` and you're done. No API keys, no `.env` configuration — Hermes detects the instance role automatically.

## Quick Start[​](#quick-start "Direct link to Quick Start")

```bash
# Install with Bedrock support
pip install hermes-agent[bedrock]

# Select Bedrock as your provider
hermes model
# → Choose "More providers..." → "AWS Bedrock"
# → Select your region and model

# Start chatting
hermes chat
```

## Configuration[​](#configuration "Direct link to Configuration")

After running `hermes model`, your `~/.hermes/config.yaml` will contain:

```yaml
model:
default: us.anthropic.claude-sonnet-4-6
provider: bedrock
base_url: https://bedrock-runtime.us-east-2.amazonaws.com

bedrock:
region: us-east-2
```

### Region[​](#region "Direct link to Region")

Set the AWS region in any of these ways (highest priority first):

1. `bedrock.region` in `config.yaml`
2. `AWS_REGION` environment variable
3. `AWS_DEFAULT_REGION` environment variable
4. Default: `us-east-1`

### Guardrails[​](#guardrails "Direct link to Guardrails")

To apply [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to all model invocations:

```yaml
bedrock:
region: us-east-2
guardrail:
guardrail_identifier:"abc123def456"# From the Bedrock console
guardrail_version:"1"# Version number or "DRAFT"
stream_processing_mode:"async"# "sync" or "async"
trace:"disabled"# "enabled", "disabled", or "enabled_full"
```

### Model Discovery[​](#model-discovery "Direct link to Model Discovery")

Hermes auto-discovers available models via the Bedrock control plane. You can customize discovery:

```yaml
bedrock:
discovery:
enabled:true
provider_filter:["anthropic","amazon"]# Only show these providers
refresh_interval:3600# Cache for 1 hour
```

## Available Models[​](#available-models "Direct link to Available Models")

Bedrock models use **inference profile IDs** for on-demand invocation. The `hermes model` picker shows these automatically, with recommended models at the top:

ModelIDNotesClaude Sonnet 4.6`us.anthropic.claude-sonnet-4-6`Recommended — best balance of speed and capabilityClaude Opus 4.6`us.anthropic.claude-opus-4-6-v1`Most capableClaude Haiku 4.5`us.anthropic.claude-haiku-4-5-20251001-v1:0`Fastest ClaudeAmazon Nova Pro`us.amazon.nova-pro-v1:0`Amazon's flagshipAmazon Nova Micro`us.amazon.nova-micro-v1:0`Fastest, cheapestDeepSeek V3.2`deepseek.v3.2`Strong open modelLlama 4 Scout 17B`us.meta.llama4-scout-17b-instruct-v1:0`Meta's latest

Cross-Region Inference

Models prefixed with `us.` use cross-region inference profiles, which provide better capacity and automatic failover across AWS regions. Models prefixed with `global.` route across all available regions worldwide.

## Switching Models Mid-Session[​](#switching-models-mid-session "Direct link to Switching Models Mid-Session")

Use the `/model` command during a conversation:

```text
/model us.amazon.nova-pro-v1:0
/model deepseek.v3.2
/model us.anthropic.claude-opus-4-6-v1
```

## Diagnostics[​](#diagnostics "Direct link to Diagnostics")

The doctor checks:

- Whether AWS credentials are available (env vars, IAM role, SSO)
- Whether `boto3` is installed
- Whether the Bedrock API is reachable (ListFoundationModels)
- Number of available models in your region

## Gateway (Messaging Platforms)[​](#gateway-messaging-platforms "Direct link to Gateway (Messaging Platforms)")

Bedrock works with all Hermes gateway platforms (Telegram, Discord, Slack, Feishu, etc.). Configure Bedrock as your provider, then start the gateway normally:

```bash
hermes gateway setup
hermes gateway start
```

The gateway reads `config.yaml` and uses the same Bedrock provider configuration.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### "No API key found" / "No AWS credentials"[​](#no-api-key-found--no-aws-credentials 'Direct link to "No API key found" / "No AWS credentials"')

Hermes checks for credentials in this order:

1. `AWS_BEARER_TOKEN_BEDROCK`
2. `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY`
3. `AWS_PROFILE`
4. EC2 instance metadata (IMDS)
5. ECS container credentials
6. Lambda execution role

If none are found, run `aws configure` or attach an IAM role to your compute instance.

### "Invocation of model ID ... with on-demand throughput isn't supported"[​](#invocation-of-model-id--with-on-demand-throughput-isnt-supported "Direct link to \"Invocation of model ID ... with on-demand throughput isn't supported\"")

Use an **inference profile ID** (prefixed with `us.` or `global.`) instead of the bare foundation model ID. For example:

- ❌ `anthropic.claude-sonnet-4-6`
- ✅ `us.anthropic.claude-sonnet-4-6`

### "ThrottlingException"[​](#throttlingexception 'Direct link to "ThrottlingException"')

You've hit the Bedrock per-model rate limit. Hermes automatically retries with backoff. To increase limits, request a quota increase in the [AWS Service Quotas console](https://console.aws.amazon.com/servicequotas/).