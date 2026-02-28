---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/reorder-or-replace-playlists-items
source: crawler
fetched_at: 2026-02-27T23:46:53.346166-03:00
rendered_js: false
word_count: 302
summary: This document explains how to reorder or replace items within a Spotify playlist using specific Web API parameters and request structures.
tags:
    - spotify-api
    - playlists
    - web-api
    - playlist-management
    - reorder-items
    - replace-items
category: api
---

Web API •References / Playlists / Update Playlist Items

## Update Playlist Items

Either reorder or replace items in a playlist depending on the request's parameters. To reorder items, include `range_start`, `insert_before`, `range_length` and `snapshot_id` in the request's body. To replace items, include `uris` as either a query parameter or in the request's body. Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist.

**Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters. These operations can't be applied together in a single request.

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`
- A comma-separated list of [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) to set, can be track or episode URIs. For example: `uris=spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M,spotify:episode:512ojhOuo1ktJprKbVcKyQ`  
  A maximum of 100 items can be set in one request.

supports free form additional properties

- The position of the first item to be reordered.
- The position where the items should be inserted.  
  To reorder the items to the end of the playlist, simply set *insert\_before* to the position after the last item.  
  Examples:  
  To reorder the first item to the last position in a playlist with 10 items, set *range\_start* to 0, and *insert\_before* to 10.  
  To reorder the last item in a playlist with 10 items to the start of the playlist, set *range\_start* to 9, and *insert\_before* to 0.
- The amount of items to be reordered. Defaults to 1 if not set.  
  The range of items to be reordered begins from the *range\_start* position, and includes the *range\_length* subsequent items.  
  Example:  
  To move the items at index 9-10 to the start of the playlist, *range\_start* is set to 9, and *range\_length* is set to 2.
- The playlist's snapshot ID against which you want to make the changes.

## Response

A snapshot ID for the playlist

## Response sample

```
{"snapshot_id": "abc"}
```