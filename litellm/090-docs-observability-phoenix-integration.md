---
title: Arize Phoenix OSS | liteLLM
url: https://docs.litellm.ai/docs/observability/phoenix_integration
source: sitemap
fetched_at: 2026-01-21T19:46:26.690017865-03:00
rendered_js: false
word_count: 204
summary: This document provides instructions for integrating LiteLLM with Arize Phoenix to enable tracing and evaluation of LLM interactions via callbacks and proxy configurations.
tags:
    - litellm
    - arize-phoenix
    - tracing
    - observability
    - llm-ops
    - python
    - integration
category: guide
---

Open source tracing and evaluation platform

## Pre-Requisites[​](#pre-requisites "Direct link to Pre-Requisites")

Make an account on [Phoenix OSS](https://phoenix.arize.com) OR self-host your own instance of [Phoenix](https://docs.arize.com/phoenix/deployment)

## Quick Start[​](#quick-start "Direct link to Quick Start")

Use just 2 lines of code, to instantly log your responses **across all providers** with Phoenix

You can also use the instrumentor option instead of the callback, which you can find [here](https://docs.arize.com/phoenix/tracing/integrations-tracing/litellm).

```
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp litellm[proxy]
```

```
litellm.callbacks =["arize_phoenix"]
```

```
import litellm
import os

# Set env variables
os.environ["PHOENIX_API_KEY"]="d0*****"# Set the Phoenix API key here. It is necessary only when using Phoenix Cloud.
os.environ["PHOENIX_COLLECTOR_HTTP_ENDPOINT"]="https://app.phoenix.arize.com/s/<space-name>/v1/traces"# Set the URL of your Phoenix OSS instance, otherwise tracer would use https://app.phoenix.arize.com/v1/traces for Phoenix Cloud.
os.environ["PHOENIX_PROJECT_NAME"]="litellm"# Configure the project name, otherwise traces would go to "default" project.
os.environ['OPENAI_API_KEY']="fake-key"# Set the OpenAI API key here.

# Set arize_phoenix as a callback & LiteLLM will send the data to Phoenix.
litellm.callbacks =["arize_phoenix"]

# OpenAI call
response = litellm.completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
]
)
```

## Using with LiteLLM Proxy[​](#using-with-litellm-proxy "Direct link to Using with LiteLLM Proxy")

1. Setup config.yaml

```
model_list:
-model_name: gpt-4o
litellm_params:
model: openai/fake
api_key: fake-key
api_base: https://exampleopenaiendpoint-production.up.railway.app/

litellm_settings:
callbacks:["arize_phoenix"]

general_settings:
master_key:"sk-1234"

environment_variables:
PHOENIX_API_KEY:"d0*****"
PHOENIX_COLLECTOR_ENDPOINT:"https://app.phoenix.arize.com/s/<space-name>/v1/traces"# OPTIONAL - For setting the gRPC endpoint
PHOENIX_COLLECTOR_HTTP_ENDPOINT:"https://app.phoenix.arize.com/s/<space-name>/v1/traces"# OPTIONAL - For setting the HTTP endpoint
```

2. Start the proxy

```
litellm --config config.yaml
```

3. Test it!

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{ "model": "gpt-4o", "messages": [{"role": "user", "content": "Hi 👋 - i'm openai"}]}'
```

## Supported Phoenix Endpoints[​](#supported-phoenix-endpoints "Direct link to Supported Phoenix Endpoints")

Phoenix now supports multiple deployment types. The correct endpoint depends on which version of Phoenix Cloud you are using.

**Phoenix Cloud (With Spaces - New Version)** Use this if your Phoenix URL contains `/s/<space-name>` path.

```
https://app.phoenix.arize.com/s/<space-name>/v1/traces
```

**Phoenix Cloud (Legacy - Deprecated)** Use this only if your deployment still shows the `/legacy` pattern.

```
https://app.phoenix.arize.com/legacy/v1/traces
```

**Phoenix Cloud (Without Spaces - Old Version)** Use this if your Phoenix Cloud URL does not contain `/s/<space-name>` or `/legacy` path.

```
https://app.phoenix.arize.com/v1/traces
```

**Self-Hosted Phoenix (Local Instance)** Use this when running Phoenix on your machine or a private server.

```
http://localhost:6006/v1/traces
```

Depending on which Phoenix Cloud version or deployment you are using, you should set the corresponding endpoint in `PHOENIX_COLLECTOR_HTTP_ENDPOINT` or `PHOENIX_COLLECTOR_ENDPOINT`.

## Support & Talk to Founders[​](#support--talk-to-founders "Direct link to Support & Talk to Founders")

- [Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)
- [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
- Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
- Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)