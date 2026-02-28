---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile
source: crawler
fetched_at: 2026-02-27T23:45:26.913395-03:00
rendered_js: true
word_count: 239
summary: This document provides the technical specification for an API endpoint used to retrieve detailed profile information for the currently authenticated user.
tags:
    - web-api
    - user-profile
    - user-data
    - api-endpoint
    - authentication
category: api
---

Web API •References / Users / Get Current User's Profile

## Get Current User's Profile

Get detailed profile information about the current user (including the current user's username).

## Request

## Response

A user

- The name displayed on the user's profile. `null` if not available.
- The user's email address, as entered by the user when creating their account. ***Important!** This email address is unverified; there is no proof that it actually belongs to the user.* *This field is only available when the current user has granted access to the [user-read-email](https://developer.spotify.com/documentation/web-api/concepts/scopes#list-of-scopes) scope.*
- The user's explicit content settings. *This field is only available when the current user has granted access to the [user-read-private](https://developer.spotify.com/documentation/web-api/concepts/scopes#list-of-scopes) scope.*
  
  - When `true`, indicates that explicit content should not be played.
  - When `true`, indicates that the explicit content setting is locked and can't be changed by the user.
- Known external URLs for this user.
- Information about the followers of the user.
  
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
- The user's Spotify subscription level: "premium", "free", etc. (The subscription level "open" can be considered the same as "free".) *This field is only available when the current user has granted access to the [user-read-private](https://developer.spotify.com/documentation/web-api/concepts/scopes#list-of-scopes) scope.*

## Response sample

```
{"country": "string","display_name": "string","email": "string","explicit_content": {"filter_enabled": false,"filter_locked": false},"external_urls": {"spotify": "string"},"followers": {"href": "string","total": 0},"href": "string","id": "string","images": [{"url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228","height": 300,"width": 300}],"product": "string","type": "string","uri": "string"}
```