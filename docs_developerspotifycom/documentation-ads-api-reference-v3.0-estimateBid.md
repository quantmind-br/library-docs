---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateBid
source: crawler
fetched_at: 2026-02-27T23:40:01.618416-03:00
rendered_js: true
word_count: 0
summary: This document provides a sample API request for retrieving bid estimates for Spotify advertisements using specific campaign objectives and targeting criteria.
tags:
    - spotify-ads-api
    - bid-estimation
    - ad-targeting
    - api-endpoint
    - marketing-data
category: api
---

```
curl --request POST \
  --url https://api-partner.spotify.com/ads/v3/estimates/bid \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "start_date": "2024-01-23T04:56:07Z",
    "end_date": "2024-01-30T04:56:07Z",
    "asset_format": "AUDIO",
    "objective": "EVEN_IMPRESSION_DELIVERY",
    "bid_strategy": "MAX_BID",
    "currency": "USD",
    "frequency_caps": [
        {
            "frequency_unit": "DAY",
            "max_impressions": 2,
            "frequency_period": 1
        },
        {
            "frequency_unit": "WEEK",
            "max_impressions": 2,
            "frequency_period": 1
        },
        {
            "frequency_unit": "MONTH",
            "max_impressions": 2,
            "frequency_period": 1
        }
    ],
    "targets": {
        "age_ranges": [
            {
                "min": 23,
                "max": 27
            },
            {
                "min": 32,
                "max": 45
            }
        ],
        "artist_ids": [
            "06HL4z0CvFAxyc27GXpf02"
        ],
        "geo_targets": {
            "country_code": "US",
            "dma_ids": [
                "501"
            ],
            "region_ids": [
                "5279468"
            ],
            "city_ids": [
                "4174700"
            ],
            "postal_code_ids": [
                "US:73170"
            ]
        },
        "genders": [
            "MALE",
            "FEMALE",
            "NON_BINARY"
        ],
        "genre_ids": [
            "rock",
            "blues"
        ],
        "interest_ids": [
            "7ebe6459-5fea-4a50-887d-273c06080c78",
            "46b303e4-09a4-4c8e-998b-37186ff8120a"
        ],
        "platforms": [
            "IOS"
        ],
        "placements": [
            "MUSIC",
            "PODCAST"
        ],
        "podcast_episode_topic_ids": [
            "automotive",
            "books-and-literature"
        ],
        "sensitive_topic_exclusions": {
            "filter_option": "PARTIAL"
        },
        "language": "en",
        "playlist_ids": [
            "holidays",
            "cooking"
        ]
    }
}'
```