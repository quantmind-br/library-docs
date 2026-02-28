---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/upload-custom-playlist-cover
source: crawler
fetched_at: 2026-02-27T23:39:01.663524-03:00
rendered_js: true
word_count: 44
summary: This document provides technical details for using the Web API endpoint to replace a specific playlist's cover image with base64 encoded JPEG data.
tags:
    - spotify-api
    - playlist-management
    - image-upload
    - rest-api
    - base64-encoding
    - put-request
category: api
---

Web API •References / Playlists / Add Custom Playlist Cover Image

## Add Custom Playlist Cover Image

Replace the image used to represent a specific playlist.

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`

Base64 encoded JPEG image data, maximum payload size is 256 KB.

Example: `"/9j/2wCEABoZGSccJz4lJT5CLy8vQkc9Ozs9R0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0cBHCcnMyYzPSYmPUc9Mj1HR0dEREdHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR//dAAQAAf/uAA5BZG9iZQBkwAAAAAH/wAARCAABAAEDACIAAREBAhEB/8QASwABAQAAAAAAAAAAAAAAAAAAAAYBAQAAAAAAAAAAAAAAAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAARAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwAAARECEQA/AJgAH//Z"`

## Response

```
curl --request PUT \
  --url https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/images \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: image/jpeg' \
  --data /9j/2wCEABoZGSccJz4lJT5CLy8vQkc9Ozs9R0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0cBHCcnMyYzPSYmPUc9Mj1HR0dEREdHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR//dAAQAAf/uAA5BZG9iZQBkwAAAAAH/wAARCAABAAEDACIAAREBAhEB/8QASwABAQAAAAAAAAAAAAAAAAAAAAYBAQAAAAAAAAAAAAAAAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAARAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwAAARECEQA/AJgAH//Z
```

* * *

## Response sample

```
empty response
```