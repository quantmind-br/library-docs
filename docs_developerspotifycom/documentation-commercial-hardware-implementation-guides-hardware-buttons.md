---
title: Connecting Hardware Buttons | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/hardware-buttons
source: crawler
fetched_at: 2026-02-27T23:41:23.040244-03:00
rendered_js: true
word_count: 119
summary: This document outlines the SpPlayback functions, callbacks, and getters required to implement media control features for physical hardware buttons using the Spotify Embedded SDK.
tags:
    - spotify-esdk
    - playback-control
    - hardware-integration
    - embedded-sdk
    - api-reference
    - media-functions
category: reference
---

Warning:

Commercial Hardware tools and the eSDK are available only for approved partners

If the device has hardware buttons for things like "Play", "Pause", "Skip Track", etc., the application should use SpPlayback*XXX*() functions to perform these actions in the Spotify Embedded SDK. The following table shows which functions exist and it also lists the corresponding callbacks and "getter" functions.

ActionFunctionCallback/EventGetterPlay[SpPlaybackPlay()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackplay)[kSpPlaybackNotifyPlay](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybacknotification)[SpPlaybackIsPlaying()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackisplaying)Pause[SpPlaybackPause()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackpause)[kSpPlaybackNotifyPlay](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybacknotification)[SpPlaybackIsPlaying()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackisplaying)Skip to next track[SpPlaybackSkipToNext()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackskiptonext)[kSpPlaybackNotifyPlay](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybacknotification)N/ASkip to previous track[SpPlaybackSkipToPrev()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackskiptoprev)[kSpPlaybackNotifyPlay](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybacknotification)N/ASeek[SpPlaybackSeek()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackseek)[SpCallbackPlaybackSeek()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spcallbackplaybackseek)[SpPlaybackGetPosition()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackgetposition)Volume[SpPlaybackUpdateVolume()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackupdatevolume)[SpCallbackPlaybackApplyVolume()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spcallbackplaybackapplyvolume)[SpPlaybackGetVolume()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackgetvolume)Shuffle[SpPlaybackEnableShuffle()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackenableshuffle)[kSpPlaybackNotifyShuffleOn](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybacknotification), [kSpPlaybackNotifyShuffleOff](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybacknotification)[SpPlaybackIsShuffled()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackisshuffled)Repeat[SpPlaybackEnableRepeat()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackenablerepeat)[kSpPlaybackNotifyRepeatOn](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybacknotification), [kSpPlaybackNotifyRepeatOff](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybacknotification)[SpPlaybackIsRepeated()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest/#spplaybackisrepeated)

**Note**: If the user is playing on another Connect-enabled device, the function [SpPlaybackPlay](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybackplay) will pull playback to the device. This way, pressing the "Play" button on the device has the same effect as pushing playback to the device by using the Spotify mobile app. The device will become the active device.