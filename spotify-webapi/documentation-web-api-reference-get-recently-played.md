---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-recently-played
source: crawler
fetched_at: 2026-02-27T23:46:49.311889-03:00
rendered_js: false
word_count: 2
summary: This document provides a detailed sample JSON response for an API endpoint that returns a list of recently played music tracks, including metadata for albums, artists, and pagination cursors.
tags:
    - api-response
    - json-schema
    - music-metadata
    - spotify-api
    - pagination-cursors
    - track-details
category: reference
---

## Response sample

```
{"href": "string","limit": 0,"next": "string","cursors": {"after": "string","before": "string"},"total": 0,"items": [{"track": {"album": {"album_type": "compilation","total_tracks": 9,"available_markets": ["CA", "BR", "IT"],"external_urls": {"spotify": "string"},"href": "string","id": "2up3OPMp9Tb4dAKM2erWXQ","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","release_date": "1981-12","release_date_precision": "year","restrictions": {"reason": "market"},"type": "album","uri": "spotify:album:2up3OPMp9Tb4dAKM2erWXQ","artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}]},"artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}],"available_markets": ["string"],"disc_number": 0,"duration_ms": 0,"explicit": false,"external_ids": {"isrc": "string","ean": "string","upc": "string"},"external_urls": {"spotify": "string"},"href": "string","id": "string","is_playable": false,"linked_from": {},"restrictions": {"reason": "string"},"name": "string","popularity": 0,"preview_url": "string","track_number": 0,"type": "track","uri": "string","is_local": false},"played_at": "string","context": {"type": "string","href": "string","external_urls": {"spotify": "string"},"uri": "string"}}]}
```