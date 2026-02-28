---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/unshareBusinessDatasetWithAdAccount
source: crawler
fetched_at: 2026-02-27T23:39:43.353016-03:00
rendered_js: true
word_count: 68
summary: This document provides technical specifications for the API endpoint used to remove the association between a measurement dataset and a specific ad account.
tags:
    - ads-api
    - measurement-datasets
    - ad-account-management
    - data-sharing
    - endpoint-reference
category: api
---

Ads API •References / measurement-datasets / Unshare A Dataset With An Ad Account

## Unshare A Dataset With An Ad Account

Unshare a dataset with an ad account within a business.

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for the dataset.
  
  Example: `0d86b9e9-70f0-4700-a725-3417ba8786f6`

## Response

No content. The dataset was unshared successfully.

```
curl --request DELETE \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/datasets/0d86b9e9-70f0-4700-a725-3417ba8786f6/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```