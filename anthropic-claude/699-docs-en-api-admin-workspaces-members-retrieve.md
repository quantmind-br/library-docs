---
title: Get Workspace Member
url: https://platform.claude.com/docs/en/api/admin/workspaces/members/retrieve.md
source: llms
fetched_at: 2026-04-16T22:52:18.08609412-03:00
rendered_js: false
word_count: 44
summary: This API documentation defines an endpoint for retrieving specific member details within a workspace, including their assigned roles and IDs.
tags:
    - api-reference
    - workspace-management
    - user-retrieval
    - endpoint-specification
category: api
---

## Retrieve

**get** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

- `user_id: string`

  ID of the User.

### Returns

- `WorkspaceMember = object { type, user_id, workspace_id, workspace_role }`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    - `"workspace_member"`

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: "workspace_user" or "workspace_developer" or "workspace_admin" or "workspace_billing"`

    Role of the Workspace Member.

    - `"workspace_user"`

    - `"workspace_developer"`

    - `"workspace_admin"`

    - `"workspace_billing"`