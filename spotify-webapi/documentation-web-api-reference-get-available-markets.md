---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-available-markets
source: crawler
fetched_at: 2026-02-27T23:46:44.284716-03:00
rendered_js: false
word_count: 41
summary: This document outlines the deprecated Spotify Web API endpoint used to retrieve a list of country codes where the service is available.
tags:
    - spotify-web-api
    - markets
    - http-get
    - deprecated-endpoint
    - country-codes
category: api
---

Web API •References / Markets / Get Available Markets

## Get Available Markets

Deprecated

Get the list of markets where Spotify is available.

## Request

GET/markets

## Response

A markets object with an array of country codes

- marketsarray of strings
  
  Example: `["CA","BR","IT"]`

## Response sample

```
{"markets": ["CA", "BR", "IT"]}
```