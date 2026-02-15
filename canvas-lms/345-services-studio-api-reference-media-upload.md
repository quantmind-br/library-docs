---
title: Media Upload | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/media_upload
source: sitemap
fetched_at: 2026-02-15T09:12:21.467084-03:00
rendered_js: false
word_count: 606
summary: This document provides technical details for API endpoints used to create media from URLs, generate file upload URLs, and finalize media uploads within specific collections or user libraries.
tags:
    - media-upload
    - api-endpoints
    - url-import
    - media-management
    - auto-captioning
    - external-media
category: api
---

### Create a new media in the specified collection from an existing file accessible by URL

AuthorizationstringRequired

collection\_idinteger · int64Required

urlstringRequired

The originating URL where the media can be retrieved.

Pattern: `^http[s]?:\/?\/`

titlestringOptional

The title of the media. Required for non-external media.

descriptionstringOptional

The description of the media.

auto\_captionbooleanOptional

Whether to request auto-captioning for the media (false by default). This option is only available if auto-captioning is enabled for your account.

Default: `false`

user\_idinteger · int64Optional

An admin user can create the media on behalf of a user by specifying the user ID.

is\_externalbooleanOptional

Whether the media is external (false by default). Only YouTube and Vimeo URLs are supported.

Default: `false`

201

The media has been uploaded.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The collection was not found by ID.

422

Invalid collection\_id is provided.

501

Auto-captioning was requested but is not enabled for the account.

/collections/{collection\_id}/media

### Create a new media in "My Uploads" or specified collection from an existing file accessible by URL

AuthorizationstringRequired

An object containing the necessary information for external media creation

urlstringRequired

The originating URL where the media can be retrieved.

Pattern: `^http[s]?:\/?\/`

titlestringOptional

The title of the media. Required for non-external media.

user\_idintegerOptional

ID of the user to upload the media on behalf of. if not provided, the video will be uploaded to requestor's user library

descriptionstringOptional

The description of the media.

collection\_idintegerOptional

The ID of a collection, user\_id and collection\_id can not be sent together as if user\_id is provided the media will be uploaded to user's user library

auto\_captionbooleanOptional

Whether to request auto-captioning for the media (false by default). This option is only available if auto-captioning is enabled for your account.

is\_externalbooleanOptional

Whether the media is external or not (false by default). Only YouTube and Vimeo are supported.

201

The media object that was created.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

501

Auto-captioning was requested but is not enabled for the account.

### Generate a URL to which a new media can be uploaded

This URL can be used in a PUT request to upload a local file, ex: curl -T /path/to/local/media.file 'URL'

AuthorizationstringRequired

An object containing the necessary information media creation

user\_idintegerOptional

ID of the user to upload the media on behalf of

201

The media upload URL has been generated.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The user was not found by id.

422

Invalid user\_id is provided.

Signifies that a media file has been uploaded to a previously-created upload URL and is ready to appear in "My Uploads"

AuthorizationstringRequired

media\_idinteger · int64Required

An object containing the necessary information for media creation

descriptionstringOptional

The description of the media.

auto\_captionbooleanOptional

Whether to request auto-captioning for the media (false by default). This option is only available if auto-captioning is enabled for your account.

200

The media object that was created.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

409

This upload has already been completed.

501

Auto-captioning was requested but is not enabled for the account.

/media/uploads/{media\_id}/complete

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).