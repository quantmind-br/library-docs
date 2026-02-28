---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/save-shows-user
source: crawler
fetched_at: 2026-02-27T23:46:55.622505-03:00
rendered_js: false
word_count: 61
summary: This document describes a deprecated Spotify Web API endpoint for saving one or more shows to a user's library and directs users to the updated alternative.
tags:
    - spotify-api
    - web-api
    - show-management
    - user-library
    - deprecated-endpoint
category: reference
---

Web API •References / Shows / Save Shows for Current User

## Save Shows for Current User

Deprecated

Save one or more shows to current Spotify user's library.

**Note:** This endpoint is deprecated. Use [Save Items to Library](https://developer.spotify.com/documentation/web-api/reference/save-library-items) instead.

Authorization scopes

## Request

- idsstring
  
  Required
  
  A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the shows. Maximum: 50 IDs.
  
  Example: `ids=5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ`

## Response

Show saved