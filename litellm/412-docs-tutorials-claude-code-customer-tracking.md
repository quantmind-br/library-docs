---
title: Claude Code - Granular Cost Tracking | liteLLM
url: https://docs.litellm.ai/docs/tutorials/claude_code_customer_tracking
source: sitemap
fetched_at: 2026-01-21T19:55:02.044194091-03:00
rendered_js: false
word_count: 100
summary: This document explains how to track Claude Code usage and attribute costs to specific customers or projects using LiteLLM proxy and custom headers.
tags:
    - claude-code
    - litellm-proxy
    - cost-attribution
    - usage-tracking
    - custom-headers
    - monitoring
category: guide
---

Track Claude Code usage by customer or tags using LiteLLM proxy. This enables granular cost attribution for billing, budgeting, and analytics.

Claude Code supports custom headers via `ANTHROPIC_CUSTOM_HEADERS`. LiteLLM automatically tracks requests with specific headers for cost attribution.

Use this to attribute costs to specific customers or end-users.

Use this to attribute costs to projects, cost centers, or environments. Pass comma-separated tags.

```
export ANTHROPIC_BASE_URL=http://localhost:4000
export ANTHROPIC_API_KEY=sk-1234
export ANTHROPIC_CUSTOM_HEADERS="x-litellm-tags: project:acme,env:prod,team:backend"
```

All requests will now be tracked under the customer ID `claude-ishaan-local`.

Navigate to the **Logs** tab in the LiteLLM UI.

Click on a request to see details.

Filter by customer ID to see all requests for that customer.