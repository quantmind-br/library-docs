---
title: Remove User
url: https://platform.claude.com/docs/en/api/admin/users/delete.md
source: llms
fetched_at: 2026-04-16T22:59:15.564703592-03:00
rendered_js: false
word_count: 32
summary: This document defines the endpoint structure and response schema for deleting a specific user within an organization.
tags:
    - api-reference
    - user-management
    - http-delete
    - endpoint-definition
category: api
---

## Delete

**delete** `/v1/organizations/users/{user_id}`

Remove User

### Path Parameters

- `user_id: string`

  ID of the User.

### Returns

- `id: string`

  ID of the User.

- `type: "user_deleted"`

  Deleted object type.

  For Users, this is always `"user_deleted"`.

  - `"user_deleted"`