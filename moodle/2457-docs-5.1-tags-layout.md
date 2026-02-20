---
title: One doc tagged with "Layout" | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/tags/layout
source: sitemap
fetched_at: 2026-02-17T15:31:32.966442-03:00
rendered_js: false
word_count: 71
summary: This document explains the requirements for defining and overriding page layouts within Moodle themes, covering both fresh theme development and theme inheritance.
tags:
    - moodle-development
    - theme-engine
    - page-layouts
    - plugin-types
    - web-design
category: concept
---

## [Layout](https://moodledev.io/docs/5.1/apis/plugintypes/theme/layout)

All themes are required to define the layouts they wish to be responsible for as well as create; however, many layout files are required by those layouts. If the theme is overriding another theme then it is a case of deciding which layouts this new theme should override. If the theme is a completely fresh start then you will need to define a layout for each of the different possibilities.