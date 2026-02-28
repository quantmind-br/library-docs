---
title: Open Access Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/reference/replace-entitlements
source: crawler
fetched_at: 2026-02-27T23:39:25.032745-03:00
rendered_js: true
word_count: 56
summary: This document specifies the technical details for the Spotify Open Access API endpoint used to replace a user's entitlements using a JWT-secured request.
tags:
    - spotify-open-access
    - api-endpoint
    - user-entitlements
    - jwt-authentication
    - entitlements-management
category: api
---

Open Access •References / Replace user entitlements

## Replace user entitlements

**Required scope:** `soa-manage-entitlements`

## Request

POST/replace-entitlements

This endpoint requires the payload to be [provided as a JWT](https://developer.spotify.com/documentation/open-access/concepts#jwt--jws-usage).

The payload has the following fields:

PropertyTypeRequiredDescriptionpartner\_idstringyes[Partner ID](https://developer.spotify.com/documentation/open-access/concepts#partner-id)partner\_user\_idstringyes[Partner User ID](https://developer.spotify.com/documentation/open-access/concepts#partner-user-id)entitlementsarray\[string]yesEntitlment IDs for this user

## Response

A successful response will have HTTP status code 200 and an empty payload.

```
curl --request POST \
  --url https://open-access.spotify.com/api/v1/replace-entitlements \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```