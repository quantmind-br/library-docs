---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCampaigns
source: crawler
fetched_at: 2026-02-27T23:39:48.807938-03:00
rendered_js: true
word_count: 299
summary: Technical documentation for the Ads API endpoint used to retrieve, filter, and sort advertising campaigns associated with a specific ad account ID.
tags:
    - ads-api
    - campaign-management
    - api-request
    - filtering
    - pagination
    - ad-account-id
category: api
---

Ads API •References / campaigns / Get Campaigns by Ad Account ID

## Get Campaigns by Ad Account ID

Returns list of campaigns linked to an ad account.

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- campaign\_idsarray of strings
  
  A list of campaigns to return.
  
  A unique identifier for the entity.
  
  Example: `campaign_ids=ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- The string that will be used to filter campaigns by name. The filter is case-insensitive and will match any campaign that contains the given string in its name.
- ad\_set\_statusesarray of strings
  
  The set of enums that will be used to filter campaigns by their ad set statuses. The filter will match any campaign that has at least one ad set with the given status.
  
  Allowed values: `"ACTIVE"`, `"ACTIVE_RESTRICTED"`, `"APPROVED"`, `"ARCHIVED"`, `"COMPLETED"`, `"PENDING_APPROVAL"`, `"READY"`, `"REJECTED"`Example: `ad_set_statuses=ACTIVE`
- Filter by campaign's status
  
  Current state of campaign.
  
  Allowed values: `"UNSET"`, `"ACTIVE"`, `"PAUSED"`, `"ARCHIVED"`, `"AGENT_CONTROLLED"`, `"ACTIVE_RESTRICTED"`, `"PENDING_ADVERTISER_REVIEW"`, `"UNRECOGNIZED"`Example: `statuses=ACTIVE`
- Subset of campaign fields to be returned.
  
  Array minimum length: `1`Example: `fields=NAME&fields=CREATED_AT&fields=STATUS`
  
  Allowed values: `"ID"`, `"NAME"`, `"CREATED_AT"`, `"UPDATED_AT"`, `"STATUS"`, `"PURCHASE_ORDER"`, `"OBJECTIVE"`, `"MEASUREMENT_METADATA"`, `"DELIVERY"`
- Field by which to sort campaigns.
  
  Default: `sort_field=CREATED_AT`Allowed values: `"ID"`, `"NAME"`, `"CREATED_AT"`, `"UPDATED_AT"`, `"STATUS"`Example: `sort_field=CREATED_AT`
- Field by which to order the results of the query.
  
  Default: `sort_direction=DESC`Allowed values: `"ASC"`, `"DESC"`Example: `sort_direction=ASC`
- Limit or page size for a given response.
  
  Default: `limit=50`Range: `1` - `50`Example: `limit=50`
- Starting position of the next record to assist in data pagination.
  
  Default: `offset=0`Example: `offset=0`

## Response

A list of campaigns.

- - total\_resultsinteger \[int32]
  - current\_pageinteger \[int32]
- - A unique identifier for the entity.
    
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
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/campaigns \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"paging": {"page_size": 0,"total_results": 0,"offset": 0,"current_page": 0},"campaigns": [{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "Spotify Ads Summer Campaign 2022","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","purchase_order": "ORDER_1","status": "ACTIVE","objective": "EVEN_IMPRESSION_DELIVERY","delivery_goal_group": "UNSET"}]}
```