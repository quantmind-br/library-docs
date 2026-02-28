---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/create-playlist-for-user
source: crawler
fetched_at: 2026-02-27T23:46:52.49877-03:00
rendered_js: false
word_count: 578
summary: This document describes the deprecated Spotify Web API endpoint for creating a new playlist for a specific user, outlining the required scopes, request parameters, and response structure.
tags:
    - spotify-api
    - web-api
    - playlists
    - user-playlists
    - deprecated
    - playlist-management
category: api
---

Web API •References / Playlists / Create Playlist for user

## Create Playlist for user

Deprecated

**Deprecated**: Use [Create Playlist](https://developer.spotify.com/documentation/web-api/reference/create-playlist) instead.

Create a playlist for a Spotify user. (The playlist will be empty until you [add tracks](https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist).) Each user is generally limited to a maximum of 11000 playlists.

## Request

supports free form additional properties

- The name for the new playlist, for example `"Your Coolest Playlist"`. This name does not need to be unique; a user may have several playlists with the same name.
- Defaults to `true`. The playlist's public/private status (if it should be added to the user's profile or not): `true` the playlist will be public, `false` the playlist will be private. To be able to create private playlists, the user must have granted the `playlist-modify-private` [scope](https://developer.spotify.com/documentation/web-api/concepts/scopes#list-of-scopes). For more about public/private status, see [Working with Playlists](https://developer.spotify.com/documentation/web-api/concepts/playlists)
- Defaults to `false`. If `true` the playlist will be collaborative. ***Note**: to create a collaborative playlist you must also set `public` to `false`. To create collaborative playlists you must have granted `playlist-modify-private` and `playlist-modify-public` [scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes#list-of-scopes).*
- value for playlist description as displayed in Spotify Clients and in the Web API.

## Response

A playlist

- `true` if the owner allows other users to modify the playlist.
- The playlist description. *Only returned for modified, verified playlists, otherwise* `null`.
- Known external URLs for this playlist.
- A link to the Web API endpoint providing full details of the playlist.
- Images for the playlist. The array may be empty or contain up to three images. The images are returned by size in descending order. See [Working with Playlists](https://developer.spotify.com/documentation/web-api/concepts/playlists). ***Note**: If returned, the source URL for the image (`url`) is temporary and will expire in less than a day.*
  
  - The source URL of the image.
    
    Example: `"https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228"`
  - The image height in pixels.
    
    Example: `300`
  - The image width in pixels.
    
    Example: `300`
- The name of the playlist.
- The user who owns the playlist
  
  - Known public external URLs for this user.
  - A link to the Web API endpoint for this user.
  - The name displayed on the user's profile. `null` if not available.
- The playlist's public/private status (if it is added to the user's profile): `true` the playlist is public, `false` the playlist is private, `null` the playlist status is not relevant. For more about public/private status, see [Working with Playlists](https://developer.spotify.com/documentation/web-api/concepts/playlists)
- The version identifier for the current playlist. Can be supplied in other requests to target a specific playlist version
- The items of the playlist. ***Note**: This field is only available for playlists owned by the current user or playlists the user is a collaborator of.*
  
  - A link to the Web API endpoint returning the full result of the request
    
    Example: `"https://api.spotify.com/v1/me/shows?offset=0&limit=20"`
  - The maximum number of items in the response (as set in the query or by default).
    
    Example: `20`
  - URL to the next page of items. ( `null` if none)
    
    Example: `"https://api.spotify.com/v1/me/shows?offset=1&limit=1"`
  - The offset of the items returned (as set in the query or by default)
    
    Example: `0`
  - URL to the previous page of items. ( `null` if none)
    
    Example: `"https://api.spotify.com/v1/me/shows?offset=1&limit=1"`
  - The total number of items available to return.
    
    Example: `4`
- **Deprecated:** Use `items` instead. The tracks of the playlist.
  
  - A link to the Web API endpoint returning the full result of the request
    
    Example: `"https://api.spotify.com/v1/me/shows?offset=0&limit=20"`
  - The maximum number of items in the response (as set in the query or by default).
    
    Example: `20`
  - URL to the next page of items. ( `null` if none)
    
    Example: `"https://api.spotify.com/v1/me/shows?offset=1&limit=1"`
  - The offset of the items returned (as set in the query or by default)
    
    Example: `0`
  - URL to the previous page of items. ( `null` if none)
    
    Example: `"https://api.spotify.com/v1/me/shows?offset=1&limit=1"`
  - The total number of items available to return.
    
    Example: `4`
- The object type: "playlist"

## Response sample

```

```