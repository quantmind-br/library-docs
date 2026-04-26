---
title: Beta Workflows Workers
url: https://docs.mistral.ai/api/endpoint/beta/workflows/workers
source: sitemap
fetched_at: 2026-04-26T04:02:01.499711104-03:00
rendered_js: false
word_count: 23
summary: Endpoint for retrieving workflow worker identity, including namespace, scheduler URL, and TLS status.
tags:
    - worker-info
    - workflow-api
    - service-discovery
    - identity-check
    - rest-api
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Workflows Workers

`GET /v1/workflows/workers/whoami`

Get worker identity information.

### Response Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `namespace` | string | - | Worker namespace |
| `scheduler_url` | string | - | Scheduler URL |
| `tls` | boolean | `false` | TLS enabled |

### Code Example

```bash
curl https://api.mistral.ai/v1/workflows/workers/whoami \
  -X GET \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

### Response

```json
{"namespace": "ipsum eiusmod", "scheduler_url": "consequat do"}
```

#worker-info #service-discovery #identity-check
