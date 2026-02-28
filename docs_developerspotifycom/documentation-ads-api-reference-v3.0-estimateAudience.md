---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateAudience
source: crawler
fetched_at: 2026-02-27T23:39:47.482775-03:00
rendered_js: true
word_count: 0
summary: This document provides a request example for the Spotify Ads API to retrieve audience size estimates based on specific campaign targeting, budget, and scheduling parameters. It demonstrates the structure of a POST request used to forecast potential reach across various segments and platforms.
tags:
    - spotify-ads-api
    - audience-estimation
    - ad-targeting
    - marketing-api
    - campaign-forecasting
    - request-payload
category: api
---

```
curl --request POST \
  --url https://api-partner.spotify.com/ads/v3/estimates/audience \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "ad_account_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a",
    "start_date": "2024-01-23T04:56:07Z",
    "end_date": "2024-01-30T04:56:07Z",
    "bid_strategy": "MAX_BID",
    "bid_micro_amount": 10000000,
    "asset_format": "AUDIO",
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
        "podcast_episode_topic_ids": [
            "automotive",
            "books-and-literature"
        ],
        "sensitive_topic_exclusions": {
            "topics": [
                {
                    "id": "alcohol",
                    "filter_option": "RESTRICTED"
                },
                {
                    "id": "hate-speech",
                    "filter_option": "RESTRICTED"
                }
            ]
        },
        "playlist_ids": [
            "holidays",
            "cooking"
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
        "genders": [
            "MALE",
            "FEMALE",
            "NON_BINARY"
        ],
        "language": "en",
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
        "genre_ids": [
            "rock",
            "blues"
        ]
    },
    "objective": "EVEN_IMPRESSION_DELIVERY",
    "budget": {
        "micro_amount": 5000000,
        "type": "DAILY",
        "currency": "USD"
    }
}'
```