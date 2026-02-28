---
title: Getting started with Android SDK
url: https://developer.spotify.com/documentation/android/tutorials/getting-started
source: crawler
fetched_at: 2026-02-27T23:40:48.69761-03:00
rendered_js: true
word_count: 1473
summary: This tutorial provides a step-by-step guide for integrating the Spotify App Remote SDK into an Android application, covering setup, authorization, and basic playback control.
tags:
    - android-sdk
    - spotify-app-remote
    - mobile-development
    - app-authorization
    - music-playback
    - kotlin
category: tutorial
---

## Introduction

This tutorial leads you step-by-step through the creation of a simple app that uses the Spotify App Remote SDK to play a playlist. We show you how to:

- Play a playlist from a URI
- Subscribe to PlayerState of the Spotify app and read its data

If you are new to developing Android apps, we recommend reading the tutorials on Google's [Android developer portal](http://developer.android.com/develop/index.html).

## Prepare Your Environment

### Register Your App

You will need to [register your application](https://developer.spotify.com/documentation/web-api/concepts/apps) on [the Developer Dashboard](https://developer.spotify.com/dashboard) and obtain a client ID. When you register your app you will also need to whitelist a redirect URI that the Spotify Accounts Service will use to callback to your app after authorization.

You also should [add your package name and app fingerprint](https://developer.spotify.com/documentation/android/tutorials/application-fingerprints) as they're used to verify the identity of your application.

Select "Android" for the question asking which APIs are you planning to use.

### Install Spotify App

App Remote SDK requires the Spotify app to be installed on the device. Install the [latest version of Spotify](https://play.google.com/store/apps/details?id=com.spotify.music) from Google Play on the device you want to use for development. Run the Spotify app and login or sign up.

### Download the SDK

Download the Spotify Android SDK from our [GitHub](https://github.com/spotify/android-sdk/releases).

## Create Your App

Create or make sure you have an [Android app](http://developer.android.com/training/basics/firstapp/creating-project.html) with at least one Activity or Service in which you can put your code to connect to Spotify.

Edit your `MainActivity` to look like this:

`1`

`class MainActivity : AppCompatActivity() {`

`2`

`3`

`override fun onCreate(savedInstanceState: Bundle?) {`

`4`

`super.onCreate(savedInstanceState)`

`5`

`setContentView(R.layout.activity_main)`

`6`

`}`

`7`

`8`

`override fun onStart() {`

`9`

`super.onStart()`

`10`

`// We will start writing our code here.`

`11`

`}`

`12`

`13`

`private fun connected() {`

`14`

`// Then we will write some more code here.`

`15`

`}`

`16`

`17`

`override fun onStop() {`

`18`

`super.onStop()`

`19`

`// Aaand we will finish off here.`

`20`

`}`

`21`

`}`

### Add the App Remote SDK

Unzip the App Remote SDK zip file that you downloaded. Add the library to your project by importing it as a module. In the *Project* side bar in Android Studio (View &gt; Tool Windows &gt; Project), right click your project's root folder and navigate to *New* &gt; *Module*.

![New module GUI](https://developer-assets.spotifycdn.com/images/documentation/android/new-module.png)

In the *New Module* window, choose the option *Import .JAR/AAR Package*. Click *Next*.

![Import Jar GUI](https://developer-assets.spotifycdn.com/images/documentation/android/import-jar.png)

Press the "..." button and locate the `spotify-app-remote-release-version.aar` under the *app-remote-lib* folder in the unzipped bundle. Click *Open* and choose a suitable subproject name. We're using spotify-app-remote in this example. Click *Finish* to import the .aar into your project.

![Create new module GUI](https://developer-assets.spotifycdn.com/images/documentation/android/create-new-module.png)

Add a dependency on the spotify-app-remote module to your app by adding the imported subproject and Gson to your app's build.gradle file. It is important that the name that you specify in the build.gradle file is the same as the subproject name you decided on.

`1`

`dependencies {`

`2`

`// your app dependencies`

`3`

`implementation project(':spotify-app-remote')`

`4`

`implementation "com.google.code.gson:gson:2.6.1"`

`5`

`}`

Since version 0.2.0 of the App Remote SDK, [Gson](https://github.com/google/gson) is used by default for serializing and deserializing the request. [Jackson](https://github.com/FasterXML/jackson) is also supported. If you would like to use Jackson instead please see the FAQ [here](https://developer.spotify.com/documentation/android#can-i-use-jackson-instead-of-gson).

### Import Dependencies

`1`

`import com.spotify.android.appremote.api.ConnectionParams;`

`2`

`import com.spotify.android.appremote.api.Connector;`

`3`

`import com.spotify.android.appremote.api.SpotifyAppRemote;`

`4`

`5`

`import com.spotify.protocol.client.Subscription;`

`6`

`import com.spotify.protocol.types.PlayerState;`

`7`

`import com.spotify.protocol.types.Track;`

### Set up your Spotify credentials

`1`

`private val clientId = "your_client_id"`

`2`

`private val redirectUri = "http://com.yourdomain.yourapp/callback"`

`3`

`private var spotifyAppRemote: SpotifyAppRemote? = null`

To be able to use the App Remote SDK the user needs to authorize your application. If they haven't, the connection will fail with `UserNotAuthorizedException`. To allow the user to authorize your app, you will use the built-in authorization described below.

### Authorizing the user using the built-in auth flow

For this use-case, you don't have to add [the Authorization Library](https://developer.spotify.com/documentation/android/tutorials/authorization) to your application. You can request that the authorization view is shown to users who have not approved the `app-remote-control` scope by passing the flag `showAuthView` in the `ConnectionParams`. The scope is automatically requested for you by the library.

Add the following to your `onStart` method:

`1`

`// Set the connection parameters`

`2`

`val connectionParams = ConnectionParams.Builder(clientId)`

`3`

`.setRedirectUri(redirectUri)`

`4`

`.showAuthView(true)`

`5`

`.build()`

Built-in auth provides offline support. This means that a user can be authorized even if the device is currently offline. Offline support works out of the box, so it doesn't require any additional implementation.

To successfully authorize a user while offline, the following conditions have to be met:

- Your application has successfully connected to Spotify within the last 24 hours
- Your application uses the same redirect URI, client ID and scopes when connecting to Spotify

### Authorizing user with Single Sign-On library

Download and add Authorization Library to your project as described in [this guide](https://developer.spotify.com/documentation/android/quick-start#install-the-spotify-android-sdk).

Create and send the authorization request as described in the [Android SDK Authorization Guide](https://developer.spotify.com/documentation/android/tutorials/authorization). You need the `app-remote-control` scope to use the Spotify App Remote SDK.

## Connect to App Remote

The first thing we need to do is to use the `SpotifyAppRemote.Connector` to connect to Spotify and get an instance of `SpotifyAppRemote`. To do this, we call the `connect` method using the `connectionParams` we defined above. Add the following to your `onStart` method.

`1`

`SpotifyAppRemote.connect(this, connectionParams, object : Connector.ConnectionListener {`

`2`

`override fun onConnected(appRemote: SpotifyAppRemote) {`

`3`

`spotifyAppRemote = appRemote`

`4`

`Log.d("MainActivity", "Connected! Yay!")`

`5`

`// Now you can start interacting with App Remote`

`6`

`connected()`

`7`

`}`

`8`

`9`

`override fun onFailure(throwable: Throwable) {`

`10`

`Log.e("MainActivity", throwable.message, throwable)`

`11`

`// Something went wrong when attempting to connect! Handle errors here`

`12`

`}`

`13`

`})`

### Play a Playlist

To play a playlist given a Spotify playlist URI, we are going to connect to the Spotify app and use the `PlayerApi` command. From there we can get the `PlayerApi` directly and call play. Add the following to your private `connected` method:

`1`

`// Play a playlist`

`2`

`spotifyAppRemote.playerApi.play("spotify:playlist:37i9dQZF1DX2sUQwD7tbmL")`

Run the application and you should hear some feel-good indie tunes playing on your phone. If you prefer something more relaxing, why not try some sweet piano music `spotify:playlist:37i9dQZF1DX7K31D69s4M1`. If you don't hear music playing and end up in the `onFailure` callback above, please read up on [connection errors](https://github.com/spotify/android-sdk/blob/master/app-remote-lib/ERRORS.md) and try again.

### Subscribe to PlayerState

The `PlayerApi` offers, in addition to the `play(uri)` method we use above, the ability to subscribe to and poll for the state of the Spotify player. Add the following to your code to subscribe to `PlayerState` and log the track title and artist of the song that will be playing:

`1`

`// Subscribe to PlayerState`

`2`

`spotifyAppRemote.playerApi.subscribeToPlayerState().setEventCallback {`

`3`

`val track: Track = it.track`

`4`

`Log.d("MainActivity", track.name + " by " + track.artist.name)`

`5`

`}`

Run the app again. You should now see a log with the track name and artist of the currently playing track.

### Disconnecting from App Remote

Don't forget to disconnect from App Remote when you no longer need it. Add the following to your `onStop` method.

`1`

`override fun onStop() {`

`2`

`super.onStop()`

`3`

`spotifyAppRemote?.let {`

`4`

`SpotifyAppRemote.disconnect(it)`

`5`

`}`

`6`

`7`

`}`

## Next Steps

**Congratulations!** You've interacted with the App Remote SDK for the first time. Time to celebrate, you did a great job! 👏

Want more? Here's what you can do next:

- Learn about best practices for handling App Remote SDK [interactions](https://developer.spotify.com/documentation/android/tutorials/making-remote-calls) and [connections](https://developer.spotify.com/documentation/android/tutorials/application-lifecycle) in your Android application.
- Dive into other things you can do with the SDK in the [App Remote SDK Reference](https://spotify.github.io/android-sdk/app-remote-lib/docs/index.html).

## Source Code

The Quick Start source code is below. Copy into your Main Activity.

`1`

`package com.yourdomain.yourapp;`

`2`

`3`

`import android.os.Bundle;`

`4`

`import android.support.v7.app.AppCompatActivity;`

`5`

`6`

`import android.util.Log;`

`7`

`8`

`import com.spotify.android.appremote.api.ConnectionParams;`

`9`

`import com.spotify.android.appremote.api.Connector;`

`10`

`import com.spotify.android.appremote.api.SpotifyAppRemote;`

`11`

`12`

`import com.spotify.protocol.client.Subscription;`

`13`

`import com.spotify.protocol.types.PlayerState;`

`14`

`import com.spotify.protocol.types.Track;`

`15`

`16`

`class MainActivity : AppCompatActivity() {`

`17`

`18`

`private val clientId = "ad0911afa57949bba362003f601876b2"`

`19`

`private val redirectUri = "https://com.spotify.android.spotifysdkkotlindemo/callback"`

`20`

`private var spotifyAppRemote: SpotifyAppRemote? = null`

`21`

`22`

`override fun onCreate(savedInstanceState: Bundle?) {`

`23`

`super.onCreate(savedInstanceState)`

`24`

`setContentView(R.layout.activity_main)`

`25`

`}`

`26`

`27`

`override fun onStart() {`

`28`

`super.onStart()`

`29`

`val connectionParams = ConnectionParams.Builder(clientId)`

`30`

`.setRedirectUri(redirectUri)`

`31`

`.showAuthView(true)`

`32`

`.build()`

`33`

`34`

`SpotifyAppRemote.connect(this, connectionParams, object : Connector.ConnectionListener {`

`35`

`override fun onConnected(appRemote: SpotifyAppRemote) {`

`36`

`spotifyAppRemote = appRemote`

`37`

`Log.d("MainActivity", "Connected! Yay!")`

`38`

`// Now you can start interacting with App Remote`

`39`

`connected()`

`40`

`}`

`41`

`42`

`override fun onFailure(throwable: Throwable) {`

`43`

`Log.e("MainActivity", throwable.message, throwable)`

`44`

`// Something went wrong when attempting to connect! Handle errors here`

`45`

`}`

`46`

`})`

`47`

`}`

`48`

`49`

`private fun connected() {`

`50`

`spotifyAppRemote?.let {`

`51`

`// Play a playlist`

`52`

`val playlistURI = "spotify:playlist:37i9dQZF1DX2sUQwD7tbmL"`

`53`

`it.playerApi.play(playlistURI)`

`54`

`// Subscribe to PlayerState`

`55`

`it.playerApi.subscribeToPlayerState().setEventCallback {`

`56`

`val track: Track = it.track`

`57`

`Log.d("MainActivity", track.name + " by " + track.artist.name)`

`58`

`}`

`59`

`}`

`60`

`61`

`}`

`62`

`63`

`override fun onStop() {`

`64`

`super.onStop()`

`65`

`spotifyAppRemote?.let {`

`66`

`SpotifyAppRemote.disconnect(it)`

`67`

`}`

`68`

`69`

`}`

`70`

`}`