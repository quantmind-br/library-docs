---
title: Threading | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/threading
source: crawler
fetched_at: 2026-02-27T23:41:25.40633-03:00
rendered_js: true
word_count: 323
summary: This document explains the thread-safety requirements of the Spotify Embedded SDK, detailing how to correctly handle API calls from multiple threads using message-passing techniques.
tags:
    - spotify-embedded-sdk
    - thread-safety
    - multi-threading
    - concurrency
    - error-handling
    - message-passing
category: guide
---

The Spotify Embedded SDK is **NOT** thread-safe.

You must make sure that you only ever invoke Spotify Embedded APIs from the same thread. This means, if you invoked [SpInit()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spinit) from one thread, all subsequent actions in the Spotify Embedded SDK must be performed from the same thread. If, for example, your application has a separate UI thread that needs to invoke APIs, the recommended way of doing this is to make your UI thread send an application-specific message to the other thread.

On most platforms, the Spotify Embedded SDK will return the error [kSpErrorMultiThreadingDetected](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sperror) if you invoke APIs from different threads. (On some platforms, the SDK is unable to detect this, and the behavior will be undefined.)

This is how the example code in the SDK package solves the issue of multiple threads: Instead of invoking the API from the UI thread, you can send some form of message to the main Embedded SDK thread, and have the main thread execute the API between calls to [SpPumpEvents()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sppumpevents).

**Note** For simplicity, the following code simply sets an integer when a button is pressed, and the main thread executes the API when the integer is set. You could use a proper message queue instead.

`1`

`/* Recommended implementation */`

`2`

`3`

`enum ButtonID {`

`4`

`kButtonNone = 0,`

`5`

`kButtonSkipToNext = 1`

`6`

`};`

`7`

`8`

`int button_pressed = kButtonNone;`

`9`

`10`

`void MainESDKThread(void) {`

`11`

`while (!shutdown) {`

`12`

`if (button_pressed == kButtonSkipToNext) {`

`13`

`SpPlaybackSkipToNext();`

`14`

`button_pressed = kButtonNone;`

`15`

`}`

`16`

`SpPumpEvents();`

`17`

`}`

`18`

`}`

`19`

`20`

`void UIThread(void) {`

`21`

`while (!shutdown) {`

`22`

`if (NextButtonWasPressed()) {`

`23`

`button_pressed = kButtonSkipToNext;`

`24`

`}`

`25`

`}`

`26`

`}`

#### Other considerations

If you implement [ZeroConf](https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/zeroconf), the web server that handles ZeroConf requests might run in a different thread as well. Make sure to add proper message-passing so that the web server thread does not invoke Embedded SDK APIs from its own thread.