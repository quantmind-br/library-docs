---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-multiple-artists
source: crawler
fetched_at: 2026-02-27T23:38:27.498912-03:00
rendered_js: true
word_count: 134
summary: This document provides the technical specification for the Spotify Web API endpoint used to retrieve catalog information for multiple artists using their unique Spotify IDs.
tags:
    - spotify-api
    - artist-data
    - batch-retrieval
    - web-api
    - metadata-extraction
category: api
---

Web API •References / Artists / Get Several Artists

## Get Several Artists

Deprecated

Get Spotify catalog information for several artists based on their Spotify IDs.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the artists. Maximum: 50 IDs.
  
  Example: `ids=2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6`

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
  --url 'https://api.spotify.com/v1/artists?ids=2CIMQHirSU0MQqyYHq0eOx%2C57dN52uHvrHOxijzpIgu3E%2C1vCWHaC5f2uS3yhpwWbIA6' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"artists": [{"external_urls": {"spotify": "string"},"followers": {"href": "string","total": 0},"genres": ["Prog rock", "Grunge"],"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","popularity": 0,"type": "artist","uri": "string"}]}
```