---
title: Web API Changelog - February 2026
url: https://developer.spotify.com/documentation/web-api/references/changes/february-2026
source: crawler
fetched_at: 2026-02-27T23:38:22.585487-03:00
rendered_js: true
word_count: 2044
summary: This document outlines significant updates to the Spotify Web API, detailing the removal, addition, and modification of various endpoints to improve platform security and streamline developer access.
tags:
    - spotify-api
    - api-changes
    - deprecation-notice
    - endpoint-updates
    - web-api
category: reference
---

## Overview

These changes are related to [this](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security) blog post. The changes are categorised by endpoints (removed, changed, or added), and then by fields on the different content types (track, playlist, chapter, etc.) Lastly you find a list with all endpoints still available, but field and behavioral changes mentioned earlier still apply.

## Changes to endpoints

The following changes have been made to the endpoints.

- \[REMOVED] **Create Playlist for user** (`POST /users/{user_id}/playlists`) - Create a playlist for a Spotify user.
  
  - Use `POST /me/playlists` instead
- \[REMOVED] **Get Artist's Top Tracks** (`GET /artists/{id}/top-tracks`) – Get Spotify catalog information about an artist's top tracks by country.
- \[REMOVED] **Get Available Markets** (`GET /markets`) – Get the list of markets where Spotify is available.
- \[REMOVED] **Get New Releases** (`GET /browse/new-releases`) – Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player's "Browse" tab).
- \[REMOVED] **Get Several Albums** (`GET /albums`) – Get Spotify catalog information for multiple albums identified by their Spotify IDs.
- \[REMOVED] **Get Several Artists** (`GET /artists`) – Get Spotify catalog information for several artists based on their Spotify IDs.
- \[REMOVED] **Get Several Audiobooks** (`GET /audiobooks`) – Get Spotify catalog information for several audiobooks identified by their Spotify IDs.
- \[REMOVED] **Get Several Browse Categories** (`GET /browse/categories`) – Get a list of categories used to tag items in Spotify (on, for example, the Spotify player's "Browse" tab).
- \[REMOVED] **Get Several Chapters** (`GET /chapters`) – Get Spotify catalog information for several audiobook chapters identified by their Spotify IDs.
- \[REMOVED] **Get Several Episodes** (`GET /episodes`) – Get Spotify catalog information for several episodes based on their Spotify IDs.
- \[REMOVED] **Get Several Shows** (`GET /shows`) – Get Spotify catalog information for several shows based on their Spotify IDs.
- \[REMOVED] **Get Several Tracks** (`GET /tracks`) – Get Spotify catalog information for multiple tracks based on their Spotify IDs.
- \[REMOVED] **Get Single Browse Category** (`GET /browse/categories/{id}`) – Get a single category used to tag items in Spotify (on, for example, the Spotify player's "Browse" tab).
- \[REMOVED] **Get User's Playlists** (`GET /users/{id}/playlists`) – Get a list of the playlists owned or followed by a Spotify user.
- \[REMOVED] **Get User's Profile** (`GET /users/{id}`) – Get public profile information about a Spotify user.
- \[ADDED] **Remove from Library** (`DELETE /me/library`) – Remove a list of Spotify URIs from the user's library.
- \[REMOVED] **Remove Albums for Current User** (`DELETE /me/albums`) – Removes albums from the user's library.
  
  - Use `DELETE /me/library` instead
- \[REMOVED] **Remove Audiobooks for Current User** (`DELETE /me/audiobooks`) – Removes audiobooks from the user's library.
  
  - Use `DELETE /me/library` instead
- \[REMOVED] **Remove Episodes for Current User** (`DELETE /me/episodes`) – Removes episodes from the user's library.
  
  - Use `DELETE /me/library` instead
- \[REMOVED] **Remove Shows for Current User** (`DELETE /me/shows`) – Removes shows from the user's library.
  
  - Use `DELETE /me/library` instead
- \[REMOVED] **Remove Tracks for Current User** (`DELETE /me/tracks`) – Removes tracks from the user's library.
  
  - Use `DELETE /me/library` instead
- \[ADDED] **Save to Library** (`PUT /me/library`) – Save a list of Spotify URIs to the user's library.
- \[REMOVED] **Save Albums for Current User** (`PUT /me/albums`) – Saves one or more albums to the user's library.
  
  - Use `PUT /me/library` instead
- \[REMOVED] **Save Audiobooks for Current User** (`PUT /me/audiobooks`) – Saves audiobooks to the user's library.
  
  - Use `PUT /me/library` instead
- \[REMOVED] **Save Episodes for Current User** (`PUT /me/episodes`) – Saves episodes to the user's library.
  
  - Use `PUT /me/library` instead
- \[REMOVED] **Save Shows for Current User** (`PUT /me/shows`) – Saves shows to the user's library.
  
  - Use `PUT /me/library` instead
- \[REMOVED] **Save Tracks for Current User** (`PUT /me/tracks`) – Saves tracks to the user's library.
  
  - Use `PUT /me/library` instead
- \[ADDED] **Check User's Saved Items** (`GET /me/library/contains`) – Check if one or more items are already saved in the current user's library.
- \[REMOVED] **Check If User Follows Artists or Users** (`GET /me/following/contains`) – Check to see if the current user is following one or more artists or other Spotify users.
  
  - Use `GET /me/library/contains` instead
- \[REMOVED] **Check if Current User Follows Playlist** (`GET /playlists/{id}/followers/contains`) – Checks whether the current user follows a given playlist.
  
  - Use `GET /me/library/contains` instead
- \[REMOVED] **Check User's Saved Albums** (`GET /me/albums/contains`) – Checks whether one or more album IDs are saved in the current user's library.
  
  - Use `GET /me/library/contains` instead
- \[REMOVED] **Check User's Saved Audiobooks** (`GET /me/audiobooks/contains`) – Checks whether one or more audiobook IDs are saved in the current user's library.
  
  - Use `GET /me/library/contains` instead
- \[REMOVED] **Check User's Saved Episodes** (`GET /me/episodes/contains`) – Checks whether one or more episode IDs are saved in the current user's library.
  
  - Use `GET /me/library/contains` instead
- \[REMOVED] **Check User's Saved Shows** (`GET /me/shows/contains`) – Checks whether one or more show IDs are saved in the current user's library.
  
  - Use `GET /me/library/contains` instead
- \[REMOVED] **Check User's Saved Tracks** (`GET /me/tracks/contains`) – Checks whether one or more track IDs are saved in the current user's library.
  
  - Use `GET /me/library/contains` instead
- \[REMOVED] **Follow Artists or Users** (`PUT /me/following`) – Follows one or more artists or users.
  
  - Use `PUT /me/library` instead
- \[REMOVED] **Follow Playlist** (`PUT /playlists/{id}/followers`) – Follows a playlist on behalf of the current user.
  
  - Use `PUT /me/library` instead
- \[REMOVED] **Unfollow Artists or Users** (`DELETE /me/following`) – Unfollows one or more artists or users.
  
  - Use `DELETE /me/library` instead
- \[REMOVED] **Unfollow Playlist** (`DELETE /playlists/{id}/followers`) – Unfollows a playlist on behalf of the current user.
  
  - Use `DELETE /me/library` instead
- \[ADDED] **Add Items to Playlist** (`POST /playlists/{id}/items`) – Add one or more items to a user's playlist.
- \[ADDED] **Get Playlist Items** (`GET /playlists/{id}/items`) – Get full details of the items of a playlist.
- \[ADDED] **Remove Playlist Items** (`DELETE /playlists/{id}/items`) – Remove one or more items from a user's playlist.
- \[ADDED] **Update Playlist Items** (`PUT /playlists/{id}/items`) – Either reorder or replace items in a playlist.
- \[REMOVED] **Add Items to Playlist** (`POST /playlists/{id}/tracks`) – Adds tracks or episodes to a playlist.
  
  - Use `POST /playlists/{id}/items` instead
- \[REMOVED] **Get Playlist Items** (`GET /playlists/{id}/tracks`) – Retrieves the tracks or episodes in a playlist.
  
  - Use `GET /playlists/{id}/items` instead
- \[REMOVED] **Remove Playlist Items** (`DELETE /playlists/{id}/tracks`) – Removes tracks or episodes from a playlist.
  
  - Use `DELETE /playlists/{id}/items` instead
- \[REMOVED] **Update Playlist Items** (`PUT /playlists/{playlist_id}/tracks`) – Either reorder or replace items in a playlist.
  
  - Use `PUT /playlists/{id}/items` instead
- \[CHANGED] **Search for Item** (`GET /search`) – The `limit` parameter maximum value has been reduced from 50 to 10, and the default value has been changed from 20 to 5.

## Changes to fields

The following content types and their objects are present in most responses - these changes apply for their occurances in all responses.

### Album

- \[REMOVED] **album\_group** - Describes the relationship between the artist and the album
- \[REMOVED] **available\_markets** – The markets in which the album is available: ISO 3166-1 alpha-2 country codes.
- \[REMOVED] **external\_ids** — Known external IDs for the album.
- \[REMOVED] **label** – The label associated with the album.
- \[REMOVED] **popularity** — The popularity of the album. The value will be between 0 and 100, with 100 being the most popular.

### Artist

- \[REMOVED] **followers** — Information about the followers of the artist.
- \[REMOVED] **popularity** — The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.

### Audiobook

- \[REMOVED] **available\_markets** – A list of the countries in which the audiobook can be played, identified by their ISO 3166-1 alpha-2 code.
- \[REMOVED] **publisher** – The publisher of the audiobook.

### Chapter

- \[REMOVED] **available\_markets** – A list of the countries in which the audiobook can be played, identified by their ISO 3166-1 alpha-2 code.

### Playlist

Will only return an **items** object for the user's playlist, other playlists will only provide metadata (not the contents of the playlist) in the response.

- \[RENAMED] **tracks -&gt; items**
- \[RENAMED] **tracks.tracks -&gt; items.items**
- \[RENAMED] **tracks.tracks.track -&gt; items.items.item**

### Show

- \[REMOVED] **available\_markets** – A list of the countries in which the show can be played, identified by their ISO 3166-1 alpha-2 code.
- \[REMOVED] **publisher** – The publisher of the show.

### Track

- \[REMOVED] **available\_markets** – A list of the countries in which the track can be played, identified by their ISO 3166-1 alpha-2 code.
- \[REMOVED] **external\_ids** — Known external IDs for the track.
- \[REMOVED] **linked\_from** – Original track when relinked.
- \[REMOVED] **popularity** — The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.

### User

- \[REMOVED] **country** – The country of the user, as set in the user's account profile. An ISO 3166-1 alpha-2 country code.
- \[REMOVED] **email** – The user's email address, as entered by the user when creating their account.
- \[REMOVED] **explicit\_content** – The user's explicit content settings.
- \[REMOVED] **followers** — Information about the followers of the user.
- \[REMOVED] **product** – The user's Spotify subscription level: "premium", "free", etc. (The subscription level "open" can be considered the same as "free".)

## Endpoints still available

These endpoints remain available, but the changes mentioned above still apply to them.

### Library

- **Change Playlist Details** (`PUT /playlists/{id}`) – Updates a playlist's name, description, or visibility.
- **Create Playlist** (`POST /me/playlists`) – Creates a new playlist for logged in users.
- **Get Current User's Playlists** (`GET /me/playlists`) – Retrieves playlists for the current authenticated user.
- **Get Followed Artists** (`GET /me/following`) – Retrieves artists followed by the current user.
- **Get User's Saved Albums** (`GET /me/albums`) – Retrieves albums saved in the user's library.
- **Get User's Saved Audiobooks** (`GET /me/audiobooks`) – Retrieves audiobooks saved in the user's library.
- **Get User's Saved Episodes** (`GET /me/episodes`) – Retrieves podcast episodes saved in the user's library.
- **Get User's Saved Shows** (`GET /me/shows`) – Retrieves podcast shows saved in the user's library.
- **Get User's Saved Tracks** (`GET /me/tracks`) – Retrieves tracks saved in the user's library.
- **Remove from Library** (`DELETE /me/library`) – Remove a list of Spotify URIs from the user's library.
- **Save to Library** (`PUT /me/library`) – Save a list of Spotify URIs to the user's library.

### Metadata

- **Get Album** (`GET /albums/{id}`) – Retrieves detailed metadata for a single album.
- **Get Album Tracks** (`GET /albums/{id}/tracks`) – Retrieves the tracks contained in a specific album.
- **Get Artist** (`GET /artists/{id}`) – Retrieves detailed metadata for a single artist.
- **Get Artist's Albums** (`GET /artists/{id}/albums`) – Retrieves albums released by a specific artist.
- **Get Audiobook** (`GET /audiobooks/{id}`) – Retrieves detailed metadata for a single audiobook.
- **Get Audiobook Chapters** (`GET /audiobooks/{id}/chapters`) – Retrieves chapters belonging to a specific audiobook.
- **Get Chapter** (`GET /chapters/{id}`) – Retrieves metadata for a single audiobook chapter.
- **Get Episode** (`GET /episodes/{id}`) – Retrieves metadata for a single podcast episode.
- **Get Show** (`GET /shows/{id}`) – Retrieves metadata for a single podcast show.
- **Get Show Episodes** (`GET /shows/{id}/episodes`) – Retrieves episodes belonging to a specific podcast show.
- **Get Track** (`GET /tracks/{id}`) – Retrieves metadata for a single track.
- **Search for Item** (`GET /search`) – Searches across the Spotify catalog for albums, artists, playlists, tracks, shows, episodes, or audiobooks.

### User

- **Get Current User's Profile** (`GET /me`) – Retrieves profile information for the current authenticated user.

### Personalisation

- **Get User's Top Items** (`GET /me/top/{type}`) – Retrieves the user's top artists or tracks over a given time range.

### Player

- **Add Item to Queue** (`POST /me/player/queue`) – Adds an item to the playback queue.
- **Get Available Devices** (`GET /me/player/devices`) – Retrieves devices available for playback.
- **Get Currently Playing Track** (`GET /me/player/currently-playing`) – Retrieves the item currently being played.
- **Get Playback State** (`GET /me/player`) – Retrieves information about the user's current playback state.
- **Get Recently Played Tracks** (`GET /me/player/recently-played`) - Get tracks from the current user's recently played tracks.
- **Get User's Queue** (`GET /me/player/queue`) – Retrieves the current playback queue.
- **Pause Playback** (`PUT /me/player/pause`) – Pauses playback.
- **Seek to Position** (`PUT /me/player/seek`) – Seeks to a specific position in the currently playing item.
- **Set Repeat Mode** (`PUT /me/player/repeat`) – Sets repeat mode for playback.
- **Set Volume** (`PUT /me/player/volume`) – Sets the playback volume.
- **Skip to Next** (`POST /me/player/next`) – Skips to the next item in the queue.
- **Skip to Previous** (`POST /me/player/previous`) – Skips to the previous item.
- **Start/Resume Playback** (`PUT /me/player/play`) – Starts or resumes playback.
- **Toggle Shuffle** (`PUT /me/player/shuffle`) – Toggles shuffle mode.
- **Transfer Playback** (`PUT /me/player`) – Transfers playback to a new device.

### Playlist

- **Get Playlist** (`GET /playlists/{id}`) – Retrieves full details of a playlist.
- **Get Playlist Cover Image** (`GET /playlists/{id}/images`) – Retrieves the cover image(s) for a playlist.
- **Upload Custom Playlist Cover Image** (`PUT /playlists/{id}/images`) – Uploads a custom image for a playlist.

## See Also

- [February 2026 Migration Guide](https://developer.spotify.com/documentation/web-api/tutorials/february-2026-migration-guide) — Step-by-step migration instructions
- [Web API Documentation](https://developer.spotify.com/documentation/web-api)