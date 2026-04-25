---
title: Update User
url: https://platform.claude.com/docs/en/api/admin/users/update.md
source: llms
fetched_at: 2026-04-16T23:03:52.409647445-03:00
rendered_js: false
word_count: 67
summary: This document defines the endpoint for updating user roles within an organization via a POST request.
tags:
    - api-reference
    - user-management
    - endpoint-specification
    - rest-api
category: api
---

## Update

**post** `/v1/organizations/users/{user_id}`

Update User

### Path Parameters

- `user_id: string`

  ID of the User.

### Body Parameters

- `role: "user" or "developer" or "billing" or 2 more`

  New role for the User. Cannot be "admin".

  - `"user"`

  - `"developer"`

  - `"billing"`

  - `"claude_code_user"`

  - `"managed"`

### Returns

- `User = object { id, added_at, email, 3 more }`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: "user" or "developer" or "billing" or 3 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

    - `"managed"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    - `"user"`