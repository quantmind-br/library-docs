---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-users-saved-audiobooks
source: crawler
fetched_at: 2026-02-27T23:46:13.553285-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response for a Spotify API endpoint that returns a paginated list of audiobooks or shows associated with a user.
tags:
    - spotify-api
    - json-response
    - pagination
    - audiobooks
    - web-api
category: reference
---

## Response sample

```
{"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20","limit": 20,"next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","offset": 0,"previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","total": 4,"items": [{"authors": [{"name": "string"}],"available_markets": ["string"],"copyrights": [{"text": "string","type": "string"}],"description": "string","html_description": "string","edition": "Unabridged","explicit": false,"external_urls": {"spotify": "string"},"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"languages": ["string"],"media_type": "string","name": "string","narrators": [{"name": "string"}],"publisher": "string","type": "audiobook","uri": "string","total_chapters": 0}]}
```