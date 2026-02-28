---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-multiple-shows
source: crawler
fetched_at: 2026-02-27T23:46:54.949467-03:00
rendered_js: false
word_count: 2
summary: This document provides a sample JSON response format for a collection of show objects, detailing metadata fields such as descriptions, copyrights, and episode counts.
tags:
    - api-response
    - spotify-api
    - media-metadata
    - json-example
    - show-data
category: api
---

## Response sample

```
{"shows": [{"available_markets": ["string"],"copyrights": [{"text": "string","type": "string"}],"description": "string","html_description": "string","explicit": false,"external_urls": {"spotify": "string"},"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"is_externally_hosted": false,"languages": ["string"],"media_type": "string","name": "string","publisher": "string","type": "show","uri": "string","total_episodes": 0}]}
```