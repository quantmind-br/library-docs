---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/createPixelInBusiness
source: crawler
fetched_at: 2026-02-27T23:39:29.865056-03:00
rendered_js: true
word_count: 291
summary: This document provides technical specifications for the Create Pixel endpoint, allowing developers to set up tracking pixels for monitoring domain activity and user conversions.
tags:
    - ads-api
    - pixel-tracking
    - conversion-measurement
    - advanced-matching
    - api-reference
    - marketing-attribution
category: api
---

Ads API •References / pixel-measurement / Create pixel

## Create pixel

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

<!--THE END-->

- The URL you would like to track. Only HTTP and HTTPS schemes are allowed.
  
  Example: `"https://www.spotify.com"`
- A unique identifier for the dataset.
  
  Example: `"0d86b9e9-70f0-4700-a725-3417ba8786f6"`
- Whether AAM is enabled for this pixel. If false, no fields will be used for matching, even if they are present in the AamFields column.
  
  Example: `false`
- aam\_fieldsarray of strings
  
  List of AAM fields to enable for matching.
  
  Array length between `0` and `11`Example: `["EMAIL","PHONE","FIRST_NAME"]`
  
  User info field for advanced matching.
  
  Allowed values: `"EMAIL"`, `"PHONE"`, `"FIRST_NAME"`, `"LAST_NAME"`, `"DATE_OF_BIRTH"`, `"GENDER"`, `"CITY"`, `"STATE"`, `"ZIP"`, `"COUNTRY"`, `"EXTERNAL_ID"`

## Response

The pixel was created successfully.

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
curl --request POST \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/pixels \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "domain": "https://www.spotify.com",
    "name": "Spotify",
    "dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6",
    "aam_opt_in": false,
    "aam_fields": [
        "EMAIL",
        "PHONE",
        "FIRST_NAME"
    ]
}'
```

* * *

## Response sample

```
{"id": "cd2f1480ba3d4f9b9c5a39893c0def91","integration_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","domain": "https://www.spotify.com","name": "Spotify","created_at": "2026-01-23T04:56:07Z","events": [{"id": "23815327f0c64cf9811516c53c465f37","type": "LEAD","created_at": "2026-01-23T04:56:07Z","last_activity_at": "2021-01-23T04:56:07Z"}],"historical_events": [{"type": "LEAD","hour_partition": "2023-08-02T10:00:00Z","count": 42}],"dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6","aam_opt_in": false,"aam_fields": ["EMAIL", "PHONE", "FIRST_NAME"]}
```