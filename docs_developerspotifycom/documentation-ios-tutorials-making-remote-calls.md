---
title: Making Remote Calls | Spotify for Developers
url: https://developer.spotify.com/documentation/ios/tutorials/making-remote-calls
source: crawler
fetched_at: 2026-02-27T23:40:54.274088-03:00
rendered_js: true
word_count: 92
summary: Explains how to use the callback pattern for handling API responses and errors when interacting with the Spotify App Remote SDK.
tags:
    - spotify-sdk
    - ios-development
    - error-handling
    - app-remote
    - callbacks
category: guide
---

When you interact with any of the APIs you pass in a `SPTAppRemoteCallback` block that gets invoked with either the expected result item or an `NSError` if the operation failed. The block is triggered after the command was received by the Spotify app (or if the connection could not be made).

Here is an example using the `SPTRemotePlayerAPI` to skip a song:

`1`

`[appRemote.playerAPI skipToNext:^(id _Nullable result, NSError * _Nullable error) {`

`2`

`if (error) {`

`3`

`// Operation failed`

`4`

`} else {`

`5`

`// Operation succeeded`

`6`

`}`

`7`

`}];`