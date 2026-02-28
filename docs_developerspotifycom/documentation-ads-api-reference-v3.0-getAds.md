---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAds
source: crawler
fetched_at: 2026-02-27T23:40:06.255024-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response format for an API call retrieving a paginated list of advertisement details, including scheduling, delivery status, and tracking information.
tags:
    - api-response
    - json-sample
    - advertising-api
    - pagination
    - ad-management
    - metadata
category: reference
---

## Response sample

```
{"paging": {"page_size": 50,"total_results": 116,"offset": 0},"ads": [{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","call_to_action": {"text": "LEARN_MORE","language": "ENGLISH","clickthrough_url": "https://www.spotify.com"},"created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","start_time": "2026-01-24T00:00:00Z","end_time": "2026-02-24T23:59:59Z","delivery": "ON","ad_set_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","status": "PENDING","reject_reason": "Your ad wasn’t approved. Create a new ad, or contact us at adstudio@spotify.com.","ad_preview_url": "https://www.adstudio.spotify.com/campaigns/ads/8ae1f562-1b4e-11ee-be56-0242ac120002/preview","advertiser_name": "Heart Dance Recordings","assets": {"asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","companion_asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","logo_asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"},"name": "Entity_1","tagline": "Good Food for Good Dogs","third_party_tracking": [{"measurement_partner": "IAS","url": "https://www.example.com/your-landing-page/?utm_campaign=test-campaign&utm_source=email"}],"ad_account_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"},{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","call_to_action": {"text": "LEARN_MORE","language": "ENGLISH","clickthrough_url": "https://www.spotify.com"},"created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","start_time": "2026-01-24T00:00:00Z","end_time": "2026-02-24T23:59:59Z","delivery": "ON","ad_set_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","status": "PENDING","reject_reason": "Your ad wasn’t approved. Create a new ad, or contact us at adstudio@spotify.com.","ad_preview_url": "https://www.adstudio.spotify.com/campaigns/ads/8ae1f562-1b4e-11ee-be56-0242ac120002/preview","advertiser_name": "Heart Dance Recordings","assets": {"asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","companion_asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","logo_asset_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"},"name": "Entity_1","tagline": "Good Food for Good Dogs","third_party_tracking": [{"measurement_partner": "IAS","url": "https://www.example.com/your-landing-page/?utm_campaign=test-campaign&utm_source=email"}],"ad_account_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"}]}
```