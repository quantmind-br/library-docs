---
title: not_authorized | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/not-authorized
source: sitemap
fetched_at: 2026-04-29T15:05:15.093859425-03:00
rendered_js: false
word_count: 162
summary: This document explains the causes and resolution steps for the not_authorized API error, which signifies insufficient permissions for a requested operation.
tags:
    - api-error
    - access-control
    - permissions
    - troubleshooting
    - http-403
    - authorization
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The `not_authorized` error occurs when the authenticated principal (user or API key) does not have sufficient permissions to perform the requested operation.

## Details

| Field | Value |
|-------|-------|
| **HTTP Status** | `403 Forbidden` |
| **Retryable** | No |
| **Task State** | FAILED |

## When does this occur?

This error is returned when:

- You attempt to access a resource owned by another team or user
- Your API key does not have the required scope for the operation
- You try to perform an admin-level operation without admin privileges
- A team-level operation is attempted by a user who is not a member of the team

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/not-authorized",
  "title": "You do not have permission to perform this operation.",
  "status": 403,
  "instance": "/api/v1/agent/tasks/abc123/cancel",
  "error": "You do not have permission to perform this operation.",
  "retryable": false
}
```

## How to resolve

1. Verify that the API key or user account belongs to the correct team.
2. Check that your role has the necessary permissions for the operation.
3. Contact a team admin if you need elevated access.

## Related

[Previous: external_authentication_required](https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/external-authentication-required) · [Next: invalid_request](https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/invalid-request)