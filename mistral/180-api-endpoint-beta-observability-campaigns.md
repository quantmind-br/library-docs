---
title: Beta Observability Campaigns
url: https://docs.mistral.ai/api/endpoint/beta/observability/campaigns
source: sitemap
fetched_at: 2026-04-26T04:01:35.176231129-03:00
rendered_js: false
word_count: 94
summary: API reference for managing evaluation campaigns, including endpoints for creating, retrieving, deleting, and checking campaign status.
tags:
    - api-reference
    - evaluation-campaigns
    - observability
    - mistral-api
    - event-tracking
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Observability Campaigns

Create and manage evaluation campaigns.

---

## List Campaigns

`GET /v1/observability/campaigns`

### Code Example

```bash
curl https://api.mistral.ai/v1/observability/campaigns \
  -X GET \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

### Response

```json
{"campaigns": {"count": 87}}
```

---

## Create Campaign

`POST /v1/observability/campaigns`

Create and start a new campaign.

| Param | Type | Description |
|-------|------|-------------|
| `description` | string | Campaign description |
| `judge_id` | string | Judge ID |
| `max_nb_events` | integer | Maximum events |
| `name` | string | Campaign name |
| `search_params` | FilterPayload | Search filter parameters |

### Code Example

```bash
curl https://api.mistral.ai/v1/observability/campaigns \
  -X POST \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
  -H 'Content-Type: application/json' \
  -d '{"description": "ipsum eiusmod", "judge_id": "consequat do", "max_nb_events": 87, "name": "reprehenderit ut dolore", "search_params": {"filters": null}}'
```

---

## Get Campaign

`GET /v1/observability/campaigns/{campaign_id}`

---

## Delete Campaign

`DELETE /v1/observability/campaigns/{campaign_id}`

---

## Get Campaign Status

`GET /v1/observability/campaigns/{campaign_id}/status`

| Status | Description |
|--------|-------------|
| `RUNNING` | Campaign in progress |
| `COMPLETED` | Campaign finished |
| `FAILED` | Campaign failed |
| `CANCELED` | Campaign canceled |
| `TERMINATED` | Campaign terminated |
| `CONTINUED_AS_NEW` | Continued as new |
| `TIMED_OUT` | Timed out |
| `UNKNOWN` | Unknown state |

---

## Get Selected Events

`GET /v1/observability/campaigns/{campaign_id}/selected-events`

Get event IDs selected by the campaign.

#evaluation-campaigns #event-tracking #observability
