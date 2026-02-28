---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateAdSet
source: crawler
fetched_at: 2026-02-27T23:40:37.994138-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample API response illustrating the schema and data structure for an advertisement set, including targeting, budgeting, and scheduling parameters.
tags:
    - advertising-api
    - ad-set
    - json-response
    - targeting-criteria
    - api-schema
    - campaign-management
category: reference
---

## Response sample

```
{"name": "Test Ad set","start_time": "2023-09-23T04:56:07Z","end_time": "2023-09-26T04:56:07Z","frequency_caps": [{"frequency_unit": "DAY","frequency_period": 1,"max_impressions": 2}],"bid_micro_amount": 10000000,"delivery": "ON","id": "d936ecbb-3a93-4cfa-b756-c61811c6cdc3","category": "ADV_1_1","campaign_id": "5bbc4fec-c9a5-4fc6-98f4-e950f40b74c7","cost_model": "CPM","created_at": "2023-07-28T17:55:12Z","updated_at": "2023-09-28T17:55:12Z","asset_format": "AUDIO","budget": {"micro_amount": 500000000,"type": "DAILY","currency": "USD"},"promotion": {"promotion_goal": "ARTIST_PROMO","promotion_target_id": "1dfeR4HaWDbWqFHLkxsg1d","conversion_events": [{"tracking_event_type": "IMPRESSION","window_duration_ms": 86400000}]},"bid_strategy": "MAX_BID","status": "PENDING_APPROVAL","targets": {"age_ranges": [{"min": 18,"max": 65}],"artist_ids": ["1dfeR4HaWDbWqFHLkxsg1d"],"geo_targets": {"country_code": "US","city_ids": [],"dma_ids": ["503", "500"],"postal_code_ids": ["US:73170"],"region_ids": ["5101760"]},"genders": ["MALE", "FEMALE"],"genre_ids": ["blues", "alternative"],"interest_ids": ["365a5223-0024-4579-a881-3b08e8720021", "46b303e4-09a4-4c8e-998b-37186ff8120a"],"platforms": ["IOS"],"podcast_episode_topic_ids": ["books-and-literature", "automotive"],"sensitive_topic_exclusions": {"filter_option": "RESTRICTED"},"language": "en","playlist_ids": ["cooking", "holidays"],"placements": ["PODCAST", "MUSIC"]},"pacing": "PACING_EVEN"}
```