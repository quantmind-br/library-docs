---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAd
source: crawler
fetched_at: 2026-02-27T23:40:00.424533-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response for an advertisement entity, detailing fields such as call-to-action settings, scheduling, and creative asset identifiers. It serves as a technical reference for the data structure returned by an advertising management API.
tags:
    - advertising-api
    - json-response
    - ad-management
    - spotify-ad-studio
    - api-reference
    - marketing-platform
category: reference
---

## Response sample

```
{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","call_to_action": {"key": "LEARN_MORE","text": "Learn more","language": "string","clickthrough_url": "https://www.spotify.com"},"created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","start_time": "2023-09-23T04:56:07Z","end_time": "2023-09-23T04:56:07Z","delivery": "ON","ad_set_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","status": "PENDING","reject_reason": "Your ad wasn’t approved. Create a new ad, or contact us at adstudio@spotify.com.","reject_reasons": [{"rejection": "Clickthrough URL doesn't work","rejection_key": "AD_POLICY_VIOLATION_REJECTION","remediation": "Submit a new ad with an updated clickthrough URL.","remediation_key": "AD_POLICY_VIOLATION_REMEDIATION"}],"ad_preview_url": "https://www.adstudio.spotify.com/campaigns/ads/8ae1f562-1b4e-11ee-be56-0242ac120002/preview","advertiser_name": "Heart Dance Recordings","assets": {"asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","companion_asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","logo_asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","canvas_asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"},"name": "New Ad","tagline": "Good Food for Good Dogs","third_party_tracking": [{"measurement_partner": "IAS","url": "https://www.example.com/your-landing-page/?utm_campaign=test-campaign&utm_source=email"}]}
```