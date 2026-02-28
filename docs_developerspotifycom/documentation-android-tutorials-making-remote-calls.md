---
title: Making Remote Calls | Spotify for Developers
url: https://developer.spotify.com/documentation/android/tutorials/making-remote-calls
source: crawler
fetched_at: 2026-02-27T23:41:59.338148-03:00
rendered_js: true
word_count: 183
summary: This guide explains how to perform synchronous and asynchronous remote calls and manage event subscriptions using the Spotify App Remote SDK. It focuses on handling results via CallResult and Subscription objects for real-time interaction with the Spotify app.
tags:
    - spotify-sdk
    - app-remote-sdk
    - asynchronous-calls
    - event-handling
    - api-requests
    - android-development
category: guide
---

This guide explains how to make remote calls from your app to the Spotify app with the App Remote SDK.

When you make a call via any of the APIs you receive an instance of a `CallResult<T>` object. `CallResult<T>` lets you receive results both asynchronously or synchronously. Lets take a look at the example of a synchronous call:

`1`

`CallResult<PlayerState> playerStateCall = playerApi.getPlayerState();`

`2`

`Result<PlayerState> playerStateResult = playerStateCall.await(10, TimeUnit.SECONDS);`

`3`

`if (playerStateResult.isSuccessful()) {`

`4`

`PlayerState playerState = playerStateResult.getData();`

`5`

`// have some fun with playerState`

`6`

`} else {`

`7`

`Throwable error = playerStateResult.getError();`

`8`

`// try to have some fun with the error`

`9`

`}`

And the preferable async way to do the same thing:

`1`

`playerApi.getPlayerState()`

`2`

`.setResultCallback(playerState -> {`

`3`

`// have fun with playerState`

`4`

`})`

`5`

`.setErrorCallback(throwable -> {`

`6`

`// =(`

`7`

`});`

As a result of subscription you receive a `Subscription<T>` object. For example:

`1`

`playerApi.subscribeToPlayerState()`

`2`

`.setEventCallback(playerState -> {`

`3`

`// the Spotify App keeps you updated on PlayerState with this event`

`4`

`})`

`5`

`.setErrorCallback(throwable -> {`

`6`

`// =( =( =(`

`7`

`});`