---
title: Speaker with Display | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/speaker-display
source: crawler
fetched_at: 2026-02-27T23:41:20.03356-03:00
rendered_js: true
word_count: 568
summary: This document outlines the mandatory branding and metadata display requirements for manufacturers developing commercial hardware with screens integrated with the Spotify eSDK. It specifies how to handle logos, cover art, and song information across various display sizes to ensure device certification.
tags:
    - spotify-esdk
    - hardware-certification
    - branding-guidelines
    - display-requirements
    - metadata-display
    - ui-design
category: guide
---

If a speaker has a display screen, follow these design rules carefully to be certified by Spotify.  

There are three main elements that can appear:

1. **The full Spotify logo** with its round icon and the wordmark “Spotify”.
2. **Cover artwork** which needs to be shown in its orginal form without trimming or animation.
3. **Metadata**. For songs it means song title, artist name, album name, playlist name (if applicable). For podcasts it includes the podcast and episode name. Because of our legal responsibilities to rights holders, the meta data should always be shown in full.

**Note:** If the device supports lossless, please see our [requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/speaker-display#lossless-indicator) further down this page.

When you use Spotify’s eSDK, content from Spotify must always be attributed. When showing the Spotify logo, please be mindful of the “exclusion zone”, or margins around the logo. The logo and the icon’s exclusion zone is equal to half the height of the icon (marked as × in the diagram below). The smallest size for the full Spotify logo is 70px in width. The smallest size for the Spotify icon is 21px.

![Metada Display](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/metadata-display.png)

There are different variations of how to show the information provided by our eSDK, depending on the size and feature(s) of the screen. It is, at all times, **mandatory** to display Spotify attribution and metadata.  
The mandatory metadata parameters for music are:

- Song title
- Artist name
- Album name

For podcasts the mandatory parameters are:

- Podcast name
- Episode name

How this is done depends on the size of the display. Here are some examples:

## Big display

If the display can show images and is big enough to contain all three main elements, please show all of them. How they fit into the UI is up to device manufacturer. **Note:** *The full Spotify logo and metadata is compulsory.*

**Example Display**

![Big Display](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/big-display.png)

## Medium display

When displays aren’t big or advanced enough to display all three main elements, album artwork may be ommitted, since the full Spotify logo and metdata is compulsory. This means the metadata and the full Spotify logo with a round icon and the wordmark “Spotify” are enough to pass certification.

**Example Display**

![Medium Display](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/medium-display.png)

## Small display

If a display is too small to fit the full Spotify logo, show the round Spotify icon and meta data only. It is ok to show the meta data in one row and use “•” to separate them. Content can be scrolled automatically in a non-stop loop inside a small screen.

**Example Display**

![Small Display](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/small-display.png)

## Mini display

The smallest round Spotify icon accepted is 42x42px including the exlusion zone. If a display is smaller than this, skip the round Spotify icon and only display the word “Spotify”.

For legal reasons, it must be clear that the content is from Spotify and meta data must be displayed.

**Example Display**

![Mini Display](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/mini-display.png)

Note: If a device can be played in multiple places or rooms and its not possible to sync the metadata between them, show the metadata on the main device and “Playing from *device\_name*” on the other devices.  Its crucial to follow these guidelines to have any device successfully certified by Spotify.

## Lossless Indicator

If the device supports lossless, please follow our guidelines below to show lossless on the speaker's display.

![Lossless Indicator](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/lossless-indicator-1.png)

![Lossless Indicator](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/lossless-indicator-2.png)

![Lossless Indicator](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/lossless-indicator-3.png)

![Lossless Indicator](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/lossless-indicator-4.png)

Please reach out to your Spotify QA contact via a Jira ticket if you have any questions about the Lossless indicator.