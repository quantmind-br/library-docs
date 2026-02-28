---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAdAccount
source: crawler
fetched_at: 2026-02-27T23:39:55.717225-03:00
rendered_js: true
word_count: 2
summary: Provides a sample JSON response representing a business or ad account profile, detailing the structure of fields such as billing addresses, status, and industry information.
tags:
    - json-sample
    - business-profile
    - ad-account
    - api-response
    - data-structure
    - metadata
category: reference
---

## Response sample

```
{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","business_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","country_code": "US","industry": "Media & Entertainment","website": "https://www.spotify.com","billing_address": {"name": "Entity_1","street": "123 Spotify Avenue","city": "Los Angeles","region": "California","postal_code": "90210","tax_region": "ES"},"legal_entity_name": "Spotify AB","status": "ACTIVE","status_reason": "string","name": "Nike SB","ad_account_role": "AD_ACCOUNT_ADMIN","tax_id": "ATU82660371","currency_code": "USD"}
```