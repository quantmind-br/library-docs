---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/updatePixelById
source: crawler
fetched_at: 2026-02-27T23:39:31.967642-03:00
rendered_js: true
word_count: 139
summary: This document outlines the API specification for updating an existing tracking pixel, including required request parameters and the structure of the successful response.
tags:
    - ads-api
    - pixel-measurement
    - update-pixel
    - tracking-pixel
    - patch-request
category: api
---

Ads API •References / pixel-measurement / Update pixel

## Update pixel

Update an existing pixel.

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for a pixel.
  
  Example: `cd2f1480ba3d4f9b9c5a39893c0def91`

<!--THE END-->

- The URL you would like to track. Only HTTP and HTTPS schemes are allowed.
  
  Example: `"https://www.spotify.com"`

## Response

The pixel was updated successfully.

- A unique identifier for a pixel.
  
  Supported content-type(s): Example: `"cd2f1480ba3d4f9b9c5a39893c0def91"`
- The URL you would like to track. Only HTTP and HTTPS schemes are allowed.
  
  Example: `"https://www.spotify.com"`
- created\_atstring \[date-time]
  
  Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Supported content-type(s): Example: `"2026-01-23T04:56:07Z"`
- updated\_atstring \[date-time]
  
  Date the entity was updated. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Supported content-type(s): Example: `"2026-01-23T04:56:07Z"`

```
curl --request PATCH \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/pixels/cd2f1480ba3d4f9b9c5a39893c0def91 \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "domain": "https://www.spotify.com",
    "name": "Spotify"
}'
```

* * *

## Response sample

```
{"id": "cd2f1480ba3d4f9b9c5a39893c0def91","domain": "https://www.spotify.com","name": "Spotify","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z"}
```