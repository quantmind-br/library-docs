---
title: Track Relinking | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/concepts/track-relinking
source: crawler
fetched_at: 2026-02-27T23:45:41.889074-03:00
rendered_js: true
word_count: 613
summary: This document explains the track relinking mechanism in the Spotify Web API, detailing how the market parameter can be used to find playable alternatives for tracks unavailable in certain regions.
tags:
    - spotify-api
    - track-relinking
    - market-availability
    - content-licensing
    - metadata-handling
category: concept
---

The availability of a track depends on the country registered in the user’s Spotify profile settings. Often Spotify has several instances of a track in its catalogue, each available in a different set of markets. This commonly happens when the track the album is on has been released multiple times under different licenses in different markets.

These tracks are linked together so that when a user tries to play a track that isn’t available in their own market, the Spotify mobile, desktop, and web players try to play another instance of the track that is available in the user’s market.

## Track Relinking in the Web API

If your application supplies a `market` parameter in its call to the following track endpoints, the Web API will attempt to return information about alternative tracks that are available in the specified market:

- [Get a Track](https://developer.spotify.com/documentation/web-api/reference/get-track)
- [Get Several Tracks](https://developer.spotify.com/documentation/web-api/reference/get-several-tracks)
- [Get an Album](https://developer.spotify.com/documentation/web-api/reference/get-an-album)
- [Get Several Albums](https://developer.spotify.com/documentation/web-api/reference/get-multiple-albums)
- [Get an Album’s Tracks](https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks)
- [Get a Playlist's Items](https://developer.spotify.com/documentation/web-api/reference/get-playlists-items)
- [Get a User’s Saved Tracks](https://developer.spotify.com/documentation/web-api/reference/get-users-saved-tracks)

When using the `market` query parameter, the response will contain another instance of the tracks only if the original track is unavailable and other instances of the track are available.

For example, the track “Heaven and Hell” by William Onyeabor is not available in the United States (market code `US`), as shown by the request to retrieve the track’s metadata:

`1`

``curl -X GET "https://api.spotify.com/v1/tracks/6kLCHFM39wkFjOuyPGLGeQ"` ``

`1`

`{`

`2`

`...`

`3`

`available_markets: [ "AT", "AU", "BE", "DK", "ES", "FI",`

`4`

`"FR", "HU", "IT", "PL", "PT", "SE",`

`5`

`"SK", "TR", "TW" ],`

`6`

`...`

`7`

`uri: "spotify:track:6kLCHFM39wkFjOuyPGLGeQ"`

`8`

`}`

If a `market` query parameter specifying the US market is appended to the call, the Web API recognizes that the specified track is unplayable and instead returns information about a track that is playable in the specified market. In addition it returns information about the original track:

`1`

``curl -X GET "https://api.spotify.com/v1/tracks/6kLCHFM39wkFjOuyPGLGeQ?market=US"` ``

`1`

`{`

`2`

`...`

`3`

`is_playable: true`

`4`

`linked_from: {`

`5`

`external_urls: {`

`6`

`spotify: "https://open.spotify.com/track/6kLCHFM39wkFjOuyPGLGeQ"`

`7`

`},`

`8`

`href: "https://api.spotify.com/v1/tracks/6kLCHFM39wkFjOuyPGLGeQ",`

`9`

`id: "6kLCHFM39wkFjOuyPGLGeQ",`

`10`

`type: "track",`

`11`

`uri: "spotify:track:6kLCHFM39wkFjOuyPGLGeQ"`

`12`

`},`

`13`

`...`

`14`

`uri: "spotify:track:6ozxplTAjWO0BlUxN8ia0A"`

`15`

`}`

There are a number of important differences between the response you get with and without the `market` query parameter.

When the `market` parameter is supplied:

- The `available_markets` property in the [Track](https://developer.spotify.com/documentation/web-api/reference/get-track) object is replaced by the `is_playable` property. (Since the request contains the `market` query parameter, there’s no need for the `available_markets` property to determine if the user can play the track or not.)
- If the track has been relinked, the response contains a `linked_from` object containing information about the original track. In the example above, the track that was requested had the Spotify URI `spotify:track:6kLCHFM39wkFjOuyPGLGeQ`. Since it’s been relinked, this original [track URI](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) can be found in the `linked_from` object. The parent track object now contains metadata about the relinked track with URI `spotify:track:6ozxplTAjWO0BlUxN8ia0A`.
- If the `is_playable` property is `false`, the original track is not available in the given market, and Spotify did not have any tracks to relink it with. The track response will still contain metadata for the original track, and a `restrictions` object containing the reason why the track is not available: `"restrictions" : {"reason" : "market"}`.
- If the `is_playable` property is `true`, the `linked_from` object may or may not exist depending on whether the original track was available in the market. If the `linked_from` object exists, the original track has been relinked.

Valid `market` query parameter values are [ISO 3166-1 alpha-2 codes](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), as well as `from_token`. If `from_token` is used, an access token tied to a user must be supplied; `from_token` is the same thing as setting the market parameter to the [user’s](https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile) `country`.