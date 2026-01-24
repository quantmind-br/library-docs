---
title: Limits · Cloudflare Agents docs
url: https://developers.cloudflare.com/agents/platform/limits/index.md
source: llms
fetched_at: 2026-01-24T14:00:00.785657735-03:00
rendered_js: false
word_count: 236
summary: This document outlines the resource constraints and operational limits for authoring, deploying, and running Agents, including specifications for concurrency, storage, and compute time.
tags:
    - cloudflare-agents
    - platform-limits
    - resource-quotas
    - compute-limits
    - durable-objects
    - workers-platform
category: reference
---

Limits that apply to authoring, deploying, and running Agents are detailed below.

Many limits are inherited from those applied to Workers scripts and/or Durable Objects, and are detailed in the [Workers limits](https://developers.cloudflare.com/workers/platform/limits/) documentation.

| Feature | Limit |
| - | - |
| Max concurrent (running) Agents per account | Tens of millions+ [1](#user-content-fn-1) |
| Max definitions per account | \~250,000+ [2](#user-content-fn-2) |
| Max state stored per unique Agent | 1 GB |
| Max compute time per Agent | 30 seconds (refreshed per HTTP request / incoming WebSocket message) [3](#user-content-fn-3) |
| Duration (wall clock) per step [3](#user-content-fn-3) | Unlimited (for example, waiting on a database call or an LLM response) |

***

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form](https://forms.gle/ukpeZVLWLnKeixDu7). If the limit can be increased, Cloudflare will contact you with next steps.

## Footnotes

1. Yes, really. You can have tens of millions of Agents running concurrently, as each Agent is mapped to a [unique Durable Object](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/) (actor). [↩](#user-content-fnref-1)

2. You can deploy up to [500 scripts per account](https://developers.cloudflare.com/workers/platform/limits/), but each script (project) can define multiple Agents. Each deployed script can be up to 10 MB on the [Workers Paid Plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) [↩](#user-content-fnref-2)

3. Compute (CPU) time per Agent is limited to 30 seconds, but this is refreshed when an Agent receives a new HTTP request, runs a [scheduled task](https://developers.cloudflare.com/agents/api-reference/schedule-tasks/), or an incoming WebSocket message. [↩](#user-content-fnref-3) [↩2](#user-content-fnref-3-2)