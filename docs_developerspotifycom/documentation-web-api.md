---
title: Web API | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api
source: crawler
fetched_at: 2026-02-27T23:45:15.873405-03:00
rendered_js: true
word_count: 334
summary: This document provides an introductory overview of the Spotify Web API, outlining the initial steps for app creation, authorization, and the types of music data and playback controls available to developers.
tags:
    - spotify-web-api
    - developer-onboarding
    - app-credentials
    - music-streaming
    - api-integration
category: guide
---

Spotify Web API enables the creation of applications that can interact with Spotify's streaming service, such as retrieving content metadata, creating and managing playlists, or controlling playback.

## Getting started

This is where the magic begins! The following steps will help you to get started with your journey towards creating some awesome music apps using the API:

**Note:** You need a Spotify Premium account to use the Web API.

1. Log into the [dashboard](https://developer.spotify.com/dashboard) using your Spotify account.
2. [Create an app](https://developer.spotify.com/documentation/web-api/concepts/apps) and select "Web API" for the question asking which APIs are you planning to use. Once you have created your app, you will have access to the app credentials. These will be required for API [authorization](https://developer.spotify.com/documentation/web-api/concepts/authorization) to obtain an [access token](https://developer.spotify.com/documentation/web-api/concepts/access-token).
3. Use the [access token](https://developer.spotify.com/documentation/web-api/concepts/access-token) in your [API requests](https://developer.spotify.com/documentation/web-api/concepts/api-calls).

You can follow the [Getting started](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) tutorial to learn how to make your first Web API call.

## Documentation

The documentation is organized as follows:

- Concepts that clarify key topics
- Tutorials, which serve as an introduction to important topics when using Web API
- How-Tos, step-by-step guides that cover practical tasks or use cases
- Reference, the API specification

## API reference

The Spotify Web API provides a wide range of functionality for developers, including:

- Retrieve data from your favourite [artist](https://developer.spotify.com/documentation/web-api/reference/get-an-artist), [album](https://developer.spotify.com/documentation/web-api/reference/get-an-album) or [show](https://developer.spotify.com/documentation/web-api/reference/get-a-show).
- [Search](https://developer.spotify.com/documentation/web-api/reference/search) for Spotify content.
- Control and interact with the playback, [play and resume](https://developer.spotify.com/documentation/web-api/reference/start-a-users-playback), [seek to a position](https://developer.spotify.com/documentation/web-api/reference/seek-to-position-in-currently-playing-track) or [retrieve your queue](https://developer.spotify.com/documentation/web-api/reference/get-queue).
- Manage your personal [library](https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists), by [creating a new playlist](https://developer.spotify.com/documentation/web-api/reference/create-playlist) and [adding your favourite tracks](https://developer.spotify.com/documentation/web-api/reference/add-items-to-playlist) to it.

And much more! You can find a complete list of available endpoints in the API Reference.

## Examples

We've provided a [step-by-step how-to](https://developer.spotify.com/documentation/web-api/howtos/web-app-profile) that will guide you through the creation of a web app to display your Spotify profile data.

## Support

If you have any questions or run into any issues while using the Spotify Web API, you can find help in the [Spotify Developer Community](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). Here, you can connect and get help from other developers.

## Legal

By using Spotify Web API, you accept the [Spotify Developer Terms of Service](https://developer.spotify.com/terms).