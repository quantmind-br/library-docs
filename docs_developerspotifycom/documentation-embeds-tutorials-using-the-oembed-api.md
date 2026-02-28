---
title: Using the oEmbed API | Spotify for Developers
url: https://developer.spotify.com/documentation/embeds/tutorials/using-the-oembed-api
source: crawler
fetched_at: 2026-02-27T23:40:22.954731-03:00
rendered_js: true
word_count: 271
summary: This document explains how to use Spotify's oEmbed API to discover and retrieve metadata for Spotify URLs, enabling link previews and embedded content in third-party applications.
tags:
    - spotify-api
    - oembed
    - content-embedding
    - link-unfurling
    - metadata
    - web-integration
category: api
---

## Overview

[oEmbed](https://oembed.com/) is an API that allows third-party websites and apps to fetch and display basic information about a Spotify URL and [Embeds](https://developer.spotify.com/documentation/embeds/tutorials/creating-an-embed). It commonly powers link previews, or link 'unfurling' functionality on websites with messaging and user-created posts.

## Discovering oEmbed URIs

### Detecting the &lt;link&gt; element

Most pages on [open.spotify.com](https://open.spotify.com), or the short link version ([https://spotify.link](https://spotify.link)), support oEmbed. If your application parses a Spotify web page then it can discover the corresponding oEmbed URI by searching the document for a `<link>` element with the type set to `application/json+oembed`. For example, the source of [the NerdOut@Spotify podcast](https://open.spotify.com/show/5eXZwvvxt3K2dxha3BSaAe) includes this HTML:

`1`

`<link rel="alternate" type="application/json+oembed" href="https://open.spotify.com/oembed?url=https%3A%2F%2Fopen.spotify.com%2Fshow%2F5eXZwvvxt3K2dxha3BSaAe" />`

## Using oEmbed data from Spotify in your app

The oEmbed response is a JSON object that contains the title of the entity, an Embed code snippet, and (if available) a thumbnail image associated with the entity. You can find a sample oEmbed response below, or learn more about the oEmbed response properties through the [oEmbed API reference documentation](https://developer.spotify.com/documentation/embeds/reference/oembed).

`1`

`{`

`2`

`"html": "<iframe width=\"100%\" height=\"152\" title=\"Spotify Embed: My Path to Spotify: Women in Engineering \" style=\"border-radius: 12px\" frameborder=\"0\" allowfullscreen allow=\"autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture\" src=\"https://open.spotify.com/embed/episode/7makk4oTQel546B0PZlDM5?utm_source=oembed\"></iframe>\n",`

`3`

`"width": 456,`

`4`

`"height": 152,`

`5`

`"version": "1.0",`

`6`

`"provider_name": "Spotify",`

`7`

`"provider_url": "https://spotify.com",`

`8`

`"type": "rich",`

`9`

`"title": "My Path to Spotify: Women in Engineering",`

`10`

`"thumbnail_url": "https://i.scdn.co/image/ab67656300005f1ff8141e891abf749375772343",`

`11`

`"thumbnail_width": 300,`

`12`

`"thumbnail_height": 300`

`13`

`}`

### Use cases

Common use cases for oEmbed include:

- Displaying the title of a Spotify link in an app or website
- Displaying the title and preview image of a Spotify link in an app or website
- Displaying an [Embed](https://developer.spotify.com/documentation/embeds/tutorials/creating-an-embed) in your app or website