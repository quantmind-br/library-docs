---
title: Increasing the security requirements for integrating with Spotify
url: https://developer.spotify.com/blog/2025-02-12-increasing-the-security-requirements-for-integrating-with-spotify
source: crawler
fetched_at: 2026-02-27T23:40:14.167395-03:00
rendered_js: true
word_count: 408
summary: This document announces upcoming security changes for Spotify integrations, including the deprecation of the implicit grant flow and the removal of support for unencrypted HTTP redirect URIs. It outlines the migration timeline and provides recommendations for moving to more secure authentication methods like PKCE.
tags:
    - spotify-api
    - authentication
    - oauth2
    - pkce
    - security-update
    - implicit-grant
    - redirect-uri
category: guide
---

Increasing the security requirements for integrating with Spotify

Posted February 12, 2025

![](https://developer.spotify.com/images/avatars/spotify.png)

Spotify

## TL;DR

To improve security for our users, Spotify is planning to remove support for two ways of integrating with Spotify that have been replaced with more secure alternatives. This includes deprecating use of [the implicit grant](https://developer.spotify.com/documentation/web-api/tutorials/implicit-flow) as well as removing support for unencrypted HTTP redirect URIs for your client.

**All clients created from the 9th of April 2025 will have the new rules enforced automatically. Migration of existing clients to an acceptable state must be made by November 2025.**

[Here is a detailed guide with migration instructions.](https://developer.spotify.com/documentation/web-api/tutorials/migration-implicit-auth-code)

## Why is this happening?

PKCE for the authorization code grant introduced clients that can’t maintain a client secret (such as mobile apps or client side web applications) to a more secure way to integrate with Spotify. Current OAuth security best practices [recommend against the use of the implicit grant](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-23#section-2.1.2), and [it will shortly be removed](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-09.html#name-removal-of-the-oauth-20-imp).

Similarly, the widespread adoption of HTTPS across the internet has made it much easier to accept redirects over HTTPS instead of unencrypted HTTP. By moving traffic from HTTP to HTTPS, users of applications that integrate with Spotify will be better protected against attacks that intercept network traffic.

## What next?

### The implicit grant

If you are using the implicit grant (sending `response_type=token` in your call to the authorization endpoint, or [in the Android SDK](https://developer.spotify.com/documentation/android/tutorials/authorization) using `AuthorizationResponse.Type.TOKEN`), then you will need to migrate to the authorization code grant.

If you are using a public client (one which cannot securely store a secret), you will be expected to use the [PKCE extension](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow). Confidential clients (ones which can store a secret) [must use it](https://developer.spotify.com/documentation/web-api/tutorials/code-flow).

### HTTP redirect URIs

Any redirect URI using HTTP will stop being supported, except loopback IP address literals such as `http://127.0.0.1` for IPv4 and `http://[::1]` for IPv6. Any invalid redirect URIs will need to be changed. You can check them under your client’s ‘settings’ tab in the developer console.

Redirects using a custom scheme will still be supported, but we recommend developers to use HTTPS redirects where possible. For mobile applications, we recommend using Android App Links and iOS Universal Links where possible.

For example:

- `http://www.example.com` could be migrated to `https://www.example.com`
- `http://localhost:3000` could be migrated to `http://127.0.0.1:3000`
- `com.example://callback` can still be used as before

**Please make these checks for yourself. Comprehensive guidance will also be published via updates to the developer portal documentation.**

Reach out to us on the developer community [forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer) for feedback.