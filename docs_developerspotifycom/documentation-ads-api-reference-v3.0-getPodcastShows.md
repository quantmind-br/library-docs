---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getPodcastShows
source: crawler
fetched_at: 2026-02-27T23:40:40.310971-03:00
rendered_js: true
word_count: 66
summary: This document provides technical details for the Get Podcast Shows endpoint, which allows users to retrieve podcast information using IDs, keywords, or market-specific filters.
tags:
    - ads-api
    - podcast-shows
    - get-request
    - api-reference
    - search-query
    - market-filter
category: api
---

Ads API •References / podcast-shows / Get Podcast Shows

## Get Podcast Shows

Returns podcast information based on given query parameter.

## Request

- A list of unique identifiers for podcast shows.
  
  Example: `ids=3zaHNdVeLiqOSXwxdoWcij`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`
- An ISO 3166-1 alpha-2 country code. Only content that is available in that market will be returned.
  
  Minimum length: `2`Example: `market=US`

## Response

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/podcast_shows?q=query&market=US' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"shows": [{"id": "target-id","name": "target-name","images": [{"width": 6,"url": "https://i.scdn.co/image/ab6765630000ba8a2e0748b75ab4b3bb0638dd74","height": 2}]}]}
```