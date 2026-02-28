---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/createMobileAppInBusiness
source: crawler
fetched_at: 2026-02-27T23:39:31.061762-03:00
rendered_js: true
word_count: 330
summary: This document describes the API endpoint for creating a mobile application record to enable measurement within the Ads API, detailing required request parameters and response data.
tags:
    - ads-api
    - mobile-measurement
    - app-registration
    - api-reference
    - ios-android
    - partner-integration
category: api
---

Ads API •References / mobile-measurement / Create mobile app

## Create mobile app

## Request

- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

<!--THE END-->

- - The name of the mobile app.
    
    Length between `2` and `50`Example: `"My Android App"`
  - The unique identifier of the app, provided by the app platform.
    
    Length between `2` and `120`Example: `"com.example.myapp"`
  - The platform for the mobile app.
    
    Allowed values: `"IOS"`, `"ANDROID"`Example: `"ANDROID"`
  - The ad type for the mobile app.
    
    Allowed values: `"VIEW_THROUGH"`, `"STORE_KIT"`Example: `"VIEW_THROUGH"`
  - The unique identifier for an app.
    
    Supported content-type(s): Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
  - The unique identifier provided by iOS.
    
    Length between `2` and `255`Example: `"ABCD123489"`
  - The unique identifier provided by Android.
    
    Length between `2` and `255`Example: `"com.example.myapp"`
  - The Apple App Store URL for the mobile app.
    
    Maximum length: `512`Example: `"https://apps.apple.com/us/app/my-example-app/id1234567890"`
  - The Google Play Store URL for the mobile app.
    
    Maximum length: `512`Example: `"https://play.google.com/store/apps/details?id=com.example.myapp&hl=en_US"`
  - A unique identifying token for every Adjust link.
    
    Length between `6` and `50`Example: `"ABCD123489"`
  - mobile\_measurement\_partnerstring
    
    The available mobile measurement partners.
    
    Allowed values: `"KOCHAVA"`, `"APPS_FLYER"`, `"ADJUST"`Example: `"KOCHAVA"`
  - A unique identifier for the dataset.
    
    Example: `"0d86b9e9-70f0-4700-a725-3417ba8786f6"`
  - integration\_idstring \[uuid]
    
    A unique identifier for the integration.
    
    Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
  - The number of active or scheduled ad sets using the dataset.
    
    Example: `0`
  - Should this mobile app be used for SKADNetwork
    
    Example: `true`

## Response

Mobile app created.

- The name of the mobile app.
  
  Length between `2` and `50`Example: `"My Android App"`
- The unique identifier of the app, provided by the app platform.
  
  Length between `2` and `120`Example: `"com.example.myapp"`
- The platform for the mobile app.
  
  Allowed values: `"IOS"`, `"ANDROID"`Example: `"ANDROID"`
- The ad type for the mobile app.
  
  Allowed values: `"VIEW_THROUGH"`, `"STORE_KIT"`Example: `"VIEW_THROUGH"`
- The unique identifier for an app.
  
  Supported content-type(s): Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- The unique identifier provided by iOS.
  
  Length between `2` and `255`Example: `"ABCD123489"`
- The unique identifier provided by Android.
  
  Length between `2` and `255`Example: `"com.example.myapp"`
- The Apple App Store URL for the mobile app.
  
  Maximum length: `512`Example: `"https://apps.apple.com/us/app/my-example-app/id1234567890"`
- The Google Play Store URL for the mobile app.
  
  Maximum length: `512`Example: `"https://play.google.com/store/apps/details?id=com.example.myapp&hl=en_US"`
- A unique identifying token for every Adjust link.
  
  Length between `6` and `50`Example: `"ABCD123489"`
- mobile\_measurement\_partnerstring
  
  The available mobile measurement partners.
  
  Allowed values: `"KOCHAVA"`, `"APPS_FLYER"`, `"ADJUST"`Example: `"KOCHAVA"`
- A unique identifier for the dataset.
  
  Example: `"0d86b9e9-70f0-4700-a725-3417ba8786f6"`
- integration\_idstring \[uuid]
  
  A unique identifier for the integration.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- The number of active or scheduled ad sets using the dataset.
  
  Example: `0`
- Should this mobile app be used for SKADNetwork
  
  Example: `true`
- An ad account a mobile app has been shared to.
  
  - A unique identifier for an Ad Account.
    
    Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`

```
curl --request POST \
  --url https://api-partner.spotify.com/ads/v3/businesses/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/mobile_apps \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "mobile_app": {
        "name": "My Android App",
        "platform_app_id": "com.example.myapp",
        "platform": "ANDROID",
        "ad_type": "VIEW_THROUGH",
        "id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a",
        "ios_app_id": "ABCD123489",
        "android_app_url": "com.example.myapp",
        "apple_app_url": "https://apps.apple.com/us/app/my-example-app/id1234567890",
        "google_play_url": "https://play.google.com/store/apps/details?id=com.example.myapp&hl=en_US",
        "link_token": "ABCD123489",
        "mobile_measurement_partner": "KOCHAVA",
        "dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6",
        "integration_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a",
        "ad_set_count": 0,
        "is_skad_network": true,
        "shared_ad_accounts": [
            {
                "id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a",
                "name": "Spotify"
            }
        ]
    }
}'
```

* * *

## Response sample

```
{"name": "My Android App","platform_app_id": "com.example.myapp","platform": "ANDROID","ad_type": "VIEW_THROUGH","id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","ios_app_id": "ABCD123489","android_app_url": "com.example.myapp","apple_app_url": "https://apps.apple.com/us/app/my-example-app/id1234567890","google_play_url": "https://play.google.com/store/apps/details?id=com.example.myapp&hl=en_US","link_token": "ABCD123489","mobile_measurement_partner": "KOCHAVA","dataset_id": "0d86b9e9-70f0-4700-a725-3417ba8786f6","integration_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","ad_set_count": 0,"is_skad_network": true,"shared_ad_accounts": [{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "Spotify"}]}
```