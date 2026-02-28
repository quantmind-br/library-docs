---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
source: crawler
fetched_at: 2026-02-27T23:39:18.01761-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response structure for the Spotify API, illustrating pagination fields and nested artist or show data objects.
tags:
    - spotify-api
    - json-response
    - api-pagination
    - data-schema
    - web-api
category: reference
---

## Response sample

```
{"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20","limit": 20,"next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","offset": 0,"previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","total": 4,"items": [{"external_urls": {"spotify": "string"},"followers": {"href": "string","total": 0},"genres": ["Prog rock", "Grunge"],"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","popularity": 0,"type": "artist","uri": "string"}]}
```