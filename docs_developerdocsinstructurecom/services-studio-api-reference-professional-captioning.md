---
title: Professional Captioning | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/professional_captioning
source: sitemap
fetched_at: 2026-02-15T09:12:41.253958-03:00
rendered_js: false
word_count: 469
summary: Technical documentation detailing API endpoints for managing professional caption requests, updating request statuses with file uploads, and configuring captioning service types.
tags:
    - api-reference
    - captioning
    - caption-requests
    - service-management
    - srt-files
    - endpoint-documentation
category: api
---

This endpoint lists caption requests. It works both with auth token and the captioning service auth headers.

AuthorizationstringRequired

providerstring · enumRequired

Provider of the caption. The only option is "professional"

Possible values:

statusstring · enumRequired

Status of the caption request. The only possible value now is "requested"

Possible values:

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

### Send the result of the caption file request.

This endpoint should be used to update a pending caption file request. Each request can be updated once with either fulfilled or failed status.

AuthorizationstringRequired

caption\_file\_request\_idintegerRequired

The id of the caption file request to be updated.

statusstring · enumRequired

Result of the file request.

Possible values:

messagestringOptional

In case the caption creation was not successful you can provide some detail why it could not be completed.

caption\_filestringOptional

The file to be uploaded. The supported file extension is .srt!

202

The results are successfully saved.

400

One ore more required parameters are missing from the request.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

/caption\_file\_requests/{caption\_file\_request\_id}

### The list of active service types

AuthorizationstringRequired

200

The list of active service types user has permission to.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

There is no active captioning service for the account.

/captioning\_service\_types

The endpoint will insert or update a service type for a captioning service. This endpoint only supports IETF language code

AuthorizationstringRequired

keystringRequired

machine readable “id” that will be included with caption file requests when a CaptionService lists available requests.

An object describing the service type

descriptionstringRequired

languagesstring\[]Optional

200

The service type has been updated successfully

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

There is no active captioning service for the account.

/captioning\_service\_types/{key}

This endpoint will delete a service type for a captioning service and will remove the associated captioning roles from it.

AuthorizationstringRequired

keystringRequired

machine readable “id” that will be included with caption file requests when a CaptionService lists available requests.

204

The service type has been deleted successfully

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

There is no active captioning service for the account or the service type does not exist.

/captioning\_service\_types/{key}

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).