---
title: 2 docs tagged with "Format" | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/tags/format
source: sitemap
fetched_at: 2026-02-17T15:19:03.760449-03:00
rendered_js: false
word_count: 76
summary: This document defines Moodle course format plugins and outlines the necessary adaptations required to migrate course formats from version 3.11 to the updated course editor introduced in Moodle 4.0.
tags:
    - moodle
    - course-format
    - plugin-development
    - migration-guide
    - moodle-api
category: guide
---

## [Course format](https://moodledev.io/docs/5.0/apis/plugintypes/format)

Course formats are plugins that determine the layout of course resources.

## [Migrating 3.11 formats](https://moodledev.io/docs/5.0/apis/plugintypes/format/migration)

The new course editor introduced in Moodle 4.0 reimplements most of the previous webservices, AMD modules, and internal logic of the course rendering. However, all formats since 3.11 will use the previous libraries by default until its final deprecation in Moodle 4.3. This document collects the main adaptations any 3.11 course format will require to continue working when this happens.