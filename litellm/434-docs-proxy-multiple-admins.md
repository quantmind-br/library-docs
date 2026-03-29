---
title: ✨ Audit Logs | liteLLM
url: https://docs.litellm.ai/docs/proxy/multiple_admins
source: sitemap
fetched_at: 2026-01-21T19:53:06.668023977-03:00
rendered_js: false
word_count: 93
summary: This document explains how Proxy Admins can use audit logs to track entity changes and perform management actions on behalf of users for compliance and monitoring purposes.
tags:
    - audit-logs
    - proxy-admin
    - compliance
    - management-api
    - litellm
    - user-impersonation
category: guide
---

As a Proxy Admin, you can check if and when a entity (key, team, user, model) was created, updated, deleted, or regenerated, along with who performed the action. This is useful for auditing and compliance.

In this example, we will delete a key.

On the LiteLLM UI, navigate to Logs -&gt; Audit Logs. You should see the audit log for the key deletion.

Call management endpoints on behalf of a user. (Useful when connecting proxy to your development platform).

Set the 'user\_id' in request headers, when calling a management endpoint. [View Full List](https://litellm-api.up.railway.app/#/team%20management).

```
{
   "id": "bd136c28-edd0-4cb6-b963-f35464cf6f5a",
   "updated_at": "2024-06-08 23:41:14.793",
   "changed_by": "krrish@berri.ai", # 👈 CHANGED BY
   "changed_by_api_key": "example-api-key-123",
   "action": "updated",
   "table_name": "LiteLLM_TeamTable",
   "object_id": "8bf18b11-7f52-4717-8e1f-7c65f9d01e52",
   "before_value": {
     "spend": 0,
     "max_budget": 0,
   },
   "updated_values": {
     "team_id": "8bf18b11-7f52-4717-8e1f-7c65f9d01e52",
     "max_budget": 2000 # 👈 CHANGED TO
   },
 }
```