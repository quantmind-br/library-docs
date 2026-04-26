---
title: Beta Observability Datasets
url: https://docs.mistral.ai/api/endpoint/beta/observability/datasets
source: sitemap
fetched_at: 2026-04-26T04:01:41.120851432-03:00
rendered_js: false
word_count: 115
summary: REST API endpoints for managing observability datasets, including operations for creating, modifying, and importing data.
tags:
    - observability
    - dataset-management
    - rest-api
    - data-import
    - data-export
    - api-endpoints
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Observability Datasets

CRUD API for observability dataset management.

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v1/observability/datasets` | List datasets |
| `POST` | `/v1/observability/datasets` | Create empty dataset |
| `GET` | `/v1/observability/datasets/{dataset_id}` | Get dataset |
| `DELETE` | `/v1/observability/datasets/{dataset_id}` | Delete dataset |
| `PATCH` | `/v1/observability/datasets/{dataset_id}` | Update dataset |

---

## Records

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v1/observability/datasets/{dataset_id}/records` | List records |
| `POST` | `/v1/observability/datasets/{dataset_id}/records` | Add conversation |

---

## Imports

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/v1/observability/datasets/{dataset_id}/imports/from-campaign` | Populate from campaign |
| `POST` | `/v1/observability/datasets/{dataset_id}/imports/from-explorer` | Populate from explorer |
| `POST` | `/v1/observability/datasets/{dataset_id}/imports/from-file` | Populate from uploaded file |
| `POST` | `/v1/observability/datasets/{dataset_id}/imports/from-playground` | Populate from playground |
| `POST` | `/v1/observability/datasets/{dataset_id}/imports/from-dataset` | Populate from another dataset |

---

## Exports

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v1/observability/datasets/{dataset_id}/exports/to-jsonl` | Export to JSONL (presigned URL) |

---

## Tasks

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v1/observability/datasets/{dataset_id}/tasks/{task_id}` | Get import task status |
| `GET` | `/v1/observability/datasets/{dataset_id}/tasks` | List import tasks |

#dataset-management #data-import #observability
