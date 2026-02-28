---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-audio-features
source: crawler
fetched_at: 2026-02-27T23:46:59.538734-03:00
rendered_js: false
word_count: 664
summary: This document provides the specification for the Spotify Web API endpoint that retrieves audio feature data, such as danceability and energy, for a single track.
tags:
    - spotify-api
    - audio-features
    - web-api
    - track-metadata
    - music-analysis
category: api
---

Web API •References / Tracks / Get Track's Audio Features

## Get Track's Audio Features

Deprecated

Get audio feature information for a single track identified by its unique Spotify ID.

## Request

- Example: `11dFghVXANMlKmJXsNCbNl`

## Response

Audio features for one track

- acousticnessnumber \[float]
  
  A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
  
  Range: `0` - `1`Example: `0.00242`
- A URL to access the full audio analysis of this track. An access token is required to access this data.
  
  Example: `"https://api.spotify.com/v1/audio-analysis/2takcwOaAZWiXQijPHIx7B"`
- danceabilitynumber \[float]
  
  Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
  
  Example: `0.585`
- The duration of the track in milliseconds.
  
  Example: `237040`
- Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
  
  Example: `0.842`
- The Spotify ID for the track.
  
  Example: `"2takcwOaAZWiXQijPHIx7B"`
- instrumentalnessnumber \[float]
  
  Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
  
  Example: `0.00686`
- The key the track is in. Integers map to pitches using standard [Pitch Class notation](https://en.wikipedia.org/wiki/Pitch_class). E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
  
  Range: `-1` - `11`Example: `9`
- Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
  
  Example: `0.0866`
- The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
  
  Example: `-5.883`
- Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
  
  Example: `0`
- speechinessnumber \[float]
  
  Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
  
  Example: `0.0556`
- The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
  
  Example: `118.211`
- An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4".
  
  Range: `3` - `7`Example: `4`
- A link to the Web API endpoint providing full details of the track.
  
  Example: `"https://api.spotify.com/v1/tracks/2takcwOaAZWiXQijPHIx7B"`
- Allowed values: `"audio_features"`
- The Spotify URI for the track.
  
  Example: `"spotify:track:2takcwOaAZWiXQijPHIx7B"`
- A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
  
  Range: `0` - `1`Example: `0.428`

## Response sample

```
{"acousticness": 0.00242,"analysis_url": "https://api.spotify.com/v1/audio-analysis/2takcwOaAZWiXQijPHIx7B","danceability": 0.585,"duration_ms": 237040,"energy": 0.842,"id": "2takcwOaAZWiXQijPHIx7B","instrumentalness": 0.00686,"key": 9,"liveness": 0.0866,"loudness": -5.883,"mode": 0,"speechiness": 0.0556,"tempo": 118.211,"time_signature": 4,"track_href": "https://api.spotify.com/v1/tracks/2takcwOaAZWiXQijPHIx7B","type": "audio_features","uri": "spotify:track:2takcwOaAZWiXQijPHIx7B","valence": 0.428}
```