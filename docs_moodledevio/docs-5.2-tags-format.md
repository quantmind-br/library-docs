---
title: 2 docs tagged with "Format" | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/tags/format
source: sitemap
fetched_at: 2026-02-17T15:40:05.527294-03:00
rendered_js: false
word_count: 76
summary: This document explains Moodle course format plugins and provides guidance on migrating 3.11 formats to the updated course editor logic introduced in Moodle 4.0.
tags:
    - moodle-development
    - course-formats
    - plugin-migration
    - moodle-4-0
    - web-services
category: guide
---

## [Course format](https://moodledev.io/docs/5.2/apis/plugintypes/format)

Course formats are plugins that determine the layout of course resources.

## [Migrating 3.11 formats](https://moodledev.io/docs/5.2/apis/plugintypes/format/migration)

The new course editor introduced in Moodle 4.0 reimplements most of the previous webservices, AMD modules, and internal logic of the course rendering. However, all formats since 3.11 will use the previous libraries by default until its final deprecation in Moodle 4.3. This document collects the main adaptations any 3.11 course format will require to continue working when this happens.