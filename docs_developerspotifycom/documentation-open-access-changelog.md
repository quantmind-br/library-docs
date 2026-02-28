---
title: Changelog | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/changelog
source: crawler
fetched_at: 2026-02-27T23:42:03.991509-03:00
rendered_js: true
word_count: 380
summary: This document tracks the version history and feature updates for the Spotify Open Access platform, detailing improvements to account linking, developer tools, and API functionality.
tags:
    - spotify-open-access
    - changelog
    - platform-updates
    - account-linking
    - developer-tools
    - api-changes
category: other
---

This page keeps track of improvements and iterations of the Spotify Open Access platform.

### Version 1.6.0 - July 27th, 2022

- [**Unlinking support**](https://developer.spotify.com/documentation/open-access/tutorials/account#unlinking) - Partners can now direct their users to [content-access.spotify.com](https://content-access.spotify.com/) to manage their linked accounts, and unlink themselves. Additionally, partners are now able to build the unlinking patterns into their own user interface using the new [/unlink-user endpoint](https://developer.spotify.com/documentation/open-access/reference/unlink-user).
- [**Example partner website**](https://lunar-industries.spotify.com/) - We've created an example website and open source repository to help guide partners as they build an integration with Open Access. Lunar Industries has three shows, [a website](https://lunar-industries.spotify.com/) and [a public git repository](https://github.com/spotify/soa-reference-integration) that simulates a working integration. The documentation now refers to the example partner with links.

### Version 1.5.0 - January 27th, 2022

- [**Sandbox mode**](https://developer.spotify.com/documentation/open-access/tutorials/content#sandbox-mode) - Content can now be used during testing without worrying that users might find it pre-launch, as it won’t be searchable. Partners will have to link directly to their show to be able to find it.
- [**Improved account linking flow**](https://developer.spotify.com/documentation/open-access/tutorials/account#linking) - We started seeing varying user flows on partner websites, often leaving the user on a general landing page, only to have to find the relevant podcast themselves. We’ve added an educational step and shortened the linking flow, which will improve and simplify our partner’s understanding of this important part of their SOA integration. Additionally, we’ve also shipped Auto-login for Android devices, which makes this experience a little smoother for users on an Android-powered phone (we already support this for iOS).
- [**Passing show state**](https://developer.spotify.com/documentation/open-access/concepts#spotify-show-uri) - When a user has linked their Spotify account to a partner account, we show them a success page with all of the shows they’ve gotten access to. With this update, we remember the show where the user has clicked “Get Access”, and show it on top of the success screen.
- **Upload membership images** - SOA supports both single publishers and membership platforms. Partners can upload their member logos using the SOA API so that when a user connects their account, they are reassured that connecting to Spotify will give them access to the creator they already support.

### Version 1.4.0 - December 12th, 2021

- [**Updated linking flow sequence diagram**](https://developer.spotify.com/documentation/open-access/tutorials/account#linking) - We now use UML to generate the linking flow sequence diagram.
- [**Introduced SOA specific concepts**](https://developer.spotify.com/documentation/open-access/concepts) - With additional domain-specific terminology, SOA concepts are now easier to grasp.