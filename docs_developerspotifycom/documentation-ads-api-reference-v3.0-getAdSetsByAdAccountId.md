---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAdSetsByAdAccountId
source: crawler
fetched_at: 2026-02-27T23:40:02.807372-03:00
rendered_js: true
word_count: 2
summary: This document provides a sample JSON response for an advertisement sets API, illustrating the data structure for campaign delivery, budgeting, and detailed audience targeting.
tags:
    - api-response
    - ad-sets
    - advertising-metadata
    - json-example
    - targeting-criteria
    - paging
category: reference
---

## Response sample

```
{"paging": {"page_size": 50,"total_results": 116,"offset": 0},"ad_sets": [{"name": "Test Ad set","start_time": "2023-08-23T04:56:07Z","end_time": "2023-08-26T04:56:07Z","frequency_caps": [{"frequency_unit": "DAY","frequency_period": 1,"max_impressions": 2}],"bid_micro_amount": 10000000,"delivery": "ON","id": "39ff503e-4baa-4e7a-9dd2-4b3f49653801","category": "ADV_1_1","campaign_id": "709076fe-2570-4dd9-94db-acc163e60fd8","cost_model": "CPM","created_at": "2023-07-26T05:54:47Z","updated_at": "2023-08-20T05:54:47Z","asset_format": "AUDIO","budget": {"micro_amount": 500000000,"type": "DAILY","currency": "USD"},"promotion": {"promotion_goal": "ARTIST_PROMO","promotion_target_id": "1dfeR4HaWDbWqFHLkxsg1d","conversion_events": [{"tracking_event_type": "IMPRESSION","window_duration_ms": 86400000}]},"bid_strategy": "MAX_BID","reject_reason": "","status": "PENDING_APPROVAL","targets": {"age_ranges": [{"min": 18,"max": 65}],"artist_ids": ["1dfeR4HaWDbWqFHLkxsg1d"],"geo_targets": {"country_code": "US","city_ids": [],"dma_ids": ["500", "503"],"postal_code_ids": ["US:73170"],"region_ids": ["5101760"]},"genders": ["MALE"],"genre_ids": ["alternative", "blues"],"interest_ids": ["46b303e4-09a4-4c8e-998b-37186ff8120a", "365a5223-0024-4579-a881-3b08e8720021"],"platforms": ["IOS"],"podcast_episode_topic_ids": ["automotive", "books-and-literature"],"sensitive_topic_exclusions": {"topics": [{"id": "tobacco","filter_option": "RESTRICTED"},{"id": "alcohol","filter_option": "PARTIAL"}]},"language": "en","playlist_ids": ["holidays", "cooking"],"placements": ["PODCAST", "MUSIC"]},"bid_optimization_goal": "CLICKS"},{"name": "Test Ad set","start_time": "2023-08-23T04:56:07Z","end_time": "2023-08-26T04:56:07Z","frequency_caps": [{"frequency_unit": "DAY","frequency_period": 1,"max_impressions": 2}],"bid_micro_amount": 10000000,"delivery": "ON","id": "86b54faf-3430-480b-80fd-4b1bad9cee7c","category": "ADV_1_1","campaign_id": "709076fe-2570-4dd9-94db-acc163e60fd8","cost_model": "CPM","created_at": "2023-07-25T23:11:27Z","updated_at": "2023-08-25T23:11:27Z","asset_format": "AUDIO","budget": {"micro_amount": 500000000,"type": "DAILY","currency": "USD"},"promotion": {"promotion_goal": "ARTIST_PROMO","promotion_target_id": "1dfeR4HaWDbWqFHLkxsg1d","conversion_events": [{"tracking_event_type": "IMPRESSION","window_duration_ms": 86400000}]},"bid_strategy": "MAX_BID","reject_reason": "","status": "PENDING_APPROVAL","targets": {"age_ranges": [{"min": 18,"max": 65}],"artist_ids": ["1dfeR4HaWDbWqFHLkxsg1d"],"geo_targets": {"country_code": "US","city_ids": [],"dma_ids": ["500", "503"],"postal_code_ids": ["US:73170"],"region_ids": ["5101760"]},"genders": ["MALE"],"genre_ids": ["alternative", "blues"],"interest_ids": ["46b303e4-09a4-4c8e-998b-37186ff8120a", "365a5223-0024-4579-a881-3b08e8720021"],"platforms": ["IOS"],"podcast_episode_topic_ids": ["automotive", "books-and-literature"],"sensitive_topic_exclusions": {"topics": [{"id": "tobacco","filter_option": "RESTRICTED"},{"id": "alcohol","filter_option": "PARTIAL"}]},"language": "en","playlist_ids": ["holidays", "cooking"],"placements": ["PODCAST", "MUSIC"]}}]}
```