---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-a-category
source: crawler
fetched_at: 2026-02-27T23:38:33.15597-03:00
rendered_js: true
word_count: 151
summary: This document provides technical specifications for the deprecated Spotify Web API endpoint used to retrieve metadata and icons for a single browse category.
tags:
    - spotify-api
    - browse-categories
    - api-reference
    - metadata
    - deprecated
category: api
---

Web API •References / Categories / Get Single Browse Category

## Get Single Browse Category

Deprecated

Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

## Request

- The desired language, consisting of an [ISO 639-1](http://en.wikipedia.org/wiki/ISO_639-1) language code and an [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), joined by an underscore. For example: `es_MX`, meaning "Spanish (Mexico)". Provide this parameter if you want the category strings returned in a particular language.  
  ***Note**: if `locale` is not supplied, or if the specified language is not available, the category strings returned will be in the Spotify default language (American English).*
  
  Example: `locale=sv_SE`

## Response

A category

- A link to the Web API endpoint returning full details of the category.
- The category icon, in various sizes.
  
  - The source URL of the image.
    
    Example: `"https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228"`
  - The image height in pixels.
    
    Example: `300`
  - The image width in pixels.
    
    Example: `300`
- The name of the category.
  
  Example: `"EQUAL"`

```
curl --request GET \
  --url https://api.spotify.com/v1/browse/categories/dinner \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"href": "string","icons": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"id": "equal","name": "EQUAL"}
```