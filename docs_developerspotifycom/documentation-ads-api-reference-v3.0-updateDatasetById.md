---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateDatasetById
source: crawler
fetched_at: 2026-02-27T23:39:42.262237-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response representing the structure of an advertising dataset, including pixel configurations, event tracking data, and conversion API integration details.
tags:
    - advertising-api
    - json-response
    - pixel-tracking
    - capi-integration
    - event-history
    - ad-account-metadata
category: api
---

## Response sample

```
{"id": "0d86b9e9-70f0-4700-a725-3417ba8786f6","name": "US Advertising","pixel": {"id": "cd2f1480ba3d4f9b9c5a39893c0def91","integration_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","domain": "https://www.spotify.com","name": "Spotify","created_at": "2026-01-23T04:56:07Z","events": [{"id": "23815327f0c64cf9811516c53c465f37","type": "LEAD","created_at": "2026-01-23T04:56:07Z","last_activity_at": "2021-01-23T04:56:07Z"}],"historical_events": [{"type": "LEAD","hour_partition": "2023-08-02T10:00:00Z","count": 42}],"dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6","aam_opt_in": false,"aam_fields": ["EMAIL", "PHONE", "FIRST_NAME"]},"capi_integration": {"capi_connection_id": "2fd920ed-a111-43d4-bee2-74d078c479a5","integration_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "Retail Sales","dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6"},"ad_set_count": 0,"is_archived": false,"is_receiving_events": false,"shared_ad_accounts": [{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "Spotify"}],"is_receiving_lead_events": false}
```