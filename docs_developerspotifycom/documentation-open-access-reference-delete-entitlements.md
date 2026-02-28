---
title: Open Access Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/reference/delete-entitlements
source: crawler
fetched_at: 2026-02-27T23:39:25.24913-03:00
rendered_js: true
word_count: 58
summary: This document specifies the Spotify Open Access API endpoint for removing user entitlements, detailing the required scope and JWT payload parameters.
tags:
    - spotify-open-access
    - user-entitlements
    - api-reference
    - jwt
    - authorization
category: api
---

Open Access •References / Removes user entitlements

## Removes user entitlements

**Required scope:** `soa-manage-entitlements`

## Request

This endpoint requires the payload to be [provided as a JWT](https://developer.spotify.com/documentation/open-access/concepts#jwt--jws-usage).

The payload has the following fields:

PropertyTypeRequiredDescriptionpartner\_idstringyes[Partner ID](https://developer.spotify.com/documentation/open-access/concepts#partner-id)partner\_user\_idstringyes[Partner User ID](https://developer.spotify.com/documentation/open-access/concepts#partner-user-id)entitlementsarray\[string]yesThe Entitlement IDs to remove from this user

## Response

A successful response will have HTTP status code 200 and an empty payload.

```
curl --request POST \
  --url https://open-access.spotify.com/api/v1/delete-entitlements \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```