---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-multiple-albums
source: crawler
fetched_at: 2026-02-27T23:45:48.646822-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response structure illustrating the data format for music albums and their associated tracks in an API. It serves as a visual guide for the metadata fields returned when querying album information.
tags:
    - api-response
    - json-format
    - spotify-api
    - album-metadata
    - rest-endpoint
category: reference
---

## Response sample

```
{"albums": [{"album_type": "compilation","total_tracks": 9,"available_markets": ["CA", "BR", "IT"],"external_urls": {"spotify": "string"},"href": "string","id": "2up3OPMp9Tb4dAKM2erWXQ","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","release_date": "1981-12","release_date_precision": "year","restrictions": {"reason": "market"},"type": "album","uri": "spotify:album:2up3OPMp9Tb4dAKM2erWXQ","artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}],"tracks": {"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20","limit": 20,"next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","offset": 0,"previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","total": 4,"items": [{"artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}],"available_markets": ["string"],"disc_number": 0,"duration_ms": 0,"explicit": false,"external_urls": {"spotify": "string"},"href": "string","id": "string","is_playable": false,"linked_from": {"external_urls": {"spotify": "string"},"href": "string","id": "string","type": "string","uri": "string"},"restrictions": {"reason": "string"},"name": "string","preview_url": "string","track_number": 0,"type": "string","uri": "string","is_local": false}]},"copyrights": [{"text": "string","type": "string"}],"external_ids": {"isrc": "string","ean": "string","upc": "string"},"genres": [],"label": "string","popularity": 0}]}
```