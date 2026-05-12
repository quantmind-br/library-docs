---
title: Agent Cancelled - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/webhook-agent-cancelled
source: sitemap
fetched_at: 2026-03-23T07:19:00.615839-03:00
rendered_js: false
word_count: 69
summary: This document defines the structure and authentication requirements for webhook notifications triggered by the cancellation of an agent process.
tags:
    - webhooks
    - api-documentation
    - event-notification
    - agent-cancellation
    - security-hmac
category: api
---

```
{
  "success": false,
  "type": "agent.cancelled",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "d4e5f6a7-0005-0000-0000-000000000000",
  "data": [
    {
      "creditsUsed": 3
    }
  ],
  "metadata": {}
}

{
  "success": false,
  "type": "agent.cancelled",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "d4e5f6a7-0005-0000-0000-000000000000",
  "data": [
    {
      "creditsUsed": 3
    }
  ],
  "metadata": {}
}
```

#### Headers

HMAC-SHA256 signature of the raw request body, formatted as `sha256=<hex>`. Present when an HMAC secret is configured in your [account settings](https://www.firecrawl.dev/app/settings?tab=advanced). See [Webhook Security](https://docs.firecrawl.dev/webhooks/security) for verification details.

Example:

`"sha256=abc123def456789..."`

#### Body

Always `false` for this event.

Allowed value: `"agent.cancelled"`

Unique identifier for this webhook delivery.

The custom metadata object you provided in the webhook configuration. Echoed back in every delivery.

#### Response

Return any `2xx` status code to acknowledge receipt.