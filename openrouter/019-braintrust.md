---
title: Braintrust
url: https://openrouter.ai/docs/guides/features/broadcast/braintrust.mdx
source: llms
fetched_at: 2026-02-13T15:14:26.092671-03:00
rendered_js: false
word_count: 408
summary: This guide explains how to integrate OpenRouter with Braintrust to automatically broadcast LLM request traces for monitoring and evaluation. It covers the setup process, configuration of API keys, and handling of custom metadata.
tags:
    - openrouter
    - braintrust
    - observability
    - tracing
    - llm-monitoring
    - integration
category: guide
---

***

title: Braintrust
subtitle: Send traces to Braintrust
headline: Broadcast to Braintrust | OpenRouter Observability
canonical-url: '[https://openrouter.ai/docs/guides/features/broadcast/braintrust](https://openrouter.ai/docs/guides/features/broadcast/braintrust)'
'og:site\_name': OpenRouter Documentation
'og:title': Broadcast to Braintrust - Send Traces to Braintrust
'og:description': >-
Connect Braintrust to automatically receive traces from your OpenRouter
requests. Step-by-step setup guide for Braintrust integration.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Braintrust%20Broadcast\&description=Send%20traces%20to%20Braintrust](https://openrouter.ai/dynamic-og?title=Braintrust%20Broadcast\&description=Send%20traces%20to%20Braintrust)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

[Braintrust](https://www.braintrust.dev) is an end-to-end platform for evaluating, monitoring, and improving LLM applications.

## Step 1: Get your Braintrust API key and Project ID

In Braintrust, go to your [Account Settings](https://www.braintrust.dev/app/settings) to create an API key, and find your Project ID in your project's settings.

## Step 2: Enable Broadcast in OpenRouter

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/7386b119bd35a485ec53b6f15e3dfe3a980fc5bf61a573256e27ae607ef5614a/content/pages/features/broadcast/broadcast-enable.png)

## Step 3: Configure Braintrust

Click the edit icon next to **Braintrust** and enter:

* **Api Key**: Your Braintrust API key
* **Project Id**: Your Braintrust project ID
* **Base Url** (optional): Default is `https://api.braintrust.dev`

![Braintrust Configuration](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/2e424e28cce938fe94f28acee1c34fc83695c7c0085d98bcbc2cc9434f695cd9/content/pages/features/broadcast/broadcast-braintrust-config.png)

## Step 4: Test and save

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

![Braintrust Configured](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/447023a4f5241b7d572d70b210fadd341824c4ee7a97d6e0a87bd8d45692457d/content/pages/features/broadcast/broadcast-braintrust-configured.png)

## Step 5: Send a test trace

Make an API request through OpenRouter and view the trace in Braintrust.

![Braintrust Trace](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/0ef5e7f7e6f1632eac10774e85b4570829e4a4236592049b3b8d0e7dbc745c19/content/pages/features/broadcast/broadcast-braintrust-trace.png)

## Custom Metadata

Braintrust supports custom metadata, tags, and nested span structures for organizing your LLM logs.

### Supported Metadata Keys

| Key               | Braintrust Mapping     | Description                                      |
| ----------------- | ---------------------- | ------------------------------------------------ |
| `trace_id`        | Span ID / Root Span ID | Group multiple logs into a single trace          |
| `trace_name`      | Name                   | Custom name displayed in the Braintrust log view |
| `span_name`       | Name                   | Name for intermediate spans in the hierarchy     |
| `generation_name` | Name                   | Name for the LLM span                            |

### Example

```json
{
  "model": "openai/gpt-4o",
  "messages": [{ "role": "user", "content": "Generate a summary..." }],
  "user": "user_12345",
  "session_id": "session_abc",
  "trace": {
    "trace_id": "eval_run_456",
    "trace_name": "Summarization Eval",
    "generation_name": "GPT-4o Summary",
    "eval_dataset": "news_articles",
    "experiment_id": "exp_789"
  }
}
```

### Metrics and Costs

Braintrust receives detailed metrics for each LLM call:

* Token counts (prompt, completion, total)
* Cached token usage when available
* Reasoning token counts for supported models
* Cost information (input, output, total costs)
* Duration and timing metrics

### Additional Context

* The `user` field maps to Braintrust's `user_id` in metadata
* The `session_id` field maps to `session_id` in metadata
* Custom metadata keys are included in the span's metadata object
* Tags are passed through for filtering in the Braintrust UI

## Privacy Mode

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) for details.