---
title: Companion App | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/companion-app
source: crawler
fetched_at: 2026-02-27T23:41:17.165259-03:00
rendered_js: true
word_count: 849
summary: This document outlines the mandatory design requirements and certification rules for hardware companion apps integrating Spotify, focusing on Spotify Connect instructions and playback interface elements.
tags:
    - spotify-connect
    - companion-app
    - design-guidelines
    - certification-requirements
    - user-interface
    - branding-rules
category: guide
---

If a device has a companion app, follow these design rules carefully to be certified by Spotify.  

## “Spotify Connect instructions” view

Your companion app must include the Spotify Connect instructions.

The elements that need to be shown in this view are:

1. The Spotify logo
2. The line *Ready to play some music? Listen on your speakers or TV, using the Spotify app as a remote*  The translation of this line to other languages can be [downloaded here](https://spotify.app.box.com/s/3rpiouxj7xsvzm25e4arntd5haruygyx).
3. A *learn more* link to the URL [spotify.com/connect](https://spotify.com/connect).
4. A button saying *OPEN SPOTIFY APP* or *GET SPOTIFY FREE*. Here are the linking guideline and translations:

<!--THE END-->

- If the user has Spotify installed, this button should say *Open Spotify App* and be linked to open Spotify app.
- If the user doesn’t have Spotify app yet, this button should say *Get Spotify Free* and link to a store where they can download Spotify.
- The translation of these lines to other languages can be [downloaded here](https://spotify.app.box.com/s/cmh3iytkk7767obyh6mqu9k6knw62nvs)

If your device supports a Spotify voice integration, you must include these additional instructions: 

*Use your voice to control Spotify. Ask &lt;voice assistant&gt; to play your favourite playlists, artists and genres. For example, just say, &lt;wakeword&gt;, play Today’s Top Hits*.

The translation of this line to other languages can be [downloaded here](https://spotify.app.box.com/s/1awp8yknp567zklxtql287p1xpvmc849).

![Companion App Voice Integration](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/companion-app-voice.png)

## “Now Playing” view

When Spotify is playing on the device, it must always be correctly attributed with the Spotify logo. If the app supports “now playing” views, you must follow the below requirements.

There are five main elements that can appear in this view as shown in the graph below: the Spotify logo, the metadata, the cover artwork, a progress bar, a play/pause button.

**Note:** If the device supports lossless, please see our [requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/companion-app#lossless-indicator) further down this page.

![Companion App Now Playing](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/companion-app-playing.png)

### Compulsory elements

**1. Spotify logo**

The Spotify logo has two parts: its round icon and the wordmark “Spotify”. When showing the Spotify logo, please be mindful of the “exclusion zone”, or margins around the logo. The downloadable logo file and the detailed logo guideline can be found [here](https://developer.spotify.com/documentation/design).

![Companion App Logo](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/companion-app-logo.png)

1. If there is enough screen real easte, please always show the full logo with its round icon and its workmark.
2. If the space doesn’t allow the display of a full logo, it is ok to only show the round icon.
3. The smallest round Spotify icon accepted is 42x42px including the exlusion zone. If space is smaller than this, skip the round Spotify icon and only display the word “Spotify”.

**2. Metadata**

The following metadata shall always be presented:

- For music, **track title**, **artist name** and **album name**.
- For podcasts, **episode title** and **show name**.

If you have a screen that supports showing images, you shall display the album artwork or the episode artwork respectively as well. If the space is limited, it is ok to show the metadata in one row and use “•” to separate them.  If there is not enough space to show all the metadata at the same time, it should be scrolled automatically in a non-stop loop.

### Optional elements

**3. Cover artwork**

The cover artwork should be shown in its original form. No manipulation such as trimming or animation is allowed.

**4. Progress bar**

A progress bar showing how far a song is played may be displayed in the companion app, however, it may not be interactable.

**5. Playback control**

The only playback control allowed in your companion app is **play/pause**. Any additional playback controls (e.g. seek using progress bar) need to be explicitly approved by Spotify. The reason is that the eSDK follows the current license applicable for the combination of user account, device, and possibly other factors. At any time, restrictions regarding the ability to move between and inside tracks may be applied.

![Companion App Elements small View](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/companion-app-elements-view.png)

![Companion App Elements small View](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/companion-app-elements-small-view.png)

**Note**: *The Spotify logo and metadata is compulsory, meaning that it must be prioritized over the optional elements such as album artwork, progress bar and playback control. This applies to every available viewing option in the companion app.*

### Link to Spotify (compulsory)

In the “Now Playing” view, there must be a deeplink to Spotify.

1. If you show a cover artwork, it must link into the Spotify app.
2. If there is no cover art due to lack of screen real estate, the metadata can be used instead.
3. If the New Playing View is very small, we recommend to make the whole area of metadata together with the logo icon clickable as a link

The link should have the same logic as the *OPEN SPOTIFY/GET SPOTIFY FREE* button:

- If the user has Spotify installed, it should be linked to open Spotify app.
- If the user doesn’t have Spotify app yet, it should be linked to a store where they can download Spotify.

![Companion App Link Spotify](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/companion-app-link-spotify.png)

![Companion App Link Spotify](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/companion-app-link-spotify-02.png)

### Lossless Indicator

If the device supports lossless, please follow our guidelines below to display it in the companion app.

![Lossless Indicator](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/lossless-indicator-1.png)

![Lossless Indicator](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/lossless-indicator-2.png)

![Lossless Indicator](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/lossless-indicator-3.png)

![Lossless Indicator](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/lossless-indicator-4.png)

Please reach out to your Spotify QA contact via a Jira ticket if you have any questions about the Lossless indicator.