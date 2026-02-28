# Spotify Web API Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://developer.spotify.com/documentation/web-api |
| **Generated** | 2026-02-27 |
| **Total Documents** | 118 |
| **Categories** | 20 |

---

## Document Index

### 1. Overview & Introduction (001)

Introduction to the Spotify Web API and getting started guide.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-documentation-web-api.md` | Web API Overview | Introductory overview of Spotify Web API, app creation, authorization, and available features | spotify-web-api, developer-onboarding, app-credentials, music-streaming, api-integration |

---

### 2. Tutorials - Getting Started (002-010)

Step-by-step tutorials for authentication flows and migrations.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 002 | `002-documentation-web-api-tutorials-getting-started.md` | Getting Started | First Web API call tutorial: app registration, access token, artist metadata retrieval | spotify-api, web-api, authentication, client-credentials, curl, getting-started |
| 003 | `003-documentation-web-api-tutorials-client-credentials-flow.md` | Client Credentials Flow | Server-to-server authentication without user context | oauth, client-credentials, server-auth, access-token |
| 004 | `004-documentation-web-api-tutorials-code-flow.md` | Authorization Code Flow | Long-running apps with secure client secret storage | oauth, authorization-code, server-apps, user-authorization |
| 005 | `005-documentation-web-api-tutorials-code-pkce-flow.md` | Authorization Code with PKCE | Secure auth for mobile, desktop, and browser apps without client secret | oauth, pkce, mobile-auth, security, csrf-protection |
| 006 | `006-documentation-web-api-tutorials-implicit-flow.md` | Implicit Flow | Client-side token retrieval (deprecated, use PKCE instead) | oauth, implicit-grant, browser-apps, deprecated |
| 007 | `007-documentation-web-api-tutorials-refreshing-tokens.md` | Refreshing Tokens | How to refresh expired access tokens using refresh tokens | refresh-token, access-token, token-renewal, oauth |
| 008 | `008-documentation-web-api-tutorials-migration-implicit-auth-code.md` | Migrate Implicit to Auth Code | Migration guide from implicit flow to authorization code with PKCE | migration, implicit-flow, pkce, security-upgrade |
| 009 | `009-documentation-web-api-tutorials-migration-insecure-redirect-uri.md` | Migrate Insecure Redirect URI | Guide for updating redirect URIs to secure schemes | migration, redirect-uri, security, localhost |
| 010 | `010-documentation-web-api-tutorials-february-2026-migration-guide.md` | February 2026 Migration | Step-by-step migration for February 2026 API changes | migration, api-changes, deprecation, endpoints |

---

### 3. Concepts (011-020)

Core concepts and fundamentals for understanding the Web API.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 011 | `011-documentation-web-api-concepts-apps.md` | Apps | Creating and managing Spotify developer apps for API credentials | apps, client-id, client-secret, dashboard, credentials |
| 012 | `012-documentation-web-api-concepts-authorization.md` | Authorization | OAuth 2.0 implementation and choosing the right authorization flow | spotify-api, oauth-2-0, authorization-flows, access-tokens, pkce |
| 013 | `013-documentation-web-api-concepts-access-token.md` | Access Token | Using access tokens for API authorization and header format | access-token, api-authorization, bearer-token, authentication |
| 014 | `014-documentation-web-api-concepts-api-calls.md` | API Calls | Making requests and handling responses from the Web API | api-calls, requests, responses, http, endpoints |
| 015 | `015-documentation-web-api-concepts-scopes.md` | Scopes | Permission scopes for accessing specific user data and features | scopes, permissions, user-data, access-control |
| 016 | `016-documentation-web-api-concepts-spotify-uris-ids.md` | Spotify URIs & IDs | Understanding Spotify identifiers: URIs, IDs, and URLs | spotify-uri, spotify-id, identifiers, catalog |
| 017 | `017-documentation-web-api-concepts-playlists.md` | Playlists | Managing playlists: creation, modification, and track management | playlists, tracks, library, user-content |
| 018 | `018-documentation-web-api-concepts-rate-limits.md` | Rate Limits | Understanding API rate limiting and quota management | rate-limits, throttling, quota, retry |
| 019 | `019-documentation-web-api-concepts-quota-modes.md` | Quota Modes | Different quota modes and their impact on API usage | quota, rate-limiting, api-usage, tiers |
| 020 | `020-documentation-web-api-concepts-track-relinking.md` | Track Relinking | Handling track availability across different markets | track-relinking, markets, availability, streaming |

---

### 4. How-Tos (021)

Practical guides for implementing common use cases.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 021 | `021-documentation-web-api-howtos-web-app-profile.md` | Web App Profile | Build a web app to display user profile data using PKCE flow | spotify-web-api, pkce-auth, oauth2, typescript, javascript |

---

### 5. API Reference - Albums (022-025)

Endpoints for retrieving album information.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 022 | `022-documentation-web-api-reference-get-an-album.md` | Get Album | Retrieve detailed metadata for a single album | album, metadata, catalog |
| 023 | `023-documentation-web-api-reference-get-an-albums-tracks.md` | Get Album Tracks | Retrieve tracks contained in a specific album | album-tracks, track-list, catalog |
| 024 | `024-documentation-web-api-reference-get-multiple-albums.md` | Get Multiple Albums | Retrieve metadata for multiple albums at once | albums, batch, catalog |
| 025 | `025-documentation-web-api-reference-get-new-releases.md` | Get New Releases | List of new album releases featured in Spotify | new-releases, browse, albums |

---

### 6. API Reference - Artists (026-030)

Endpoints for retrieving artist information.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 026 | `026-documentation-web-api-reference-get-an-artist.md` | Get Artist | Retrieve detailed metadata for a single artist | artist, metadata, catalog |
| 027 | `027-documentation-web-api-reference-get-an-artists-albums.md` | Get Artist Albums | Retrieve albums released by a specific artist | artist-albums, discography, catalog |
| 028 | `028-documentation-web-api-reference-get-an-artists-top-tracks.md` | Get Artist Top Tracks | Get artist's top tracks by country | top-tracks, artist, country |
| 029 | `029-documentation-web-api-reference-get-an-artists-related-artists.md` | Get Related Artists | Get artists similar to a given artist | related-artists, recommendations, similar |
| 030 | `030-documentation-web-api-reference-get-multiple-artists.md` | Get Multiple Artists | Retrieve metadata for multiple artists at once | artists, batch, catalog |

---

### 7. API Reference - Audiobooks (031-037)

Endpoints for audiobook content management.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 031 | `031-documentation-web-api-reference-get-an-audiobook.md` | Get Audiobook | Retrieve metadata for a single audiobook | audiobook, metadata, catalog |
| 032 | `032-documentation-web-api-reference-get-audiobook-chapters.md` | Get Audiobook Chapters | Retrieve chapters belonging to an audiobook | audiobook-chapters, chapters, catalog |
| 033 | `033-documentation-web-api-reference-get-multiple-audiobooks.md` | Get Multiple Audiobooks | Retrieve metadata for multiple audiobooks | audiobooks, batch, catalog |
| 034 | `034-documentation-web-api-reference-get-users-saved-audiobooks.md` | Get Saved Audiobooks | Retrieve audiobooks saved in user's library | saved-audiobooks, library, user |
| 035 | `035-documentation-web-api-reference-save-audiobooks-user.md` | Save Audiobooks | Save audiobooks to user's library | save-audiobooks, library, user |
| 036 | `036-documentation-web-api-reference-remove-audiobooks-user.md` | Remove Audiobooks | Remove audiobooks from user's library | remove-audiobooks, library, user |
| 037 | `037-documentation-web-api-reference-check-users-saved-audiobooks.md` | Check Saved Audiobooks | Check if audiobooks are saved in user's library | check-saved, audiobooks, library |

---

### 8. API Reference - Chapters (038-039)

Endpoints for audiobook chapters.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 038 | `038-documentation-web-api-reference-get-a-chapter.md` | Get Chapter | Retrieve metadata for a single audiobook chapter | chapter, audiobook, metadata |
| 039 | `039-documentation-web-api-reference-get-several-chapters.md` | Get Several Chapters | Retrieve metadata for multiple chapters | chapters, batch, audiobook |

---

### 9. API Reference - Episodes (040-045)

Endpoints for podcast episodes.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 040 | `040-documentation-web-api-reference-get-an-episode.md` | Get Episode | Retrieve metadata for a single podcast episode | episode, podcast, metadata |
| 041 | `041-documentation-web-api-reference-get-multiple-episodes.md` | Get Multiple Episodes | Retrieve metadata for multiple episodes | episodes, batch, podcast |
| 042 | `042-documentation-web-api-reference-get-users-saved-episodes.md` | Get Saved Episodes | Retrieve episodes saved in user's library | saved-episodes, library, user |
| 043 | `043-documentation-web-api-reference-save-episodes-user.md` | Save Episodes | Save episodes to user's library | save-episodes, library, user |
| 044 | `044-documentation-web-api-reference-remove-episodes-user.md` | Remove Episodes | Remove episodes from user's library | remove-episodes, library, user |
| 045 | `045-documentation-web-api-reference-check-users-saved-episodes.md` | Check Saved Episodes | Check if episodes are saved in user's library | check-saved, episodes, library |

---

### 10. API Reference - Shows (046-052)

Endpoints for podcast shows.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 046 | `046-documentation-web-api-reference-get-a-show.md` | Get Show | Retrieve metadata for a single podcast show | show, podcast, metadata |
| 047 | `047-documentation-web-api-reference-get-a-shows-episodes.md` | Get Show Episodes | Retrieve episodes belonging to a show | show-episodes, podcast, catalog |
| 048 | `048-documentation-web-api-reference-get-multiple-shows.md` | Get Multiple Shows | Retrieve metadata for multiple shows | shows, batch, podcast |
| 049 | `049-documentation-web-api-reference-get-users-saved-shows.md` | Get Saved Shows | Retrieve shows saved in user's library | saved-shows, library, user |
| 050 | `050-documentation-web-api-reference-save-shows-user.md` | Save Shows | Save shows to user's library | save-shows, library, user |
| 051 | `051-documentation-web-api-reference-remove-shows-user.md` | Remove Shows | Remove shows from user's library | remove-shows, library, user |
| 052 | `052-documentation-web-api-reference-check-users-saved-shows.md` | Check Saved Shows | Check if shows are saved in user's library | check-saved, shows, library |

---

### 11. API Reference - Tracks (053-061)

Endpoints for track information and audio analysis.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 053 | `053-documentation-web-api-reference-get-track.md` | Get Track | Retrieve metadata for a single track | track, metadata, catalog |
| 054 | `054-documentation-web-api-reference-get-several-tracks.md` | Get Several Tracks | Retrieve metadata for multiple tracks | tracks, batch, catalog |
| 055 | `055-documentation-web-api-reference-get-audio-analysis.md` | Get Audio Analysis | Get detailed audio analysis for a track | audio-analysis, features, metadata |
| 056 | `056-documentation-web-api-reference-get-audio-features.md` | Get Audio Features | Get audio features for a track | audio-features, analysis, metadata |
| 057 | `057-documentation-web-api-reference-get-several-audio-features.md` | Get Several Audio Features | Get audio features for multiple tracks | audio-features, batch, analysis |
| 058 | `058-documentation-web-api-reference-get-users-saved-tracks.md` | Get Saved Tracks | Retrieve tracks saved in user's library | saved-tracks, library, user |
| 059 | `059-documentation-web-api-reference-save-tracks-user.md` | Save Tracks | Save tracks to user's library | save-tracks, library, user |
| 060 | `060-documentation-web-api-reference-remove-tracks-user.md` | Remove Tracks | Remove tracks from user's library | remove-tracks, library, user |
| 061 | `061-documentation-web-api-reference-check-users-saved-tracks.md` | Check Saved Tracks | Check if tracks are saved in user's library | check-saved, tracks, library |

---

### 12. API Reference - Albums Library (062-065)

Endpoints for managing saved albums.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 062 | `062-documentation-web-api-reference-get-users-saved-albums.md` | Get Saved Albums | Retrieve albums saved in user's library | saved-albums, library, user |
| 063 | `063-documentation-web-api-reference-save-albums-user.md` | Save Albums | Save albums to user's library | save-albums, library, user |
| 064 | `064-documentation-web-api-reference-remove-albums-user.md` | Remove Albums | Remove albums from user's library | remove-albums, library, user |
| 065 | `065-documentation-web-api-reference-check-users-saved-albums.md` | Check Saved Albums | Check if albums are saved in user's library | check-saved, albums, library |

---

### 13. API Reference - Library (066-069)

Endpoints for library management and personalization.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 066 | `066-documentation-web-api-reference-save-library-items.md` | Save Library Items | Save Spotify URIs to user's library | save-library, library, uris, user |
| 067 | `067-documentation-web-api-reference-remove-library-items.md` | Remove Library Items | Remove Spotify URIs from user's library | remove-library, library, uris, user |
| 068 | `068-documentation-web-api-reference-check-library-contains.md` | Check Library Contains | Check if items are saved in user's library | check-library, contains, library |
| 069 | `069-documentation-web-api-reference-get-users-top-artists-and-tracks.md` | Get User's Top Items | Get user's top artists or tracks over time | top-artists, top-tracks, personalization |

---

### 14. API Reference - Playlists (070-087)

Endpoints for playlist management.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 070 | `070-documentation-web-api-reference-get-playlist.md` | Get Playlist | Retrieve full details of a playlist | playlist, details, catalog |
| 071 | `071-documentation-web-api-reference-get-playlists-items.md` | Get Playlist Items | Get full details of playlist items | playlist-items, items, catalog |
| 072 | `072-documentation-web-api-reference-get-playlists-tracks.md` | Get Playlist Tracks | Retrieve tracks in a playlist (legacy) | playlist-tracks, tracks, legacy |
| 073 | `073-documentation-web-api-reference-get-playlist-cover.md` | Get Playlist Cover | Retrieve cover image for a playlist | playlist-cover, images, cover |
| 074 | `074-documentation-web-api-reference-create-playlist.md` | Create Playlist | Create a new playlist for current user | create-playlist, playlist, user |
| 075 | `075-documentation-web-api-reference-create-playlist-for-user.md` | Create Playlist for User | Create playlist for a user (deprecated) | create-playlist, deprecated, user |
| 076 | `076-documentation-web-api-reference-add-items-to-playlist.md` | Add Items to Playlist | Add items to a user's playlist | add-items, playlist, modify |
| 077 | `077-documentation-web-api-reference-add-tracks-to-playlist.md` | Add Tracks to Playlist | Add tracks to a playlist (legacy) | add-tracks, playlist, legacy |
| 078 | `078-documentation-web-api-reference-change-playlist-details.md` | Change Playlist Details | Update playlist name, description, visibility | playlist-details, modify, playlist |
| 079 | `079-documentation-web-api-reference-reorder-or-replace-playlists-items.md` | Reorder/Replace Items | Reorder or replace items in a playlist | reorder-items, replace-items, playlist |
| 080 | `080-documentation-web-api-reference-reorder-or-replace-playlists-tracks.md` | Reorder/Replace Tracks | Reorder or replace tracks (legacy) | reorder-tracks, legacy, playlist |
| 081 | `081-documentation-web-api-reference-remove-items-playlist.md` | Remove Playlist Items | Remove items from a playlist | remove-items, playlist, modify |
| 082 | `082-documentation-web-api-reference-remove-tracks-playlist.md` | Remove Tracks Playlist | Remove tracks from playlist (legacy) | remove-tracks, legacy, playlist |
| 083 | `083-documentation-web-api-reference-get-a-list-of-current-users-playlists.md` | Get Current User Playlists | Get playlists for authenticated user | user-playlists, current-user, library |
| 084 | `084-documentation-web-api-reference-get-list-users-playlists.md` | Get User Playlists | Get playlists for a user (deprecated) | user-playlists, deprecated, library |
| 085 | `085-documentation-web-api-reference-get-featured-playlists.md` | Get Featured Playlists | Get featured playlists on Spotify | featured-playlists, browse, discover |
| 086 | `086-documentation-web-api-reference-get-a-categories-playlists.md` | Get Category Playlists | Get playlists for a browse category | category-playlists, browse, discover |
| 087 | `087-documentation-web-api-reference-upload-custom-playlist-cover.md` | Upload Playlist Cover | Upload custom image for a playlist | playlist-cover, upload, image |

---

### 15. API Reference - Player/Playback (088-102)

Endpoints for controlling playback.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 088 | `088-documentation-web-api-reference-get-a-users-available-devices.md` | Get Available Devices | Retrieve devices available for playback | devices, playback, player |
| 089 | `089-documentation-web-api-reference-get-information-about-the-users-current-playback.md` | Get Playback State | Get current playback state information | playback-state, player, current |
| 090 | `090-documentation-web-api-reference-get-the-users-currently-playing-track.md` | Get Currently Playing | Get currently playing track info | currently-playing, track, player |
| 091 | `091-documentation-web-api-reference-get-queue.md` | Get Queue | Retrieve current playback queue | queue, playback, player |
| 092 | `092-documentation-web-api-reference-get-recently-played.md` | Get Recently Played | Get user's recently played tracks | recently-played, history, player |
| 093 | `093-documentation-web-api-reference-transfer-a-users-playback.md` | Transfer Playback | Transfer playback to a different device | transfer-playback, device, player |
| 094 | `094-documentation-web-api-reference-start-a-users-playback.md` | Start/Resume Playback | Start or resume playback | start-playback, resume, player |
| 095 | `095-documentation-web-api-reference-pause-a-users-playback.md` | Pause Playback | Pause current playback | pause-playback, player, control |
| 096 | `096-documentation-web-api-reference-skip-users-playback-to-next-track.md` | Skip to Next | Skip to next track in queue | skip-next, player, control |
| 097 | `097-documentation-web-api-reference-skip-users-playback-to-previous-track.md` | Skip to Previous | Skip to previous track | skip-previous, player, control |
| 098 | `098-documentation-web-api-reference-seek-to-position-in-currently-playing-track.md` | Seek to Position | Seek to position in current track | seek, position, player |
| 099 | `099-documentation-web-api-reference-set-repeat-mode-on-users-playback.md` | Set Repeat Mode | Set repeat mode for playback | repeat-mode, player, control |
| 100 | `100-documentation-web-api-reference-set-volume-for-users-playback.md` | Set Volume | Set playback volume | volume, player, control |
| 101 | `101-documentation-web-api-reference-toggle-shuffle-for-users-playback.md` | Toggle Shuffle | Toggle shuffle mode for playback | shuffle, player, control |
| 102 | `102-documentation-web-api-reference-add-to-queue.md` | Add to Queue | Add item to playback queue | add-queue, player, playback |

---

### 16. API Reference - Search & Browse (103-106)

Endpoints for searching and browsing content.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 103 | `103-documentation-web-api-reference-search.md` | Search | Search Spotify catalog for content | search, catalog, discover |
| 104 | `104-documentation-web-api-reference-get-categories.md` | Get Categories | Get list of browse categories | categories, browse, discover |
| 105 | `105-documentation-web-api-reference-get-a-category.md` | Get Category | Get single browse category | category, browse, discover |
| 106 | `106-documentation-web-api-reference-get-available-markets.md` | Get Available Markets | Get list of available markets | markets, countries, availability |

---

### 17. API Reference - Recommendations (107-108)

Endpoints for content recommendations.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 107 | `107-documentation-web-api-reference-get-recommendations.md` | Get Recommendations | Get recommendations based on seeds | recommendations, discover, seeds |
| 108 | `108-documentation-web-api-reference-get-recommendation-genres.md` | Get Recommendation Genres | Get available recommendation genres | genres, recommendations, seeds |

---

### 18. API Reference - User Profile (109-110)

Endpoints for user profile information.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 109 | `109-documentation-web-api-reference-get-current-users-profile.md` | Get Current User Profile | Get profile for authenticated user | user-profile, current-user, account |
| 110 | `110-documentation-web-api-reference-get-users-profile.md` | Get User Profile | Get public profile for a user (deprecated) | user-profile, public, deprecated |

---

### 19. API Reference - Follow (111-117)

Endpoints for following artists and playlists.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 111 | `111-documentation-web-api-reference-get-followed.md` | Get Followed Artists | Get artists followed by current user | followed-artists, following, user |
| 112 | `112-documentation-web-api-reference-follow-artists-users.md` | Follow Artists/Users | Follow artists or users | follow, artists, users |
| 113 | `113-documentation-web-api-reference-unfollow-artists-users.md` | Unfollow Artists/Users | Unfollow artists or users | unfollow, artists, users |
| 114 | `114-documentation-web-api-reference-follow-playlist.md` | Follow Playlist | Follow a playlist | follow-playlist, playlist |
| 115 | `115-documentation-web-api-reference-unfollow-playlist.md` | Unfollow Playlist | Unfollow a playlist | unfollow-playlist, playlist |
| 116 | `116-documentation-web-api-reference-check-current-user-follows.md` | Check User Follows | Check if current user follows artists/users | check-follows, following, artists |
| 117 | `117-documentation-web-api-reference-check-if-user-follows-playlist.md` | Check Playlist Follows | Check if user follows a playlist | check-follows, playlist, following |

---

### 20. Changelog (118)

API changes and deprecation notices.

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 118 | `118-documentation-web-api-references-changes-february-2026.md` | February 2026 Changes | Significant API changes, removed/added/modified endpoints | spotify-api, api-changes, deprecation-notice, migration-guide |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Authentication & OAuth** | 002-010, 012-013, 015 |
| **Core Concepts** | 011-020 |
| **Albums** | 022-025, 062-065 |
| **Artists** | 026-030 |
| **Audiobooks** | 031-039 |
| **Podcasts (Shows/Episodes)** | 040-052 |
| **Tracks** | 053-061 |
| **Playlists** | 070-087 |
| **Playback Control** | 088-102 |
| **Search & Browse** | 103-108 |
| **User Profile & Library** | 109-117 |
| **API Changes** | 118 |

### By HTTP Method

| Method | Typical File Numbers |
|--------|---------------------|
| **GET** | 022-057, 062, 069, 070-073, 083-092, 103-117 |
| **POST** | 074-077, 096, 102 |
| **PUT** | 063, 066, 078-080, 093-101 |
| **DELETE** | 064, 067, 081-082, 113, 115 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read **001** for Web API overview
- Complete **002** for your first API call
- Learn concepts from **011-020**

### Level 2: Authentication
- Study **012** for OAuth overview
- Choose your flow: **003** (server), **004** (long-running), or **005** (mobile/browser)
- Learn token refresh: **007**

### Level 3: Core API Usage
- Understand scopes (**015**) and URIs (**016**)
- Read about rate limits (**018**) and API calls (**014**)

### Level 4: Content Access
- Albums: **022-025**
- Artists: **026-030**
- Tracks: **053-061**
- Search: **103**

### Level 5: User Features
- Playlists: **070-087**
- Playback control: **088-102**
- User profile: **109-110**
- Library management: **062-069**

### Level 6: Migration & Updates
- Review **118** for latest API changes
- Follow **010** for migration steps

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression.*
