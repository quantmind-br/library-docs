---
title: Media | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/media
source: sitemap
fetched_at: 2026-02-15T09:10:53.409806-03:00
rendered_js: false
word_count: 1099
summary: This document defines a series of API endpoints for searching, managing, archiving, and controlling access permissions for media assets.
tags:
    - media-api
    - content-management
    - access-control
    - search-operations
    - lti-integration
    - api-reference
category: api
---

### Search media by the given query parameters. If multiple options are provided, we will use a logical AND operation when searching!

AuthorizationstringRequired

titlestringOptional

Substring of the media title you want to search for.

min\_sizeintegerOptional

Minimum size of the media in bytes.

max\_sizeintegerOptional

Maximum size of the media in bytes.

start\_datestring · dateOptional

Start of the creation date (inclusive). Format: YYYY-MM-DD.

end\_datestring · dateOptional

End of the creation date (inclusive). Format: YYYY-MM-DD.

last\_viewed\_start\_datestring · dateOptional

Start of the last viewed date (inclusive). Format: YYYY-MM-DD.

last\_viewed\_end\_datestring · dateOptional

End of the last viewed date (inclusive). Format: YYYY-MM-DD.

last\_viewed\_by\_student\_start\_datestring · dateOptional

Start of the last viewed by student date (inclusive). Format: YYYY-MM-DD.

last\_viewed\_by\_student\_end\_datestring · dateOptional

End of the last viewed by student date (inclusive). Format: YYYY-MM-DD.

ownerstring · emailOptional

Email address of the owner of the media.

tagstringOptional

The full name of the tag, you want to list media objects for.

sourcestring · enumOptional

The source of the media you want to list media objects for.

Possible values:

pageintegerOptional

The page to retrieve. Default: 1.

Default: `1`

per\_pageinteger · max: 50Optional

The number of results per page. Default: 20, Max: 50.

Default: `20`

200

The list of media objects that matched the given query.

401

Authorization information is missing or invalid.

AuthorizationstringRequired

media\_idinteger · int64Required

200

The media object that was requested.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media ID was not found.

### Deletes the specified media object and all related perspectives.

AuthorizationstringRequired

media\_idinteger · int64Required

200

The media object that was deleted.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media ID was not found.

### Archives the specified media object and all related perspectives.

AuthorizationstringRequired

media\_idinteger · int64Required

200

The media object that was archived.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media ID was not found.

/media/{media\_id}/archive

### Get a list of courses which contains the media

AuthorizationstringRequired

media\_idinteger · int64Required

200

The list of courses that were requested.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

422

Invalid media\_id is provided.

/media/{media\_id}/courses

### Adds a Media to a Course Collection for the given course\_id. Returns the URL to LTI-launch the embedded media.

AuthorizationstringRequired

media\_idinteger · int64Required

An object containing the necessary information for embedding the media

course\_idintegerRequired

Id of the course to embed the media in.

embed\_typestringRequired

The type of the embed. Studio uses "embed" to create embedding with media tabs and "bare\_embed" to create one with only the media player.

downloadablebooleanOptional

A flag that controlls if the embedded media should be downloadable or not.

200

The URL to LTI-launch the embedded media. Please note that the URL in the result will work only if it is called with the proper LTI params.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

422

Invalid media\_id is provided.

/media/{media\_id}/create\_embed

### Download best or specified version of a media

AuthorizationstringRequired

media\_idinteger · int64Required

qualitystring · enumOptional

The quality the user wants to download

Possible values:

302

Redirects to the Notorious URL from where the media can be downloaded. The URL is only valid for 24 hours.

401

Authorization information is missing or invalid.

403

If a user without permission tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media or its version was not found.

422

Invalid media\_id is provided or the media is external.

/media/{media\_id}/download

### Get users and groups the media is shared with directly

AuthorizationstringRequired

media\_idinteger · int64Required

200

List of users and groups extended with permission type.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

422

Invalid media\_id is provided.

/media/{media\_id}/permissions

### Add permissions to a media

AuthorizationstringRequired

media\_idinteger · int64Required

200

Permissions were added, the updated list of permissions is returned.

400

One ore more permission was not found or can not be created, because already exists

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

422

Invalid media\_id is provided.

/media/{media\_id}/permissions

### Get perspectives belonging to a media

AuthorizationstringRequired

media\_idinteger · int64Required

200

List of perspectives extended with collection.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

422

Invalid media\_id is provided.

/media/{media\_id}/perspectives

### Get a media's sources by its id

AuthorizationstringRequired

media\_idinteger · int64Required

200

The media sources that were requested.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

/media/{media\_id}/sources

### Unarchives the specified media object and all related perspectives.

AuthorizationstringRequired

media\_idinteger · int64Required

collection\_idinteger · int64Optional

Move the media to this collection after unarchiving.

200

The media object that was archived.

401

Authorization information is missing or invalid.

403

If a user without proper permissions tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media ID was not found.

/media/{media\_id}/unarchive

### Get a list of users, who have access to the media

AuthorizationstringRequired

media\_idinteger · int64Required

min\_permissionstring · enumOptional

Filter users by a minimum permission level. If provided, only users with this permission or higher will be returned. The permissions are hierarchical: 'edit' includes 'view', and 'view' includes 'access'.

Default: `access`Possible values:

200

The users who have access to the media.

401

Authorization information is missing or invalid.

403

If a user without permission tries to call this endpoint, the call is rejected with 403 Forbidden.

404

The media was not found by ID.

422

Invalid media\_id is provided.

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).