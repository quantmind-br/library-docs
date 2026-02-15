---
title: Tags | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/tags
source: sitemap
fetched_at: 2026-02-15T09:12:41.890087-03:00
rendered_js: false
word_count: 182
summary: This document outlines the API endpoints for managing media tags, including functionality to retrieve, create, and delete tags associated with specific media assets.
tags:
    - media-management
    - api-endpoints
    - tagging
    - authorization
    - rest-api
category: api
---

### Show all tags for the given media

AuthorizationstringRequired

media\_idinteger · int64Required

201

The tag object(s) for the given media.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

### Create a new tag for the given media

AuthorizationstringRequired

media\_idinteger · int64Required

201

The tag object that was created.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

AuthorizationstringRequired

media\_idinteger · int64Required

tag\_idinteger · int64Required

200

The media tag has been deleted.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media or tag ID was not found.

/media/{media\_id}/tags/{tag\_id}

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).