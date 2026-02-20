---
title: One doc tagged with "Layout" | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/tags/layout
source: sitemap
fetched_at: 2026-02-17T15:40:41.427777-03:00
rendered_js: false
word_count: 71
summary: This document outlines the requirements for Moodle themes to define their own layout files and explains the process for overriding layouts from parent themes.
tags:
    - moodle-development
    - theme-layout
    - plugin-types
    - web-design
    - moodle-api
category: guide
---

## [Layout](https://moodledev.io/docs/5.2/apis/plugintypes/theme/layout)

All themes are required to define the layouts they wish to be responsible for as well as create; however, many layout files are required by those layouts. If the theme is overriding another theme then it is a case of deciding which layouts this new theme should override. If the theme is a completely fresh start then you will need to define a layout for each of the different possibilities.