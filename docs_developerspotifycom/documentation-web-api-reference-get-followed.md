---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-followed
source: crawler
fetched_at: 2026-02-27T23:39:15.813713-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response structure for an API request retrieving artist information, including pagination details and metadata.
tags:
    - api-response
    - json-schema
    - artist-metadata
    - pagination
    - data-structure
category: reference
---

## Response sample

```
{"artists": {"href": "string","limit": 0,"next": "string","cursors": {"after": "string","before": "string"},"total": 0,"items": [{"external_urls": {"spotify": "string"},"followers": {"href": "string","total": 0},"genres": ["Prog rock", "Grunge"],"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","popularity": 0,"type": "artist","uri": "string"}]}}
```