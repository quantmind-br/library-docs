---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-playlist-cover
source: crawler
fetched_at: 2026-02-27T23:46:53.929426-03:00
rendered_js: false
word_count: 58
summary: This document describes how to retrieve the cover image associated with a specific playlist through a Web API, outlining the required parameters and the structure of the image data response.
tags:
    - web-api
    - playlists
    - cover-art
    - api-reference
    - image-retrieval
category: reference
---

Web API •References / Playlists / Get Playlist Cover Image

## Get Playlist Cover Image

Get the current image associated with a specific playlist.

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`

## Response

A set of images

An array of:

- The source URL of the image.
  
  Example: `"https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228"`
- The image height in pixels.
  
  Example: `300`
- The image width in pixels.
  
  Example: `300`

## Response sample

```
[{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}]
```