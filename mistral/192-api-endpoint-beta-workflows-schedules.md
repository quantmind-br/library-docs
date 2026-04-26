---
title: Beta Workflows Schedules
url: https://docs.mistral.ai/api/endpoint/beta/workflows/schedules
source: sitemap
fetched_at: 2026-04-26T04:01:59.371009574-03:00
rendered_js: false
word_count: 137
summary: API reference for managing workflow schedules, including endpoints for creating, listing, and deleting scheduled workflow tasks.
tags:
    - api-reference
    - workflow-automation
    - scheduling
    - rest-api
    - task-management
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Workflows Schedules

Create and manage workflow schedules.

---

## List Schedules

`GET /v1/workflows/schedules`

### Response

```json
{"schedules": [{"input": null, "schedule_id": "ipsum eiusmod"}]}
```

---

## Create Schedule

`POST /v1/workflows/schedules`

### Parameters

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `deployment_name` | string\|null | - | Deployment name for routing |
| `schedule` | ScheduleDefinition | - | Schedule specification (calendars, intervals, cron_expressions, skip) |
| `schedule_id` | string\|null | - | Custom schedule ID (auto-generated if not provided) |
| `workflow_identifier` | string\|null | - | Name or ID of workflow to schedule |
| `workflow_registration_id` | string\|null | - | Workflow registration ID |
| `workflow_task_queue` | string\|null | - | **Deprecated.** Use `deployment_name` |
| `workflow_version_id` | string\|null | - | **Deprecated.** Use `workflow_registration_id` |

### Code Example

```bash
curl https://api.mistral.ai/v1/workflows/schedules \
  -X POST \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
  -H 'Content-Type: application/json' \
  -d '{"schedule": {"input": null}}'
```

### Response

```json
{"schedule_id": "ipsum eiusmod"}
```

---

## Delete Schedule

`DELETE /v1/workflows/schedules/{schedule_id}`

#workflow-automation #scheduling #task-management
