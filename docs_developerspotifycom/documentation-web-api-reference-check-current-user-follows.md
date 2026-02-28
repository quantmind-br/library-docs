---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-current-user-follows
source: crawler
fetched_at: 2026-02-27T23:39:18.150124-03:00
rendered_js: true
word_count: 102
summary: This document describes a deprecated Spotify Web API endpoint used to determine if the current user follows specific artists or other Spotify users.
tags:
    - spotify-api
    - web-api
    - user-following
    - artists
    - social-features
    - deprecated-endpoint
category: api
---

Web API •References / Users / Check If User Follows Artists or Users

## Check If User Follows Artists or Users

Deprecated

Check to see if the current user is following one or more artists or other Spotify users.

**Note:** This endpoint is deprecated. Use [Check User's Saved Items](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) instead.

## Request

- The ID type: either `artist` or `user`.
  
  Allowed values: `"artist"`, `"user"`Example: `type=artist`
- A comma-separated list of the artist or the user [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) to check. For example: `ids=74ASZWbe4lXaubB36ztrGX,08td7MxkoHQkXnWAYD8d6Q`. A maximum of 50 IDs can be sent in one request.
  
  Example: `ids=2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6`

## Response

Array of booleans

An array of:

Example: `[false,true]`

```
curl --request GET \
  --url 'https://api.spotify.com/v1/me/following/contains?type=artist&ids=2CIMQHirSU0MQqyYHq0eOx%2C57dN52uHvrHOxijzpIgu3E%2C1vCWHaC5f2uS3yhpwWbIA6' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
[false, true]
```