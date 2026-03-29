---
title: Online Wallpapers | Pyprland web
url: https://hyprland-community.github.io/pyprland/wallpapers/online
source: github_pages
fetched_at: 2026-01-31T15:58:29.196411178-03:00
rendered_js: true
word_count: 70
summary: This document describes configuration options for managing online image fetching and caching behavior, including parameters for controlling online ratio, backend selection, keyword filtering, and cache management.
tags:
    - configuration
    - image-fetching
    - caching
    - online-content
    - parameters
category: reference
---

OptionDescription[`online_ratio`i](#config-online-ratio "More details below")float

=`0`

Probability of fetching online (0.0-1.0)[`online_backends`i](#config-online-backends "More details below")list

=`["unsplash","picsum","wallhaven","reddit"]`

Enabled online backends[`online_keywords`i](#config-online-keywords "More details below")listKeywords to filter online images[`online_folder`i](#config-online-folder "More details below")str

=`"online"`

Subfolder for downloaded online images

### `online_ratio` float=`0` [​](#config-online-ratio)

### `online_backends` list=`["unsplash","picsum","wallhaven","reddit"]` [​](#config-online-backends)

### `online_keywords` list [​](#config-online-keywords)

### `online_folder` str=`"online"` [​](#config-online-folder)

OptionDescription[`cache_days`i](#config-cache-days "More details below")int

=`0`

Days to keep cached images (0 = forever)[`cache_max_mb`i](#config-cache-max-mb "More details below")int

=`100`

Maximum cache size in MB (0 = unlimited)[`cache_max_images`i](#config-cache-max-images "More details below")int

=`0`

Maximum number of cached images (0 = unlimited)

### `cache_days` int=`0` [​](#config-cache-days)

### `cache_max_mb` int=`100` [​](#config-cache-max-mb)

### `cache_max_images` int=`0` [​](#config-cache-max-images)