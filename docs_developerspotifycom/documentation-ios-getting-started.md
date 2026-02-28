---
title: Getting Started with iOS SDK
url: https://developer.spotify.com/documentation/ios/getting-started
source: crawler
fetched_at: 2026-02-27T23:40:17.515948-03:00
rendered_js: true
word_count: 1540
summary: This guide provides step-by-step instructions for integrating the Spotify iOS SDK into an Xcode project to enable user authentication, music playback control, and real-time player updates.
tags:
    - spotify-sdk
    - ios-development
    - xcode
    - authentication
    - music-playback
    - mobile-development
category: guide
---

Welcome! In this Getting Started guide, we will go through how to use the Spotify iOS SDK in your existing Xcode application to integrate:

- Authentication (via the Spotify Accounts API)
- Shuffle playback for Spotify Free users
- On-demand playback for Spotify Premium users
- Real-time player state updates

You can read more about the iOS SDK in the [overview](https://developer.spotify.com/documentation/ios), or dig into the [reference documentation](https://spotify.github.io/ios-sdk/html).

## Prepare Your Environment

### Register a Developer App

Go to the [Developer Dashboard](https://developer.spotify.com/dashboard) and create an app with the following configuration values:

- Redirect URI: Set this to `spotify-ios-quick-start://spotify-login-callback`. We'll use this to send users back to your application
- Bundle ID: This is your iOS app bundle identifier, in a format similar to `com.spotify.iOS-SDK-Quick-Start`.
- Which API/SDKs are you planning to use: iOS

### Install the Spotify App

Install the [latest version of Spotify](https://itunes.apple.com/us/app/spotify-music/id324684580?mt=8) from the Apple App Store on the device you wish to use for this tutorial. Run the Spotify app and be sure to login or register to Spotify on your device.

### Download the iOS SDK

Download the latest version of Spotify's iOS SDK from [our GitHub repository](https://github.com/spotify/ios-sdk/releases). You'll need to add the `SpotifyiOS.framework` file as a dependency in your iOS project for the next section.

## Set up the iOS SDK

At this point, we should have the following:

- A registered Client ID
- A downloaded copy of the Spotify iOS SDK
- The latest version of the Spotify app installed on an iOS device

Next we'll focus on installing the SDK inside of an existing Xcode application.

### Import `SpotifyiOS.framework`

You'll need to import the `SpotifyiOS.framework`. You can simply drag it into your Xcode project.

### Configure `Info.plist`

We'll need to configure our `Info.plist` to support the iOS SDK. There are two things we need to add:

##### 1. Add `spotify` to `LSApplicationQueriesSchemes`

We'll need this to check if the Spotify main application is installed. The `LSApplicationQueriesSchemes` key in `Info.plist` allows your application to perform this check. To set this up, add this to your `Info.plist`:

`1`

`<key>LSApplicationQueriesSchemes</key>`

`2`

`<array>`

`3`

`<string>spotify</string>`

`4`

`</array>`

##### 2. Add a URI Scheme in `CFBundleURLTypes`

In order for Spotify to send users back to your application, we need to set up [a URI scheme](https://developer.apple.com/library/content/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html#/apple_ref/doc/uid/TP40007072-CH6-SW1) in our `Info.plist`. To do this, we'll need our Bundle ID and Redirect URI from earlier. From the Redirect URI, we just need the protocol (which for `spotify-ios-quick-start://spotify-login-callback` would be `spotify-ios-quick-start`).

We'll then need to put our Bundle ID in `CFBundleURLName` and our Redirect URI protocol in `CFBundleURLSchemes`:

`1`

`<key>CFBundleURLTypes</key>`

`2`

`<array>`

`3`

`<dict>`

`4`

`<key>CFBundleURLName</key>`

`5`

`<string>com.spotify.iOS-SDK-Quick-Start</string>`

`6`

`<key>CFBundleURLSchemes</key>`

`7`

`<array>`

`8`

`<string>spotify-ios-quick-start</string>`

`9`

`</array>`

`10`

`</dict>`

`11`

`</array>`

### Set `-ObjC` Linker Flag

In order to support the iOS SDK, we will need to add the `-ObjC` linker flag. This allows us to compile the Objective-C code that is contained within the iOS SDK.

In XCode, to add the linker flag, we need to do the following:

- In the File Navigator, click on your project.
- Click your project under `Targets`
- Go to `Build Settings`
- In the search box, enter `Other Linker Flags`
- Besides `Other Linker Flags`, double click and enter `-ObjC`

In the last step, we added the linker flag to compile Objective-C code. Next, we need to add a bridging header, which will allow us to include Objective-C binaries inside of our Swift app.

Typically, this is named with the `[YourApp]-Bridging-Header.h` convention. Xcode may generate this for you, otherwise you will need to create this in the root directory of your project.

In your newly created file, you'll need to replace it with the following contents:

`1`

`#import <SpotifyiOS/SpotifyiOS.h>`

Then you'll need to set the location of this bridging header by:

- In the File Navigator, click on your project.
- Click your project under `Targets`
- Go to `Build Settings`
- In the search box, enter `Objective-C Bridging Header`
- Besides `Objective-C Bridging Header`, double click and enter `[YourApp]-Bridging-Header.h`

In order for the iOS SDK to control the Spotify app, they will need to authorize your app.

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

#### Configure Auth Callback

Once a user successfully returns to your application, we'll need to the assign the access token to the `appRemote` connection parameters

`1`

`func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {`

`2`

`let parameters = appRemote.authorizationParameters(from: url);`

`3`

`4`

`if let access_token = parameters?[SPTAppRemoteAccessTokenKey] {`

`5`

`appRemote.connectionParameters.accessToken = access_token`

`6`

`self.accessToken = access_token`

`7`

`} else if let error_description = parameters?[SPTAppRemoteErrorDescriptionKey] {`

`8`

`// Show the error`

`9`

`}`

`10`

`return true`

`11`

`}`

If you are using UIScene then you need to use appropriate method in your scene delegate.

`1`

`func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {`

`2`

`guard let url = URLContexts.first?.url else {`

`3`

`return`

`4`

`}`

`5`

`6`

`let parameters = appRemote.authorizationParameters(from: url);`

`7`

`8`

`if let access_token = parameters?[SPTAppRemoteAccessTokenKey] {`

`9`

`appRemote.connectionParameters.accessToken = access_token`

`10`

`self.accessToken = access_token`

`11`

`} else if let error_description = parameters?[SPTAppRemoteErrorDescriptionKey] {`

`12`

`// Show the error`

`13`

`}`

`14`

`}`

User authorization provides offline support. This means that a user can be authorized even if the device is currently offline. Offline support works out of the box, so it doesn't require any additional implementation.

To successfully authorize a user while offline, the following conditions have to be met:

- Your application has successfully connected to Spotify within the last 24 hours
- Your application uses the same redirect URI, client ID and scopes when connecting to Spotify

## Set up App Remote

With authentication implemented, we can now control the Spotify main application to play music and notify us on playback state:

#### Implement Remote Delegates

We'll need to implement two delegates: `SPTAppRemoteDelegate` and `SPTAppRemotePlayerStateDelegate`. These will respectively provide connection and playback state methods to implement inside of our `AppDelegate.swift`:

`1`

`class AppDelegate: UIResponder, UIApplicationDelegate, SPTAppRemoteDelegate, SPTAppRemotePlayerStateDelegate {`

`2`

`...`

or if you are using UIScene:

`1`

`class SceneDelegate: UIResponder, UIWindowSceneDelegate, SPTAppRemoteDelegate, SPTAppRemotePlayerStateDelegate`

`2`

`...`

These will require us to implement the following methods:

`1`

`func appRemoteDidEstablishConnection(_ appRemote: SPTAppRemote) {`

`2`

`print("connected")`

`3`

`}`

`4`

`func appRemote(_ appRemote: SPTAppRemote, didDisconnectWithError error: Error?) {`

`5`

`print("disconnected")`

`6`

`}`

`7`

`func appRemote(_ appRemote: SPTAppRemote, didFailConnectionAttemptWithError error: Error?) {`

`8`

`print("failed")`

`9`

`}`

`10`

`func playerStateDidChange(_ playerState: SPTAppRemotePlayerState) {`

`11`

`print("player state changed")`

`12`

`}`

#### Initialize App Remote

We'll need to initialize App Remote on a class-level closure, which can take the `self.configuration` we defined earlier:

`1`

`lazy var appRemote: SPTAppRemote = {`

`2`

`let appRemote = SPTAppRemote(configuration: self.configuration, logLevel: .debug)`

`3`

`appRemote.connectionParameters.accessToken = self.accessToken`

`4`

`appRemote.delegate = self`

`5`

`return appRemote`

`6`

`}()`

#### Configure Initial Music

iOS requires us to define a `playURI` (as shown in the last step) in order to play music to wake up the Spotify main application. This is an iOS-specific requirement. This can be:

**An empty value:** If empty, it will resume playback of user's last track or play a random track. If offline, one of the downloaded for offline tracks will play. Example:

**A valid Spotify URI:** Otherwise, provide a Spotify URI. Example:

`1`

`self.playURI = "spotify:track:20I6sIOMTCkB6w7ryavxtO"`

#### Authorizing and Connecting to Spotify

We need to initiate authorization and connect to Spotify:

`1`

`func connect()) {`

`2`

`self.appRemote.authorizeAndPlayURI(self.playURI)`

`3`

`}`

Upon a successful connection, this will invoke the `appRemoteDidEstablishConnection(_ appRemote: SPTAppRemote)` method we defined earlier.

#### Subscribing to state changes

We'll need to invoke a request to subscribe to player state updates, which we can do in the `appRemoteDidEstablishConnection` method:

`1`

`func appRemoteDidEstablishConnection(_ appRemote: SPTAppRemote) {`

`2`

`// Connection was successful, you can begin issuing commands`

`3`

`self.appRemote.playerAPI?.delegate = self`

`4`

`self.appRemote.playerAPI?.subscribe(toPlayerState: { (result, error) in`

`5`

`if let error = error {`

`6`

`debugPrint(error.localizedDescription)`

`7`

`}`

`8`

`})`

`9`

`}`

Inside `playerStateDidChange`, we can begin logging the output:

`1`

`func playerStateDidChange(_ playerState: SPTAppRemotePlayerState) {`

`2`

`debugPrint("Track name: %@", playerState.track.name)`

`3`

`}`

#### Cleaning up

When the user switches from our application we should disconnect from App Remote. We can do this by inserting the following code into our `applicationWillResignActive` method:

`1`

`func applicationWillResignActive(_ application: UIApplication) {`

`2`

`if self.appRemote.isConnected {`

`3`

`self.appRemote.disconnect()`

`4`

`}`

`5`

`}`

And similarly when a user re-opens our application, we should re-connect to App Remote. We can do by inserting the following code into our `applicationDidBecomeActive` method:

`1`

`func applicationDidBecomeActive(_ application: UIApplication) {`

`2`

`if let _ = self.appRemote.connectionParameters.accessToken {`

`3`

`self.appRemote.connect()`

`4`

`}`

`5`

`}`

Or if you are using UIScene:

`1`

`func sceneDidBecomeActive(_ scene: UIScene) {`

`2`

`if let _ = self.appRemote.connectionParameters.accessToken {`

`3`

`self.appRemote.connect()`

`4`

`}`

`5`

`}`

`6`

`7`

`func sceneWillResignActive(_ scene: UIScene) {`

`8`

`if self.appRemote.isConnected {`

`9`

`self.appRemote.disconnect()`

`10`

`}`

`11`

`}`

Having issues? Take a look at a [full example of `AppDelegate.swift`](https://gist.github.com/bih/38aadb1e618623589d54902e016d32eb). Or check out the [SceneDelegate example](https://gist.github.com/kkarayannis/65f8927ecc6444515c6525db72c7544a).

## Next Steps

**Congratulations!** You've interacted with the Spotify iOS SDK for the first time. Time to celebrate, you did great! 👏

Want more? Here's what you can do next:

- Learn about how our iOS SDK interacts with iOS in our [application lifecycle guide](https://developer.spotify.com/documentation/ios/concepts/application-lifecycle).
- Dive into other things you can do with the SDK in the [reference documentation](https://spotify.github.io/ios-sdk/html).
- Be sure to check out the sample code in the **Demo Projects** folder included with the SDK.