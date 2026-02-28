---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getMobileAppsByBusinessId
source: crawler
fetched_at: 2026-02-27T23:39:32.232203-03:00
rendered_js: true
word_count: 2
summary: This document provides an example JSON response structure for retrieving mobile application data, including platform details, tracking identifiers, and integration settings.
tags:
    - api-response
    - mobile-apps
    - json-sample
    - advertising-data
    - app-tracking
    - metadata
category: reference
---

## Response sample

```
{"paging": {"page_size": 0,"total_results": 0,"offset": 0,"current_page": 0},"mobile_apps": [{"name": "My Android App","platform_app_id": "com.example.myapp","platform": "ANDROID","ad_type": "VIEW_THROUGH","id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","ios_app_id": "ABCD123489","android_app_url": "com.example.myapp","apple_app_url": "https://apps.apple.com/us/app/my-example-app/id1234567890","google_play_url": "https://play.google.com/store/apps/details?id=com.example.myapp&hl=en_US","link_token": "ABCD123489","mobile_measurement_partner": "KOCHAVA","dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6","integration_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","ad_set_count": 0,"is_skad_network": true,"shared_ad_accounts": [{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "Spotify"}]}]}
```