---
title: Get Invite
url: https://platform.claude.com/docs/en/api/admin/invites/retrieve.md
source: llms
fetched_at: 2026-04-16T22:50:11.099232379-03:00
rendered_js: false
word_count: 51
summary: This document defines the endpoint and schema for retrieving specific organization invitation details via an ID.
tags:
    - api-reference
    - organizations
    - invitation-management
    - endpoint-definition
category: api
---

## Retrieve

**get** `/v1/organizations/invites/{invite_id}`

Get Invite

### Path Parameters

- `invite_id: string`

  ID of the Invite.

### Returns

- `Invite = object { id, email, expires_at, 4 more }`

  - `id: string`

    ID of the Invite.

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

  - `role: "user" or "developer" or "billing" or 3 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

    - `"managed"`

  - `status: "accepted" or "expired" or "deleted" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"expired"`

    - `"deleted"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    - `"invite"`