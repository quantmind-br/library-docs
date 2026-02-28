---
title: Token Swap and Refresh | Spotify for Developers
url: https://developer.spotify.com/documentation/ios/concepts/token-swap-and-refresh
source: crawler
fetched_at: 2026-02-27T23:40:52.554523-03:00
rendered_js: true
word_count: 298
summary: This document provides technical specifications for implementing token swap and refresh endpoints required by the Spotify iOS-SDK to manage authentication lifecycles.
tags:
    - spotify-ios-sdk
    - oauth2
    - authentication
    - token-management
    - token-swap
    - backend-integration
category: reference
---

Access tokens issued from the Spotify account service has a lifetime of one hour. The iOS-SDK provides helper functionality to simplify the use of the Code grant flow.

By setting [tokenSwapURL](https://developer.spotify.com/documentation/ios/concepts/token-swap-and-refresh#tokenswapurl) and [tokenRefreshURL](https://developer.spotify.com/documentation/ios/concepts/token-swap-and-refresh#tokenrefreshurl) it is possible for the iOS-SDK to request a new access token with a refresh token whenever needed. The iOS-SDK demo project has a Ruby example of the needed back-end services. The example is not recommended for use in production.

This page contains a description of the requests made by the iOS-SDK and the expected responses.

## tokenSwapURL

Swaps a code for an access token and a refresh token.

HeaderValueContent-Typeapplication/x-www-form-urlencoded

### Request Body

ParameterdescriptioncodeThe code returned from Spotify account service to be used in the token request.

### Request Example

`1`

`curl -X POST "https://example.com/v1/swap” -H "Content-Type: application/x-www-form-urlencoded" --data “code=AQDy8...xMhKNA”`

HeaderValueContent-Typeapplication/json

### Expected Response Body Parameters

Parameters must be JSON encoded.

Parameterdescriptionaccess\_tokenAccess token received from Spotify account service.expires\_inThe time period (in seconds) for which the access token is valid. Returned from the Spotify account service.refresh\_tokenThe refresh token returned from the Spotify account service. It should not return the actual refresh token but a reference to the token or an encrypted version of the token. Encryption solution is shown in the ruby example.

### Response Example

`1`

`{`

`2`

`"access_token" : "NgAagA...Um_SHo",`

`3`

`"expires_in" : "3600",`

`4`

`"refresh_token" : "NgCXRK...MzYjw"`

`5`

`}`

## tokenRefreshURL

Uses the refresh token to get a new access token.

HeaderValueContent-Typeapplication/x-www-form-urlencoded

### Request Body

Parameterdescriptionrefresh\_tokenThe refresh\_token value previously returned from the token swap endpoint.

### Request Example

`1`

`curl -X POST "https://example.com/v1/refresh" -H "Content-Type: application/x-www-form-urlencoded" --data "refresh_token=NgCXRK...MzYjw"`

HeaderValueContent-Typeapplication/json

### Expected Response Body Parameters

Parameterdescriptionaccess\_tokenAccess token received from Spotify account service.expires\_inThe time period (in seconds) for which the access token is valid. Returned from the Spotify account service.

### Response Example

`1`

`{`

`2`

`"access_token" : "NgAagA...Um_SHo",`

`3`

`"expires_in" : "3600"`

`4`

`}`