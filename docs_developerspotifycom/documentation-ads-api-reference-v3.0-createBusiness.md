---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/createBusiness
source: crawler
fetched_at: 2026-02-27T23:39:56.882079-03:00
rendered_js: true
word_count: 190
summary: This document provides the technical specification for the Create Business API endpoint, detailing the required request parameters and the resulting business object response.
tags:
    - ads-api
    - business-creation
    - endpoint-reference
    - post-request
    - account-management
category: api
---

Ads API •References / businesses / Create Business

## Create Business

## Request

- The name of the business.
  
  Pattern: `^(?!\s*$).+`Length between `1` and `255`Example: `"My Ad Studio Business"`
- business\_admin\_namestring
  
  The display name of a user in or invited to a business. It will be defined for active users, and null for pending users.
  
  Example: `"John Doe"`
- business\_admin\_emailstring
  
  The email address of a user in or invited to a business.
  
  Maximum length: `319`Example: `"discovery@gmail.com"`
- The type of the business.
  
  Allowed values: `"ADVERTISER"`, `"AGENCY"`, `"MUSIC_ARTIST_CONCERT_PROMOTER"`, `"PODCAST_PROMOTER"`
- business\_admin\_has\_marketing\_opt\_inboolean
  
  Indicates if user has opted into marketing.

## Response

A business object.

- A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- The name of the business.
  
  Pattern: `^(?!\s*$).+`Length between `1` and `255`Example: `"My Ad Studio Business"`
- created\_atstring \[date-time]
  
  Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- updated\_atstring \[date-time]
  
  Date the entity was updated. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- The status of the business.
  
  Allowed values: `"ACTIVE"`
- The type of the business.
  
  Allowed values: `"ADVERTISER"`, `"AGENCY"`, `"MUSIC_ARTIST_CONCERT_PROMOTER"`, `"PODCAST_PROMOTER"`

```
curl --request POST \
  --url https://api-partner.spotify.com/ads/v3/businesses \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "My Ad Studio Business",
    "business_admin_name": "John Doe",
    "business_admin_email": "discovery@gmail.com",
    "type": "ADVERTISER",
    "business_admin_has_marketing_opt_in": false
}'
```

* * *

## Response sample

```
{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "My Ad Studio Business","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","status": "ACTIVE","type": "ADVERTISER"}
```