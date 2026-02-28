---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-a-categories-playlists
source: crawler
fetched_at: 2026-02-27T23:39:02.093513-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response structure for an API endpoint that retrieves a paginated list of playlists.
tags:
    - spotify-api
    - api-response
    - json-example
    - playlist-metadata
    - web-api
category: reference
---

## Response sample

```
{"message": "Popular Playlists","playlists": {"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20","limit": 20,"next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","offset": 0,"previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","total": 4,"items": [{"collaborative": false,"description": "string","external_urls": {"spotify": "string"},"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","owner": {"external_urls": {"spotify": "string"},"href": "string","id": "string","type": "user","uri": "string","display_name": "string"},"public": false,"snapshot_id": "string","items": {"href": "string","total": 0},"tracks": {"href": "string","total": 0},"type": "string","uri": "string"}]}}
```