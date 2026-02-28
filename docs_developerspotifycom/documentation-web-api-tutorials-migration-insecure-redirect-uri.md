---
title: Migrate away from Insecure Redirect URIs
url: https://developer.spotify.com/documentation/web-api/tutorials/migration-insecure-redirect-uri
source: crawler
fetched_at: 2026-02-27T23:38:19.038-03:00
rendered_js: true
word_count: 194
summary: This document provides instructions for migrating Spotify applications to secure redirect URIs by replacing insecure protocols and updating localhost addresses to loopback IPs.
tags:
    - spotify-web-api
    - redirect-uri
    - authentication
    - security-migration
    - oauth2
    - developer-console
category: guide
---

Spotify is deprecating the use of insecure redirect URIs. This guide will help you migrate your application to use secure redirect URIs. To better understand which redirect URIs are considered secure, please refer to the [Redirect URI](https://developer.spotify.com/documentation/web-api/concepts/redirect_uri) guide.

## Prerequisites

This guide assumes that:

- You have read the [authorization guide](https://developer.spotify.com/documentation/web-api/concepts/authorization).
- You have created an app following the [app guide](https://developer.spotify.com/documentation/web-api/concepts/apps).
- You have read the [Redirect URI](https://developer.spotify.com/documentation/web-api/concepts/redirect_uri) guide.
- You have access to the [console](https://developer.spotify.com/dashboard/applications) to update your app settings.

## Migrate from Insecure Redirect URIs

In you app settings, you can see all the redirect URIs that are currently setup. Make sure to check all of them and update any non-loopback addresses that are using `http://` to `https://` if possible. If not possible remove them and add the new secure redirect URIs.

If there are any redirect URIs that are pointing to localhost, you need to update those to point to a loopback address. For example, if you have `http://localhost:8888/callback` you should update it to `http://127.0.0.1:8888/callback`. We do support dynamic ports for loopback interfaces, you can read more [here](https://developer.spotify.com/documentation/web-api/concepts/redirect_uri) .

If you see any redirect URIs that are not in use, make sure to remove them as well.