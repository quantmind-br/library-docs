---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks
source: crawler
fetched_at: 2026-02-27T23:45:46.98376-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response for a Spotify API request, illustrating the pagination structure and data fields for items like tracks or shows.
tags:
    - spotify-api
    - json-response
    - pagination
    - api-schema
    - web-api
category: reference
---

## Response sample

```
{"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20","limit": 20,"next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","offset": 0,"previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","total": 4,"items": [{"artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}],"available_markets": ["string"],"disc_number": 0,"duration_ms": 0,"explicit": false,"external_urls": {"spotify": "string"},"href": "string","id": "string","is_playable": false,"linked_from": {"external_urls": {"spotify": "string"},"href": "string","id": "string","type": "string","uri": "string"},"restrictions": {"reason": "string"},"name": "string","preview_url": "string","track_number": 0,"type": "string","uri": "string","is_local": false}]}
```