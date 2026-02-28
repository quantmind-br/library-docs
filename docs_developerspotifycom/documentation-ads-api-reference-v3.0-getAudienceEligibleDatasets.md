---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAudienceEligibleDatasets
source: crawler
fetched_at: 2026-02-27T23:40:39.141965-03:00
rendered_js: true
word_count: 96
summary: This document details the API endpoint for retrieving a list of datasets eligible for creating custom audiences within a specific ad account. It includes request parameters, response object fields, and a code example for implementation.
tags:
    - ads-api
    - custom-audiences
    - datasets
    - audience-targeting
    - spotify-advertising
    - api-reference
category: api
---

Ads API •References / audiences / List Datasets eligible for creating Custom Audiences

## List Datasets eligible for creating Custom Audiences

A list of datasets eligible for creating custom audiences

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`
- Limit or page size for a given response.
  
  Default: `limit=50`Range: `1` - `50`Example: `limit=50`

## Response

A list of audiences.

- - total\_resultsinteger \[int32]
  - current\_pageinteger \[int32]
- - A unique identifier for the entity.
    
    Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
  - Example: `"Spring Promotion Dataset"`
  - Event names with activity for the dataset.
    
    Example: `"add_to_cart"`

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/audiences/datasets?q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"paging": {"page_size": 0,"total_results": 0,"offset": 0,"current_page": 0},"datasets": [{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "Spring Promotion Dataset","events": ["add_to_cart"]}]}
```