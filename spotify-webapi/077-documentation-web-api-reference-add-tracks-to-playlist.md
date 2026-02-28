---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist
source: crawler
fetched_at: 2026-02-27T23:46:51.635613-03:00
rendered_js: false
word_count: 271
summary: This document specifies the request parameters and response format for the deprecated endpoint used to add tracks or episodes to a playlist. It details how to position items within a playlist and provides constraints on the number of items allowed per request.
tags:
    - spotify-api
    - playlist-management
    - deprecated-endpoint
    - web-api
    - track-insertion
    - api-reference
category: api
---

Web API •References / Playlists / Add Items to Playlist \[DEPRECATED]

## Add Items to Playlist \[DEPRECATED]

Deprecated

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`
- The position to insert the items, a zero-based index. For example, to insert the items in the first position: `position=0`; to insert the items in the third position: `position=2`. If omitted, the items will be appended to the playlist. Items are added in the order they are listed in the query string or request body.
  
  Example: `position=0`
- A comma-separated list of [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) to add, can be track or episode URIs. For example:  
  `uris=spotify:track:4iV5W9uYEdYUVa79Axb7Rh, spotify:track:1301WleyT98MSxVHPZCA6M, spotify:episode:512ojhOuo1ktJprKbVcKyQ`  
  A maximum of 100 items can be added in one request.  
  ***Note**: it is likely that passing a large number of item URIs as a query parameter will exceed the maximum length of the request URI. When adding a large number of items, it is recommended to pass them in the request body, see below.*
  
  Example: `uris=spotify%3Atrack%3A4iV5W9uYEdYUVa79Axb7Rh,spotify%3Atrack%3A1301WleyT98MSxVHPZCA6M`

supports free form additional properties

- A JSON array of the [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) to add. For example: `{"uris": ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98MSxVHPZCA6M", "spotify:episode:512ojhOuo1ktJprKbVcKyQ"]}`  
  A maximum of 100 items can be added in one request. ***Note**: if the `uris` parameter is present in the query string, any URIs listed here in the body will be ignored.*
- The position to insert the items, a zero-based index. For example, to insert the items in the first position: `position=0` ; to insert the items in the third position: `position=2`. If omitted, the items will be appended to the playlist. Items are added in the order they appear in the uris array. For example: `{"uris": ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98MSxVHPZCA6M"], "position": 3}`

## Response

A snapshot ID for the playlist

## Response sample

```

```