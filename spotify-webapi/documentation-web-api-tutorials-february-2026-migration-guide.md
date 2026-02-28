---
title: February 2026 Web API Dev Mode Changes - Migration Guide
url: https://developer.spotify.com/documentation/web-api/tutorials/february-2026-migration-guide
source: crawler
fetched_at: 2026-02-27T23:45:45.483981-03:00
rendered_js: true
word_count: 998
summary: This migration guide provides instructions for developers to update their Spotify Development Mode applications in response to the 2026 Web API changes, covering endpoint consolidations, field renames, and new app restrictions.
tags:
    - spotify-web-api
    - migration-guide
    - api-updates
    - development-mode
    - breaking-changes
    - endpoint-migration
category: guide
---

This guide is here to help developers with existing apps migrate to the updated Web API following the [February 2026 announcement](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security). It covers what's changing, who is affected, and provides step-by-step migration paths for common use cases.

## Who is affected?

**Extended Quota Mode apps:** No migration required. Apps in extended quota mode are not affected by any of the changes described in this guide — all existing endpoints, fields, and behaviors remain unchanged. You can optionally adopt the new generic library endpoints (`PUT/DELETE /me/library`) but your existing integrations will remain fully functional.

**Development Mode apps:** This guide is for you. Read on for the full details of what's changing and how to update your app.

## Timeline

DateWhat happens**February 11, 2026**New Development Mode apps are created with new restrictions**March 9, 2026**Existing Development Mode apps are migrated to new restrictions

## Account and App Limit Changes

### Premium Requirement

All Development Mode apps require the app owner to have an active Spotify Premium subscription. If the owner's Premium subscription lapses, the app will stop working. It will resume functioning once the owner resubscribes.

### App Limits

RequirementNew appsClient IDs per developer1Users per app5

**Existing apps are grandfathered:** If you already have multiple Client IDs or more than 5 users, you will retain them. These limits only restrict what you can create or add going forward.

* * *

## Endpoint Changes

### Library Management

The entity type specific save, remove, follow, and unfollow endpoints have been replaced with generic library endpoints that work with Spotify URIs.

#### Saving items and following

**Before:**

`1`

`PUT /me/tracks`

`2`

`PUT /me/albums`

`3`

`PUT /me/episodes`

`4`

`PUT /me/shows`

`5`

`PUT /me/audiobooks`

`6`

`PUT /me/following`

`7`

`PUT /playlists/{id}/followers`

**After:**

The new [`PUT /me/library`](https://developer.spotify.com/documentation/web-api/reference/save-library-items) endpoint accepts [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) instead of IDs, allowing you to save or follow any supported content type in a single request. Appropriate scopes need to be passed depending on the entities being saved.

#### Removing items and unfollowing

**Before:**

`1`

`DELETE /me/tracks`

`2`

`DELETE /me/albums`

`3`

`DELETE /me/episodes`

`4`

`DELETE /me/shows`

`5`

`DELETE /me/audiobooks`

`6`

`DELETE /me/following`

`7`

`DELETE /playlists/{id}/followers`

**After:**

Like the save endpoint, [`DELETE /me/library`](https://developer.spotify.com/documentation/web-api/reference/remove-library-items) accepts [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) instead of IDs.

#### Checking if items are saved

The individual "contains" endpoints have been replaced with a single generic endpoint.

**Before:**

`1`

`GET /me/tracks/contains`

`2`

`GET /me/albums/contains`

`3`

`GET /me/episodes/contains`

`4`

`GET /me/shows/contains`

`5`

`GET /me/audiobooks/contains`

`6`

`GET /me/following/contains`

`7`

`GET /playlists/{id}/followers/contains`

**After:**

`1`

`GET /me/library/contains`

The new [`GET /me/library/contains`](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) endpoint accepts [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) instead of IDs.

* * *

### Playlist Endpoint Renames

The playlist track management endpoints have been renamed from `/tracks` to `/items`:

* * *

### Batch/Bulk Fetch Endpoints (Removed)

The following batch endpoints are no longer available. Fetch items individually instead.

**Migration example:**

`1`

`// Before: Batch fetch`

`2`

`const response = await fetch('/v1/tracks?ids=id1,id2,id3');`

`3`

`const { tracks } = await response.json();`

`4`

`5`

`// After: Individual fetches`

`6`

`const trackIds = ['id1', 'id2', 'id3'];`

`7`

`const tracks = await Promise.all(`

`8`

`trackIds.map(id =>`

`9`

``fetch(`/v1/tracks/${id}`).then(r => r.json())``

`10`

`)`

`11`

`);`

### Browse and Artist Endpoints (Removed)

Removed endpointDescription`GET /browse/new-releases`New album releases`GET /browse/categories`Browse categories list`GET /browse/categories/{id}`Single category details`GET /artists/{id}/top-tracks`Artist's top tracks by country

* * *

### Other User Data (Removed)

Removed endpointReplacement`GET /users/{id}`No replacement - use [`GET /me`](https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile) for current user`GET /users/{id}/playlists`No replacement - use [`GET /me/playlists`](https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists) for current user`POST /users/{user_id}/playlists`[`POST /me/playlists`](https://developer.spotify.com/documentation/web-api/reference/create-playlist)`GET /markets`No replacement

* * *

### Search Endpoint

The [`GET /search`](https://developer.spotify.com/documentation/web-api/reference/search) endpoint's `limit` parameter has been updated:

ParameterBeforeAfter`limit` maximum5010`limit` default205

If your app relies on fetching more than 10 results per search request, you will need to paginate through results using the `offset` parameter.

* * *

## Field Changes by Content Type

The following field changes apply across all endpoints that return these content types.

### Removed fields

The following fields have been removed from response objects. Update your code to handle their absence gracefully.

#### Track

`available_markets`, `external_ids`, `linked_from`, `popularity`

#### Album

`album_group`, `available_markets`, `external_ids`, `label`, `popularity`

#### Artist

`followers`, `popularity`

#### User (from `GET /me`)

`country`, `email`, `explicit_content`, `followers`, `product`

#### Show

`available_markets`, `publisher`

#### Audiobook / Chapter

`available_markets`, `publisher` (audiobook only)

### Renamed fields

#### Playlist

The `tracks` field has been renamed:

BeforeAfter`tracks``items``tracks.tracks``items.items``tracks.tracks.track``items.items.item`

**Important:** Playlist contents (`items`) are only returned for playlists the user owns or collaborates on. For other playlists, only metadata is returned and the `items` field will be absent from the response.

* * *

## Migration Checklist

Use this checklist to ensure your app is ready:

- **Account:** Ensure the app owner has Spotify Premium
- **Library endpoints:** Replace content-specific save/remove/follow/unfollow calls with `PUT/DELETE /me/library`
- **Contains checks:** Replace content-specific "contains" calls with `GET /me/library/contains`
- **Batch fetches:** Replace batch endpoints with individual fetch calls
- **Browse and artist endpoints:** Remove features using browse categories, new releases, or artist top tracks
- **Other users:** Remove features that fetch other users' profiles or playlists
- **Playlist endpoints:** Update `/playlists/{id}/tracks` calls to `/playlists/{id}/items`
- **Playlist handling:** Update code for the `tracks` → `items` field rename
- **Removed fields:** Handle missing fields gracefully (check for undefined/null)
- **Search pagination:** Update search requests to handle the reduced `limit` maximum (10) and paginate if needed
- **Global recommendation:** Limit API calls to avoid hitting rate limits

* * *

## Common Migration Patterns

### Pattern 1: Updating library save calls

`1`

`// Before`

`2`

`await spotify.put('/me/tracks', { ids: ['trackId1', 'trackId2'] });`

`3`

`await spotify.put('/me/albums', { ids: ['albumId1'] });`

`4`

`await spotify.put('/me/following', { ids: ['artistId1'], type: 'artist' });`

`5`

`6`

`// After — all entity types in a single call`

`7`

`await spotify.put('/me/library', {`

`8`

`uris: [`

`9`

`'spotify:track:trackId1',`

`10`

`'spotify:track:trackId2',`

`11`

`'spotify:album:albumId1',`

`12`

`'spotify:artist:artistId1'`

`13`

`]`

`14`

`});`

### Pattern 2: Handling missing popularity field

`1`

`// Before`

`2`

`const sortedTracks = tracks.sort((a, b) => b.popularity - a.popularity);`

`3`

`4`

`// After - popularity is no longer available`

`5`

`// Consider alternative sorting criteria or remove this feature`

`6`

`const sortedTracks = tracks.sort((a, b) =>`

`7`

`a.name.localeCompare(b.name)`

`8`

`);`

### Pattern 3: Handling playlist field rename

`1`

`// Before`

`2`

`const trackCount = playlist.tracks.total;`

`3`

`const firstTrack = playlist.tracks.items[0].track;`

`4`

`5`

`// After`

`6`

`const trackCount = playlist.items?.total ?? 0;`

`7`

`const firstTrack = playlist.items?.items?.[0]?.item;`

`8`

`9`

`// Note: items may be undefined for playlists you don't own`

`10`

`if (!playlist.items) {`

`11`

`console.log('Track details not available for this playlist');`

`12`

`}`

* * *

## Need Help?

- [Full list of available endpoints](https://developer.spotify.com/documentation/web-api/references/changes/february-2026#endpoints-still-available)
- [Developer Community forum](https://community.spotify.com/t5/Community-Prep/February-2026-Spotify-for-Developers-update-thread/m-p/7330564)