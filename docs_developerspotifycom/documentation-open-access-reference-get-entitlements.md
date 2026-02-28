---
title: Open Access Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/reference/get-entitlements
source: crawler
fetched_at: 2026-02-27T23:39:26.762626-03:00
rendered_js: true
word_count: 55
summary: This document outlines the technical specifications for the Spotify Open Access API endpoint used to retrieve a user's current entitlements.
tags:
    - spotify-open-access
    - entitlements
    - api-reference
    - user-access
    - jwt-authentication
category: api
---

Open Access •References / Get user entitlements

## Get user entitlements

**Required scope:** `soa-manage-entitlements`

## Request

This endpoint requires the payload to be [provided as a JWT](https://developer.spotify.com/documentation/open-access/concepts#jwt--jws-usage).

The payload has the following fields:

## Response

On success the response contains the ID of the newly created partner

- entitlementsarray of strings
  
  The entitlements this user currently has

```
curl --request POST \
  --url https://open-access.spotify.com/api/v1/get-entitlements \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"entitlements": ["entitlement-1", "entitlement-2", "entitlement-3"]}
```