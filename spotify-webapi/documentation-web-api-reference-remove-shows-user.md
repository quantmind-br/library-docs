---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/remove-shows-user
source: crawler
fetched_at: 2026-02-27T23:46:57.465566-03:00
rendered_js: false
word_count: 137
summary: This document provides the API reference for the deprecated endpoint used to delete one or more shows from a Spotify user's library. It specifies the required query parameters and notes that the functionality has been superseded by a newer library management endpoint.
tags:
    - spotify-api
    - shows
    - user-library
    - deprecated
    - delete-method
category: api
---

Web API •References / Shows / Remove User's Saved Shows

## Remove User's Saved Shows

Deprecated

Delete one or more shows from current Spotify user's library.

**Note:** This endpoint is deprecated. Use [Remove Items from Library](https://developer.spotify.com/documentation/web-api/reference/remove-library-items) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the shows. Maximum: 50 IDs.
  
  Example: `ids=5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ`
- An [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). If a country code is specified, only content that is available in that market will be returned.  
  If a valid user access token is specified in the request header, the country associated with the user account will take priority over this parameter.  
  ***Note**: If neither market or user country are provided, the content is considered unavailable for the client.*  
  Users can view the country that is associated with their account in the [account settings](https://www.spotify.com/account/overview/).
  
  Example: `market=ES`

## Response

## Response sample

```
empty response
```