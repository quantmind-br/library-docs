---
title: Access Token | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/concepts/access-token
source: crawler
fetched_at: 2026-02-27T23:45:17.684443-03:00
rendered_js: true
word_count: 183
summary: This document explains the purpose and usage of access tokens for API authorization, including the required header format and token expiration details.
tags:
    - access-token
    - api-authorization
    - bearer-token
    - authentication
    - web-api
category: guide
---

The *access token* is a string which contains the credentials and permissions that can be used to access a given resource (e.g artists, albums or tracks) or user's data (e.g your profile or your playlists).

To use the *access token* you must include the following header in your API calls:

Header ParameterValueAuthorizationValid access token following the format: `Bearer <Access Token>`

Note that the *access token* is valid for 1 hour (3600 seconds). After that time, the token expires and you need to request a new one.

## Examples

The following example uses `cURL` to retrieve information about a track using the [Get a track](https://developer.spotify.com/documentation/web-api/reference/get-track) endpoint:

`1`

`curl --request GET \`

`2`

`'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V' \`

`3`

`--header "Authorization: Bearer NgCXRK...MzYjw"`

The following code implements the `getProfile()` function which performs the API call to the [Get Current User's Profile](https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile) endpoint to retrieve the user profile related information:

`1`

`async function getProfile(accessToken) {`

`2`

`let accessToken = localStorage.getItem('access_token');`

`3`

`4`

`const response = await fetch('https://api.spotify.com/v1/me', {`

`5`

`headers: {`

`6`

`Authorization: 'Bearer ' + accessToken`

`7`

`}`

`8`

`});`

`9`

`10`

`const data = await response.json();`

`11`

`}`