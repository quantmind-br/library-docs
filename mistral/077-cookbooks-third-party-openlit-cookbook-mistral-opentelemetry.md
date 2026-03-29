---
title: Monitoring Mistral AI with OpenTelemetry - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-openlit-cookbook_mistral_opentelemetry
source: crawler
fetched_at: 2026-01-29T07:33:53.435905894-03:00
rendered_js: false
word_count: 446
summary: A guide on how to implement observability and monitoring for Mistral AI applications using the OpenTelemetry framework.
tags:
    - Mistral AI
    - OpenTelemetry
    - monitoring
    - observability
    - LLM
category: guide
---

This cookbook will cover the process of integrating OpenLIT with the Mistral SDK. A straightforward guide demonstrates how adding a single line of code can seamlessly enable OpenLIT to track various metrics, including cost, tokens, prompts, responses, and all chat/completion activities from the Mistral SDK using OpenTelemetry.

## About OpenLIT

**OpenLIT** is an open-source AI Engineering tool that help you to simplify your AI development workflow, especially for Generative AI and LLMs. It streamlines essential tasks like experimenting with LLMs, organizing and versioning prompts, and securely handling API keys. With just one line of code, you can enable **OpenTelemetry-native** observability, offering full-stack monitoring that includes LLMs, vector databases, and GPUs. This enables developers to confidently build AI features and applications, transitioning smoothly from testing to production.

This project proudly follows and maintains the [Semantic Conventions](https://github.com/open-telemetry/semantic-conventions/tree/main/docs/gen-ai) with the OpenTelemetry community, consistently updating to align with the latest standards in Observability.

Set your Mistral API key as an environment variable. If you haven't already, [sign up for a Mistral acccount](https://console.mistral.ai/). Then [subscribe](https://console.mistral.ai/billing/) to a free trial or billing plan, after which you'll be able to [generate an API key](https://console.mistral.ai/api-keys/).

## Chat Completions

Once OpenLIT is initialized in the application, It auto-instruments all Mistral Chat function usage from the SDK. This helps track LLM interactions, capturing inputs, outputs, model parameters along with cost.

## Embeddings

Once OpenLIT is initialized in the application, It auto-instruments all Mistral embedding function usage from the SDK. This helps track embedding inputs, outputs, model parameters along with cost.

## Sending Traces and metrics to OpenLIT

By default, OpenLIT generates OpenTelemetry traces and metrics that are logged to your console. To set up a detailed monitoring environment, this guide outlines how to deploy OpenLIT and direct all traces and metrics there. You also have the flexibility to send the telemetry data to any OpenTelemetry-compatible endpoint, such as Grafana, Jaeger, or DataDog.

## Deploy OpenLIT Stack

1. Clone the OpenLIT Repository
   
   Open your terminal or command line and execute:
2. Host it Yourself with Docker
   
   Deploy and start OpenLIT using the command:

> For instructions on installing in Kubernetes using Helm, refer to the [Kubernetes Helm installation guide](https://docs.openlit.io/latest/installation#kubernetes).

Configure the telemetry data destination as follows:

> 💡 Info: If the `otlp_endpoint` or `OTEL_EXPORTER_OTLP_ENDPOINT` is not provided, the OpenLIT SDK will output traces directly to your console, which is recommended during the development phase.

## Visualize and Optimize!

With the Observability data now being collected and sent to OpenLIT, the next step is to visualize and analyze this data to get insights into your AI application's performance, behavior, and identify areas of improvement.

Just head over to OpenLIT at `127.0.0.1:3000` on your browser to start exploring. You can login using the default credentials

- **Email**: `user@openlit.io`
- **Password**: `openlituser`

![](https://github.com/openlit/.github/blob/main/profile/assets/openlit-client-1.png?raw=true) ![](https://github.com/openlit/.github/blob/main/profile/assets/openlit-client-2.png?raw=true)