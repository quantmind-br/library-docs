---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-an-artists-related-artists
source: crawler
fetched_at: 2026-02-27T23:46:05.799015-03:00
rendered_js: true
word_count: 133
summary: This document provides technical specifications for the Spotify Web API endpoint used to retrieve a list of artists similar to a specified artist based on listening patterns.
tags:
    - spotify-api
    - artist-metadata
    - related-artists
    - web-api
    - endpoint-reference
category: api
---

Web API •References / Artists / Get Artist's Related Artists

## Get Artist's Related Artists

Deprecated

Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of the Spotify community's listening history.

## Request

- Example: `0TnOYISbd1XYRBk9myaseg`

## Response

A set of artists

- - Known external URLs for this artist.
  - Information about the followers of the artist.
    
    - This will always be set to null, as the Web API does not support it at the moment.
    - The total number of followers.
  - A list of the genres the artist is associated with. If not yet classified, the array is empty.
    
    Example: `["Prog rock","Grunge"]`
  - A link to the Web API endpoint providing full details of the artist.
  - Images of the artist in various sizes, widest first.
  - The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.

```
curl --request GET \
  --url https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg/related-artists \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"artists": [{"external_urls": {"spotify": "string"},"followers": {"href": "string","total": 0},"genres": ["Prog rock", "Grunge"],"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","popularity": 0,"type": "artist","uri": "string"}]}
```