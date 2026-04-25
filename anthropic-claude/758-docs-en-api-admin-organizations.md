---
title: Organizations
url: https://platform.claude.com/docs/en/api/admin/organizations.md
source: llms
fetched_at: 2026-04-16T22:59:12.018525151-03:00
rendered_js: false
word_count: 47
summary: This document defines the API endpoint and data structure for retrieving information about the authenticated organization.
tags:
    - api-reference
    - organizations
    - endpoint-specification
    - object-schema
category: api
---

# Organizations

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

## Domain Types

### Organization

- `Organization = object { id, name, type }`

  - `id: string`

    ID of the Organization.

  - `name: string`

    Name of the Organization.

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

    - `"organization"`