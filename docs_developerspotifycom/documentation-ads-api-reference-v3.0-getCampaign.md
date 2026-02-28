---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCampaign
source: crawler
fetched_at: 2026-02-27T23:40:02.601897-03:00
rendered_js: true
word_count: 232
summary: This document provides technical specifications for the Get Campaign by ID endpoint, allowing users to retrieve detailed metadata for a specific advertising campaign using its unique identifier.
tags:
    - ads-api
    - campaign-management
    - spotify-ads
    - api-reference
    - endpoint-documentation
    - campaign-metadata
category: api
---

Ads API •References / campaigns / Get Campaign by ID

## Get Campaign by ID

Returns campaign based on a given campaign ID.

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- Subset of campaign fields to be returned.
  
  Array minimum length: `1`Example: `fields=NAME&fields=CREATED_AT&fields=STATUS`
  
  Allowed values: `"ID"`, `"NAME"`, `"CREATED_AT"`, `"UPDATED_AT"`, `"STATUS"`, `"PURCHASE_ORDER"`, `"OBJECTIVE"`, `"MEASUREMENT_METADATA"`, `"DELIVERY"`

## Response

Metadata for a single campaign.

- A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- Name given to identify your campaign.
  
  Pattern: `^\S.*\S$`Length between `2` and `200`Example: `"Spotify Ads Summer Campaign 2022"`
- created\_atstring \[date-time]
  
  Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- updated\_atstring \[date-time]
  
  Date the entity was updated. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- A purchase order number, to be shown on your invoice, for your own personal organization.
  
  Length between `2` and `45`Example: `"ORDER_1"`
- Current state of campaign.
  
  Allowed values: `"UNSET"`, `"ACTIVE"`, `"PAUSED"`, `"ARCHIVED"`, `"AGENT_CONTROLLED"`, `"ACTIVE_RESTRICTED"`, `"PENDING_ADVERTISER_REVIEW"`, `"UNRECOGNIZED"`Example: `"ACTIVE"`
- Deprecated: Use delivery\_goal\_group and delivery\_goal on ad sets instead. Objective for a campaign. UNSET should not be used.
  
  Default: `"EVEN_IMPRESSION_DELIVERY"`Allowed values: `"UNSET"`, `"REACH"`, `"EVEN_IMPRESSION_DELIVERY"`, `"CLICKS"`, `"VIDEO_VIEWS"`, `"PODCAST_STREAMS"`, `"APP_INSTALLS"`, `"WEBSITE_VISITS"`Example: `"EVEN_IMPRESSION_DELIVERY"`
- delivery\_goal\_groupstring
  
  deliveryGoal group grouping selection for a campaign.
  
  Allowed values: `"UNSET"`, `"AWARENESS"`, `"WEBSITE_TRAFFIC"`, `"APP_PROMOTION"`, `"ENGAGEMENT_ON_SPOTIFY"`, `"LEAD_GEN"`

```
curl --request GET \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/campaigns/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "Spotify Ads Summer Campaign 2022","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","purchase_order": "ORDER_1","status": "ACTIVE","objective": "EVEN_IMPRESSION_DELIVERY","delivery_goal_group": "UNSET"}
```