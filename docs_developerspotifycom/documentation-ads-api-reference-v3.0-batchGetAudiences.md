---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/batchGetAudiences
source: crawler
fetched_at: 2026-02-27T23:39:51.024442-03:00
rendered_js: true
word_count: 2
summary: This document provides a structural example of a JSON response for an audience-related API endpoint, detailing paging information and audience attributes.
tags:
    - api-response
    - audience-management
    - json-structure
    - paging
    - audience-targeting
category: reference
---

## Response sample

```
{"paging": {"page_size": 0,"total_results": 0,"offset": 0,"current_page": 0},"audiences": [{"created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "US - 18-24 - All gender","description": "For spring promotion campaign","type": "CUSTOM","size": {"min": 0,"max": 0},"status": "PROCESSING","sources": ["UNKNOWN"],"seed_audience_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","seed_audience_name": "US - 18-24 - All gender","lookalike_audience_ids": ["ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"],"datasets": [{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "string"}],"included_events": ["ADDTOCART"],"excluded_events": ["PURCHASE"],"lookback_days": 30}]}
```