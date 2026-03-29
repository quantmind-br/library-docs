---
title: Monitoring LlamaIndex + Mistral applications with PostHog and Langfuse - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-langfuse-cookbook_langfuse_posthog_llama_langfuse
source: crawler
fetched_at: 2026-01-29T07:33:55.180626587-03:00
rendered_js: false
word_count: 800
summary: A guide on integrating PostHog and Langfuse to monitor and trace LLM applications built using LlamaIndex and Mistral AI models.
tags:
    - Mistral AI
    - LlamaIndex
    - PostHog
    - Langfuse
    - Observability
    - Monitoring
category: guide
---

In this cookbook, we show you how to build a RAG application with [LlamaIndex](https://www.llamaindex.ai/), observe the steps with [Langfuse](https://langfuse.com/), and analyze the data in [PostHog](https://posthog.com/).

## What is Langfuse?

[Langfuse](https://langfuse.com/) is an open-source LLM engineering platform. It includes features such as [traces](https://langfuse.com/docs/tracing), [evals](https://langfuse.com/docs/scores/overview), and [prompt management](https://langfuse.com/docs/prompts/get-started) to help you debug and improve your LLM app.

## What is LlamaIndex?

LlamaIndex [(GitHub)](https://github.com/run-llama/llama_index) is a data framework designed to connect LLMs with external data sources. It helps structure, index, and query data effectively. This makes it easier for developers to build advanced LLM applications.

## What is PostHog?

[PostHog](https://posthog.com/) is a popular choice for product analytics. Combining Langfuse's LLM analytics with PostHog's product analytics makes it easy to answer questions about your app like:

- "What are my LLM costs by customer, model, and in total?"
- "Does interacting with LLM features correlate with other metrics (retention, usage, revenue, etc.)?"
- "How does the user feedback that I capture in Langfuse correlate with user behavior in PostHog?"

## **How to build a Simple RAG app with LlamaIndex and Mistral**

In this example, we create a chat app that answers questions about how to care for hedgehogs. LlamaIndex vectorizes a [hedgehog care guide](https://www.pro-igel.de/downloads/merkblaetter_engl/wildtier_engl.pdf) using the [Mistral 8x22B model](https://docs.mistral.ai/getting-started/models/). Then, all model generations are traced using Langfuse's [LLamaIndex integration](https://langfuse.com/docs/integrations/llama-index/get-started).

Lastly, the [PostHog integration](https://langfuse.com/docs/analytics/posthog) enables you to view detailed analytics about your hedgehog app directly in PostHog.

### Step 1: Set up LlamaIndex and Mistral

First, we set our Mistral API key as an environment variable. If you haven't already, [sign up for a Mistral acccount](https://console.mistral.ai/). Then [subscribe](https://console.mistral.ai/billing/) to a free trial or billing plan, after which you'll be able to [generate an API key](https://console.mistral.ai/api-keys/) (💡 You can use any other model supported by LlamaIndex; we just use Mistral in this cookbook).

Then, we use LlamaIndex to initialize both a Mistral language model and an embedding model. We then set these models in the LlamaIndex `Settings` object:

### Step 2: Initialize Langfuse

Next, we initialize the Langfuse client. [Sign up](https://cloud.langfuse.com/auth/sign-up) for Langfuse if you haven't already. Copy your [API keys](https://langfuse.com/faq/all/where-are-langfuse-api-keys) from your project settings and add them to your environment.

Lastly, we register Langfuse's `LlamaIndexCallbackHandler` in the LlamaIndex `Settings.callback_manager` at the root of the app.

Find out more about the Langfuse's LlamaIndex integration [here](https://langfuse.com/docs/integrations/llama-index/get-started).

### Step 3: Download data

We download the file we want to use for RAG. In this example, we use a [hedgehog care guide](https://www.pro-igel.de/downloads/merkblaetter_engl/wildtier_engl.pdf) pdf file to enable the language model to answer questions about caring for hedgehogs 🦔.

Next, we load the pdf using the LlamaIndex [`SimpleDirectoryReader`](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/).

### Step 4: Build RAG on the hedgehog doc

Next, we create vector embeddings of the hedgehog document using [`VectorStoreIndex`](https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index/) and then convert it into a [queryable engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/) to retrieve information based on queries.

Finally, to put everything together, we query the engine and print a response:

All steps of the LLM chain are now tracked in Langfuse.

Example trace in Langfuse: [https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/367db23d-5b03-446b-bc73-36e289596c00](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/367db23d-5b03-446b-bc73-36e289596c00)

![Example trace](https://docs.mistral.ai/cookbooks/third_party/Langfuse/images/integration-posthog-llamaindex-mistral.png)

### Step 5: (Optional) Implement user feedback to see how your application is performing

To monitor the quality of your hedgehog chat application, you can use [Langfuse Scores](https://langfuse.com/docs/scores/overview) to store user feedback (e.g. thumps up/down or comments). These scores can then be analysed in PostHog.

Scores are used to evaluate single observations or entire traces. You can create them via the annotation workflow in the Langfuse UI, run model-based evaluation or ingest via the SDK as we do it in this example.

To get the context of the current observation, we use the [`observe()` decorator](https://langfuse.com/docs/sdk/python/decorators) and apply it to the hedgehog\_helper() function.

### Step 6: See your data in PostHog

Finally, we connect PostHog to our Langfuse account. Below is a summary of the steps to take (or see the [docs](https://posthog.com/docs/ai-engineering/langfuse-posthog) for full details):

1. [Sign up](https://us.posthog.com/) for your free PostHog account if you haven't already
2. Copy both your project API key and host from your [project settings](https://us.posthog.com/project/settings/project-details).
3. In your [Langfuse dashboard](https://cloud.langfuse.com/), click on **Settings** and scroll down to the **Integrations** section to find the PostHog integration.
4. Click **Configure** and paste in your PostHog host and project API key (you can find these in your [PostHog project settings](https://us.posthog.com/settings/project)).
5. Click **Enabled** and then **Save**.

Langfuse will then begin exporting your data to PostHog once a day.

**Using the Langfuse dashboard template:**

Once you've installed the integration, [dashboard templates](https://posthog.com/docs/ai-engineering/langfuse-posthog#using-the-langfuse-dashboard-template) help you quickly set up relevant insights.

For our hedgehog chat application, we are using the template dashboard shown below. This enables you to analyze model cost, user feedback, and latency in PostHog.

To create your own dashboard from a template:

1. Go to the [dashboard](https://us.posthog.com/dashboard) tab in PostHog.
2. Click the **New dashboard** button in the top right.
3. Select **LLM metrics – Langfuse** from the list of templates.

![Posthog Dashboard 1](https://docs.mistral.ai/cookbooks/third_party/Langfuse/images/dashboard-posthog-1.png)

![Posthog Dashboard 1](https://docs.mistral.ai/cookbooks/third_party/Langfuse/images/dashboard-posthog-2.png)

## Feedback

* * *

If you have any feedback or requests, please create a GitHub [Issue](https://langfuse.com/issue) or share your idea with the community on [Discord](https://discord.langfuse.com/).