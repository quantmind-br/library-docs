---
title: oEmbed API | Spotify for Developers
url: https://developer.spotify.com/documentation/embeds/reference/oembed
source: crawler
fetched_at: 2026-02-27T23:40:20.204741-03:00
rendered_js: true
word_count: 129
summary: This document specifies the request and response format for the Spotify oEmbed API, which allows developers to retrieve embeddable HTML and metadata for Spotify content.
tags:
    - spotify-api
    - oembed
    - web-embeds
    - api-reference
    - media-integration
category: api
---

Embeds •References / oEmbed API

## Request

- The URL-encoded URL of a Spotify podcast show, episode, artist, album or track
  
  Example: `url=https%3A%2F%2Fopen.spotify.com%2Fepisode%2F7makk4oTQel546B0PZlDM5`

## Response

A response containing oEmbed data

- HTML of an Embed for this item
  
  Example: `"<iframe width=\"100%\" height=\"152\" title=\"Spotify Embed: My Path to Spotify: Women in Engineering \" style=\"border-radius: 12px\" frameborder=\"0\" allowfullscreen allow=\"autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture\" src=\"https://open.spotify.com/embed/episode/7makk4oTQel546B0PZlDM5?utm_source=oembed\"></iframe>"`
- Width in pixels of the Embed
  
  Example: `456`
- Height in pixels of the Embed
  
  Example: `152`
- Provider name for the oEmbed
  
  Allowed values: `"Spotify"`Example: `"Spotify"`
- Allowed values: `"https://spotify.com"`Example: `"https://spotify.com"`
- Allowed values: `"rich"`Example: `"rich"`
- Example: `"My Path to Spotify: Women in Engineering"`
- URL of a thumbnail image for the item
  
  Example: `"https://i.scdn.co/image/ab67656300005f1ff8141e891abf749375772343"`
- Width of the thumbnail image
  
  Minimum value: `0`Example: `300`
- Height of the thumbnail image
  
  Minimum value: `0`Example: `300`

## Response sample

```
{"html": "<iframe width=\"100%\" height=\"152\" title=\"Spotify Embed: My Path to Spotify: Women in Engineering \" style=\"border-radius: 12px\" frameborder=\"0\" allowfullscreen allow=\"autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture\" src=\"https://open.spotify.com/embed/episode/7makk4oTQel546B0PZlDM5?utm_source=oembed\"></iframe>","width": 456,"height": 152,"version": "1.0","provider_name": "Spotify","provider_url": "https://spotify.com","type": "rich","title": "My Path to Spotify: Women in Engineering","thumbnail_url": "https://i.scdn.co/image/ab67656300005f1ff8141e891abf749375772343","thumbnail_width": 300,"thumbnail_height": 300}
```