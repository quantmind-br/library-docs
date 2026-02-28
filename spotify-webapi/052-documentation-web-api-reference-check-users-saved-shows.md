---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-users-saved-shows
source: crawler
fetched_at: 2026-02-27T23:46:57.504805-03:00
rendered_js: false
word_count: 70
summary: This document describes a deprecated Spotify Web API endpoint used to verify if one or more shows are saved in the current user's library.
tags:
    - spotify-api
    - web-api
    - user-library
    - shows
    - deprecated
category: reference
---

Web API •References / Shows / Check User's Saved Shows

## Check User's Saved Shows

Deprecated

Check if one or more shows is already saved in the current Spotify user's library.

**Note:** This endpoint is deprecated. Use [Check User's Saved Items](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) instead.

Authorization scopes

## Request

- idsstring
  
  Required
  
  A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the shows. Maximum: 50 IDs.
  
  Example: `ids=5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ`

## Response

Array of booleans

An array of:

Example: `[false,true]`