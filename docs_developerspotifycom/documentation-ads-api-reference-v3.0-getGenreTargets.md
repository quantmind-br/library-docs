---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getGenreTargets
source: crawler
fetched_at: 2026-02-27T23:40:43.793202-03:00
rendered_js: true
word_count: 50
summary: This document provides technical details for the Ads API endpoint used to retrieve genre targeting information via identifiers or search queries.
tags:
    - ads-api
    - genre-targeting
    - api-reference
    - targeting-criteria
    - http-get
category: api
---

Ads API •References / targets / Get Genre Targets

## Get Genre Targets

Returns genre information. If no query parameter is provided, all genres will be returned.

## Request

- A list of unique identifiers for genres.
  
  Example: `ids=rock&ids=jazz`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`

## Response

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/targets/genres?q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"genres": [{"id": "rock","name": "Rock"}]}
```