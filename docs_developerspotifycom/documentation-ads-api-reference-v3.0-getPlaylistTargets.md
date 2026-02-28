---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getPlaylistTargets
source: crawler
fetched_at: 2026-02-27T23:40:44.95668-03:00
rendered_js: true
word_count: 50
summary: This document provides technical details for the Get Playlist Targets endpoint of the Ads API, explaining how to retrieve playlist data using query parameters or specific identifiers.
tags:
    - ads-api
    - playlist-targets
    - api-reference
    - targeting
    - spotify-platform
category: api
---

Ads API •References / targets / Get Playlist Targets

## Get Playlist Targets

Returns playlist information. If no query parameter is provided, all playlists will be returned.

## Request

- A list of unique identifiers for playlists.
  
  Example: `ids=cooking&ids=gaming`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`

## Response

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/targets/playlists?q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"playlists": [{"id": "holidays","name": "Holidays"}]}
```