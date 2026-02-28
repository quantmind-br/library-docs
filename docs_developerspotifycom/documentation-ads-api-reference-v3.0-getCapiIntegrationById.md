---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCapiIntegrationById
source: crawler
fetched_at: 2026-02-27T23:39:46.772708-03:00
rendered_js: true
word_count: 87
summary: This document provides the technical specification for retrieving a specific Conversions API (CAPI) integration by its unique ID. It outlines the required request parameters, the structure of the JSON response, and includes a sample curl command.
tags:
    - ads-api
    - capi
    - conversions-api
    - measurement
    - api-reference
    - integration-management
category: api
---

Ads API •References / capi-measurement / Get CAPI Integration

## Get CAPI Integration

Get a CAPI Integration by ID

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- capi\_connection\_idstring \[uuid]
  
  A unique identifier for the CAPI integration.
  
  Example: `2fd920ed-a111-43d4-bee2-74d078c479a5`

## Response

The requested CAPI integration.

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
curl --request GET \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/capi/2fd920ed-a111-43d4-bee2-74d078c479a5 \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"capi_connection_id": "2fd920ed-a111-43d4-bee2-74d078c479a5","integration_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "Retail Sales","dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6"}
```