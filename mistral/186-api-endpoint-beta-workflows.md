---
title: Beta Workflows
url: https://docs.mistral.ai/api/endpoint/beta/workflows
source: sitemap
fetched_at: 2026-04-26T04:01:47.580640658-03:00
rendered_js: false
word_count: 25
summary: API endpoints for managing and executing workflow registrations and their associated lifecycle states.
tags:
    - api-endpoints
    - workflow-management
    - rest-api
    - registration-lifecycle
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Workflows

Workflow registration and execution API.

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v1/workflows/registrations` | List workflow registrations |
| `POST` | `/v1/workflows/{workflow_identifier}/execute` | Execute by identifier |
| `POST` | `/v1/workflows/registrations/{workflow_registration_id}/execute` | Execute by registration ID |
| `GET` | `/v1/workflows/{workflow_identifier}` | Get registration |
| `PUT` | `/v1/workflows/{workflow_identifier}` | Update registration |
| `GET` | `/v1/workflows/registrations/{workflow_registration_id}` | Get by registration ID |
| `PUT` | `/v1/workflows/{workflow_identifier}/archive` | Archive |
| `PUT` | `/v1/workflows/{workflow_identifier}/unarchive` | Unarchive |

#workflow-management #registration-lifecycle
