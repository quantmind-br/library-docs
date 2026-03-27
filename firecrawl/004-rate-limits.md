---
title: Rate Limits | Firecrawl
url: https://docs.firecrawl.dev/rate-limits
source: sitemap
fetched_at: 2026-03-23T07:27:47.504225-03:00
rendered_js: false
word_count: 393
summary: This document outlines the subscription-based billing model, concurrent browser limits, and API rate limits for the Firecrawl platform.
tags:
    - billing-model
    - subscription-plans
    - concurrency-limits
    - rate-limiting
    - api-usage
category: concept
---

## Billing Model

Firecrawl uses subscription-based monthly plans. We do not offer a pure pay-as-you-go model, but our **auto-recharge feature** provides flexible scaling—once you subscribe to a plan, you can automatically purchase additional credits when you dip below a threshold, with better rates on larger auto-recharge packs. For testing before committing to a larger plan, start with the Free or Hobby tier. Plan downgrades are scheduled to take effect at the next renewal, and unused-time credits are not issued.

## Concurrent Browser Limits

Concurrent browsers represent how many web pages Firecrawl can process for you at the same time. Your plan determines how many of these jobs can run simultaneously - if you exceed this limit, additional jobs will wait in a queue until resources become available. Note that time spent waiting in the queue counts against the request’s [`timeout`](https://docs.firecrawl.dev/advanced-scraping-guide#timing-and-cache) parameter, so you can set a lower timeout to fail fast instead of waiting. You can also check current availability via the [Queue Status](https://docs.firecrawl.dev/api-reference/endpoint/queue-status) endpoint.

### Current Plans

PlanConcurrent BrowsersMax Queued JobsFree250,000Hobby550,000Standard50100,000Growth100200,000Scale / Enterprise150+300,000+

Each team has a maximum number of jobs that can be waiting in the concurrency queue. If you exceed this limit, new jobs will be rejected with a `429` status code until existing jobs complete. For larger plans with custom concurrency limits, the max queued jobs is 2,000 times your concurrency limit, capped at 2,000,000. If you require higher concurrency limits, [contact us about enterprise plans](https://firecrawl.dev/enterprise).

PlanConcurrent BrowsersMax Queued JobsFree250,000Starter50100,000Explorer100200,000Pro200400,000

Rate limits are measured in requests per minute and are primarily in place to prevent abuse. When configured correctly, your real bottleneck will be concurrent browsers.

### Current Plans

Plan/scrape/map/crawl/search/agent/crawl/status/agent/statusFree101015101500500Hobby1001001550100150025000Standard50050050250500150025000Growth5000500025025001000150025000Scale75007500750750010002500025000

These rate limits are enforced to ensure fair usage and availability of the API for all users. If you require higher limits, please contact us at [help@firecrawl.com](mailto:help@firecrawl.com) to discuss custom plans.

The extract endpoints share limits with the corresponding /agent rate limits.

### Batch Scrape Endpoints

The batch scrape endpoints share limits with the corresponding /crawl rate limits.

### Browser Sessions

While the /browser endpoint is in preview, each team can have up to 20 active browser sessions at a time. If you exceed this limit, new session requests will return a `429` status code until existing sessions are destroyed.

### FIRE-1 Agent

Requests involving the FIRE-1 agent requests have separate rate limits that are counted independently for each endpoint:

EndpointRate Limit (requests/min)/scrape10/extract10

Plan/extract (requests/min)/extract/status (requests/min)Starter10025000Explorer50025000Pro100025000