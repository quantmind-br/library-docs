---
title: iOS Content Linking | Spotify for Developers
url: https://developer.spotify.com/documentation/ios/tutorials/content-linking
source: crawler
fetched_at: 2026-02-27T23:40:52.998942-03:00
rendered_js: true
word_count: 582
summary: This tutorial explains how to detect the Spotify app on iOS and implement content linking using URI schemes and Universal Links. It provides instructions for deep linking to content, handling app installation, and implementing web-based fallbacks.
tags:
    - ios
    - spotify-api
    - deeplinking
    - universal-links
    - app-detection
    - mobile-development
category: tutorial
---

This tutorial covers content linking for iOS devices, where it is possible to detect Spotify.

The Spotify app registers the `spotify:` [URI scheme](https://www.iana.org/assignments/uri-schemes/prov/spotify) to handle deeplinks. These URIs are found in entities returned from the Spotify Web API under the uri field. For example, the [get album](https://developer.spotify.com/documentation/web-api/reference/get-an-album) endpoint returns:

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

Your app must declare its intent to detect Spotify. Add `spotify` under the `LSApplicationQueriesSchemes` key in your project’s `Info.plist`:

`1`

`<?xml version="1.0" encoding="UTF-8"?>`

`2`

`<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">`

`3`

`<plist version="1.0">`

`4`

`<dict>`

`5`

`...`

`6`

`<key>LSApplicationQueriesSchemes</key>`

`7`

`<array>`

`8`

`<string>spotify</string>`

`9`

`...`

`10`

`</array>`

`11`

`...`

`12`

`</dict>`

`13`

`</plist>`

Pass a Spotify URI to `canOpenURL` on the [UIApplication](https://developer.apple.com/documentation/uikit/uiapplication/) class to determine if Spotify is installed:

`1`

`[[UIApplication sharedApplication] canOpenURL:[NSURL URLWithString:@"spotify:"]]`

## Opening Spotify content in the Spotify app

Once you've determined Spotify is installed, you can navigate directly to Spotify deeplinks.

Pass a Spotify web link to the `openURL` method of the [UIApplication class](https://developer.apple.com/documentation/uikit/uiapplication/) to open the content in the Spotify app. Start with passing your app’s Bundle ID in the `~campaign` parameter. Append the Spotify Content link to the `~$canonical_url` parameter to ensure proper routing and user experience. A web link is preferred over a `spotify:` deeplink in this scenario because a deeplink will trigger an iOS confirmation prompt before switching to Spotify. Spotify handles the web link through the [Universal Links](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html#/apple_ref/doc/uid/TP40016308-CH12-SW1) mechanism.

Example:

`1`

`2`

`NSString *bundleId = [[NSBundle mainBundle] bundleIdentifier];`

`3`

`NSString *canonicalURL = @"https://open.spotify.com/album/0sNOF9WDwhWunNAHPD3Baj";`

`4`

`NSString *branchLink = [NSString stringWithFormat:@"https://spotify.link/content_linking?~campaign=%@&$canonical_url=%@", bundleId, canonicalURL];`

`5`

`6`

`NSURL *url = [NSURL URLWithString:branchLink];`

`7`

`8`

`[[UIApplication sharedApplication] openURL:url];`

## Installing Spotify

Follow the steps below if you wish to link users directly to the app store so that they can install Spotify. Spotify partners with [Branch](https://branch.io/) for mobile install attribution.

Trigger the Branch tracker URL. Pass your application’s bundle ID in the `~campaign` parameter. You can optionally append the Spotify Content link through the `~$canonical_url` parameter to support deferred deep linking.

`1`

`NSString *bundleId = [[NSBundle mainBundle] bundleIdentifier];`

`2`

`NSString *canonicalURL = @"https://open.spotify.com/album/0sNOF9WDwhWunNAHPD3Baj";`

`3`

`NSString *branchLink = [NSString stringWithFormat:@"https://spotify.link/content_linking?~campaign=%@&$canonical_url=%@", bundleId, canonicalURL];`

`4`

`NSURLRequest *request = [[NSURLRequest alloc] initWithURL:[NSURL URLWithString:branchLink]];`

`5`

`6`

`[[[NSURLSession sharedSession] dataTaskWithRequest:request`

`7`

`completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {`

`8`

`}] resume];`

Open Spotify in the App Store:

`1`

`NSString *url = @"https://itunes.apple.com/app/spotify-music/id324684580?mt=8";`

`2`

`[[UIApplication sharedApplication] openURL:[NSURL URLWithString:url]];`

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

In order for Spotify to attribute traffic to your app, pass your application's bundle ID in the `utm_campaign` query string parameter. For example: `https://open.spotify.com/track/55fmthmn3rgnk9Wyx7G5dU?utm_campaign=com.app`

## Allow deeplinking from Webviews

Content at `open.spotify.com` links directly into Spotify or the app store. By default, iOS restricts webviews and prevent deeplinking into apps.

Support deeplinks by ensuring the webview handles the following schemes:

- `spotify:`
- `itms:`
- `itms-apps:`

## Further read

iOS: [https://stackoverflow.com/a/4442594](https://stackoverflow.com/a/4442594)