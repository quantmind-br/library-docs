---
title: Refreshing tokens | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens
source: crawler
fetched_at: 2026-02-27T23:45:38.614743-03:00
rendered_js: true
word_count: 382
summary: A guide explaining how to exchange a refresh token for a new access token using the Spotify OAuth 2.0 flow.
tags:
    - Spotify API
    - OAuth 2.0
    - authentication
    - refresh token
    - access token
category: guide
---

A refresh token is a security credential that allows client applications to obtain new access tokens without requiring users to reauthorize the application.

[Access tokens](https://developer.spotify.com/documentation/web-api/concepts/access-token) are intentionally configured to have a limited lifespan (1 hour), at the end of which, new tokens can be obtained by providing the original refresh token acquired during the authorization token request response:

`1`

`{`

`2`

`"access_token": "NgCXRK...MzYjw",`

`3`

`"token_type": "Bearer",`

`4`

`"scope": "user-read-private user-read-email",`

`5`

`"expires_in": 3600,`

`6`

`"refresh_token": "NgAagA...Um_SHo"`

`7`

`}`

## Request

To refresh an access token, we must send a `POST` request with the following parameters:

Body ParameterRelevanceValuegrant\_type*Required*Set it to `refresh_token`.refresh\_token*Required*The refresh token returned from the authorization token request.client\_id**Only required for the** [PKCE extension](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow)The client ID for your app, available from the developer dashboard.

And the following headers:

Header ParameterRelevanceValueContent-Type*Required*Always set to `application/x-www-form-urlencoded`.Authorization**Only required for the** [Authorization Code](https://developer.spotify.com/documentation/web-api/tutorials/code-flow)Base 64 encoded string that contains the client ID and client secret key. The field must have the format: `Authorization: Basic <base64 encoded client_id:client_secret>`

### Example

The following code snippets represent two examples:

- A client side (browser) JavaScript function to refresh tokens issued following the [Authorization Code with PKCE extension flow](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow).
- A server side (nodeJS with express) Javascript method to refresh tokens issued under the [Authorization Code flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow).

`1`

`const getRefreshToken = async () => {`

`2`

`3`

`// refresh token that has been previously stored`

`4`

`const refreshToken = localStorage.getItem('refresh_token');`

`5`

`const url = "https://accounts.spotify.com/api/token";`

`6`

`7`

`const payload = {`

`8`

`method: 'POST',`

`9`

`headers: {`

`10`

`'Content-Type': 'application/x-www-form-urlencoded'`

`11`

`},`

`12`

`body: new URLSearchParams({`

`13`

`grant_type: 'refresh_token',`

`14`

`refresh_token: refreshToken,`

`15`

`client_id: clientId`

`16`

`}),`

`17`

`}`

`18`

`const body = await fetch(url, payload);`

`19`

`const response = await body.json();`

`20`

`21`

`localStorage.setItem('access_token', response.access_token);`

`22`

`if (response.refresh_token) {`

`23`

`localStorage.setItem('refresh_token', response.refresh_token);`

`24`

`}`

`25`

`}`

## Response

If everything goes well, you'll receive a `200 OK` response which is very similar to the response when issuing an access token:

`1`

`{`

`2`

`access_token: 'BQBLuPRYBQ...BP8stIv5xr-Iwaf4l8eg',`

`3`

`token_type: 'Bearer',`

`4`

`expires_in: 3600,`

`5`

`refresh_token: 'AQAQfyEFmJJuCvAFh...cG_m-2KTgNDaDMQqjrOa3',`

`6`

`scope: 'user-read-email user-read-private'`

`7`

`}`

The refresh token contained in the response, can be used to request new tokens. Depending on the grant used to get the initial refresh token, a refresh token might not be included in each response. When a refresh token is not returned, continue using the existing token.