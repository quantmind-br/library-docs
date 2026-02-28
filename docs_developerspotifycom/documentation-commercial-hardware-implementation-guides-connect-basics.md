---
title: Spotify Connect Basics | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/connect-basics
source: crawler
fetched_at: 2026-02-27T23:41:23.503516-03:00
rendered_js: true
word_count: 2400
summary: This document explains how to integrate Spotify Connect into hardware devices using the Spotify Embedded SDK, focusing on handling playback events, synchronizing volume, and displaying track metadata.
tags:
    - spotify-connect
    - embedded-sdk
    - hardware-integration
    - playback-control
    - volume-management
    - metadata-handling
    - iot-development
category: guide
---

Spotify Connect allows users to control hardware devices from the Spotify mobile app. For example, by selecting a wireless speaker in the Connect menu of the Spotify mobile app, playback will be transferred from the phone to the wireless speaker. The phone continues to work as a remote control, so the user can pause playback, skip tracks, or change the volume on the speaker by using the Spotify mobile app.

The application that runs on the wireless speaker receives notifications through the callbacks defined in the Spotify Embedded SDK. In these callbacks, the application updates the speaker's UI (if any) and plays the audio data that it receives.

For example, when the user transfers playback to the speaker, one of the callbacks that is invoked is [SpCallbackPlaybackNotify()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spcallbackplaybacknotify) with the event [kSpPlaybackNotifyBecameActive](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#kspplaybacknotifybecameactive). When the user pauses playback using the Spotify mobile app, the application receives the event [kSpPlaybackNotifyPause](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification).

**Note**: In order to test Connect, log in to the Spotify mobile app while on the same WiFi as your Spotify Embedded application. Alternatively, if you don't have ZeroConf working, log in with the same user account on your Spotify Embedded application. When you tap the "Devices available" button in the mobile app or the speaker icon in the desktop app, the Spotify Embedded application appears in the list of available speakers under the name that you specified in [SpConfig::display\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig).

## Reacting To Volume Changes

The application is responsible for applying the desired volume level to the audio data that is delivered in the audio data callback.

Whenever the user changes the playback volume of the speaker using Spotify Connect, the callback [SpCallbackPlaybackApplyVolume()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spcallbackplaybackapplyvolume) is invoked. The application can then either set the volume level in the audio driver or apply the volume to the samples when decoding them from the data that eSDK delivers.

In addition, the application is expected to inform the library if the output volume changes without having received a volume change event through Connect. For example, the speaker might have a volume knob that changes the master volume of the device. When this happens, the application should call the function [SpPlaybackUpdateVolume()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybackupdatevolume) so that Connect-enabled remote control apps can update the volume of the speaker in their UIs.

**Note**: When the library is initialized, it assumes a volume level of 65535 (maximum volume). The application must invoke [SpPlaybackUpdateVolume()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybackupdatevolume) at some point after calling [SpInit()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spinit) to inform the library of the actual volume level of the device's audio output.

The following example shows how to do this:

`1`

`...`

`2`

`3`

`void CallbackPlaybackApplyVolume(uint16_t volume, uint8_t remote, void *context) {`

`4`

`LOG("Playback status: volume now %u\n", volume);`

`5`

`audio_callbacks.audio_volume(volume);`

`6`

`}`

`7`

`8`

`int main(int argc, char *argv[]) {`

`9`

`...`

`10`

`SpPlaybackCallbacks playback_cb;`

`11`

`...`

`12`

`13`

`memset(&playback_cb, 0, sizeof(playback_cb));`

`14`

`playback_cb.on_audio_data = audio_callbacks.audio_data;`

`15`

`playback_cb.on_apply_volume = CallbackPlaybackApplyVolume;`

`16`

`SpRegisterPlaybackCallbacks(&playback_callbacks, NULL);`

`17`

`18`

`while (error_occurred == kSpErrorOk) {`

`19`

`SpPumpEvents();`

`20`

`21`

`/* Get the volume level of the audio driver using an application-defined`

`22`

`function. If it doesn't match the volume level that was last reported`

`23`

`to the library, report the new volume.`

`24`

`*/`

`25`

`if (SoundGetOutputVolume() != SpPlaybackGetVolume())`

`26`

`SpPlaybackUpdateVolume(SoundGetOutputVolume());`

`27`

`}`

`28`

`29`

`return 0;`

`30`

`}`

## Displaying Track Metadata

If the device has a UI, it should display information about the currently playing track, such as the track name and artist name, the length of the track, and the current playback position within the track.

It will also want to display the playback status ("playing" or "paused") and whether "shuffle" and "repeat" are enabled.

The Embedded SDK invokes callbacks when any of this information changes. Here is an example that shows how to use two of them, [SpCallbackPlaybackNotify()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spcallbackplaybacknotify) and [SpCallbackPlaybackSeek()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spcallbackplaybackseek):

`1`

`static struct SpMetadata current_metadata[3];`

`2`

`...`

`3`

`4`

`static void CallbackPlaybackNotify(enum SpPlaybackNotification event,`

`5`

`void *context)`

`6`

`{`

`7`

`SpError err;`

`8`

`switch (event) {`

`9`

`case kSpPlaybackNotifyPlay:`

`10`

`LOG("Playback status: playing\n");`

`11`

`if (active && !playing)`

`12`

`audio_callbacks.audio_pause(0);`

`13`

`playing = 1;`

`14`

`break;`

`15`

`case kSpPlaybackNotifyPause:`

`16`

`LOG("Playback status: paused\n");`

`17`

`if (active && playing)`

`18`

`audio_callbacks.audio_pause(1);`

`19`

`playing = 0;`

`20`

`break;`

`21`

`case kSpPlaybackNotifyTrackChanged:`

`22`

`memset(&current_metadata, 0, sizeof(current_metadata));`

`23`

`SpGetMetadata(&current_metadata[0], kSpMetadataTrackPrevious);`

`24`

`SpGetMetadata(&current_metadata[2], kSpMetadataTrackNext);`

`25`

`err = SpGetMetadata(&current_metadata[1], kSpMetadataTrackCurrent);`

`26`

`if (err == kSpErrorOk) {`

`27`

`LOG("Track event: playing %s -- %s\n",`

`28`

`current_metadata[1].artist, current_metadata[1].track);`

`29`

`LOG(" prev: %s, next: %s\n",`

`30`

`current_metadata[0].track[0] ? current_metadata[0].track : "N/A",`

`31`

`current_metadata[2].track[0] ? current_metadata[2].track : "N/A");`

`32`

`} else {`

`33`

`LOG("Track event: start of unknown track\n");`

`34`

`}`

`35`

`break;`

`36`

`case kSpPlaybackNotifyMetadataChanged: {`

`37`

`struct SpMetadata new_metadata[3];`

`38`

`SpGetMetadata(&new_metadata[0], kSpMetadataTrackPrevious);`

`39`

`SpGetMetadata(&new_metadata[2], kSpMetadataTrackNext);`

`40`

`err = SpGetMetadata(&new_metadata[1], kSpMetadataTrackCurrent);`

`41`

`if (memcmp(current_metadata, new_metadata, sizeof(current_metadata))) {`

`42`

`memcpy(current_metadata, new_metadata, sizeof(current_metadata));`

`43`

`LOG("Metadata changed: playing %s -- %s\n",`

`44`

`current_metadata[1].artist, current_metadata[1].track);`

`45`

`LOG(" prev: %s, next: %s\n",`

`46`

`current_metadata[0].track[0] ? current_metadata[0].track : "N/A",`

`47`

`current_metadata[2].track[0] ? current_metadata[2].track : "N/A");`

`48`

`} else {`

`49`

`LOG("Metadata change: Nothing to update\n");`

`50`

`}`

`51`

`break;`

`52`

`}`

`53`

`case kSpPlaybackNotifyShuffleOn:`

`54`

`LOG("Shuffle status: 1\n");`

`55`

`break;`

`56`

`case kSpPlaybackNotifyShuffleOff:`

`57`

`LOG("Shuffle status: 0\n");`

`58`

`break;`

`59`

`case kSpPlaybackNotifyRepeatOn:`

`60`

`LOG("Repeat status: 1\n");`

`61`

`break;`

`62`

`case kSpPlaybackNotifyRepeatOff:`

`63`

`LOG("Repeat status: 0\n");`

`64`

`break;`

`65`

`...`

`66`

`67`

`default:`

`68`

`break;`

`69`

`}`

`70`

`}`

`71`

`72`

`static void CallbackPlaybackSeek(uint32_t position_ms, void *context)`

`73`

`{`

`74`

`LOG("Playback status: seeked to %u\n", position_ms);`

`75`

`}`

`76`

`77`

`int main(int argc, char *argv[]) {`

`78`

`...`

`79`

`struct SpPlaybackCallbacks playback_cb;`

`80`

`...`

`81`

`82`

`memset(&playback_callbacks, 0, sizeof(playback_callbacks));`

`83`

`playback_callbacks.on_notify = CallbackPlaybackNotify;`

`84`

`playback_callbacks.on_audio_data = audio_callbacks.audio_data;`

`85`

`playback_callbacks.on_seek = CallbackPlaybackSeek;`

`86`

`playback_callbacks.on_apply_volume = CallbackPlaybackApplyVolume;`

`87`

`88`

`...`

`89`

`SpRegisterPlaybackCallbacks(&playback_callbacks, NULL);`

`90`

`...`

`91`

`92`

`return 0;`

`93`

`}`

In addition to these callbacks, the library contains functions to retrieve the current status of playback. Using these functions, the previous example can be rewritten without callbacks as follows.

**Notes**

- The notifications [kSpPlaybackNotifyNext](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification) and [kSpPlaybackNotifyPrev](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification) cannot be replaced.
- These functions reflect the state of the playback among all Connect-enabled devices, even if the device is not the active playback device.

`1`

`...`

`2`

`3`

`struct SpMetadata previous_metadata = {0};`

`4`

`uint8_t previous_playing = 0;`

`5`

`uint8_t previous_shuffle = 0;`

`6`

`uint8_t previous_repeat = 0;`

`7`

`uint32_t previous_position_ms = 0;`

`8`

`uint8_t previous_active = 0;`

`9`

`10`

`int main(int argc, char *argv[]) {`

`11`

`...`

`12`

`struct SpMetadata metadata;`

`13`

`uint8_t playing, shuffle, repeat, active;`

`14`

`uint32_t position_ms;`

`15`

`...`

`16`

`17`

`while (error_occurred == kSpErrorOk) {`

`18`

`SpPumpEvents();`

`19`

`20`

`active = SpPlaybackIsActiveDevice();`

`21`

`if (active != previous_active) {`

`22`

`if (active) {`

`23`

`LOG("This device is the active speaker.\n");`

`24`

`} else {`

`25`

`LOG("This device is not the active speaker.\n");`

`26`

`LOG("The following state reflects what is playing on another\n");`

`27`

`LOG("Connect-enabled device.\n");`

`28`

`}`

`29`

`previous_active = active;`

`30`

`}`

`31`

`32`

`/* Retrieve the metadata of the current track and compare against the`

`33`

`previous metadata. If the metadata changed, update the display.`

`34`

`*/`

`35`

`err = SpGetMetadata(&metadata, kSpMetadataTrackCurrent);`

`36`

`if (err == kSpErrorFailed)`

`37`

`memset(&metadata, 0, sizeof(metadata));`

`38`

`if (memcmp(&metadata, &previous_metadata, sizeof(metadata))) {`

`39`

`if (err == kSpErrorFailed)`

`40`

`LOG("Nothing playing\n");`

`41`

`else`

`42`

`LOG("Playing track: \"%s\" - %s (%d:%02d)\n", metadata.track, metadata.artist,`

`43`

`(metadata.duration_ms / 1000) / 60, (metadata.duration_ms / 1000) % 60);`

`44`

`memcpy(&previous_metadata, &metadata, sizeof(previous_metadata));`

`45`

`}`

`46`

`47`

`playing = SpPlaybackIsPlaying();`

`48`

`if (playing != previous_playing) {`

`49`

`LOG(playing ? "Playing\n" : "Paused\n");`

`50`

`previous_playing = playing;`

`51`

`}`

`52`

`53`

`shuffle = SpPlaybackIsShuffled();`

`54`

`if (shuffle != previous_shuffle) {`

`55`

`LOG(shuffle ? "Shuffle ON\n" : "Shuffle OFF\n");`

`56`

`previous_shuffle = shuffle;`

`57`

`}`

`58`

`59`

`repeat = SpPlaybackIsRepeated();`

`60`

`if (repeat != previous_repeat) {`

`61`

`LOG(repeat ? "Repeat ON\n" : "Repeat OFF\n");`

`62`

`previous_repeat = repeat;`

`63`

`}`

`64`

`65`

`position_sec = SpPlaybackGetPosition() / 1000;`

`66`

`if (position_sec != previous_position_sec) {`

`67`

`LOG("Playback position %d:%02d\n", position_sec / 60, position_sec % 60);`

`68`

`previous_position_sec = position_sec;`

`69`

`}`

`70`

`}`

`71`

`72`

`return 0;`

`73`

`}`

## Reacting to playback restrictions

The playback restrictions are part of the metadata for the current track. Whenever the restrictions change, the application will receive the notification ([kSpPlaybackNotifyMetadataChanged](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification)). To retrieve the restrictions, call [SpGetMetadata()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spgetmetadata) with `relative_index` set to ([kSpMetadataTrackCurrent](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spmetadatatrack)), and look at the fields in [SpMetadata::playback\_restrictions](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spmetadata):

- A value of 0 means the action is allowed.
- A value other than 0 means the action is not allowed. (See [SP\_PLAYBACK\_RESTRICTION\_UNKNOWN](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spotify-embedded-macros) for a special case).

The corresponding playback API will most likely fail. For example, when the field "disallow\_skipping\_next\_reasons" is not 0, and the application invokes [SpPlaybackSkipToNext()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybackskiptonext), the API call will either fail with an error or have no effect.

The UI of the application should update according to the restrictions to grey-out/disable any action that is currently not allowed. This is done in order to make clear to the user what is clickable and what is not to avoid confusion.

Restrictions are useful only for the current track. You **should not** look at the restrictions of the previous or upcoming tracks.

You **must not** build any solution that assumes some behaviour, because any current behaviour can change in the future if our licences change. For example advertisements might be skippable one day.

If the application wants to check the particular reason why an action is not allowed, it can check which bits of the field are set. For example:

`1`

`uint32_t disallow_skip_reasons;`

`2`

`SpMetadata metadata;`

`3`

`If (kSpErrorOk != SpGetMetadata(&metadata, kSpMetadaraTrackCurrent)) {`

`4`

`// An error occurred. Maybe there is no track currently playing?`

`5`

`return;`

`6`

`}`

`7`

`disallow_skip_reasons = metadata.playback_restrictions.disallow_skipping_next_reasons;`

`8`

`if (0 == disallow_skip_reasons) {`

`9`

`// Skipping to the next track is allowed. Can enable Skip button in UI.`

`10`

`} else {`

`11`

`// Skipping to the next track is not allowed. Can disable Skip button in UI.`

`12`

`if (disallow_skip_reasons & SP_PLAYBACK_RESTRICTION_NO_NEXT_TRACK) {`

`13`

`// Skipping is not allowed because there is no next track to skip to.`

`14`

`}`

`15`

`if (disallow_skip_reasons & SP_PLAYBACK_RESTRICTION_AD_DISALLOW) {`

`16`

`// Skipping is not allowed because an ad is playing that can’t be interrupted.`

`17`

`}`

`18`

`// Any number of reasons can apply at the same time.`

`19`

`// ...`

`20`

`}`

### SP\_PLAYBACK\_RESTRICTION\_UNKNOWN

Sometimes the "disallow\_XXX\_reasons" field for an action can be set to [SP\_PLAYBACK\_RESTRICTION\_UNKNOWN](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spotify-embedded-macros). This means that eSDK has not retrieved the restrictions from the backend yet. As soon as eSDK retrieves the information, the notification [kSpPlaybackNotifyMetadataChanged](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification) will be sent again, and the application can check the field again. Until then treat the action as disallowed.

For example, here is a sequence of events:

- When a new track has just started playing, [kSpPlaybackNotifyMetadataChanged](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification) is sent.
- When looking at the metadata, the track and artist names might already have changed, but the field `disallow_skipping_next_reasons` might be set to `SP_PLAYBACK_RESTRICTION_UNKNOWN`.

This means the eSDK has not received the information about whether there is another track after the one that just started playing. After a short while, the backend sends the information and [kSpPlaybackNotifyMetadataChanged](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification) is sent again. This time, `disallow_skipping_next_reasons` might be set to 0.

#### Restrictions on "Repeat" and "Repeat Track"

In the Spotify UI, the "Repeat" button usually cycles through three states: "Don’t repeat", "Repeat", and "Repeat Track". These states are reflected in the eSDK API as follows:

 Don't repeatRepeatRepeat TrackChanging[SpPlaybackEnableRepeat](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackenablerepeat)(0)[SpPlaybackEnableRepeat](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackenablerepeat)(1)[SpPlaybackEnableRepeat](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackenablerepeat)(2)Querying[SpPlaybackGetRepeatMode](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackgetrepeatmode) == 0[SpPlaybackGetRepeatMode](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackgetrepeatmode) == 1[SpPlaybackGetRepeatMode](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackgetrepeatmode) == 2Restricted?disallow\_toggling\_repeat\_context\_reasons != 0disallow\_toggling\_repeat\_track\_reasons != 0

When implementing the UI in your application, make sure users don’t get stuck in a state when attempting to cycle through the states. For example, if "Repeat Track" is not allowed, the application can’t go from "Repeat" to "Repeat Track", and it must go to "Don’t repeat" directly.

`1`

`void on_cycle_repeat_button_pressed() {`

`2`

`uint32_t disallow_repeat, disallow_repeat_track;`

`3`

`SpMetadata metadata;`

`4`

`If (SpGetMetadata(&metadata, kSpMetadataTrackCurrent)!= kSpErrorOk) {`

`5`

`// An error occurred. Maybe there is no track currently playing?`

`6`

`return;`

`7`

`}`

`8`

`disallow_repeat = metadata.playback_restrictions.disallow_toggling_repeat_context_reasons;`

`9`

`disallow_repeat_track = metadata.playback_restrictions.disallow_toggling_repeat_track_reasons;`

`10`

`// Currently in “Don’t repeat”, want to go to “Repeat” (if allowed),`

`11`

`// otherwise to “Repeat Track” (if allowed), otherwise no change.`

`12`

`if (SpPlaybackGetRepeatMode() == 0) {`

`13`

`if (disallow_repeat == 0) {`

`14`

`SpPlaybackEnableRepeat(1);`

`15`

`} else if (0 == disallow_repeat_track) {`

`16`

`SpPlaybackEnableRepeat(2);`

`17`

`}`

`18`

`// Currently in “Repeat”, want to go to “Repeat Track” (if allowed),`

`19`

`// otherwise to “Don’t repeat”.`

`20`

`} else if (SpPlaybackGetRepeatMode() == 1) {`

`21`

`if (disallow_repeat_track == 0) {`

`22`

`SpPlaybackEnableRepeat(2);`

`23`

`} else {`

`24`

`SpPlaybackEnableRepeat(0);`

`25`

`}`

`26`

`// Currently in “Repeat Track”, want to go to “Don’t repeat”.`

`27`

`} else {`

`28`

`//`

`29`

`SpPlaybackEnableRepeat(0);`

`30`

`}`

`31`

`}`

## Other playback events

There are additional playback events that the application can react to. Please see the enum [SpPlaybackNotification](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification) for a complete list.

Important here is to actively listen for the audio playback state. You will have to pause ([kSpPlaybackNotifyPause](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification)) and unpause ([kSpPlaybackNotifyPlay](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification)) independently of the audio data arriving from the audio callback.

Audio data may be delivered while you are paused, and you might have to start playback even though no samples have arrived since the last pause - these samples are then already delivered to you and must be kept in your audio pipeline.

Similarly, you should keep track of if you are the active device or not. Only the active device plays audio. You must receive [kSpPlaybackNotifyBecameActive](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification) in order to be allowed to play audio. It can be received while paused, so that once [kSpPlaybackNotifyPlay](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification) is then received, you should start playing.

The following code shows how these events can be used.

`1`

`2`

`void CallbackPlaybackNotify(enum SpPlaybackNotification event, void *context) {`

`3`

`SpError err;`

`4`

`5`

`switch (event) {`

`6`

`case kSpPlaybackNotifyPlay:`

`7`

`LOG("Playback status: playing\n");`

`8`

`if (active && !playing)`

`9`

`audio_callbacks.audio_pause(0);`

`10`

`playing = 1;`

`11`

`break;`

`12`

`case kSpPlaybackNotifyPause:`

`13`

`LOG("Playback status: paused\n");`

`14`

`if (active && playing)`

`15`

`audio_callbacks.audio_pause(1);`

`16`

`playing = 0;`

`17`

`break;`

`18`

`}`

`19`

`...`

`20`

`21`

`case kSpPlaybackNotifyNext:`

`22`

`LOG("Playing skipped to next track\n");`

`23`

`break;`

`24`

`case kSpPlaybackNotifyPrev:`

`25`

`LOG("Playing jumped to previous track\n");`

`26`

`break;`

`27`

`case kSpPlaybackNotifyBecameActive:`

`28`

`active = 1;`

`29`

`if (playing)`

`30`

`audio_callbacks.audio_pause(0);`

`31`

`LOG("Became active\n");`

`32`

`break;`

`33`

`case kSpPlaybackNotifyBecameInactive:`

`34`

`active = 0;`

`35`

`LOG("Became inactive\n");`

`36`

`if (playing) {`

`37`

`audio_callbacks.audio_pause(1);`

`38`

`playing = 0;`

`39`

`}`

`40`

`break;`

`41`

`case kSpPlaybackNotifyLostPermission:`

`42`

`LOG("Lost permission\n");`

`43`

`if (playing)`

`44`

`audio_callbacks.audio_pause(1);`

`45`

`break;`

`46`

`case kSpPlaybackEventAudioFlush:`

`47`

`LOG("Audio flush\n");`

`48`

`audio_callbacks.audio_flush();`

`49`

`break;`

`50`

`case kSpPlaybackNotifyAudioDeliveryDone:`

`51`

`LOG("Audio delivery done\n");`

`52`

`break;`

`53`

`case kSpPlaybackNotifyTrackDelivered:`

`54`

`LOG("Track delivered\n");`

`55`

`break;`

`56`

`default:`

`57`

`break;`

`58`

`}`

`59`

`}`

`60`

`61`

`...`