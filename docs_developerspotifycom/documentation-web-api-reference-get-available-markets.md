---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-available-markets
source: crawler
fetched_at: 2026-02-27T23:38:42.526692-03:00
rendered_js: true
word_count: 37
summary: This document provides details on a deprecated Spotify Web API endpoint used to retrieve the list of country codes where Spotify is available.
tags:
    - spotify-api
    - markets
    - country-codes
    - deprecated-endpoint
    - available-markets
category: api
---

Web API •References / Markets / Get Available Markets

## Get Available Markets

Deprecated

Get the list of markets where Spotify is available.

## Request

## Response

A markets object with an array of country codes

- Example: `["CA","BR","IT"]`

```
curl --request GET \
  --url https://api.spotify.com/v1/markets \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"markets": ["CA", "BR", "IT"]}
```