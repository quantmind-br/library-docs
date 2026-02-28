---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-recommendations
source: crawler
fetched_at: 2026-02-27T23:39:14.479115-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response structure for an API endpoint that returns music track recommendations and metadata, including detailed objects for albums, artists, and seeds.
tags:
    - api-response
    - music-metadata
    - spotify-api
    - json-schema
    - track-details
category: reference
---

## Response sample

```
{"seeds": [{"afterFilteringSize": 0,"afterRelinkingSize": 0,"href": "string","id": "string","initialPoolSize": 0,"type": "string"}],"tracks": [{"album": {"album_type": "compilation","total_tracks": 9,"available_markets": ["CA", "BR", "IT"],"external_urls": {"spotify": "string"},"href": "string","id": "2up3OPMp9Tb4dAKM2erWXQ","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","release_date": "1981-12","release_date_precision": "year","restrictions": {"reason": "market"},"type": "album","uri": "spotify:album:2up3OPMp9Tb4dAKM2erWXQ","artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}]},"artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}],"available_markets": ["string"],"disc_number": 0,"duration_ms": 0,"explicit": false,"external_ids": {"isrc": "string","ean": "string","upc": "string"},"external_urls": {"spotify": "string"},"href": "string","id": "string","is_playable": false,"linked_from": {},"restrictions": {"reason": "string"},"name": "string","popularity": 0,"preview_url": "string","track_number": 0,"type": "track","uri": "string","is_local": false}]}
```