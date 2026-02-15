---
title: Captions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/captions
source: sitemap
fetched_at: 2026-02-15T09:12:28.587521-03:00
rendered_js: false
word_count: 203
summary: This document outlines API endpoints for managing media captions, including methods for listing existing captions, uploading new caption files, and downloading specific files.
tags:
    - api-endpoints
    - media-management
    - caption-files
    - rest-api
    - authentication
    - error-handling
category: api
---

### List all available captions for the given media

AuthorizationstringRequired

media\_idinteger · int64Required

200

The list of captions that are available for the media.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

422

Invalid media\_id is provided.

/media/{media\_id}/caption\_files

### Create a new caption for the given media

AuthorizationstringRequired

media\_idinteger · int64Required

srclangstringRequired

The ISO code for the language of the caption.

caption\_filestringRequired

201

The caption object that was created.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

422

Invalid media\_id is provided.

/media/{media\_id}/caption\_files

AuthorizationstringRequired

caption\_file\_idinteger · int64Required

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The caption was not found by id.

422

Invalid caption\_file\_id is provided.

/caption\_files/{caption\_file\_id}/download

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).