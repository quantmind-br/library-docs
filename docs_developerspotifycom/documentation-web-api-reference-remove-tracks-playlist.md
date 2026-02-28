---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/remove-tracks-playlist
source: crawler
fetched_at: 2026-02-27T23:38:55.626459-03:00
rendered_js: true
word_count: 106
summary: This document describes the deprecated Spotify Web API endpoint for removing specific tracks or episodes from a playlist using URIs and snapshot IDs.
tags:
    - spotify-api
    - web-api
    - playlist-management
    - deprecated
    - endpoint-reference
category: api
---

Web API •References / Playlists / Remove Playlist Items \[DEPRECATED]

## Remove Playlist Items \[DEPRECATED]

Deprecated

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`

<!--THE END-->

- An array of objects containing [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) of the tracks or episodes to remove. For example: `{ "tracks": [{ "uri": "spotify:track:4iV5W9uYEdYUVa79Axb7Rh" },{ "uri": "spotify:track:1301WleyT98MSxVHPZCA6M" }] }`. A maximum of 100 objects can be sent at once.
- The playlist's snapshot ID against which you want to make the changes. The API will validate that the specified items exist and in the specified positions and make the changes, even if more recent changes have been made to the playlist.

## Response

A snapshot ID for the playlist

```
curl --request DELETE \
  --url https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/tracks \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "tracks": [
        {
            "uri": "string"
        }
    ],
    "snapshot_id": "string"
}'
```

* * *

## Response sample

```
{"snapshot_id": "abc"}
```