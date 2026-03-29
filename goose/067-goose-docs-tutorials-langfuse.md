---
title: Observability with Langfuse | goose
url: https://block.github.io/goose/docs/tutorials/langfuse
source: github_pages
fetched_at: 2026-01-22T22:16:19.146337629-03:00
rendered_js: true
word_count: 104
summary: This tutorial explains how to integrate goose with Langfuse for monitoring and debugging LLM agent performance through environment variables.
tags:
    - goose
    - langfuse
    - llm-monitoring
    - observability
    - agent-telemetry
    - integration
category: tutorial
---

This tutorial covers how to integrate goose with Langfuse to monitor your goose requests and understand how the agent is performing.

[Langfuse](https://langfuse.com/) is an [open-source](https://github.com/langfuse/langfuse) LLM engineering platform that enables teams to collaboratively monitor, evaluate, and debug their LLM applications.

Sign up for Langfuse Cloud [here](https://cloud.langfuse.com) or self-host Langfuse [Docker Compose](https://langfuse.com/self-hosting/local) to get your Langfuse API keys.

Set the environment variables so that goose (written in Rust) can connect to the Langfuse server.

```
export LANGFUSE_INIT_PROJECT_PUBLIC_KEY=pk-lf-...
export LANGFUSE_INIT_PROJECT_SECRET_KEY=sk-lf-...
export LANGFUSE_URL=https://cloud.langfuse.com # EU data region 🇪🇺

# https://us.cloud.langfuse.com if you're using the US region 🇺🇸
# https://localhost:3000 if you're self-hosting
```

Now, you can run goose and monitor your AI requests and actions through Langfuse.

With goose running and the environment variables set, Langfuse will start capturing traces of your goose activities.