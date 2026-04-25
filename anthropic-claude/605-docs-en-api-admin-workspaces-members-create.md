---
title: Create Workspace Member
url: https://platform.claude.com/docs/en/api/admin/workspaces/members/create.md
source: llms
fetched_at: 2026-04-16T22:42:54.808730959-03:00
rendered_js: false
word_count: 64
summary: This document defines the API endpoint for creating a new member within a specific workspace, detailing required parameters and response structures.
tags:
    - api-reference
    - workspace-management
    - user-roles
    - endpoint-definition
category: api
---

## Create

**post** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

### Body Parameters

- `user_id: string`

  ID of the User.

- `workspace_role: "workspace_user" or "workspace_developer" or "workspace_admin"`

  Role of the new Workspace Member. Cannot be "workspace_billing".

  - `"workspace_user"`

  - `"workspace_developer"`

  - `"workspace_admin"`

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