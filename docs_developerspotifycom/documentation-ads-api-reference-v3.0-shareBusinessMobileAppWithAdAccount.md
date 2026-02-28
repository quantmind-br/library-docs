---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/shareBusinessMobileAppWithAdAccount
source: crawler
fetched_at: 2026-02-27T23:39:34.572951-03:00
rendered_js: true
word_count: 75
summary: This document specifies the technical details for an API endpoint used to associate a mobile application with a specific ad account within a business context.
tags:
    - ads-api
    - mobile-measurement
    - ad-account-management
    - mobile-apps
    - api-reference
category: api
---

Ads API •References / mobile-measurement / Share A Mobile App With An Ad Account

## Share A Mobile App With An Ad Account

Share a mobile app with an ad account within a business.

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

No content. The mobile app was shared successfully.

```
curl --request POST \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/mobile_apps/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```