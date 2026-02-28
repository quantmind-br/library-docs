---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAsset
source: crawler
fetched_at: 2026-02-27T23:40:03.950805-03:00
rendered_js: true
word_count: 311
summary: This document provides the technical specifications for the Get Asset by ID endpoint, allowing users to retrieve detailed metadata for image, audio, and video assets within an ad account.
tags:
    - ads-api
    - asset-management
    - metadata-retrieval
    - api-reference
    - media-assets
category: api
---

Ads API •References / assets / Get Asset by ID

## Get Asset by ID

Returns asset metadata for a given asset ID.

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

## Response

Asset object.

Will be one of the following:

- Metadata object for an image asset type.
  
  - A unique identifier for the entity.
    
    Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
  - The name of the asset file.
    
    Example: `"logoImage.png"`
  - The current status of an asset throughout lifecycle processes.
    
    Allowed values: `"ERROR"`, `"PROCESSING"`, `"READY"`, `"WAITING_UPLOAD"`Example: `"READY"`
  - URL of asset. Will be either Google Cloud Storage URL or CDN URL depending on the asset type and the transcoding completion status.
    
    Example: `"https://i.scdn.co/image/123"`
  - created\_atstring \[date-time]
    
    Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Example: `"2026-01-23T04:56:07Z"`
  - updated\_atstring \[date-time]
    
    Date the entity was updated. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Example: `"2026-01-23T04:56:07Z"`
  - The file type of the image asset as defined by the 'file type' specification of the ISO base media file format standard.
    
    Allowed values: `"JPEG"`, `"PNG"`Example: `"JPEG"`
  - String representation of all supported aspect ratios
    
    Allowed values: `"HORIZONTAL_16_9"`, `"HORIZONTAL_1_91_1"`, `"SQUARE"`, `"VERTICAL_9_16"`
- Metadata object for an audio asset type.
  
  - A unique identifier for the entity.
    
    Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
  - The name of the asset file.
    
    Example: `"logoImage.png"`
  - The current status of an asset throughout lifecycle processes.
    
    Allowed values: `"ERROR"`, `"PROCESSING"`, `"READY"`, `"WAITING_UPLOAD"`Example: `"READY"`
  - URL of asset. Will be either Google Cloud Storage URL or CDN URL depending on the asset type and the transcoding completion status.
    
    Example: `"https://i.scdn.co/image/123"`
  - created\_atstring \[date-time]
    
    Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Example: `"2026-01-23T04:56:07Z"`
  - updated\_atstring \[date-time]
    
    Date the entity was updated. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Example: `"2026-01-23T04:56:07Z"`
  - Allowed values: `"ADSTUDIO_SUPPLIED_AUDIO"`, `"BACKGROUND_MUSIC"`, `"STOCK_BACKGROUND_MUSIC"`, `"USER_UPLOADED_AUDIO"`Example: `"USER_UPLOADED_AUDIO"`
  - duration\_msinteger \[int32]
    
    The duration of the asset in milliseconds. This value is populated as part of asset processing, and will be null until the asset is in ready state.
    
    Example: `30000`
  - The file type of the audio asset as defined by the 'file type' specification of the ISO base media file format standard.
    
    Allowed values: `"MP3"`, `"OGG"`, `"WAV"`
- Metadata object for a video asset type.
  
  - A unique identifier for the entity.
    
    Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
  - The name of the asset file.
    
    Example: `"logoImage.png"`
  - The current status of an asset throughout lifecycle processes.
    
    Allowed values: `"ERROR"`, `"PROCESSING"`, `"READY"`, `"WAITING_UPLOAD"`Example: `"READY"`
  - URL of asset. Will be either Google Cloud Storage URL or CDN URL depending on the asset type and the transcoding completion status.
    
    Example: `"https://i.scdn.co/image/123"`
  - created\_atstring \[date-time]
    
    Date the entity was created. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Example: `"2026-01-23T04:56:07Z"`
  - updated\_atstring \[date-time]
    
    Date the entity was updated. Time should be in ISO 8601 format using Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ
    
    Example: `"2026-01-23T04:56:07Z"`
  - duration\_msinteger \[int32]
    
    The duration of the asset in milliseconds. This value is populated as part of asset processing, and will be null until the asset is in ready state.
    
    Example: `30000`
  - String representation of all supported aspect ratios
    
    Allowed values: `"HORIZONTAL_16_9"`, `"HORIZONTAL_1_91_1"`, `"SQUARE"`, `"VERTICAL_9_16"`
  - The file type of the video asset as defined by the 'file type' specification of the ISO base media file format standard.
    
    Allowed values: `"MP4"`, `"QUICKTIME"`
  - thumbnail\_urlstring \[uri]
    
    URL of thumbnail image of the video asset.
    
    Example: `"https://adstudio-video-preview-image.spotifycdn.com/123-preview"`

```
curl --request GET \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/assets/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "logoImage.png","asset_type": "string","status": "READY","url": "https://i.scdn.co/image/123","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","file_type": "JPEG","aspect_ratio": "HORIZONTAL_16_9","width": 720,"height": 1280}
```