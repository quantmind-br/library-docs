---
title: Change Tracking | Firecrawl
url: https://docs.firecrawl.dev/features/change-tracking
source: sitemap
fetched_at: 2026-03-23T07:26:03.026985-03:00
rendered_js: false
word_count: 883
summary: This document explains how to use Firecrawl's change tracking feature to detect modifications, additions, or removals in web content by comparing current scrapes against historical snapshots.
tags:
    - change-tracking
    - web-scraping
    - diff-analysis
    - data-monitoring
    - automation
    - api-integration
    - structured-data
category: guide
---

![Change Tracking](https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc56c24d15e1b2ed4806ddb66d0f5c3f) Change tracking compares the current content of a page against the last time you scraped it. Add `changeTracking` to your `formats` array to detect whether a page is new, unchanged, or modified, and optionally get a structured diff of what changed.

- Works with `/scrape`, `/crawl`, and `/batch/scrape`
- Two diff modes: `git-diff` for line-level changes, `json` for field-level comparison
- Scoped to your team, and optionally scoped to a tag that you pass in

## How it works

Every scrape with `changeTracking` enabled stores a snapshot and compares it against the previous snapshot for that URL. Snapshots are stored persistently and do not expire, so comparisons remain accurate regardless of how much time has passed between scrapes.

ScrapeResultFirst time`changeStatus: "new"` (no previous version exists)Content unchanged`changeStatus: "same"`Content modified`changeStatus: "changed"` (diff data available)Page removed`changeStatus: "removed"`

The response includes these fields in the `changeTracking` object:

FieldTypeDescription`previousScrapeAt``string | null`Timestamp of the previous scrape (`null` on first scrape)`changeStatus``string``"new"`, `"same"`, `"changed"`, or `"removed"``visibility``string``"visible"` (discoverable via links/sitemap) or `"hidden"` (URL works but is no longer linked)`diff``object | undefined`Line-level diff (only present in `git-diff` mode when status is `"changed"`)`json``object | undefined`Field-level comparison (only present in `json` mode when status is `"changed"`)

## Basic usage

Include both `markdown` and `changeTracking` in the `formats` array. The `markdown` format is required because change tracking compares pages via their markdown content.

### Response

On the first scrape, `changeStatus` is `"new"` and `previousScrapeAt` is `null`:

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $9/mo\nPro: $29/mo...",
    "changeTracking": {
      "previousScrapeAt": null,
      "changeStatus": "new",
      "visibility": "visible"
    }
  }
}
```

On subsequent scrapes, `changeStatus` reflects whether content changed:

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $12/mo\nPro: $39/mo...",
    "changeTracking": {
      "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible"
    }
  }
}
```

## Git-diff mode

The `git-diff` mode returns line-by-line changes in a format similar to `git diff`. Pass an object in the `formats` array with `modes: ["git-diff"]`:

### Response

The `diff` object contains both a plain-text diff and a structured JSON representation:

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "diff": {
      "text": "@@ -1,3 +1,3 @@\n # Pricing\n-Starter: $9/mo\n-Pro: $29/mo\n+Starter: $12/mo\n+Pro: $39/mo",
      "json": {
        "files": [{
          "chunks": [{
            "content": "@@ -1,3 +1,3 @@",
            "changes": [
              { "type": "normal", "content": "# Pricing" },
              { "type": "del", "ln": 2, "content": "Starter: $9/mo" },
              { "type": "del", "ln": 3, "content": "Pro: $29/mo" },
              { "type": "add", "ln": 2, "content": "Starter: $12/mo" },
              { "type": "add", "ln": 3, "content": "Pro: $39/mo" }
            ]
          }]
        }]
      }
    }
  }
}
```

The structured `diff.json` object contains:

- `files`: array of changed files (typically one for web pages)
- `chunks`: sections of changes within a file
- `changes`: individual line changes with `type` (`"add"`, `"del"`, or `"normal"`), line number (`ln`), and `content`

## JSON mode

The `json` mode extracts specific fields from both the current and previous version of the page using a schema you define. This is useful for tracking changes in structured data like prices, stock levels, or metadata without parsing a full diff. Pass `modes: ["json"]` with a `schema` defining the fields to extract:

### Response

Each field in the schema is returned with `previous` and `current` values:

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-05T08:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "json": {
      "price": {
        "previous": "$19.99",
        "current": "$24.99"
      },
      "availability": {
        "previous": "In Stock",
        "current": "In Stock"
      }
    }
  }
}
```

You can also pass an optional `prompt` to guide the LLM extraction alongside the schema.

By default, change tracking compares against the most recent scrape of the same URL scraped by your team. Tags let you maintain **separate tracking histories** for the same URL, which is useful when you monitor the same page at different intervals or in different contexts.

## Crawl with change tracking

Add change tracking to crawl operations to monitor an entire site for changes. Pass the `changeTracking` format inside `scrapeOptions`:

## Batch scrape with change tracking

Use [batch scrape](https://docs.firecrawl.dev/features/batch-scrape) to monitor a specific set of URLs:

## Scheduling change tracking

Change tracking is most useful when you scrape on a regular schedule. You can automate this with cron, cloud schedulers, or workflow tools.

### Cron job

Create a script that scrapes a URL and alerts on changes:

```
#!/bin/bash
RESPONSE=$(curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://competitor.com/pricing",
    "formats": [
      "markdown",
      {
        "type": "changeTracking",
        "modes": ["json"],
        "schema": {
          "type": "object",
          "properties": {
            "starter_price": { "type": "string" },
            "pro_price": { "type": "string" }
          }
        }
      }
    ]
  }')

STATUS=$(echo "$RESPONSE" | jq -r '.data.changeTracking.changeStatus')

if [ "$STATUS" = "changed" ]; then
  echo "$RESPONSE" | jq '.data.changeTracking.json'
  # Send alert via email, Slack, etc.
fi
```

Schedule it with `crontab -e`:

```
0 */6 * * * /path/to/check-pricing.sh >> /var/log/price-monitor.log 2>&1
```

ScheduleExpressionEvery hour`0 * * * *`Every 6 hours`0 */6 * * *`Daily at 9 AM`0 9 * * *`Weekly on Monday at 8 AM`0 8 * * 1`

### Cloud and serverless schedulers

- **AWS**: EventBridge rule triggering a Lambda function
- **GCP**: Cloud Scheduler triggering a Cloud Function
- **Vercel / Netlify**: Cron-triggered serverless functions
- **GitHub Actions**: Scheduled workflows with `schedule` and `cron` trigger

### Workflow automation

No-code platforms like **n8n**, **Zapier**, and **Make** can call the Firecrawl API on a schedule and route results to Slack, email, or databases. See the [workflow automation guides](https://docs.firecrawl.dev/developer-guides/workflow-automation/n8n).

## Webhooks

For async operations like crawl and batch scrape, use [webhooks](https://docs.firecrawl.dev/webhooks/overview) to receive change tracking results as they arrive instead of polling.

The `crawl.page` event payload includes the `changeTracking` object for each page:

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [{
    "markdown": "# Pricing\n\nStarter: $12/mo...",
    "metadata": {
      "title": "Pricing",
      "url": "https://example.com/pricing",
      "statusCode": 200
    },
    "changeTracking": {
      "previousScrapeAt": "2025-06-05T12:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible",
      "diff": {
        "text": "@@ -2,1 +2,1 @@\n-Starter: $9/mo\n+Starter: $12/mo"
      }
    }
  }]
}
```

For webhook configuration details (headers, metadata, events, retries, signature verification), see the [Webhooks documentation](https://docs.firecrawl.dev/webhooks/overview).

## Configuration reference

The full set of options available when passing a `changeTracking` format object:

ParameterTypeDefaultDescription`type``string`(required)Must be `"changeTracking"``modes``string[]``[]`Diff modes to enable: `"git-diff"`, `"json"`, or both`schema``object`(none)JSON Schema for field-level comparison (required for `json` mode)`prompt``string`(none)Custom prompt to guide LLM extraction (used with `json` mode)`tag``string``null`Separate tracking history identifier

### Data models

## Important details

- **Snapshot retention**: Snapshots are stored persistently and do not expire. A scrape performed months after the previous one will still compare correctly against the earlier snapshot.
- **Scoping**: Comparisons are scoped to your team. Your first scrape of any URL returns `"new"`, even if other users have scraped it.
- **URL matching**: Previous scrapes are matched on exact source URL, team ID, `markdown` format, and `tag`. Keep URLs consistent between scrapes.
- **Parameter consistency**: Using different `includeTags`, `excludeTags`, or `onlyMainContent` settings across scrapes of the same URL produces unreliable comparisons.
- **Comparison algorithm**: The algorithm is resistant to whitespace and content order changes. Iframe source URLs are ignored to handle captcha/antibot randomization.
- **Caching**: Requests with `changeTracking` bypass the index cache. The `maxAge` parameter is ignored.
- **Error handling**: Monitor the `warning` field in responses and handle the `changeTracking` object potentially being absent (this can occur if the database lookup for the previous scrape times out).

## Billing

ModeCostBasic change trackingNo extra cost (standard scrape credits)`git-diff` modeNo extra cost`json` mode5 credits per page

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.