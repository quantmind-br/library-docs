---
title: Structured Data Extraction Service Observability with Mistral AI and Phoenix - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-phoenix-arize_phoenix_tracing
source: crawler
fetched_at: 2026-01-29T07:34:05.80649023-03:00
rendered_js: false
word_count: 547
---

In this tutorial, you will:

- Use Mistral's [tool calling feature](https://docs.mistral.ai/guides/function-calling/) to perform structured data extraction: the task of transforming unstructured input (e.g., user requests in natural language) into structured format (e.g., tabular format),
- Instrument your Mistral AI client to record trace data in [OpenInference tracing](https://github.com/Arize-ai/openinference) format,
- Inspect the traces and spans of your application to visualize your trace data,

## Background

One powerful feature of the Mistral AI chat completions API is tool calling, wherein a user describes the signature and arguments of one or more tools to the Mistral AI API via a JSON Schema and natural language descriptions, and the LLM decides when to use each tool and provides argument values depending on the context of the conversation. In addition to its primary purpose of integrating function inputs and outputs into a sequence of chat messages, tool calling is also useful for structured data extraction, since you can specify a "function" that describes the desired format of your structured output. Structured data extraction is useful for a variety of purposes, including ETL or as input to another machine learning model such as a recommender system.

While it's possible to produce structured output without using tool calling via careful prompting, tool calling is more reliable at producing output that conforms to a particular format. For more details on Mistral AI's tool calling API, see the [Mistral AI documentation](https://docs.mistral.ai/guides/function-calling/).

Let's get started!

ℹ️ This notebook requires a Mistral AI API key.

## 1. Install Dependencies and Import Libraries

Install dependencies.

Import libraries.

## 2. Configure Your Mistral API Key

Set your Mistral API key if it is not already set as an environment variable.

## 3. Run Phoenix in the Background

Launch Phoenix as a background session to collect the trace data emitted by your instrumented Mistral client. For details on how to self-host Phoenix or connect to a remote Phoenix instance, see the [Phoenix documentation](https://docs.arize.com/phoenix/quickstart).

## 4. Instrument Your Mistral Client

Instrument your Mistral client with a tracer that emits telemetry data in OpenInference format. [OpenInference](https://github.com/Arize-ai/openinference) is an open standard for capturing and storing LLM application traces that enables LLM applications to seamlessly integrate with LLM observability solutions such as Phoenix.

We'll extract structured data from the following list of ten travel requests.

The Mistral AI API uses [JSON Schema](https://json-schema.org/) and natural language descriptions to specify the signature of a function to call. In this case, we'll describe a function to record the following attributes of the unstructured text input:

- **location:** The desired destination,
- **budget\_level:** A categorical budget preference,
- **purpose:** The purpose of the trip.

The use of JSON Schema enables us to define the type of each field in the output and even enumerate valid values in the case of categorical outputs. Mistral AI tool calling can thus be used for tasks that might previously have been performed by named-entity recognition (NER) and/ or classification models.

Run the extractions.

## 6. View traces in Phoenix

You should now be able to view traces in Phoenix.

![Traces](https://docs.mistral.ai/cookbooks/third_party/Phoenix/images/traces-1.png)

## 7. Export Your Trace Data

Your OpenInference trace data is collected by Phoenix and can be exported to a pandas dataframe for further analysis and evaluation.

## 8. Recap

Congrats! In this tutorial, you:

- Built a service to perform structured data extraction on unstructured text using Mistral AI tool calling
- Instrumented your service with an OpenInference tracer
- Examined your telemetry data in Phoenix