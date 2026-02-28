---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/unshareBusinessMobileAppWithAdAccount
source: crawler
fetched_at: 2026-02-27T23:39:38.594285-03:00
rendered_js: true
word_count: 75
summary: This document outlines the API endpoint and parameters required to remove the association between a mobile app and an ad account within a business.
tags:
    - ads-api
    - mobile-measurement
    - ad-account
    - mobile-app
    - endpoint-reference
    - delete-method
category: api
---

Ads API •References / mobile-measurement / Unshare A Mobile App With An Ad Account

## Unshare A Mobile App With An Ad Account

Unshare a mobile app with an ad account within a business.

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- mobile\_app\_idstring \[uuid]
  
  A unique identifier for a mobile app.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

## Response

No content. The mobile app was unshared successfully.

```
curl --request DELETE \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/mobile_apps/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```