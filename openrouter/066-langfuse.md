---
title: Langfuse
url: https://openrouter.ai/docs/guides/features/broadcast/langfuse.mdx
source: llms
fetched_at: 2026-02-13T15:14:36.332009-03:00
rendered_js: false
word_count: 418
summary: This guide provides step-by-step instructions for connecting Langfuse to OpenRouter to automatically send and manage LLM request traces for monitoring and debugging.
tags:
    - langfuse
    - observability
    - tracing
    - openrouter
    - llm-monitoring
    - integration
    - metadata
category: guide
---

***

title: Langfuse
subtitle: Send traces to Langfuse
headline: Broadcast to Langfuse | OpenRouter Observability
canonical-url: '[https://openrouter.ai/docs/guides/features/broadcast/langfuse](https://openrouter.ai/docs/guides/features/broadcast/langfuse)'
'og:site\_name': OpenRouter Documentation
'og:title': Broadcast to Langfuse - Send Traces to Langfuse
'og:description': >-
Connect Langfuse to automatically receive traces from your OpenRouter
requests. Step-by-step setup guide for Langfuse integration.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Langfuse%20Broadcast\&description=Send%20traces%20to%20Langfuse](https://openrouter.ai/dynamic-og?title=Langfuse%20Broadcast\&description=Send%20traces%20to%20Langfuse)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

[Langfuse](https://langfuse.com) is an open-source LLM engineering platform for tracing, evaluating, and debugging LLM applications.

## Step 1: Create a Langfuse API key

In Langfuse, go to your project's **Settings > API Keys** and create a new key pair. Copy both the Secret Key and Public Key.

![Langfuse API Keys](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/2fda0df2def9f2d969130c4704f72937461f4cbb8bb9435aa2245bb07391a35e/content/pages/features/broadcast/broadcast-langfuse-keys.png)

## Step 2: Enable Broadcast in OpenRouter

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/7386b119bd35a485ec53b6f15e3dfe3a980fc5bf61a573256e27ae607ef5614a/content/pages/features/broadcast/broadcast-enable.png)

## Step 3: Configure Langfuse

Click the edit icon next to **Langfuse** and enter:

* **Secret Key**: Your Langfuse Secret Key
* **Public Key**: Your Langfuse Public Key
* **Base URL** (optional): Default is `https://us.cloud.langfuse.com`. Change for other regions or self-hosted instances

![Langfuse Configuration](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/10178cb9915dae07364910b865f4dbdbfc18936d91ca39ab0a9f9f1d9892ad79/content/pages/features/broadcast/broadcast-langfuse-config.png)

## Step 4: Test and save

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

![Langfuse Configured](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/77277ddb0cd573d0efe91338a32735d6b710c4c7ecfdcd610f0750d0262b4202/content/pages/features/broadcast/broadcast-langfuse-configured.png)

## Step 5: Send a test trace

Make an API request through OpenRouter and view the trace in Langfuse.

![Langfuse Trace](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/cbd93fc215244ec3906102bdfb3a46c4938c7dd92b076c6a3f3510cc701a9487/content/pages/features/broadcast/broadcast-langfuse-trace.png)

## Custom Metadata

Langfuse supports rich trace hierarchies and metadata. Use the `trace` field to customize how your traces appear in Langfuse.

### Supported Metadata Keys

| Key               | Langfuse Mapping      | Description                                      |
| ----------------- | --------------------- | ------------------------------------------------ |
| `trace_id`        | Trace ID              | Group multiple requests into a single trace      |
| `trace_name`      | Trace Name            | Custom name displayed in the Langfuse trace list |
| `span_name`       | Span Name             | Name for intermediate spans in the hierarchy     |
| `generation_name` | Generation Name       | Name for the LLM generation observation          |
| `parent_span_id`  | Parent Observation ID | Link to an existing span in your trace hierarchy |

### Example

```json
{
  "model": "openai/gpt-4o",
  "messages": [{ "role": "user", "content": "Summarize this document..." }],
  "user": "user_12345",
  "session_id": "session_abc",
  "trace": {
    "trace_id": "workflow_12345",
    "trace_name": "Document Processing Pipeline",
    "span_name": "Summarization Step",
    "generation_name": "Generate Summary",
    "environment": "production",
    "pipeline_version": "2.1.0"
  }
}
```

This creates a hierarchical trace structure in Langfuse:

```
Document Processing Pipeline (trace)
└── Summarization Step (span)
    └── Generate Summary (generation)
```

### Additional Context

* The `user` field maps to Langfuse's User ID for user-level analytics
* The `session_id` field maps to Langfuse's Session ID for grouping conversations
* Any additional keys in `trace` are passed as trace metadata and can be used for filtering and analysis in Langfuse

## Privacy Mode

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) for details.