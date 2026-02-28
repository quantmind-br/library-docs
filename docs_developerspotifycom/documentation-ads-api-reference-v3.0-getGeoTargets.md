---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getGeoTargets
source: crawler
fetched_at: 2026-02-27T23:40:06.278592-03:00
rendered_js: true
word_count: 178
summary: This document describes the Ads API endpoint for retrieving geographic targeting information based on parameters like country code, location types, and keyword queries.
tags:
    - ads-api
    - geo-targeting
    - location-data
    - api-endpoint
    - search-filters
    - pagination
category: api
---

Ads API •References / targets / Get Geo Targets

## Get Geo Targets

Returns geo information filterable by query parameters. At least one query parameter must be provided.

## Request

- The country or region of a geo in ISO alpha-2 country code format.
  
  Default: `country_code=`Example: `country_code=US`
- A list of unique identifiers for geos.
  
  Example: `ids=5259444&ids=US%3A11214`
- Example: `types=CITY&types=COUNTRY&types=DMA_REGION&types=POSTAL_CODE&types=REGION`
- Query to search by keyword via case-insensitive wildcard matching.
  
  Example: `q=query`
- Limit or page size for a given response. The maximum limit is 50, except for when bulk uploading zip codes, where the maximum limit is 1000.
  
  Default: `limit=50`Range: `1` - `1000`Example: `limit=50`
- Starting position of the next record to assist in data pagination.
  
  Default: `offset=0`Example: `offset=0`
- A two-letter ISO 639-1 language code for querying geo targets. Defaults to "en" if missing.
  
  Pattern: `^[a-z]{2}$`Example: `language=en`

## Response

A list of geos.

- An object that represents the geo target entity.
  
  - The country or region of the geo in ISO alpha-2 country code format.
    
    Example: `"US"`
  - A unique identifier for a geo.
    
    Example: `"94110"`
  - The parent location to this geo if it exists (e.g. city, state, or country).
    
    Example: `"California"`

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/targets/geos?types=CITY&types=COUNTRY&types=DMA_REGION&types=POSTAL_CODE&types=REGION&q=query' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"offset": 0,"page_size": 0,"geos": [{"country_code": "US","id": "94110","type": "DMA_REGION","name": "San Francisco","parent_geo_name": "California"}]}
```