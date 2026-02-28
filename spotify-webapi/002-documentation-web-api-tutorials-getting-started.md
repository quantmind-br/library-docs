---
title: Getting started with Web API
url: https://developer.spotify.com/documentation/web-api/tutorials/getting-started
source: crawler
fetched_at: 2026-02-27T23:45:18.792589-03:00
rendered_js: true
word_count: 852
summary: This tutorial provides a step-by-step guide for making a first Spotify Web API call, covering app registration, obtaining an access token via client credentials, and retrieving artist metadata using cURL.
tags:
    - spotify-api
    - web-api
    - authentication
    - client-credentials
    - curl
    - getting-started
category: tutorial
---

This tutorial will help you to make your first Web API call by retriving an artist's metadata. The steps to do so are the following:

1. [Create an app](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app), if you haven't done so.
2. [Request an access token](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token).
3. Use the access token to [request the artist data](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-artist-data).

Here we go, let's rock & roll!

## Prerequisites

- This tutorial assumes you have a Spotify Premium account.
- We will use `cURL` to make API calls. You can install it from [here](https://curl.se/download.html) our using the package manager of your choice.

## Set Up Your Account

Login to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard). If necessary, read the latest [Developer Terms of Service](https://developer.spotify.com/terms) to complete your account set up.

## Create an app

An app provides the *Client ID* and *Client Secret* needed to request an *access token* by implementing any of the [authorization](https://developer.spotify.com/documentation/web-api/concepts/authorization) flows.

To create an app, go to [your Dashboard](https://developer.spotify.com/dashboard), click on the *Create an app* button and enter the following information:

- App Name: *My App*
- App Description: *This is my first Spotify app*
- Redirect URI: You won't need this parameter in this example, so let's use `http://127.0.0.1:3000`.

Finally, check the *Developer Terms of Service* checkbox and tap on the *Create* button.

## Request an access token

The *access token* is a string which contains the credentials and permissions that can be used to access a given resource (e.g artists, albums or tracks) or user's data (e.g your profile or your playlists).

In order to request the *access token* you need to get your *Client\_ID* and *Client Secret*:

1. Go to the [Dashboard](https://developer.spotify.com/dashboard)
2. Click on the name of the app you have just created (`My App`)
3. Click on the *Settings* button

The *Client ID* can be found here. The *Client Secret* can be found behind the *View client secret* link.

With our credentials in hand, we are ready to request an access token. This tutorial uses the [Client Credentials](https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow), so we must:

- Send a POST request to the token endpoint URI.
- Add the `Content-Type` header set to the `application/x-www-form-urlencoded` value.
- Add a HTTP body containing the *Client ID* and *Client Secret*, along with the `grant_type` parameter set to `client_credentials`.

`1`

`curl -X POST "https://accounts.spotify.com/api/token" \`

`2`

`-H "Content-Type: application/x-www-form-urlencoded" \`

`3`

`-d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"`

The response will return an *access token* valid for 1 hour:

`1`

`{`

`2`

`"access_token": "BQDBKJ5eo5jxbtpWjVOj7ryS84khybFpP_lTqzV7uV-T_m0cTfwvdn5BnBSKPxKgEb11",`

`3`

`"token_type": "Bearer",`

`4`

`"expires_in": 3600`

`5`

`}`

## Request artist data

For this example, we will use the [Get Artist](https://developer.spotify.com/documentation/web-api/reference/get-an-artist) endpoint to request information about an artist. According to the API Reference, the endpoint needs the [Spotify ID](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) of the artist.

An easy way to get the Spotify ID of an artist is using the Spotify Desktop App:

1. Search the artist
2. Click on the three dots icon from the artist profile
3. Select *Share &gt; Copy link to artist*. The Spotify ID is the value that comes right after the `open.spotify.com/artist` URI.

Our API call must include the *access token* we have just generated using the `Authorization` header as follows:

`1`

`curl "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb" \`

`2`

`-H "Authorization: Bearer BQDBKJ5eo5jxbtpWjVOj7ryS84khybFpP_lTqzV7uV-T_m0cTfwvdn5BnBSKPxKgEb11"`

If everything goes well, the API will return the following JSON response:

`1`

`{`

`2`

`"external_urls": {`

`3`

`"spotify": "https://open.spotify.com/artist/4Z8W4fKeB5YxbusRsdQVPb"`

`4`

`},`

`5`

`"followers": {`

`6`

`"href": null,`

`7`

`"total": 7625607`

`8`

`},`

`9`

`"genres": [`

`10`

`"alternative rock",`

`11`

`"art rock",`

`12`

`"melancholia",`

`13`

`"oxford indie",`

`14`

`"permanent wave",`

`15`

`"rock"`

`16`

`],`

`17`

`"href": "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb",`

`18`

`"id": "4Z8W4fKeB5YxbusRsdQVPb",`

`19`

`"images": [`

`20`

`{`

`21`

`"height": 640,`

`22`

`"url": "https://i.scdn.co/image/ab6761610000e5eba03696716c9ee605006047fd",`

`23`

`"width": 640`

`24`

`},`

`25`

`{`

`26`

`"height": 320,`

`27`

`"url": "https://i.scdn.co/image/ab67616100005174a03696716c9ee605006047fd",`

`28`

`"width": 320`

`29`

`},`

`30`

`{`

`31`

`"height": 160,`

`32`

`"url": "https://i.scdn.co/image/ab6761610000f178a03696716c9ee605006047fd",`

`33`

`"width": 160`

`34`

`}`

`35`

`],`

`36`

`"name": "Radiohead",`

`37`

`"popularity": 79,`

`38`

`"type": "artist",`

`39`

`"uri": "spotify:artist:4Z8W4fKeB5YxbusRsdQVPb"`

`40`

`}`

Congratulations! You made your first API call to the Spotify Web API.

## Summary

- The Spotify Web API provides different endpoints depending on the data we want to access. The API calls must include the `Authorization` header along with a valid access token.
- This tutorial makes use of the [client credentials](https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow) grant type to retrieve the access token. That works fine in scenarios where you control the API call to Spotify, for example where your backend is connecting to the Web API. It will not work in cases where your app will connect on behalf of a specific user, for example when getting private playlist or profile data.

## What's next?

- The tutorial used the Spotify Desktop App to retrieve the Spotify ID of the artist. The ID can also be retrieved using the [Search endpoint](https://developer.spotify.com/documentation/web-api/reference/search). An interesting exercise would be to extend the example with a new API call to the `/search` endpoint. Do you accept the challenge?
- The [authorization](https://developer.spotify.com/documentation/web-api/concepts/authorization) guide provides detailed information about which authorization flow suits you best. Make sure you read it first!
- You can continue your journey by reading the [API calls](https://developer.spotify.com/documentation/web-api/concepts/api-calls) guide which describes in detail the Web API request and responses.
- Finally, if you are looking for a more practical documentation, you can follow the [Display your Spotify Profile Data in a Web App](https://developer.spotify.com/documentation/web-api/howtos/web-app-profile) how-to which implements a step-by-step web application using [authorization code flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow) to request the *access token*.