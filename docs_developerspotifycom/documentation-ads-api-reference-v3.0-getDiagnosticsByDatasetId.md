---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getDiagnosticsByDatasetId
source: crawler
fetched_at: 2026-02-27T23:39:41.64406-03:00
rendered_js: true
word_count: 117
summary: This document provides technical specifications for an Ads API endpoint used to retrieve diagnostic information for a specific measurement dataset. It details the required request parameters, filter options for granularities and datasources, and the structure of the resulting diagnostic data.
tags:
    - ads-api
    - measurement-datasets
    - diagnostics
    - api-reference
    - data-tracking
    - dataset-monitoring
category: api
---

Ads API •References / measurement-datasets / Get diagnostics for a dataset.

## Get diagnostics for a dataset.

Get diagnostics for a dataset.

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for the dataset.
  
  Example: `0d86b9e9-70f0-4700-a725-3417ba8786f6`
- granularitiesarray of strings
  
  A list of diagnostic granularities to retrieve for a dataset.
  
  What granularity of diagnostic data is present.
  
  Allowed values: `"DAILY"`, `"HOURLY"`
- datasource\_idsarray of strings
  
  A list of datasources you want to filter by.
  
  A unique identifier for a datasource
  
  Example: `datasource_ids=ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

## Response

Diagnostics response.

- A unique identifier for the dataset.
  
  Example: `"0d86b9e9-70f0-4700-a725-3417ba8786f6"`
- - Type of datasource that diagnostic data is using.
    
    Allowed values: `"PIXEL"`, `"CAPI"`
  - A unique identifier for a datasource
    
    Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
  - What granularity of diagnostic data is present.
    
    Allowed values: `"DAILY"`, `"HOURLY"`

```
curl --request GET \
  --url 'https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/datasets/0d86b9e9-70f0-4700-a725-3417ba8786f6/diagnostics?granularities=DAILY' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6","datasources": [{"datasource_type": "PIXEL","datasource_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","granularity": "DAILY","timeseries": [{"total": 0,"timestamp": 0,"event_counts": [{"name": "string","event_count": 0,"last_activity_ms": 0}]}]}]}
```