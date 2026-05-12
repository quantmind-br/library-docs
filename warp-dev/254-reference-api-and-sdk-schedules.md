---
title: Schedules | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/schedules
source: sitemap
fetched_at: 2026-04-29T15:05:08.681750406-03:00
rendered_js: false
word_count: 1012
summary: This document provides the API specifications for creating, managing, and controlling the lifecycle of scheduled agents using cron expressions.
tags:
    - api-reference
    - agent-management
    - cron-scheduling
    - automation
    - rest-api
category: api
optimized: true
optimized_at: 2026-04-29T19:05:00Z
---
# Schedules

Operations for creating and managing scheduled agents using cron expressions.

## List scheduled agents

`GET /agent/schedules`

Retrieve all scheduled agents accessible to the authenticated user. Results are sorted alphabetically by name.

### Request

| Parameter | Type | Description |
|-----------|------|-------------|
| Authorization | string (required) | Authentication via a Warp API key |

### Response

| Status | Description |
|--------|-------------|
| 200 | List of scheduled agents (`application/json`) |
| 401 | Authentication required (`application/json`) |

## Create a scheduled agent

`POST /agent/schedules`

Create a new scheduled agent that runs on a cron schedule. The agent will be triggered automatically based on the cron expression.

### Request

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Authorization | string | Yes | Authentication via a Warp API key |
| name | string | Yes | Human-readable name for the schedule |
| cron_schedule | string | Yes | Cron expression defining when the agent runs (e.g., "0 9 * * *" for daily at 9am UTC) |
| prompt | string | No | The prompt/instruction for the agent to execute. Required unless `agent_config.skill_spec` is provided. |
| enabled | boolean | No | Whether the schedule should be active immediately. Default: `true` |
| agent_uid | string | No | Agent UID to use as the execution principal for this schedule. Only valid for team-owned schedules. |
| team | boolean | No | Whether to create a team-owned schedule. Defaults to true for users on a single team. |

### Response

| Status | Description |
|--------|-------------|
| 201 | Scheduled agent created successfully (`application/json`) |
| 400 | Invalid request (missing required fields, invalid cron expression) (`application/json`) |
| 401 | Authentication required (`application/json`) |
| 403 | No permission or feature not available (`application/json`) |

## Get scheduled agent details

`GET /agent/schedules/{scheduleId}`

Retrieve detailed information about a specific scheduled agent, including its configuration, history, and next scheduled run time.

### Request

| Parameter | Type | Description |
|-----------|------|-------------|
| Authorization | string (required) | Authentication via a Warp API key |
| scheduleId | string (required) | The unique identifier of the scheduled agent |

### Response

| Status | Description |
|--------|-------------|
| 200 | Scheduled agent details (`application/json`) |
| 401 | Authentication required (`application/json`) |
| 403 | No permission to access schedule (`application/json`) |

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier for the scheduled agent |
| name | string | Human-readable name for the schedule |
| cron_schedule | string | Cron expression defining when the agent runs (e.g., "0 9 * * *" for daily at 9am UTC) |
| enabled | boolean | Whether the schedule is currently active |
| prompt | string | The prompt/instruction for the agent to execute |
| last_spawn_error | string · nullable | Error message from the last failed spawn attempt, if any |
| created_at | string · date-time | Timestamp when the schedule was created (RFC3339) |
| updated_at | string · date-time | Timestamp when the schedule was last updated (RFC3339) |

## Update a scheduled agent

`PUT /agent/schedules/{scheduleId}`

Update an existing scheduled agent's configuration. All fields except agent_config are required.

### Request

| Parameter | Type | Description |
|-----------|------|-------------|
| Authorization | string (required) | Authentication via a Warp API key |
| scheduleId | string (required) | The unique identifier of the scheduled agent |

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Human-readable name for the schedule |
| cron_schedule | string | Yes | Cron expression defining when the agent runs |
| prompt | string | No | The prompt/instruction for the agent to execute. Required unless `agent_config.skill_spec` is provided. |
| enabled | boolean | Yes | Whether the schedule should be active |
| agent_uid | string | No | Agent UID to use as the execution principal for this schedule. Only valid for team-owned schedules. |

### Response

| Status | Description |
|--------|-------------|
| 200 | Scheduled agent updated successfully (`application/json`) |
| 401 | Authentication required (`application/json`) |
| 403 | No permission to update schedule (`application/json`) |

## Delete a scheduled agent

`DELETE /agent/schedules/{scheduleId}`

Delete a scheduled agent. This will stop all future scheduled runs.

### Request

| Parameter | Type | Description |
|-----------|------|-------------|
| Authorization | string (required) | Authentication via a Warp API key |
| scheduleId | string (required) | The unique identifier of the scheduled agent |

### Response

| Status | Description |
|--------|-------------|
| 200 | Scheduled agent deleted successfully (`application/json`) |
| 401 | Authentication required (`application/json`) |
| 403 | No permission to delete schedule (`application/json`) |

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | Whether the deletion was successful |

## Pause a scheduled agent

`POST /agent/schedules/{scheduleId}/pause`

Pause a scheduled agent. The agent will not run until resumed.

### Request

| Parameter | Type | Description |
|-----------|------|-------------|
| Authorization | string (required) | Authentication via a Warp API key |
| scheduleId | string (required) | The unique identifier of the scheduled agent |

### Response

| Status | Description |
|--------|-------------|
| 200 | Scheduled agent paused successfully (`application/json`) |
| 401 | Authentication required (`application/json`) |
| 403 | No permission to pause schedule (`application/json`) |

## Resume a scheduled agent

`POST /agent/schedules/{scheduleId}/resume`

Resume a paused scheduled agent. The agent will start running according to its cron schedule.

### Request

| Parameter | Type | Description |
|-----------|------|-------------|
| Authorization | string (required) | Authentication via a Warp API key |
| scheduleId | string (required) | The unique identifier of the scheduled agent |

### Response

| Status | Description |
|--------|-------------|
| 200 | Scheduled agent resumed successfully (`application/json`) |
| 401 | Authentication required (`application/json`) |
| 403 | No permission to resume schedule (`application/json`) |

#api-reference #schedules #cron #agent-scheduling
