---
title: Spotify Open Access | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access
source: crawler
fetched_at: 2026-02-27T23:38:13.288836-03:00
rendered_js: true
word_count: 402
summary: This document introduces Spotify Open Access (SOA), a system that allows creators to manage access to restricted podcast content on Spotify using their existing subscription databases. It explains the core mechanisms of account linking via OAuth and entitlement management for securing paywalled audio content.
tags:
    - spotify-open-access
    - podcasts
    - entitlements
    - oauth
    - subscription-integration
    - content-protection
    - audio-streaming
category: concept
---

Spotify Open Access (SOA) allows partners with existing subscription or membership systems to publish podcast content on Spotify, and restrict access to that content based on existing subscription enforcement.

Spotify Open Access (SOA) is a first-of-its-kind offering in the audio industry, broadening distribution for creators who offer paid content. The system enables creators with existing paid content businesses to activate their customers on Spotify, and it allows Spotify users to unlock and listen to content they paid for via third-party services: for example, publications with paywalled content or licensed audiobook providers.

![soa-abstracted-linking-flow](https://developer-assets.spotifycdn.com/images/documentation/open-access/soa-abstracted-linking-flow.png)

## How it works

### You control who has access

Use the Open Access API to tell Spotify what episodes or shows are playable by whom using the concept of [Entitlements](https://developer.spotify.com/documentation/open-access/concepts#entitlements). Subscription canceled or credit card expired? You can revoke or update entitlements in near realtime.

### Tell your subscribers to connect with Spotify

Your subscribers can link their accounts to a Spotify account using [OAuth](https://oauth.net/2/). Spotify does not store any passwords or usernames of your subscribers and they can revoke access at any time.

### Securing your content

Content hosted on the Spotify platform is protected by Spotify's battle-tested content protection/DRM systems. Restrictions are enforced by services in the Spotify backend, ensuring that only authorized users are allowed to stream a particular media item. Restrictions take into account the content's availability markets and dates, as well as the users access permissions to SOA content.

## Example

[Lunar Industries](https://lunar-industries.spotify.com/) is a fictitious company we’ve created to help illustrate various scenarios, and examples, and to provide sample data from the SOA API.

Lunar Industries has multiple shows on Spotify. Users can subscribe to either a "Bonus" tier or a "Premium" tier on Lunar Industries' website. Of all of their shows on Spotify, one is public (no authorization required), one has bonus episodes that only certain subscribers can access, and one is a paid show apart from a teaser trailer. Each gated show has been set up with corresponding [entitlements](https://developer.spotify.com/documentation/open-access/concepts#entitlements). Lunar Industries has published the following shows:

- **Public** - [Moonshots](https://open.spotify.com/show/7inz2m1bx25SgNBZcRzqBP) does not require a paid subscription.
- **Limited Access** - [The Dark Side](https://open.spotify.com/show/0hFhphwy0gCuuFkOGF4BRu) is a show that has a few bonus episodes available to subscribers in the “Bonus Content” tier or higher.
- **Premium Access** - [Living on the Moon](https://open.spotify.com/show/0EwATaqqn7Yb0LX6O9XiqI) is for “Premium Tier” subscribers only.

The source code can be found on [GitHub](https://github.com/spotify/soa-reference-integration)

[![Lunar Industries](https://developer-assets.spotifycdn.com/assets/lunar-industries-screenshot.png)](https://lunar-industries.spotify.com/)

## Legal

Integrating with Spotify Open Access is subject to applicable terms and conditions.