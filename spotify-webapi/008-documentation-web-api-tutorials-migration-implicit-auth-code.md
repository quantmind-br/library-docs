---
title: Migrate from Implicit Grant Flow to Authorization Code with PKCE
url: https://developer.spotify.com/documentation/web-api/tutorials/migration-implicit-auth-code
source: crawler
fetched_at: 2026-02-27T23:45:41.546538-03:00
rendered_js: true
word_count: 518
summary: This guide provides instructions for migrating a Web Application from the deprecated Implicit Grant Flow to the Authorization Code with PKCE flow for the Spotify Web API.
tags:
    - spotify-web-api
    - oauth-2-0
    - pkce
    - migration-guide
    - authentication
    - web-apps
category: guide
---

Since we are deprecating the Implicit Grant Flow, you should migrate your application to use the Authorization Code with PKCE flow. This guide will help you migrate complete the migration for a Web Application.

## Prerequisites

This guide assumes that:

- You have read the [authorization guide](https://developer.spotify.com/documentation/web-api/concepts/authorization).
- You have created an app following the [app guide](https://developer.spotify.com/documentation/web-api/concepts/apps).
- You have read the [Authorization Code with PKCE](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow) guide.

### Step 1: Update your app to use Authorization Code with PKCE

The first step of this migration is to find the code that calls the `/authorize` endpoint with the `token` response type. You should replace the `token` response type with `code` and add the `code_challenge` and `code_challenge_method` parameters.

For instance, let's say you have the following code:

`1`

`var client_id = 'CLIENT_ID';`

`2`

`var redirect_uri = 'http://127.0.0.1:8888/callback';`

`3`

`4`

`var state = generateRandomString(16);`

`5`

`6`

`localStorage.setItem(stateKey, state);`

`7`

`var scope = 'user-read-private user-read-email';`

`8`

`9`

`var url = 'https://accounts.spotify.com/authorize';`

`10`

`url += '?response_type=token';`

`11`

`url += '&client_id=' + encodeURIComponent(client_id);`

`12`

`url += '&scope=' + encodeURIComponent(scope);`

`13`

`url += '&redirect_uri=' + encodeURIComponent(redirect_uri);`

`14`

`url += '&state=' + encodeURIComponent(state);`

you need to update it to:

`1`

`const clientId = 'YOUR_CLIENT_ID';`

`2`

`const redirectUri = 'http://127.0.0.1:8080';`

`3`

`4`

`const scope = 'user-read-private user-read-email';`

`5`

`const authUrl = new URL("https://accounts.spotify.com/authorize")`

`6`

`7`

`// generated in the previous step`

`8`

`window.localStorage.setItem('code_verifier', codeVerifier);`

`9`

`10`

`const params = {`

`11`

`response_type: 'code',`

`12`

`client_id: clientId,`

`13`

`scope,`

`14`

`code_challenge_method: 'S256',`

`15`

`code_challenge: codeChallenge,`

`16`

`redirect_uri: redirectUri`

`17`

`}`

`18`

`19`

`authUrl.search = new URLSearchParams(params).toString();`

`20`

`window.location.href = authUrl.toString();`

As you can see there is quite a difference between the two code snippets. The new code snippet generates a PKCE code challenge and redirects to the Spotify authorization server login page by updating the `window.location` object value. If you are not familiar with PKCE, you can read more about it in the [Authorization Code with PKCE](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow) guide.

### Step 2: Handle the authorization code

After the user grants permissions to your application, the Spotify authorization server will redirect the user back to the URL specified in the `redirect_uri` field. This is similar to the Implicit Grant Flow, but the response will contain an `authorization code` instead of an `access token`.

Now you need to exchange the `authorization code` for an `access token`. To do this, you need to parse the URL to retrieve the `code` parameter:

`1`

`const urlParams = new URLSearchParams(window.location.search);`

`2`

`let code = urlParams.get('code');`

The `code` will be necessary to request the access token in the next step.

### Step 3: Request the access token (and refresh token)

The last step is to request the access token using the `authorization code` you received in the previous step. You can follow the steps in the [Authorization Code with PKCE](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow) guide to request the access token.

Bear in mind that the `access token` you receive will have a refresh token. This means that if the `access token` expires, you can use the `refresh token` to get a new `access token` without doing the whole authorization process again. If you want to know more about refresh tokens, you can read the [refresh token guide](https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens).