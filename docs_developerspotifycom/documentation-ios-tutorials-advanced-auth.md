---
title: Advanced User Authentication | Spotify for Developers
url: https://developer.spotify.com/documentation/ios/tutorials/advanced-auth
source: crawler
fetched_at: 2026-02-27T23:40:51.854555-03:00
rendered_js: true
word_count: 506
summary: This document provides a step-by-step guide for implementing authorization and session management in an iOS application using the Spotify iOS SDK.
tags:
    - ios-sdk
    - spotify-api
    - authentication
    - swift
    - oauth2
    - session-management
    - app-delegate
category: guide
---

In order for the iOS SDK to control the Spotify app, they will need to authorize your app. The functionality to do this is built in and can be implemented directly inside of your `AppDelegate.swift`:

#### Implement Session Delegate

In order to handle auth, we need to add a `SPTSessionManagerDelegate` inside of your `AppDelegate.swift`:

`1`

`class AppDelegate: UIResponder, UIApplicationDelegate, SPTSessionManagerDelegate {`

`2`

`...`

This will require us to implement the following three methods:

`1`

`func sessionManager(manager: SPTSessionManager, didInitiate session: SPTSession) {`

`2`

`print("success", session)`

`3`

`}`

`4`

`func sessionManager(manager: SPTSessionManager, didFailWith error: Error) {`

`5`

`print("fail", error)`

`6`

`}`

`7`

`func sessionManager(manager: SPTSessionManager, didRenew session: SPTSession) {`

`8`

`print("renewed", session)`

`9`

`}`

#### Instantiate `SPTConfiguration`

At a class-level, we can define our Client ID, Redirect URI and instantiate the SDK:

`1`

`let SpotifyClientID = "[your spotify client id here]"`

`2`

`let SpotifyRedirectURL = URL(string: "spotify-ios-quick-start://spotify-login-callback")!`

`3`

`4`

`lazy var configuration = SPTConfiguration(`

`5`

`clientID: SpotifyClientID,`

`6`

`redirectURL: SpotifyRedirectURL`

`7`

`)`

#### Setup Token Swap

The authentication process provides a `refresh_token`, which can be stored locally inside your app. This can be used, along with your Client ID, Client Secret and Redirect URL, to obtain an `access_token` that is valid for 60 minutes.

However, as we strongly discourage the use of Client Secrets in your iOS app code, we have written two well-documented web server examples that can do this for you:

- [Glitch](https://glitch.com/~spotify-token-swap)
- [One-click deploy with Heroku](https://github.com/bih/spotify-token-swap-service#one-click-with-heroku)

Once you have set them up, and have the `tokenSwapURL` and `tokenRefreshURL` we can set this up in our `AppDelegate.swift` in a class-level closure:

`1`

`lazy var sessionManager: SPTSessionManager = {`

`2`

`if let tokenSwapURL = URL(string: "https://[my token swap app domain]/api/token"),`

`3`

`let tokenRefreshURL = URL(string: "https://[my token swap app domain]/api/refresh_token") {`

`4`

`self.configuration.tokenSwapURL = tokenSwapURL`

`5`

`self.configuration.tokenRefreshURL = tokenRefreshURL`

`6`

`self.configuration.playURI = ""`

`7`

`}`

`8`

`let manager = SPTSessionManager(configuration: self.configuration, delegate: self)`

`9`

`return manager`

`10`

`}()`

#### Configure Initial Music

iOS requires us to define a `playURI` (as shown in the last step) in order to play music to wake up the Spotify main application. This is an iOS-specific requirement. There's two values `self.configuration.playURI` accepts:

**An empty value:** If empty, it will resume playback of user's last track. Example:

`1`

`self.configuration.playURI = ""`

**A valid Spotify URI:** Otherwise, provide a Spotify URI. Example:

`1`

`self.configuration.playURI = "spotify:track:20I6sIOMTCkB6w7ryavxtO"`

#### Invoke Auth Modal

With `SPTConfiguration` and `SPTSessionManager` both configured, we can invoke the authorization screen. Notice the optional *campaign* parameter, which can be set for attribution purposes to help indicate where the account linking was initiated from:

`1`

`let requestedScopes: SPTScope = [.appRemoteControl]`

`2`

`self.sessionManager.initiateSession(with: requestedScopes, options: .default, campaign: "utm-campaign")`

#### Configure Auth Callback

Once a user successfully returns to your application, we'll need to notify `sessionManager` about it by implementing the following method:

`1`

`func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {`

`2`

`self.sessionManager.application(app, open: url, options: options)`

`3`

`return true`

`4`

`}`

Now, when a user authorizes, they should return to your application with the `sessionManager(manager: SPTSessionManager, didInitiate session: SPTSession)` method being successfully invoked.