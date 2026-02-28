---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-users-saved-shows
source: crawler
fetched_at: 2026-02-27T23:39:05.175917-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response structure for the Spotify Web API endpoint that retrieves a user's saved shows.
tags:
    - spotify-api
    - web-api
    - json-response
    - user-library
    - podcast-metadata
    - pagination
category: reference
---

## Response sample

```
{"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20","limit": 20,"next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","offset": 0,"previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","total": 4,"items": [{"added_at": "string","show": {"available_markets": ["string"],"copyrights": [{"text": "string","type": "string"}],"description": "string","html_description": "string","explicit": false,"external_urls": {"spotify": "string"},"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"is_externally_hosted": false,"languages": ["string"],"media_type": "string","name": "string","publisher": "string","type": "show","uri": "string","total_episodes": 0}}]}
```