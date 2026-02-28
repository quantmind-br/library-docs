---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getLanguageTargets
source: crawler
fetched_at: 2026-02-27T23:40:42.62683-03:00
rendered_js: true
word_count: 76
summary: This document provides technical specifications for the Spotify Ads API endpoint used to retrieve and filter available language targeting options.
tags:
    - ads-api
    - language-targeting
    - api-reference
    - endpoint-documentation
    - spotify-advertising
category: api
---

Ads API •References / targets / Get Language Targets

## Get Language Targets

Returns language targets information. If no query parameter is provided, all language targets will be returned.

## Request

- A list of unique identifiers for languages.
  
  Example: `ids=en&ids=cz`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`
- ad\_account\_idstring \[uuid]
  
  Optional ad account ID for per-account feature flag resolution. When omitted, returns safe default behavior.
  
  Example: `ad_account_id=ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

## Response

A list of language targets.

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/targets/languages?q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"languages": [{"id": "en","name": "English"}]}
```