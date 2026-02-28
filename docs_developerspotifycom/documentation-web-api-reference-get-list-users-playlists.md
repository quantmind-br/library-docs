---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-list-users-playlists
source: crawler
fetched_at: 2026-02-27T23:38:56.837396-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response structure for a Spotify API endpoint, demonstrating how paginated show data is returned.
tags:
    - spotify-api
    - json-response
    - pagination
    - api-reference
    - user-content
category: reference
---

## Response sample

```
{"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20","limit": 20,"next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","offset": 0,"previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","total": 4,"items": [{"collaborative": false,"description": "string","external_urls": {"spotify": "string"},"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","owner": {"external_urls": {"spotify": "string"},"href": "string","id": "string","type": "user","uri": "string","display_name": "string"},"public": false,"snapshot_id": "string","items": {"href": "string","total": 0},"tracks": {"href": "string","total": 0},"type": "string","uri": "string"}]}
```