---
title: Track Usage for Coding Tools | liteLLM
url: https://docs.litellm.ai/docs/tutorials/cost_tracking_coding
source: sitemap
fetched_at: 2026-01-21T19:55:12.043749504-03:00
rendered_js: false
word_count: 140
summary: This document explains how to track and monitor usage, costs, and engagement for AI-powered coding tools by using User-Agent headers with the LiteLLM proxy.
tags:
    - litellm-proxy
    - usage-tracking
    - cost-monitoring
    - user-agent
    - ai-coding-tools
    - analytics-dashboard
category: guide
---

Track usage and costs for AI-powered coding tools like Claude Code, Roo Code, Gemini CLI, and OpenAI Codex through LiteLLM.

Monitor requests, costs, and user engagement metrics for each coding tool using User-Agent headers.

Central AI Platform teams providing developers access to coding tools through LiteLLM. Monitor tool engagement and track individual user usage patterns.

Configure your coding tool to send requests through the LiteLLM proxy with appropriate User-Agent headers.

Confirm LiteLLM is properly tracking requests by checking logs for the expected User-Agent values.

Access the LiteLLM dashboard to view aggregated usage metrics and user engagement data.

View total cost and successful requests for each coding tool.

View active user metrics for each coding tool.

LiteLLM tracks coding tools by monitoring the `User-Agent` header in incoming API requests (`/chat/completions`, `/responses`, etc.). Each unique User-Agent is tracked separately for usage analytics.

```
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -H "User-Agent: claude-cli/1.0" \
  -d '{"model": "claude-3-5-sonnet-latest", "messages": [{"role": "user", "content": "Hello, how are you?"}]}' \
  http://localhost:4000/chat/completions
```