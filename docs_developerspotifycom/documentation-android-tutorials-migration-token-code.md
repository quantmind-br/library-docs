---
title: Migrating from Token to Authorization Code Flow
url: https://developer.spotify.com/documentation/android/tutorials/migration-token-code
source: crawler
fetched_at: 2026-02-27T23:42:03.996628-03:00
rendered_js: true
word_count: 256
summary: This document provides instructions for migrating Android applications from the deprecated token flow to the more secure authorization code flow within the Spotify SDK.
tags:
    - android-sdk
    - spotify-api
    - authentication
    - migration-guide
    - oauth2
    - authorization-code-flow
category: guide
---

This guide explains how to migrate your Android application from `AuthorizationResponse.Type.TOKEN` to `AuthorizationResponse.Type.CODE`. This is necessary because the `TOKEN` flow is deprecated and will be removed in a future version of the Spotify Android SDK. To understand the differences between the two flows, see the [Implicit Grant documentation](https://developer.spotify.com/documentation/web-api/tutorials/implicit-flow) and the [Authorization Code Flow documentation](https://developer.spotify.com/documentation/web-api/tutorials/code-flow).

## Why migrate?

Spotify takes security seriously and is committed to protecting your applications and your users' data. The `CODE` flow provides a more secure way to authenticate your users and obtain access tokens.

## How to migrate

### Step 1: Identify where you use the `TOKEN` flow

Search your codebase for instances where you use the `AuthorizationResponse.Type.TOKEN` constant. This should give you an indication of where you need to make changes.

### Step 2: Update your code

Replace instances of `AuthorizationResponse.Type.TOKEN` with `AuthorizationResponse.Type.CODE`. This will make your authorization requests ask for an authorization code instead of an access token.

This step is completely new if you were using the `TOKEN` flow. After you receive the authorization code, you need to exchange it for an access token. To do this, you need to make a POST request to the Spotify Authorization Server. To understand how to do this, see the [Authorization Code Flow documentation](https://developer.spotify.com/documentation/web-api/tutorials/code-flow).

### Step 4: Familiarize yourself with the refresh token

Using the authorization code flow also means you get a refresh token. This token allows you to get a new access token without requiring any user interaction. To understand how to use the refresh token, see the [guide on how to use Refresh Tokens](https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens).