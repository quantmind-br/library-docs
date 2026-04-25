---
title: Get Current Organization
url: https://platform.claude.com/docs/en/api/admin/organizations/me.md
source: llms
fetched_at: 2026-04-16T22:49:32.110076332-03:00
rendered_js: false
word_count: 29
summary: This API endpoint retrieves details of the organization linked to an authenticated API key.
tags:
    - api-endpoint
    - organizations
    - authentication-context
    - json-response
category: api
---

## Me

**get** `/v1/organizations/me`

Retrieve information about the organization associated with the authenticated API key.

### Returns

- `Organization = object { id, name, type }`

  - `id: string`

    ID of the Organization.

  - `name: string`

    Name of the Organization.

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

    - `"organization"`