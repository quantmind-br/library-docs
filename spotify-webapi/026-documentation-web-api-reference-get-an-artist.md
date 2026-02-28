---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-an-artist
source: crawler
fetched_at: 2026-02-27T23:45:21.081489-03:00
rendered_js: true
word_count: 159
summary: This document outlines the Spotify Web API endpoint for retrieving detailed catalog information for a single artist using their unique Spotify ID.
tags:
    - spotify-api
    - artist-endpoints
    - rest-api
    - music-metadata
    - json-response
category: api
---

Web API •References / Artists / Get Artist

## Get Artist

Get Spotify catalog information for a single artist identified by their unique Spotify ID.

## Request

- Example: `0TnOYISbd1XYRBk9myaseg`

## Response

An artist

- Known external URLs for this artist.
- Information about the followers of the artist.
  
  - This will always be set to null, as the Web API does not support it at the moment.
  - The total number of followers.
- A list of the genres the artist is associated with. If not yet classified, the array is empty.
  
  Example: `["Prog rock","Grunge"]`
- A link to the Web API endpoint providing full details of the artist.
- Images of the artist in various sizes, widest first.
  
  - The source URL of the image.
    
    Example: `"https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228"`
  - The image height in pixels.
    
    Example: `300`
  - The image width in pixels.
    
    Example: `300`
- The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.

## Response sample

```
{"external_urls": {"spotify": "string"},"followers": {"href": "string","total": 0},"genres": ["Prog rock", "Grunge"],"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"name": "string","popularity": 0,"type": "artist","uri": "string"}
```