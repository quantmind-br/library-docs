---
title: Delete Workspace Member
url: https://platform.claude.com/docs/en/api/admin/workspaces/members/delete.md
source: llms
fetched_at: 2026-04-16T22:46:26.421109583-03:00
rendered_js: false
word_count: 46
summary: This documentation specifies the endpoint structure, parameters, and return values for deleting a member from a specific workspace.
tags:
    - api-reference
    - workspace-management
    - user-deletion
    - rest-endpoint
category: api
---

## Delete

**delete** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

- `user_id: string`

  ID of the User.

### Returns

- `type: "workspace_member_deleted"`

  Deleted object type.

  For Workspace Members, this is always `"workspace_member_deleted"`.

  - `"workspace_member_deleted"`

- `user_id: string`

  ID of the User.

- `workspace_id: string`

  ID of the Workspace.