---
title: Account | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/account
source: sitemap
fetched_at: 2026-02-15T09:15:06.815042-03:00
rendered_js: false
word_count: 668
summary: This document outlines API endpoints for managing account-level settings, branding assets, and curators, as well as searching for accounts within a learning object repository.
tags:
    - canvas-api
    - account-settings
    - branding-management
    - curator-api
    - rest-endpoints
    - account-search
category: api
---

Gets settings on an account. Only Canvas Administrators are allowed to perform this action.

**Example:** `curl -X GET -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" "https://lor.instructure.com/api/account/settings"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

200

Account settings retrieved successfully

Update settings on an account. Only Canvas Administrators are allowed to perform this action.

**Example:** `curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data '{"canShowPublic":true, "canSharePublic":"false"}' "https://lor.instructure.com/api/account/settings"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

canShowPublicbooleanOptional

If true, show publicly shared resources in search results.

canSharePublicbooleanOptional

If true, allow users to share resources publicly.

canShowFeaturedbooleanOptional

If true, it will show featured resources if there are any.

showCuratedResourcesFirstbooleanOptional

If true, resources marked as CURATED will be shown firsts on search results

showFederalStandardsbooleanOptional

If true, allow users to use federal outcomes tagging

showStateStandardsbooleanOptional

If true, allow users to use state outcomes tagging

stateStandardstring · min: 2 · max: 2Optional

Which state the standards should reflect. Must be a valid postal abbreviation or "NONE" if you wish to not include a state

allowApprovedContentbooleanOptional

If true, allow curators to allow approved content

### Post a Custom Branding Icon

/api/account/settings/branding

Post a custom branding image to be displayed on account curated content. The image needs to be a PNG, GIF, or JPEG. Branding must be uploaded as multipart/form-data.

**Example:** `curl -X POST -H "X-Session-ID: 0123456789" -F "thumbnail=@example.png" "https://lor.instructure.com/api/account/settings/branding"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

thumbnailstring · binaryOptional

The branding image file (PNG, GIF, or JPEG)

200

Branding image uploaded successfully

/api/account/settings/branding

### Reset Custom Branding Icon to Default Image

/api/account/settings/branding

Reset custom branding image to default whiteCheckmark icon.

**Example:** `curl -X DELETE -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/account/settings/branding"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

200

Branding image reset to default

/api/account/settings/branding

### Add a curator to the Account Settings field

/api/account/settings/curators

Add a new curator to the account settings.

**Example:** `curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data '{"userId":"UUID_HERE"}' "https://lor.instructure.com/api/account/settings/curators"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringOptional

The uuid for the user to add

200

Curator added successfully

204

No Content (when a curator has already been added)

/api/account/settings/curators

### Deletes a curator from the Account

/api/account/settings/curators/{userId}

Deletes an existing curator from the account. Only Canvas Administrators are allowed to perform this action.

**Example:** `* curl -X DELETE -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" "https://lor.instructure.com/api/account/settings/curators/userId"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringRequired

The UUID of the user to find and delete from the curators array

/api/account/settings/curators/{userId}

Search through a list of all of the accounts in commons.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/account?q=arizona&includePublicOnly=true"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

qstring · min: 3Required

The text to search for in the name of the accounts. The results will be empty until the minimum length of 3 characters is satisfied.

cursorstringOptional

An identifier from a prior query to continue retrieving results for.

includePublicOnlybooleanOptional

Whether or not to include publicOnly accounts in the search.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).