---
title: Compliance Tips | Spotify for Developers
url: https://developer.spotify.com/compliance-tips
source: crawler
fetched_at: 2026-02-27T23:39:21.579079-03:00
rendered_js: true
word_count: 1625
summary: This document provides high-level guidance and best practices for developers to ensure their applications comply with Spotify's developer policies and maintain user trust.
tags:
    - developer-policy
    - user-privacy
    - data-handling
    - oauth-scopes
    - application-compliance
    - ux-design
category: guide
---

## Introduction

Spotify is home to communities where people can create, express themselves, listen, share, learn, and be inspired. As a platform, we have a duty to the users to ensure they maintain their privacy, keep control of their experience, and stay safe while using Spotify and applications using the Spotify Platform.

As a member of the Spotify for Developers community, please make sure that you are familiar with our [Developer Terms](https://developer.spotify.com/terms), [Developer Policy](https://developer.spotify.com/policy) and [Widgets Terms](https://developer.spotify.com/documentation/embeds/terms). Spotify wants to help you successfully build and launch your apps without issue, so we are including more information here about acceptable uses and behaviors to avoid. This resource serves to complement the [Spotify Developer Policy](https://developer.spotify.com/policy) and has been created to help you understand some of its guiding principles. We also give a few examples that demonstrate how our policies would apply in practice. We review the applications on our platform from time to time and may take action if you are found to violate our policies, including suspension, disabling your application or permanently revoking your access to the Spotify Platform.

## Focus on the User

Spotify’s users and their experience are at the core of what we do as a company. When using the Spotify Platform to build apps, keep user experience and user trust top of mind.

### User Experience

Build a quality experience. If your application crashes, takes long to load, or is otherwise difficult to use or navigate, this will be a poor experience for users. To help avoid negative user experiences, refer to Spotify’s [Platform Documentation](https://developer.spotify.com/).

### User Trust

We encourage our developer community to create value from data and in turn, foster user trust. Developers are encouraged to use data made available through the Spotify Platform, but must do so in a way that abides by our developer documentation and keeps the best interest of the user in mind.

#### OAuth Permission Scopes

Your app can use OAuth to request scopes from the users of your app. When users visit the OAuth grant screen, the requested permissions will be displayed to them, and they will then choose to approve or reject the request. Use this feature carefully. Users tend to be suspicious of apps that request too many scopes, and of apps that ask for scopes that are particularly sensitive. When you are determining which scopes that your app should request from users, keep these tips in mind:

- Make sure that your app isn’t requesting any OAuth scopes that it does not need. You can find information in our reference documentation about the data that is provided by each scope.
- Make it clear to the user why your app is asking for the scopes that it does. You can write a privacy policy or help document for users who want to better understand your app’s usage of their data, or include a dialog in the app before the user begins the OAuth flow.
- Sometimes, using the API is not the best way to deliver a product feature. Consider alternatives — like linking to a playlist in Spotify where the user can follow it manually, instead of building a programmatic follow button into your app.
- If some scopes are only required by a subset of your app’s users, then consider customizing the scope request to each user as they install your app. Remember that you can always ask users to re-authorize your app later if they begin using your product in a new way that requires new scopes.
- Don’t ask for scopes on the basis that your app might include a feature later that requires them.

For more information about Spotify’s OAuth scopes, see [Authorization Scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes).

#### Storing personal data

Avoid storing data that your app can fetch on the fly through the Spotify API. Users sometimes change their Spotify profile image, their display name, and even their account country. By fetching the data that you need at the time it is required, your app can avoid rendering any stale information.

Do periodically review the personal data stored by your app, and look for ways to retrieve less personal data, store less personal data, and shorten the length of time for which you store any personal data. To do this, consider:

- Removing unpopular features from your app that may consume extra personal data. Not every feature is a hit, and removing an obscure feature can also help you simplify your codebase and improve the user experience.
- Using newer Spotify APIs that enable you to deliver your applications, websites and services (SDAs) with less personal data.
- Feedback from your users about how your app handles personal data. Take steps to proactively communicate with your users about how their personal data is handled, and listen to them about concerns they may raise.

If at any point, a user wishes to request deletion of their data, this request should be easy and your response must be prompt and clear. When fielding requests from your users, it’s your duty as a developer to make this clear and easily navigable. For example, when a user requests the deletion of their data from your service, as a developer, you should make this process simple. Good practice would be to create a clickable button within your SDA user interface which is easy to find and allows a user to self-serve the request without difficulty. Don’t make simple user requests more difficult, such as requiring a user to email, phone or otherwise need to contact you for the removal of their data.

To learn more about how to respect users and user data, see [this section of the Developer Policy.](https://developer.spotify.com/policy#i-respect-users-and-data)

## Use of content

Spotify is home to over tens of millions of tracks, millions of podcast titles and thrives off its relationship with creators. When working with the Spotify Platform, ensure you represent your app, its function, and every component of your use of the Spotify platform (including all creators) accurately and appropriately.

When using content provided by Spotify, including artwork and metadata, it is important to follow our [Design Guidelines](https://developer.spotify.com/documentation/design#introduction). Ensure that you follow these guidelines closely and do not modify, crop or adjust artwork, including album art that is made available to you. If ever you are unsure about allowable use of content provided to you by Spotify, follow the easy to use guidelines and examples in the [Design Guidelines.](https://developer.spotify.com/documentation/design#introduction)

## Disallowed Use Cases

Spotify encourages our developer community to be creative and build positive experiences for users through their applications. Make sure to familiarize yourself with the prohibited use cases in the Developer Policy, in particular in [section III](https://developer.spotify.com/policy#iii-some-prohibited-applications).

Here are some common app use cases that break our policy, and you should not build:

- **Ringtones, alarms and alert tones:** Using or modifying Spotify song clips for alarm, ringtones, or alert integrations.
- **Software for restaurants, shops, bars, or other retail locations:** Spotify is for personal non-commercial use only.
- **DJ/Mixes:** Using Spotify’s catalog to segue, mix, re-mix, or overlap any Spotify Content with any other audio content (including other Spotify content).
- **Games or trivia quizzes:** Incorporating Spotify into any gaming or quiz functionality. For example, a “name that tune” quiz would not be allowed.
- **Synchronization:** Syncing sound recordings accessed via the Spotify Platform with other recordings, lyrics, or video.
- **Voice-Control:** Using Spotify’s tools to build voice-enabled experiences.

## Special Considerations for Streaming

Be sure to make yourself aware that some features and capabilities are only available to users subscribed to the Premium version of Spotify. For example, only subscribers to the Premium Spotify Service are able to stream music sound recordings through the Spotify Platform, whereas widgets, audio preview clips and podcast streaming may be made available to users of Spotify’s Free service to the extent these functionalities are available through the platform at the time.

Streaming apps include:

- Apps using Web Playback SDK to play music
- Apps using our `/v1/me/player/play` endpoint to play music
- Apps using the `/v1/me/player/next` endpoint where music could be next
- Apps using the `/v1/me/player/previous` endpoint when music could be the previous entity
- Apps using the iOS or Android SDKs to start, stop or modify playback of music
- Apps using any other Spotify API or SDK to control playback of music or stream music

Streaming SDAs have specific considerations, including limited monetization options. To learn more about these, visit Spotify’s Developer Policy, specifically [IV. Streaming and Commercial Use](https://developer.spotify.com/policy#iv-streaming-and-commercial-use).

## Commercial Use

If you are a developer looking to monetize your app, familiarize yourself with [IV. Streaming and Commercial Use of the Developer Policy.](https://developer.spotify.com/policy#iv-streaming-and-commercial-use) Pay special attention to the rules for streaming apps as they differ from the rules for non-streaming apps when it comes to monetization. Some examples of Streaming SDAs are given above.

The following are a few examples of use cases that **are not** allowed:

- Any commercialization of streaming apps such as:
  
  - Charging users $5/month for a home automation app that includes the ability to trigger music with the press of a button
  - Creating a Spotify player with the Web Playback SDK that includes advertising served via Google Ads
- Selling hoodies or merchandise featuring artwork or metadata that you obtained using our developer tools
- Repackaging data that you’ve gathered from the API and selling it to businesses

The following are a few examples of use cases that **are** allowed, provided you comply with the rest of our developer terms and policies:

- Selling access to a non-streaming app such as:
  
  - Making a playlist manager app and charging users $5/month to use it.
  - Building an app that notifies users when a podcast episode is released with their chosen keyword in the description, and charging $2 for it in an app store.
- Advertising served via Google Ads on a non-streaming app.
- Creating a playlist discovery website with pay-per-click advertising on it

If you have any questions, please check out our [Support Page](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer) for more information.