---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getSensitiveTopicTargets
source: crawler
fetched_at: 2026-02-27T23:40:46.765074-03:00
rendered_js: true
word_count: 60
summary: This document provides technical details for the Get Sensitive Topic Targets API endpoint, which allows users to retrieve information about sensitive ad targeting categories using IDs or search queries.
tags:
    - ads-api
    - targeting
    - sensitive-topics
    - endpoint-reference
    - rest-api
category: api
---

Ads API •References / targets / Get Sensitive Topic Targets

## Get Sensitive Topic Targets

Returns sensitive topics information. If no query parameter is provided, all sensitive topics will be returned.

## Request

- A list of unique identifiers for sensitive topics.
  
  Example: `ids=gambling`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`

## Response

A list of sensitive topics.

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/targets/sensitive_topics?q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"sensitive_topics": [{"id": "crime-and-violence","name": "Crime and Violence"},{"id": "alcohol","name": "Alcohol"}]}
```