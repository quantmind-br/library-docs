---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-users-profile
source: crawler
fetched_at: 2026-02-27T23:39:13.464271-03:00
rendered_js: true
word_count: 105
summary: This document provides technical details for the deprecated Spotify Web API endpoint used to retrieve public profile information for a specific user.
tags:
    - spotify-api
    - user-profile
    - endpoint-reference
    - get-request
    - deprecated-api
category: api
---

Web API •References / Users / Get User's Profile

## Get User's Profile

Deprecated

Get public profile information about a Spotify user.

## Request

## Response

A user

- The name displayed on the user's profile. `null` if not available.
- Known public external URLs for this user.
- Information about the followers of this user.
  
  - This will always be set to null, as the Web API does not support it at the moment.
  - The total number of followers.
- A link to the Web API endpoint for this user.
- The user's profile image.
  
  - The source URL of the image.
    
    Example: `"https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228"`
  - The image height in pixels.
    
    Example: `300`
  - The image width in pixels.
    
    Example: `300`

```
curl --request GET \
  --url https://api.spotify.com/v1/users/smedjan \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"display_name": "string","external_urls": {"spotify": "string"},"followers": {"href": "string","total": 0},"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"type": "user","uri": "string"}
```