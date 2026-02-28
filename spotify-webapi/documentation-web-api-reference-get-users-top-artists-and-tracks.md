---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
source: crawler
fetched_at: 2026-02-27T23:47:01.283692-03:00
rendered_js: false
word_count: 2
summary: This document provides a sample JSON response format for the Spotify API endpoint used to retrieve a user's saved shows. It illustrates the structure of paginated results and the metadata fields associated with show objects.
tags:
    - spotify-api
    - json-response
    - user-library
    - api-pagination
    - saved-shows
category: reference
---

## Response sample

```
{"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20","limit": 20,"next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","offset": 0,"previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","total": 4,"items": [{"external_urls": {"spotify": "string"},"followers": {"href": "string","total": 0},"genres": ["Prog rock", "Grunge"],"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","popularity": 0,"type": "artist","uri": "string"}]}
```