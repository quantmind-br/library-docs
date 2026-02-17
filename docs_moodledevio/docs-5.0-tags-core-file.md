---
title: 2 docs tagged with "core_file" | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/tags/core-file
source: sitemap
fetched_at: 2026-02-17T15:17:36.209188-03:00
rendered_js: false
word_count: 69
summary: This document explains the purpose and implementation of file converters, which allow Moodle plugins to transform files into different formats via the File conversion API.
tags:
    - moodle-development
    - file-conversion
    - plugin-api
    - file-converter
    - api-integration
category: api
---

## [File Converters](https://moodledev.io/docs/5.0/apis/plugintypes/fileconverter)

File converters are an important tool to support other plugins with file conversion supported between a wide range of file formats. File converters are accessed using the File conversion API and are typically consumed by other plugins rather than by the user directly.

## [File Converters](https://moodledev.io/docs/5.0/apis/subsystems/files/converter)

Users are able to submit a wide range of files, and it is a common requirement to convert these to alternative formats.