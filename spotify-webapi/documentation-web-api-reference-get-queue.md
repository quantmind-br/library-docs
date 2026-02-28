---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-queue
source: crawler
fetched_at: 2026-02-27T23:45:28.08756-03:00
rendered_js: true
word_count: 2
summary: Provides a sample JSON response structure for retrieving the currently playing track and the user's playback queue from a music streaming API.
tags:
    - spotify-api
    - playback-queue
    - json-response
    - currently-playing
    - media-metadata
category: api
---

## Response sample

```
{"currently_playing": {"album": {"album_type": "compilation","total_tracks": 9,"available_markets": ["CA", "BR", "IT"],"external_urls": {"spotify": "string"},"href": "string","id": "2up3OPMp9Tb4dAKM2erWXQ","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","release_date": "1981-12","release_date_precision": "year","restrictions": {"reason": "market"},"type": "album","uri": "spotify:album:2up3OPMp9Tb4dAKM2erWXQ","artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}]},"artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}],"available_markets": ["string"],"disc_number": 0,"duration_ms": 0,"explicit": false,"external_ids": {"isrc": "string","ean": "string","upc": "string"},"external_urls": {"spotify": "string"},"href": "string","id": "string","is_playable": false,"linked_from": {},"restrictions": {"reason": "string"},"name": "string","popularity": 0,"preview_url": "string","track_number": 0,"type": "track","uri": "string","is_local": false},"queue": [{"album": {"album_type": "compilation","total_tracks": 9,"available_markets": ["CA", "BR", "IT"],"external_urls": {"spotify": "string"},"href": "string","id": "2up3OPMp9Tb4dAKM2erWXQ","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","release_date": "1981-12","release_date_precision": "year","restrictions": {"reason": "market"},"type": "album","uri": "spotify:album:2up3OPMp9Tb4dAKM2erWXQ","artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}]},"artists": [{"external_urls": {"spotify": "string"},"href": "string","id": "string","name": "string","type": "artist","uri": "string"}],"available_markets": ["string"],"disc_number": 0,"duration_ms": 0,"explicit": false,"external_ids": {"isrc": "string","ean": "string","upc": "string"},"external_urls": {"spotify": "string"},"href": "string","id": "string","is_playable": false,"linked_from": {},"restrictions": {"reason": "string"},"name": "string","popularity": 0,"preview_url": "string","track_number": 0,"type": "track","uri": "string","is_local": false}]}
```