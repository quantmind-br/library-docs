---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAudienceInsightReport
source: crawler
fetched_at: 2026-02-27T23:40:07.441244-03:00
rendered_js: true
word_count: 110
summary: This document defines the available fields and enum values for generating reports, including specific validation rules and restrictions for insight reports.
tags:
    - reporting-api
    - metrics
    - enum-definitions
    - data-validation
    - insight-reports
category: reference
---

Example: `fields=IMPRESSIONS&fields=STREAMED_IMPRESSIONS&fields=CLICKS&fields=SPEND`

Users can define a set of fields that they would like populated in the report. This enum defines the global list of available fields. However, not all fields are applicable to both report types. This is validated at request time. The following fields are not allowed for insight reports:

- E\_CPCL
- FREQUENCY
- OFF\_SPOTIFY\_IMPRESSIONS
- PAID\_LISTENS\_FREQUENCY
- SKIPS
- SPEND
- STARTS
- UNMUTES

Allowed values: `"CLICKS"`, `"COMPLETES"`, `"COMPLETION_RATE"`, `"CONVERSION_RATE"`, `"CTR"`, `"E_CPCL"`, `"FIRST_QUARTILES"`, `"FREQUENCY"`, `"IMPRESSIONS"`, `"INTENT_RATE"`, `"LISTENERS"`, `"MIDPOINTS"`, `"NEW_LISTENERS"`, `"NEW_LISTENER_CONVERSION_RATE"`, `"NEW_LISTENER_STREAMS"`, `"OFF_SPOTIFY_IMPRESSIONS"`, `"PAID_LISTENS"`, `"PAID_LISTENS_FREQUENCY"`, `"PAID_LISTENS_REACH"`, `"REACH"`, `"SKIPS"`, `"SPEND"`, `"STARTS"`, `"STREAMS"`, `"STREAMS_PER_NEW_LISTENER"`, `"STREAMS_PER_USER"`, `"THIRD_QUARTILES"`, `"VIDEO_VIEWS"`, `"VIDEO_EXPANDS"`, `"VIDEO_EXPAND_RATE"`, `"UNMUTES"`, `"PAGE_VIEWS"`, `"LEADS"`, `"ADD_TO_CART"`, `"PURCHASES"`, `"REVENUE"`, `"AVERAGE_ORDER_VALUE"`, `"RETURN_ON_AD_SPEND"`, `"CUSTOMER_ACQUISITION_COST"`, `"COST_PER_LEAD"`, `"START_CHECKOUT"`, `"PRODUCTS"`, `"SIGN_UPS"`, `"CUSTOM_EVENT_1"`, `"CUSTOM_EVENT_2"`, `"CUSTOM_EVENT_3"`, `"CUSTOM_EVENT_4"`, `"CUSTOM_EVENT_5"`, `"STREAMED_IMPRESSIONS"`