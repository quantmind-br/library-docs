---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres
source: crawler
fetched_at: 2026-02-27T23:46:42.612678-03:00
rendered_js: true
word_count: 37
summary: This document describes the Spotify Web API endpoint used to retrieve a list of available genre seed parameter values for use in recommendation queries.
tags:
    - spotify-api
    - genre-seeds
    - recommendations
    - web-api
    - endpoint-reference
category: api
---

Web API •References / Genres / Get Available Genre Seeds

## Get Available Genre Seeds

Deprecated

Retrieve a list of available genres seed parameter values for [recommendations](https://developer.spotify.com/documentation/web-api/reference/get-recommendations).

## Request

GET/recommendations/available-genre-seeds

## Response

A set of genres

- Example: `["alternative","samba"]`

```
curl --request GET \
  --url https://api.spotify.com/v1/recommendations/available-genre-seeds \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"genres": ["alternative", "samba"]}
```