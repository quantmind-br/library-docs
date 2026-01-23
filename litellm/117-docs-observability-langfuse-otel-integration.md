---
title: "\U0001FAA2 Langfuse OpenTelemetry Integration | liteLLM"
url: https://docs.litellm.ai/docs/observability/langfuse_otel_integration
source: sitemap
fetched_at: 2026-01-21T19:46:12.857718636-03:00
rendered_js: false
word_count: 473
summary: This document provides a comprehensive guide for integrating Langfuse with LiteLLM using the OpenTelemetry protocol to collect and analyze LLM trace and observability data.
tags:
    - langfuse
    - opentelemetry
    - litellm
    - observability
    - llm-tracing
    - otel-integration
    - python
category: guide
---

The Langfuse OpenTelemetry integration allows you to send LiteLLM traces and observability data to Langfuse using the OpenTelemetry protocol. This provides a standardized way to collect and analyze your LLM usage data.

## Features[​](#features "Direct link to Features")

- Automatic trace collection for all LiteLLM requests
- Support for Langfuse Cloud (EU and US regions)
- Support for self-hosted Langfuse instances
- Custom endpoint configuration
- Secure authentication using Basic Auth
- Consistent attribute mapping with other OTEL integrations

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

1. **Langfuse Account**: Sign up at [Langfuse Cloud](https://cloud.langfuse.com) or set up a self-hosted instance
2. **API Keys**: Get your public and secret keys from your Langfuse project settings
3. **Dependencies**: Install required packages:
   
   ```
   pip install litellm opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp
   ```

## Configuration[​](#configuration "Direct link to Configuration")

### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

VariableRequiredDescriptionExample`LANGFUSE_PUBLIC_KEY`YesYour Langfuse public key`pk-lf-...``LANGFUSE_SECRET_KEY`YesYour Langfuse secret key`sk-lf-...``LANGFUSE_OTEL_HOST`NoOTEL endpoint host`https://otel.my-langfuse.com`

### Endpoint Resolution[​](#endpoint-resolution "Direct link to Endpoint Resolution")

The integration automatically constructs the OTEL endpoint from `LANGFUSE_OTEL_HOST`

- **Default (US)**: `https://us.cloud.langfuse.com/api/public/otel`
- **EU Region**: `https://cloud.langfuse.com/api/public/otel`
- **Self-hosted**: `{LANGFUSE_OTEL_HOST}/api/public/otel`

## Usage[​](#usage "Direct link to Usage")

### Basic Setup[​](#basic-setup "Direct link to Basic Setup")

```
import os
import litellm

# Set your Langfuse credentials
os.environ["LANGFUSE_PUBLIC_KEY"]="pk-lf-..."
os.environ["LANGFUSE_SECRET_KEY"]="sk-lf-..."

# Enable Langfuse OTEL integration
litellm.callbacks =["langfuse_otel"]

# Make LLM requests as usual
response = litellm.completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Hello!"}]
)
```

### Advanced Configuration[​](#advanced-configuration "Direct link to Advanced Configuration")

```
import os
import litellm

# Set your Langfuse credentials
os.environ["LANGFUSE_PUBLIC_KEY"]="pk-lf-..."
os.environ["LANGFUSE_SECRET_KEY"]="sk-lf-..."

# Use EU region
os.environ["LANGFUSE_OTEL_HOST"]="https://cloud.langfuse.com"# EU region
# os.environ["LANGFUSE_OTEL_HOST"] = "https://otel.my-langfuse.company.com"  # custom OTEL endpoint

# Or use self-hosted instance
# os.environ["LANGFUSE_OTEL_HOST"] = "https://my-langfuse.company.com"

litellm.callbacks =["langfuse_otel"]
```

### Manual OTEL Configuration[​](#manual-otel-configuration "Direct link to Manual OTEL Configuration")

If you need direct control over the OpenTelemetry configuration:

```
import os
import base64
import litellm

# Get keys for your project from the project settings page: https://cloud.langfuse.com
os.environ["LANGFUSE_PUBLIC_KEY"]="pk-lf-..."
os.environ["LANGFUSE_SECRET_KEY"]="sk-lf-..."
os.environ["LANGFUSE_OTEL_HOST"]="https://cloud.langfuse.com"# EU region
# os.environ["LANGFUSE_OTEL_HOST"] = "https://us.cloud.langfuse.com" # US region
# os.environ["LANGFUSE_OTEL_HOST"] = "https://otel.my-langfuse.company.com" # custom OTEL endpoint

LANGFUSE_AUTH = base64.b64encode(
f"{os.environ.get('LANGFUSE_PUBLIC_KEY')}:{os.environ.get('LANGFUSE_SECRET_KEY')}".encode()
).decode()

host = os.environ.get("LANGFUSE_OTEL_HOST")
os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"]= host +"/api/public/otel"
os.environ["OTEL_EXPORTER_OTLP_HEADERS"]=f"Authorization=Basic {LANGFUSE_AUTH}"

litellm.callbacks =["langfuse_otel"]
```

### With LiteLLM Proxy[​](#with-litellm-proxy "Direct link to With LiteLLM Proxy")

Add the integration to your proxy configuration:

1. Add the credentials to your environment variables

```
export LANGFUSE_PUBLIC_KEY="pk-lf-..."
export LANGFUSE_SECRET_KEY="sk-lf-..."
export LANGFUSE_OTEL_HOST="https://us.cloud.langfuse.com"  # Default US region
# export LANGFUSE_OTEL_HOST="https://otel.my-langfuse.company.com"  # custom OTEL endpoint
```

2. Setup config.yaml

```
# config.yaml
litellm_settings:
callbacks:["langfuse_otel"]
```

3. Run the proxy

```
litellm --config /path/to/config.yaml
```

## Data Collected[​](#data-collected "Direct link to Data Collected")

The integration automatically collects the following data:

- **Request Details**: Model, messages, parameters (temperature, max\_tokens, etc.)
- **Response Details**: Generated content, token usage, finish reason
- **Timing Information**: Request duration, time to first token
- **Metadata**: User ID, session ID, custom tags (if provided)
- **Error Information**: Exception details and stack traces (if errors occur)

All metadata fields available in the vanilla Langfuse integration are now **fully supported** when you use the OTEL integration.

- Any key you pass in the `metadata` dictionary (`generation_name`, `trace_id`, `session_id`, `tags`, and the rest) is exported as an OpenTelemetry span attribute.
- Attribute names are prefixed with `langfuse.` so you can filter or search for them easily in your observability backend. Examples: `langfuse.generation.name`, `langfuse.trace.id`, `langfuse.trace.session_id`.

### Passing Metadata – Example[​](#passing-metadata--example "Direct link to Passing Metadata – Example")

```
response = litellm.completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Hello!"}],
    metadata={
"generation_name":"welcome-message",
"trace_id":"trace-123",
"session_id":"sess-42",
"tags":["prod","beta-user"]
}
)
```

The resulting span will contain attributes similar to:

```
langfuse.generation.name   = "welcome-message"
langfuse.trace.id          = "trace-123"
langfuse.trace.session_id  = "sess-42"
langfuse.trace.tags        = ["prod", "beta-user"]
```

Use the **Langfuse UI** (Traces tab) to search, filter and analyse spans that contain the `langfuse.*` attributes. The OTEL exporter in this integration sends data directly to Langfuse’s OTLP HTTP endpoint; it is **not** intended for Grafana, Honeycomb, Datadog, or other generic OTEL back-ends.

## Authentication[​](#authentication "Direct link to Authentication")

The integration uses HTTP Basic Authentication with your Langfuse public and secret keys:

```
Authorization: Basic <base64(public_key:secret_key)>
```

This is automatically handled by the integration - you just need to provide the keys via environment variables.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Common Issues[​](#common-issues "Direct link to Common Issues")

1. **Missing Credentials Error**
   
   ```
   ValueError: LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY must be set
   ```
   
   **Solution**: Ensure both environment variables are set with valid keys.
2. **Connection Issues**
   
   - Check your internet connection
   - Verify the endpoint URL is correct
   - For self-hosted instances, ensure the `/api/public/otel` endpoint is accessible
3. **Authentication Errors**
   
   - Verify your public and secret keys are correct
   - Check that the keys belong to the same Langfuse project
   - Ensure the keys have the necessary permissions

### Debug Mode[​](#debug-mode "Direct link to Debug Mode")

Enable verbose logging to see detailed information:

- SDK
- PROXY

```
import litellm
litellm._turn_on_debug()
```

This will show:

- Endpoint resolution logic
- Authentication header creation
- OTEL trace submission details

<!--THE END-->

- [Langfuse Documentation](https://langfuse.com/docs)
- [Langfuse OpenTelemetry Guide](https://langfuse.com/docs/integrations/opentelemetry)
- [OpenTelemetry Python SDK](https://opentelemetry.io/docs/languages/python/)
- [LiteLLM Observability](https://docs.litellm.ai/docs/observability/)