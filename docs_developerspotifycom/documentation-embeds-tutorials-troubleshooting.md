---
title: Troubleshooting | Spotify for Developers
url: https://developer.spotify.com/documentation/embeds/tutorials/troubleshooting
source: crawler
fetched_at: 2026-02-27T23:40:22.750101-03:00
rendered_js: true
word_count: 193
summary: This document provides troubleshooting steps for issues where Spotify Embeds only play audio previews, focusing on browser compatibility and iframe attributes.
tags:
    - spotify-embed
    - iframe-integration
    - encrypted-media
    - troubleshooting
    - web-player
category: guide
---

In some situations the Embed will only stream a preview clip of less than 30 seconds. You may see a warning message in the JavaScript console that says "Spotify was not able to play encrypted media." If this happens, try these steps:

## Try a different browser

Embeds work best in Chrome, Firefox, Edge, Opera and Safari. If your browser is not on this list then it may not be possible to listen to full episodes and songs through the Embed. [Here](https://support.spotify.com/us/article/web-player-help/) you can find a complete list of browser versions we support.

## Make sure that the Embed code is complete

The generated Embed code includes an `<iframe>` tag. If your application modifies the iFrame tag, or if you've made changes to the code manually, then this can cause the Embed to only stream a preview of the audio. In particular, make sure that you have not removed the `allow="encrypted-media"` attribute from the iFrame element — without this, the Embed will only allow users to listen to previews.

## Ask for help

Still need help with debugging a problem with your Embed? Visit the [Spotify for Developers community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer) and tell us about your implementation.