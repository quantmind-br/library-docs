---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/deleteCapiAuthToken
source: crawler
fetched_at: 2026-02-27T23:39:45.109018-03:00
rendered_js: true
word_count: 58
summary: This document outlines the API endpoint and request parameters required to soft delete an authentication token for a Conversion API (CAPI) integration.
tags:
    - ads-api
    - capi
    - auth-token
    - conversion-api
    - endpoint-reference
    - measurement
category: api
---

Ads API •References / capi-measurement / Delete CAPI Auth Token

## Delete CAPI Auth Token

Soft delete the authentication token

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- capi\_connection\_idstring \[uuid]
  
  A unique identifier for the CAPI integration.
  
  Example: `2fd920ed-a111-43d4-bee2-74d078c479a5`
- capi\_auth\_token\_idstring \[uuid]
  
  A unique identifier for an Authentication Token.
  
  Example: `bb7a8ba9-f77a-11ee-ae13-42010a8e0056`

## Response

The token has been deleted.

```
curl --request DELETE \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/capi/2fd920ed-a111-43d4-bee2-74d078c479a5/tokens/bb7a8ba9-f77a-11ee-ae13-42010a8e0056 \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```