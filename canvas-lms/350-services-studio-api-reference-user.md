---
title: User | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/user
source: sitemap
fetched_at: 2026-02-15T08:58:10.525568-03:00
rendered_js: false
word_count: 406
summary: This document outlines API endpoints for managing users, including retrieving their collections and media access, and modifying user roles. It provides technical details on request parameters, authorization requirements, and HTTP response codes.
tags:
    - user-management
    - api-documentation
    - media-access
    - collections
    - role-assignment
    - authentication
    - pagination
category: api
---

### Get all collections the user has access to.

AuthorizationstringRequired

user\_idinteger · int64Required

pageintegerOptional

The page to retrieve. Default: 1.

Default: `1`

per\_pageinteger · max: 50Optional

The number of results per page. Default: 20, Max: 50.

Default: `20`

200

The list of collections the user has access to, with permissions.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

/users/{user\_id}/collections

### Get the user's "My Library" collection.

Returns the user's personal collection (type: user). This is the default collection where users store their personal media.

AuthorizationstringRequired

user\_idinteger · int64Required

200

The user's My Library collection.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

### Get a list of media the user has access to.

AuthorizationstringRequired

user\_idinteger · int64Required

pageintegerOptional

The page to retrieve. Default: 1.

Default: `1`

per\_pageinteger · max: 50Optional

The number of results per page. Default: 20, Max: 50.

Default: `20`

200

The requested media list extended with permission of the user on the media.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

AuthorizationstringRequired

user\_idinteger · int64Required

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

AuthorizationstringRequired

rolestring · enumOptional

A role to filter the users by.

Possible values:

emailstringOptional

Email address of the user.

pageintegerOptional

The page to retrieve. Default: 1.

Default: `1`

per\_pageinteger · max: 50Optional

The number of results per page. Default: 20, Max: 50.

Default: `20`

200

The list of user objects.

400

Required parameter is missing.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

### Add/Remove roles from users

AuthorizationstringRequired

200

Role updates are successfully applied, the updated list of user objects

400

Required parameter is missing.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The user(s) was not found.

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).