---
title: Implicit Grant Flow | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/tutorials/implicit-flow
source: crawler
fetched_at: 2026-02-27T23:45:38.687562-03:00
rendered_js: true
word_count: 652
summary: This document explains the Spotify Implicit Grant flow, a client-side authorization method that allows applications to obtain access tokens without server-side code. It details the steps for constructing authorization requests, handling user redirects, and processing the resulting access tokens.
tags:
    - oauth2
    - implicit-grant
    - spotify-api
    - authorization
    - access-token
    - client-side
    - javascript
category: guide
---

The implicit grant flow is carried out on the client side and it does not involve secret keys. Thus, you do not need any server-side code to use it. Access tokens issued are short-lived with no refresh token to extend them when they expire.

The following diagram shows how the *Implicit Grant Flow* works:

![Implicit Grant](https://developer-assets.spotifycdn.com/images/documentation/web-api/auth-implicit-grant.png)

#### Pre-requisites

This guide assumes that:

- You have read the [authorization guide](https://developer.spotify.com/documentation/web-api/concepts/authorization).
- You have created an app following the [app guide](https://developer.spotify.com/documentation/web-api/concepts/apps).

#### Source Code

You can find an example app implementing Implicit Grant flow on GitHub in the [web-api-examples](https://github.com/spotify/web-api-examples/tree/master/authorization/implicit_grant) repository.

Our application must build a `GET` request to the `/authorize` endpoint with the following parameters:

Query ParameterRelevanceValueclient\_id*Required*The client ID provided to you by Spotify when you register your application.response\_type*Required*Set it to `token`.redirect\_uri*Required*The URI to redirect to after the user grants or denies permission. This URI needs to have been entered in the Redirect URI allowlist that you specified when you registered your application (See the [app guide](https://developer.spotify.com/documentation/web-api/concepts/apps)). The value of `redirect_uri` here must exactly match one of the values you entered when you registered your application, including upper or lowercase, terminating slashes, and such.state*Optional,* but strongly recommended.The state can be useful for correlating requests and responses. Because your `redirect_uri` can be guessed, using a state value can increase your assurance that an incoming connection is the result of an authentication request. If you generate a random string or encode the hash of some client state (e.g., a cookie) in this state variable, you can validate the response to additionally ensure that the request and response originated in the same browser. This provides protection against attacks such as cross-site request forgery. See [RFC-6749](https://datatracker.ietf.org/doc/html/rfc6749#section-10.12).scope*Optional*A space-separated list of [scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes).show\_dialog*Optional*Whether or not to force the user to approve the app again if they’ve already done so. If false (default), a user who has already approved the application may be automatically redirected to the URI specified by `redirect_uri`. If true, the user will not be automatically redirected and will have to approve the app again.

The request is typically sent from the browser.

The following JavaScript sample builds the authorization request:

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

Once the request is processed, the user will see the authorization dialog asking to authorize access within the scopes.

The Spotify Accounts service presents details of the [scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes) for which access is being sought. If the user is not logged in, they are prompted to do so using their Spotify credentials. When the user is logged in, they are asked to authorize access to the resources or actions defined in the scopes.

Finally, the user is redirected back to your specified `redirect_uri`. After the user accepts, or denies your request, the Spotify OAuth 2.0 server redirects the user back to your `redirect_uri`. In this example, the redirect address is `https://127.0.0.1:8888/callback`

### Response

If the user grants access, the final URL will contain a *hash fragment* with the following data encoded as a query string.

Query ParameterValueaccess\_tokenAn access token that can be provided in subsequent calls, for example to Spotify Web API services.token\_typeValue: "Bearer"expires\_inThe time period (in seconds) for which the access token is valid.stateThe value of the state parameter supplied in authorization URI.

For example:

`1`

`https://example.com/callback#access_token=NwAExz...BV3O2Tk&token_type=Bearer&expires_in=3600&state=123`

If the user denies access, access token is not included and the final URL includes a query string containing the following parameters:

Query ParameterValueerrorThe reason authorization failed, for example: "access\_denied".stateThe value of the state parameter supplied in the request.

For example:

`1`

`https://example.com/callback?error=access_denied&state=123`

### What's next?

Learn how to use an access token to fetch data from the Spotify Web API by reading the [access token guide](https://developer.spotify.com/documentation/web-api/concepts/access-token).