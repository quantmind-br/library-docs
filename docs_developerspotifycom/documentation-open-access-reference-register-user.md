---
title: Open Access Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/reference/register-user
source: crawler
fetched_at: 2026-02-27T23:39:23.502928-03:00
rendered_js: true
word_count: 225
summary: This document describes the API endpoint for linking a Spotify user to a partner user ID and managing their entitlements within the Open Access framework. It outlines request requirements, including JWT payload structure and the mandatory redirect process to complete account linking.
tags:
    - spotify-api
    - account-linking
    - user-registration
    - entitlements
    - jwt-authentication
    - open-access
category: api
---

Open Access •References / Register new user

## Register new user

**Required scope:** `user-soa-link`

There must be a 1:1 mapping between a Spotify user and a partner user ID (PUID). A Spotify account can only be linked to a single PUID, and vice versa. If the Spotify user has already been linked to the PUID, the entitlements in the request will replace all existing entitlements.

Spotify maintains the source of truth for which user accounts are linked to which partner user accounts. The integration should not attempt to determine this mapping itself. Therefore, whenever a user comes through the account linking flow, the integration should always call this endpoint to register the user. Failing to do so will lead to synchronization issues and ultimately a broken experience for the user.

Finally, in the case of a successful registration, the integration should always redirect the user to the completion\_url provided in the response.

## Request

This endpoint requires the payload to be [provided as a JWT](https://developer.spotify.com/documentation/open-access/concepts#jwt--jws-usage).

The payload has the following fields:

PropertyTypeRequiredDescriptionpartner\_idstringyes[Partner ID](https://developer.spotify.com/documentation/open-access/concepts#partner-id)partner\_user\_idstringyes[Partner User ID](https://developer.spotify.com/documentation/open-access/concepts#partner-user-id)entitlementsarray\[string]N/Ayes

## Response

A successful response will have HTTP status code 200 and the body will contain a json payload providing the url that the user must be directed to in order to complete the linking process.

- The spotify.com page that the user must be redirected to complete the account linking flow

```
curl --request POST \
  --url https://open-access.spotify.com/api/v1/register-user \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"completion_url": "https://spotify.com/link/"}
```