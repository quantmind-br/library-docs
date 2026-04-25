---
title: Spotify | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-spotify
source: crawler
fetched_at: 2026-04-24T17:05:33.594631427-03:00
rendered_js: false
word_count: 707
summary: This document serves as a detailed reference guide for controlling Spotify via the Hermes Agent's skillset, outlining when to use the skill and providing specific instructions and examples for various actions like playback, searching, and playlist management.
tags:
    - spotify-control
    - music-api
    - playback-management
    - playlist-operations
    - media-reference
category: reference
---

Control Spotify — play music, search the catalog, manage playlists and library, inspect devices and playback state. Loads when the user asks to play/pause/queue music, search tracks/albums/artists, manage playlists, or check what's playing. Assumes the Hermes Spotify toolset is enabled and `hermes auth spotify` has been run.

SourceBundled (installed by default)Path`skills/media/spotify`Version`1.0.0`AuthorHermes AgentLicenseMITTags`spotify`, `music`, `playback`, `playlists`, `media`Related skills[`gif-search`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-gif-search)

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Spotify

Control the user's Spotify account via the Hermes Spotify toolset (7 tools). Setup guide: [https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify](https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify)

## When to use this skill[​](#when-to-use-this-skill "Direct link to When to use this skill")

The user says something like "play X", "pause", "skip", "queue up X", "what's playing", "search for X", "add to my X playlist", "make a playlist", "save this to my library", etc.

- `spotify_playback` — play, pause, next, previous, seek, set\_repeat, set\_shuffle, set\_volume, get\_state, get\_currently\_playing, recently\_played
- `spotify_devices` — list, transfer
- `spotify_queue` — get, add
- `spotify_search` — search the catalog
- `spotify_playlists` — list, get, create, add\_items, remove\_items, update\_details
- `spotify_albums` — get, tracks
- `spotify_library` — list/save/remove with `kind: "tracks"|"albums"`

Playback-mutating actions require Spotify Premium; search/library/playlist ops work on Free.

### "Play &lt;artist/track/album&gt;"[​](#play-artisttrackalbum 'Direct link to "Play <artist/track/album>"')

One search, then play by URI. Do NOT loop through search results describing them unless the user asked for options.

```text
spotify_search({"query": "miles davis kind of blue", "types": ["album"], "limit": 1})
→ got album URI spotify:album:1weenld61qoidwYuZ1GESA
spotify_playback({"action": "play", "context_uri": "spotify:album:1weenld61qoidwYuZ1GESA"})
```

For "play some &lt;artist&gt;" (no specific song), prefer `types: ["artist"]` and play the artist context URI — Spotify handles smart shuffle. If the user says "the song" or "that track", search `types: ["track"]` and pass `uris: [track_uri]` to play.

### "What's playing?" / "What am I listening to?"[​](#whats-playing--what-am-i-listening-to "Direct link to \"What's playing?\" / \"What am I listening to?\"")

Single call — don't chain get\_state after get\_currently\_playing.

```text
spotify_playback({"action": "get_currently_playing"})
```

If it returns 204/empty (`is_playing: false`), tell the user nothing is playing. Don't retry.

### "Pause" / "Skip" / "Volume 50"[​](#pause--skip--volume-50 'Direct link to "Pause" / "Skip" / "Volume 50"')

Direct action, no preflight inspection needed.

```text
spotify_playback({"action": "pause"})
spotify_playback({"action": "next"})
spotify_playback({"action": "set_volume", "volume_percent": 50})
```

### "Add to my &lt;playlist name&gt; playlist"[​](#add-to-my-playlist-name-playlist 'Direct link to "Add to my <playlist name> playlist"')

1. `spotify_playlists list` to find the playlist ID by name
2. Get the track URI (from currently playing, or search)
3. `spotify_playlists add_items` with the playlist\_id and URIs

```text
spotify_playlists({"action": "list"})
→ found "Late Night Jazz" = 37i9dQZF1DX4wta20PHgwo
spotify_playback({"action": "get_currently_playing"})
→ current track uri = spotify:track:0DiWol3AO6WpXZgp0goxAV
spotify_playlists({"action": "add_items",
                   "playlist_id": "37i9dQZF1DX4wta20PHgwo",
                   "uris": ["spotify:track:0DiWol3AO6WpXZgp0goxAV"]})
```

### "Create a playlist called X and add the last 3 songs I played"[​](#create-a-playlist-called-x-and-add-the-last-3-songs-i-played 'Direct link to "Create a playlist called X and add the last 3 songs I played"')

```text
spotify_playback({"action": "recently_played", "limit": 3})
spotify_playlists({"action": "create", "name": "Focus 2026"})
→ got playlist_id back in response
spotify_playlists({"action": "add_items", "playlist_id": <id>, "uris": [<3 uris>]})
```

### "Save / unsave / is this saved?"[​](#save--unsave--is-this-saved 'Direct link to "Save / unsave / is this saved?"')

Use `spotify_library` with the right `kind`.

```text
spotify_library({"kind": "tracks", "action": "save", "uris": ["spotify:track:..."]})
spotify_library({"kind": "albums", "action": "list", "limit": 50})
```

### "Transfer playback to my &lt;device&gt;"[​](#transfer-playback-to-my-device 'Direct link to "Transfer playback to my <device>"')

```text
spotify_devices({"action": "list"})
→ pick the device_id by matching name/type
spotify_devices({"action": "transfer", "device_id": "<id>", "play": true})
```

## Critical failure modes[​](#critical-failure-modes "Direct link to Critical failure modes")

**`403 Forbidden — No active device found`** on any playback action means Spotify isn't running anywhere. Tell the user: "Open Spotify on your phone/desktop/web player first, start any track for a second, then retry." Don't retry the tool call blindly — it will fail the same way. You can call `spotify_devices list` to confirm; an empty list means no active device.

**`403 Forbidden — Premium required`** means the user is on Free and tried to mutate playback. Don't retry; tell them this action needs Premium. Reads still work (search, playlists, library, get\_state).

**`204 No Content` on `get_currently_playing`** is NOT an error — it means nothing is playing. The tool returns `is_playing: false`. Just report that to the user.

**`429 Too Many Requests`** = rate limit. Wait and retry once. If it keeps happening, you're looping — stop.

**`401 Unauthorized` after a retry** — refresh token revoked. Tell the user to run `hermes auth spotify` again.

## URI and ID formats[​](#uri-and-id-formats "Direct link to URI and ID formats")

Spotify uses three interchangeable ID formats. The tools accept all three and normalize:

- URI: `spotify:track:0DiWol3AO6WpXZgp0goxAV` (preferred)
- URL: `https://open.spotify.com/track/0DiWol3AO6WpXZgp0goxAV`
- Bare ID: `0DiWol3AO6WpXZgp0goxAV`

When in doubt, use full URIs. Search results return URIs in the `uri` field — pass those directly.

Entity types: `track`, `album`, `artist`, `playlist`, `show`, `episode`. Use the right type for the action — `spotify_playback.play` with a `context_uri` expects album/playlist/artist; `uris` expects an array of track URIs.

## What NOT to do[​](#what-not-to-do "Direct link to What NOT to do")

- **Don't call `get_state` before every action.** Spotify accepts play/pause/skip without preflight. Only inspect state when the user asked "what's playing" or you need to reason about device/track.
- **Don't describe search results unless asked.** If the user said "play X", search, grab the top URI, play it. They'll hear it's wrong if it's wrong.
- **Don't retry on `403 Premium required` or `403 No active device`.** Those are permanent until user action.
- **Don't use `spotify_search` to find a playlist by name** — that searches the public Spotify catalog. User playlists come from `spotify_playlists list`.
- **Don't mix `kind: "tracks"` with album URIs** in `spotify_library` (or vice versa). The tool normalizes IDs but the API endpoint differs.