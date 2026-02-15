---
title: Transfer Media | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/transfer_media
source: sitemap
fetched_at: 2026-02-15T09:12:44.158693-03:00
rendered_js: false
word_count: 128
summary: This document describes an API endpoint used to transfer ownership of all unshared media objects and collections from one user to another.
tags:
    - media-transfer
    - user-ownership
    - api-endpoint
    - content-management
    - access-control
category: api
---

### Transfer all media owned by one user to another

The endpoint transfers all not shared media objects owned by the user to a new owner. We transfer the media objects themselves, all perspectives stored in the "My Library" and in custom collections.

AuthorizationstringRequired

from\_user\_idintegerRequired

to\_user\_idintegerRequired

200

The media has been successfully transferred to the target user.

400

If users are not found with the provided ids, the endpoint returns HTTP 400.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

422

Invalid user\_id is provided.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).