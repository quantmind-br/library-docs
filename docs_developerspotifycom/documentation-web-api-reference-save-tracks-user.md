---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/save-tracks-user
source: crawler
fetched_at: 2026-02-27T23:39:07.599448-03:00
rendered_js: true
word_count: 180
summary: This document provides technical details for a deprecated Spotify Web API endpoint used to save tracks to a user's 'Your Music' library, including request parameters for track IDs and timestamps.
tags:
    - spotify-api
    - tracks-endpoint
    - library-management
    - deprecated-api
    - web-api-reference
category: api
---

Web API •References / Tracks / Save Tracks for Current User

## Save Tracks for Current User

Deprecated

Save one or more tracks to the current user's 'Your Music' library.

**Note:** This endpoint is deprecated. Use [Save Items to Library](https://developer.spotify.com/documentation/web-api/reference/save-library-items) instead.

## Request

supports free form additional properties

- A JSON array of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `["4iV5W9uYEdYUVa79Axb7Rh", "1301WleyT98MSxVHPZCA6M"]`  
  A maximum of 50 items can be specified in one request. ***Note**: if the `timestamped_ids` is present in the body, any IDs listed in the query parameters (deprecated) or the `ids` field in the body will be ignored.*
- A JSON array of objects containing track IDs with their corresponding timestamps. Each object must include a track ID and an `added_at` timestamp. This allows you to specify when tracks were added to maintain a specific chronological order in the user's library.  
  A maximum of 50 items can be specified in one request. ***Note**: if the `timestamped_ids` is present in the body, any IDs listed in the query parameters (deprecated) or the `ids` field in the body will be ignored.*
  
  - added\_atstring \[date-time]
    
    The timestamp when the track was added to the library. Use ISO 8601 format with UTC timezone (e.g., `2023-01-15T14:30:00Z`). You can specify past timestamps to insert tracks at specific positions in the library's chronological order. The API uses minute-level granularity for ordering, though the timestamp supports millisecond precision.

## Response

```
curl --request PUT \
  --url https://api.spotify.com/v1/me/tracks \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "ids": [
        "string"
    ],
    "timestamped_ids": [
        {
            "id": "string",
            "added_at": "string"
        }
    ]
}'
```

* * *

## Response sample

```
empty response
```