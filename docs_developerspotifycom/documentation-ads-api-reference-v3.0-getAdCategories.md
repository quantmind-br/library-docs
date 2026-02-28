---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAdCategories
source: crawler
fetched_at: 2026-02-27T23:40:35.873447-03:00
rendered_js: true
word_count: 101
summary: This document describes the Get Ad Categories endpoint, which allows users to retrieve a list of all ad categories or search for specific categories using a keyword query.
tags:
    - ads-api
    - ad-categories
    - api-endpoint
    - category-search
    - rest-api
category: api
---

Ads API •References / ad-categories / Get Ad Categories

## Get Ad Categories

Returns ad category information based on given query parameter. If no query parameter is provided, all categories will be returned.

## Request

- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`

## Response

A list of ad categories.

- - The ID of a given ad category. IDs with a 0 value are parent categories.
    
    Example: `"ADV_1_8"`
  - The name of the parent category.
    
    Example: `"Automotive"`
  - A string concatenation of category and sub category names with a " - " delimiter. The name here will be only the category name for parent categories.
    
    Example: `"Automotive - Auto Towing and Repair"`

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/ad_categories?q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"categories": [{"id": "ADV_1_8","parent_category": "Automotive","name": "Automotive - Auto Towing and Repair"}]}
```