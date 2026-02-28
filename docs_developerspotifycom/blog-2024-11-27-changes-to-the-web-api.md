---
title: Introducing some changes to our Web API
url: https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api
source: crawler
fetched_at: 2026-02-27T23:40:12.731503-03:00
rendered_js: true
word_count: 247
summary: This document announces security-related updates to the Spotify Web API that restrict access to specific endpoints, such as Recommendations and Audio Features, for new and development-mode applications.
tags:
    - spotify-api
    - api-updates
    - web-api
    - developer-policy
    - access-restrictions
category: api
---

Introducing some changes to our Web API

Posted November 27, 2024

![](https://developer.spotify.com/images/avatars/spotify.png)

Spotify

Since our last broader update on the Community platform, we continue to see new integrations made through Spotify’s APIs and SDKs. We’re excited about the continued engagement we’re seeing to learn, experiment, innovate, and deliver unique experiences with Spotify.

As we continue to review the experience provided on Spotify for Developers, we've decided to roll out a number of measures with the aim of creating a more secure platform.

## Web API endpoint integration

Effective today, ***new*** Web API use cases will no longer be able to access or use the following endpoints and functionality in their third-party applications. Applications with existing extended mode Web API access that were relying on these endpoints remain unaffected by this change.

1. [Related Artists](https://developer.spotify.com/documentation/web-api/reference/get-an-artists-related-artists)
2. [Recommendations](https://developer.spotify.com/documentation/web-api/reference/get-recommendations)
3. [Audio Features](https://developer.spotify.com/documentation/web-api/reference/get-audio-features)
4. [Audio Analysis](https://developer.spotify.com/documentation/web-api/reference/get-audio-analysis)
5. [Get Featured Playlists](https://developer.spotify.com/documentation/web-api/reference/get-featured-playlists)
6. [Get Category's Playlists](https://developer.spotify.com/documentation/web-api/reference/get-a-categories-playlists)
7. [30-second preview URLs](https://developer.spotify.com/documentation/web-api/reference/get-track), in multi-get responses (`SimpleTrack` object)
8. Algorithmic and Spotify-owned editorial playlists

These changes will impact the following Web API applications:

- Existing apps that are still in [development mode](https://developer.spotify.com/documentation/web-api/concepts/quota-modes) without a pending extension request
- New apps that are registered on or after today's date

## What’s next?

Third party integrations continue to play an important role in the way users can experience the Spotify experience through third party apps. We evaluate the set up of our platform on an ongoing basis and remain committed to ensuring it provides the best possible opportunities for developers, artists, creators and listeners.

Our [forum](https://community.spotify.com/t5/Spotify-for-Developers/Changes-to-Web-API/td-p/6540414) remains open to any feedback.