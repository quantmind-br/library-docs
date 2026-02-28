---
title: Open Access Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/reference/add-entitlements
source: crawler
fetched_at: 2026-02-27T23:39:23.8599-03:00
rendered_js: true
word_count: 51
summary: This document describes the API endpoint for adding entitlements to a user account within the Spotify Open Access framework, detailing the required authentication scope and request payload.
tags:
    - spotify-open-access
    - user-entitlements
    - api-endpoint
    - jwt-authentication
    - partner-integration
category: api
---

Open Access •References / Add user entitlements

## Add user entitlements

**Required scope:** `soa-manage-entitlements`

## Request

This endpoint requires the payload to be [provided as a JWT](https://developer.spotify.com/documentation/open-access/concepts#jwt--jws-usage).

The payload has the following fields:

PropertyTypeRequiredDescriptionpartner\_idstringyes[Partner ID](https://developer.spotify.com/documentation/open-access/concepts#partner-id)partner\_user\_idstringyes[Partner User ID](https://developer.spotify.com/documentation/open-access/concepts#partner-user-id)entitlementsarray\[string]N/Ayes

## Response

A successful response will have HTTP status code 200 and an empty payload.

```
curl --request POST \
  --url https://open-access.spotify.com/api/v1/add-entitlements \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```