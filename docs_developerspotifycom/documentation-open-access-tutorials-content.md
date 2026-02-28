---
title: Content Management | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/tutorials/content
source: crawler
fetched_at: 2026-02-27T23:42:07.553262-03:00
rendered_js: true
word_count: 877
summary: This document explains how Spotify Open Access uses entitlements and specific RSS feed tags to control user access to restricted podcast content and manage the ingestion process.
tags:
    - spotify-open-access
    - entitlements
    - rss-ingestion
    - access-control
    - podcast-metadata
    - sandbox-mode
category: guide
---

## Content access

SOA uses a concept of entitlements to control how users can access restricted content. [Entitlements](https://developer.spotify.com/documentation/open-access/concepts#entitlements) are identifiers that the partner defines and assigns to users and episodes. An episode is playable if the user and the episode have at least one entitlement identifier in common.

User entitlements are supplied by the partner during the authentication process. A user can have 0, 1, or multiple active entitlements.

Episode entitlements are defined in the RSS feed during ingestion. An episode can have 0, 1, or multiple entitlements. Episodes with 0 entitlements are publicly available without further authorization.

In the [Lunar Industries](https://lunar-industries.spotify.com/) example, in the content:

- **Moonshots** will have no entitlements attached to any episodes.
- **The Dark Side** has its bonus episodes tagged with the `"lunar_dark_side"` entitlement. Living on the Moon has all its episodes (except the teaser trailer) tagged with the `"lunar_living"` entitlement.

And for the users:

- Users that subscribe to the "Bonus Content" tier are given the `"lunar_dark_side"` entitlement.
- Users that subscribe to the "Premium" tier are given both the `"lunar_dark_side"` and `"lunar_living"` entitlements in their tokens.

![SOA Content Playback](https://developer-assets.spotifycdn.com/images/documentation/open-access/soa-content-playback.png)

An example for the **Lunar Industries** show **The Dark Side** is below. This is not complete RSS as it is of course missing many tags required for full ingestion, but we highlight some SOA details. You can also view [the show's RSS feed directly](https://content-access.spotifycdn.com/lunar-industries/the-dark-side-bonus.rss).

`1`

`<?xml version="1.0" encoding="UTF-8"?>`

`2`

`<rss xmlns:spotify="http://www.spotify.com/ns/rss">`

`3`

`<channel>`

`4`

`<title>The Dark Side</title>`

`5`

`<description>Lunar's Bonus Content</description>`

`6`

`<spotify:access>`

`7`

`<partner id="2zkvpokj55bj2sCHxCejJs"/>`

`8`

`</spotify:access>`

`9`

`<item>`

`10`

`<title>Free Episode #1</title>`

`11`

`<!-- Note no spotify:access section -->`

`12`

`<enclosure url="https://l-i.com/free1.mp3" length="10" type="audio/mpeg"/>`

`13`

`</item>`

`14`

`<item>`

`15`

`<title>Bonus Episode #1</title>`

`16`

`<spotify:access>`

`17`

`<entitlement name="lunar_dark_side"/>`

`18`

`</spotify:access>`

`19`

`<enclosure url="https://l-i.com/bonus1.mp3" length="10" type="audio/mpeg"/>`

`20`

`</item>`

`21`

`</channel>`

`22`

`</rss>`

Similarly, the **Living on the Moon** RSS would have all its episodes tagged:

`1`

`<?xml version="1.0" encoding="UTF-8"?>`

`2`

`<rss xmlns:spotify="http://www.spotify.com/ns/rss">`

`3`

`<channel>`

`4`

`<title>Living on the Moon</title>`

`5`

`<description>Lunar's Premium Content</description>`

`6`

`<spotify:access>`

`7`

`<partner id="2zkvpokj55bj2sCHxCejJs"/>`

`8`

`</spotify:access>`

`9`

`<item>`

`10`

`<title>Living Episode #1</title>`

`11`

`<spotify:access>`

`12`

`<entitlement name="lunar_living"/>`

`13`

`</spotify:access>`

`14`

`<enclosure url="https://l-i.com/ep1.mp3" length="10" type="audio/mpeg"/>`

`15`

`</item>`

`16`

`<item>`

`17`

`<title>Living Episode #2</title>`

`18`

`<spotify:access>`

`19`

`<entitlement name="lunar_living"/>`

`20`

`</spotify:access>`

`21`

`<enclosure url="https://l-i.com/ep2.mp3" length="10" type="audio/mpeg"/>`

`22`

`</item>`

`23`

`</channel>`

`24`

`</rss>`

View [the full RSS feed here](https://content-access.spotifycdn.com/lunar-industries/living-on-the-moon.rss).

### Supporting many shows

In the case that a partner has a large number of shows which are bundled, it may make more sense to define entitlements that map to a "tier" rather than individual shows, to reduce the size of the set of entitlements that would need to be sent in register and update calls. Spotify Open Access supports this as well - it is up to the partner how to define entitlements.

## Content ingestion

All gated content will be ingested and served through the Spotify platform.

RSS-based podcast feeds are submitted through [podcasters.spotify.com](https://podcasters.spotify.com).

Content ingested through RSS must conform to the [Spotify Podcast Delivery Specification](https://providersupport.spotify.com/article/podcast-delivery-specification-1-9) in addition to the addenda in this section.

Spotify recommends having an RSS feed that is specific to Spotify ingestion, which contains the additional information described in this section.

For the ingestion of a podcast RSS feed that has a mix of free and paid episodes, Spotify has introduced two new fields in the spotify namespace in the RSS that will allow the ingestion of the mixed subscription tier episodes for the podcast show. The two fields are partner-id at the channel level:

`1`

`<spotify:access>`

`2`

`<partner id="2zkvpokj55bj2sCHxCejJs"/>`

`3`

`</spotify:access>`

and entitlement at the item level -- example from The Dark Side restricted episode:

`1`

`<spotify:access>`

`2`

`<entitlement name="lunar_dark_side"/>`

`3`

`</spotify:access>`

Note that in the opening xml tag, the Spotify namespace must be referenced, using `xmlns:spotify="http://www.spotify.com/ns/rss"`

### Sandbox mode

Sandbox mode allows partners to test a show before it becomes widely available to Spotify users. A sandboxed show can be accessed only via a direct link if the link is known: `https://open.spotify.com/show/0CTGu9RccEYBWxDJF1LovM`. It will not be available through search and it will not be recommended to users. The same applies to all the episodes in the show.

Spotify has introduced a new field in the `spotify` namespace in the RSS that will allow sandbox mode. The field is `sandbox` at the channel level:

`1`

`<spotify:access>`

`2`

`<partner id="2zkvpokj55bj2sCHxCejJs"/>`

`3`

`<sandbox enabled="true"/>`

`4`

`</spotify:access>`

Once a show is tested and is ready to be consumed by Spotify users, remove the tag altogether or mark sandbox enabled as false.

`1`

`<spotify:access>`

`2`

`<partner id="2zkvpokj55bj2sCHxCejJs"/>`

`3`

`<sandbox enabled="false"/>`

`4`

`</spotify:access>`

Note that this only goes into effect when the `partner-id` field is also present; a `sandbox` tag on its own has no effect. This field can be toggled as suited. However, some surfaces might not be covered. For example, if this show has previously been searched by a user, since search results are heavily cached, it might still show up on a search for that user. If it has been added to a user’s library, it will stay available.

## Content protection

Content hosted on the Spotify platform is protected by Spotify's content protection/DRM systems.

Restrictions are enforced by services in the Spotify backend, ensuring that only authorized users are allowed to stream a particular media item. Restrictions take into account the content's availability markets and dates, and the user's authorization status (for SOA content).