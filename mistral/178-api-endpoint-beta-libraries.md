---
title: Beta Libraries
url: https://docs.mistral.ai/api/endpoint/beta/libraries
source: sitemap
fetched_at: 2026-04-26T04:01:29.174236945-03:00
rendered_js: false
word_count: 114
summary: API endpoints for managing libraries, including listing, creating, retrieving, updating, and deleting library resources.
tags:
    - api-documentation
    - library-management
    - rest-api
    - resource-lifecycle
    - endpoint-reference
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Libraries

CRUD API for library resource management.

---

## List Libraries

`GET /v1/libraries`

List all libraries you created or have been shared with you.

---

## Create Library

`POST /v1/libraries`

Create a new library. You become the owner with sole sharing permission. Initially only accessible by you.

---

## Get Library

`GET /v1/libraries/{library_id}`

Get detailed information about a library.

---

## Update Library

`PUT /v1/libraries/{library_id}`

Update library name and description.

---

## Delete Library

`DELETE /v1/libraries/{library_id}`

Delete a library and all its uploaded documents.

#library-management #resource-lifecycle #rest-api
