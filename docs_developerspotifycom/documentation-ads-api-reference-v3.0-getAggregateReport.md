---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAggregateReport
source: crawler
fetched_at: 2026-02-27T23:39:29.953098-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response for an advertising performance report, illustrating the structure of data rows, performance metrics, and pagination tokens.
tags:
    - advertising-api
    - reporting-metrics
    - json-response
    - ad-performance
    - api-reference
    - data-structure
category: reference
---

## Response sample

```
{"continuation_token": "AMC-fuxpGRIqFcOUEzDEdWQsM5Iy7mkRThKFo94mEys6RF1lzeKyq1sOlWU4RsdjSsgDWR2D7An1nFgLXNBU9hocKnWQ9jRsps6kCLqKd7Q77zNEhHm_Xlb6J_Fci6kK7tXVM3U6H8OajjcTA18eFcr-kv0etZJZBWlMhtP84xj4WiVDZnPWaMo7AL3jRrHH32grJ3eRA2PAoZmhg80=","report_start": "2021-01-23T04:56:07Z","report_end": "2021-01-26T04:56:07Z","granularity": "HOUR","rows": [{"entity_type": "AD_SET","entity_id": "9a7b6c5d-4e3f-4b21-8c99-bf1c2a3d4e5f","entity_name": "Ad Set 1","entity_status": "ACTIVE","start_time": "2025-08-01T00:00:00Z","end_time": "2025-08-02T00:00:00Z","stats": [{"field_type": "IMPRESSIONS","field_value": 1920},{"field_type": "STREAMED_IMPRESSIONS","field_value": 1920},{"field_type": "CLICKS","field_value": 9},{"field_type": "SPEND","field_value": 17.482913}]}],"warnings": [{"entity_type": "AD_SET","entity_id": "9a7b6c5d-4e3f-4b21-8c99-bf1c2a3d4e5f","entity_name": "Ad Set 1","entity_status": "ACTIVE","start_time": "2025-08-01T00:00:00Z","end_time": "2025-08-02T00:00:00Z","stats": [{"field_type": "IMPRESSIONS","field_value": 1920},{"field_type": "STREAMED_IMPRESSIONS","field_value": 1920},{"field_type": "CLICKS","field_value": 9},{"field_type": "SPEND","field_value": 17.482913}]},{"entity_type": "AD_SET","entity_id": "9a7b6c5d-4e3f-4b21-8c99-bf1c2a3d4e5f","entity_name": "Ad Set 1","entity_status": "ACTIVE","start_time": "2025-08-02T00:00:00Z","end_time": "2025-08-03T00:00:00Z","stats": [{"field_type": "IMPRESSIONS","field_value": 1811},{"field_type": "STREAMED_IMPRESSIONS","field_value": 1811},{"field_type": "CLICKS","field_value": 14},{"field_type": "SPEND","field_value": 16.994382}]},{"entity_type": "AD_SET","entity_id": "9a7b6c5d-4e3f-4b21-8c99-bf1c2a3d4e5f","entity_name": "Ad Set 1","entity_status": "ACTIVE","start_time": "2025-08-03T00:00:00Z","end_time": "2025-08-04T00:00:00Z","stats": [{"field_type": "IMPRESSIONS","field_value": 1888},{"field_type": "STREAMED_IMPRESSIONS","field_value": 1888},{"field_type": "CLICKS","field_value": 15},{"field_type": "SPEND","field_value": 17.112837}]},{"entity_type": "AD_SET","entity_id": "9a7b6c5d-4e3f-4b21-8c99-bf1c2a3d4e5f","entity_name": "Ad Set 1","entity_status": "ACTIVE","start_time": "2025-08-04T00:00:00Z","end_time": "2025-08-05T00:00:00Z","stats": [{"field_type": "IMPRESSIONS","field_value": 1855},{"field_type": "STREAMED_IMPRESSIONS","field_value": 1855},{"field_type": "CLICKS","field_value": 11},{"field_type": "SPEND","field_value": 16.785441}]}]}
```