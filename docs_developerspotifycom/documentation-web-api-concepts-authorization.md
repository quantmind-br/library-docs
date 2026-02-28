---
title: Authorization | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/concepts/authorization
source: crawler
fetched_at: 2026-02-27T23:37:53.604959-03:00
rendered_js: true
word_count: 417
summary: This document provides an overview of Spotify's OAuth 2.0 authorization framework and explains how applications can obtain permissions to access user data. It outlines the various authorization flows available and guides developers in choosing the most appropriate one for their application architecture.
tags:
    - spotify-api
    - oauth-2-0
    - authorization
    - access-token
    - scopes
    - pkce
    - grant-types
category: concept
---

Authorization refers to the process of granting a user or application access permissions to Spotify data and features (e.g your application needs permission from a user to access their playlists).

Spotify implements the [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) authorization framework:

![Auth Intro](https://developer-assets.spotifycdn.com/images/documentation/web-api/auth_intro.png)

Where:

- *End User* corresponds to the Spotify user. The *End User* grants access to the protected resources (e.g. playlists, personal information, etc.)
- *My App* is the client that requests access to the protected resources (e.g. a mobile or web app).
- *Server* which hosts the protected resources and provides authentication and authorization via OAuth 2.0.

The access to the protected resources is determined by one or several *scopes*. Scopes enable your application to access specific functionality (e.g. read a playlist, modify your library or just streaming) on behalf of a user. The set of scopes you set during the authorization, determines the access permissions that the user is asked to grant. You can find detailed information about scopes in the [scopes documentation](https://developer.spotify.com/documentation/web-api/concepts/scopes).

The authorization process requires valid *client credentials*: a client ID and a client secret. You can follow the [Apps guide](https://developer.spotify.com/documentation/web-api/concepts/apps) to learn how to generate them.

Once the authorization is granted, the authorization server issues an access token, which is used to make API calls on behalf the user or application.

The OAuth2 standard defines four grant types (or flows) to request and get an access token. Spotify implements the following ones:

- [Authorization code](https://developer.spotify.com/documentation/web-api/tutorials/code-flow)
- [Authorization code with PKCE extension](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow)
- [Client credentials](https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow)

### Which OAuth flow should I use?

Choosing one flow over the rest depends on the application you are building:

- If you are developing a long-running application (e.g. web app running on the server) in which the user grants permission only once, and the client secret can be safely stored, then the [authorization code flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow) is the recommended choice.
- In scenarios where storing the client secret is not safe (e.g. desktop, mobile apps or JavaScript web apps running in the browser), you can use the [authorization code with PKCE](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow), as it provides protection against attacks where the authorization code may be intercepted.
- For some applications running on the backend, such as CLIs or daemons, the system authenticates and authorizes the app rather than a user. For these scenarios, [Client credentials](https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow) is the typical choice. This flow does not include user authorization, so only endpoints that do not request user information (e.g. user profile data) can be accessed.

The following table summarizes the flows' behaviors:

FLOWAccess User ResourcesRequires Secret Key (Server-Side)Access Token RefreshAuthorization codeYesYesYesAuthorization code with PKCEYesNoYesClient credentialsNoYesNo