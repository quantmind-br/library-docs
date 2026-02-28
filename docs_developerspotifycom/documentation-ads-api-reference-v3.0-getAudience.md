---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAudience
source: crawler
fetched_at: 2026-02-27T23:39:54.191556-03:00
rendered_js: true
word_count: 276
summary: This document provides the technical specification for the Get an Audience API endpoint, detailing how to retrieve information about a specific advertising audience using its unique identifier.
tags:
    - ads-api
    - audience-management
    - api-endpoint
    - data-retrieval
    - spotify-ads
    - audience-targeting
category: api
---

Ads API •References / audiences / Get an Audience

## Get an Audience

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

## Response

An audience.

- created\_atstring \[date-time]
  
  Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- updated\_atstring \[date-time]
  
  Date the entity was updated. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- Length between `2` and `80`Example: `"US - 18-24 - All gender"`
- Description of the audience.
  
  Maximum length: `80`Example: `"For spring promotion campaign"`
- Default: `"CUSTOM"`Allowed values: `"CUSTOM"`, `"LOOKALIKE"`
- An approximate range of users in the audience.
  
  - Minimum of an approximate range of users in the audience.
    
    Minimum value: `0`
  - Maximum of an approximate range of users in the audience.
    
    Minimum value: `0`
- Default: `"PROCESSING"`Allowed values: `"ARCHIVED"`, `"PROCESSING"`, `"EMPTY"`, `"LEARNING"`, `"BOOKABLE"`, `"LIVE"`
- Sources of the audience data.
  
  Source of the audience data.
  
  Default: `"UNKNOWN"`Allowed values: `"UNKNOWN"`, `"CUSTOMER_LIST"`, `"AUDIENCE"`, `"PIXEL"`, `"CONVERSIONS_API"`
- seed\_audience\_idstring \[uuid]
  
  ID of the seed audience for the lookalike audience.
  
  Supported content-type(s): Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- Length between `2` and `80`Example: `"US - 18-24 - All gender"`
- lookalike\_audience\_idsarray of strings
  
  IDs of the lookalike audiences created from the current audience.
  
  A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- Datasets associated with the web event custom audience.
  
  - A unique identifier for the entity.
    
    Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- included\_eventsarray of strings
  
  Event names included in the web event custom audience.
- excluded\_eventsarray of strings
  
  Event names excluded from the web event custom audience.
- Lookback window for events in the web event custom audience.
  
  Example: `30`

```
curl --request GET \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/audiences/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "US - 18-24 - All gender","description": "For spring promotion campaign","type": "CUSTOM","size": {"min": 0,"max": 0},"status": "PROCESSING","sources": ["UNKNOWN"],"seed_audience_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","seed_audience_name": "US - 18-24 - All gender","lookalike_audience_ids": ["ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"],"datasets": [{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "string"}],"included_events": ["ADDTOCART"],"excluded_events": ["PURCHASE"],"lookback_days": 30}
```