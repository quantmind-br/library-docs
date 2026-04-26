---
title: Beta Libraries Accesses
url: https://docs.mistral.ai/api/endpoint/beta/libraries/accesses
source: sitemap
fetched_at: 2026-04-26T04:01:31.504007618-03:00
rendered_js: false
word_count: 108
summary: API endpoints for managing entity access levels within a library, including listing, creating, updating, and deleting access permissions.
tags:
    - library-access
    - entity-permissions
    - access-control
    - resource-sharing
    - authorization-management
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## List Library Access

`GET /v1/libraries/{library_id}/accesses`

Returns all entities with access to the library and their access levels.

---

## Create or Update Access

`PUT /v1/libraries/{library_id}/accesses`

Set the access level for an entity. Requires library ownership. Owners cannot modify their own role. Libraries cannot be shared outside the organization.

| Param | Type | Description |
|-------|------|-------------|
| `entity_type` | string | Type of entity (user, organization) |
| `entity_id` | string | ID of the entity |
| `access_level` | string | Access level to assign |

---

## Delete Access

`DELETE /v1/libraries/{library_id}/accesses`

Remove an entity's access. Owners cannot delete their own access. Requires ownership.

| Param | Type | Description |
|-------|------|-------------|
| `entity_type` | string | Type of entity |
| `entity_id` | string | ID of the entity |

#library-access #entity-permissions #access-control
