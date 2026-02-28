---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getInterestTargets
source: crawler
fetched_at: 2026-02-27T23:40:11.719602-03:00
rendered_js: true
word_count: 57
summary: This document provides technical details for the API endpoint used to retrieve and search for interest-based targeting options within the Spotify Ads platform.
tags:
    - spotify-ads-api
    - targeting
    - interest-targets
    - api-endpoint
    - ad-targeting
category: api
---

Ads API •References / targets / Get Interest Targets

## Get Interest Targets

Returns interest targets information. If no query parameter is provided, all interest targets will be returned.

## Request

- A list of unique identifiers for interests.
  
  Example: `ids=ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`

## Response

A list of interest targets.

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/targets/interests?q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"interests_with_subtargets": [{"id": "661a6418-1fa0-4640-a86b-8fb1ef5249f8","name": "Academic Interests","subtargets": [{"id": "32147515-b339-4b35-80c7-309ce4bb9024","name": "Clinical Science"},{"id": "5bd1a4c8-11db-4245-85f7-b3571aec0a9e","name": "History"},{"id": "b7167be4-4a1f-421d-96b8-6211d723e3ad","name": "Medicine and Healthcare"}]},{"id": "5012bb54-9ff3-404e-b892-afffa7e08cdf","name": "Business and Finance","subtargets": [{"id": "1f926bd0-bc40-49db-8a70-d8fcc068be58","name": "Marketing and advertising"},{"id": "91e181b4-a0ad-4ab5-bd66-64457da7d1db","name": "Sales"}]}]}
```