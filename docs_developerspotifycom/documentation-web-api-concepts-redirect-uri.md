---
title: Redirect URIs | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/concepts/redirect_uri
source: crawler
fetched_at: 2026-02-27T23:38:15.202256-03:00
rendered_js: true
word_count: 247
summary: This document defines the security requirements and configuration rules for redirect URIs used in Spotify app authorization flows. It explains protocol requirements, loopback address constraints, and dynamic port assignment for developers.
tags:
    - spotify-api
    - redirect-uri
    - authentication
    - oauth2
    - security-requirements
    - loopback-address
category: configuration
---

When you create an app, you need to specify a redirect URI. This is the URI to which Spotify redirects the user after they have granted or denied permission to your app. The redirect URI is required for the authorization code flow and implicit grant flow. The definition of the redirect URI must exactly match the redirect URI you provide when you create your app. The only exception is for loopback IP literals, which can dynamically be assigned ports.

## Requirements

Since we at Spotify, take security very seriously you must follow these requirements when defining your redirect URI:

- Use HTTPS for your redirect URI, unless you are using a loopback address, when HTTP is permitted.
- If you are using a loopback address, use the explicit IPv4 or IPv6, like `http://127.0.0.1:PORT` or `http://[::1]:PORT` as your redirect URI.
- `localhost` is not allowed as redirect URI.

### Loopback addresses and port numbers

When using a loopback IP literal, you might not know the port number used in advance if it can be assigned dynamically. If you don't know the port number in advance, register your redirect URI with a loopback IP literal, but without any port number. You can add the dynamically assigned port number to the redirect URI in the authorization request. Please note that this is only supported for loopback IP literals, and not for other redirect URIs. This is on-par with the [IETF recommendations](https://www.rfc-editor.org/rfc/rfc8252.html#section-7.3).

## Examples

Here are some examples of redirect URIs:

`1`

`https://example.com/callback`

`2`

`http://127.0.0.1:8000/callback`

`3`

`http://[::1]:8000/callback`