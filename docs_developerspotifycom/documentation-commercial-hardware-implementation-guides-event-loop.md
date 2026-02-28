---
title: The Event Loop | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/event-loop
source: crawler
fetched_at: 2026-02-27T23:41:23.023754-03:00
rendered_js: true
word_count: 502
summary: This document explains how to implement the main event loop and manage authentication processes using the Spotify Embedded SDK, including requirements for threading and callback efficiency.
tags:
    - spotify-embedded-sdk
    - event-loop
    - authentication
    - threading
    - callbacks
    - asynchronous-processing
category: guide
---

In order to do work, the library function [SpPumpEvents()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sppumpevents) must be called periodically. This is where the library performs all asynchronous operations, and this is where it invokes the callback functions that the application registers (such as the error callback that is specified in [SpConfig::error\_callback](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig)).

There are two major ways to write the main event loop:

- Call [SpPumpEvents()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sppumpevents) from the application's main event loop
- Call [SpPumpEvents()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sppumpevents) from a separate thread and communicate with the application's main thread

In both cases, you must make sure that you never invoke Spotify Embedded APIs from different threads. The Spotify Embedded SDK is not thread-safe, and will typically refuse to execute APIs called from another thread. See Threading for details.

## Logging In And Logging Out

**Note**: The following example uses [SpConnectionLoginOauthToken()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionloginoauthtoken:~:text=SpConnectionLoginOauthToken%28%29) to log in. This API exists for testing purposes only.

In order to be certified, hardware devices must either enable the internal ZeroConf implementation (see [SpConfig::zeroconf\_serve](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig)), or implement the ZeroConf in the eSDK integration and use the function [SpConnectionLoginZeroConf()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionloginpassword:~:text=SpConnectionLoginZeroConf%28%29) to log in.

Change the code from the previous example so that it passes a valid Spotify OAuth access token (see [Authorization Guide](https://developer.spotify.com/documentation/general/guides/authorization-guide/)) to SpConnectionLoginOauthToken(). Register a callback of type [SpCallbackConnectionNotify()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spcallbackconnectionnotify) by calling [SpRegisterConnectionCallbacks()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spregisterconnectioncallbacks) to receive the notification [kSpConnectionNotifyLoggedIn](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionnotification)when login is successful.

As soon as the example application has logged in successfully, it will log out again using [SpConnectionLogout()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionlogout) and wait for the notification [kSpConnectionNotifyLoggedOut](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionnotification).

Here is the new code:

`1`

`int has_logged_in = 0;`

`2`

`int has_logged_out = 0;`

`3`

`4`

`static void CallbackConnectionNotify(enum SpConnectionNotification event,`

`5`

`void *context) {`

`6`

`switch (event) {`

`7`

`case kSpConnectionNotifyLoggedIn:`

`8`

`LOG("Logged in\n");`

`9`

`has_logged_in = 1;`

`10`

`break;`

`11`

`case kSpConnectionNotifyLoggedOut:`

`12`

`LOG("Logged out\n");`

`13`

`has_logged_in = 0;`

`14`

`has_logged_out = 1;`

`15`

`break;`

`16`

`...`

`17`

`18`

`default:`

`19`

`break;`

`20`

`}`

`21`

`}`

`22`

`23`

`...`

`24`

`25`

`int main(int argc, char *argv[]) {`

`26`

`SpError err;`

`27`

`struct SpConnectionCallbacks connection_callbacks;`

`28`

`29`

`memset(&connection_callbacks, 0, sizeof(connection_callbacks));`

`30`

`connection_callbacks.on_notify = CallbackConnectionNotify;`

`31`

`32`

`...`

`33`

`34`

`if (kSpErrorOk != (err = SpInit(&conf)))`

`35`

`LOG("Error %d\n", err);`

`36`

`return 0;`

`37`

`}`

`38`

`39`

`SpRegisterConnectionCallbacks(&connection_callbacks, NULL);`

`40`

`41`

`err = SpConnectionLoginOauthToken(YOUR_OAUTH_TOKEN);`

`42`

`if (err != kSpErrorOk) {`

`43`

`LOG("Error %d\n", err);`

`44`

`SpFree();`

`45`

`return 0;`

`46`

`}`

`47`

`48`

`while (1) {`

`49`

`err = SpPumpEvents();`

`50`

`if (kSpErrorOk != err || error_occurred) {`

`51`

`goto end;`

`52`

`}`

`53`

`54`

`if (has_logged_in) {`

`55`

`LOG("Login was successful. Logging out again.\n");`

`56`

`has_logged_in = 0;`

`57`

`SpConnectionLogout();`

`58`

`}`

`59`

`if (has_logged_out) {`

`60`

`LOG("Logged out. Exiting.\n");`

`61`

`break;`

`62`

`}`

`63`

`}`

`64`

`65`

`SpFree();`

`66`

`67`

`return 0;`

`68`

`}`

## Writing Callbacks

The application should not perform time-consuming tasks in any of the callbacks. Try to return from the callback as quickly as possible. If a time-consuming operation needs to be performed as a reaction to an event, the callback should trigger an asynchronous task.

**Note**: Only Spotify Embedded API functions that are explicitly marked as such are allowed to be invoked from callbacks.