---
title: SigNoz LiteLLM Integration | liteLLM
url: https://docs.litellm.ai/docs/observability/signoz
source: sitemap
fetched_at: 2026-01-21T19:46:35.274792303-03:00
rendered_js: false
word_count: 707
summary: This guide explains how to integrate LiteLLM with SigNoz using OpenTelemetry to capture logs, traces, and metrics for AI applications. It provides step-by-step instructions for instrumenting the LiteLLM SDK to monitor model performance and system-level metrics.
tags:
    - litellm
    - signoz
    - opentelemetry
    - observability
    - llm-monitoring
    - tracing
category: guide
---

For more details on setting up observability for LiteLLM, check out the [SigNoz LiteLLM observability docs](https://signoz.io/docs/litellm-observability/).

## Overview[​](#overview "Direct link to Overview")

This guide walks you through setting up observability and monitoring for LiteLLM SDK and Proxy Server using [OpenTelemetry](https://opentelemetry.io/) and exporting logs, traces, and metrics to SigNoz. With this integration, you can observe various models performance, capture request/response details, and track system-level metrics in SigNoz, giving you real-time visibility into latency, error rates, and usage trends for your LiteLLM applications.

Instrumenting LiteLLM in your AI applications with telemetry ensures full observability across your AI workflows, making it easier to debug issues, optimize performance, and understand user interactions. By leveraging SigNoz, you can analyze correlated traces, logs, and metrics in unified dashboards, configure alerts, and gain actionable insights to continuously improve reliability, responsiveness, and user experience.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- A [SigNoz Cloud account](https://signoz.io/teams/) with an active ingestion key
- Internet access to send telemetry data to SigNoz Cloud
- [LiteLLM](https://www.litellm.ai/) SDK or Proxy integration
- For Python: `pip` installed for managing Python packages and *(optional but recommended)* a Python virtual environment to isolate dependencies

## Monitoring LiteLLM[​](#monitoring-litellm "Direct link to Monitoring LiteLLM")

LiteLLM can be monitored in two ways: using the **LiteLLM SDK** (directly embedded in your Python application code for programmatic LLM calls) or the **LiteLLM Proxy Server** (a standalone server that acts as a centralized gateway for managing and routing LLM requests across your infrastructure).

- LiteLLM SDK
- LiteLLM Proxy Server

For more detailed info on instrumenting your LiteLLM SDK applications click [here](https://docs.litellm.ai/docs/observability/opentelemetry_integration).

- No Code(Recommended)
- Code

No-code auto-instrumentation is recommended for quick setup with minimal code changes. It's ideal when you want to get observability up and running without modifying your application code and are leveraging standard instrumentor libraries.

**Step 1:** Install the necessary packages in your Python environment.

```
pip install \
  opentelemetry-api \
  opentelemetry-distro \
  opentelemetry-exporter-otlp \
  httpx \
  opentelemetry-instrumentation-httpx \
  litellm
```

**Step 2:** Add Automatic Instrumentation

```
opentelemetry-bootstrap --action=install
```

**Step 3:** Instrument your LiteLLM SDK application

Initialize LiteLLM SDK instrumentation by calling `litellm.callbacks = ["otel"]`:

```
from litellm import litellm

litellm.callbacks =["otel"]
```

This call enables automatic tracing, logs, and metrics collection for all LiteLLM SDK calls in your application.

> 📌 Note: Ensure this is called before any LiteLLM related calls to properly configure instrumentation of your application

**Step 4:** Run an example

```
from litellm import completion, litellm

litellm.callbacks =["otel"]

response = completion(
  model="openai/gpt-4o",
  messages=[{"content":"What is SigNoz","role":"user"}]
)

print(response)
```

> 📌 Note: LiteLLM supports a [variety of model providers](https://docs.litellm.ai/docs/providers) for LLMs. In this example, we're using OpenAI. Before running this code, ensure that you have set the environment variable `OPENAI_API_KEY` with your generated API key.

**Step 5:** Run your application with auto-instrumentation

```
OTEL_RESOURCE_ATTRIBUTES="service.name=<service_name>" \
OTEL_EXPORTER_OTLP_ENDPOINT="https://ingest.<region>.signoz.cloud:443" \
OTEL_EXPORTER_OTLP_HEADERS="signoz-ingestion-key=<your_ingestion_key>" \
OTEL_EXPORTER_OTLP_PROTOCOL=grpc \
OTEL_TRACES_EXPORTER=otlp \
OTEL_METRICS_EXPORTER=otlp \
OTEL_LOGS_EXPORTER=otlp \
OTEL_PYTHON_LOG_CORRELATION=true \
OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true \
OTEL_PYTHON_DISABLED_INSTRUMENTATIONS=openai \
opentelemetry-instrument <your_run_command>
```

> 📌 Note: We're using `OTEL_PYTHON_DISABLED_INSTRUMENTATIONS=openai` in the run command to disable the OpenAI instrumentor for tracing. This avoids conflicts with LiteLLM's native telemetry/instrumentation, ensuring that telemetry is captured exclusively through LiteLLM's built-in instrumentation.

- **`<service_name>`**  is the name of your service
- Set the `<region>` to match your SigNoz Cloud [region](https://signoz.io/docs/ingestion/signoz-cloud/overview/#endpoint)
- Replace `<your_ingestion_key>` with your SigNoz [ingestion key](https://signoz.io/docs/ingestion/signoz-cloud/keys/)
- Replace `<your_run_command>` with the actual command you would use to run your application. For example: `python main.py`

> 📌 Note: Using self-hosted SigNoz? Most steps are identical. To adapt this guide, update the endpoint and remove the ingestion key header as shown in [Cloud → Self-Hosted](https://signoz.io/docs/ingestion/cloud-vs-self-hosted/#cloud-to-self-hosted).

## View Traces, Logs, and Metrics in SigNoz[​](#view-traces-logs-and-metrics-in-signoz "Direct link to View Traces, Logs, and Metrics in SigNoz")

Your LiteLLM commands should now automatically emit traces, logs, and metrics.

You should be able to view traces in Signoz Cloud under the traces tab:

![LiteLLM SDK Trace View](https://signoz.io/img/docs/llm/litellm/litellmsdk-traces.webp)

When you click on a trace in SigNoz, you'll see a detailed view of the trace, including all associated spans, along with their events and attributes.

![LiteLLM SDK Detailed Trace View](https://signoz.io/img/docs/llm/litellm/litellmsdk-detailed-traces.webp)

You should be able to view logs in Signoz Cloud under the logs tab. You can also view logs by clicking on the “Related Logs” button in the trace view to see correlated logs:

![LiteLLM SDK Logs View](https://signoz.io/img/docs/llm/litellm/litellmsdk-logs.webp)

When you click on any of these logs in SigNoz, you'll see a detailed view of the log, including attributes:

![LiteLLM SDK Detailed Logs View](https://signoz.io/img/docs/llm/litellm/litellmsdk-detailed-logs.webp)

You should be able to see LiteLLM related metrics in Signoz Cloud under the metrics tab:

![LiteLLM SDK Metrics View](https://signoz.io/img/docs/llm/litellm/litellmsdk-metrics.webp)

When you click on any of these metrics in SigNoz, you'll see a detailed view of the metric, including attributes:

![LiteLLM Detailed Metrics View](https://signoz.io/img/docs/llm/litellm/litellmsdk-detailed-metrics.webp)

## Dashboard[​](#dashboard "Direct link to Dashboard")

You can also check out our custom LiteLLM SDK dashboard [here](https://signoz.io/docs/dashboards/dashboard-templates/litellm-sdk-dashboard/) which provides specialized visualizations for monitoring your LiteLLM usage in applications. The dashboard includes pre-built charts specifically tailored for LLM usage, along with import instructions to get started quickly.

![LiteLLM SDK Dashboard Template](https://signoz.io/img/docs/llm/litellm/litellm-sdk-dashboard.webp)