---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getPixelById
source: crawler
fetched_at: 2026-02-27T23:39:33.409437-03:00
rendered_js: true
word_count: 225
summary: This document specifies the Ads API endpoint for retrieving detailed information about a specific tracking pixel associated with a unique business identifier.
tags:
    - ads-api
    - pixel-measurement
    - tracking-pixel
    - rest-api
    - marketing-tools
    - data-tracking
category: api
---

Ads API •References / pixel-measurement / Get pixel by id for a given business.

## Get pixel by id for a given business.

Get pixel by id for a given business.

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for a pixel.
  
  Example: `cd2f1480ba3d4f9b9c5a39893c0def91`

## Response

Pixel

- A unique identifier for a pixel.
  
  Supported content-type(s): Example: `"cd2f1480ba3d4f9b9c5a39893c0def91"`
- integration\_idstring \[uuid]
  
  A unique identifier for the integration.
  
  Supported content-type(s): Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- The URL you would like to track. Only HTTP and HTTPS schemes are allowed.
  
  Example: `"https://www.spotify.com"`
- created\_atstring \[date-time]
  
  Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Supported content-type(s): Example: `"2026-01-23T04:56:07Z"`
- - A unique identifier for an event.
    
    Supported content-type(s): Example: `"23815327f0c64cf9811516c53c465f37"`
  - Allowed values: `"PAGE_VIEW"`, `"LEAD"`, `"PURCHASE"`, `"ADD_TO_CART"`Example: `"LEAD"`
  - created\_atstring \[date-time]
    
    Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Supported content-type(s): Example: `"2026-01-23T04:56:07Z"`
  - last\_activity\_atstring \[date-time]
    
    Date the event was last used. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Example: `"2021-01-23T04:56:07Z"`
- - Allowed values: `"PAGE_VIEW"`, `"LEAD"`, `"PURCHASE"`, `"ADD_TO_CART"`Example: `"LEAD"`
  - hour\_partitionstring \[date-time]
    
    The hour the event counts pertain to, in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Example: `"2023-08-02T10:00:00Z"`
  - Count of historical events, aggregated for the hour.
    
    Example: `42`
- A unique identifier for the dataset.
  
  Example: `"0d86b9e9-70f0-4700-a725-3417ba8786f6"`
- Whether AAM is enabled for this pixel. If false, no fields will be used for matching, even if they are present in the AamFields column.
  
  Example: `false`
- aam\_fieldsarray of strings
  
  List of AAM fields to enable for matching.
  
  Array length between `0` and `11`Example: `["EMAIL","PHONE","FIRST_NAME"]`
  
  User info field for advanced matching.
  
  Allowed values: `"EMAIL"`, `"PHONE"`, `"FIRST_NAME"`, `"LAST_NAME"`, `"DATE_OF_BIRTH"`, `"GENDER"`, `"CITY"`, `"STATE"`, `"ZIP"`, `"COUNTRY"`, `"EXTERNAL_ID"`

```
curl --request GET \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/pixels/cd2f1480ba3d4f9b9c5a39893c0def91 \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"id": "cd2f1480ba3d4f9b9c5a39893c0def91","integration_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","domain": "https://www.spotify.com","name": "Spotify","created_at": "2026-01-23T04:56:07Z","events": [{"id": "23815327f0c64cf9811516c53c465f37","type": "LEAD","created_at": "2026-01-23T04:56:07Z","last_activity_at": "2021-01-23T04:56:07Z"}],"historical_events": [{"type": "LEAD","hour_partition": "2023-08-02T10:00:00Z","count": 42}],"dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6","aam_opt_in": false,"aam_fields": ["EMAIL", "PHONE", "FIRST_NAME"]}
```