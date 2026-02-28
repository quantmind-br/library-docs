---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getEpisodeTopicTargets
source: crawler
fetched_at: 2026-02-27T23:40:46.133736-03:00
rendered_js: true
word_count: 65
summary: This document provides technical details for the Ads API endpoint used to retrieve and search for podcast episode topic targets.
tags:
    - spotify-ads-api
    - podcast-targeting
    - episode-topics
    - api-endpoint
    - targeting-options
category: api
---

Ads API •References / targets / Get Podcast Episode Topic Targets

## Get Podcast Episode Topic Targets

Returns Podcast episode topic information. If no query parameter is provided, all episode topics will be returned.

## Request

- A list of unique identifiers for podcast episode topics.
  
  Example: `ids=healthy-living`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`

## Response

A list of podcast episode topics.

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/targets/episode_topics?q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"episode_topics": [{"id": "healthy-living","name": "Healthy Living"}]}
```