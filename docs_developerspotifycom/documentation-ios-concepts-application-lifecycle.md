---
title: Application Lifecycle | Spotify for Developers
url: https://developer.spotify.com/documentation/ios/concepts/application-lifecycle
source: crawler
fetched_at: 2026-02-27T23:40:53.989198-03:00
rendered_js: true
word_count: 193
summary: This document explains how to manage the Spotify App Remote SDK connection state during iOS app switching and application lifecycle events. It provides best practices for connecting and disconnecting the SDK to maintain stability and handle playback resumption.
tags:
    - spotify-sdk
    - ios-development
    - app-remote
    - app-switching
    - lifecycle-management
    - connection-handling
category: guide
---

When the App Remote SDK wants to wake up the Spotify client it must perform an app switch to do so. The Spotify client will use the redirect URI you have registered on the Developer Dashboard to switch back to your app once the user has approved the authorization (or once a token is retrieved if the user has already approved your app).

In order to make sure your app doesn't error during iOS App Switching, we recommend disconnecting the App Remote when your app is inactive, and reconnecting when your app is re-activated:

`1`

`- (void)applicationWillResignActive:(UIApplication *)application {`

`2`

`if (self.appRemote.isConnected) {`

`3`

`[self.appRemote disconnect];`

`4`

`}`

`5`

`}`

`6`

`7`

`- (void)applicationDidBecomeActive:(UIApplication *)application {`

`8`

`if (self.appRemote.connectionParameters.accessToken) {`

`9`

`[self.appRemote connect];`

`10`

`}`

`11`

`}`

Please note that currently an app switch is required to resume playback when the user pauses the music. We recommend having a button that says "Resume Playback" or "Open Spotify" if App Remote is not connected so it's clear to the user an app switch will occur. You should still show a normal play button if App Remote is connected and the music is paused however.