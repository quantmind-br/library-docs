---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/unfollow-artists-users
source: crawler
fetched_at: 2026-02-27T23:39:19.339559-03:00
rendered_js: true
word_count: 140
summary: This document describes a deprecated Spotify Web API endpoint used to remove the current user as a follower of specific artists or other Spotify users.
tags:
    - spotify-web-api
    - user-endpoints
    - artist-following
    - deprecated
    - delete-method
category: reference
---

Web API •References / Users / Unfollow Artists or Users

## Unfollow Artists or Users

Deprecated

Remove the current user as a follower of one or more artists or other Spotify users.

**Note:** This endpoint is deprecated. Use [Remove Items from Library](https://developer.spotify.com/documentation/web-api/reference/remove-library-items) instead.

## Request

- The ID type: either `artist` or `user`.
  
  Allowed values: `"artist"`, `"user"`Example: `type=artist`
- A comma-separated list of the artist or the user [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `ids=74ASZWbe4lXaubB36ztrGX,08td7MxkoHQkXnWAYD8d6Q`. A maximum of 50 IDs can be sent in one request.
  
  Example: `ids=2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6`

supports free form additional properties

- A JSON array of the artist or user [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `{ids:["74ASZWbe4lXaubB36ztrGX", "08td7MxkoHQkXnWAYD8d6Q"]}`. A maximum of 50 IDs can be sent in one request. ***Note**: if the `ids` parameter is present in the query string, any IDs listed here in the body will be ignored.*

## Response

Artist or user unfollowed

```
curl --request DELETE \
  --url 'https://api.spotify.com/v1/me/following?type=artist&ids=2CIMQHirSU0MQqyYHq0eOx%2C57dN52uHvrHOxijzpIgu3E%2C1vCWHaC5f2uS3yhpwWbIA6' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "ids": [
        "string"
    ]
}'
```

* * *

## Response sample

```
empty response
```