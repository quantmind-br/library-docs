---
title: Delete Invite
url: https://platform.claude.com/docs/en/api/admin/invites/delete.md
source: llms
fetched_at: 2026-04-16T22:44:44.606846678-03:00
rendered_js: false
word_count: 32
summary: This document defines the API endpoint for deleting a specific organization invitation using its unique identifier.
tags:
    - api-reference
    - organization-management
    - http-delete
    - endpoint-specification
category: api
---

## Delete

**delete** `/v1/organizations/invites/{invite_id}`

Delete Invite

### Path Parameters

- `invite_id: string`

  ID of the Invite.

### Returns

- `id: string`

  ID of the Invite.

- `type: "invite_deleted"`

  Deleted object type.

  For Invites, this is always `"invite_deleted"`.

  - `"invite_deleted"`