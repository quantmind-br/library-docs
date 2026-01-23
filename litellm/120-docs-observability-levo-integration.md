---
title: Levo AI | liteLLM
url: https://docs.litellm.ai/docs/observability/levo_integration
source: sitemap
fetched_at: 2026-01-21T19:46:15.867829984-03:00
rendered_js: false
word_count: 392
summary: This document explains how to integrate the Levo AI observability platform with LiteLLM to enable monitoring, compliance tracking, and performance metrics for LLM applications. It provides setup instructions, configuration details, and troubleshooting steps for sending trace data via OpenTelemetry.
tags:
    - levo
    - litellm
    - observability
    - opentelemetry
    - llm-monitoring
    - compliance
    - tracing
category: guide
---

[Levo](https://levo.ai/) is an AI observability and compliance platform that provides comprehensive monitoring, analysis, and compliance tracking for LLM applications.

## Quick Start[​](#quick-start "Direct link to Quick Start")

Send all your LLM requests and responses to Levo for monitoring and analysis using LiteLLM's built-in Levo integration.

### What You'll Get[​](#what-youll-get "Direct link to What You'll Get")

- **Complete visibility** into all LLM API calls across all providers
- **Request and response data** including prompts, completions, and metadata
- **Usage and cost tracking** with token counts and cost breakdowns
- **Error monitoring** and performance metrics
- **Compliance tracking** for audit and governance

### Setup Steps[​](#setup-steps "Direct link to Setup Steps")

**1. Install OpenTelemetry dependencies:**

```
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http opentelemetry-exporter-otlp-proto-grpc
```

**2. Enable Levo callback in your LiteLLM config:**

Add to your `litellm_config.yaml`:

```
litellm_settings:
callbacks:["levo"]
```

**3. Configure environment variables:**

[Contact Levo support](mailto:support@levo.ai) to get your collector endpoint URL, API key, organization ID, and workspace ID.

Set these required environment variables:

```
export LEVOAI_API_KEY="<your-levo-api-key>"
export LEVOAI_ORG_ID="<your-levo-org-id>"
export LEVOAI_WORKSPACE_ID="<your-workspace-id>"
export LEVOAI_COLLECTOR_URL="<your-levo-collector-url>"
```

**Note:** The collector URL should be the full endpoint URL provided by Levo support. It will be used exactly as provided.

**4. Start LiteLLM:**

```
litellm --config config.yaml
```

**5. Make requests - they'll automatically be sent to Levo!**

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
    --header 'Content-Type: application/json' \
    --data '{
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": "Hello, this is a test message"
        }
    ]
    }'
```

## What Data is Captured[​](#what-data-is-captured "Direct link to What Data is Captured")

FeatureDetails**What is logged**OpenTelemetry Trace Data (OTLP format)**Events**Success + Failure**Format**OTLP (OpenTelemetry Protocol)**Headers**Automatically includes `Authorization: Bearer {LEVOAI_API_KEY}`, `x-levo-organization-id`, and `x-levo-workspace-id`

## Configuration Reference[​](#configuration-reference "Direct link to Configuration Reference")

### Required Environment Variables[​](#required-environment-variables "Direct link to Required Environment Variables")

VariableDescriptionExample`LEVOAI_API_KEY`Your Levo API key`levo_abc123...``LEVOAI_ORG_ID`Your Levo organization ID`org-123456``LEVOAI_WORKSPACE_ID`Your Levo workspace ID`workspace-789``LEVOAI_COLLECTOR_URL`Full collector endpoint URL from Levo support`https://collector.levo.ai/v1/traces`

### Optional Environment Variables[​](#optional-environment-variables "Direct link to Optional Environment Variables")

VariableDescriptionDefault`LEVOAI_ENV_NAME`Environment name for tagging traces`None`

**Note:** The collector URL is used exactly as provided by Levo support. No path manipulation is performed.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Not seeing traces in Levo?[​](#not-seeing-traces-in-levo "Direct link to Not seeing traces in Levo?")

1. **Verify Levo callback is enabled**: Check LiteLLM startup logs for `initializing callbacks=['levo']`
2. **Check required environment variables**: Ensure all required variables are set:
   
   ```
   echo $LEVOAI_API_KEY
   echo $LEVOAI_ORG_ID
   echo $LEVOAI_WORKSPACE_ID
   echo $LEVOAI_COLLECTOR_URL
   ```
3. **Verify collector connectivity**: Test if your collector is reachable:
   
   ```
   curl <your-collector-url>/health
   ```
4. **Check for initialization errors**: Look for errors in LiteLLM startup logs. Common issues:
   
   - Missing OpenTelemetry packages: Install with `pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http opentelemetry-exporter-otlp-proto-grpc`
   - Missing required environment variables: All four required variables must be set
   - Invalid collector URL: Ensure the URL is correct and reachable
5. **Enable debug logging**:
   
   ```
   export LITELLM_LOG="DEBUG"
   ```
6. **Wait for async export**: OTLP sends traces asynchronously. Wait 10-15 seconds after making requests before checking Levo.

### Common Errors[​](#common-errors "Direct link to Common Errors")

**Error: "LEVOAI\_COLLECTOR\_URL environment variable is required"**

- Solution: Set the `LEVOAI_COLLECTOR_URL` environment variable with your collector endpoint URL from Levo support.

**Error: "No module named 'opentelemetry'"**

- Solution: Install OpenTelemetry packages: `pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http opentelemetry-exporter-otlp-proto-grpc`

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Levo Documentation](https://docs.levo.ai)
- [OpenTelemetry Specification](https://opentelemetry.io/docs/specs/otel/)

## Need Help?[​](#need-help "Direct link to Need Help?")

For issues or questions about the Levo integration with LiteLLM, please [contact Levo support](mailto:support@levo.ai) or open an issue on the [LiteLLM GitHub repository](https://github.com/BerriAI/litellm/issues).