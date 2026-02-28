---
title: Authorization Code with PKCE Flow
url: https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow
source: crawler
fetched_at: 2026-02-27T23:38:04.117677-03:00
rendered_js: true
word_count: 1152
summary: Explains the implementation of the OAuth 2.0 authorization code flow with PKCE for applications that cannot securely store a client secret, such as mobile or single-page apps.
tags:
    - oauth2
    - pkce
    - spotify-api
    - authorization-flow
    - security
    - authentication
category: tutorial
---

The authorization code flow with PKCE is the recommended authorization flow if you’re implementing authorization in a mobile app, single page web apps, or any other type of application where the client secret can’t be safely stored.

The implementation of the PKCE extension consists of the following steps:

- [Code Challenge](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow#code-challenge) generation from a [Code Verifier](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow#code-verifier).
- [Request authorization](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow#request-user-authorization) from the user and retrieve the authorization code.
- [Request an access token](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow#request-an-access-token) from the authorization code.
- Finally, use the access token to make API calls.

#### Pre-requisites

This guide assumes that:

- You have read the [authorization guide](https://developer.spotify.com/documentation/web-api/concepts/authorization).
- You have created an app following the [apps guide](https://developer.spotify.com/documentation/web-api/concepts/apps).

#### Example

You can find an example app implementing Authorization Code flow with PKCE extension on GitHub in the [web-api-examples](https://github.com/spotify/web-api-examples/tree/master/authorization/authorization_code_pkce) repository.

## Code Verifier

The PKCE authorization flow starts with the creation of a code verifier. According to the [PKCE standard](https://datatracker.ietf.org/doc/html/rfc7636#section-4.1), a code verifier is a high-entropy cryptographic random string with a length between 43 and 128 characters (the longer the better). It can contain letters, digits, underscores, periods, hyphens, or tildes.

The code verifier could be implemented using the following JavaScript function:

`1`

`const generateRandomString = (length) => {`

`2`

`const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';`

`3`

`const values = crypto.getRandomValues(new Uint8Array(length));`

`4`

`return values.reduce((acc, x) => acc + possible[x % possible.length], "");`

`5`

`}`

`6`

`7`

`const codeVerifier = generateRandomString(64);`

## Code Challenge

Once the code verifier has been generated, we must transform (hash) it using the SHA256 algorithm. This is the value that will be sent within the user authorization request.

Let's use [window.crypto.subtle.digest](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest) to generate the value using the SHA256 algorithm from the given data:

`1`

`const sha256 = async (plain) => {`

`2`

`const encoder = new TextEncoder()`

`3`

`const data = encoder.encode(plain)`

`4`

`return window.crypto.subtle.digest('SHA-256', data)`

`5`

`}`

Next, we will implement a function `base64encode` that returns the `base64` representation of the digest we just calculated with the `sha256` function:

`1`

`const base64encode = (input) => {`

`2`

`return btoa(String.fromCharCode(...new Uint8Array(input)))`

`3`

`.replace(/=/g, '')`

`4`

`.replace(/\+/g, '-')`

`5`

`.replace(/\//g, '_');`

`6`

`}`

Let's put all the pieces together to implement the code challenge generation:

`1`

`const hashed = await sha256(codeVerifier)`

`2`

`const codeChallenge = base64encode(hashed);`

To request authorization from the user, a `GET` request must be made to the `/authorize` endpoint. This request should include the same parameters as the [authorization code flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow), along with two additional parameters: `code_challenge` and `code_challenge_method`:

Query ParameterRelevanceValueclient\_id*Required*The Client ID generated after registering your application.response\_type*Required*Set to `code`.redirect\_uri*Required*The URI to redirect to after the user grants or denies permission. This URI needs to have been entered in the Redirect URI allowlist that you specified when you registered your application (See the [app guide](https://developer.spotify.com/documentation/web-api/concepts/apps)). The value of `redirect_uri` here must exactly match one of the values you entered when you registered your application, including upper or lowercase, terminating slashes, and such.state*Optional, but strongly recommended*This provides protection against attacks such as cross-site request forgery. See [RFC-6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1).scope*Optional*A space-separated list of [scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes). If no scopes are specified, authorization will be granted only to access publicly available information: that is, only information normally visible in the Spotify desktop, web, and mobile players.code\_challenge\_method*Required*Set to `S256`.code\_challenge*Required*Set to the code challenge that your app calculated in the previous step.

The code for requesting user authorization looks as follows:

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

`redirect_uri: redirectUri,`

`17`

`}`

`18`

`19`

`authUrl.search = new URLSearchParams(params).toString();`

`20`

`window.location.href = authUrl.toString();`

The app generates a PKCE code challenge and redirects to the Spotify authorization server login page by updating the `window.location` object value. This allows the user to grant permissions to our application

Please note that the code verifier value is stored locally using the `localStorage` JavaScript property for use in the next step of the authorization flow.

### Response

If the user accepts the requested permissions, the OAuth service redirects the user back to the URL specified in the `redirect_uri` field. This callback contains two query parameters within the URL:

Query ParameterValuecodeAn authorization code that can be exchanged for an access token.stateThe value of the `state` parameter supplied in the request.

We must then parse the URL to retrieve the `code` parameter:

`1`

`const urlParams = new URLSearchParams(window.location.search);`

`2`

`let code = urlParams.get('code');`

The `code` will be necessary to request the access token in the next step.

If the user does not accept your request or if an error has occurred, the response query string contains the following parameters:

Query ParameterValueerrorThe reason authorization failed, for example: "access\_denied"stateThe value of the `state` parameter supplied in the request.

## Request an access token

After the user accepts the authorization request of the previous step, we can exchange the authorization code for an access token. We must send a `POST` request to the `/api/token` endpoint with the following parameters:

Body ParametersRelevanceValuegrant\_type*Required*This field must contain the value `authorization_code`.code*Required*The authorization code returned from the previous request.redirect\_uri*Required*This parameter is used for validation only (there is no actual redirection). The value of this parameter must exactly match the value of `redirect_uri` supplied when requesting the authorization code.client\_id*Required*The client ID for your app, available from the developer dashboard.code\_verifier*Required*The value of this parameter must match the value of the `code_verifier` that your app generated in the previous step.

The request must include the following HTTP header:

Header ParameterRelevanceValueContent-Type*Required*Set to `application/x-www-form-urlencoded`.

The request of the token could be implemented with the following JavaScript function:

`1`

`const getToken = async code => {`

`2`

`3`

`// stored in the previous step`

`4`

`const codeVerifier = localStorage.getItem('code_verifier');`

`5`

`6`

`const url = "https://accounts.spotify.com/api/token";`

`7`

`const payload = {`

`8`

`method: 'POST',`

`9`

`headers: {`

`10`

`'Content-Type': 'application/x-www-form-urlencoded',`

`11`

`},`

`12`

`body: new URLSearchParams({`

`13`

`client_id: clientId,`

`14`

`grant_type: 'authorization_code',`

`15`

`code,`

`16`

`redirect_uri: redirectUri,`

`17`

`code_verifier: codeVerifier,`

`18`

`}),`

`19`

`}`

`20`

`21`

`const body = await fetch(url, payload);`

`22`

`const response = await body.json();`

`23`

`24`

`localStorage.setItem('access_token', response.access_token);`

`25`

`}`

### Response

On success, the response will have a `200 OK` status and the following JSON data in the response body:

keyTypeDescriptionaccess\_tokenstringAn access token that can be provided in subsequent calls, for example to Spotify Web API services.token\_typestringHow the access token may be used: always "Bearer".scopestringA space-separated list of scopes which have been granted for this `access_token`expires\_inintThe time period (in seconds) for which the access token is valid.refresh\_tokenstringSee [refreshing tokens](https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens).

### What's next?

- Great! We have the access token. Now you might be wondering: *what do I do with it?* Take a look at to the [access token](https://developer.spotify.com/documentation/web-api/concepts/access-token) guide to learn how to make an API call using your new fresh access token.
- If your access token has expired, you can learn how to issue a new one without requiring users to reauthorize your application by reading the [refresh token](https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens) guide.