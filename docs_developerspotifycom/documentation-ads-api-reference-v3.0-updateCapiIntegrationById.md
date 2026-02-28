---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateCapiIntegrationById
source: crawler
fetched_at: 2026-02-27T23:39:45.246233-03:00
rendered_js: true
word_count: 92
summary: This document provides the technical specification for updating an existing Conversions API (CAPI) integration, detailing the required parameters and the response structure.
tags:
    - ads-api
    - capi-measurement
    - patch-request
    - integration-update
    - conversions-api
category: api
---

Ads API •References / capi-measurement / Update CAPI Integration

## Update CAPI Integration

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- capi\_connection\_idstring \[uuid]
  
  A unique identifier for the CAPI integration.
  
  Example: `2fd920ed-a111-43d4-bee2-74d078c479a5`

<!--THE END-->

- The name of the CAPI integration.
  
  Example: `"Retail Sales"`

## Response

The updated CAPI integration.

- capi\_connection\_idstring \[uuid]
  
  A unique identifier for the CAPI integration.
  
  Supported content-type(s): Example: `"2fd920ed-a111-43d4-bee2-74d078c479a5"`
- integration\_idstring \[uuid]
  
  A unique identifier for the integration.
  
  Supported content-type(s): Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- The name of the CAPI integration.
  
  Example: `"Retail Sales"`
- A unique identifier for the dataset.
  
  Example: `"0d86b9e9-70f0-4700-a725-3417ba8786f6"`

```
curl --request PATCH \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/capi/2fd920ed-a111-43d4-bee2-74d078c479a5 \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "Retail Sales"
}'
```

* * *

## Response sample

```
{"capi_connection_id": "2fd920ed-a111-43d4-bee2-74d078c479a5","integration_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "Retail Sales","dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6"}
```