---
title: Client Credentials Flow | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow
source: crawler
fetched_at: 2026-02-27T23:38:07.42482-03:00
rendered_js: true
word_count: 324
summary: This document explains how to implement the Client Credentials flow for server-to-server authentication with the Spotify Web API. It details the necessary request parameters, headers, and expected response format to obtain an access token.
tags:
    - spotify-api
    - oauth2
    - client-credentials-flow
    - authentication
    - server-to-server
    - access-token
category: guide
---

The Client Credentials flow is used in server-to-server authentication. Since this flow does not include authorization, only endpoints that do not access user information can be accessed.

The following diagram shows how the *Client Credentials Flow* works:

![Client Credentials Flow](https://developer-assets.spotifycdn.com/images/documentation/web-api/auth-client-credentials.png)

#### Pre-requisites

This guide assumes that:

- You have read the [authorization guide](https://developer.spotify.com/documentation/web-api/concepts/authorization).
- You have created an app following the [app guide](https://developer.spotify.com/documentation/web-api/concepts/apps).

#### Source Code

You can find an example app implementing Client Credentials flow on GitHub in the [web-api-examples](https://github.com/spotify/web-api-examples/tree/master/authorization/client_credentials) repository.

The first step is to send a `POST` request to the `/api/token` endpoint of the *Spotify OAuth 2.0 Service* with the following parameters encoded in `application/x-www-form-urlencoded`:

Body ParametersRelevanceValuegrant\_type*Required*Set it to `client_credentials`.

The headers of the request must contain the following parameters:

Header ParameterRelevanceValueAuthorization*Required*Base 64 encoded string that contains the client ID and client secret key. The field must have the format: `Authorization: Basic <base64 encoded client_id:client_secret>`Content-Type*Required*Set to `application/x-www-form-urlencoded`.

The following JavaScript creates and sends an authorization request:

`1`

`var client_id = 'CLIENT_ID';`

`2`

`var client_secret = 'CLIENT_SECRET';`

`3`

`4`

`var authOptions = {`

`5`

`url: 'https://accounts.spotify.com/api/token',`

`6`

`headers: {`

`7`

`'Authorization': 'Basic ' + (new Buffer.from(client_id + ':' + client_secret).toString('base64'))`

`8`

`},`

`9`

`form: {`

`10`

`grant_type: 'client_credentials'`

`11`

`},`

`12`

`json: true`

`13`

`};`

`14`

`15`

`request.post(authOptions, function(error, response, body) {`

`16`

`if (!error && response.statusCode === 200) {`

`17`

`var token = body.access_token;`

`18`

`}`

`19`

`});`

### Response

If everything goes well, you'll receive a response with a `200 OK` status and the following JSON data in the response body:

keyTypeDescriptionaccess\_tokenstringAn access token that can be provided in subsequent calls, for example to Spotify Web API services.token\_typestringHow the access token may be used: always "Bearer".expires\_inintThe time period (in seconds) for which the access token is valid.

For example:

`1`

`{`

`2`

`"access_token": "NgCXRKc...MzYjw",`

`3`

`"token_type": "bearer",`

`4`

`"expires_in": 3600`

`5`

`}`

### What's next?

Learn how to use an access token to fetch data from the Spotify Web API by reading the [access token guide](https://developer.spotify.com/documentation/web-api/concepts/access-token).