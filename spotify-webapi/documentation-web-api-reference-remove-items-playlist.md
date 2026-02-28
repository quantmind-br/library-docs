---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/remove-items-playlist
source: crawler
fetched_at: 2026-02-27T23:46:53.035568-03:00
rendered_js: false
word_count: 112
summary: This document describes the Web API endpoint for removing one or more tracks or episodes from a user's playlist using Spotify URIs and snapshot IDs. It outlines the request structure, including the maximum number of items per request and the expected response format.
tags:
    - web-api
    - playlist-management
    - spotify-uri
    - endpoint-reference
    - snapshot-id
category: reference
---

Web API •References / Playlists / Remove Playlist Items

## Remove Playlist Items

Remove one or more items from a user's playlist.

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`

<!--THE END-->

- An array of objects containing [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) of the tracks or episodes to remove. For example: `{ "items": [{ "uri": "spotify:track:4iV5W9uYEdYUVa79Axb7Rh" },{ "uri": "spotify:track:1301WleyT98MSxVHPZCA6M" }] }`. A maximum of 100 objects can be sent at once.
- The playlist's snapshot ID against which you want to make the changes. The API will validate that the specified items exist and in the specified positions and make the changes, even if more recent changes have been made to the playlist.

## Response

A snapshot ID for the playlist

## Response sample

```
{"snapshot_id": "abc"}
```