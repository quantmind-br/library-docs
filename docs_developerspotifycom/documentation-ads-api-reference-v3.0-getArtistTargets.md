---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getArtistTargets
source: crawler
fetched_at: 2026-02-27T23:40:45.561972-03:00
rendered_js: true
word_count: 44
summary: This document outlines the Spotify Ads API endpoint for retrieving artist information used for targeting based on specific IDs or search queries.
tags:
    - spotify-ads-api
    - artist-targeting
    - api-endpoint
    - target-retrieval
    - ad-campaigns
category: api
---

Ads API •References / targets / Get Artist Targets

## Get Artist Targets

Returns artist information based on given query parameter.

## Request

- A list of unique identifiers for artists.
  
  Example: `ids=1XpDYCrUJnvCo9Ez6yeMWh`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`

## Response

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/targets/artists?q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"artists": [{"id": "target-id","name": "target-name","images": [{"width": 6,"url": "https://i.scdn.co/image/ab6765630000ba8a2e0748b75ab4b3bb0638dd74","height": 2}]}]}
```