---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateBusiness
source: crawler
fetched_at: 2026-02-27T23:40:01.465609-03:00
rendered_js: true
word_count: 142
summary: This document outlines the endpoint and data requirements for updating the name of an existing business entity within the Ads API.
tags:
    - ads-api
    - business-management
    - update-business
    - api-reference
    - endpoint-details
category: api
---

Ads API •References / businesses / Update Business

## Update Business

Update the given existing business.

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

<!--THE END-->

- The name of the business.
  
  Pattern: `^(?!\s*$).+`Length between `1` and `255`Example: `"My Ad Studio Business"`

## Response

Metadata for a business.

- A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- The name of the business.
  
  Pattern: `^(?!\s*$).+`Length between `1` and `255`Example: `"My Ad Studio Business"`
- created\_atstring \[date-time]
  
  Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- updated\_atstring \[date-time]
  
  Date the entity was updated. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- The status of the business.
  
  Allowed values: `"ACTIVE"`
- The type of the business.
  
  Allowed values: `"ADVERTISER"`, `"AGENCY"`, `"MUSIC_ARTIST_CONCERT_PROMOTER"`, `"PODCAST_PROMOTER"`

```
curl --request PATCH \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "My Ad Studio Business"
}'
```

* * *

## Response sample

```
{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "My Ad Studio Business","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","status": "ACTIVE","type": "ADVERTISER"}
```