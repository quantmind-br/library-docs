---
title: Open Access Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/reference/create-partner
source: crawler
fetched_at: 2026-02-27T23:42:05.142801-03:00
rendered_js: true
word_count: 104
summary: This document describes the API endpoint for creating a new partner within the Spotify Open Access system to enable user account linking and entitlement management.
tags:
    - spotify-api
    - open-access
    - partner-management
    - account-linking
    - jwt-authentication
category: api
---

Open Access •References / Create new partner

## Create new partner

**Required scope:** `soa-create-partner`

Create a new partner so that users of that partner can be linked to Spotify users. Returns the partner ID to use in subsequent requests managing partner information, user linking, and entitlements.

## Request

This endpoint requires the payload to be [provided as a JWT](https://developer.spotify.com/documentation/open-access/concepts#jwt--jws-usage).

The payload has the following fields:

PropertyTypeRequiredDescriptionpartner\_namestringyesThe display name of the partner to createentrypoint\_urlstringyesUsed to initiate the account linking flow from Spotify surfaces. Must be served over SSL (https). See [Entrypoint URL](https://developer.spotify.com/documentation/open-access/concepts#entrypoint-url)

## Response

On success the response contains the ID of the newly created partner

```
curl --request POST \
  --url https://open-access.spotify.com/api/v1/create-partner \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"partner_id": "1234567890aBcDeFgHiJkL"}
```