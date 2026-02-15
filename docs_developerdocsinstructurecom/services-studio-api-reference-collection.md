---
title: Collection | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/collection
source: sitemap
fetched_at: 2026-02-15T09:10:47.803104-03:00
rendered_js: false
word_count: 617
summary: This document defines the REST API endpoints for managing collections, including operations for creation, deletion, archiving, and configuring user permissions.
tags:
    - collections-api
    - rest-api
    - permissions-management
    - resource-archiving
    - content-management
    - api-endpoints
category: api
---

### List all collections the authenticated user has permission to.

AuthorizationstringRequired

pageintegerOptional

The page to retrieve. Default: 1.

Default: `1`

per\_pageinteger · max: 50Optional

The number of results per page. Default: 20, Max: 50.

Default: `20`

200

The collections the authenticated user has permission to.

401

Authorization information is missing or invalid.

### Create a new collection with the specified name

AuthorizationstringRequired

namestringRequired

The name of the collection.

user\_idintegerOptional

ID of the user to create the collection on behalf of. If not provided, the collection will be created in the requestor's library

201

The collection object that was created.

401

Authorization information is missing or invalid.

403

If a user without permission tries to call this endpoint with user\_id parameter, the call is rejected with 403 Forbidden.

404

The user was not found by id.

422

Invalid user\_id is provided.

AuthorizationstringRequired

collection\_idinteger · int64Required

The ID of the collection.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The collection was not found.

422

Invalid collection\_id is provided.

/collections/{collection\_id}

### Deletes the specified collection and all related media and perspectives.

AuthorizationstringRequired

collection\_idinteger · int64Required

The ID of the collection.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The collection was not found.

422

Invalid collection\_id is provided.

/collections/{collection\_id}

### Archives the specified collection and all related media and perspectives.

AuthorizationstringRequired

collection\_idinteger · int64Required

The ID of the collection.

200

The collection was archived.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The collection was not found.

422

Invalid collection\_id is provided.

/collections/{collection\_id}/archive

### List media in a specific collection

AuthorizationstringRequired

collection\_idinteger · int64Required

pageintegerOptional

The page to retrieve. Default: 1.

Default: `1`

per\_pageinteger · max: 50Optional

The number of results per page. Default: 20, Max: 50.

Default: `20`

200

The list of media in a specific collection.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The collection was not found by ID.

/collections/{collection\_id}/media

### Get users and groups who have access to the collection

AuthorizationstringRequired

collection\_idinteger · int64Required

The ID of the collection.

200

List of users and groups extended with permission type.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The collection was not found.

422

Invalid collection\_id is provided.

/collections/{collection\_id}/permissions

### Add permissions to the collection

AuthorizationstringRequired

collection\_idinteger · int64Required

The ID of the collection.

200

Permissions were added, the updated list of permissions is returned.

400

One ore more permission was not found or can not be created, because already exists

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The collection was not found.

422

Invalid collection\_id is provided.

/collections/{collection\_id}/permissions

### Unarchives the specified collection and all related media and perspectives.

AuthorizationstringRequired

collection\_idinteger · int64Required

The ID of the collection.

200

The collection was unarchived.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The collection was not found.

422

Invalid collection\_id is provided.

/collections/{collection\_id}/unarchive

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).