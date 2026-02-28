---
title: Authorization Code Flow | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/tutorials/code-flow
source: crawler
fetched_at: 2026-02-27T23:45:30.566027-03:00
rendered_js: true
word_count: 1044
summary: This document explains how to implement the OAuth 2.0 authorization code flow to obtain user authorization and access tokens for long-running applications using the Spotify Web API.
tags:
    - oauth2
    - authorization-code-flow
    - spotify-web-api
    - authentication
    - access-token
    - pkce
category: guide
---

The authorization code flow is suitable for long-running applications (e.g. web and mobile apps) where the user grants permission only once.

If you’re using the authorization code flow in a mobile app, or any other type of application where the client secret can't be safely stored, then you should use the PKCE extension. Keep reading to learn how to correctly implement it.

The following diagram shows how the *authorization code flow* works:

![Authorization Code Flow](https://developer-assets.spotifycdn.com/images/documentation/web-api/auth-code-flow.png)

#### Pre-requisites

This guide assumes that:

- You have read the [authorization guide](https://developer.spotify.com/documentation/web-api/concepts/authorization).
- You have created an app following the [apps guide](https://developer.spotify.com/documentation/web-api/concepts/apps).

#### Example

You can find an example app implementing Authorization Code flow on GitHub in the [web-api-examples](https://github.com/spotify/web-api-examples/tree/master/authorization/authorization_code) repository.

The first step is to request authorization from the user so that our app can access to the Spotify resources on the user's behalf. To do this, our application must build and send a `GET` request to the `/authorize` endpoint with the following parameters:

Query ParameterRelevanceValueclient\_id*Required*The Client ID generated after registering your application.response\_type*Required*Set to `code`.redirect\_uri*Required*The URI to redirect to after the user grants or denies permission. This URI needs to have been entered in the Redirect URI allowlist that you specified when you registered your application (See the [app guide](https://developer.spotify.com/documentation/web-api/concepts/apps)). The value of `redirect_uri` here must exactly match one of the values you entered when you registered your application, including upper or lowercase, terminating slashes, and such.state*Optional, but strongly recommended*This provides protection against attacks such as cross-site request forgery. See [RFC-6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1).scope*Optional*A space-separated list of [scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes).If no scopes are specified, authorization will be granted only to access publicly available information: that is, only information normally visible in the Spotify desktop, web, and mobile players.show\_dialog*Optional*Whether or not to force the user to approve the app again if they’ve already done so. If `false` (default), a user who has already approved the application may be automatically redirected to the URI specified by `redirect_uri`. If `true`, the user will not be automatically redirected and will have to approve the app again.

The following JavaScript code example implements the `/login` method using [Express](https://expressjs.com/) framework to initiates the authorization request:

`1`

`var client_id = 'CLIENT_ID';`

`2`

`var redirect_uri = 'http://127.0.0.1:8888/callback';`

`3`

`4`

`var app = express();`

`5`

`6`

`app.get('/login', function(req, res) {`

`7`

`8`

`var state = generateRandomString(16);`

`9`

`var scope = 'user-read-private user-read-email';`

`10`

`11`

`res.redirect('https://accounts.spotify.com/authorize?' +`

`12`

`querystring.stringify({`

`13`

`response_type: 'code',`

`14`

`client_id: client_id,`

`15`

`scope: scope,`

`16`

`redirect_uri: redirect_uri,`

`17`

`state: state`

`18`

`}));`

`19`

`});`

Once the request is processed, the user will see the authorization dialog asking to authorize access within the `user-read-private` and `user-read-email` scopes.

The Spotify OAuth 2.0 service presents details of the [scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes) for which access is being sought. If the user is not logged in, they are prompted to do so using their Spotify credentials. When the user is logged in, they are asked to authorize access to the data sets or features defined in the scopes.

Finally, the user is redirected back to your specified `redirect_uri`. After the user accepts, or denies your request, the Spotify OAuth 2.0 service redirects the user back to your `redirect_uri`. In this example, the redirect address is `https://127.0.0.1:8888/callback`

#### Response

If the user accepts your request, then the user is redirected back to the application using the `redirect_uri` passed on the authorized request described above.

The callback contains two query parameters:

Query ParameterValuecodeAn authorization code that can be exchanged for an access token.stateThe value of the `state` parameter supplied in the request.

For example:

`1`

`https://my-domain.com/callback?code=NApCCg..BkWtQ&state=34fFs29kd09`

If the user does not accept your request or if an error has occurred, the response query string contains the following parameters:

Query ParameterValueerrorThe reason authorization failed, for example: "access\_denied"stateThe value of the `state` parameter supplied in the request.

For example:

`1`

`https://my-domain.com/callback?error=access_denied&state=34fFs29kd09`

In both cases, your app should compare the `state` parameter that it received in the redirection URI with the state parameter it originally provided to Spotify in the authorization URI. If there is a mismatch then your app should reject the request and stop the authentication flow.

## Request an access token

If the user accepted your request, then your app is ready to exchange the authorization code for an access token. It can do this by sending a `POST` request to the `/api/token` endpoint.

The body of this `POST` request must contain the following parameters encoded in `application/x-www-form-urlencoded`:

Body ParametersRelevanceValuegrant\_type*Required*This field must contain the value `"authorization_code"`.code*Required*The authorization code returned from the previous request.redirect\_uri*Required*This parameter is used for validation only (there is no actual redirection). The value of this parameter must exactly match the value of `redirect_uri` supplied when requesting the authorization code.

The request must include the following HTTP headers:

Header ParameterRelevanceValueAuthorization*Required*Base 64 encoded string that contains the client ID and client secret key. The field must have the format: `Authorization: Basic <base64 encoded client_id:client_secret>`Content-Type*Required*Set to `application/x-www-form-urlencoded`.

This step is usually implemented within the callback described on the request of the previous steps:

`1`

`app.get('/callback', function(req, res) {`

`2`

`3`

`var code = req.query.code || null;`

`4`

`var state = req.query.state || null;`

`5`

`6`

`if (state === null) {`

`7`

`res.redirect('/#' +`

`8`

`querystring.stringify({`

`9`

`error: 'state_mismatch'`

`10`

`}));`

`11`

`} else {`

`12`

`var authOptions = {`

`13`

`url: 'https://accounts.spotify.com/api/token',`

`14`

`form: {`

`15`

`code: code,`

`16`

`redirect_uri: redirect_uri,`

`17`

`grant_type: 'authorization_code'`

`18`

`},`

`19`

`headers: {`

`20`

`'content-type': 'application/x-www-form-urlencoded',`

`21`

`'Authorization': 'Basic ' + (new Buffer.from(client_id + ':' + client_secret).toString('base64'))`

`22`

`},`

`23`

`json: true`

`24`

`};`

`25`

`}`

`26`

`});`

### Response

On success, the response will have a `200 OK` status and the following JSON data in the response body:

keyTypeDescriptionaccess\_tokenstringAn access token that can be provided in subsequent calls, for example to Spotify Web API services.token\_typestringHow the access token may be used: always "Bearer".scopestringA space-separated list of scopes which have been granted for this `access_token`expires\_inintThe time period (in seconds) for which the access token is valid.refresh\_tokenstringSee [refreshing tokens](https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens).

### What's next?

- Congratulations! Your fresh access token is ready to be used! How can we make API calls with it? take a look at to the [access token](https://developer.spotify.com/documentation/web-api/concepts/access-token) guide to learn how to make an API call using your new fresh access token.
- If your access token has expired, you can learn how to issue a new one without requiring users to reauthorize your application by reading the [refresh token](https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens) guide.