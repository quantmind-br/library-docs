---
title: Get User
url: https://platform.claude.com/docs/en/api/admin/users/retrieve.md
source: llms
fetched_at: 2026-04-16T22:51:36.780908768-03:00
rendered_js: false
word_count: 43
summary: This API endpoint provides a method to retrieve detailed user profile information within an organization using a specific user ID.
tags:
    - api-reference
    - user-management
    - organization-data
    - endpoint-specification
category: api
---

## Retrieve

**get** `/v1/organizations/users/{user_id}`

Get User

### Path Parameters

- `user_id: string`

  ID of the User.

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