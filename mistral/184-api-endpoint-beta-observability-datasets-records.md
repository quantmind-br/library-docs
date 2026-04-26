---
title: Beta Observability Datasets Records
url: https://docs.mistral.ai/api/endpoint/beta/observability/datasets/records
source: sitemap
fetched_at: 2026-04-26T04:01:42.926623423-03:00
rendered_js: false
word_count: 53
summary: API endpoints for managing individual conversation records within a dataset, including retrieval, deletion, and updates.
tags:
    - api-endpoints
    - dataset-management
    - observability
    - data-retrieval
    - record-deletion
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Observability Datasets Records

API for managing conversation records within datasets.

---

## Get Record

`GET /v1/observability/dataset-records/{dataset_record_id}`

Get conversation content from a dataset.

---

## Delete Record

`DELETE /v1/observability/dataset-records/{dataset_record_id}`

Delete a record from a dataset.

---

## Bulk Delete

`POST /v1/observability/dataset-records/bulk-delete`

Delete multiple records from datasets.

---

## Live Judging

`POST /v1/observability/dataset-records/{dataset_record_id}/live-judging`

Run Judge on a dataset record.

---

## Update Payload

`PUT /v1/observability/dataset-records/{dataset_record_id}/payload`

Update dataset record conversation payload.

---

## Update Properties

`PUT /v1/observability/dataset-records/{dataset_record_id}/properties`

Update conversation properties.

#dataset-management #record-deletion #observability
