---
title: Get Workspace
url: https://platform.claude.com/docs/en/api/admin/workspaces/retrieve.md
source: llms
fetched_at: 2026-04-16T22:52:16.459155637-03:00
rendered_js: false
word_count: 43
summary: This document defines the API endpoint and schema for retrieving specific workspace information using a unique identifier.
tags:
    - api-reference
    - workspace-management
    - endpoint-specification
    - json-schema
category: api
---

## Retrieve

**get** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

### Returns

- `Workspace = object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

  - `data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo }`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `UnionMember0 = array of string`

      - `UnionMember1 = "unrestricted"`

        - `"unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `name: string`

    Name of the Workspace.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    - `"workspace"`