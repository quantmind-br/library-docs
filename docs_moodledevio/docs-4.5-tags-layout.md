---
title: One doc tagged with "Layout" | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/tags/layout
source: sitemap
fetched_at: 2026-02-17T15:08:32.609676-03:00
rendered_js: false
word_count: 71
summary: This document explains the requirements for defining and managing layout files within Moodle theme plugins, including how to handle overrides and new theme structures.
tags:
    - moodle-development
    - theme-design
    - layout-files
    - plugin-types
    - user-interface
category: concept
---

## [Layout](https://moodledev.io/docs/4.5/apis/plugintypes/theme/layout)

All themes are required to define the layouts they wish to be responsible for as well as create; however, many layout files are required by those layouts. If the theme is overriding another theme then it is a case of deciding which layouts this new theme should override. If the theme is a completely fresh start then you will need to define a layout for each of the different possibilities.