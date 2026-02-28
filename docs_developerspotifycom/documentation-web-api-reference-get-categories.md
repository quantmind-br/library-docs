---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-categories
source: crawler
fetched_at: 2026-02-27T23:38:34.034362-03:00
rendered_js: true
word_count: 233
summary: This document provides technical details for the deprecated Spotify Web API endpoint used to retrieve a paginated list of browse categories, including request parameters and response formats.
tags:
    - spotify-api
    - web-api
    - browse-categories
    - pagination
    - api-reference
    - deprecated-api
category: api
---

Web API •References / Categories / Get Several Browse Categories

## Get Several Browse Categories

Deprecated

Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

## Request

- The desired language, consisting of an [ISO 639-1](http://en.wikipedia.org/wiki/ISO_639-1) language code and an [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), joined by an underscore. For example: `es_MX`, meaning "Spanish (Mexico)". Provide this parameter if you want the category strings returned in a particular language.  
  ***Note**: if `locale` is not supplied, or if the specified language is not available, the category strings returned will be in the Spotify default language (American English).*
  
  Example: `locale=sv_SE`
- The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
  
  Default: `limit=20`Range: `0` - `50`Example: `limit=10`
- The index of the first item to return. Default: 0 (the first item). Use with limit to get the next set of items.
  
  Default: `offset=0`Example: `offset=5`

## Response

A paged set of categories

- - A link to the Web API endpoint returning the full result of the request
    
    Example: `"https://api.spotify.com/v1/me/shows?offset=0&limit=20"`
  - The maximum number of items in the response (as set in the query or by default).
    
    Example: `20`
  - URL to the next page of items. ( `null` if none)
    
    Example: `"https://api.spotify.com/v1/me/shows?offset=1&limit=1"`
  - The offset of the items returned (as set in the query or by default)
    
    Example: `0`
  - URL to the previous page of items. ( `null` if none)
    
    Example: `"https://api.spotify.com/v1/me/shows?offset=1&limit=1"`
  - The total number of items available to return.
    
    Example: `4`

```
curl --request GET \
  --url https://api.spotify.com/v1/browse/categories \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"categories": {"href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20","limit": 20,"next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","offset": 0,"previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1","total": 4,"items": [{"href": "string","icons": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"id": "equal","name": "EQUAL"}]}}
```