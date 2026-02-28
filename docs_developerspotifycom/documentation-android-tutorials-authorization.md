---
title: Authorization | Spotify for Developers
url: https://developer.spotify.com/documentation/android/tutorials/authorization
source: crawler
fetched_at: 2026-02-27T23:40:47.295738-03:00
rendered_js: true
word_count: 1154
summary: This tutorial explains how to integrate and use Spotify's Android auth-lib to authenticate users and obtain authorization codes for API access. It details library installation via Gradle and provides implementation steps for both native client and web-based authentication flows.
tags:
    - spotify-sdk
    - android-development
    - authentication
    - auth-lib
    - authorization-code
    - gradle
category: tutorial
---

In this tutorial, we explain how to use Spotify's Android `auth-lib`. The Android `auth-lib` is a small library included in the Android Spotify SDK, which authenticates the user and allows apps to get an authorization code through the Spotify client. The authorization code can be exchanged for an access token as [explained here](https://developer.spotify.com/documentation/web-api/tutorials/code-flow). The access token can then be used with [Spotify's API](https://developer.spotify.com/documentation/web-api).

The `auth-lib` is independent of the `app-remote` library, which is also included in the Android Spotify SDK.

## Library installation

In Android Studio, edit the `build.gradle` file in the *app* directory (it can also be labelled as `Module: app`) and make sure it contains the dependency on the library. Check [Maven Central Repository](https://search.maven.org/search?q=g%3Acom.spotify.android) to make sure you're using the latest library version in your project.

To be able to get the library dependency, you should also add `mavenCentral()` into a repositories block. Your updated Gradle file should look something like this:

`1`

`repositories {`

`2`

`mavenCentral()`

`3`

`}`

`4`

`5`

`dependencies {`

`6`

`implementation 'com.spotify.android:auth:1.2.5' // Maven dependency`

`7`

`8`

`// All other dependencies for your app should also be here:`

`9`

`implementation 'androidx.browser:browser:1.0.0'`

`10`

`implementation "androidx.appcompat:appcompat:$appCompatVersion"`

`11`

`}`

There are two basic ways you can authorize your application to get access to the data served by Spotify APIs:

- [Using the Spotify client to authenticate the user](https://developer.spotify.com/documentation/android/tutorials/authorization#using-the-spotify-client-to-authenticate-the-user)
- [Login Through a Web Browser](https://developer.spotify.com/documentation/android/tutorials/authorization#login-through-a-web-browser)

### Using the Spotify client to authenticate the user

This is the preferred and recommended method of authentication because users don't need to enter their credentials.

- If Spotify is **installed** on the device, the `auth-lib` will connect to the Spotify client and fetch the authorization code for the current user. Since the user is already logged into Spotify, they don’t need to type in their username and password. If the application requests scopes that have not been approved before, the user will see a list of scopes and will need to accept them.
- If Spotify is **not installed** on the device, the auth-lib will fallback to the `WebView` based authorization and open the Spotify Accounts login page at [https://accounts.spotify.com](https://accounts.spotify.com) in a native `WebView`. User will have to enter their username and password to login to Spotify and accept the supplied scopes.

In both cases the result of the authorization flow will be returned in the `onActivityResult` method of the activity that initiated it.

This flow is completed within the application; there is no need to open a web browser.

#### Logging In

To login using this flow, open the `LoginActivity` from one of your activities:

`1`

`// Request code will be used to verify if result comes from the login activity. Can be set to any integer.`

`2`

`private static final int REQUEST_CODE = 1337;`

`3`

`private static final String REDIRECT_URI = "yourcustomprotocol://callback";`

`4`

`5`

`AuthorizationRequest.Builder builder =`

`6`

`new AuthorizationRequest.Builder(CLIENT_ID, AuthorizationResponse.Type.CODE, REDIRECT_URI);`

`7`

`8`

`builder.setScopes(new String[]{"streaming"});`

`9`

`AuthorizationRequest request = builder.build();`

`10`

`11`

`AuthorizationClient.openLoginActivity(this, REQUEST_CODE, request);`

To receive the authorization result, your activity needs to override the `onActivityResult` callback:

`1`

`protected void onActivityResult(int requestCode, int resultCode, Intent intent) {`

`2`

`super.onActivityResult(requestCode, resultCode, intent);`

`3`

`4`

`// Check if result comes from the correct activity`

`5`

`if (requestCode == REQUEST_CODE) {`

`6`

`AuthorizationResponse response = AuthorizationClient.getResponse(resultCode, intent);`

`7`

`8`

`switch (response.getType()) {`

`9`

`// Response was successful and contains auth token`

`10`

`case CODE:`

`11`

`// Handle successful response`

`12`

`break;`

`13`

`14`

`// Auth flow returned an error`

`15`

`case ERROR:`

`16`

`// Handle error response`

`17`

`break;`

`18`

`19`

`// Most likely auth flow was cancelled`

`20`

`default:`

`21`

`// Handle other cases`

`22`

`}`

`23`

`}`

`24`

`}`

#### Logging Out

By default, the authenticated session is persisted in the `WebView`, which allows user to log in again without re-typing in their password.

To log out and clear all stored tokens, use the `AuthorizationClient#clearCookies` method. Both Spotify and Facebook tokens will be removed.

### Login Through a Web Browser

Only if the first way is not possible.

This method opens the Spotify Accounts page in a separate, external browser window, completes the authentication process, and then redirects back to your application. This method does not involve the auth-lib.

#### Logging in

To log in using the web browser, open it from one of your activities:

`1`

`private static final String REDIRECT_URI = "yourcustomprotocol://callback";`

`2`

`3`

`AuthorizationRequest.Builder builder =`

`4`

`new AuthorizationRequest.Builder(CLIENT_ID, AuthorizationResponse.Type.CODE, REDIRECT_URI);`

`5`

`6`

`builder.setScopes(new String[]{"streaming"});`

`7`

`AuthorizationRequest request = builder.build();`

`8`

`9`

`AuthorizationClient.openLoginInBrowser(this, request);`

The activity that will receive and process the result must be configured in the `AndroidManifest.xml`:

`1`

`<activity`

`2`

`android:name=".MySpotifyAuthorizationActivity"`

`3`

`android:label="@string/app_name"`

`4`

`android:launchMode="singleInstance" >`

`5`

`6`

`// An intent filter that will receive the response`

`7`

`// from the authentication service`

`8`

`<intent-filter>`

`9`

`<action android:name="android.intent.action.VIEW"/>`

`10`

`11`

`<category android:name="android.intent.category.DEFAULT"/>`

`12`

`<category android:name="android.intent.category.BROWSABLE"/>`

`13`

`14`

`// this needs to match the scheme and host of the redirect URI as defined in My applications page`

`15`

`<data`

`16`

`android:host="callback"`

`17`

`android:scheme="yourcustomprotocol"/>`

`18`

`</intent-filter>`

`19`

`20`

`<intent-filter>`

`21`

`// Other intent filters this activity requires`

`22`

`</intent-filter>`

`23`

`</activity>`

To process the result, the receiving activity (`MySpotifyAuthorizationActivity` in this example) needs to override one of its callbacks. With launch mode set to `singleInstance` or `singleTask` the callback to use is `onNewIntent`:

`1`

`protected void onNewIntent(Intent intent) {`

`2`

`super.onNewIntent(intent);`

`3`

`4`

`Uri uri = intent.getData();`

`5`

`if (uri != null) {`

`6`

`AuthorizationResponse response = AuthorizationResponse.fromUri(uri);`

`7`

`8`

`switch (response.getType()) {`

`9`

`// Response was successful and contains auth token`

`10`

`case CODE:`

`11`

`// Handle successful response`

`12`

`break;`

`13`

`14`

`// Auth flow returned an error`

`15`

`case ERROR:`

`16`

`// Handle error response`

`17`

`break;`

`18`

`19`

`// Most likely auth flow was cancelled`

`20`

`default:`

`21`

`// Handle other cases`

`22`

`}`

It is also possible to use other launch modes for the activity that processes the authorization result. In this case it can be either `onNewIntent` or `onCreate` callback that will receive an intent containing the result. See [information about launch modes](https://developer.android.com/guide/components/tasks-and-back-stack.html#TaskLaunchModes) in Android to choose the correct mode.

Be aware of the fact that activities launched in `standard` or `singleTop` mode can have multiple instances existing at the same time. Make sure you don’t create multiple `Player` instances in your application.

![Android login screen](https://developer-assets.spotifycdn.com/images/documentation/android/oauth.png)

#### Logging out from Spotify

To log out user from Spotify in the app, they must be logged out using the same browser they used to log in. To log out, open url [https://accounts.spotify.com](https://accounts.spotify.com) in the browser. The user that is currently logged in will then be able to log out:

![Android log out screen](https://developer-assets.spotifycdn.com/images/documentation/android/androidlogout.png)

Another option to log out is to add `showDialog` parameter to the authorization request. This will force the page that lists the granted scopes and currently logged-in user giving them the chance to log out by choosing the “Not you?” link:

`1`

`private static final String REDIRECT_URI = "yourcustomprotocol://callback";`

`2`

`3`

`AuthorizationRequest.Builder builder =`

`4`

`new AuthorizationRequest.Builder(CLIENT_ID, AuthorizationResponse.Type.CODE, REDIRECT_URI);`

`5`

`6`

`builder.setScopes(new String[]{"streaming"});`

`7`

`builder.setShowDialog(true);`

`8`

`AuthorizationRequest request = builder.build();`

`9`

`10`

`AuthorizationClient.openLoginInBrowser(this, request);`