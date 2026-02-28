---
title: 'Reminder: OAuth Migration - 27 November 2025'
url: https://developer.spotify.com/blog/2025-10-14-reminder-oauth-migration-27-nov-2025
source: crawler
fetched_at: 2026-02-27T23:42:04.817967-03:00
rendered_js: true
word_count: 386
summary: This document notifies developers of mandatory security updates to Spotify's OAuth system and provides instructions for migrating to secure authorization flows and redirect URIs.
tags:
    - oauth-migration
    - spotify-web-api
    - authentication
    - security-best-practices
    - authorization-code-flow
    - pkce
    - redirect-uris
category: guide
---

Reminder: OAuth Migration - 27 November 2025

Posted October 14, 2025

![](https://developer.spotify.com/images/avatars/spotify.png)

Spotify

**TL;DR:** As communicated in [February 2025](https://developer.spotify.com/blog/2025-02-12-increasing-the-security-requirements-for-integrating-with-spotify), Spotify will end support for the implicit grant flow, HTTP redirect URIs, and localhost aliases in their OAuth system. Existing apps must migrate to secure alternatives like Authorization Code Flow with PKCE and HTTPS redirect URIs to avoid service disruption.

On *27 November 2025*, Spotify will remove support for the *implicit grant flow*, as well as *HTTP redirect URIs* and *localhost aliases* in our OAuth offering.

## What’s changing

- The *implicit grant flow* will no longer be supported.
- *HTTP redirect URIs* will no longer be allowed.
- *Localhost aliases* (such as `localhost` or similar patterns) will be prohibited.

These changes align with industry best practices and are critical to protecting both Spotify users and partners.

## Who is affected

- *Existing applications* that still rely on implicit grant, HTTP redirect URIs, or localhost aliases must migrate before *27 November 2025*.
- *New applications* are already subject to these rules.

## What happens if you don’t migrate

If your app has not been updated by *27 November*, it will *stop working*. Requests relying on deprecated flows or redirect URIs will fail.

## How to migrate

We've published detailed migration guides [here](https://developer.spotify.com/documentation/web-api/tutorials/migration-implicit-auth-code) and [here](https://developer.spotify.com/documentation/web-api/tutorials/migration-insecure-redirect-uri). These cover supported OAuth flows and provides step-by-step instructions for updating redirect URIs.

## ✅ Quick migration checklist

- Stop using *implicit grant flow*. Switch to Authorization Code Flow with PKCE or another supported flow.
- Replace all *HTTP redirect URIs* with HTTPS equivalents.
- Remove any *localhost aliases* (e.g. `localhost`) from your redirect URIs. You can still use local IP addresses like `http://127.0.0.1`.
- Test your app thoroughly to confirm the new configuration works as expected.

## FAQ

### Why is http:// no longer supported for production apps?

Allowing `http://` redirect URIs in production apps poses security risks such as token interception. All production apps must use HTTPS redirect URIs.

### What if I don’t update my redirect URIs in time?

Any requests using `http://` or localhost aliases will fail after 27 November 2025, causing your app to stop working.

No. If you’re already using HTTPS redirect URIs and a supported flow (e.g. Authorization Code or PKCE), you’re compliant and no further action is required.

## Need help?

If you encounter issues, the [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer) is the best place to get support from both the Spotify team and other developers.