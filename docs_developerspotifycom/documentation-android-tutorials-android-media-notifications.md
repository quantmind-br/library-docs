---
title: Android Media Notifications | Spotify for Developers
url: https://developer.spotify.com/documentation/android/tutorials/android-media-notifications
source: crawler
fetched_at: 2026-02-27T23:42:00.919761-03:00
rendered_js: true
word_count: 672
summary: This document explains how Android applications can subscribe to broadcast notifications from the Spotify app to receive updates on track metadata, playback states, and queue changes.
tags:
    - android-development
    - spotify-api
    - broadcast-receiver
    - playback-state
    - metadata-changes
    - intent-actions
category: guide
---

If you are developing an Android application and want to know what is happening in the Spotify app, you can subscribe to broadcast notifications from it.

The Spotify app can posts sticky media [broadcast notifications](http://developer.android.com/reference/android/content/BroadcastReceiver.html) that can be read by any app on the same Android device. The media notifications contain information about what is currently being played in the Spotify App, as well as the playback position and the playback status of the app.

## Enabling Media Notifications

The media notifications feature of the Spotify app may be disabled by the user for potential privacy concerns. For new or upgrading users of the Spotify app, this feature is disabled unless the user has enabled Facebook scrobbling.

It is not possible for your app to programmatically configure Spotify to enable broadcasting. If your app does not find any broadcast messages, consider showing the user a message asking them to enable this feature by turning **Device Broadcast Status** to `ON` in the Spotify app’s settings.

## Event Types

The following type of events are sent with these respective intent extras:

- A metadata change intent is sent when a new track starts playing. It uses the intent action `com.spotify.music.metadatachanged`, and contains the following intent extras:

Intent ExtraTypeDescriptionidStringA Spotify URI for the trackartistStringThe track artistalbumStringThe album nametrackStringThe track namelengthIntegerLength of the track, in seconds

- A playback state change is sent whenever the user presses play/pause, or when seeking the track position. It uses the intent action `com.spotify.music.playbackstatechanged` and contains the following intent extras:

Intent ExtraTypeDescriptionplayingBooleanTrue if playing, false if pausedplaybackPositionIntegerThe current playback position in milliseconds

- A queue change is sent whenever the play queue is changed. It uses the intent action `com.spotify.music.queuechanged` and does not contain any additional intent extras.

In addition to the respective intent extras noted above, all broadcasts sent by Spotify contain an additional extra named `timeSent` (Long), which is the value of `system.currentTimeMillis()` at the time the broadcast was posted to the system. Since broadcasts can take a bit of time to propagate to your app’s `BroadcastReceiver`, this can be used to synchronize your app more precisely with the Spotify app. Also it is possible that the last value posted by Spotify is quite old, your app should account for this case if necessary.

## Example

This example code shows how to read media notifications. For it to work, the app must first create a *broadcast receiver* which can be done in the `AndroidManifest.xml` file:

`1`

`<receiver`

`2`

`android:name="MyBroadcastReceiver"`

`3`

`android:enabled="true"`

`4`

`android:exported="true">`

`5`

`6`

`<intent-filter>`

`7`

`<action android:name="com.spotify.music.playbackstatechanged"/>`

`8`

`<action android:name="com.spotify.music.metadatachanged"/>`

`9`

`<action android:name="com.spotify.music.queuechanged"/>`

`10`

`</intent-filter>`

`11`

`12`

`</receiver>`

You can also register the broadcast receiver from in your `Activity` or `Fragment` (for more information about this, see the official Android documentation for [BroadcastReceiver](http://developer.android.com/reference/android/content/BroadcastReceiver.html). Once the receiver has been registered, broadcasts will be sent to the class:

`1`

`import android.content.BroadcastReceiver;`

`2`

`import android.content.Context;`

`3`

`import android.content.Intent;`

`4`

`5`

`public class MyBroadcastReceiver extends BroadcastReceiver {`

`6`

`static final class BroadcastTypes {`

`7`

`static final String SPOTIFY_PACKAGE = "com.spotify.music";`

`8`

`static final String PLAYBACK_STATE_CHANGED = SPOTIFY_PACKAGE + ".playbackstatechanged";`

`9`

`static final String QUEUE_CHANGED = SPOTIFY_PACKAGE + ".queuechanged";`

`10`

`static final String METADATA_CHANGED = SPOTIFY_PACKAGE + ".metadatachanged";`

`11`

`}`

`12`

`13`

`@Override`

`14`

`public void onReceive(Context context, Intent intent) {`

`15`

`// This is sent with all broadcasts, regardless of type. The value is taken from`

`16`

`// System.currentTimeMillis(), which you can compare to in order to determine how`

`17`

`// old the event is.`

`18`

`long timeSentInMs = intent.getLongExtra("timeSent", 0L);`

`19`

`20`

`String action = intent.getAction();`

`21`

`22`

`if (action.equals(BroadcastTypes.METADATA_CHANGED)) {`

`23`

`String trackId = intent.getStringExtra("id");`

`24`

`String artistName = intent.getStringExtra("artist");`

`25`

`String albumName = intent.getStringExtra("album");`

`26`

`String trackName = intent.getStringExtra("track");`

`27`

`int trackLengthInSec = intent.getIntExtra("length", 0);`

`28`

`// Do something with extracted information...`

`29`

`} else if (action.equals(BroadcastTypes.PLAYBACK_STATE_CHANGED)) {`

`30`

`boolean playing = intent.getBooleanExtra("playing", false);`

`31`

`int positionInMs = intent.getIntExtra("playbackPosition", 0);`

`32`

`// Do something with extracted information`

`33`

`} else if (action.equals(BroadcastTypes.QUEUE_CHANGED)) {`

`34`

`// Sent only as a notification, your app may want to respond accordingly.`

`35`

`}`

`36`

`}`

`37`

`}`