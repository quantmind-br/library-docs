---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/deleteAudience
source: crawler
fetched_at: 2026-02-27T23:39:52.218821-03:00
rendered_js: true
word_count: 44
summary: This document provides technical specifications for deleting a specific audience associated with an ad account via the Spotify Ads API.
tags:
    - ads-api
    - audience-management
    - delete-request
    - api-reference
    - spotify-advertising
category: api
---

Ads API •References / audiences / Delete an Audience

## Delete an Audience

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

## Response

The audience was deleted successfully.

- Number of audiences deleted.

```
curl --request DELETE \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/audiences/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"deletion_count": 0}
```