---
title: Android Content Linking | Spotify for Developers
url: https://developer.spotify.com/documentation/android/tutorials/content-linking
source: crawler
fetched_at: 2026-02-27T23:42:00.502648-03:00
rendered_js: true
word_count: 494
summary: This guide explains how to integrate Spotify content linking in Android applications, including app detection, deeplink implementation, and installation fallbacks.
tags:
    - android
    - spotify-api
    - deeplinking
    - content-linking
    - app-detection
    - mobile-development
category: tutorial
---

This tutorial covers content linking for Android devices, where it is possible to detect Spotify.

The Spotify app registers the `spotify:` [URI scheme](https://www.iana.org/assignments/uri-schemes/prov/spotify) for handling deeplinks. These URIs are found in entities returned from the Spotify Web API under the uri field. For example, the [get album](https://developer.spotify.com/documentation/web-api/reference/get-an-album) endpoint returns:

`1`

`{`

`2`

`"name": "This Is All Yours",`

`3`

`"release_date": "2014-09-22",`

`4`

`"release_date_precision": "day",`

`5`

`"type": "album",`

`6`

`"uri": "spotify:album:4oktVvRuO1In9B7Hz0xm0a"`

`7`

`}`

When Spotify is installed, navigating directly to content in the Spotify app provides the best user experience, since it brings Spotify to the foreground with the selected content. However, you must first determine whether Spotify is present on the device.

## Detecting Spotify

Use `getPackageInfo` on the [PackageManager class](https://developer.android.com/reference/android/content/pm/PackageManager.html) to determine if Spotify is installed. The Spotify app for Android uses the package name `com.spotify.music`.

Example:

`1`

`PackageManager pm = getPackageManager();`

`2`

`boolean isSpotifyInstalled;`

`3`

`try {`

`4`

`pm.getPackageInfo("com.spotify.music", 0);`

`5`

`isSpotifyInstalled = true;`

`6`

`} catch (PackageManager.NameNotFoundException e) {`

`7`

`isSpotifyInstalled = false;`

`8`

`}`

## Opening Spotify content in the Spotify app

Once you've determined Spotify is installed, you can navigate directly to Spotify deeplinks.

Start an activity for an `ACTION_VIEW` Intent, passing your app's package name in the `EXTRA_REFERRER` field.

Example:

`1`

`final String spotifyContent = "https://open.spotify.com/album/0sNOF9WDwhWunNAHPD3Baj";`

`2`

`final String branchLink = "https://spotify.link/content_linking?~campaign=" + context.getPackageName() + "&$deeplink_path=" + spotifyContent + "&$fallback_url=" + spotifyContent;`

`3`

`Intent intent = new Intent(Intent.ACTION_VIEW);`

`4`

`intent.setData(Uri.parse(branchLink));`

`5`

`startActivity(intent);`

## Installing Spotify

Follow the steps below if you wish to link users directly to the app store so that they can install Spotify. Spotify partners with [Branch](https://www.branch.io/) for mobile install attribution.

Open Spotify in the Google Play Store, passing your application's package name in the `~campaign` parameter of the `_branch_link` in the `referrer`:

`1`

`final String branchLink = Uri.encode("https://spotify.link/content_linking?~campaign=" + context.getPackageName());`

`2`

`final String appPackageName = "com.spotify.music";`

`3`

`final String referrer = "_branch_link=" + branchLink;`

`4`

`5`

`try {`

`6`

`Uri uri = Uri.parse("market://details")`

`7`

`.buildUpon()`

`8`

`.appendQueryParameter("id", appPackageName)`

`9`

`.appendQueryParameter("referrer", referrer)`

`10`

`.build();`

`11`

`startActivity(new Intent(Intent.ACTION_VIEW, uri));`

`12`

`} catch (android.content.ActivityNotFoundException ignored) {`

`13`

`Uri uri = Uri.parse("https://play.google.com/store/apps/details")`

`14`

`.buildUpon()`

`15`

`.appendQueryParameter("id", appPackageName)`

`16`

`.appendQueryParameter("referrer", referrer)`

`17`

`.build();`

`18`

`startActivity(new Intent(Intent.ACTION_VIEW, uri));`

`19`

`}`

## Fallback experience: Web Links

If the user doesn’t have Spotify installed or you’re otherwise unable to detect Spotify, you should open Spotify web links (open.spotify.com) in the system browser or a webview.

Web links are provided in Web API entities under the `external_urls.spotify` field.

`1`

`{`

`2`

`"name": "She's So Unusual",`

`3`

`"type": "album",`

`4`

`...`

`5`

`"external_urls" : {`

`6`

`"spotify" : "https://open.spotify.com/album/0sNOF9WDwhWunNAHPD3Baj"`

`7`

`}`

`8`

`}`

## Attribution

In order for Spotify to attribute traffic to your app, pass your application's package name in the `utm_campaign` query string parameter. For example: `https://open.spotify.com/track/55fmthmn3rgnk9Wyx7G5dU?utm_campaign=com.app`

## Allow deeplinking from Webviews

Content at `open.spotify.com` links directly into Spotify or the app store. By default, Android restricts webviews and prevent deeplinking into apps.

Support deeplinks by ensuring the webview handles the following schemes:

- `spotify:`
- `market:`

## Further read

Android: [https://stackoverflow.com/a/20134598](https://stackoverflow.com/a/20134598)