---
title: Application Lifecycle | Spotify for Developers
url: https://developer.spotify.com/documentation/android/tutorials/application-lifecycle
source: crawler
fetched_at: 2026-02-27T23:41:58.190217-03:00
rendered_js: true
word_count: 427
summary: This document outlines best practices for managing the connection lifecycle between an Android application and the Spotify client using the App Remote SDK, including error handling and resource optimization.
tags:
    - spotify-sdk
    - android-development
    - app-remote-api
    - connection-management
    - lifecycle-management
    - error-handling
category: guide
---

When an application connects to Spotify client through the SpotifyAppRemote API, it will prevent Spotify from shutting down even if the user is not playing anything. This is expected behavior - we want Spotify to remain active as long as there's something interacting with it. At the same time the application using the Spotify App Remote SDK should not keep Spotify alive if there's no need for it, for example if it's in the background. The Spotify client will take care of the background playback which means you don't need to do it. In most cases you don't need to implement your own service to keep the connection alive, it's enough to connect when user is actually interacting with your app and disconnect when they're not.

We recommend connecting to Spotify in the onStart method of the Activity that shows the playback state and controls, and disconnecting in the onStop method. Do not keep the connection alive when your app is in the background, **otherwise Spotify will not be able to shutdown when it's inactive**. We also recommend that your app checks for an existing connection before connecting again - otherwise two connections will be created and this will keep Spotify running in the background until the app is killed.

`1`

`@Override`

`2`

`protected void onStart() {`

`3`

`super.onStart();`

`4`

`SpotifyAppRemote.disconnect(mSpotifyAppRemote);`

`5`

`SpotifyAppRemote.connect(this, mConnectionParams, mConnectionListener);`

`6`

`}`

`7`

`8`

`@Override`

`9`

`protected void onStop() {`

`10`

`super.onStop();`

`11`

`SpotifyAppRemote.disconnect(mSpotifyAppRemote);`

`12`

`}`

If the connection succeeds, you're good to go! If it fails then you can use connection errors to show additional visual feedback to the user. For details about connection errors see the [error handling page](https://github.com/spotify/android-sdk/blob/master/app-remote-lib/ERRORS.md).

Specifically, for cases where the user is not logged in to Spotify, or the user has not authorized your app, you can use the Authorization Library to prompt them to log in and approve the required scopes.

`1`

`Connector.ConnectionListener mConnectionListener = new Connector.ConnectionListener() {`

`2`

`@Override`

`3`

`public void onConnected(SpotifyAppRemote spotifyAppRemote) {`

`4`

`mSpotifyAppRemote = spotifyAppRemote;`

`5`

`// setup all the things`

`6`

`}`

`7`

`8`

`@Override`

`9`

`public void onFailure(Throwable error) {`

`10`

`if (error instanceof NotLoggedInException || error instanceof UserNotAuthorizedException) {`

`11`

`// Show login button and trigger the login flow from auth library when clicked`

`12`

`} else if (error instanceof CouldNotFindSpotifyApp) {`

`13`

`// Show button to download Spotify`

`14`

`}`

`15`

`}`

`16`

`};`

`17`

`18`

`@Override`

`19`

`protected void onStart() {`

`20`

`super.onStart();`

`21`

`SpotifyAppRemote.disconnect(mSpotifyAppRemote);`

`22`

`SpotifyAppRemote.connect(this, mConnectionParams, mConnectionListener);`

`23`

`}`

`24`

`25`

`@Override`

`26`

`protected void onStop() {`

`27`

`super.onStop();`

`28`

`SpotifyAppRemote.disconnect(mSpotifyAppRemote);`

`29`

`}`