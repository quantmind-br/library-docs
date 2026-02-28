---
title: Account Linking | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/tutorials/account
source: crawler
fetched_at: 2026-02-27T23:42:02.826272-03:00
rendered_js: true
word_count: 386
summary: This document explains how partners can link their users to Spotify accounts and manage content access through the Open Access API using OAuth 2.0 flows.
tags:
    - spotify-api
    - account-linking
    - oauth-2-0
    - open-access
    - entitlements
    - user-management
    - authentication
category: concept
---

Account linking makes it possible for partners to link their users to Spotify users, and to control the user's content access through Spotify’s Web API.

- Link their users to Spotify users.
- Control content access via the SOA API.

As a partner, you initiate account linking using the [OAuth 2.0 authorization code flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow) with Spotify’s OAuth 2.0 server. This returns an access token. Subsequent calls to the `/register-user` endpoint require this token to create a link between the third-party user and a Spotify account.

![SOA Linking Sequence](https://developer-assets.spotifycdn.com/images/documentation/open-access/soa-linking-sequence.png)

The image is also accessible with [better resolution](https://developer.spotify.com/images/documentation/open-access/soa-linking-sequence.png).

Account linking is initiated by the partner using the [OAuth 2.0 authorization code flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow) with Spotify’s OAuth 2.0 server. The resulting access token can be used to call the `/register-user` endpoint, creating a link between the third-party user and a Spotify account.

The API also provides endpoints to modify the access permissions (see [Entitlements](https://developer.spotify.com/documentation/open-access/concepts#entitlements)) for an already existing user, and to create new partner ID’s. These use the [OAuth 2.0 client credentials flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow), making it possible to call these endpoints without user involvement.

## Account unlinking

Users can manage their linked accounts at [content-access.spotify.com](https://content-access.spotify.com). By unlinking, they lose all access permissions on Spotify associated with that account. To regain access, they must go through the account linking flow again. Partners can direct their users to the [Content Access page](https://content-access.spotify.com) to verify what Spotify account is linked to the partner account and to see what shows they have access to.

The API also provides an endpoint [to unlink a user account](https://developer.spotify.com/documentation/open-access/reference/unlink-user). To prevent confusion, we advise to only call this endpoint when it's triggered by a user.

## Source of truth for account links

Spotify maintains the source of truth for which user accounts are linked to which partner user accounts. The integration should not attempt to determine this mapping itself. Therefore, whenever a user comes through the account linking flow, the integration should always call the `/register-user` endpoint. Failing to do so will lead to synchronization issues and ultimately a broken experience for the user.

To learn about the current state of an account link, please refer to the `/get-entitlements` endpoint. A 404 response from `/get-entitlements`, or any of the write-paths `/add-entitlements`, `/delete-entitlements`, and `/replace-entitlements`, means that no such account link exists, and the integration should stop sending entitlement updates to that account link.