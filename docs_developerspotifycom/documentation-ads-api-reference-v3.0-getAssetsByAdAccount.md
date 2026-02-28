---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAssetsByAdAccount
source: crawler
fetched_at: 2026-02-27T23:39:55.674619-03:00
rendered_js: true
word_count: 214
summary: This document specifies the 'Get Assets by Ad Account' API endpoint used to retrieve a paginated list of media asset metadata, including image, audio, and video details for a specific ad account.
tags:
    - ads-api
    - asset-management
    - media-assets
    - api-reference
    - ad-account
    - metadata-retrieval
    - pagination
category: api
---

Ads API •References / assets / Get Assets by Ad Account

## Get Assets by Ad Account

Returns list of asset metadata in descending order via the creation time within each asset type for a given ad account ID.

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- asset\_idsarray of strings
  
  A unique identifier for the entity.
  
  Example: `asset_ids=ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- asset\_typesarray of strings
  
  Allowed values: `"AUDIO"`, `"IMAGE"`, `"VIDEO"`Example: `asset_types=IMAGE`
- asset\_subtypesarray of strings
  
  The general type of audio asset, with ADSTUDIO\_SUPPLIED\_AUDIO and USER\_UPLOADED\_AUDIO being included as part of the AUDIO\_AD categorization.
  
  Allowed values: `"AUDIO_AD"`, `"BACKGROUND_MUSIC"`Example: `asset_subtypes=AUDIO_AD`
- The current status of an asset throughout lifecycle processes.
  
  Allowed values: `"ERROR"`, `"PROCESSING"`, `"READY"`, `"WAITING_UPLOAD"`Example: `statuses=READY`
- aspect\_ratiosarray of strings
  
  String representation of all supported aspect ratios
  
  Allowed values: `"HORIZONTAL_16_9"`, `"HORIZONTAL_1_91_1"`, `"SQUARE"`, `"VERTICAL_9_16"`
- Search word provided is applied to the asset name.
- Default: `sort_direction=DESC`Allowed values: `"ASC"`, `"DESC"`
- Allowed values: `"CREATED_AT"`, `"NAME"`
- Limit or page size for a given response.
  
  Default: `limit=50`Range: `1` - `50`Example: `limit=50`
- Starting position of the next record to assist in data pagination.
  
  Default: `offset=0`Example: `offset=0`

## Response

List of asset metadata objects.

- - total\_resultsinteger \[int32]
  - current\_pageinteger \[int32]
- Will be one of the following:
  
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
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/assets \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"paging": {"page_size": 50,"total_results": 116,"offset": 0},"assets": [{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "logoImage.png","asset_type": "IMAGE","status": "READY","url": "https://i.scdn.co/image/123","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","file_type": "JPEG"},{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","name": "logoImage.png","asset_type": "IMAGE","status": "READY","url": "https://i.scdn.co/image/123","created_at": "2026-01-23T04:56:07Z","updated_at": "2026-01-23T04:56:07Z","file_type": "JPEG"}]}
```