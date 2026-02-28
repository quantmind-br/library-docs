---
title: iFrame API | Spotify for Developers
url: https://developer.spotify.com/documentation/embeds/references/iframe-api
source: crawler
fetched_at: 2026-02-27T23:40:20.282452-03:00
rendered_js: true
word_count: 671
summary: This document defines the methods and events for the Spotify IFrame API, providing developers with the technical specifications to programmatically embed and control Spotify content.
tags:
    - spotify-api
    - iframe-api
    - javascript-sdk
    - web-embeds
    - media-playback
    - api-reference
category: api
---

## Methods

### `window.onSpotifyIframeApiReady(object)`

Define this global function so that your app knows when the iFrame API is ready to use. It receives an object (`IFrameAPI` in our example) which you can use to create controllers.

#### Parameters

ParameterTypeDescriptionIFrameAPIobjectObject you can use to create iFrame API controllers

#### Code sample

`1`

`window.onSpotifyIframeApiReady = IFrameAPI => {`

`2`

`let element = document.getElementById('embed-iframe');`

`3`

`let options = {`

`4`

`uri: 'spotify:episode:7makk4oTQel546B0PZlDM5',`

`5`

`};`

`6`

`let callback = EmbedController => {};`

`7`

`IFrameAPI.createController(element, options, callback);`

`8`

`};`

* * *

### `IFrameAPI.createController(element, options, callback)`

Call `createController` for each Embed that you'd like to position on the web page.

#### Parameters

ParameterTypeDescriptionelementobjectDOM element that you'd like replaced by the EmbedoptionsobjectKey value pairs that configure the new controller. The available options are `uri`, the Spotify URI of the content you'd like loaded first; `width`, the width in pixels of the Embed, and `height`, the height in pixels of the Embed. See the sample below for an example.callbackfunctionFunction that receives the created controller object (*EmbedController* in the following examples)

#### Code sample

`1`

`let element = document.getElementById('embed-iframe');`

`2`

`let options = {`

`3`

`width: 200,`

`4`

`height: 400,`

`5`

`uri: 'spotify:episode:7makk4oTQel546B0PZlDM5',`

`6`

`};`

`7`

`let callback = EmbedController => {};`

`8`

`IFrameAPI.createController(element, options, callback);`

* * *

### `EmbedController.loadUri(spotifyUri)`

Use this method to load a new podcast episode into an Embed that you have created.

#### Parameters

ParameterTypeDescriptionspotifyUristringString of a podcast episode URI you'd like to load in the EmbedpreferVideobooleanAn optional parameter to play the video of a podcast episode, if availablestartAtnumberThe timestamp (in seconds) from where playback should start when the `play` method is calledthemestringAn optional parameter to set the theme of the Embed. Possible value is `dark`

#### Code sample

`1`

`EmbedController.loadUri('spotify:episode:7makk4oTQel546B0PZlDM5');`

* * *

### `EmbedController.play()`

This method begins playing the content that had been previously loaded.

#### Code sample

* * *

### `EmbedController.pause()`

This method pauses playback.

#### Code sample

`1`

`EmbedController.pause();`

* * *

### `EmbedController.resume()`

If playback is paused, this method can be used to resume it. If playback was not started, this method will start playback.

#### Code sample

`1`

`EmbedController.resume();`

* * *

### `EmbedController.togglePlay()`

This method toggles between play and pause.

#### Code sample

`1`

`EmbedController.togglePlay();`

* * *

### `EmbedController.restart()`

Use this method to restart playback from the beginning.

#### Code sample

`1`

`EmbedController.restart();`

* * *

### `EmbedController.seek(seconds)`

Use this method to seek to a given point in the podcast episode that has been loaded in the Embed.

#### Parameters

ParameterTypeDescriptionsecondsintegerThe number of seconds into the podcast episode after which you would like to move the cursor

#### Code sample

`1`

`EmbedController.seek(200);`

* * *

### `EmbedController.destroy()`

Destroys the Embed and removes its DOM element from the page.

#### Code sample

`1`

`EmbedController.destroy();`

* * *

## Events

### `ready`

This event fires after an Embed has initialized and is ready to stream content

#### Code sample

`1`

`EmbedController.addListener('ready', () => {`

`2`

`console.log('The Embed has initialized');`

`3`

`});`

* * *

### `playback_started`

This event fires when a track or podcast episode starts playing. For tracks in a collection like playlist or album, it will be fired once for each track as and when it starts playing. Additionally, it also fires if the playback was restarted after it was completed. The event handler will receive an object with a property describing the currently playing entity: `playingURI` (string).

#### Code sample

`1`

`EmbedController.addListener('playback_started', e => {`

`2`

`console.log('The playback has started for: ' + e.data.playingURI);`

`3`

`});`

* * *

### `playback_update`

This event fires after the state of playback changes. Playback state changes can occur by the user tapping on the playback controls in the Embed, or programmatically through methods of the iFrame API, such as the seek() method.

The event handler will receive an object with four properties describing the current playback state: `playingURI` (string), `isPaused` (bool), `isBuffering` (bool), `duration` (number) and `position` (number). `duration` describes the length of the loaded podcast episode in milliseconds and `position` describes the cursor location in milliseconds.

#### Code sample

`1`

`EmbedController.addListener('playback_update', e => {`

`2`

``document.getElementById('progressTimestamp').innerText = `${parseInt(``

`3`

`e.data.position / 1000,`

`4`

`10,`

`5`

``)} s`;``

`6`

`});`

## Notes

- The iFrame API's `play` method, which starts playback of the Embed player without user interaction, might not be supported in all browsers and for all users. For instance, Safari blocks autoplay without user interaction. Read more about [autoplay policy](https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide#autoplay_policy) or [autoplay policy in Chrome](https://developer.chrome.com/blog/autoplay).