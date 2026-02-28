---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateAdAccount
source: crawler
fetched_at: 2026-02-27T23:39:58.070575-03:00
rendered_js: true
word_count: 391
summary: This document provides technical specifications for the Update Ad Account endpoint, detailing the required parameters and response structure for modifying ad account details.
tags:
    - ads-api
    - ad-accounts
    - endpoint-reference
    - account-management
    - patch-request
category: api
---

Ads API •References / ad-accounts / Update Ad Account

## Update Ad Account

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

<!--THE END-->

- Name given to identify your account.
  
  Pattern: `^(?!\s).+(?<!\s)$`Length between `1` and `120`Example: `"Account Name"`
- Allowed values: `"AGENCY"`, `"AUTO"`, `"AUTOMOTIVE"`, `"BUSINESS_SERVICES_INDUSTRIALS"`, `"CPG"`, `"EDUCATION_TRAINING"`, `"ENERGY_UTILITIES"`, `"FINANCE"`, `"FINANCIAL_REAL_ESTATE"`, `"FOOD_DINING_SERVICES"`, `"GAMING"`, `"GOVERNMENT_NON_PROFIT"`, `"HEALTH_WELLNESS"`, `"JOBS_EDUCATION"`, `"LAW_GOVERNMENT_POLITICAL_NON_PROFIT"`, `"MEDIA_ENTERTAINMENT"`, `"MEDICAL_PHARMACEUTICAL"`, `"OTHER"`, `"POLITICAL"`, `"RESTAURANTS_FOOD_SERVICE"`, `"RETAIL"`, `"RETAILER_WHOLESALE"`, `"TECHNOLOGY"`, `"TELECOM"`, `"TELECOMMUNICATIONS"`, `"TRAVEL_LEISURE"`, `"TRAVEL_TOURISM"`
- - Billing name for the account that will appear on bills and invoices.
    
    Pattern: `^\S(.*\S)?$`Length between `1` and `120`Example: `"Entity_1"`
  - Street number and address of ad account.
    
    Example: `"123 Spotify Avenue"`
  - Region where city is located.
    
    Example: `"California"`
  - Geo in ISO alpha-2 country code format for taxable country.
    
    Example: `"ES"`
- The tax ID on record for the ad account.
  
  Example: `"ATU82660371"`
- The legal name of the entity funding ads for the ad account.
  
  Example: `"Spotify AB"`
- The website associated with the ad account.
  
  Example: `"https://www.spotify.com"`
- restricted\_ad\_categorystring
- - - Billing name for the account that will appear on bills and invoices.
      
      Pattern: `^\S(.*\S)?$`Length between `1` and `120`Example: `"Entity_1"`
    - Street number and address of ad account.
      
      Example: `"123 Spotify Avenue"`
    - Region where city is located.
      
      Example: `"California"`
    - Geo in ISO alpha-2 country code format for taxable country.
      
      Example: `"ES"`
  - The billing currency for the account
    
    Maximum length: `3`Example: `"USD"`

## Response

Metadata of business' permission to an ad account.

- A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- created\_atstring \[date-time]
  
  Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- updated\_atstring \[date-time]
  
  Date the entity was updated. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
  
  Example: `"2026-01-23T04:56:07Z"`
- The country or region of the geo in ISO alpha-2 country code format.
  
  Example: `"US"`
- The Ad Account's listed industry.
  
  Example: `"Media & Entertainment"`
- The website associated with the ad account.
  
  Example: `"https://www.spotify.com"`
- - Billing name for the account that will appear on bills and invoices.
    
    Pattern: `^\S(.*\S)?$`Length between `1` and `120`Example: `"Entity_1"`
  - Street number and address of ad account.
    
    Example: `"123 Spotify Avenue"`
  - Region where city is located.
    
    Example: `"California"`
  - Geo in ISO alpha-2 country code format for taxable country.
    
    Example: `"ES"`
- The legal name of the entity funding ads for the ad account.
  
  Supported content-type(s): Example: `"Spotify AB"`
- The status of the ad account.
  
  Allowed values: `"ACTIVE"`, `"INACTIVE"`, `"GREY_LISTED"`, `"SUSPEND_LISTED"`, `"BLACKLISTED"`
- The reason for the status of the ad account.
- Name given to identify your account.
  
  Pattern: `^\S.*\S$`Example: `"Nike SB"`
- The role of a user in an ad account.
  
  Allowed values: `"AD_ACCOUNT_ADMIN"`, `"AD_ACCOUNT_CONTRIBUTOR"`, `"AD_ACCOUNT_VIEWER"`
- The tax ID on record for the ad account.
  
  Example: `"ATU82660371"`
- The billing currency for the account
  
  Maximum length: `3`Example: `"USD"`

```
curl --request PATCH \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "Account Name",
    "industry": "AGENCY",
    "billing_address": {
        "name": "Entity_1",
        "street": "123 Spotify Avenue",
        "city": "Los Angeles",
        "region": "California",
        "postal_code": "90210",
        "tax_region": "ES"
    },
    "tax_id": "ATU82660371",
    "legal_entity_name": "Spotify AB",
    "website": "https://www.spotify.com",
    "restricted_ad_category": "string",
    "internal": {
        "bill_to_address": {
            "name": "Entity_1",
            "street": "123 Spotify Avenue",
            "city": "Los Angeles",
            "region": "California",
            "postal_code": "90210",
            "tax_region": "ES"
        },
        "tax_ids": [
            {
                "id": "ATU82660371",
                "type": "VAT"
            }
        ],
        "currency_code": "USD"
    }
}'
```

* * *

## Response sample

```
{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","business_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","country_code": "US","industry": "Media & Entertainment","website": "https://www.spotify.com","billing_address": {"name": "Entity_1","street": "123 Spotify Avenue","city": "Los Angeles","region": "California","postal_code": "90210","tax_region": "ES"},"legal_entity_name": "Spotify AB","status": "ACTIVE","status_reason": "string","name": "Nike SB","ad_account_role": "AD_ACCOUNT_ADMIN","tax_id": "ATU82660371","currency_code": "USD"}
```