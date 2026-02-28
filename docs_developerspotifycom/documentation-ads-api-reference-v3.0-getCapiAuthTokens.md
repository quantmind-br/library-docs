---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCapiAuthTokens
source: crawler
fetched_at: 2026-02-27T23:39:43.949483-03:00
rendered_js: true
word_count: 64
summary: This document provides technical specifications for the GET endpoint used to retrieve active authentication tokens for a Conversions API (CAPI) integration.
tags:
    - ads-api
    - capi-measurement
    - authentication-tokens
    - conversions-api
    - rest-api
category: api
---

Ads API •References / capi-measurement / Get CAPI Auth Token(s)

## Get CAPI Auth Token(s)

Gets all active authentication token(s)

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- capi\_connection\_idstring \[uuid]
  
  A unique identifier for the CAPI integration.
  
  Example: `2fd920ed-a111-43d4-bee2-74d078c479a5`

## Response

List of active CAPI auth tokens.

- - capi\_auth\_token\_idstring \[uuid]
    
    A unique identifier for an Authentication Token.
    
    Example: `"bb7a8ba9-f77a-11ee-ae13-42010a8e0056"`
  - A JSON web token to be included in CAPI event calls.
    
    Example: `"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl9pZCI6IjMxNTRjMzEzLTliNmYtNDYzNS1hNjE2LTAzNTJhODI0ODBkOCJ9.QBADF2P0S-WCEB7wluhvMxRRHcIazAyiitzeFPqZ_xY"`
  - created\_atstring \[date-time]
    
    Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Example: `"2026-01-23T04:56:07Z"`

```
curl --request GET \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/capi/2fd920ed-a111-43d4-bee2-74d078c479a5/tokens \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"data": [{"capi_auth_token_id": "bb7a8ba9-f77a-11ee-ae13-42010a8e0056","capi_auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl9pZCI6IjMxNTRjMzEzLTliNmYtNDYzNS1hNjE2LTAzNTJhODI0ODBkOCJ9.QBADF2P0S-WCEB7wluhvMxRRHcIazAyiitzeFPqZ_xY","created_at": "2026-01-23T04:56:07Z"}]}
```