---
title: "Agent"
url: https://docs.warp.dev/reference/api-and-sdk/agent
source: sitemap
fetched_at: 2026-04-29T15:05:08-03:00
rendered_js: false
word_count: 5
summary: This document defines the schema for a run object, detailing the properties related to agent execution, session management, and resource usage tracking.
tags:
    - api-schema
    - json-structure
    - run-metadata
    - agent-configuration
    - execution-tracking
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Agent Schema

```json
{
  "runs": [
    {
      "run_id": "text",
      "title": "text",
      "state": "QUEUED",
      "execution_location": "LOCAL",
      "prompt": "text",
      "created_at": "2026-04-28T19:20:17.535Z",
      "updated_at": "2026-04-28T19:20:17.535Z",
      "started_at": "2026-04-28T19:20:17.535Z",
      "status_message": {
        "message": "text",
        "error_code": "insufficient_credits",
        "retryable": true
      },
      "source": "LINEAR",
      "schedule": {
        "schedule_id": "text",
        "schedule_name": "text",
        "cron_schedule": "text"
      },
      "session_id": "text",
      "session_link": "https://example.com",
      "trigger_url": "https://example.com",
      "creator": {
        "type": "user",
        "uid": "text",
        "display_name": "text",
        "email": "text",
        "photo_url": "https://example.com"
      },
      "request_usage": {
        "inference_cost": 1,
        "compute_cost": 1
      },
      "agent_config": {
        "name": "text",
        "model_id": "text",
        "base_prompt": "text",
        "environment_id": "text",
        "skill_spec": "text",
        "mcp_servers": {
          "ANY_ADDITIONAL_PROPERTY": {
            "warp_id": "text",
            "command": "text",
            "args": [
              "text"
            ],
            "url": "https://example.com",
            "env": {
              "ANY_ADDITIONAL_PROPERTY": "text"
            },
            "headers": {
              "ANY_ADDITIONAL_PROPERTY": "text"
            }
          }
        },
        "computer_use_enabled": true,
        "idle_timeout_minutes": 1,
        "worker_host": "text",
        "harness": {
          "type": "oz"
        },
        "harness_auth_secrets": {
          "claude_auth_secret_name": "text"
        },
        "session_sharing": {
          "public_access": "VIEWER"
        }
      },
      "conversation_id": "text",
      "parent_run_id": "text",
      "is_sandbox_running": true,
      "artifacts": [
        {
          "artifact_type": "PLAN",
          "created_at": "2026-04-28T19:20:17.535Z",
          "data": {
            "artifact_uid": "text",
            "document_uid": "text",
            "notebook_uid": "text",
            "url": "https://example.com",
            "title": "text"
          }
        }
      ],
      "agent_skill": {
        "name": "text",
        "description": "text",
        "full_path": "text",
        "bundled_skill_id": "text"
      },
      "scope": {
        "type": "User",
        "uid": "text"
      }
    }
  ],
  "page_info": {
    "has_next_page": true,
    "next_cursor": "text"
  }
}
```

#reference #api-schema
