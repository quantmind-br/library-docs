---
title: 5 docs tagged with "Theme" | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/tags/theme
source: sitemap
fetched_at: 2026-02-17T15:01:23.74858-03:00
rendered_js: false
word_count: 208
summary: This document provides an overview of the core components of Moodle theme development, including font customization, image overrides, layout definitions, and CSS style management.
tags:
    - moodle
    - theme-development
    - css
    - layout-management
    - plugin-architecture
    - web-design
category: guide
---

## [Fonts](https://moodledev.io/docs/4.4/apis/plugintypes/theme/fonts)

CSS3 standard introduced the possibility to specify custom fonts, see CSS web fonts tutorial.

## [Images and icons in themes](https://moodledev.io/docs/4.4/apis/plugintypes/theme/images)

One of the theme features is the ability to override any of the standard images within Moodle when your theme is in use. At this point, let's explore how to utilize your own images within your theme and how to override the images being used by Moodle.

## [Layout](https://moodledev.io/docs/4.4/apis/plugintypes/theme/layout)

All themes are required to define the layouts they wish to be responsible for as well as create; however, many layout files are required by those layouts. If the theme is overriding another theme then it is a case of deciding which layouts this new theme should override. If the theme is a completely fresh start then you will need to define a layout for each of the different possibilities.

## [Styles](https://moodledev.io/docs/4.4/apis/plugintypes/theme/styles)

Let's begin by exploring the various locations within Moodle from which CSS can be included:

## [Theme plugins](https://moodledev.io/docs/4.4/apis/plugintypes/theme)

A Moodle theme allows users to customize the appearance and functionality of their Moodle site, from overall design to specific activities. Users can create their own themes or modify existing ones, leveraging CSS and JavaScript for customization. The theme architecture ensures smooth fallbacks for minimal changes, fostering flexibility and ease of use.